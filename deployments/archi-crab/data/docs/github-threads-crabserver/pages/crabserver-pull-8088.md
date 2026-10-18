# dmwm/CRABServer pull request #8088: PYPI proof-of-concept

State: closed
Opened: 2023-12-04T23:58:28Z
Closed: 2024-02-19T14:33:41Z
Merged: 2024-02-19T14:33:41Z
URL: https://github.com/dmwm/CRABServer/pull/8088

## Opening post (novicecpp, 2023-12-04T23:58:28Z)

Proof-of-concept of https://github.com/dmwm/CRABServer/issues/7560

Please see design choices https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1859531116 and walkthrough of both images https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1916881209 https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1923506222

## Comment (cmsdmwmbot, 2023-12-04T23:59:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1778/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-12-05T00:12:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1779/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-12-18T04:45:03Z)

@belforte let's go back to the issue in https://github.com/dmwm/CRABServer/issues/7560 and discuss there.
Will follow up later, after new year.

## Comment (novicecpp, 2023-12-23T02:55:15Z)

(Let me giving some quick reply that I have in my mind right now. I will provide in-detail answer later after I come back)

First of all, thanks for your comments. I really appreciate it.

- About the dependencies, I will fix the documentation.
- All scripts here should be independent from original copy and self-documents. I can add ref to the original file in separate docs, what you see now is the result of my bad documenting.
- I still think it is needed to go through Dockerfile and understand each step by yourself. Of course, it is my job to make it easier to read, I will fix that.
- The `build.sh` you want is described in https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1859531116 in *1. Building* section, please have a look. 
    - In summary, pull this PR, cd to git root dir, then simply run `docker build` command without passing any build args.

## Comment (cmsdmwmbot, 2024-01-30T13:45:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1807/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-02T12:54:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1823/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-09T15:11:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1826/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-02-09T15:29:09Z)

I need to test in devthree later.
But it should have no more changes unless a bug has been found.

## Comment (cmsdmwmbot, 2024-02-12T16:35:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1827/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-12T16:39:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 9 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1829/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-02-12T16:44:19Z)

@belforte @mapellidario PR is ready for review.
 All status tracking tests passed (running in devthree env).
```
240212_105438:tseethon_crab_20240212_115438
240212_105440:tseethon_crab_20240212_115439
240212_105441:tseethon_crab_20240212_115441
240212_105443:tseethon_crab_20240212_115443
240212_105447:tseethon_crab_20240212_115445
240212_105449:tseethon_crab_rucio_transfers_20240212_115448
240212_105451:tseethon_crab_rucio_transfers_group_20240212_115451
240212_105454:tseethon_crab_rucio_transfers_manyedm_nopublication_20240212_115452
240212_105457:tseethon_crab_rucio_transfers_nopublication_20240212_115455
240212_105500:tseethon_crab_rucio_transfers_withnoneedm_20240212_115458
240212_105502:tseethon_crab_rucio_transfers_withnoneedm_nopublication_20240212_115501'
```
For example, [240212_105441:tseethon_crab_20240212_115441](https://cmsweb-test12.cern.ch/crabserver/ui/task/240212_105443%3Atseethon_crab_20240212_115443) ([Grafana](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=tseethon&var-task=240212_105441%3Atseethon_crab_20240212_115441&from=1707731681000&to=now)).

## Comment (belforte, 2024-02-12T20:28:15Z)

sorry, I mixed single comments and review comments... sloppy clicking :-(

## Comment (belforte, 2024-02-12T20:47:00Z)

Thanks @novicecpp . I am done looking at this. I can not claim I really "reviewed" but since 1. it works 2. is new and will not break anything, I did not look for mistakes, only tried to have something that I can read an understand at least in broad terms.

## Comment (cmsdmwmbot, 2024-02-16T10:53:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 9 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1847/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-02-19T13:25:40Z)

@belforte @mapellidario may I merge this?

## Comment (belforte, 2024-02-19T13:53:53Z)

sorry for delayed action. Something new always happens here. Please go ahead

## Comment (novicecpp, 2024-02-19T14:33:32Z)

Thanks. Merging...
