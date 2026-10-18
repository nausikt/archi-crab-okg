# dmwm/CRABServer issue #9348: resubmission delay does not work in new code

State: open
Opened: 2026-07-15T20:04:14Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9348

## Opening post (belforte, 2026-07-15T20:04:14Z)

refactored Retry/Resubmission code now allows for introducing additional, flexible, delays in the retry policy executed during automatic resubmissions
https://github.com/dmwm/CRABServer/blob/1038e05ebaf8cc0ae95906d385899d8344b1d460/src/python/TaskWorker/Actions/RetryJob.py#L23-L26
https://github.com/dmwm/CRABServer/blob/1038e05ebaf8cc0ae95906d385899d8344b1d460/src/python/TaskWorker/Actions/PreJob.py#L539-L549

but when testing the delay is not applied.

Initial guess is that https://github.com/dmwm/CRABServer/blob/1038e05ebaf8cc0ae95906d385899d8344b1d460/src/python/TaskWorker/Actions/PreJob.py#L543
points to current retry number while PostJob write the delay policy when processign the previous submission.

But an attempt change to
```python
key = str(crab_retry-1)
```
did not work.

Deeper "digging" is needed.

## Comment (belforte, 2026-07-15T20:05:07Z)

@aspiringmind-code I will take over as agreed, please write down what you tried and which problems you found.

## Comment (aspiringmind-code, 2026-07-16T13:42:58Z)

See [task](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=260715_082255:vchakrav_crab_20260715_102252&from=2026-07-15T07:22:55.000Z&to=now&timezone=utc&var-site=$__all&var-schedd=059&var-cmsUserId=&var-task_str=vchakrav_crab_20260715_102252&var-status=$__all&var-crabid=$__all&var-Filters=&var-rest_host=https:%2F%2Fcmsweb.cern.ch) for example.
The main problem is that the RRN remains the same in the next retry if the delay happens in the last retry (using inkey and str(crab_retry -1) concept). In the given task, RRN=2 for both prejob.1.1.txt and prejob.1.2.txt in which prejob.1.1 TaskManagerBootstrap ended with exit code 4 due to the delay. When prejob.1.2.txt picks it up again, we get `Wed, 15 Jul 2026 10:28:49 CEST(+0200):INFO:PreJob RRN for job 1 reused as 2 (interrupted pre-job, not re-incrementing)` and therefore RRN is at 2 in both. We run into prejob.1.3.txt for RRN=3.
Another problem because of this is that the retry in which delay happened (1 in this case) is missing from the all retries [monitoring](https://monit-grafana.cern.ch/goto/dfsacmqss1ybkc?orgId=11)
To summarise, RRN concept needs to be aligned with the delay generated Exit Code 4. RRN originally without delay is reusing the last RRN and not re incrementing it to handle interrupted prejob.
