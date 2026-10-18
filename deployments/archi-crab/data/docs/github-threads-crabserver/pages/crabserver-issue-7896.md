# dmwm/CRABServer issue #7896: Jenkins tests wrongly reports success

State: closed
Opened: 2023-10-06T12:47:17Z
Closed: 2023-10-09T14:09:45Z
Labels: Status: Done, Priority: TOP, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7896

## Opening post (belforte, 2023-10-06T12:47:17Z)

see e.g.
https://github.com/dmwm/CRABServer/issues/7895#issuecomment-1750322572

```
'231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED',
```
but the test is classifies as "TestPassed"
```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 5}, 'TN': '231006_093458:cmsbot_crab_20231006_113457', 'combinedStatus': 'FAILED', 'publication (fail/tdb/DBS)': '0/0/0'}
```

## Comment (belforte, 2023-10-06T16:25:12Z)

that was an automatic splitting task. Ultimate cause is that things failed early in the PreDag phase so no job was submitted but the probe jobs. In this case the current https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/statusTracking.py finds that all jobs succeeded and declares "test passed".
This makes impossible to detect failures in PreDag like we had today due to Rucio cert https://github.com/dmwm/CRABServer/pull/7897

## Comment (belforte, 2023-10-06T16:42:35Z)

Current test will also show a fake "passed" if dagman is not started for whatever reason

## Comment (belforte, 2023-10-06T19:28:50Z)

I have added the check on schedule status, but the question is what to do when task fails to submit any (non-probe) jobs.
For generality I am falling back to resubmission.
In case of persistent problem (but in new code e.g.), the test will stay in `'testResult': 'TestResubmitted',` until all retries are consumed.
