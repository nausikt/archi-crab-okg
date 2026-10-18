# dmwm/CRABServer pull request #8860: Add support for microarch 8855

State: closed
Opened: 2024-12-11T16:39:08Z
Closed: 2024-12-11T17:30:26Z
Merged: 2024-12-11T17:30:26Z
URL: https://github.com/dmwm/CRABServer/pull/8860

## Opening post (belforte, 2024-12-11T16:39:08Z)

fix #8855 

adds to job submission JDL's a line like:
```
+REQUIRED_MINIMUM_MICROARCH = "x86-64-v3"
```

* CI validation: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/9587340
* test specific for the change: https://cmsweb-test2.cern.ch/crabserver/ui/task/241211_155400%3Abelforte_crab_20241211_165356

## Comment (cmsdmwmbot, 2024-12-11T16:44:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 9 warnings
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 662 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2310/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-12-11T17:23:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 9 warnings
   * 110 comments to review
 * Pycodestyle check: succeeded
   * 662 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2311/artifact/artifacts/PullRequestReport.html
