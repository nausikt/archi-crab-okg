# dmwm/CRABServer pull request #9243: Generic withExponentialRetry decorater derived/combined from/with Vijay's Robustified CRAB Rucio client wrapper for robustify monit report recall quota cron.

State: closed
Opened: 2025-12-08T16:26:19Z
Closed: 2025-12-12T17:34:57Z
Merged: 2025-12-12T17:34:57Z
URL: https://github.com/dmwm/CRABServer/pull/9243

## Opening post (nausikt, 2025-12-08T16:26:19Z)

Resolve #9241 

Put `getRucioUsage`, `getRuleQuota` into Vijay's Client wrapper umbrella this way, will allow us to catch *non-RucioExceptions* that highly coupling with unavailability/unstability of Rucio, Thus utilize the centralized retry/attempt mechanism.

I guessed this patch will make monit_reportrecallquota CRON more robust out of the box. thus mitigate currently flooding emails.

## Notes
- [x] [1] we will give this a try in CRON monitoring first, whether its effective or not. 
> i've to merged this PR First then making a release tag for monit to use, and leave CRON like that for a week to see whether it effectively mitigate the problem.
- [ ] [2] Then, adopt in other places that also use `getRucioUsage` like in `DBSDataDiscovery` when checking things before making taperecall request.
https://github.com/dmwm/CRABServer/blob/5e84119c18a939ea13f1afde4abf6dc680e4f28d/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L560-L566
- [x] [3] Deprecate `getRucioUsage`, `getRuleQuota` standalone fns in `RucioUtils`, We fully start using them from Vijay's client wrapper instead.
- [x] [4?] adopt exponential backoffs? would it be helpful in general? we help Rucio by not to stressing them too much, ALSO Overall, tasks can tolerate the instabilities of Rucio longer than 3 x (180 ms | 1 seconds) retry attempts, may be can tolerate up to 20 minutes or half an hr for example.

P.S. Please, let me know your opinions on notes OR feel free to give me green right? on proceeding to [2],[3],[4] in this PR.

## Comment (cmsdmwmbot, 2025-12-08T16:28:41Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 20 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2701/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-08T17:11:47Z)

We used Vijay's Client but The problematic ChunkedEncoding error are obviously outside the wrapper. 
Have to brings those fns in as Client attrs to enjoy retry/attempt wrapper.

## Comment (nausikt, 2025-12-08T17:19:53Z)

The problematic line that raise error is **\#158**, outside of wrapper scope **\#157** (when we typically call any originally native rucio client fns).
https://github.com/dmwm/CRABServer/blob/5e84119c18a939ea13f1afde4abf6dc680e4f28d/src/python/RucioUtils.py#L157-L159

## Comment (belforte, 2025-12-08T17:41:57Z)

but the ChunkedEncoding  exception is raised inside urllib !
```
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 701, in _update_chunk_length
    raise InvalidChunkLength(self, line)
urllib3.exceptions.InvalidChunkLength: InvalidChunkLength(got length b'', 0 bytes read)
```
You get the exception from line 158 because `files` is not a list, but a generator, so every iteration in the `for` loop is basically a new call to the server to retrieve a new `file` object.
It looks to me that your new getRuleQuota is still exposed to same problem. Simply moving code into RucioUtils makes no difference.

I fully agree with exponential backoffs, your [4]. those are always a must.

But am quite puzzled by 1-2-3.

I still think that you need to make sure that you understand what's happening before you change the code.

At worst put a try/except/retry around https://github.com/dmwm/CRABServer/blob/5e84119c18a939ea13f1afde4abf6dc680e4f28d/src/python/RucioUtils.py#L157-L159
at least is woud be simpler, no ?

## Comment (nausikt, 2025-12-08T18:54:04Z)

Thank you for being patient with me, please, allow me to clarify my disagreement.

> but the ChunkedEncoding exception is raised inside urllib !
> 
> ```
>   File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 701, in _update_chunk_length
>     raise InvalidChunkLength(self, line)
> urllib3.exceptions.InvalidChunkLength: InvalidChunkLength(got length b'', 0 bytes read)
> ```
That's aligned with what i understood.
it was raised from lower-level urllib3 `InvalidChunkLength` -> higher wrapped urllib3 `ProtocolError` -> higher lib request-level, the wrapped exception, `ChunkedEncoding` (the one that we need to catch it here in this layer)

> You get the exception from line 158 because `files` is not a list, but a generator, so every iteration in the `for` loop is basically a new call to the server to retrieve a new `file` object. 

Precisely. but all of that is matter happened outside Vijay's wrapped `client.list_files` (**\#157**) and no try/catch in this outer layer yet. Thus, why current wrapped client still missed this exception.

> It looks to me that your new getRuleQuota is still exposed to same problem. Simply moving code into RucioUtils makes no difference.

May I disagreed?

___

> At worst put a try/except/retry around
> 
> https://github.com/dmwm/CRABServer/blob/5e84119c18a939ea13f1afde4abf6dc680e4f28d/src/python/RucioUtils.py#L157-L159
> 
> 
> at least is woud be simpler, no ?

That was my very first glance solution, But what i try to propose here is we can reuse Vijay's centralized try/except/retry such that we don't repeat ourself. (don't introduce boilerplate of try/except/retry)

If we look carefully, It just like we directly put try/catch as you mentioned above, but we ***instead*** wrap try/catch around the whole `getRuleQuota` fn via the same wrapper mechanic elegantly by line **\#24**. 
https://github.com/dmwm/CRABServer/blob/5e84119c18a939ea13f1afde4abf6dc680e4f28d/src/python/RucioUtils.py#L20-L45

So everything that didn't catch previously inside `getRuleQuota` will be centrally catched by just simply moving things in like this PR.

## Comment (belforte, 2025-12-09T09:28:26Z)

I see. Clearly I have no looked hard enough at new code. Let me try again !

But still I would have liked more that you ran the code w/o stdout to /dev/null to find out if the excpeption logged to mail is fatal or not.
And then run the modified version to verify that it works, i.e. the PR is tested, before we consider merging.

## Comment (belforte, 2025-12-09T09:32:33Z)

so IIUC you created two new methods for Rucio Client, nice trick.  But please document it well, because one may try to find those in Rucio documentation and get very confused.

## Comment (nausikt, 2025-12-09T09:36:51Z)

Acknowledged Stefano! that's true... let me get back to you with tests and docs.
I guessed `caMelCase` might be a little bit helpful here, distinguishing from native Rucio `snake_case_fn`.

## Comment (belforte, 2025-12-09T09:44:20Z)

> I guessed caMelCase might be a little bit helpful here, distinguishing from native Rucio snake_case_fn.

everything helps, but have some pity of who will read this 3 years from now with only a very superficial knowledge of Rucio !

Even if that person were you, you will have forgotten all of this by then and will be puzzled about the rational of moving some RucioUtils inside the wrapped client and some not :-)

Generally speaking, if you nail out a clean ,core, simple rational for things and write it down, code will be easier to write ad will most likely work at first try. Sort of "user manual first".

BTW, this was not first priority. Do not loose sleep on it.

## Comment (nausikt, 2025-12-09T09:50:34Z)

I see. Thanks man for thoughtful review & feedbacks, will do.

## Comment (cmsdmwmbot, 2025-12-09T17:59:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 17 comments to review
 * Pycodestyle check: succeeded
   * 24 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2702/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-09T18:55:05Z)

beautiful :bow:

## Comment (cmsdmwmbot, 2025-12-10T11:43:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 17 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2703/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-10T11:58:37Z)

Thanks to Vijay for ground work and your insightful feedbacks!. 

I've re-think and found these sweet spot, common ground solution that 
1. make this mechanism more *generic* & *reusable* as decorator.
2. *meanwhile* we're not *mixing* our custom/adhoc Rucio utilities fns with the native rucio fns inside Vijay's Client wrapper, as you pointed out!

Things left to test a little bit more Later:
- [x] ensure Vijay's Client retry wrapper is working same as before.
- [x] test on tape recalling logic where using ***getRucioUsage***, and make sure they not crash with new wrapped retry mechanism.
- [ ] [?] may be test more around python2 compatibility if we would like to put ***withExponentialBackOffRetry*** in `ServerUtilities` for better sharing through out server codebase later.

## Tested here 
[1] When things get bad for more than 1 mins, it's raise Exception  terminate right away.
```bash
crab3@crab-dev-tw04:/data/srv/monit$ python ReportRecallQuota.py
Starting new HTTP connection (1): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /ping HTTP/1.1" 200 21
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch']"
NeedRegenerationException
no value, waiting for create lock
value creation lock <dogpile.cache.region.CacheRegion._LockWrapper object at 0x7f865ecd9850> acquired
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch']"
Calling creation function for not-yet-present value
Cache value generated in 0.000 seconds for key(s): "host_to_choose_choice['http://cms-rucio.cern.ch']"
Released creation lock
http://cms-rucio.cern.ch:80 "GET /accounts/whoami HTTP/1.1" 303 209
http://cms-rucio.cern.ch:80 "GET /accounts/crab_server HTTP/1.1" 200 226
rucio client initialized: {'version': '38.5.1'} {'account_type': 'SERVICE', 'suspended_at': None, 'status': 'ACTIVE', 'created_at': '2020-04-29T15:40:28', 'updated_at': '2020-04-29T15:40:28', 'account': 'crab_server', 'email': 'Stefano.Belforte@cern.ch', 'deleted_at': None}
http://cms-rucio.cern.ch:80 "GET /rules/?activity=Analysis+TapeRecall HTTP/1.1" 200 None
Starting new HTTP connection (2): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Retryable exception in 'getRuleQuota' (attempt 1/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (3): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Retryable exception in 'getRuleQuota' (attempt 2/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (4): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Retryable exception in 'getRuleQuota' (attempt 3/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (5): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Retryable exception in 'getRuleQuota' (attempt 4/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (6): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Retryable exception in 'getRuleQuota' (attempt 5/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (7): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
[MOCK] Random failure with 90% chances...
Operation 'getRuleQuota' failed after 5 retries: Random ChunkedEncodingError for testing
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 224, in getRucioUsage
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 224, in <genexpr>
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 190, in getRuleQuota
    mock_fail()
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 179, in mock_fail
    raise ChunkedEncodingError("Random ChunkedEncodingError for testing")
requests.exceptions.ChunkedEncodingError: Random ChunkedEncodingError for testing

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "ReportRecallQuota.py", line 110, in <module>
    main(logger)
  File "ReportRecallQuota.py", line 86, in main
    report = createQuotaReport(rucioClient=rucioClient,
  File "ReportRecallQuota.py", line 35, in createQuotaReport
    totalBytes = getRucioUsage(rucioClient=rucioClient,account=account,activity=activity)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 46, in wrapper
    logger.warning(f"Retryable exception in '{name}' (attempt {attempt+1}/{retryAttempts}): {e}")
AttributeError: 'NoneType' object has no attribute 'warning'
``` 

[2] Logs, when things not severe, with 30% chances of failures, and were tolerable.
```bash
Starting new HTTP connection (1): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /ping HTTP/1.1" 200 21
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch']"
NeedRegenerationException
no value, waiting for create lock
value creation lock <dogpile.cache.region.CacheRegion._LockWrapper object at 0x7f4692963850> acquired
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch']"
Calling creation function for not-yet-present value
Cache value generated in 0.000 seconds for key(s): "host_to_choose_choice['http://cms-rucio.cern.ch']"
Released creation lock
http://cms-rucio.cern.ch:80 "GET /accounts/whoami HTTP/1.1" 303 209
http://cms-rucio.cern.ch:80 "GET /accounts/crab_server HTTP/1.1" 200 226
rucio client initialized: {'version': '38.5.1'} {'account_type': 'SERVICE', 'suspended_at': None, 'status': 'ACTIVE', 'created_at': '2020-04-29T15:40:28', 'updated_at': '2020-04-29T15:40:28', 'account': 'crab_server', 'email': 'Stefano.Belforte@cern.ch', 'deleted_at': None}
http://cms-rucio.cern.ch:80 "GET /rules/?activity=Analysis+TapeRecall HTTP/1.1" 200 None
Starting new HTTP connection (2): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/872e65c88d7b4e1a88fcecadea29eab1 HTTP/1.1" 200 1340
http://cms-rucio.cern.ch:80 "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251209_080215.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes1_part3%2FUSER/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/2a0ec244c2ee48499f930112fcb0f924 HTTP/1.1" 200 1031
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FJetMET1%2FRun2024E-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 1/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (3): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/2a0ec244c2ee48499f930112fcb0f924 HTTP/1.1" 200 1031
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FJetMET1%2FRun2024E-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 2/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (4): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/1d7009b9588f4eb39492fb6c060b1a33 HTTP/1.1" 200 1728
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FDYJetsToMuMu_H2ErratumFix_PDFExt_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos%2FRunIISummer20UL17RECO-106X_mc2017_realistic_v6-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/353c7e70d0c443a68c0310d897e99ba0 HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-24_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 1/5): Random ChunkedEncodingError for testing
Starting new HTTP connection (7): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/353c7e70d0c443a68c0310d897e99ba0 HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-24_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/dbfba49ed04f4a65bd2f402a536861da HTTP/1.1" 200 1030
...
Starting new HTTP connection (36): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/6444a4c86c954c57a24698c9f222fe0f HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-21_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /accounts/crab_input/usage/local HTTP/1.1" 200 None
Starting new HTTPS connection (1): monit-metrics.cern.ch:10014
/usr/local/lib/python3.8/site-packages/urllib3/connectionpool.py:1043: InsecureRequestWarning: Unverified HTTPS request is being made to host 'monit-metrics.cern.ch'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
https://monit-metrics.cern.ch:10014 "POST /crab-test HTTP/1.1" 200 None
```

## Comment (cmsdmwmbot, 2025-12-10T13:08:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 17 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2704/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-10T13:25:37Z)

Vijay's Client wrapper works well!
have tested by hijack Rucio Native Client at `/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py`. 
*P.S. [1,2] were how's robust/tolerance looks like.*

In **[1]** it's seems like we made twice/thrice catch/retry here but it just make getRucioUsage tolerate 10 times of failures with 2~3 mins time span of retrying. 
> Of course! we can configure ***withExponentialBackOffRetry*** to be more/less specific via *fatalExceptions*, *retryExceptions* knobs depends on use cases.

[1] Mock Raised both `RucioException` and `Non-Rucio` ValueError Exception. 
```bash
http://cms-rucio.cern.ch:80 "GET /rules/69ea782d10f94d73b141db1eadd7f8be HTTP/1.1" 200 1182
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-15_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 1/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 2/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 3/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
value creation lock <dogpile.cache.region.CacheRegion._LockWrapper object at 0x7f2caf3026d0> acquired
Calling creation function for previously expired value
Cache value generated in 0.000 seconds for key(s): "host_to_choose_choice['http://cms-rucio.cern.ch']"
Released creation lock
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 1/5): [Mock] Non-RucioException inside RucioNative Client call...
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 4/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 5/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1029
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FJetMET1%2FRun2024B-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/922bf4b9423f40e9bc4db3bfa711f9bf HTTP/1.1" 200 1182
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 1/5): [Mock] Non-RucioException inside RucioNative Client call...
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-18_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/957673435c844864a0edabd9ad99dc20 HTTP/1.1" 200 1180
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 1/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/957673435c844864a0edabd9ad99dc20 HTTP/1.1" 200 1180
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-3_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/2a2282b5203448c3b7d53c5057d9dc10 HTTP/1.1" 200 1180
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 1/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/2a2282b5203448c3b7d53c5057d9dc10 HTTP/1.1" 200 1180
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-3_M-400_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/3d2749ebfdba49eaa2b34eb11576606c HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-15_M-1200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/54a301a25d0b480f8dcda4a6cd8bb918 HTTP/1.1" 200 1182
[MOCK] Fail on Rucio 503 with 20% chances...
Fatal exception in 'list_files' : An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 37, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 68, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 397, in list_files
    mock_fail()
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 31, in mock_fail
    raise RucioException("[Mock 503] An unknown exception occurred...")
rucio.common.exception.RucioException: An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
Retryable exception in 'getRuleQuota' (attempt 1/5): An unknown exception occurred.
Details: [Mock 503] An unknown exception occurred...
http://cms-rucio.cern.ch:80 "GET /rules/54a301a25d0b480f8dcda4a6cd8bb918 HTTP/1.1" 200 1182
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-21_M-600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/202393e17291409dbf7dbb41eeb868c3 HTTP/1.1" 200 1182
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 1/5): [Mock] Non-RucioException inside RucioNative Client call...
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-21_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/da91994b8ecd4ebfad020f63b175acab HTTP/1.1" 200 1182
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-15_M-100_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/1904112396c54157b360df031449568d HTTP/1.1" 200 1182
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 1/5): [Mock] Non-RucioException inside RucioNative Client call...
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 2/5): [Mock] Non-RucioException inside RucioNative Client call...
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-24_M-100_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/d1e2c0db44644fa39541704cbbd8a9ed HTTP/1.1" 200 1182
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-6_M-1200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/27f58f80a39e424dbf6dd7b9ee107610 HTTP/1.1" 200 1180
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-6_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/2d9896f97772474abb67216bdf4a766f HTTP/1.1" 200 1182
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-18_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/e8f69a009c52447a88d7b6488831e93f HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-15_M-2400_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/43d3dd89bad940f999652edacf39cb1a HTTP/1.1" 200 1035
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FJetMET1%2FRun2025C-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/69798a6149ce4ae28c7cfe5166943cab HTTP/1.1" 200 1182
[MOCK] Non-RucioException with 20% chances...
Retryable exception in 'list_files' (attempt 1/5): [Mock] Non-RucioException inside RucioNative Client call...
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-15_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/eb6165d0b73a4d0aa4632bfcde3f951b HTTP/1.1" 200 1180
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-9_M-600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
http://cms-rucio.cern.ch:80 "GET /rules/6444a4c86c954c57a24698c9f222fe0f HTTP/1.1" 200 1184
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FHSCPmchamp_Q-21_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
Resetting dropped connection: cms-rucio.cern.ch
http://cms-rucio.cern.ch:80 "GET /accounts/crab_input/usage/local HTTP/1.1" 200 None
Starting new HTTPS connection (1): monit-metrics.cern.ch:10014
/usr/local/lib/python3.8/site-packages/urllib3/connectionpool.py:1043: InsecureRequestWarning: Unverified HTTPS request is being made to host 'monit-metrics.cern.ch'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
https://monit-metrics.cern.ch:10014 "POST /crab-test HTTP/1.1" 200 None
```

[2] Finalized Warning logs for all cases.
```bash
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 1/5): Random ChunkedEncodingError for testing, waiting for 1 seconds...
Starting new HTTP connection (3): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/7be04d7cc9bb49fa9fa6d68c14ab08d8 HTTP/1.1" 200 1251
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FDYJetsToMuMu_H2ErratumFix_PDFExt_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 2/5): Random ChunkedEncodingError for testing, waiting for 2 seconds...
Starting new HTTP connection (4): cms-rucio.cern.ch:80
http://cms-rucio.cern.ch:80 "GET /rules/7be04d7cc9bb49fa9fa6d68c14ab08d8 HTTP/1.1" 200 1251
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FDYJetsToMuMu_H2ErratumFix_PDFExt_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[MOCK] Random failure with 30% chances...
Retryable exception in 'getRuleQuota' (attempt 3/5): Random ChunkedEncodingError for testing, waiting for 4 seconds...
Starting new HTTP connection (5): cms-rucio.cern.ch:80
```

## Comment (cmsdmwmbot, 2025-12-10T13:31:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 9 comments to review
 * Pycodestyle check: succeeded
   * 11 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2705/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-10T13:31:18Z)

just try to run it for real a few times and see how it goes. Or run it alongside the current one.

## Comment (nausikt, 2025-12-10T13:41:57Z)

> just try to run it for real a few times and see how it goes. Or run it alongside the current one.

O.K. Stefano, we quite confident with decorator now, may i have your final review/approve please? 

I would like to merge -> make release tag/image *just* for monit cron -> deploy *only* on **crab-dev-tw02**.

if  cron daemon of **crab-dev-tw02** completely slience for a week, i will apply to **crab-prod-tw02** as well.

## Comment (belforte, 2025-12-10T13:55:45Z)

let's only merge tested PR's.
You can temporarily stop puppet on dev-tw02 and add whatever crontab you like.
Or run a crontab with your user name

## Comment (nausikt, 2025-12-10T15:29:15Z)

I've switched cron to the new code on ***crab-dev-tw02***.
```cron
# Puppet Name: Monit ReportRecallQuota crab rucio quota
# 3-59/5 * * * * export loguuid=$(uuidgen);                 test -f /home/crab3/runContainer.sh &&                 bash /home/crab3/runContainer.sh -v v3.latest                 -s TaskWorker_monit_reportrecallquota -u ${loguuid}                 -c 'python3 /data/srv/monit/ReportRecallQuota.py'                 >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ]                 && cat /tmp/monit-${loguuid}.txt
3-59/5 * * * * export loguuid=$(uuidgen);                 test -f /home/crab3/runContainer.sh &&                 bash /home/crab3/runContainer.sh -v krittin_test_monit_taperecallquota-2                 -s TaskWorker_monit_reportrecallquota -u ${loguuid}                 -c 'python3 /data/srv/monit/ReportRecallQuota.py'                 >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ]                 && cat /tmp/monit-${loguuid}.txt
```
it periodically spin up the new code and run well for a while.
```
Every 2.0s: docker ps                                           crab-dev-tw02.cern.ch: Wed Dec 10 16:18:05 2025

CONTAINER ID   IMAGE                                                                       COMMAND
     CREATED	     STATUS         PORTS     NAMES
d1d74bb6c406   registry.cern.ch/cmscrab/crabtwmonit:krittin_test_monit_taperecallquota-2   "tini -- python3 /da
…"   4 seconds ago   Up 4 seconds             TaskWorker_monit_reportrecallquota
4268fa637fb0   registry.cern.ch/cmscrab/crabtwmonit:v3.latest                              "tini -- python3 /da
…"   5 minutes ago   Up 5 minutes             TaskWorker_monit_checktaperecall
6ea2c5806450   registry.cern.ch/cmscrab/crabtaskworker:v3.250812-stable                    "tini -- /data/run.s
h"   4 months ago    Up 4 months              TaskWorker
```
Let's see how things goes for a few days...
Historically, *crab-dev-tw02* crash *multiple times a day every day*, since at least **30th Nov**.

## Comment (belforte, 2025-12-10T15:58:22Z)

sounds good. As you may have notice most times we get error at same time from prod-tw02 and dev-tw02, reinforcing the idea that the problem is a temporarily overload on Rucio server side. So if now we get the error on prod but not on dev, we can call it success

## Comment (nausikt, 2025-12-10T16:04:00Z)

I fail to find Grafana dashboard, opensearch that reflect these cron `monit_reportrecallquota` collected data on `dev-tw02`, `prod-tw02`. Are they redundant to each other? or dev-tw02 just for your testing.

Could you pointed out for me please? i would like to check whether data points are cleanly there thus silence not falsified success data collecting.

## Comment (belforte, 2025-12-10T16:10:27Z)

https://monit-grafana.cern.ch/d/bf6n7bbah7ev4b/crab-overview-test-monitoring?orgId=11&refresh=1h
see
https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-crontabs.html

## Comment (cmsdmwmbot, 2025-12-12T17:04:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 9 comments to review
 * Pycodestyle check: succeeded
   * 11 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2706/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-12T17:34:35Z)

`ChunkedEncodingError` flooding emails were gone from `crab-dev-tw02`. patch looks addressed issue well.

As we discussed, We will proceeding to merge this PR, make release, deploy on `dev` and `prod` (`crab-prod-tw02`) and address another cron email flooding[1] .
[1]
```
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)
```

## Comment (nausikt, 2025-12-16T10:31:20Z)

So far, `crab-dev-tw02` test monitoring have been working well, see [Grafana](https://monit-grafana.cern.ch/d/f72be185-5789-4015-933a-a29a6ed75514/crab-overview-test-monitoring?orgId=11&refresh=1h) and **NO** *simultaneously* `ChunkedEncodingError` flooding like happened on `crab-prod-tw02` over last week as we expected. `503`(s) were gone as well, may be Rucio have been relieved from overloading.

That being said, this canary twmonit image is now eligible for promoting into prod explicitly via puppet. (affect cron in `crab-prod-tw02`, `crab-dev-twX`) 

**For 503 Rucio Overloaded error investigations**, that we try to gathering more information.
IIUC, It's turned out that `_send_request` even trying to ***Categorized*** http response into `ServerConnectionException`, `ConnectionError`, `OSError`, `IOError` as we can see in [[2](https://github.com/rucio/rucio/blob/45b19709d28ecccc39cd0e73e4087a7e79a71c49/lib/rucio/client/baseclient.py#L446-L529)].  But this weird 503 raised from server went through them all somehow.

The result is not `None` and response output was redirected to `_get_exception` with very *default* exception and *default* message was raised, no  *specific* ExceptionClass was mentioned in response data too.
See [here]( https://github.com/rucio/rucio/blob/45b19709d28ecccc39cd0e73e4087a7e79a71c49/lib/rucio/client/baseclient.py#L396-L410)
if  ExceptionClass was mentioned in the response.
```python
        exc_cls = 'RucioException'
        exc_msg = 'no error information passed (http status code: %s)' % status_code
        if 'ExceptionClass' in data:
            exc_cls = data['ExceptionClass']
        elif 'ExceptionClass' in headers:
            exc_cls = headers['ExceptionClass']
        if 'ExceptionMessage' in data:
            exc_msg = data['ExceptionMessage']
        elif 'ExceptionMessage' in headers:
            exc_msg = headers['ExceptionMessage']
```
it would be retrieved well in `_get_exception` but in this case, may be it was very **uncanny** bugs, so was raised with plain message. Thus why it can't be categorized to any well defined 503, i guessed.
```python
if hasattr(exception, exc_cls):
            return getattr(exception, exc_cls), exc_msg
```

***Type of Exception***: `<class 'rucio.common.exception.RucioException'>`
***repr()***: `RucioException('no error information passed (http status code: 503)')`

[1] Full log of 503.
```bash
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)
Type of Exception: <class 'rucio.common.exception.RucioException'>
Traceback (most recent call last):
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 218, in getRucioUsage
   totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 218, in <genexpr>
   totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 181, in getRuleQuota
   rule = rucioClient.get_replication_rule(ruleId)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
   return attr(*args, **kwargs)
 File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
   raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)
repr(): RucioException('no error information passed (http status code: 503)')
Traceback (most recent call last):
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 218, in getRucioUsage
   totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 218, in <genexpr>
   totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 181, in getRuleQuota
   rule = rucioClient.get_replication_rule(ruleId)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
   return attr(*args, **kwargs)
 File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
   raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
```

[2] https://github.com/rucio/rucio/blob/45b19709d28ecccc39cd0e73e4087a7e79a71c49/lib/rucio/client/baseclient.py#L446-L529

## Comment (belforte, 2025-12-17T11:49:47Z)

thanks @nausikt

Even if I do not fully agree with your analysis of Rucio code, this indeed a case where Rucio does not give us a useful Exception type to use.

Do you think it would make sense to look for `http status code: 503` in `repr(exception)` and trigger the retry loop in that case ?

Otherwise we may very well bite the bulled and put an try/except around our `getRuleQuota` and either retry or skip the rule which fails. Or retry a couple times and then skip.

## Comment (belforte, 2025-12-17T11:50:11Z)

in the meantime you can put this in production and reduce the noise, thanks !

## Comment (nausikt, 2025-12-17T12:15:08Z)

> Do you think it would make sense to look for `http status code: 503` in `repr(exception)` and trigger the retry loop in that case ?
> 
Its make sense and doable to me! i will do it asap man, expected to be after migrating code to py3.12 compatible and also after desired CUDA capabilities bug fixing.

*P.S. I've got py3.12 support almost done now, it has been verified/tested on test14 via pipeline, also manually with `CMSSW_16_0_PY312_X_2025-12-16-2300` for [[Normal Task](https://cmsweb-test14.cern.ch/crabserver/ui/task/251217_111001%3Akphornsi_crab_test14-CMSSW_16_py312-testing)] and [[AS Task](https://cmsweb-test14.cern.ch/crabserver/ui/task/251217_113451%3Akphornsi_crab_test14-automatic-splitting-CMSSW-16-py312-compatible)], So far they looks really good.*
> in the meantime you can put this in production and reduce the noise, thanks !
>
I did put it in prod yesterday. we've officially farewelled to `ChunkedEncodingError`!
