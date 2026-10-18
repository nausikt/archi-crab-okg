# dmwm/CRABServer issue #8354: add a per-user policy to tape recall

State: closed
Opened: 2024-04-24T17:13:20Z
Closed: 2024-07-16T16:25:48Z
Labels: Type: Enhancement, Priority: High, Status: In Progress, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/8354

## Opening post (belforte, 2024-04-24T17:13:20Z)

last week two users managed to put tape recall requests for a total of about 7PB

We can't deliver that "timely" nor can they process all that data. Clearly they do not know what they are doing.

We want to put a limit  on how much each individual user can request at any given time, i.e. until all of her/his previous requests are satisfied.

We had an initial discussion in DM Ops MatterMost, moving here to converge on a concrete proposal and implement it.

@dynamic-entropy

## Comment (belforte, 2024-04-24T20:28:29Z)

Rahul, currently each rule that we create has a comment like this
```
Comment:                    Recall 605 GBytes for user: sleontsi dataset: /Charmonium/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD
```
Format is fixed becasue we use it for our monitoring

I am open to change to (or add as) a rule metadata.

I think that what we need is a small database of how much a given user has already in recall in order to make a decision whether to accept a request or not.

Can you summarize how you do this for automatic recall ?

## Comment (dynamic-entropy, 2024-05-03T17:55:20Z)

Hello, Stefano
I saw your mail. Did they just repeat the jobs that triggered the recalls?
Does this need to be taken urgently? I wanted to do some tests on my own to pitch a concrete proposal before saying anything, hence the delay.

## Comment (belforte, 2024-05-03T18:36:58Z)

Simply I had not done anything until now. I think he will be careful. But we do not want to continuously watch things.

## Comment (belforte, 2024-05-10T14:36:48Z)

On Hold, waiting for a proposal from @dynamic-entropy on how to track usage by user.
As a reminder currently limits to each request are applied here
https://github.com/dmwm/CRABServer/blob/5ca7cae6d4ebe374f945eb46a7768a64c2b24fa2/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L474

And currently those are in English:
* tiers in `['AOD', 'AODSIM', 'MINIAOD', 'MINIAODSIM', 'NANOAOD', 'NANOAODSIM']` are recalled no matter how big
* other data tiers are recalled if recall request is <50TB
   * users can indicate a list of blocks which fits if dataset is too big

Beyond that the old plan was to have a global quota cap on `crab_tape_recall` account. Couple of years ago Nick told me that this cap was there but for technical reasons was not implemented in Rucio. I do not know any details on that.

## Comment (belforte, 2024-05-15T14:18:05Z)

Stefano and Rahul had a chat. Proposal:

* tape recall rules will be created with `account=username` and `activity="Analysis Tape Recall"`  and `askApproval=True`
* Rahul will make RUcio accept that activity.
* Rahul will make sure that only `crab_tape_recall` account  can create rules in this activity and they will be automatically approved. This will avoid that the rule is charged to the user  Rucio quota on the selected RSE
* CRAB will ask Rucio for all rule belonging to the user wich this activity and compute the overall size (Rahul has code example to do it https://github.com/dmwm/CMSRucio/blob/5469bb52226ce9cde59eb7b538fcb96cde386a1f/src/policy/CMSRucioPolicy/permission.py#L179-L186 )
* CRAB will then apply the limit and communicate to user accordingly
* per-user-limit will be set in coordination with Comp.Ops. We can start with 200TB total

we prefer to do the check in CRAB code because Rucio does not have a way (yet) to communicate to the user what the usage is etc. Only a yes/no.

If computing the total size for a user takes too long, we will reconsider

## Comment (belforte, 2024-05-16T09:33:25Z)

implementation tasks in https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/RucioActions.py
- [x]  add the quota check in DBSDataDiscovery/executeTapeRecallPolicy ?
- [x] add user limit in ServerUtilities with all other constants ? Or in TW config like e.g. `maxTierToBlockRecallSize` ? i.e. in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L107-108
- [x] pass `activity` as arguments to `createOrReuseRucioRule` . Account can be selected inside there since `self.username` is available
- [x] make sure that rule is removed once data is recalled so that user regains their quota. Modify TapeRecall recurring action. Now data will be locked as soon as task is submitted, letting rule to expire in 1h is fine.

## Comment (belforte, 2024-05-20T16:01:20Z)

@dynamic-entropy 
a first implementation is ready in https://github.com/belforte/CRABServer/tree/add-user-policy-to-tape-recall-8354

currently it uses `crab_tape_recall` account and `Analysis Input` activity with `AskForApproval=False`. Waiting for `Analysis Tape Recall` activity to be accepted by Rucio with automatic approval. So that I can verify that nothing is broken.

if you care to have a look, relevant code changes are below. Any comment is always welcome

https://github.com/belforte/CRABServer/blob/72c66a157e1263637108afa0ac5fbfcf5467cf06/src/python/RucioUtils.py#L98-L120

https://github.com/belforte/CRABServer/blob/72c66a157e1263637108afa0ac5fbfcf5467cf06/src/python/TaskWorker/Actions/RucioActions.py#L62-L85

https://github.com/belforte/CRABServer/blob/72c66a157e1263637108afa0ac5fbfcf5467cf06/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L529-L550

## Comment (belforte, 2024-05-22T10:52:20Z)

on hold. wating for at least the new activity to be allowed on Rucio side.
@dynamic-entropy I think that's safe enough that you can put it in production w/o me testing on integration, right ?

Then we can put in production and test still using account `crab_tape_recall` and `askforapproval=False` and switch those once code is tested and the permission part in Rucio is also true.

## Comment (dynamic-entropy, 2024-05-22T12:24:03Z)

Hello Stefano
I have created a PR to add the activity to the schema as well as check for the crab_tape_recall account, after which the rule shall created. 
The `approve` part will need yet another PR. But now you can create rules without askApproval.
https://github.com/dmwm/CMSRucio/pull/802

## Comment (belforte, 2024-05-22T12:27:36Z)

thank you Rahul. Kindly let me know when it is deployed so I can try it and verify that I correctly compute the used quota

## Comment (dynamic-entropy, 2024-05-22T12:38:38Z)

Sure, I have added commits for `auto-approve` too. I will let you know when it's deployed. 
Cheers

## Comment (dynamic-entropy, 2024-06-19T16:07:36Z)

Hello @belforte 
It's in production now. Apologies, for the delay.
Kindly test if everything is okay and let me know if more things need plumbing.
Cheers

## Comment (belforte, 2024-06-19T16:09:46Z)

many thanks @dynamic-entropy 
I am awfully busy atm with VOMS-to-IAM transition and removing deprecated HTCondor calls from CRAB.
But this is top of the list after that.
Hopefully sometimes next week.

## Comment (belforte, 2024-06-28T14:27:14Z)

Hi @dynamic-entropy 
I finally got to test and have stumbled on a permission issue with this code
https://github.com/belforte/CRABServer/blob/1b400d1d3a739024960c2c0980e349b53d66d28f/src/python/TaskWorker/Actions/RucioActions.py#L79-L84
```python
            ruleIds = self.rucioClient.add_replication_rule(  # N.B. returns a list
                dids=[did], copies=copies, rse_expression=rseExpression,
                grouping=grouping, weight=weight, lifetime=lifetime,
                account=account, activity=activity,
                comment=comment,
                ask_approval=askApproval, asynchronous=True)
```
it appears that no matter what I put as `account`, Rucio will try to create the use using the user of the current client and I get 
```text
Rucio exception creating rule: Access to the requested resource denied.
Details: Account crab_tape_recall can not add replication rule
```
I have `askApprova=True` and `activity="Analysis TapeRecall"`

Any idea ? Your PR has the same `crab_tape_recall ` username so it does not look a simple typo.

## Comment (belforte, 2024-06-28T14:30:03Z)

maybe scope matters ?
This is a test where I have  this did  `'{scope': 'user.crab_tape_recall', 'name': '/TapeRecall/pippo1/USER'}`

## Comment (dynamic-entropy, 2024-07-01T10:51:06Z)

Hello @belforte 

I am unable to reproduce this. 
```
rucio add-rule user.crab_tape_recall:/TapeRecall/pippo1/USER 1 T2_RC_MOCK --lifetime 86400 --activity "Analysis TapeRecall" --ask-approval --account rchauhan 

d135f23c65764f9f9bf0b5a3600ecae3
```

https://cms-rucio-webui.cern.ch/rule?rule_id=d135f23c65764f9f9bf0b5a3600ecae3#locks

Can you please provide me with the values of those variables in the test?

## Comment (belforte, 2024-07-01T17:02:39Z)

thanks Rahul. I am holiday this week, but will do more tests (with more details) ASAP

## Comment (belforte, 2024-07-01T17:03:38Z)

from which Rucio account did you issue the `rucio add-rule` ?

## Comment (dynamic-entropy, 2024-07-01T17:09:53Z)

```
rucio whoami | grep account
account    : crab_tape_recall
```

## Comment (dynamic-entropy, 2024-07-01T17:11:12Z)

Just created another rule: https://cms-rucio-webui.cern.ch/rule?rule_id=7e35f6942243492c890633034dcd47ec

## Comment (belforte, 2024-07-02T08:37:13Z)

thanks will investigate ASAP what was happening in my code

## Comment (belforte, 2024-07-03T15:40:31Z)

@dynamic-entropy how could your command in https://github.com/dmwm/CRABServer/issues/8354#issuecomment-2199829697 work w/o number of copies and RSE expression ?

## Comment (belforte, 2024-07-03T15:45:56Z)

this worked for me as well from CLI
```
belforte@lxplus806/Rucio> rucio add-rule $did  --activity "Analysis TapeRecall" --ask-approval --account belforte 1 T1_FR_CCIN2P3_Disk
0e615779a04940199cd7e9f218243b04
belforte@lxplus806/Rucio> rucio whoami
status     : ACTIVE
deleted_at : None
updated_at : 2020-10-15T20:57:44
suspended_at : None
account    : crab_tape_recall
account_type : SERVICE
email      : stefano.belforte@cern.ch
created_at : 2020-10-15T20:57:44
belforte@lxplus806/Rucio> rucio list-content $did
+------------------------------------------------------------------+--------------+
| SCOPE:NAME                                                       | [DID TYPE]   |
|------------------------------------------------------------------+--------------|
| cms:/MuonEG/Run2016B-v1/RAW#86bc5e3e-1519-11e6-a3f4-001e67ac06a0 | DATASET      |
+------------------------------------------------------------------+--------------+
belforte@lxplus806/Rucio> echo $did
user.crab_tape_recall:/TapeRecall/testtask-1720020665/USER
belforte@lxplus806/Rucio> 
```

I will try to find what is different when doing it in python

## Comment (dynamic-entropy, 2024-07-03T15:53:41Z)

> how could your command in [#8354 (comment)](https://github.com/dmwm/CRABServer/issues/8354#issuecomment-2199829697) work w/o number of copies and RSE expression ?

Hello @belforte , 
I do specify those
```
rucio add-rule user.crab_tape_recall:/TapeRecall/pippo1/USER 1 T2_RC_MOCK [NAMES ARGUMENTS]
```

You created the rule for `FR_CCIN2P3` this will trigger transfers. 
Its okay if you also wanted this to be the case. However, for testing you can use the `T2_RC_MOCK` rse. this does not have any protocols specified.

## Comment (belforte, 2024-07-03T15:55:11Z)

thanks for the tip about MOCK. I will cleanup

## Comment (belforte, 2024-07-03T16:24:32Z)

when trying a minimal python, I get a new error, w/o any useful detail :-(
```
belforte@lxplus806/Rucio> python3
Python 3.6.8 (default, Apr 25 2024, 09:54:46) 
[GCC 8.5.0 20210514 (Red Hat 8.5.0-22)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from rucio.client import Client
>>> rucio=Client(account='crab_tape_recall')
>>> rucio.whoami()
{'status': 'ACTIVE', 'deleted_at': None, 'updated_at': '2020-10-15T20:57:44', 'suspended_at': None, 'account': 'crab_tape_recall', 'email': 'stefano.belforte@cern.ch', 'account_type': 'SERVICE', 'created_at': '2020-10-15T20:57:44'}
>>> did='user.crab_tape_recall:/TapeRecall/testtask-1720020665/USER'
>>> ruleIds = rucio.add_replication_rule(
...     dids=[did], copies=1,
...     grouping='ALL', weight='ddm_quota', lifetime=86400,
...     account='belforte', activity='Analysis TapeRecall',
...     comment='this is a test', ask_approval=True,
...     rse_expression='T2_RC_MOCK',
...     asynchronous=True)
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/ruleclient.py", line 91, in add_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 500)
>>> 
```

what is different from CLI which worked above ?

## Comment (belforte, 2024-07-03T16:33:29Z)

user client version (`user.user_agent`) is the same in the code and the example in lxplus (1.31.7). Why http 500 vs. `Access to the requested resource denied.\nDetails: Account crab_tape_recall can not add replication rule` ?

I am quite confused and unsure what to do :-(

## Comment (belforte, 2024-07-03T16:34:39Z)

so fare `rucio.add_replication_rule` worked for me, in this case I only change value of arguments.

## Comment (belforte, 2024-07-03T16:47:38Z)

explicitly adding `auth_type='x509'` to Rucio client instantiation resulted in same http 500 error. I am quite curious why I can't reproduce the resource denied in the simple test.

## Comment (dynamic-entropy, 2024-07-03T18:07:16Z)

> when trying a minimal python, I get a new error, w/o any useful detail :-(

Hello @belforte , did should be a dict of the form
```{'scope':'user.crab_tape_recall', name:'<lfn>}```

## Comment (dynamic-entropy, 2024-07-03T18:08:29Z)

I didn't check the logs yet, but it seems like this is not handled properly in the rucio code. 
Can you give it a try?

Cheers

## Comment (belforte, 2024-07-03T20:48:23Z)

🤦

## Comment (belforte, 2024-07-03T21:02:59Z)

thanks @dynamic-entropy . Using the correct DID format makes the standalone python script work.  I should be abel to find out what makes it fail in the code.

## Comment (belforte, 2024-07-05T10:45:50Z)

The error appears when I use this rse_expression

T1_DE_KIT_Disk|T1_ES_PIC_Disk|T1_FR_CCIN2P3_Disk|T1_IT_CNAF_Disk|T1_RU_JINR_Disk|T1_UK_RAL_Disk|T1_US_FNAL_Disk|T2_BE_IIHE|T2_BE_UCL|T2_BR_SPRACE|T2_CH_CERN|T2_CH_CSCS|T2_DE_DESY|T2_DE_RWTH|T2_EE_Estonia|T2_ES_CIEMAT|T2_FI_HIP|T2_FR_GRIF|T2_FR_GRIF_IRFU|T2_FR_GRIF_LLR|T2_FR_IPHC|T2_HU_Budapest|T2_IT_Bari|T2_IT_Legnaro|T2_IT_Pisa|T2_IT_Rome|T2_KR_KISTI|T2_RU_JINR|T2_UK_London_IC|T2_UK_SGrid_RALPP|T2_US_Caltech|T2_US_Florida|T2_US_MIT|T2_US_Nebraska|T2_US_Purdue|T2_US_UCSD|T2_US_Vanderbilt|T2_US_Wisconsin

if I simply put `T1_FR_CCIN2P3` it works.

puzzled.

## Comment (dynamic-entropy, 2024-07-05T10:59:56Z)

Hmm, so the reason is, 
https://github.com/dmwm/CMSRucio/blob/26e67bead81417e59fd2811569b842db2fddd7f6/src/policy/CMSRucioPolicy/permission.py#L318-L320

Let me fix it asap

## Comment (dynamic-entropy, 2024-07-05T11:13:40Z)

Hello @belforte 
Should be good now. Can you please try again?
Cheers

## Comment (belforte, 2024-07-05T12:45:52Z)

Works finely now. Thanks a lot @dynamic-entropy :pray:

## Comment (dynamic-entropy, 2024-07-05T12:52:24Z)

I see you created rules under my account :sweat_smile:

## Comment (belforte, 2024-07-05T12:55:21Z)

I was testing copypasting your command line before I read your update.
your, mine... the command is issued by crab_tape_recall, makes no difference. 
I am deleting all those rules anyhow

## Comment (belforte, 2024-07-05T14:00:32Z)

mechanics is working now, I will work next week on making sure that also checking user limits and enforcing quota works before putting in production.
Thanks again @dynamic-entropy

## Comment (ericvaandering, 2024-07-09T19:14:23Z)

Closing

## Comment (ericvaandering, 2024-07-09T20:31:40Z)

Sorry, this is your issue not mine. It was in my board. :-)
