# dmwm/CRABServer issue #7575: must issue tape recall for non completely replicated blocks

State: closed
Opened: 2023-03-28T08:55:53Z
Closed: 2023-03-31T17:22:00Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7575

## Opening post (belforte, 2023-03-28T08:55:53Z)

if a block is only partially on disk. tape recall is not called [1].
Not even if `config.Data.inputBlocks` is used [2]

I can't make sense of log [2] though. Maybe production TW has not proper code ? Need to investigate


[1]
```
2023-03-28 10:33:41,192:INFO:DBSDataDiscovery:Data discovery with DBS
2023-03-28 10:33:41,192:INFO:DBSDataDiscovery:will connect to DBS at URL: https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader
2023-03-28 10:33:41,445:DEBUG:DBSDataDiscovery:Data discovery through <WMCore.Services.DBS.DBS3Reader.DBS3Reader object at 0x7f7c013b6790> for 230328_083302:belforte_crab_20230328_103258
2023-03-28 10:33:41,472:DEBUG:DBSDataDiscovery:Datablock from DBS: ['/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD#5bd32ed7-c409-4ec7-a1b6-0b228b76e414'] 
2023-03-28 10:33:41,473:INFO:DBSDataDiscovery:Looking up data location with Rucio in cms scope.
2023-03-28 10:33:41,507:DEBUG:DBSDataDiscovery:Dataset size in GBytes: 4769.417627349
2023-03-28 10:33:41,508:WARNING:DBSDataDiscovery:Some blocks are on TAPE only and will not be processed.
There is no automatic recall from tape for data tier 'GEN-SIM-DIGI-RAW-MINIAOD' if 'Data.inputBlocks' is not provided.
If you need the full dataset, contact Data Transfer team via cmstalk+computing-tools@dovecotmta.cern.ch
2023-03-28 10:33:42,102:DEBUG:DataDiscovery: Formatting data discovery output 
2023-03-28 10:33:42,110:WARNING:DataDiscovery:1 blocks will be skipped because are not completely replicated on DISK: ['/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD#5bd32ed7-c409-4ec7-a1b6-0b228b76e414']
2023-03-28 10:33:42,165:DEBUG:DataDiscovery:Tot events found: 0
2023-03-28 10:33:42,166:DEBUG:DataDiscovery:Tot lumis found: 0
2023-03-28 10:33:42,166:DEBUG:DataDiscovery:Duplicate lumis found: 0
2023-03-28 10:33:42,166:DEBUG:DataDiscovery:Tot files found: 0
2023-03-28 10:33:42,167:DEBUG:DataDiscovery:Starting to create compact lumilists for input dataset
2023-03-28 10:33:42,167:DEBUG:DataDiscovery:Finished to create compact lumilists for input dataset
2023-03-28 10:33:42,194:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 80, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 255, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 532, in executeInternal
    raise TaskWorkerException(("Cannot find any valid file inside the dataset. Please, check your dataset in DAS, %s.\n" +
TaskWorker.WorkerExceptions.TaskWorkerException: Cannot find any valid file inside the dataset. Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD.
Aborting submission. Resubmitting your task will not help.

2023-03-28 10:33:42,244:DEBUG:ServerUtilities:Will execute:
curl -f -v -X POST  -H "User-Agent: CRAB" -F "key=belforte/230328_083302:belforte_crab_20230328_103258/twlog" -F "AWSAccessKeyId=ab00fcc889f248c495d2875f15a3badb" -F "policy=eyJleHBpcmF0aW9uIjogIjIwMjMtMDMtMjhUMDk6MzM6NDJaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiY3JhYmNhY2hlX3Byb2QifSwgeyJrZXkiOiAiYmVsZm9ydGUvMjMwMzI4XzA4MzMwMjpiZWxmb3J0ZV9jcmFiXzIwMjMwMzI4XzEwMzI1OC90d2xvZyJ9XX0=" -F "signature=1ileA3wKecx1AFl1MA2Jp7kfyF4=" -F "file=@./logs/tasks/belforte/230328_083302:belforte_crab_20230328_103258.log" "https://s3.cern.ch/crabcache_prod"
2023-03-28 10:33:43,461:DEBUG:ServerUtilities:exitcode: 0
stdout: b''
2023-03-28 10:33:43,462:DEBUG:ServerUtilities:twlog ./logs/tasks/belforte/230328_083302:belforte_crab_20230328_103258.log successully uploaded to S3
2023-03-28 10:33:43,479:INFO:Worker:Uploading failure message to the REST:
Cannot find any valid file inside the dataset. Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD.
Aborting submission. Resubmitting your task will not help.
2023-03-28 10:33:43,577:INFO:Worker:Failure message successfully uploaded to the REST
2023-03-28 10:33:43,578:DEBUG:Worker:Process-5: SUBMIT work on 230328_083302:belforte_crab_20230328_103258 completed in 8 seconds: Status: ERROR
Error = Cannot find any valid file inside the dataset. Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD.
Aborting submission. Resubmitting your task will not help.

2023-03-28 10:33:43,633:DEBUG:Worker:RSS after finishing 230328_083302:belforte_crab_20230328_103258: b'291.227' MB

```

[2]
```
2023-03-28 10:47:15,594:INFO:DBSDataDiscovery:Data discovery with DBS
2023-03-28 10:47:15,596:INFO:DBSDataDiscovery:will connect to DBS at URL: https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader
2023-03-28 10:47:15,694:DEBUG:DBSDataDiscovery:Data discovery through <WMCore.Services.DBS.DBS3Reader.DBS3Reader object at 0x7f7c114af8e0> for 230328_084631:belforte_crab_20230328_104627
2023-03-28 10:47:15,718:DEBUG:DBSDataDiscovery:Datablock from DBS: ['/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD#5bd32ed7-c409-4ec7-a1b6-0b228b76e414'] 
2023-03-28 10:47:15,719:INFO:DBSDataDiscovery:Looking up data location with Rucio in cms scope.
2023-03-28 10:47:15,747:DEBUG:DBSDataDiscovery:Dataset size in GBytes: 4769.417627349
2023-03-28 10:47:15,747:WARNING:DBSDataDiscovery:Some blocks are on TAPE only and will not be processed.
There is no automatic recall from tape for data tier 'GEN-SIM-DIGI-RAW-MINIAOD' if 'Data.inputBlocks' is not provided.
If you need the full dataset, contact Data Transfer team via cmstalk+computing-tools@dovecotmta.cern.ch
2023-03-28 10:47:15,877:DEBUG:DataDiscovery: Formatting data discovery output 
2023-03-28 10:47:15,881:WARNING:DataDiscovery:1 blocks will be skipped because are not completely replicated on DISK: ['/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD#5bd32ed7-c409-4ec7-a1b6-0b228b76e414']
2023-03-28 10:47:15,931:DEBUG:DataDiscovery:Tot events found: 0
2023-03-28 10:47:15,931:DEBUG:DataDiscovery:Tot lumis found: 0
2023-03-28 10:47:15,931:DEBUG:DataDiscovery:Duplicate lumis found: 0
2023-03-28 10:47:15,931:DEBUG:DataDiscovery:Tot files found: 0
2023-03-28 10:47:15,932:DEBUG:DataDiscovery:Starting to create compact lumilists for input dataset
2023-03-28 10:47:15,932:DEBUG:DataDiscovery:Finished to create compact lumilists for input dataset
2023-03-28 10:47:15,944:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 80, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 255, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/slc7_amd64_gcc630/cms/crabtaskworker/v3.230221-933df59b9caab94e7e8dcf8de2e67f29/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 532, in executeInternal
    raise TaskWorkerException(("Cannot find any valid file inside the dataset. Please, check your dataset in DAS, %s.\n" +
TaskWorker.WorkerExceptions.TaskWorkerException: Cannot find any valid file inside the dataset. Please, check your dataset in DAS, https://cmsweb.cern.ch/das/request?instance=prod/global&input=dataset=/QCD_Pt-80To120_TuneCP5_14TeV-pythia8/PhaseIISpring22DRMiniAOD-PU200_123X_mcRun4_realistic_v11-v1/GEN-SIM-DIGI-RAW-MINIAOD.
Aborting submission. Resubmitting your task will not help.
```

## Comment (belforte, 2023-03-31T17:21:59Z)

this happened because the user was using a CRABClient version w/o support for `inputBlocks`. I verified that things work as expected when TW has the correct `tm_user_config':{'inputblocks':[...],...}`
