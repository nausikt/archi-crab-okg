# dmwm/CRABServer issue #7857: TW should not issue misleading message when parent dataset is missing

State: closed
Opened: 2023-08-29T16:06:15Z
Closed: 2024-08-11T16:29:57Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7857

## Opening post (belforte, 2023-08-29T16:06:15Z)

see: https://cms-talk.web.cern.ch/t/crab-submit-fails-because-of-invalid-input-files/28833/7

TaskWorker fails with `Cannot find any valid file inside the dataset` and points to input dataset, while the message should refer to the parent dataset !

example:
```
belforte@lxplus805/ste> crab status 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20230829_180205
Task name:			230829_160227:belforte_crab_20230829_180205
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	QUEUED on command SUBMIT
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/230829_160227%3Abelforte_crab_20230829_180205
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230829_160227%3Abelforte_crab_20230829_180205&from=1693321347000&to=now
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20230829_180205/crab.log
belforte@lxplus805/ste> crab status 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20230829_180205
Task name:			230829_160227:belforte_crab_20230829_180205
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/230829_160227%3Abelforte_crab_20230829_180205
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230829_160227%3Abelforte_crab_20230829_180205&from=1693321347000&to=now
Failure message from server:	Cannot find any valid file inside the dataset. Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/MinBias_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD.
				Aborting submission. Resubmitting your task will not help.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20230829_180205/crab.log
belforte@lxplus805/ste> 
```

## Comment (belforte, 2024-08-11T16:02:19Z)

This is not a simple "parent dataset is not found in DBS", but it is when the user asked for `useParent` but the dataset files have no parents.

The check that fails is inside `formatOutput` 
https://github.com/dmwm/CRABServer/blob/414396a15bfa287ff00fbc9edcbc5417f4c342c3/src/python/TaskWorker/Actions/DataDiscovery.py#L44-L55
so all files are skipped and the `formatOutput` returns an empty list, which the caller can not tell apart from the case of "all files are invalid", which is more common and drove that message in DBSDataDiscovery.

There is no simple way to tell one situation from the other w/o altering code a lot given that it is all mixed: invalid files, files in block w/o location and files w/o parents.

Since this is really a corner use case, I will settle for improving the message.

## Comment (belforte, 2024-08-11T16:14:57Z)

message now is like this
```text
	You specified to accept a partial dataset, so all blocks
	 on disk will be processed even if only partially replicated
	All dataset files are either invalid or w/o location or w/o a parent.
	Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/MinBias_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD
	Aborting submission. Resubmitting your task will not help.

```
