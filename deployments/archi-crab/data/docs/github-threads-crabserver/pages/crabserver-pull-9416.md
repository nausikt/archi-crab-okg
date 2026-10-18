# dmwm/CRABServer pull request #9416: avoid races in handling tooManyASOErrors fix #9408 fix #9403

State: closed
Opened: 2026-09-09T20:00:34Z
Closed: 2026-09-14T12:50:11Z
Merged: 2026-09-14T12:50:10Z
URL: https://github.com/dmwm/CRABServer/pull/9416

## Opening post (belforte, 2026-09-09T20:00:34Z)

this will hopefully close the "too many ASO error" saga.

Code to deal with those should hopefully be a template for the implementation of #9402 hopefully leading to a common, cleaner, leaner solution.

I tried to be general already e.g. CRAB_ForcefullyTerminated allows for more reasons besides "ASO", same for `tagAllJobsInTask()` and `killThisTask()`.

There may be some un-needed lock files now as well.

## Comment (cmsdmwmbot, 2026-09-09T20:04:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 292 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2918/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-09-09T20:56:24Z)

test task with this code
https://cmsweb-test2.cern.ch/crabserver/ui/task/260909_200903%3Abelforte_crab_20260909_220901

<strike> rats... there's regression from my previous test in https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=260909_200238:belforte_crab_20260909_220236&from=2026-09-09T12:01:28.000Z&to=now&timezone=utc&var-site=$__all&var-schedd=059&var-cmsUserId=&var-task_str=belforte_crab_20260909_220236&var-status=$__all&var-crabid=$__all&var-Filters=&var-rest_host=https:%2F%2Fcmsweb.cern.ch

need more work :-( </strike>

I wrote too soon. After some 15min data have been updated in OS and now everything is as it should be in
[task dashboard](https://monit-grafana.cern.ch/goto/cfxrufvkvkjr4b?orgId=11) and [OS](https://monit-opensearch.cern.ch/dashboards/goto/90554682e93e89ad1f1ebc8d2252d796)

See note [1.2] in https://github.com/dmwm/CRABServer/issues/9408#issuecomment-5540717492 for proper reading of OS values

## Comment (belforte, 2026-09-14T12:50:00Z)

thanks @nausikt . There are some un-necessary locks, but we can cleanup when adding code for #9402
