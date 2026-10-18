# dmwm/CRABServer pull request #7792: refactor getCentralConfig Fix #7758

State: closed
Opened: 2023-08-02T17:55:03Z
Closed: 2023-08-08T15:36:34Z
Merged: 2023-08-08T15:36:34Z
URL: https://github.com/dmwm/CRABServer/pull/7792

## Opening post (belforte, 2023-08-02T17:55:03Z)

(no text)

## Comment (belforte, 2023-08-02T17:56:34Z)

Dario, this looks larger than needed, simply because I also took this chance to remove the "below 'if' condition is only added for the transition period " since that transition period ended about 2y ago !

## Comment (cmsdmwmbot, 2023-08-02T17:58:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 1 warnings
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1639/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-03T14:59:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1640/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-03T15:25:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1641/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-07T15:18:00Z)

did you test yourself again? Since last time you spotted a problem which I missed... I'd rather not trust myself alone !
