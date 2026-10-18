# dmwm/CRABServer pull request #7597: do not recall across Atlantic. Fix #7589

State: closed
Opened: 2023-04-14T09:57:35Z
Closed: 2023-04-14T12:50:39Z
Merged: 2023-04-14T12:50:39Z
URL: https://github.com/dmwm/CRABServer/pull/7597

## Opening post (belforte, 2023-04-14T09:57:35Z)

(no text)

## Comment (cmsdmwmbot, 2023-04-14T10:03:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1490/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-04-14T10:10:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1491/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-04-14T11:53:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1492/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-04-14T12:32:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1493/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-14T12:44:14Z)

> using the set complement operator is a nice touch :)

no, no ! AFAIK that's not a python operator. That's the way RUcio wants the RSE Expressions to be written !
" The syntactic functionality of the Rucio RSE Expressions Parser allows the basic operations defined in mathematical set theory "
I had to look up thing s in google to figure out what "set complement" mean ! 
Should I improve the comment ?

## Comment (belforte, 2023-04-14T12:46:02Z)

what about
```python
   ALL_RSES += "\country=US\country=BR"  # Rucio wants the set complement operator \
```

## Comment (belforte, 2023-04-14T12:51:23Z)

I need to leave for a while now. So I merged. We can still change before tagging
