# dmwm/CRABClient issue #5359: publication status not correctly reported for automatic splitting

State: closed
Opened: 2024-12-03T20:24:06Z
Closed: 2024-12-04T21:18:35Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5359

## Opening post (belforte, 2024-12-03T20:24:06Z)

`crab status` says : `No publication information available yet` 
```console
belforte@lxplus825/bot> crab status --instance prod --task 241203_105225:cmsbot_crab_20241203_115223
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_20241203_115223 folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_20241203_115223
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20241203_115223
Task name:			241203_105225:cmsbot_crab_20241203_115223
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-prod-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/241203_105225%3Acmsbot_crab_20241203_115223
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=241203_105225%3Acmsbot_crab_20241203_115223&from=1733219545000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_IT_Rome', 'T2_UK_SGrid_Bristol', 'T2_ES_IFCA']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	COMPLETED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/241203_105225:cmsbot_crab_20241203_115223/AutomaticSplitting/

Jobs status:                    finished     		100.0% (1/1)

Output dataset:			/GenericTTbar/cmsbot-autotest-1733223143-94ba0e06145abd65ccb1d21786dc7e1d/USER

No publication information available yet

Warning: the max jobs runtime is less than 30% of the task requested value (1250 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Summary of run jobs:
 * Memory: 70MB min, 973MB max, 974MB ave
 * Runtime: 0:03:01 min, 0:13:08 max, 0:13:08 ave
 * CPU eff: 78% min, 78% max, 78% ave
 * Waste: 0:03:54 (23% of total)

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20241203_115223/crab.log
belforte@lxplus825/bot> 

```

but output dataset as indicated in TaskDB is properly filled
https://cmsweb.cern.ch/das/request?instance=prod/phys03&input=file+dataset%3D%2FGenericTTbar%2Fcmsbot-autotest-1733223143-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER


I suspect that this is why StatusTracking Jenkins test still reports the test as `running`
https://github.com/dmwm/CRABServer/issues/8856#issuecomment-2515237877

## Comment (belforte, 2024-12-04T20:34:59Z)

the origin is that in that task one probe failed, so there are 5 probe jobs and only 5 jobs in "finished" (4 probes plus the processing one) therefore this condition fails
https://github.com/dmwm/CRABClient/blob/e5bc03c96cdd4c3f28b83e668773400e840b619b/src/python/CRABClient/Commands/status.py#L1037

## Comment (belforte, 2024-12-04T20:40:42Z)

should use a more robust logic looking at `jobList`  in `shortResult` dictionary
```
{'jobsPerStatus': {'finished': 5, 'failed': 1}, 'jobList': [['finished', '0-1'], ['finished', '0-4'], ['failed', '0-3'], ['finished', '0-5'], ['finished', '0-2'], ['finished', '1']], 'numProbes': 5, 'numUnpublishable': 0}
```
