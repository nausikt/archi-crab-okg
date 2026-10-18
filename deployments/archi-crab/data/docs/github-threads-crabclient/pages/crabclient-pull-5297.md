# dmwm/CRABClient pull request #5297: Add suffix uuid string to filename and subdir

State: closed
Opened: 2024-03-07T11:18:35Z
Closed: 2024-03-07T13:36:35Z
Merged: 2024-03-07T13:36:35Z
URL: https://github.com/dmwm/CRABClient/pull/5297

## Opening post (novicecpp, 2024-03-07T11:18:35Z)

Fix https://github.com/dmwm/CRABClient/issues/5296

Need to add suffix uuid to both `self.filename` and `self.subdir` because we also test deleting directory.

Tested manually on el7 CMSSW_10_6_40 and el8 CMSSW_13_0_2.
(Did not test on slc6 because there is no `checkwrite` in command list of CV)

## Comment (cmsdmwmbot, 2024-03-07T11:36:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 2 warnings
   * 63 comments to review
 * Pycodestyle check: succeeded
   * 40 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1053/artifact/artifacts/PullRequestReport.html
