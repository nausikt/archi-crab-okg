# dmwm/CRABServer pull request #8198: CMSRunAnalysis.py takes JSON file as arg Fix #8196

State: closed
Opened: 2024-01-30T17:09:33Z
Closed: 2024-01-30T17:26:04Z
Merged: 2024-01-30T17:26:04Z
URL: https://github.com/dmwm/CRABServer/pull/8198

## Opening post (belforte, 2024-01-30T17:09:33Z)

also small changes to CMSRunAnalysis.sh for compatibility and remove double conversion to JSON of `ScriptArgs` in DagmanCreator

## Comment (cmsdmwmbot, 2024-01-30T17:12:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 174 comments to review
 * Pycodestyle check: succeeded
   * 127 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1808/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-30T17:21:45Z)

too many pylint/pep-8 comments to fix. The only warning is the known one about optparse
