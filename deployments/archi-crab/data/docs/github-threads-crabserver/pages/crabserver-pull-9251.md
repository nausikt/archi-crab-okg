# dmwm/CRABServer pull request #9251: [Draft] Support floor Py3.9 - Py3.12 up-to Py3.13 on Alma9 and Debian Trixie, WMCore 2.4.5.2 (wmfreeze) compatible

State: closed
Opened: 2025-12-18T16:49:15Z
Closed: 2026-03-03T17:12:58Z
Labels: PR: do not merge
URL: https://github.com/dmwm/CRABServer/pull/9251

## Opening post (nausikt, 2025-12-18T16:49:15Z)

This is `DO NOT MERGE` draft PR, an all-in-one PR for testing.
*P.S. [Ordinary Task](https://cmsweb-test14.cern.ch/crabserver/ui/task/251217_111001%3Akphornsi_crab_test14-CMSSW_16_py312-testing) and [Automatic Splitting Task](https://cmsweb-test14.cern.ch/crabserver/ui/task/251217_113451%3Akphornsi_crab_test14-automatic-splitting-CMSSW-16-py312-compatible) were tested on `CMSSW_16_0_PY312_X_2025-12-16-2300`, also regression tests via pipeline [here](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13614503)* to address #8956, #9150, #8804,

Please, see detail in upcoming write-up/comment in #8956.

## Comment (cmsdmwmbot, 2025-12-18T16:54:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 5 warnings
   * 236 comments to review
 * Pycodestyle check: succeeded
   * 194 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2709/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-03-03T17:12:59Z)

This could be closed as well, since we have succeed lifting with lot of image refactoring in https://github.com/dmwm/CRABServer/pull/9265.
