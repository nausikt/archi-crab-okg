# dmwm/CRABServer pull request #8844: better separation of WM/CMSSW python. Fix #8805

State: closed
Opened: 2024-11-27T17:42:24Z
Closed: 2024-11-27T20:13:43Z
Merged: 2024-11-27T20:13:43Z
URL: https://github.com/dmwm/CRABServer/pull/8844

## Opening post (belforte, 2024-11-27T17:42:24Z)

(no text)

## Comment (cmsdmwmbot, 2024-11-27T17:45:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2302/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-11-27T17:46:34Z)

validation
- [x] dev pipeline on test2 (with CMSSW_13) : https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8609440
- [x] py3.12 and current TW (should fail): https://cmsweb.cern.ch/crabserver/ui/task/241127_171230%3Abelforte_crab_20241127_181226
- [x] py3.12 and new TW on test2 (should work): https://cmsweb-test2.cern.ch/crabserver/ui/task/241127_171247%3Abelforte_crab_20241127_181243
- [x] https://github.com/dmwm/CRABServer/issues/8843
- [x] https://github.com/dmwm/CRABServer/issues/8842
- [x] https://github.com/dmwm/CRABServer/issues/8841
- [x] https://github.com/dmwm/CRABServer/issues/8845
- [x] https://github.com/dmwm/CRABServer/issues/8847
- [x] https://github.com/dmwm/CRABServer/issues/8846
- [x] https://github.com/dmwm/CRABServer/issues/8848
- [x] https://github.com/dmwm/CRABServer/issues/8849
- [x] https://github.com/dmwm/CRABServer/issues/8850
