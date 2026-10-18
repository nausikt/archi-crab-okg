# dmwm/CRABServer issue #7797: RUCIO_Transfers.py: Things need to be done before deploy on production

State: closed
Opened: 2023-08-04T12:34:36Z
Closed: 2024-02-14T10:32:00Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7797

## Opening post (novicecpp, 2023-08-04T12:34:36Z)

While we are waiting for subtasks in https://github.com/dmwm/CRABServer/issues/7632 to close, and waiting for [more test](https://monit-grafana.cern.ch/d/ByvZ-kX4k/user-tseethon-cms-tasks-monitoring-globalview?orgId=11&var-user=tseethon&var-site=All&var-current_url=%2Fd%2FIF-s18qVk%2Fuser-tseethon-cms-task-monitoring-task-view&var-task=All&var-match_env=usertask_test12), here is a list of things that we need to do before we deploy Rucio ASO to production and starting ask user to use, that can be done in parallel: 

- Changes in client
  - [x] ~~New crab args, storagArea = sitelocal/rucio~~ ([see  comment](https://github.com/dmwm/CRABServer/issues/7797#issuecomment-1669685313))
  - [x] Enrich crab status (rucio rule id)
  - [x] Fix web ui
- User docs
  - [x] How does it work (transfer/publish container)
  - [x] How to request quota
  - [x] Example task submit with rucio aso
  - [x] Limitation
  - [x] Common FAQ and Troubleshooting
- Server
  - [x] Merge `rucio_transfers` to master
- Monitoring
  - [ ] Script crash (gathering "exception" logs using filebeat)

Note that these tasks are not include in this round:
  - Publisher
  - crab checkwrite
  - TW check Rucio quota before submit to schedd
  - Validation publish container
  - Rucio ASO scripts performance

## Comment (novicecpp, 2023-08-08T14:03:59Z)

I decided not to add new client args (storagArea = sitelocal/rucio) because it will make it more confusing, especially when we need to debug later.
In example:
```python
config.Data.outLFNDirBase = '/store/user/tseethon/mytestoutput-1532'
config.Data.storageArea = 'rucio' # new args
```

When we submitting task to server we put `/store/user/rucio/tseethon/mytestoutput-1532` in `tm_output_lfn`, but when we trace it back what this value come from, it will not match what we see expect to see in client config until we notice `storageArea` option later.

## Comment (belforte, 2023-08-08T15:21:17Z)

Agreed, Anyhow we can always revisit this as needs come

## Comment (novicecpp, 2023-09-07T09:19:18Z)

First draft of User Documentation. 
https://cmscrab.docs.cern.ch/randoms/rucio-stageout/rucio-stageout.html

Request for comment @belforte @mapellidario

## Comment (belforte, 2023-09-12T14:35:06Z)

thanks for the new documentation ! And sorry that it took a while to get to read it.
I  have a list of comments. Let me try to paste it here:

```
User Guides / Rucio Stageout
1. this is not lxplus specific
2. rucio cli vs. cmsenv needs to allow for py3 based cmssw where rucio works
3. publication is now done
4. Monitoring statusof the transfer will become part of CRAB client, right ?
5. what does it mean "We are in the process of implementing automatic retries from different job retry"

Randoms / Rucio Stageout Twiki 
1. why Twiki ?

Randoms/ Rucio Stageout Twiki / Rucio Stageout / Example
1. make it more clear: one Transfer Container for each Task
2. make it clear that multiple tasks can add files to same
   Publish Container (and DBS dataset), just like now.
3. Publish Container with /FakeDataset can be used to manage dataset with Rucio but will not be published to DBS (we may need to ensure that this is done)

Randoms/ Rucio Stageout Twiki / Rucio Stageout / How does it work ?
1. clarify "sends the list" ? leave it as "implementation detail" ?
2. 1.a. should be moved under 2.
3. add a note to indicate that e.g. expiration date can be differet for transfer and publication container (why do we need a replication rule on publish container otherwise ?)
4. indicate that timeout is currently 7 days after the end life of the DAG, i.e. once all job (re)submission has stopped, we wait for up to 7 days before giving up.
5. indicate what happens when ASO stops: containers and rules will still be there, and Rucio will keep trying stuck trasnfers for up to 14 dasy (after that rule becomes SUSPENDED), but CRAB internal bookkeeping will not be updated and files which manage to be xferred (if any) will not be published.

Randoms/ Rucio Stageout Twiki / Rucio Stageout / Monitoring transfer status / Note about Rule/Lock

1. rule/lock state must take into account SUSPENDED rules https://mattermost.web.cern.ch/cms-o-and-c/pl/7aobhfttqtdtiyg6xrxe5ur6nh
2. We need to find out what we can do with SUSPENDED rules

Randoms/ Rucio Stageout Twiki / Rucio Stageout / Compare to FTS Stageout
1. remove phedex
2. Monitoring Transfer in the table needs fixing

Randoms/ Rucio Stageout Twiki / Rucio Stageout / Current Limitation
1. bullet points are duplicated
2. transferLog IIUC is a technicality and will be ther, CERNBOX will stay there forever, resubmit of hopeless xfers is possible with a lot of work but unlikely to ever be done

Randoms / Rucio Stageout Twiki / Tutorial
1. should this rather be in Users Guides ?

Randoms / Rucio Stageout Twiki / Tutorial / Get Public Container and it*s* rule ID
1. this will be done in CRABClient, right ? No need to have it here.


```

## Comment (novicecpp, 2023-09-13T08:04:44Z)

Thank you very much for the comments.

> User Guides / Rucio Stageout
> 1. this is not lxplus specific
> 2. rucio cli vs. cmsenv needs to allow for py3 based cmssw where rucio works
> 3. publication is now done
> 4. Monitoring statusof the transfer will become part of CRAB client, right ?
> 5. what does it mean "We are in the process of implementing automatic retries from different job retry"

Sorry, I forgot to take this section down. It was written by Diego long times ago when you and Deigo asked us to try Rucio ASO.

> Randoms / Rucio Stageout Twiki
> 1. why Twiki ?

Because it is users documentation. As we agreed, operator docs put it here and user docs move to Twiki.
I am not familiar with Twiki syntax so I wrote in markdown first and put in `Randoms / Rucio Stageout Twiki`.


> Randoms/ Rucio Stageout Twiki / Rucio Stageout / Example
> 1. make it more clear: one Transfer Container for each Task
> 2. make it clear that multiple tasks can add files to same Publish Container (and DBS dataset), just like now.
> 3. Publish Container with /FakeDataset can be used to manage dataset with Rucio but will not be published to DBS (we may need to ensure that this is done)
>
>
> Randoms/ Rucio Stageout Twiki / Rucio Stageout / How does it work ?
> 1. clarify "sends the list" ? leave it as "implementation detail" ?
> 2. 1.a. should be moved under 2.
> 3. add a note to indicate that e.g. expiration date can be differet for transfer and publication container (why do we need a replication rule on publish container otherwise ?)
> 4. indicate that timeout is currently 7 days after the end life of the DAG, i.e. once all job (re)submission has stopped, we wait for up to 7 days before giving up.
> 5. indicate what happens when ASO stops: containers and rules will still be there, and Rucio will keep trying stuck trasnfers for up to 14 dasy (after that rule becomes SUSPENDED), but CRAB internal bookkeeping will not be updated and files which manage to be xferred (if any) will not be published.
>
>
> Randoms/ Rucio Stageout Twiki / Rucio Stageout / Monitoring transfer status / Note about Rule/Lock
>
> 1. rule/lock state must take into account SUSPENDED rules https://mattermost.web.cern.ch/cms-o-and-c/pl/7aobhfttqtdtiyg6xrxe5ur6nh
> 2. We need to find out what we can do with SUSPENDED rules
>
>
> Randoms/ Rucio Stageout Twiki / Rucio Stageout / Compare to FTS Stageout
> 1. remove phedex
> 2. Monitoring Transfer in the table needs fixing

Will fix.


> Randoms/ Rucio Stageout Twiki / Rucio Stageout / Current Limitation
> 1. bullet points are duplicated
> 2. transferLog IIUC is a technicality and will be ther, CERNBOX will stay there forever, resubmit of hopeless xfers is possible with a lot of work but unlikely to ever be done

I will adjust the wording to your suggestion.
But, what does `CERNBOX will stay there forever` mean?


> Randoms / Rucio Stageout Twiki / Tutorial
> 1. should this rather be in Users Guides ?

I will merge "Users Guides" to this page.

> Randoms / Rucio Stageout Twiki / Tutorial / Get Public Container and it*s* rule ID
> 1. this will be done in CRABClient, right ? No need to have it here.

I see. I will open PR in CRABClient soon.

## Comment (belforte, 2023-09-13T15:21:51Z)

I think we can take care of changes when we move from MD to twiki. Which I fear is on me !
As to CERNBOX, the point is that CERNBOX will never be writeable by Rucio since it is a CERN resource, not a CMS one. CMS will not create an RSE using /eos/home as disk resource.
Just like we can't support reading data from there remotely (it not part of the redirector phederation) nor via local PFN to PFN translation.
It is a "send" only location. 
That CERN decided to use several PB's to give every user 1TB on EOS, well... nice of them, we can't tell them to give it to use so that we can manage that space

## Comment (belforte, 2023-09-13T15:22:26Z)

Let's move the list above to a different GH, that' s all.

## Comment (novicecpp, 2024-02-14T10:32:00Z)

`Script crash (gathering "exception" logs using filebeat)` will do later when we have more users. 
Closing
