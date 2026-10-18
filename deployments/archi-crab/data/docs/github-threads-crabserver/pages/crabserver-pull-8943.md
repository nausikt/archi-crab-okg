# dmwm/CRABServer pull request #8943: Enabling CRIC-related sites checking functionalities on TaskWorker.

State: closed
Opened: 2025-02-26T00:55:18Z
Closed: 2025-04-02T08:26:41Z
URL: https://github.com/dmwm/CRABServer/pull/8943

## Opening post (nausikt, 2025-02-26T00:55:18Z)

Fix #6917 This is the first PR of Splitted #8937.
- [x] Enabling CRIC-related sites checking functionalities on **TaskWorker**.
- [ ] Decommissioning CRIC-related sites checking functionalities on **CRABServer**.

enabling of _expandSites, _checkSites and _checkASODestination functionalities on TaskWorker. Suppressing CRIC service debugging log and also utilizing WMCore's Service cache mechanism by enabling usestalecache. 

N.B. Apologize for the unintentional PEP8-style compliant enforcement by my IDE's automatic formatter. please, let me know whether it's unacceptable or tolerable. Thanks!

## Comment (cmsdmwmbot, 2025-02-26T01:00:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 1 warnings
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 358 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2384/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-02-26T01:40:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 1 warnings
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 358 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2385/artifact/artifacts/PullRequestReport.html
