# dmwm/CRABServer issue #7876: GOALS for 2024

State: closed
Opened: 2023-09-14T16:25:16Z
Closed: 2025-02-17T09:33:51Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7876

## Opening post (belforte, 2023-09-14T16:25:16Z)

based on discussion in CRAB meeting on Sept 14, we have a first set of goals for 2024 (things moved there !)
Similarly to #7635 

**goals we expect we will achieve**:
- [x] Move all VM's to alma9 #8257 
- [x] stop using deprecated HTC API's  #8337 
- [x] adapt to new HTCondor python bindings v2
- [x] Install via piypi #7560
- [x] automatic CI pipeline #7958 
- [x] Improved recovery task #7595
     - [x] only a small bit remains FileBased splitting: https://github.com/dmwm/CRABClient/issues/5330 
- [x]  https://github.com/dmwm/CRABClient/issues/5221
- [x] Canary deployment for TW, https://github.com/dmwm/CRABServer/issues/8650
- [x] Task scheduler (something before TaskWorker) #7485 
- [x] fix  HC dealyed submission is disrupted when condor restarts on the scheduler https://github.com/dmwm/CRABServer/issues/7410
- [x] complete "improved monitoring" based on Summer Students output #7169 and more
- [x] #6544 #7461


**Things which  go to 2025**

- [ ] canary deployment for REST
- [x] switch to HTCondor v2 API
- [ ] reboot each schedd every 6 months or so (automatically). We can do via a crontab (in puppet) which stops submissions to Vanilla  pool, holds al jobs, wa and reboots. Ned to syncronize with TW putting in drain the day before. Proposal: have hiera variable with list of reboot dates placed in TW config and parsed by TW code and placed in scheduler disk and parsed by crontab. See also #8651
- [ ] use of tokens for talking to CMSWEB #7845 (predicated on CMS TokenTeam progresses)
- [ ] refactor/re-evalluate crab resubmit  #6270
- [ ] revisit JobRetry.py policies (more retries, re-eval site list, add cooloff ...)
- [ ] ArgoCD for our K8s applications ?
- [ ] more monitoring via Spark ? Make it possible to build panels "as needed" in Grafana ?
- [ ] a job status table for each task (avoid accessing status cache on schedd) (and modify crab status)
- [ ] DAG status in taskDB (running/completed/failed) (and modify crab status)
- [ ] use submitted task info in task scheduling
- [ ] cleanup code source (remove "transients" from past migrations)
- [ ] can we "evolve" crab status command to avoid the need to retrieve files from scheduler's WEB_DIR ? Maybe not useful ?
- [ ] cleanup an update documentation
- [ ] Utilitiies for users to deal with data management via Rucio (list/delete rules e.g.)

**things that we may realistically do, but it is not clear if/when we will want to do**
- [ ] adopt  Rahuls tool to insert user data into rucio https://github.com/dmwm/CRABServer/issues/7755
- [ ] crab recall #7594
- [ ] new copycat functionality for our testing and use in automatic recovery #7877 
- [ ] ...
