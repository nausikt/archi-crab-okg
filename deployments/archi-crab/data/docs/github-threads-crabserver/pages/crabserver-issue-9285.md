# dmwm/CRABServer issue #9285: RucioException - 503 service temporary unavailable should be retryable and have extra tolerance.

State: closed
Opened: 2026-03-26T11:38:49Z
Closed: 2026-07-22T20:19:52Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9285

## Opening post (nausikt, 2026-03-26T11:38:49Z)

Today, Rucio was down almost an hour, 
all submissions and rucio commands failed as Stefano reported and fixed by Panos.

## Problem:
Our wait-and-retry logic [1] has effectively ignored 503 errors so far, 
because *fatal* `RucioExceptions` were all treated the **same**.

## Solution
We should instead give 503 responses extra tolerance in the retry delay.

*P.S. This should put an end to the almost daily flood of 503 emails [2] whenever Rucio is under stress.*
*P.S. This aligned with retryable mechanism on our REST side[3]*

[1] CRAB wait-n-retry wrapper, treat RucioException as fatal that should be raise immediately. 
https://github.com/dmwm/CRABServer/blob/216d7f5d698a020104d72b1d354fbcfe906b721e/src/python/RucioUtils.py#L70-L75

[2] The last remaining flooding email.
```
^[[33;1m2026-03-25 16:13:24,170	WARNING	Waiting 0.25s due to reason: server returned 503 ^[[0m
Waiting 0.25s due to reason: server returned 503
Starting new HTTP connection (3): [cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/)
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/705a10ff09a94da6b8f2d71b6b3621b5 HTTP/1.1" 503 190
^[[33;1m2026-03-25 16:13:24,424	WARNING	Waiting 0.5s due to reason: server returned 503 ^[[0m
Waiting 0.5s due to reason: server returned 503
Starting new HTTP connection (4): [cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/)
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/705a10ff09a94da6b8f2d71b6b3621b5 HTTP/1.1" 503 190
^[[33;1m2026-03-25 16:13:24,929	WARNING	Waiting 1.0s due to reason: server returned 503 ^[[0m
Waiting 1.0s due to reason: server returned 503
Fatal exception in 'get_replication_rule' : An unknown exception occurred.
Details: no error information passed (http status code: 503)
Traceback (most recent call last):
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
   return attr(*args, **kwargs)
 File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
   raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
Details: no error information passed (http status code: 503)
Type of Exception: <class 'rucio.common.exception.RucioException'>
Traceback (most recent call last):
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
   return func(*args, **kwargs)
 File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
   return attr(*args, **kwargs)
 File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
   raise exc_cls(exc_msg)
rucio.common.exception.RucioException: An unknown exception occurred.
Traceback (most recent call last):
 File "/data/srv/monit/ReportRecallQuota.py", line 110, in <module>
   main(logger)
 File "/data/srv/monit/ReportRecallQuota.py", line 86, in main
   report = createQuotaReport(rucioClient=rucioClient,
 File "/data/srv/monit/ReportRecallQuota.py", line 35, in createQuotaReport
   totalBytes = getRucioUsage(rucioClient=rucioClient,account=account,activity=activity)
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
```

[3] CRAB REST also treat 503 (when DB unavailable) as retryable as well, with extra 20s tolerances.
https://github.com/dmwm/CRABServer/blob/216d7f5d698a020104d72b1d354fbcfe906b721e/src/python/RESTInteractions.py#L29-L38

## Comment (belforte, 2026-03-26T11:57:02Z)

see also https://github.com/dmwm/CRABServer/issues/9281
