# dmwm/CRABServer pull request #8562: Fixing PB entrypoint

State: closed
Opened: 2024-07-25T12:43:54Z
Closed: 2024-07-26T10:26:57Z
Merged: 2024-07-26T10:26:57Z
URL: https://github.com/dmwm/CRABServer/pull/8562

## Opening post (novicecpp, 2024-07-25T12:43:54Z)

Fix https://github.com/dmwm/CRABServer/issues/8561

## Comment (cmsdmwmbot, 2024-07-25T12:49:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 11 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2063/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-07-25T13:46:21Z)

Thanks for review Stefano.
Waiting for https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7820917 to finish.

## Comment (cmsdmwmbot, 2024-07-25T13:46:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 11 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2064/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-25T13:50:36Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 11 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2065/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-25T14:13:57Z)

I am looking at pylint errors.

## Comment (belforte, 2024-07-25T18:42:27Z)

1. due to "import confusion" pylint did not spot those issues until now. but issues are real bugs
2. those are only present in Publisher_Rucio and would only be triggered when something goes wrong, which never happens in our tests since we do same thing over and over
3. at this point it is better do it while also pursuing more commonality between pub_schedd and pub_rucio, i.e. changing things a bit
4. so I will make a PR in CRABServer repo to fix the bugs and then you can merge into your branch. Seems simpler than making a PR for your repository
