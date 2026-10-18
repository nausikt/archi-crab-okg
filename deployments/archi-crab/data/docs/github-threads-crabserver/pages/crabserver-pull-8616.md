# dmwm/CRABServer pull request #8616: rename classad TaskType to CRAB_DAGType. Fix #8488

State: closed
Opened: 2024-08-12T21:27:03Z
Closed: 2024-08-19T16:44:11Z
Merged: 2024-08-19T16:44:11Z
URL: https://github.com/dmwm/CRABServer/pull/8616

## Opening post (belforte, 2024-08-12T21:27:03Z)

renaming something used in so many places is dangerous.

This PR will need very good testing.

## Comment (belforte, 2024-08-12T21:29:06Z)

anyhow all remaining instances of `TaskType` string in the code are only for the ads used to send information to the MONIT dashboards
```
test/makeTests.py
103:lookFor "JOB AD: CMS_TaskType = \\"hctestnew\\"" "${workDir}/results/job_out.1.*.txt"

scripts/dag_bootstrap_startup.sh
230:        CMSTTASKYPE=`grep '^CMS_TaskType =' $_CONDOR_JOB_AD | awk '{print $NF;}'`
243:+CMS_TaskType = $CMSTTASKYPE

src/python/TaskWorker/Actions/PreJob.py
145:                  'taskType': self.task_ad.get("CRAB_DashboardTaskType", 'analysistest'),

src/python/TaskWorker/Actions/DagmanSubmitter.py
79:    ('+CRAB_DashboardTaskType', 'taskType'),
84:    ('+CMS_TaskType', 'cms_tasktype'),

src/python/TaskWorker/Actions/DagmanCreator.py
113:+CMS_TaskType = %(cms_tasktype)s
387:    def getDashboardTaskType(self, task):
391:            return getattr(self.config.TaskWorker, 'dashboardTaskType', 'analysistest')
407:    def setCMS_TaskType(self, task):
478:        info['taskType'] = self.getDashboardTaskType(task)
488:        info['cms_tasktype'] = self.setCMS_TaskType(task)

src/script/Deployment/TaskWorker/TaskWorkerConfig.py
91:config.TaskWorker.dashboardTaskType = 'analysis'
LapSB:CRABServer$ 

```

## Comment (cmsdmwmbot, 2024-08-12T21:33:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2105/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-12T21:36:30Z)

Once this is in. We will need to update all places where `TaskType=="ROOT"` is used in the documentation (if any).

## Comment (cmsdmwmbot, 2024-08-13T07:50:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2106/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-13T13:00:31Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 294 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2107/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-13T13:05:07Z)

I will start by deploying to crab-dev-tw01 and check that it works for new tasks.
A simple submit+kill+resubmit worked.
I will test a task with many jobs. But as usual the critical points will be automatic splitting and error situations

## Comment (belforte, 2024-08-14T11:02:41Z)

large task and automatic split work. I could not test tail jobs though.

## Comment (belforte, 2024-08-14T12:08:46Z)

more testing
- [x] https://github.com/dmwm/CRABServer/issues/8619

## Comment (belforte, 2024-08-14T19:10:00Z)

i tried automatic splitting on a large dataset https://cmsweb-test2.cern.ch/crabserver/ui/task/240814_190344%3Abelforte_crab_20240814_210338
same input as in recent user problem [report](https://cms-talk.web.cern.ch/t/crab-produces-corrupted-file-and-does-not-fail/45888?u=belforte)  which when through 3 set of tails. But maybe my application is too fast

cool, I got tail jobs
```
Jobs status:                    finished     		  1.4% (  88/6126)
				idle         		 16.8% (1032/6126)
				rescheduled as tail jobs		  5.2% ( 316/6126)
				running      		  6.6% ( 406/6126)
				transferring 		 17.6% (1077/6126)
				unsubmitted  		 52.4% (3207/6126)
```
then I killed
```
Status on the scheduler:	FAILED (KILLED)

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch:8443/scheddmon/059/belforte/240814_190344:belforte_crab_20240814_210338/AutomaticSplitting/

Jobs status:                    finished     		  1.4% (  88/6126)
				rescheduled as tail jobs		 47.8% (2931/6126)
				unsubmitted  		 50.7% (3107/6126)
```
and resubmitted

but that's too much to ask for, original automatic splitting implementors disabled it
```
 Error: Tasks using automatic splitting cannot be resubmitted after a kill.
```

I should have killed single jobs with `condor_rm`

## Comment (belforte, 2024-08-17T10:38:37Z)

try again the large dataset  with https://cmsweb-test2.cern.ch/crabserver/ui/task/240817_103627%3Abelforte_crab_20240817_123622

so far so good
```text

Jobs status:                    finished     		  2.1% ( 151/7038)
				idle         		 14.3% (1006/7038)
				running      		  2.9% ( 204/7038)
				transferring 		  9.1% ( 639/7038)
				unsubmitted  		 71.6% (5038/7038)
```

only tail jobs can be resubmitted thought. Need to wait.

all sub-dag completed now, task is FAILED with 6k failed jobs (my EOS was full). But `crab resubmit` does nothing. AFAICT it only does "something" as long as ROOT/MAIN/BASE DAG is running. Once it compltetes it can't be put in hold/release anymore so this code is ineffective
https://github.com/dmwm/CRABServer/blob/0a57bb936ed5c729f06a1f2cfe8b36ca4d49c680/src/python/TaskWorker/Actions/DagmanResubmitter.py#L67-L73
https://github.com/dmwm/CRABServer/blob/0a57bb936ed5c729f06a1f2cfe8b36ca4d49c680/src/python/TaskWorker/Actions/DagmanResubmitter.py#L108-L110

In the SPOOL_DIR there are `DAGresque` files for the subdags, but not for the ROOT/BASE one, and we do not have a command to trigger those. Our resubmission relies on dagman job to be in HOLD so that we can trigger re-execution by releasing it.

I am not sure why that job is in COMPLETE now, but I never tested automatic splitting in this way.  JobStatuses: 4=COMPLETE, 5=HOLD

```
[crabtw@vocms059 cluster9777486.proc0.subproc0]$ condor_q -con 'crab_reqname=="240817_103627:belforte_crab_20240817_123622"&&jobuniverse==7' -af clusterid jobstatus crab_dagtype 
9777486 4 BASE
9777493 5 PROCESSING
9783994 5 TAIL
9787264 5 TAIL
9800547 5 TAIL
[crabtw@vocms059 cluster9777486.proc0.subproc0]$ condor_q 9777486


-- Schedd: crab3@vocms059.cern.ch : <188.184.103.189:4080?... @ 08/19/24 18:41:10
 ID         OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD
9777486.0   crabtw          8/17 12:36   0+00:00:00 C  10   0.0 dag_bootstrap_startup.sh RunJobs.dag

Total for query: 0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended 
Total for all users: 15 jobs; 0 completed, 14 removed, 0 idle, 1 running, 0 held, 0 suspended

[crabtw@vocms059 cluster9777486.proc0.subproc0]$ 
```

## Comment (belforte, 2024-08-19T16:43:51Z)

OTOH, I got no error and I looked at things deep and long enough to be quite confident that the name change is done properly.
So will merge
