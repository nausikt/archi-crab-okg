# dmwm/CRABServer issue #8178: Some publications fail when usign Rucio ASO

State: closed
Opened: 2024-01-12T14:46:31Z
Closed: 2024-01-15T08:26:28Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8178

## Opening post (belforte, 2024-01-12T14:46:31Z)

e.g.
```
belforte@lxplus800/bot> crab status -d crab_rucio_transfers_20240111_230331/
ruciBEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

o list-content Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_rucio_transfers_20240111_230331
Task name:			240111_220333:cmsbot_crab_rucio_transfers_20240111_230331
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/240111_220333%3Acmsbot_crab_rucio_transfers_20240111_230331
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240111_220333%3Acmsbot_crab_rucio_transfers_20240111_230331&from=1705007013000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_London_Brunel', 'T2_ES_IFCA']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (40/40)

Transfer container's name:	/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d_TRANSFER.c705f90a/USER
Transfer container's rule:	https://cms-rucio-webui.cern.ch/rule?rule_id=815ecfc60ffa4185bc6a2fbe180ebeac

Tips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 

Publication status of 1 dataset(s):	done         		 35.0% (14/40)
(from CRAB internal bookkeeping in transferdb)
					failed       		 65.0% (26/40)

Output dataset:			/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER
Output dataset DAS URL:		https://cmsweb.cern.ch/das/request?input=%2FGenericTTbar%2Fcmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER&instance=prod%2Fphys03
Publish container's rule:	https://cms-rucio-webui.cern.ch/rule?rule_id=f8e9c9b33cf74722b537a31e3fb9aa97

Warning: the max jobs runtime is less than 30% of the task requested value (60 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 36MB min, 892MB max, 256MB ave
 * Runtime: 0:02:18 min, 0:04:33 max, 0:02:53 ave
 * CPU eff: 0% min, 14% max, 5% ave
 * Waste: 2:36:59 (58% of total)

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_rucio_transfers_20240111_230331/crab.log
belforte@lxplus800/bot> 
```

looking at log in Publisher_rucio (running v3.240111) I find and attempt to create twili the same block

```
2024-01-11 23:59:49,119:INFO: Found 16 files not already present in DBS which will be published.
2024-01-11 23:59:49,197:ERROR: Error when publishing /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664
2024-01-11 23:59:49,202:ERROR: FAILING BLOCK DUE TO HTTP Error 400: DBSError Code:128 Description:Not defined Function:dbs.bulkblocks.checkBlockExist Message:Block /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664 already exists Error: nil SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1705013989.1971571.txt
```

## Comment (belforte, 2024-01-12T15:50:36Z)

hmmm...
the Publisher log has no record of having created that block
```

[crab3@crab-preprod-tw01 cmsbot]$ cat 240111_220333:cmsbot_crab_rucio_transfers_20240111_230331.log|grep d1be98c93664
2024-01-11 23:59:49,197:ERROR: Error when publishing /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664
2024-01-11 23:59:49,202:ERROR: FAILING BLOCK DUE TO HTTP Error 400: DBSError Code:128 Description:Not defined Function:dbs.bulkblocks.checkBlockExist Message:Block /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664 already exists Error: nil SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1705013989.1971571.txt
2024-01-11 23:59:49,202:ERROR: Publish FAIL for Block: /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664
[crab3@crab-preprod-tw01 cmsbot]$ 
```

and it is not listed by Rucio in the publish container for that task

```
belforte@lxplus800/bot> rucio list-content user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER
+---------------------------------------------------------------------------------------------------------------------------------------+--------------+
| SCOPE:NAME                                                                                                                            | [DID TYPE]   |
|---------------------------------------------------------------------------------------------------------------------------------------+--------------|
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#22f42cc2-8958-44d6-a769-49e88dcc4b6e | DATASET      |
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#2e6516a0-344e-45d9-9be3-97abb5c6dcb6 | DATASET      |
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#364986df-a3fd-4d2a-9337-a4fcdb9d69c8 | DATASET      |
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#56ef1584-ba2c-4a6d-afd6-f12e71c82cb4 | DATASET      |
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#c1adb992-85ea-48a6-8dc5-f0fccbebd744 | DATASET      |
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664 | DATASET      |
+---------------------------------------------------------------------------------------------------------------------------------------+--------------+
belforte@lxplus800/bot> 
```
maybe was created in a different task ?

the block is there in Rucio
```
ot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| SCOPE:NAME                                                                                                                            | [DID TYPE]      |
|---------------------------------------------------------------------------------------------------------------------------------------+-----------------|
| user.cmsbot:/GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#d0f6fa30-af6f-41ba-98b5-d1be98c93664 | DIDType.DATASET |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------+
belforte@lxplus800/bot> 
```

hmm...
block info info in DBS https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fphys03&input=%2FGenericTTbar%2Fcmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER%23d0f6fa30-af6f-41ba-98b5-d1be98c93664
indicates that it was created on `Thu Jan 11 23:39:01 CET 2024` , twenty minutes before the failure message.

## Comment (belforte, 2024-01-12T15:59:21Z)

but the log indicates that publication work on that task started at 23:59 !
```
[crab3@crab-preprod-tw01 cmsbot]$ head 240111_220333:cmsbot_crab_rucio_transfers_20240111_230331.log
2024-01-11 23:59:48,101:INFO: Start new iteration on taskname:  240111_220333:cmsbot_crab_rucio_transfers_20240111_230331
Get files to publish
2024-01-11 23:59:48,101:INFO: Will connect to CRAB service: preprod
```

Puzzling.

Same result looking at the publisher subprocess which deal with this task
```
[crab3@crab-preprod-tw01 processes]$ cat proc.c3id_240111_220333:cmsbot_crab_rucio_transfers_20240111_230331.txt
2024-01-11 23:59:47,394:INFO:slave:Process 240111_220333:cmsbot_crab_rucio_transfers_20240111_230331 is starting. PID 114
2024-01-11 23:59:47,806:INFO:slave:Got filemetadata for 32 LFNs
2024-01-11 23:59:47,821:INFO:slave:Now execute: python3 /data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/crabtaskworker/v3.240111-ac252900ca96a6784d9e561ca231c954/lib/python3.8/site-packages/Publisher/TaskPublishRucio.py --configFile=/data/srv/Publisher/PublisherConfig.py --taskname=240111_220333:cmsbot_crab_rucio_transfers_20240111_230331
2024-01-11 23:59:50,818:INFO:slave:TaskPublishScript done : b"DBS Server error: [{'error': {'reason': 'nil', 'message': 'Block /GenericTTbar/cmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d/USER#22f42cc2-8958-44d6-a769-49e88dcc4b6e already exists',
```

that one is the only suprocess for this task
```
[crab3@crab-preprod-tw01 processes]$ pwd
/data/srv/Publisher/logs/processes
[crab3@crab-preprod-tw01 processes]$ ls -l *240111_220333*
-rw-r--r--. 1 crab3 crab3 7097 Jan 12 00:59 proc.c3id_240111_220333:cmsbot_crab_rucio_transfers_20240111_230331.txt
[crab3@crab-preprod-tw01 processes]$ 
```

## Comment (belforte, 2024-01-12T16:03:56Z)

also in main log first occurrence of that task is at 23:59
```
[crab3@crab-preprod-tw01 logs]$ grep 240111_220333 log.txt.2024-01-11
2024-01-11 23:59:47,387:INFO:PublisherMasterRucio,373:acquired_files:   OK    32 : 240111_220333:cmsbot_crab_rucio_transfers_20240111_230331
```

Publisher was started just a bit before 23:00 so there is no possible contamination by Publisher's restarts either
```
log.txt.2024-01-11:2024-01-11 22:59:46,803:INFO:PublisherMasterRucio,150:PUBSTART: {"version": "v3.240111", "asoworker": "rucio", "instance": "preprod", "max_slaves": 5, "DBShost": "cmsweb-prod.cern.ch", "dryRun": false}
```

## Comment (belforte, 2024-01-12T16:06:44Z)

OH MY, I think I got it.
looking better in DBS via DAS: https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fphys03&input=%2FGenericTTbar%2Fcmsbot-ruciotransfers-1705010611-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER%23d0f6fa30-af6f-41ba-98b5-d1be98c93664
the block was created by the publisher in a  test VM: `create_by:"/DC=ch/DC=cern/OU=computers/CN=tw/crab-dev-tw02.cern.ch"`

We are running two publishers which point to same DB, they are likely getting confused.
I would think that we should be protected against this, but... never tested, likely to fail !

I will stop the publisher in `crab-dev-tw02` and try again.

![image](https://github.com/dmwm/CRABServer/assets/1837785/6ee4dc0e-fec8-49ff-9218-3534c41ed8be)

## Comment (belforte, 2024-01-15T08:26:28Z)

Yeah. the problem was two publishers running at same time.
