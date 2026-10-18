# dmwm/CRABServer issue #8002: improve message when submit fails due to run/lumi empty selection

State: closed
Opened: 2023-11-10T23:18:47Z
Closed: 2023-12-14T15:35:05Z
Labels: Type: Enhancement, Type: Support, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8002

## Opening post (belforte, 2023-11-10T23:18:47Z)

https://cmsweb.cern.ch/crabserver/ui/task/231110_195041%3Abelforte_crab_20231110_205030

DataDIscovery was OK
```
2023-11-10 20:51:06,209:INFO:DBSDataDiscovery:Looking up data location with Rucio in cms scope.
2023-11-10 20:51:07,782:DEBUG:DBSDataDiscovery:Dataset size in GBytes: 15806.294403243
2023-11-10 20:51:11,348:DEBUG:DataDiscovery: Formatting data discovery output 
2023-11-10 20:51:12,853:DEBUG:DataDiscovery:Tot events found: 60537490
2023-11-10 20:51:12,854:DEBUG:DataDiscovery:Tot lumis found: 26448
2023-11-10 20:51:12,854:DEBUG:DataDiscovery:Duplicate lumis found: 0
2023-11-10 20:51:12,855:DEBUG:DataDiscovery:Tot files found: 4439
2023-11-10 20:51:12,856:DEBUG:DataDiscovery:Starting to create compact lumilists for input dataset
2023-11-10 20:51:12,874:DEBUG:DataDiscovery:Finished to create compact lumilists for input dataset
2023-11-10 20:51:12,883:DEBUG:DBSDataDiscovery:Got 4439 files
```
yet I got the cryptic
```
2023-11-10 20:51:13,995:DEBUG:Handler:Starting <TaskWorker.Actions.Splitter.Splitter object at 0x7f09115d4cd0> on 231110_195041:belforte_crab_20231110_205030
2023-11-10 20:51:14,060:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.231101-490c3036613f40b166346f09f19c5327/slc7_amd64_gcc630/cms/crabtaskworker/v3.231101-490c3036613f40b166346f09f19c5327/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 85, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.231101-490c3036613f40b166346f09f19c5327/slc7_amd64_gcc630/cms/crabtaskworker/v3.231101-490c3036613f40b166346f09f19c5327/lib/python3.8/site-packages/TaskWorker/Actions/Splitter.py", line 75, in execute
    raise TaskWorkerException(msg)
TaskWorker.WorkerExceptions.TaskWorkerException: The CRAB3 server backend could not submit any job to the Grid scheduler: splitting task 231110_195041:belforte_crab_20231110_205030 on dataset /SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD with FileBased method does not generate any job. See
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Splitting
```

## Comment (belforte, 2023-11-28T08:25:37Z)

OK. The problem is that I had in crabConfig
```
config.Data.runRange = '0'
```
And input dataset is AOD (non SIM).
Time to make this more clear, since users also get puzzled everytime they get this errror.

## Comment (belforte, 2023-11-28T19:45:32Z)

It should be enough to check run ranges in dataset and split-algo-params.
I do not think we have ever seen a case where the exact lumi matters.
At least it will be a start

## Comment (belforte, 2023-12-08T16:50:52Z)

with the above commt the message will be instead:
```
belforte@lxplus803/TC3> crab status 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20231208_174911
Task name:			231208_164915:belforte_crab_20231208_174911
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/231208_164915%3Abelforte_crab_20231208_174911
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=231208_164915%3Abelforte_crab_20231208_174911&from=1702050555000&to=now
Failure message from server:	CRAB could not submit any job to the Grid scheduler:
				splitting task 231208_164915:belforte_crab_20231208_174911
				on dataset /SingleMuon/Run2018D-UL2018_MiniAODv2_GT36-v2/MINIAOD
				with FileBased method does not generate any job. See
				https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Splitting
				Some hopefully helpful information to help you figure out the reason:
				Run list from task configuration is inside the range: 0 - 0
				Run list from input dataset is inside the range: 320500 - 325175
				The intersection of the two lists is: []
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20231208_174911/crab.log
belforte@lxplus803/TC3> 

```
