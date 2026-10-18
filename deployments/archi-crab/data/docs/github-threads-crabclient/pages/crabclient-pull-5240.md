# dmwm/CRABClient pull request #5240: Add change dbs dataset file status fix #5204

State: closed
Opened: 2023-10-25T12:19:03Z
Closed: 2023-10-25T16:32:34Z
URL: https://github.com/dmwm/CRABClient/pull/5240

## Opening post (belforte, 2023-10-25T12:19:03Z)

I am creating this to allow people a peek at current code to give early feedback
There a few changes coming
1) rename commands  to set...status
2) remove --block for crab setfilestatus
3) try with a new option in HTTPRequest to force `-H "Content-type: application/json"` as per https://github.com/dmwm/dbs2go/blob/master/docs/Client.md#dbs-client
     * nope. I tried that with CLI `curl` and did not help https://github.com/dmwm/dbs2go/issues/102#issuecomment-1779163892

## Comment (cmsdmwmbot, 2023-10-25T12:23:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 27 comments to review
 * Pycodestyle check: succeeded
   * 411 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/956/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T13:30:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 28 comments to review
 * Pycodestyle check: succeeded
   * 401 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/957/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T13:43:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 28 comments to review
 * Pycodestyle check: succeeded
   * 401 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/958/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T14:20:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 64 comments to review
 * Pycodestyle check: succeeded
   * 411 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/959/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T14:30:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 64 comments to review
 * Pycodestyle check: succeeded
   * 411 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/960/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T15:21:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 411 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/961/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T15:25:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 411 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/962/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T16:15:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/963/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T16:16:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/964/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T16:17:39Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/965/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T16:25:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/966/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T16:27:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/967/artifact/artifacts/PullRequestReport.html
