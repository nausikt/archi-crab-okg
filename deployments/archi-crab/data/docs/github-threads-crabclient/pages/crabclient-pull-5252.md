# dmwm/CRABClient pull request #5252: add checkfile.py fix #5234

State: closed
Opened: 2023-11-22T22:57:12Z
Closed: 2023-11-27T13:36:32Z
Merged: 2023-11-27T13:36:32Z
URL: https://github.com/dmwm/CRABClient/pull/5252

## Opening post (belforte, 2023-11-22T22:57:12Z)

initial version. Works, but details of what is reported, how, and possibly other/different checks needs to be tuned based on experience.
E.g. I have put some `print` statements which make output prettied on console, but may be messy if this is used via python API. 

**N.B.** I have not tested `--instance` nor `--scope` options. I am not even sure `--scope` is useful

Ref: https://github.com/dmwm/CRABClient/issues/5234

## Comment (cmsdmwmbot, 2023-11-22T22:59:44Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 384 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1009/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T23:06:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 384 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1010/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T23:19:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 384 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1011/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-22T23:23:13Z)

@novicecpp I welcome advice on how to better structure this. I tried "my best" but in the end the "main" i.e. `__call__` seems too long and some method is maybe too short or should be removed. But do not spend too much time. Overall file length is average among other commands.

## Comment (cmsdmwmbot, 2023-11-22T23:28:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 384 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1012/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T23:32:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 380 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1013/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T23:37:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1014/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-22T23:40:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1015/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-24T18:42:39Z)

I think I have addresses all points. Feel free to review again.

## Comment (cmsdmwmbot, 2023-11-24T18:43:36Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1018/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-27T13:31:57Z)

I have rename `--scope` to `--rucio-scope` and moved renaming of `--instance` to #5253

## Comment (cmsdmwmbot, 2023-11-27T13:35:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1019/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-27T13:36:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1020/artifact/artifacts/PullRequestReport.html
