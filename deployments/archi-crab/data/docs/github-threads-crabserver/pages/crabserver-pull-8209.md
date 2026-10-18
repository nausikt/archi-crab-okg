# dmwm/CRABServer pull request #8209: only set a default for missing args. Fix #8208

State: closed
Opened: 2024-01-31T14:00:43Z
Closed: 2024-01-31T19:53:57Z
Merged: 2024-01-31T19:53:57Z
URL: https://github.com/dmwm/CRABServer/pull/8209

## Opening post (belforte, 2024-01-31T14:00:43Z)

(no text)

## Comment (cmsdmwmbot, 2024-01-31T14:03:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 82 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1814/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-01-31T15:08:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 55 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1815/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-31T15:10:30Z)

ready to merge, wait for Jenkins https://github.com/dmwm/CRABServer/issues/8211

## Comment (belforte, 2024-01-31T16:02:59Z)

number of events is now OK. But there are still failures
hint from job log
```
mv: cannot stat 'PSet.pkl-seeds': No such file or directory
```

error was introduced in the "fix pylint" step. Something wrong with f-string, likely

## Comment (cmsdmwmbot, 2024-01-31T16:36:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 55 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1816/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-31T19:52:37Z)

finally got successful CCV tests
- [x] #8212 
- [x] #8213
