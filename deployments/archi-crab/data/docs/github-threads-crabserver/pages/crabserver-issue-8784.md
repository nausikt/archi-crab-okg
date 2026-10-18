# dmwm/CRABServer issue #8784: submission is broken when asking for GPU

State: closed
Opened: 2024-11-12T20:11:44Z
Closed: 2024-11-15T10:23:09Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8784

## Opening post (belforte, 2024-11-12T20:11:44Z)

see https://cms-talk.web.cern.ch/t/crab-jobs-requesting-gpu-stay-idle-forever/61932/1

The problem is that the initial dag bootstrap job submitted to scheduler universe requires one GPU.

Need to convert "Request_GPUs" to "CRAB_Request_GPUs".

```console
belforte@vocms0199/~> condor_q 72591015 -af crab_reqname jobuniverse RequestGPUs RequiresGPU
241112_124253:alherrer_crab_gpu_test_job 7 1 1
belforte@vocms0199/~> condor_q 72591015 -l |grep "Requirements ="
Requirements = (true) && (TARGET.Arch == "X86_64") && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) && (TARGET.GPUs >= RequestGPUs)
belforte@vocms0199/~> 
```

so the dag boostrap stay idle forever

## Comment (belforte, 2024-11-12T20:26:47Z)

https://github.com/dmwm/CRABServer/blob/95ce26a579c755b807235a6a7a344217f427a8d6/src/python/TaskWorker/Actions/DagmanCreator.py#L521

## Comment (belforte, 2024-11-12T20:33:13Z)

note this
https://github.com/dmwm/CRABServer/issues/6989#issuecomment-1253964599

maybe we need to keep `Request_GPUs` in the `Job.submit` file but make sure it does not go in the dagboostrap submission
Not sure about `RequiresGPU`.

## Comment (belforte, 2024-11-12T20:39:57Z)

maybe all of this is useless
https://github.com/dmwm/CRABServer/blob/95ce26a579c755b807235a6a7a344217f427a8d6/src/python/TaskWorker/Actions/DagmanSubmitter.py#L96-L109

Note this !
https://github.com/dmwm/CRABServer/blob/95ce26a579c755b807235a6a7a344217f427a8d6/src/python/TaskWorker/Actions/DagmanSubmitter.py#L31-L35

Lack of cleanup strikes back :-(

## Comment (belforte, 2024-11-13T15:02:46Z)

for reference, here's the user's config file
```python
config = config()

# General settings
config.General.requestName = 'gpu_test_job'
config.General.workArea = 'testcrabgpu_nov12_1'
config.General.transferOutputs = True
config.General.transferLogs = True

# JobType settings
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'PSet.py'  
config.JobType.allowUndistributedCMSSW = True 
config.JobType.scriptExe = './run_job.sh'  # Shell script that runs the Python job
config.JobType.inputFiles = ['gpu_test.py', 'run_job.sh', 'FrameworkJobReport.xml']  # Include Python code and shell script

config.JobType.outputFiles = ['gpu_output.txt']  # Expected output file

config.JobType.maxMemoryMB = 2000 
config.JobType.maxJobRuntimeMin = 100  

config.Data.outputPrimaryDataset = 'GPU_Test_Dataset'
config.Data.splitting = 'EventBased'  # Splitting type for non-CMSSW jobs
config.Data.unitsPerJob = 1  
config.Data.totalUnits = 1  
#config.Data.outLFNDirBase = '/store/user/aherrera'  # Output directory for job results
config.Data.publication = False 
#config.Data.secondaryInputFiles = ['root://cmseos.fnal.gov//store/user/aherrera/JOBMERGED/ttboosted/ttboosted_01/tt_jj0p5.root']

# Site settings
config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.whitelist = ['T2_US_Caltech', 'T2_US_Florida', 'T2_US_Purdue', 'T2_US_Wisconsin']
config.Site.requireAccelerator = True  # Specify supports GPUs

```

## Comment (belforte, 2024-11-15T09:28:42Z)

removing the lines indicated above made dag bootstrap run and submit jobs.
But my test submission is not getting matched in the global pool.

I have asked SI for help: https://mattermost.web.cern.ch/cms-o-and-c/pl/yi4eoususjgo8gg8k616qu6m9r

## Comment (belforte, 2024-11-15T09:49:37Z)

there is some special problem with KIT. Once I extended the possible site list job ran immediately at T2_US_Wisconsin.
The fact that it was restricted to KIT was due to the current dysfunctional JobRouter. I turned it off.

## Comment (belforte, 2024-11-15T10:23:09Z)

closed via #8796
