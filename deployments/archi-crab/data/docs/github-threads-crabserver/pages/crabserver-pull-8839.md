# dmwm/CRABServer pull request #8839: clear PYTHONPATH before executing payload. Fix #8805

State: closed
Opened: 2024-11-26T17:53:03Z
Closed: 2024-11-26T18:05:14Z
Merged: 2024-11-26T18:05:14Z
URL: https://github.com/dmwm/CRABServer/pull/8839

## Opening post (belforte, 2024-11-26T17:53:03Z)

with this the job stdout has
```
==== Will execute unset PYTHONPATH; stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
```
and jobs submitted with /CMSSW_14_2_PY312_X_2024-11-20-2300 (via client v3.241125) work

## Comment (belforte, 2024-11-26T17:54:19Z)

submissions with current CMSSW works as well. Tested in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8595258

## Comment (cmsdmwmbot, 2024-11-26T17:57:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2300/artifact/artifacts/PullRequestReport.html
