# dmwm/CRABServer issue #8908: deferred job submission failes after #8893

State: closed
Opened: 2025-01-31T10:21:08Z
Closed: 2025-01-31T16:29:43Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8908

## Opening post (belforte, 2025-01-31T10:21:08Z)

*  ref in preprod with v3.250109   https://cmsweb-testbed.cern.ch/crabserver/ui/task/250131_092508%3Abelforte_crab_20250131_102502 : all OK
* test in test2 with current master https://cmsweb-test2.cern.ch/crabserver/ui/task/250131_100639%3Abelforte_crab_20250131_110635

after #8893 all PreJob scripts run at same time at beginning and all jobs are submitted even if `+CRAB_JobReleaseTimeout=60` is correctly propagated to scheduler in Job.submit and DAG file has

```text
SCRIPT DEFER 4 60 PRE  Job1 dag_bootstrap.sh PREJOB $RETRY 1
SCRIPT DEFER 4 120 PRE  Job2 dag_bootstrap.sh PREJOB $RETRY 2
SCRIPT DEFER 4 180 PRE  Job3 dag_bootstrap.sh PREJOB $RETRY 3
SCRIPT DEFER 4 240 PRE  Job4 dag_bootstrap.sh PREJOB $RETRY 4
SCRIPT DEFER 4 300 PRE  Job5 dag_bootstrap.sh PREJOB $RETRY 5
SCRIPT DEFER 4 360 PRE  Job6 dag_bootstrap.sh PREJOB $RETRY 6
SCRIPT DEFER 4 420 PRE  Job7 dag_bootstrap.sh PREJOB $RETRY 7
SCRIPT DEFER 4 480 PRE  Job8 dag_bootstrap.sh PREJOB $RETRY 8
SCRIPT DEFER 4 540 PRE  Job9 dag_bootstrap.sh PREJOB $RETRY 9
...
SCRIPT DEFER 4 1440 PRE  Job24 dag_bootstrap.sh PREJOB $RETRY 24
SCRIPT DEFER 4 1500 PRE  Job25 dag_bootstrap.sh PREJOB $RETRY 25
SCRIPT DEFER 4 1560 PRE  Job26 dag_bootstrap.sh PREJOB $RETRY 26
SCRIPT DEFER 4 1620 PRE  Job27 dag_bootstrap.sh PREJOB $RETRY 27
SCRIPT DEFER 4 1680 PRE  Job28 dag_bootstrap.sh PREJOB $RETRY 28
SCRIPT DEFER 4 1740 PRE  Job29 dag_bootstrap.sh PREJOB $RETRY 29
SCRIPT DEFER 4 1800 PRE  Job30 dag_bootstrap.sh PREJOB $RETRY 30
```

## Comment (belforte, 2025-01-31T10:48:41Z)

PreJob needs to find `CRAB_JobReleaseTimeout` among the task ads and indeed it is not in _CONDOR_JOB_AD 
 file. But it is listed together with all other ads in that file in DagmanSubmitter code
https://github.com/dmwm/CRABServer/blob/c90d64829034084e3eafb8b72c9527c9d18e1680/src/python/TaskWorker/Actions/DagmanSubmitter.py#L60

yet it is not in the DAGJob.jdl logged in the TW temp directory
 ```console
crab3@crab-dev-tw01:/data/srv/tmp/_250131_100639:belforte_crab_20250131_110635rz9qfzbv$ grep CRAB_Job DAGJob.jdl 
My.CRAB_JobSW = "CMSSW_13_3_0"
My.CRAB_JobArch = "el8_amd64_gcc12"
My.CRAB_JobCount = 30
crab3@crab-dev-tw01:/data/srv/tmp/_250131_100639:belforte_crab_20250131_110635rz9qfzbv$ 
```

## Comment (belforte, 2025-01-31T10:51:09Z)

could this be `+ad` vs. `My.ad` ???

## Comment (belforte, 2025-01-31T11:00:53Z)

using `My.CRAB_JobReleaseTimeout=60` in the crabConfig.py makes it to correctly reach the PreJob
```
[crabtw@vocms059 SPOOL_DIR]$ grep CRAB_JobReleaseTimeout _CONDOR_JOB_AD 
CRAB_JobReleaseTimeout = 60
```
But now PreJob fails
```
  File "/data/srv/glidecondor/condor_local/spool/3028/0/cluster10093028.proc0.subproc0/TaskWorker/Actions/PreJob.py", line 470, in needsDefer
    submitTime = int(self.task_ad.get("CRAB_TaskSubmitTime"))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

## Comment (belforte, 2025-01-31T11:03:11Z)

`CRAB_TaskSubmitTime` is in the `subdag.jdl` and in the `DAGJob.jdl` created in TW, but not in the `_CONDOR_JOB_AD` file.

## Comment (belforte, 2025-01-31T11:27:31Z)

the `My.` suffix was lost when preparing DAGJob.jdl.  So these lines
```console
crab3@crab-dev-tw01:/data/srv/tmp/_250131_105201:belforte_crab_20250131_115157toscgred$ grep CRAB_TaskSubmitTime *jdl
DAGJob.jdl:CRAB_TaskSubmitTime = 1738320746
subdag.jdl:CRAB_TaskSubmitTime = 1738320746
```
define (unusee) variables, not classAds

## Comment (belforte, 2025-01-31T11:29:38Z)

bug. `My.` is missing here !
https://github.com/dmwm/CRABServer/blob/c90d64829034084e3eafb8b72c9527c9d18e1680/src/python/TaskWorker/Actions/DagmanSubmitter.py#L415

## Comment (belforte, 2025-01-31T11:46:46Z)

after that PreJobs run and say things like 
```
Fri, 31 Jan 2025 12:35:41 CET(+0100):INFO:PreJob   Defer time of this job (1800 seconds since initial task submission) not elapsed yet, deferring for 1800 seconds
```
but the DEFER is gone from DAG file
```console
[crabtw@vocms059 cluster10093032.proc0.subproc0]$ cat RunJobs.dag|grep PRE|grep -v SKIP|cut -d' ' -f 1-9|head
#SCRIPT PRE FinalCleanup dag_bootstrap.sh FINAL $DAG_STATUS $FAILED_COUNT cmsweb-test2.cern.ch:8443
SCRIPT  PRE  Job1 dag_bootstrap.sh PREJOB $RETRY 1
SCRIPT  PRE  Job2 dag_bootstrap.sh PREJOB $RETRY 2
SCRIPT  PRE  Job3 dag_bootstrap.sh PREJOB $RETRY 3
SCRIPT  PRE  Job4 dag_bootstrap.sh PREJOB $RETRY 4
SCRIPT  PRE  Job5 dag_bootstrap.sh PREJOB $RETRY 5
SCRIPT  PRE  Job6 dag_bootstrap.sh PREJOB $RETRY 6
SCRIPT  PRE  Job7 dag_bootstrap.sh PREJOB $RETRY 7
SCRIPT  PRE  Job8 dag_bootstrap.sh PREJOB $RETRY 8
```
that led to PRE being retried 3 times always failing and Dagman aborted

## Comment (belforte, 2025-01-31T12:15:01Z)

pfff..
https://github.com/dmwm/CRABServer/blob/c90d64829034084e3eafb8b72c9527c9d18e1680/src/python/TaskWorker/Actions/DagmanCreator.py#L556
works with `+.CRAB_JobReleaseTimeout` but not with `My.CRAB_JobReleaseTimeout`
I have no idea why they used such a strict check

## Comment (belforte, 2025-01-31T15:46:00Z)

after fixing all of that, things look OK.
```
belforte@lxplus806/TC3> crab status -d ./crab_20250131_162920 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250131_162920
Task name:			250131_152924:belforte_crab_20250131_162920
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/250131_152924%3Abelforte_crab_20250131_162920
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=250131_152924%3Abelforte_crab_20250131_162920&from=1738333765000&to=now
Status on the scheduler:	SUBMITTED

Jobs status:                    finished     		  3.3% ( 1/30)
				idle         		  6.7% ( 2/30)
				transferring 		 23.3% ( 7/30)
				unsubmitted  		 66.7% (20/30)

```

## Comment (belforte, 2025-01-31T15:51:35Z)

that was using `'My.CRAB_JobReleaseTimeout=60` in crabConfig.
Let's make sure that `config.Debug.extraJDL=['+CRAB_JobReleaseTimeout=Nsec']` also still work, as that's what they use in HC atm

## Comment (belforte, 2025-01-31T15:59:23Z)

I also used [above task](https://github.com/dmwm/CRABServer/issues/8908#issuecomment-2627657929) to try `crab kill` and `crab resubmit` and they worked as expected

## Comment (belforte, 2025-01-31T16:05:21Z)

rats.. 
config.Debug.extraJDL=['+CRAB_JobReleaseTimeout=120']
did not work.
The '+' was not changed to 'My.' as I expected from
https://github.com/dmwm/CRABServer/blob/ba252033b37b3045480c7386d7d2f33348164ddd/src/python/TaskWorker/Actions/DagmanCreator.py#L522-L526

## Comment (belforte, 2025-01-31T16:11:36Z)

my bad.  I need to do `+ --> My.` in the key, not the value !

## Comment (belforte, 2025-01-31T16:29:17Z)

All OK now !
