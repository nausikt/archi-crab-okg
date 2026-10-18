# dmwm/CRABServer issue #9423: protect against failure to submit task_proc_wrapper

State: closed
Opened: 2026-09-17T17:02:51Z
Closed: 2026-09-24T07:14:17Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9423

## Opening post (belforte, 2026-09-17T17:02:51Z)

Investigating ASO failures, I found a task with this with DAGstatus NOT_READY in the UI

<img width="656" height="446" alt="Image" src="https://github.com/user-attachments/assets/568ac492-8173-45e7-83db-d3714112afe0" />

Then from `crab status`
```
Task name:			260916_101527:nstrautn_crab_Bpark_MiniAOD_DATA_2_2024_runG_PromptReco_SM
Grid scheduler - Task Worker:	crab3@vocms0107.cern.ch - crab-prod-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/260916_101527%3Anstrautn_crab_Bpark_MiniAOD_DATA_2_2024_runG_PromptReco_SM
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=nstrautn&var-task=260916_101527%3Anstrautn_crab_Bpark_MiniAOD_DATA_2_2024_runG_PromptReco_SM&from=1789550127000&to=now
Task bootstrapped at 2026-09-16 10:18:24 UTC. 98277 seconds ago
Task bootstrapped on schedd more than 1637 minutes ago
But no status info is available yet. If this persists report it to cmstalk+computing-tools@dovecotmta.cern.ch 
```
Looking in SPOOL_DIR I found that Dagman was happily running, but the `task_process` directory had no logs. Transfer and status_cache scripts had never run.

The bootstrap log in `_condor_stderr` reported
```
+ chmod +x task_process/task_proc_wrapper.sh
+ condor_submit task_process/daemon.jdl

ERROR: Failed to connect to local queue manager
AUTHENTICATE:1006:exceeded 1789553924 deadline during authentication
AUTHENTICATE:1004:Failed to authenticate using SCITOKENS
```
So somehow the submission failed dye to some odd error in
https://github.com/dmwm/CRABServer/blob/be37a0af0873e3612a646c22ef0a4a3509bc1fd4/scripts/dagman/dag_bootstrap_startup.sh#L258
but `dag_bootstrap_startup.sh` kept going to
https://github.com/dmwm/CRABServer/blob/be37a0af0873e3612a646c22ef0a4a3509bc1fd4/scripts/dagman/dag_bootstrap_startup.sh#L282

In a way this was intentional and supposed to be a "feature", since I could "fix" with
`sudo su crabtw; condor_submit  task_process/daemon.jdl`
but in practice jobs have been submitted and executed for > 24h, resulting in ASO timeout in PostJob and total waste of CPU.

I.e. we were assuming that the user would notify us of this unusual situation so we would investigate and correct. But it did not happen here, and we do not know how many other times.

Options:
1. leave it
2. exit the script, so that dagman does not start. Easy and safe, but starting dagman by hand will be next to impossible, user will have to submit a new task.
3. retry the condor_submit in case it fails
4. send a message to operators in addition 
5. investigate if `crab resubmit` could fix, esp. after 2.

Which way to go ?

## Comment (belforte, 2026-09-23T16:45:13Z)

safest option would be
6. exit the script and somehow mark the task as failed.
 * but submission of wrapper + dagman start are done in the bash script, while sending a msg to server or changing the status_cache.pkl require python. Introducing a new python script to be called only in this rare case seems too messy to me.

Therefore:
**Plan:**
1. retry condor_submit after 10 seconds
2. if it still fails, exit w/o starting dagman and let user contact us when they notice so we can say "submit again"

ANyhow  I have also asked SI to keep FS as first authentication method, which may help avoid timeouts like the one indicated in initial comment: https://gitlab.cern.ch/CMSSI/cmsgwms-htcondor-configurations/-/merge_requests/27

## Comment (belforte, 2026-09-23T20:07:27Z)

When the task wrapper fails to start an attempt to issue `crab resubmit` ends with
```
Error: Status information is unavailable, will not proceed with the resubmission. Try again a few minutes later if the task has just been submitted.
```

So it is pretty clear anyhow. And I see no reason to make this more complicated by trying to change task status in the DB.
