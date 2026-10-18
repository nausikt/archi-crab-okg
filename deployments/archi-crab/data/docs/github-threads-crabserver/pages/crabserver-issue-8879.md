# dmwm/CRABServer issue #8879: GOALS for 2025

State: closed
Opened: 2025-01-14T09:03:54Z
Closed: 2026-02-11T09:33:50Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8879

## Opening post (belforte, 2025-01-14T09:03:54Z)

Picking up from #7876

**goals we expect we will achieve**:
legend: Qx = milestone for that quarter , Hx = milestone for that year

- [x] canary deployment for REST
- [x] switch to HTCondor v2 API
- [x] multiple tests running in parallel in our gitlab CI pipeline
- [x] **Q4** reboot each schedd every 6 months or so (automatically). We can do via a crontab (in puppet) which stops submissions to Vanilla  pool, holds al jobs, wa and reboots. Ned to syncronize with TW putting in drain the day before. Proposal: have hiera variable with list of reboot dates placed in TW config and parsed by TW code and placed in scheduler disk and parsed by crontab. See also #8651
       * **Move to 2026** 
- [x] **H2** use of tokens for talking to CMSWEB #7845 (predicated on CMS TokenTeam progresses)
       * **Move to 2026** 
- [x] **Q3** refactor/re-evalluate crab resubmit  #6270
- [x] **Q3** ArgoCD for our K8s applications 
       * **Finish in  2026** 
- [x] **Q1** DAG status in taskDB 
   - [x] **Q1** (running/completed/failed) (and modify crab status) #8394 
   - [x] **Q1** add Num of jobs per task to Task table #7766
   - [x] **H2** use submitted task info in task scheduling #9073
       * **Move to 2026** 
- [x] **H2** cleanup code source (remove "transients" from past migrations)
       * **Continues 2026** 
- [x] **H2** cleanup an update documentation
       * **Continues 2026** 

**things that we may realistically do, but it is not clear if/when we will want to do**

- [x] revisit JobRetry.py policies (more retries, re-eval site list, add cooloff ...)
       * **Move  2026** 
- [ ] Utilitiies for users to deal with data management via Rucio (list/delete rules e.g.)  - **NOPE**
 - [ ] a job status table for each task (avoid accessing status cache on schedd) (and modify crab status) - **NOPE**
- [x] more monitoring via Spark ? **DONE**
- [x] can we "evolve" crab status command to avoid the need to retrieve files from scheduler's WEB_DIR ? Maybe not useful ? **NOPE**
- [x] adopt  Rahuls tool to insert user data into rucio https://github.com/dmwm/CRABServer/issues/7755 - **NOPE**
- [x] crab recall #7594 - **NOPE**
- [x] new copycat functionality for our testing and use in automatic recovery #7877 - **NOPE**
- [ ] 
- [ ] full monitoring for preprod ?
- [ ] ...
