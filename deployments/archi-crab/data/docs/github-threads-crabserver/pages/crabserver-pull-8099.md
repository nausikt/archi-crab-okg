# dmwm/CRABServer pull request #8099: raise exception if ARCH does not map to OS. For #8098

State: closed
Opened: 2023-12-14T17:12:07Z
Closed: 2023-12-20T13:02:46Z
Merged: 2023-12-20T13:02:46Z
URL: https://github.com/dmwm/CRABServer/pull/8099

## Opening post (belforte, 2023-12-14T17:12:07Z)

with this PR in crab-dev-tw01:
```
belforte@lxplus936/EL9> crab status -d ./crab_20231214_180639 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/EL9/crab_20231214_180639
Task name:			231214_170642:belforte_crab_20231214_180639
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/231214_170642%3Abelforte_crab_20231214_180639
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=231214_170642%3Abelforte_crab_20231214_180639&from=1702570002000&to=now
Failure message from server:	Unsupported architecture el9
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/EL9/crab_20231214_180639/crab.log
belforte@lxplus936/EL9> 
```
instead of the run time failure reported in https://cms-talk.web.cern.ch/t/jobs-failing-with-exit-code-10040/32699

## Comment (cmsdmwmbot, 2023-12-14T17:16:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 121 comments to review
 * Pycodestyle check: succeeded
   * 129 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1786/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-12-14T18:17:36Z)

there are too many pylint complains to make me feel like trying to reduce them :-(

## Comment (belforte, 2023-12-19T21:58:37Z)

@mapellidario ping. Let me know if you do not have time for this.

## Comment (belforte, 2023-12-20T13:02:40Z)

thanks Dario. I agree that should be very safe, but whenever possible/sensible I think it is always good that another pair of eyes have a look.
