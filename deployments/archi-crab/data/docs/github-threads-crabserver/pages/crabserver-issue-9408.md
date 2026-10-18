# dmwm/CRABServer issue #9408: new PostJob with kill-on-ASO fails to properly report to MONIT

State: closed
Opened: 2026-09-01T15:55:50Z
Closed: 2026-09-14T12:50:12Z
Labels: Type: Bug, Priority: Critical, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9408

## Opening post (belforte, 2026-09-01T15:55:50Z)

I noticed this after https://github.com/dmwm/CRABServer/pull/9383 and https://github.com/dmwm/CRABServer/pull/9396 have been merged already. Can't says which one specifically is at fault.

But after those changes something is wrong in how things are reported to MONIT. ExitCode is not updated with the value in `JobExitCode`  and thus keeps reporting the job exit code (0) instead of the ASO error, `CRAB_PostJobLastUpdate` is 0 and `CRAB_PostJobStatus` stays stuck at `postProc`.

I think that the problem is in
https://github.com/dmwm/CRABServer/blob/b6ffcb6157b058daf50a8245d6ac8b840302e6e5/src/python/TaskWorker/Actions/PostJob.py#L2203-L2207

But haven't nailed down yet, nor found the right fix.
Most likely `self.set_state_ClassAds` was doing much more than editing those two classAds.

Note: I can't easily debug since re-running PostJob in the AP is only doable w/o the ASO part, so have to go the slow way by change+submit...

## Comment (belforte, 2026-09-01T15:57:41Z)

this e.g. affects v3.260828 and we can't deploy new TW until is fixed.  FYI @nausikt

## Comment (nausikt, 2026-09-01T16:05:46Z)

Acknowledged.

## Comment (belforte, 2026-09-02T07:37:56Z)

I tried to add back the call to  `set_state_ClassAds()`   before every `return`

```python

            except PermanentStageoutError as pse:
                retmsg = "Got fatal stageout exception:\n%s" % (str(pse))
                self.logger.error(retmsg)
                ASOExitCode = mostCommon(self.stageout_exit_codes, 60324)
                msg = "There was at least one permanent stageout error; user will need to resubmit."
                self.logger.error(msg)
                self.set_dashboard_state('FAILED', exitCode=ASOExitCode)
                ## OUCH this removes job from queue !! so the following tagAllJobsInTask will not work
                #self.set_state_ClassAds('FAILED', exitCode=ASOExitCode)
                # let's do the pedantic and safe way instead
                #self.schedd.edit([self.dag_jobid], 'JobExitCode', str(ASOExitCode))
                #self.schedd.edit([self.dag_jobid], 'CRAB_PostJobStatus', '"FAILED"')
                self.recordPermanentStageoutError(exitCode=ASOExitCode)
                self.logger.info("====== Finished to check for ASO transfers.")
                if self.tooManyPermanentStageoutErrors():
                    if self.maxFatalAsoDryRun:
                        self.logger.error("**** Too Many Fatal ASO errors. ****")
                        self.logger.error("**** If dry run were False, I would abort DAG and kill task ****")
                        # send msg to operators (only once per task) and go on normally
                        if self.maxFatalAsoNotificationMail and not self.maxFatalAsoMailAlreadySent():
                            self.sendMaxFatalAsoMailToOperators()
                        self.logger.info("Tag Jobs as ForcefullyTerminated")
                        self.tagAllJobsInTask(ad='CRAB_ForcefullyTerminated', value='DryASO')
                        self.set_state_ClassAds('FAILED', exitCode=ASOExitCode)
                        return JOB_RETURN_CODES.FATAL_ERROR, retmsg, ASOExitCode
                    # abort DAG, kill task and tag jobs
                    self.logger.error("**** Too Many Fatal ASO errors. Abort DAG and kill task ****")
                    killMsg = "Killed by CRAB because output can't be placed at destination site."
                    killMsg += "\nMake sure that your destination site is healthy and"
                    killMsg += "\nthat you have enough free disk space there"
                    killMsg += " before submitting again"
                    self.killThisTask(killMsg)
                    self.logger.info("Tag Jobs as ForcefullyTerminated")
                    self.tagAllJobsInTask(ad='CRAB_ForcefullyTerminated', value='ASO')
                    retmsg += '\ntoo Many Fatal ASO errors. Abort task DAG'
                    if self.maxFatalAsoNotificationMail:
                        self.sendMaxFatalAsoMailToOperators()
                    self.set_state_ClassAds('FAILED', exitCode=ASOExitCode)
                    return JOB_RETURN_CODES.DAG_ABORT, retmsg, ASOExitCode
                self.set_state_ClassAds('FAILED', exitCode=ASOExitCode)
                return JOB_RETURN_CODES.FATAL_ERROR, retmsg, ASOExitCode
            except RecoverableStageoutError as rse:
        self.set_state_ClassAds('FAILED', exitCode=ASOExitCode)
        return JOB_RETURN_CODES.FATAL_ERROR, retmsg, ASOExitCode
```

## Comment (belforte, 2026-09-02T07:38:49Z)

that seems to do, even if it left me worried for quite a while, but after >1hr eventually things showed up in OpenSearch in the desired way.

<img width="1364" height="949" alt="Image" src="https://github.com/user-attachments/assets/2140031e-3dcd-497e-b201-36cb6b5cd60d" />

I'll run more tests.

## Comment (belforte, 2026-09-02T16:08:14Z)

that change works for DryRun and for successful jobs.
But when PostJob issues the kill and aborts the DAG, the data in OS keeps only showing jobs as completed with exit code 0 and no PostJob info. But a local condor_history shows the changes.

🙄 
While in the [TaskDashboard](https://monit-grafana.cern.ch/goto/dfx208jq8apkwc?orgId=11) the jobs are listed as Removed. And still exit code 0.
I can try to delay the kill, but I suspect that there is still something to understand in https://github.com/dmwm/cms-htcondor-es/blob/master/src/htcondor_es/history.py

## Comment (belforte, 2026-09-02T17:24:39Z)

looking better, in the task in DryMode only 4/10 jobs got properly reported.
Very strange, and very puzzling.
https://monit-opensearch.cern.ch/dashboards/goto/e2fb16af6278fa96f800ac5d1932fe9a

but consistent with the Task dashboard https://monit-grafana.cern.ch/goto/dfx26zan3yf40b?orgId=11

## Comment (belforte, 2026-09-04T12:54:06Z)

lot of confusion here, I forgot that `./start.sh -c` after `./start.sh -g` does not fully revert, tarballs are not reset.
So let's make a clean comparison . I deploy same version as we have in prod/canary v3.260814 on `test12` and disable stageoutcheck in tw03's config so that can send test task where all ASO fails. Same task is also sent to my dev instance (test2+tw01). I use storage destination =DESY for "fail" and "CERN" for "succeed". Also blacklist CERN for execution to avoid local stageout.  4 jobs in the task.

instance | TW | tw version | ASO OK | ASO fail + below thresh|fail + Dry | fail + kill  |
-------------|------|-----------------|------------------------|---------------------------|--------------|--------------|
test12     | 03  | v3.260814  | [task](https://cmsweb-test12.cern.ch/crabserver/ui/task/260904_130128%3Abelforte_crab_20260904_150124) -   All OK [1]              | [task](https://cmsweb-test12.cern.ch/crabserver/ui/task/260904_130341%3Abelforte_crab_20260904_150339) -      All OK [1]           |      n.a.     | n.a.         |
test2       | 01  |      try2         | [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_131450%3Abelforte_crab_20260904_151448) -   All OK [1]              | [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_133841%3Abelforte_crab_20260904_153839) -    All OK [1]                |  [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_150124%3Abelforte_crab_20260904_170122) -  Bad [2]   | [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_150313%3Abelforte_crab_20260904_170311) -    Bad [3]         |
test2       | 01  |  try2 but 20 jobs, not 4   |     not run       |  [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_174822%3Abelforte_crab_20260904_194820)  -     All OK [1]          |  [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260904_175203%3Abelforte_crab_20260904_195201) -  All OK [1.1]  | [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260905_150636%3Abelforte_crab_20260905_170632) -    Bad ~like [3]    |
test2       | 01  | avoid-races-in-PJ try 1  20 jobs thr at 10 |                             |                                  |   [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260909_103701%3Abelforte_crab_20260909_123659) -   All OK [1.1]            |  [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260909_124455%3Abelforte_crab_20260909_144453) - All OK [1.2]           |
test2       | 01  | avoid-races-in-PJ try 1  4 jobs thr at 2 |                             |                                  |    [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260909_090059%3Abelforte_crab_20260909_110057) -    All OK  [1.1]       |   [task](https://cmsweb-test2.cern.ch/crabserver/ui/task/260909_124814%3Abelforte_crab_20260909_144812) - All OK [1.2]         |
test2       | 01  |                      |                             |                                  |                 |                 |
test2       | 01  |                      |                             |                                  |                 |                 |


[1] crab status OK, task dashboard OK, in OS `CRAB_PostJobStatus` and  `CRAB_PostJobLastUpdate` OK
[1.1] like [1] + mail OK + CRAB_ForcefullyTerminated OK
[1.2] like [1.1] but jobs whose PostJob had not processed FTS status yet when DAG was aborted will only show the execution status (0) and appear in task dashboard as "Removed" with exit code 0 and in OS as "completes" with exit code 0, `CRAB_PostJobStatus=postProc`,`CRAB_PostJobLastUpdate=0` and `CRAB_ForcefullyTerminated not defined`

[2] crab status OK (all failed), mail OK,  task dashboard NO (status postProc), in OS `CRAB_PostJobStatus`=`postProc` and   `CRAB_PostJobLastUpdate` =0 for all 4 jobs, `forcefullyTerminated` not set.  **bad** `condor_history` [4]
[3]  crab status OK all failed), mail OK,  task dashboard NO (3 postProc, 1 removed), in OS  OS `CRAB_PostJobStatus`=`postProc` and   `CRAB_PostJobLastUpdate` =0 for all 4 jobs,  `forcefullyTerminated` not set, **bad** `condor_history` and `condor_q` [5]
[4] only some jobs have `CRAB_ForcefullyTerminated` set:
```
clusterid crab_id jobexitcode CRAB_PostJobLastUpdate CRAB_ForcefullyTerminated
10609117  2       60322       1788535509.536235      DryASO                   
10609115  1       60322       1788535509.493913      DryASO                   
10609116  3       60322       1788535133.086554      undefined                
10609114  4       60322       1788535113.299909      undefined  
```
[5]
job 4 was left in the queue:
```
belforte@vocms059/SPOOL_DIR> condor_q  -con 'crab_reqname=="260904_150313:belforte_crab_20260904_170311"' -af:h jobuniverse clusterid crab_id jobexitcode CRAB_PostJobLastUpdate crab_forcefullyTerminated
jobuniverse clusterid crab_id jobexitcode CRAB_PostJobLastUpdate crab_forcefullyTerminated
7           10609118  undefined undefined   undefined              ASO                      
12          10609119  undefined undefined   undefined              undefined                
5           10609122  4         undefined   0                      ASO               
```
of other 3 in condor_history one does not have  `CRAB_ForcefullyTerminated` set
```
belforte@vocms059/SPOOL_DIR> condor_history  -con 'crab_reqname=="260904_150313:belforte_crab_20260904_170311"' -af:h clusterid crab_id jobexitcode CRAB_PostJobLastUpdate crab_forcefullyTerminated
clusterid crab_id jobexitcode CRAB_PostJobLastUpdate crab_forcefullyTerminated
10609123  3       60322       1788535152.809311      ASO                      
10609121  1       60322       1788535143.066695      ASO                      
10609120  2       60322       1788535108.284545      undefined                
```

## Comment (belforte, 2026-09-04T16:20:03Z)

* good news: if we do not activate "too many fatal jobs detected" all is fine
* bad news: if we activate it, even in dryRun mode, status in OpenSearch and Task dashboard is disrupted !!!!

## Comment (belforte, 2026-09-05T15:10:12Z)

* when I increased task to 20 jobs and failure threshold to 10, DryRun was OK.
   * Maybe I still have a race which is only (more) likely with few jobs ?
   * With more jobs and longer wait, PostJobs should be more scattered as jobs starts on different slots during different negotiator cycles...

## Comment (belforte, 2026-09-06T14:52:20Z)

I am leaning toward:
* dry run still OK but maybe some race
* real killing most likely suffer of races #9403 

I will try to make sure that there are no races and try again. More tests with DryRun in the meanwhile

## Comment (belforte, 2026-09-07T10:22:52Z)

2 more 40-jobs task All OK with DryASO.
Looks like this is good to deploy. Kill requires fixing the race.

## Comment (belforte, 2026-09-09T15:46:09Z)

out of the woods ?
