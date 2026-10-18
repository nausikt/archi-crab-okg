# dmwm/CRABServer pull request #8915: Fix8913

State: closed
Opened: 2025-02-06T15:14:46Z
Closed: 2025-02-12T08:23:36Z
Merged: 2025-02-12T08:23:35Z
URL: https://github.com/dmwm/CRABServer/pull/8915

## Opening post (aspiringmind-code, 2025-02-06T15:14:46Z)

See Issue https://github.com/dmwm/CRABServer/issues/8913
The check for task['status'] == Completed should happen after the checkpublication condition
Tested ```{'TN': '250206_133625:crabint1_crab_20250206_143624', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1, 'probe': 5, 'rescheduled': 0}, 'publication (fail/tdb/DBS)': '0/0/0'}```

## Comment (cmsdmwmbot, 2025-02-06T15:17:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2371/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-02-06T15:43:38Z)

at first sight I think that moving the status check is a mistake. We should talk about this, or you can point to a test w/o it.

## Comment (aspiringmind-code, 2025-02-06T15:49:06Z)

> at first sight I think that moving the status check is a mistake. We should talk about this, or you can point to a test w/o it.

A test without the movement of the block continues to be stuck at "TestRunning": See ```250206_105544:crabint1_crab_20250206_115542``` in [here](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/50535104)

## Comment (belforte, 2025-02-06T15:50:20Z)

if publication is not completed, TestRunning is the desired outcome.

## Comment (belforte, 2025-02-06T15:52:48Z)

OK. Now I am lost in CMS/Atlas build system presentation. Will try to figure out when I have time. Given that current test is broken, feel free to merge.

## Comment (belforte, 2025-02-06T17:30:08Z)

I looked a bit more and I think that this PR is wrong. I suggest to disable publication check in the pipeline yaml file to make pipeline succeed and run the test scrip interactively making sure we cover all use cases. Failing probes, failing processing, failing publication  ....

## Comment (aspiringmind-code, 2025-02-06T17:48:18Z)

I think i understand the problem now. Since we already subtract probe_jobs to get total_jobs in [here](https://github.com/aspiringmind-code/CRABServer/blob/ccd2967e36b783e8c125de00e2337245a08f93bd/cicd/gitlab/st/statusTracking.py#L44), by having it again, we are effectively subtracting twice. You're right the movement of the task['status'] after the checkpublication block is wrong. All we need to do is just use simple total_jobs as jobstoPublish instead of double subtraction of probe_jobs.

## Comment (belforte, 2025-02-06T17:55:47Z)

maybe there's a cleaner way to detect how many jobs should be checked !  Setting aside proble job only once.  But I am now taken until tomorrow afternoon. Basically this is "code that was written w/o knowing that automatic splitting exists" which was then adapted "hack by hack based on the failure of the day" :-(

## Comment (cmsdmwmbot, 2025-02-06T17:59:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2372/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-02-11T16:16:30Z)

@belforte Is it ok if I merge this for now?

## Comment (belforte, 2025-02-12T08:23:32Z)

yeah.. sorry for delay
