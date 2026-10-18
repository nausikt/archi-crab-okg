# dmwm/CRABServer issue #8140: tape recall fails when using inputBlocks

State: closed
Opened: 2024-01-05T11:11:55Z
Closed: 2024-01-11T15:31:40Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8140

## Opening post (belforte, 2024-01-05T11:11:55Z)

as reported in
https://cms-talk.web.cern.ch/t/rucio-exception-creating-container/33001/3

failure is
```
2024-01-03 17:56:19,929:INFO:RucioUtils:Initializing native Rucio client
2024-01-03 17:56:19,929:DEBUG:RucioUtils:Using cert [/data/certs/robotcert.pem]
 and key [/data/certs/robotkey.pem] for rucio client.
2024-01-03 17:56:19,942:INFO:RucioUtils:Rucio server v.32.6.0 contacted
2024-01-03 17:56:19,958:INFO:RucioUtils:Rucio client initialized for crab_tape_recall in status ACTIVE
2024-01-03 17:56:19,958:INFO:RucioActions:Total size of data to recall : 5 TBytes
2024-01-03 17:56:19,958:INFO:RucioActions:Create Rucio container /TapeRecall/240103_165439.rchudasa_crab_Tau_Run2018D_RAW-AOD/USER
2024-01-03 17:56:19,959:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.231215-79f791a1c915cc44ddd0729bbad60a1f/slc7_amd64_gcc630/cms/crabtaskworker/v3.231215-79f791a1c915cc44ddd0729bbad60a1f/lib/python3.8/site-packages/TaskWorker/Actions/RucioActions.py", line 46, in makeContainerFromBlockList
    rucio.add_container(scope, containerName)
AttributeError: 'NoneType' object has no attribute 'add_container'
```

affected task https://cmsweb.cern.ch/crabserver/ui/task/240103_165439%3Archudasa_crab_Tau_Run2018D_RAW-AOD
on crab-prod-tw01 running `crabtaskworker:v3.231215 `

here's  crabConfig to reproduce
```
from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'Tau_Run2018D_RAW-AODv2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'recoskim_Run2018D_Tau.py'
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores=8

#config.section_('Data')
#config.Data.userInputFiles = open('data_TauRAWD_filelist.txt').readlines()
config.Data.inputDataset ='/Tau/Run2018D-v1/RAW'  
config.Data.inputBlocks = [
    '/Tau/Run2018D-v1/RAW#04b58dd0-bfca-43b8-99b6-5060a84112f9',
    '/Tau/Run2018D-v1/RAW#0a94f4be-26b1-4451-953f-150656b5d522',
    '/Tau/Run2018D-v1/RAW#13acc5e3-6145-41d0-a416-b0b303fabce2',
]
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
#config.Data.outputPrimaryDataset = 'Tau_Run2018D_AOD'

config.Data.runRange = '314472-325175'
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/Tau_Run2018D-v1_AOD'
config.Data.publication = True
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
```

## Comment (belforte, 2024-01-05T11:22:21Z)

bug seems clear

this line
https://github.com/dmwm/CRABServer/blob/5a8a2aab15b1fc5393f51640425958a8ccd00b63/src/python/TaskWorker/Actions/RucioActions.py#L202
should rather be like this one
https://github.com/dmwm/CRABServer/blob/5a8a2aab15b1fc5393f51640425958a8ccd00b63/src/python/TaskWorker/Actions/RucioActions.py#L258-L260
so to be compatible with
https://github.com/dmwm/CRABServer/blob/5a8a2aab15b1fc5393f51640425958a8ccd00b63/src/python/TaskWorker/Actions/RucioActions.py#L37

## Comment (belforte, 2024-01-10T17:32:26Z)

A better solution is to remove `rucio=` from the arguments and instead use internally `self.rucioClient`

## Comment (belforte, 2024-01-10T20:21:09Z)

tested https://github.com/belforte/CRABServer/commit/309df0c1bfd9785cf466dbf58916b9ec0ddacf98 on crab-preprod-tw01 via `run from GH` using https://github.com/belforte/CRABServer/tree/fix-tape-recall-with-inputblocks and tape recall request was properly submitted https://cms-rucio-webui.cern.ch/rule?rule_id=6a1fa13254644de694119887a841b0be
