# dmwm/CRABServer pull request #8233: handle RSE not found in getWritePfn fix #7107 fix #8230

State: closed
Opened: 2024-02-12T16:33:27Z
Closed: 2024-02-13T15:31:25Z
Merged: 2024-02-13T15:31:25Z
URL: https://github.com/dmwm/CRABServer/pull/8233

## Opening post (belforte, 2024-02-12T16:33:27Z)

(no text)

## Comment (cmsdmwmbot, 2024-02-12T16:35:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1828/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-02-12T16:54:53Z)

tested on crab-dev-tw01. Now crab status prints
```txt
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240212_173308
Task name:			240212_163314:belforte_crab_20240212_173308
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240212_163314%3Abelforte_crab_20240212_173308
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=240212_163314%3Abelforte_crab_20240212_173308&from=1707751994000&to=now
Failure message from server:	Site T2_CH_CERNBOX not found in CMS site list
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240212_173308/crab.log
belforte@lxplus806/TC3> 


```

## Comment (cmsdmwmbot, 2024-02-12T16:55:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1830/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-12T17:11:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1831/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-02-12T17:15:20Z)

rebased and ready for merging

## Comment (cmsdmwmbot, 2024-02-12T17:18:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1832/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-13T12:17:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1837/artifact/artifacts/PullRequestReport.html
