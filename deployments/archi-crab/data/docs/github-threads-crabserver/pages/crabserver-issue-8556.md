# dmwm/CRABServer issue #8556: FTS_Transfer does not handle external connection and bookkeeping properly, caused some files to be stale in the state "SUBMITTED"

State: closed
Opened: 2024-07-23T16:43:06Z
Closed: 2024-07-24T14:16:18Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8556

## Opening post (novicecpp, 2024-07-23T16:43:06Z)

Reported by Oscar in Computing tools: https://cms-talk.web.cern.ch/t/re-stageout-exceptions-from-crab-jobs/44154
Task URL: https://cmsweb.cern.ch/crabserver/ui/task/240722_082324%3Aoglez_crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD
`FTS_Transfer.py`'logs: [vocms0194:/data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/task_process/transfers/transfer_inject.log](https://cmsweb.cern.ch:8443/scheddmon/0194/oglez/240722_082324:oglez_crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD/SPOOL_DIR/task_process/transfers/transfer_inject.log)
Example FileID: `7fbb708684d552f510ba862f5dfb547b25fdc08d214c125bd4041781`, Job ID: `4442ee32-4824-11ef-9376-fa163eaa97bf`

What happened here was:
1. `check_FTSJob()` finished execute for FTS Job ID `4442ee32-4824-11ef-9376-fa163eaa97bf`, found `7fbb708684d552f510ba862f5dfb547b25fdc08d214c125bd4041781` was finished.
    `7fbb708684d552f510ba862f5dfb547b25fdc08d214c125bd4041781` were removed from bookkeeping records `4442ee32-4824-11ef-9376-fa163eaa97bf.json` at [line 276](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L276). 
    (log line: 23038-23040)
    ```
    2024-07-22 16:05:26,027: Getting state of job 4442ee32-4824-11ef-9376-fa163eaa97bf
    2024-07-22 16:05:26,087: State of job 4442ee32-4824-11ef-9376-fa163eaa97bf: ACTIVE
    2024-07-22 16:05:26,234: file XFER OK will remove davs://xrootd.cmsaf.mit.edu:1094/store/temp/user/oglez.c0781276b3d41d890451044b1ce34cb8259a05e4/craboutput/Muon/crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD/240722_082324/0000/log/cmsRun_1.log.tar.gz
    2024-07-22 16:05:26,248: Getting state of job 783f97de-481b-11ef-8fff-fa163e9e00e6
    ```
2. Next FTS Job ID processed normally, until ID `53b71580-4821-11ef-8578-fa163e255442`. Exception was raised at [line 213](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L213), program exited.

    (log line: before 23356)
    ```
    ...    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/task_process/FTS_Transfers.py", line 679, in <module>
        algorithm()
      File "/data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/task_process/FTS_Transfers.py", line 669, in algorithm
        jobs_ongoing = state_manager(ftsContext, crabserver)
      File "/data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/task_process/FTS_Transfers.py", line 546, in state_manager
        check_FTSJob(logging, ftsContext, jobid, jobsEnded, jobs_ongoing, done_id, failed_id, failed_reasons)
      File "/data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/task_process/FTS_Transfers.py", line 174, in check_FTSJob
        file_statuses = fts3.get_job_status(ftsContext, jobid, list_files=True)['files']
      File "/usr/lib/python3.9/site-packages/fts3/rest/client/easy/state.py", line 59, in get_job_status
        return inquirer.get_job_status(job_id, list_files)
      File "/usr/lib/python3.9/site-packages/fts3/rest/client/inquirer.py", line 38, in get_job_status
        job_info["dm"] = json.loads(self.context.get("/jobs/%s/dm" % job_id))
      File "/usr/lib/python3.9/site-packages/fts3/rest/client/context.py", line 214, in get
        return self._requester.method(
      File "/usr/lib/python3.9/site-packages/fts3/rest/client/request.py", line 111, in method
        response = requests.request(
      File "/usr/lib/python3.9/site-packages/requests/api.py", line 61, in request
        return session.request(method=method, url=url, **kwargs)
      File "/usr/lib/python3.9/site-packages/requests/sessions.py", line 544, in request
        resp = self.send(prep, **send_kwargs)
      File "/usr/lib/python3.9/site-packages/requests/sessions.py", line 657, in send
        r = adapter.send(request, **kwargs)
      File "/usr/lib/python3.9/site-packages/requests/adapters.py", line 516, in send
        raise ConnectionError(e, request=request)
    requests.exceptions.ConnectionError: HTTPSConnectionPool(host='fts3-cms.cern.ch', port=8446): Max retries exceeded with url: //jobs/53b71580-4821-11ef-8578-fa163e255442/dm (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x15516a1e5c40>: Failed to establish a new connection: [Errno 111] Connection refused'))
    2024-07-22 16:05:34,440: transfer_inject.py exiting
    ```
3. FTS\_Transfer.py started new round.
    (log line: 23356)
    ```
    2024-07-22 16:10:36,639: using user's proxy from /data/srv/glidecondor/condor_local/spool/7021/0/cluster107037021.proc0.subproc0/0defbdc2956bbbd335400fd42baccb1536baa936
    ```
4. When `check_FTSJob()` execute FTS Job ID `4442ee32-4824-11ef-9376-fa163eaa97bf` again, it read the `fileIDs` list from json `4442ee32-4824-11ef-9376-fa163eaa97bf.json`. 
    But the `fileIDs` got removed by previous round at point 1. So it simply skipped `7fbb708684d552f510ba862f5dfb547b25fdc08d214c125bd4041781`, only 3 files got added to `done_id['4442ee32-4824-11ef-9376-fa163eaa97bf']`.
    (log line: 23680-23684)
    ```
    2024-07-22 16:11:02,541: Getting state of job 4442ee32-4824-11ef-9376-fa163eaa97bf
    2024-07-22 16:11:02,610: State of job 4442ee32-4824-11ef-9376-fa163eaa97bf: FINISHED
    2024-07-22 16:11:02,725: file XFER OK will remove davs://xrootd.cmsaf.mit.edu:1094/store/temp/user/oglez.c0781276b3d41d890451044b1ce34cb8259a05e4/craboutput/Muon/crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD/240722_082324/0000/outputfile_1.root
    2024-07-22 16:11:02,725: file XFER OK will remove davs://xrootd.cmsaf.mit.edu:1094/store/temp/user/oglez.c0781276b3d41d890451044b1ce34cb8259a05e4/craboutput/Muon/crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD/240722_082324/0000/log/cmsRun_738.log.tar.gz
    2024-07-22 16:11:02,726: file XFER OK will remove davs://xrootd.cmsaf.mit.edu:1094/store/temp/user/oglez.c0781276b3d41d890451044b1ce34cb8259a05e4/craboutput/Muon/crab_og07_22_102320__Muon_Run2022F-22Sep2023-v2_NANOAOD/240722_082324/0000/outputfile_738.root
    2024-07-22 16:11:02,743: Getting state of job d1d81806-4817-11ef-bd53-fa163e4409e3
    ```

5. Then, at the loop [line 593](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L593), those 3 files from point 4 got mark done.
    ```
    (log line: 23958-23959)
    2024-07-22 16:11:16,192: Marking job 3 files done and 0 files failed for job 4442ee32-4824-11ef-9376-fa163eaa97bf
    2024-07-22 16:11:16,265: Marked good ['168acb70538eaefb5aba53bf8ba61cb5e89df0c9d380a667f35273cc', '39757f780b4b35dadee5784be561109fbd997c28ff91442904fc0655', '276b440c0ba7b09
    ```
    
6. Because FTS job status IS "FINISHED" (log line: 23681) so `4442ee32-4824-11ef-9376-fa163eaa97bf` got evicted from FTS IDs ongoing list `fts_jobids.txt` by [line 608](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L608). So, FileID `7fbb708684d552f510ba862f5dfb547b25fdc08d214c125bd4041781` left in stale state `SUBMITTED`, never got processed again.

-----------------

The problems here are 2 things

- We get status of FTS job again at [line 213](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L213) without handling any exception. This cause the error in the first place.
- Then we wrongly handle the bookkeeping of fileIDs, we remove the fileIDs at the stage the fileIDs does not update to FileTransferDB yet.


Quick fix would be reuse `status` at [line 196](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L196) instead.

## Comment (novicecpp, 2024-07-23T16:43:35Z)

@belforte @mapellidario Could you please verify?

## Comment (belforte, 2024-07-23T17:38:29Z)

possibly related to https://github.com/dmwm/CRABServer/issues/8323
I need some time to digest this

## Comment (belforte, 2024-07-23T19:33:14Z)

The reason why I left this aside is that I believe that no matter what happens with our handling of FTS, PostJob will give up after 24h, submit a new job, and things will be OK. Of course that requires FTS errors to be rare.
Proper handling of exception is better.

This is hard to make fully robust, since FTS_Transfer is not stateless enough with all those files 

I am struggling a bit to understand because you pointed to lines from current master, while log has lines from [v3.240527](https://github.com/dmwm/CRABServer/blob/v3.240527/scripts/task_process/FTS_Transfers.py)

## Comment (belforte, 2024-07-23T20:06:40Z)

a  bit earlier in the log FTS job `aceb8c56-4828-11ef-99a3-fa163e4409e3` checking also fails, but at line [line 196](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L196), in that case exception is handled and the job is "elegantly" skipped
```
2024-07-22 16:05:33,751: Getting state of job aceb8c56-4828-11ef-99a3-fa163e4409e3
2024-07-22 16:05:33,770: failed to retrieve status for aceb8c56-4828-11ef-99a3-fa163e4409e3
```
The problem with [line 213](https://github.com/dmwm/CRABServer/blob/bc76faca7b55d6e351348831517c54501bf26da0/scripts/task_process/FTS_Transfers.py#L213) seems that there is no exception handlling. It **may be** (but I am not sure yet) that if we `return` there similarly to what done at this FTS call few lines above, the FTS_transfer will go on and eventually properly mark in the DB all files which were removed from the `<fts_job_id>.json` files. 

We can not reuse the output of L196
```python
status = fts3.get_job_status(ftsContext, jobid, list_files=False)
```
as a substitute for L213
```python
 file_statuses = fts3.get_job_status(ftsContext, jobid, list_files=True)['files']
```
output is different.
maybe we can replace the former with the latter. This was not done in order not to ask to FTS the details of all files in a job while that jobs was simply queued, to avoid overloading the server. Of course... we do not know if the extra load would be too much or not. Maybe it was back then and things improved at FTS side...

Overall what is not good is that we track transfer status in the local `json` files and in the `tranfersdb` table, in difference places of the code separated by a  lot of things which can go wrong. It is "interesting" that the doc lines for `check_FTSJob()` says that file transfer states are updated in Oracle, but they are not !

I think that the update to Oracle was moved out of the loop on FTS jobs in order to use a single POST to crabserver for the list of all files to be udpated in a run of FTS_Transfers, to reduce load on CRABServer.

But I guess we can't rewrite the script to be solid. At least not as long as there's the hope that we can switch to Rucio.

At the moment I favor catching the exception and simply returning from `check_FTSJob`. If something else fails between changing JSON files and writing to Oracle, we will have to rely on eventual PostJob time out and resubmission anyhow. Simply it should be more rare (basically VM reboots).

## Comment (belforte, 2024-07-23T20:21:15Z)

OTOH, the reason for all those JSON files seems to be to avoid marking files in Oracle over and over, since an FTS job can contain many files and every time it returns the status of all. But if that's the case, why don't we update the content of that file AFTER a successful POST of the status to CRABServer ?

well.. better is the enemy of good . Let's try to be minimal

## Comment (novicecpp, 2024-07-24T09:40:36Z)

Thanks for confirming. 

> Overall what is not good is that we track transfer status in the local json files and in the tranfersdb table, in difference places of the code separated by a lot of things which can go wrong. 

I think it is OK because it save quite a lot of traffics to rest but you need to be extra careful handle the state there. I am not sure myself if we change to pure REST will make code more clear.

And I agree with you that simply wrap try-exception around L213 should be enough to make it more robust with less code changes.

## Comment (belforte, 2024-07-24T10:10:42Z)

thanks, I will make a PR
