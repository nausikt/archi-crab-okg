# dmwm/CRABServer pull request #9044: Fix #8953

State: closed
Opened: 2025-04-14T09:51:54Z
Closed: 2025-04-14T13:11:25Z
Merged: 2025-04-14T13:11:25Z
URL: https://github.com/dmwm/CRABServer/pull/9044

## Opening post (aspiringmind-code, 2025-04-14T09:51:54Z)

Adding Psethash is done in a try-except block with two separate functions. For CMSSW releases 15_1_X and beyond, the FrameworkJobReport will be used whereas for earlier ones, existing method of using edmProvDump will be the default fallback. See #8953

## Comment (cmsdmwmbot, 2025-04-14T09:56:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 7 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2432/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-04-14T10:26:29Z)

Tested with **CMSSW_15_1_X_2025-04-13-0000** See [task](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=250414_100547%3Avchakrav_crab_20250414_120541&from=1744621548000&to=now)
```
==== Job Exit Code from FrameworkJobReport.xml and Application exit code: 0 ====
==== Checksum computation STARTING at Mon Apr 14 10:11:50 2025 UTC ====
==== Checksum FINISHED at Mon Apr 14 10:11:50 2025 UTC ====
== FileName: output.root  -  FileAdler32: d86dfeca- FileSize: 0.6160116195678711.3f MBytes
Extracted ParameterSetID (PSet Hash): 071187f715f3611227f78a9e9808f215
== Adding PSet Hash for filename: output.root
== Assigning PSet Hash 071187f715f3611227f78a9e9808f215 to output.root
== Execution site from site-local-config.xml: T1_UK_RAL
==== Report file creation FINISHED at Mon Apr 14 10:11:50 2025 UTC ====
==== CMSRunAnalysis.py FINISHED at Mon Apr 14 10:11:50 2025 UTC ====
```
 For CMSSW_13_0_2 See [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/11757355)

## Comment (belforte, 2025-04-14T11:58:14Z)

LGTM Thanks

## Comment (nausikt, 2025-04-14T13:09:47Z)

No objection!, Looks very thoughtful by catching missing attributes and errors beforehand everywhere, Thanks!

## Comment (aspiringmind-code, 2025-04-14T13:11:33Z)

Thanks, merged!
