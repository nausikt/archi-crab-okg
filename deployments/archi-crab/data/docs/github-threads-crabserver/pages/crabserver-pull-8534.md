# dmwm/CRABServer pull request #8534: print time zone in logs and when next test iteration will be

State: closed
Opened: 2024-06-27T21:00:34Z
Closed: 2024-06-28T10:58:27Z
Merged: 2024-06-28T10:58:27Z
URL: https://github.com/dmwm/CRABServer/pull/8534

## Opening post (belforte, 2024-06-27T21:00:34Z)

I think that pipeline logs are in UTC. Usually we have all logs in local time zone. So I often get confused and worry because I can't match messages to task logs in other places etc. So I would like to add time zone whenever a data is printed.

I also added that when in the retry loop it prints when it will run next time, I am not good at making the addition myself and I need to scroll up and look for last date, which is not convenient.

Check whether you like this.
testing in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7653955

## Comment (cmsdmwmbot, 2024-06-27T21:02:04Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2038/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-28T08:17:34Z)

looks like it is working, from https://gitlab.cern.ch/crab3/CRABServer/-/jobs/40588915/raw
```
Command fail with exit code 4 (1/10 attempted)
Sleep for 900 seconds. Until  10:30 CEST

```
