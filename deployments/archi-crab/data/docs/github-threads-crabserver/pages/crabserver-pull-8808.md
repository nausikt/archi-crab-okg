# dmwm/CRABServer pull request #8808: Canary tw implementation

State: closed
Opened: 2024-11-22T11:27:41Z
Closed: 2024-11-28T13:20:18Z
Merged: 2024-11-28T13:20:18Z
URL: https://github.com/dmwm/CRABServer/pull/8808

## Opening post (aspiringmind-code, 2024-11-22T11:27:41Z)

Implementation of canary TW for https://github.com/dmwm/CRABServer/issues/8806
Also see corresponding changes in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/292

## Comment (cmsdmwmbot, 2024-11-22T11:31:30Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2290/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-25T09:54:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2291/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T09:45:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2294/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T10:46:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2295/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T11:25:36Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2296/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T13:33:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2297/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T14:03:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2298/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-26T17:39:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2299/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-28T09:25:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2303/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-28T10:13:29Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2304/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-11-28T10:37:14Z)

@belforte Tested on preprod. See [task](https://cmsweb-testbed.cern.ch/crabserver/ui/task/241128_102130%3Avchakrav_crab_20241128_112126)
The task was submitted on crab-preprod-tw01
```
crab3@crab-preprod-tw01:/data/srv/TaskManager/logs$ grep -C 5 "vchakrav" twlog.txt
2024-11-28 11:21:58,387:INFO:MasterWorker,255:Starting external scheduling.
2024-11-28 11:21:58,471:INFO:TaskUtils,25:Retrieved a total of 1 WAITING tasks
2024-11-28 11:21:58,471:INFO:MasterWorker,314:
Username | Waiting | Selected
---------|---|--
vchakrav | 1 | 1
2024-11-28 11:21:58,472:INFO:TaskUtils,55:Will set to NEW task 241128_102130:vchakrav_crab_20241128_112126
2024-11-28 11:21:58,502:INFO:MasterWorker,352:Task 241128_102130:vchakrav_crab_20241128_112126 status updated to 'NEW'.
2024-11-28 11:21:58,502:INFO:MasterWorker,331:Pruning the queue if required...logic tbd
2024-11-28 11:21:58,502:INFO:MasterWorker,334:Report Queue status... logic tbd
2024-11-28 11:21:58,502:INFO:MasterWorker,574:Work selected successfully.
2024-11-28 11:21:58,622:INFO:MasterWorker,428:TW changed from crab-preprod-tw01 to crab-preprod-tw02 during runCanary
2024-11-28 11:21:58,709:DEBUG:Worker,253:Ready to inject 0 items
```
And the task ran on canary crab-preprod-tw02
```
2024-11-28 11:23:27,505:DEBUG:Worker,284:Completed work 14 on 241128_102130:vchakrav_crab_20241128_112126
2024-11-28 11:23:27,505:INFO:MasterWorker,579:This is canary TW crab-preprod-tw02 running.
```
For the test we had set canary_fraction as 1 so that it certainly goes to canary. It will be set to a small number like 0.05 by default in master TW config.

## Comment (belforte, 2024-11-28T11:07:32Z)

I suggest to put in preprod with at 30% fraction and on monday enable at low rate in prod

## Comment (aspiringmind-code, 2024-11-28T11:14:29Z)

Preprod set to 0.3 in [here](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/0b267773c0b684da0d9b2cdfdfb4b202fa946ed7) Ok to merge?

## Comment (cmsdmwmbot, 2024-11-28T12:13:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 67 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2305/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-11-28T13:15:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 58 comments to review
 * Pycodestyle check: succeeded
   * 65 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2306/artifact/artifacts/PullRequestReport.html
