# dmwm/CRABServer pull request #8969: Remove WMArchive

State: closed
Opened: 2025-03-07T11:07:12Z
Closed: 2025-03-10T11:17:23Z
Merged: 2025-03-10T11:17:23Z
URL: https://github.com/dmwm/CRABServer/pull/8969

## Opening post (aspiringmind-code, 2025-03-07T11:07:12Z)

Fix #8424
Tested with PostJob logs of task [250307_102825:vchakrav_crab_20250307_112819](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=250307_102825%3Avchakrav_crab_20250307_112819&from=1741339705000&to=now)

## Comment (cmsdmwmbot, 2025-03-07T11:11:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 370 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2393/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-07T16:31:22Z)

Very good. Thanks. Please check puppet side as well

## Comment (aspiringmind-code, 2025-03-10T11:20:13Z)

[MR](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/323) for Puppet side created
