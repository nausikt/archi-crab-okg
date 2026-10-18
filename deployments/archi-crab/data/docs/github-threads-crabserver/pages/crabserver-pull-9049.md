# dmwm/CRABServer pull request #9049: Use new cache status

State: closed
Opened: 2025-04-16T15:36:02Z
Closed: 2025-04-23T10:21:10Z
Merged: 2025-04-23T10:21:10Z
URL: https://github.com/dmwm/CRABServer/pull/9049

## Opening post (belforte, 2025-04-16T15:36:02Z)

switch in as default what was `cache_status_new.py` while still running the old one and running comparison.

## Comment (cmsdmwmbot, 2025-04-16T15:38:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2436/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-16T15:40:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2437/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-16T15:48:35Z)

about Jenkins:
- I know that code in  `collapseDAGStatus` is not final: #9048 
- `Compare.py` is going to be removed

## Comment (belforte, 2025-04-16T16:01:18Z)

@aspiringmind-code I like that every PR gets a second set of eye to look at it. But am afraid that reviewing this is hard, at least the way differences are shown here makes little sense. GH decided to compare `cache_status_old.py` with previous cache_status_new.py while it should better be identical to previous `cache_status.py` other than renaming output and log files. I have confirmed this with retrieving files from GH.
So feel free to skip over this.

## Comment (cmsdmwmbot, 2025-04-17T09:41:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2438/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-17T10:34:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2439/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-17T15:00:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2440/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-23T10:00:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2441/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-23T10:08:29Z)

@aspiringmind-code  I have worked a bit on comments in the source and squashed commits. Do you want to read things, or may I merge and put in canary ?

## Comment (aspiringmind-code, 2025-04-23T10:10:25Z)

Hi, I have read the comments. Please feel free to merge and put in canary. Thanks!

## Comment (belforte, 2025-04-23T10:21:00Z)

thanks @aspiringmind-code
