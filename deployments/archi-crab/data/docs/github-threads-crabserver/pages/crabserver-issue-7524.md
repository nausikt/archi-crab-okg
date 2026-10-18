# dmwm/CRABServer issue #7524: fill properly tm_dbs_blockname and tm_block_complete in RUCIO_Transfers

State: closed
Opened: 2023-02-06T13:02:17Z
Closed: 2023-07-19T08:36:48Z
Labels: Priority: High, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7524

## Opening post (belforte, 2023-02-06T13:02:17Z)

now that updateRucioInfo API is available in REST
https://github.com/dmwm/CRABServer/blob/2cbd932bd64724dcbcca915f21665af1d9b5a08f/src/python/CRABInterface/RESTFileTransfers.py#L185-L198

usage example in https://github.com/belforte/utils/blob/master/notebooks/TestTransfersdb.ipynb

And from https://github.com/dmwm/CRABServer/wiki/ASO-via-Rucio the plan is:

* 1 rule per container
* 1 dataset each 100 file or when lumi limit is exceeded
* when a dataset is completed at least one of the files in it must be flagged via setting `block_complete` to `YES`

## Comment (belforte, 2023-02-06T13:16:33Z)

Findings from looking at code in https://github.com/dmwm/CRABServer/blob/master/scripts/task_process/RUCIO_Transfers.py 
* currently the file limit per dataset is not implemented 
* not clear if all files go in same dataset or if in some conditions a new one would be opened
* as long as there's one dataset there is also one rule, this must be kept moving role creation to when container is created
* why do we have `lfn2pfn` mapping code here instead of using Rucio's `lfns2pfns` ?
* global structures are not documented, must do this and find the correct way to fill dataset/DBS_block name in `filetransfersdb` table when inserting new files there.
* `task_process/transfers.txt` is opened and read 4 times
* logs are known to be too much verbose
* need a writeup of the procedure to test/debug RUCIO_transfers interactively on scheduler

## Comment (belforte, 2023-02-06T17:44:48Z)

bugs found
- [x] https://github.com/dmwm/CRABServer/blob/2cbd932bd64724dcbcca915f21665af1d9b5a08f/scripts/task_process/RUCIO_Transfers.py#L237 the initial `/` is there already in `publishname` also `g.logs_dataset` is defined already
- [ ] `task_process/transfers/last_transfer.txt` is updated at the end of `register_replicas` but before info is stored in CRAB's DB transfersdb table. Are we protected against a script crash at this point ?
- [ ]  there is some naming confusion IMHO: `{lfn:id}` is a map from LFN to IDs (lfn2id) not viceversa 
- [ ]  more ?

## Comment (belforte, 2023-02-06T18:48:08Z)

steps to implement the needed functionality
- [ ] register_replicas should not return list of names, but rather add success/fail info and dataset name into each replica dictionary so that information can be used when updating oracle.
   - hmm. no. replica dictionaries have the format needed for adding to rucio, better make the success/fail lists, lists of dictionaries, not LFN's 
- [ ] update_db should be changed to take alist of replica dictionaries as input ? Or maybe the needed info can be added to filedoc_for_db ? The the new updateRucioInfo api may even be not needed ?
- [ ] should not mark files as "done" (i.e. update lastline) unless info in CRAB DB was updated, and therefore be prepared for finding already processed files (which may be the case already)
- [ ] decide when to add dbs block info to filtransfersdb: when replica is registered in Rucio, or when transfer is completed ? What will happen if one file xfer get stuck ? Do we remove the file from the rucio-dataset ?

## Comment (belforte, 2023-02-15T13:19:44Z)

after discussion with @dciangot , some code reformatting is needed to implement internal bookkeeping as now sketched in the [wiki](https://github.com/dmwm/CRABServer/wiki/ASO-via-Rucio)

that overrides all above concepts/questions

## Comment (belforte, 2023-02-16T12:01:42Z)

work in progress on this is in https://github.com/belforte/CRABServer/tree/fill-block-info-from-RT-fix-7524

## Comment (belforte, 2023-03-22T10:59:43Z)

here's a contribution from Wa: https://github.com/belforte/CRABServer/compare/fill-block-info-from-RT-fix-7524...novicecpp:CRABServer:rucio_transfer_fill_info_to_db_for_publisher_upstream_belforte

## Comment (novicecpp, 2023-05-10T08:15:22Z)

Items Stefano and Wa were discussed on May 10:

- [x] How do we notify postjob that transfer is complete?
    - there is a file in the SPOOL_DIR where the transfer script(s) update thing.
        - **Action Item**: Details need to be looked at in the code and **document**ed
    - "semantically" this duplicatest the fact that status of transfer is also updated in transfersdb table in CRAB DB. The idea was to avoid polling the DB in the PostJob to reduce traffic.
    - also, which condition?
        - for FTS based ASO the script waits until FTS reports success or failure. AFAIR (to be verified in the code, of course) we ask FTS to retry a maximum of 3 times and with a maximum time of ... 12h ? FTS_Transfers script runs every 15min and polls status of all submitted FTS jobs every time.
        - for RUCIO base ASO, script still is organized as : run every 15min, at each run checks if there are new files to transfer and status of ongoing transfers. With RUcio "transfers never fail". Once we have a rule to replicate from temp to final storage, Rucio will try forever. RUle may bevome stuck, it simply means rate of retries is lower. If we want to call it "done with error" we have to do it ourselves.
            - **Action Items** check update is already done. only need to update files in spool dir for postjob. 
        - Current plan (to be revised in light of experience) is:
            - wait 24h (PostJOb does the waiting, like now). If it is not done, assume it will never do. So try to submit a new job (at a different site if possible), need to detach this LFN froom the container so that it goes away from the rule and Rucio will not try the transfer anymore, also gfal-rm the replica in tmp. Then PostJob will trigger a new job and at some point RUCIO_Transfer will find again that LFN as a new file to  transfer. But the LFN exists already in Rucio, and has the old checksum. New file will have same data content but different internal timestamps, so different checksum. Currently the user can not change the stored checksum, we need a "fix" to Rucio permissions in this case.
                - Ref
                    - https://github.com/dmwm/CRABServer/issues/7404
                    - https://github.com/dmwm/CRABServer/wiki/ASO-via-Rucio
                    - https://github.com/dmwm/CMSRucio/issues/159#issuecomment-1270713057
                    - https://github.com/dmwm/CMSRucio/issues/297
                - RECAP: crab resubmit will resubmit but jobs will always fail for the file that already register as replicas 
                - **Action Items**: add code to handle files that not-OK after threshold time.
- [x] We do not handle the case where files in temp is gone. Both before and after transfer complete
    - subset of above problem
- [x] We add new files as bulk (current default is 20) but current code will fail the whole bulk if fail. Should we fix it?
    - It should not be failed in this step unless connection error. 
    - fail the script or put it back to the queue and try again later 
- [x] What about direct stageout?
    - should we disable it for rucio transfers? or still enable it but add code to RUCIO_Transfers.py to add files to container 
later?
      - it explicitly disabled for rucio transfers
- [x] Condition to stop execute RUCIO_Transfers.py?
    - From TODO: if replicas take > 12h to transfer, what shall we do?
    - Stefano will look at it
- [x] bookkeeping for monitoring replicas?
    - I am not sure because currently 
    - 1) we fetch all replicas status the whole container from container's rule ID. 
    - 2) we update all replicas to rest. 
      Then which level we want to optimize ? only part on update filetransfers table? or fetch and only complete block (need to add rule to each dataset to archieve this)?
    - **Action item**: do 2)
- [x] TODO: Broken site config in rucio (not 100% sure)
  - `T2_DE_DESY` Rucio expect `<prefix>/store/temp` but `lfn2pfns` return `<prefix>/temp` (at least it is valid path).
  - `T2_UK_SGrid_Bristol` register replicas report no protocol available for `T2_UK_SGrid_Bristol_Temp` where we get protocol info from `T2_UK_SGrid_Bristol`.
- [x] TODO: Test with production tasks
    - grep random tasks from production and run ourselves in preprod?
        - less effort compare to shadowing transfer, submit user job in preprod can be automated.
        - crab copycat
- [x] TODO: LOGS transfers (need to be done).
    - Maybe not do it at all. 
    - **Action Items**: make it clear somehow that we will do it when it requires
- [x] TODO: 1 container for multiple tasks.
    - REMINDER: same pset will have same output tag have.
- [x] TODO: Long way to go for better unittest/integration test.
  - It is spaghetti code.
  - Only simple testcase.
  - No integration code at all (It is done by hand for now).

## Comment (novicecpp, 2023-05-11T08:45:31Z)

Next to do list for RUCIO_Transfers.py
- [x] (move) ~~update files in SPOOL_DIR to notify postjob that transfer is complete.~~ Update correct status to database when files transfer is completed.
- [x] ~~add code to handle files that not-OK after threshold time has passed.~~ No need to do anything. Add complete transfer files to top level container.
- [x] check what happen to the `RUCIO_Transfers.py` script when files checksum is incorrect.
- [x] (move) Fix `add_replicas` to try again instead of fail them (It should not failed on this step).
- [x] (move) bookkeeping locks monitoring.
- [x] (move) Fix rucio config broken on site `T2_DE_DESY` and `T2_UK_SGrid_Bristol`.
- [x] add comment in code that we will not do log transfer for rucio (until it requires by user).
- [x] (move) 1 container for multiple tasks.
- [ ] documentation. 

Some tasks are moved to https://github.com/dmwm/CRABServer/issues/7632#issue-1707380092

## Comment (belforte, 2023-05-11T12:11:05Z)

I can not find the place in above lists, but IIRC the action on me was to explains how and when RUCIO_Transfers.py stops running. This is controlled in these lines:
https://github.com/dmwm/CRABServer/blob/18af83f510e5ff8579ad30a5073cc97af9c060a9/scripts/task_process/task_proc_wrapper.sh#L36-L51
combined with the `while True` look at the bottom of the script.

In other words:
the task_process will execute RUCIO_Transfers.py every 5 minutes until all the PostJob have completed. If we want to keep waiting and testing, the PostJob has to wait

How much we wait is a classAd in the job
https://github.com/dmwm/CRABServer/blob/18af83f510e5ff8579ad30a5073cc97af9c060a9/src/python/TaskWorker/Actions/PostJob.py#L2543-L2545

The value of ASOTimeout if set for the taks by
https://github.com/dmwm/CRABServer/blob/18af83f510e5ff8579ad30a5073cc97af9c060a9/src/python/TaskWorker/Actions/DagmanCreator.py#L471-L475

Using values from TaskWorker congiguration
We currently have a 7 days timeout in PostJob when using Rucio as per https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L84-87

## Comment (belforte, 2023-05-12T08:46:17Z)

One more thing:
 * when user issues `crab resubmit` the DAG is restarted and a new `task_proc_wrapper.sh` is started (as a condor job in local universe, `jobuniverse==12`) and again executes until the DAG completes (or the `task_proc_wrapper.sh` script crashes).

## Comment (novicecpp, 2023-05-12T11:14:36Z)

Thanks Stefano. I will write this somewhere in our docs.

One question: how do you want to proceed on my stale PR [#7587](https://github.com/dmwm/CRABServer/pull/7587) ?
Do you want to review it by yourself or review it together in zoom chat (one Actions class at a time, total 3 Actions classes)?

I prefer to have someone crosscheck my code before merging it (It will merge to feature branch `rucio_transfers` in `dmwm/CRABServer` repo, but in the end, it will get merged to master). Then, I can close this issue and move on to https://github.com/dmwm/CRABServer/issues/7632 .

## Comment (novicecpp, 2023-07-19T08:36:48Z)

This issue is solved via this [commit](https://github.com/dmwm/CRABServer/commit/1a6dd1fd4117fc738aef612d83e50d98d2d83bf1#diff-cff0a0719b4ec8b470d2a039241db3675479d70b42212c530efd5d0cc62aab0b) (just work, another patch is incoming).
 Tracking other Rucio ASO issues in [#7632](https://github.com/dmwm/CRABServer/issues/7632) and closing this one.
