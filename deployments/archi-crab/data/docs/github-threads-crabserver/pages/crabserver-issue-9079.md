# dmwm/CRABServer issue #9079: defer PostJob for a longer time when waiting on Rucio

State: closed
Opened: 2025-05-16T15:21:39Z
Closed: 2026-04-07T11:01:33Z
Labels: Type: Enhancement, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/9079

## Opening post (belforte, 2025-05-16T15:21:39Z)

We may be waiting for Rucio  transfer to many days (failing the PostJob will not help since we can not resubmit jobs which failed in transfer, Rucio will not accept an old LFN with a different checksum).

In this case it is better not to run many PostJobs uselessly every 30min, since we may end up overloading the AccessPoint resources. Better to increase defer time.

The best (only?) way seems to exit immediately from `dag_bootstrap.sh` with exit code 4, i.e. deferral stays at 30min (hardcoded in DAG description file), but PJ duration is minimal and Python is not started, saving a lot on memory.

See
https://github.com/dmwm/CRABServer/issues/8429#issuecomment-2886703358

## Comment (belforte, 2025-05-16T16:41:33Z)

one idea
* `grep DEFERRING` in PostJob log to find how many times we tried.
   * after 10 times exit immediately with 50% chance and log DEFERRING
   * after 20 times with 10%
   * ...

something like this
| number of DEFERRING | hours since completion | probabiliyt of running PostJob|Hours between PJ runs (average) |
| - | - | - |- |
| 0 | 0 | 1 | 0.5 |
| 8 | 4 | 1/2 | 1 |
|24 |12 | 1/6  |3 |
|48 |24 | 1/12  |6 |
| 96 | 48 | 1/24 | 12 |

which is the simple formula `if Ndefer > 8, prob of runnin PJ is 1/(Ndefer/4)`

I think that the "run or not run" can be done via `/usr/bin/shuf` see [stackoverflow](https://stackoverflow.com/a/2556282/13696042)

## Comment (belforte, 2025-05-21T15:39:53Z)

PostJob is called by DAGMAN via this POST script macro (broken into multiple lines for readibility)
```
SCRIPT DEFER 4 1800 POST Job1 dag_bootstrap.sh POSTJOB $JOBID $RETURN $RETRY $MAX_RETRIES
250520_093145:belforte_crab_20250520_113141 1 
/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/StefanoTest-240524/250520_093145/0000
/store/user/belforte/GenericTTbar/Stefano-Test-240524/250520_093145/0000
cmsRun_1.log.tar.gz conventional kk_1.root
```
as per
https://github.com/dmwm/CRABServer/blob/accd4c8ae43333584366d76cb263155972bfa7f9/src/python/TaskWorker/Actions/DagmanCreator.py#L55

so the arguments for `dag_bootstrap.sh` are:
|`#` |arg| meaning/use
| - |-|-|
1 | stage | (PREJOB/PREDAG/POSTJOB)
2|$JOBID |   the HTCondor job ID [ClusterId.ProcId] of the node job [HTC doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-introduction.html#special-script-argument-macros), irrelevant for this
3|$RETURN  | the return value of the HTCondor job [HTC doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-introduction.html#special-script-argument-macros), irrelevant for this
4|$RETRY  | the current job retry #, starts at 0 [HTC doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-introduction.html#special-script-argument-macros)
5|$MAX_RETRIES | the max number of retries, irrelevant for this
6|TaskName | irrelevant for this
7|crabId | a.k.a. the job number. toghether with $RETRY identifies the postJob log file 
8|temp_dir | irrelevant for this
9|out_dir | irrelevant for this
10|log file tarball | irrelevant for this
11|stage | conventional/probe/tail... irrelevant for this
12- |output files | irrelevant for this

see also
https://github.com/dmwm/CRABServer/blob/accd4c8ae43333584366d76cb263155972bfa7f9/src/python/TaskWorker/TaskManagerBootstrap.py#L13-L14
and
https://github.com/dmwm/CRABServer/blob/accd4c8ae43333584366d76cb263155972bfa7f9/src/python/TaskWorker/Actions/PostJob.py#L1575-L1594

## Comment (belforte, 2026-03-31T14:31:29Z)

this does not work well in practice. With a decreasing probability to run PJ we may and up not running it for a long time even after transfers are done like in the example below[*]. I think that we should want to make sure that waiting time is e.g. never more then twice the foreseen average in the [table](https://github.com/dmwm/CRABServer/issues/9079#issuecomment-2887210722).
Or replace the probability with a deterministic condition on number of deferrals.

[*] from https://cmsweb.cern.ch/scheddmon/059/crabint1/260330_160719:crabint1_crab_rucio_transfers_20260330_180716/postjob.3.0.txt
```

/GenericTTbar/crabint1-ruciotransfers-1774886836-94ba0e06145abd65ccb1d21786dc7e1d/USER
Tue, 31 Mar 2026 08:11:55 CEST(+0200):INFO:PostJob ====== Starting to check for ASO transfers.
Tue, 31 Mar 2026 08:11:55 CEST(+0200):DEBUG:PostJob Querying ASO RDBMS database.
Tue, 31 Mar 2026 08:11:55 CEST(+0200):INFO:PostJob Got statuses: submitted; 13.0 hours since transfer submit.
Tue, 31 Mar 2026 08:11:55 CEST(+0200):INFO:PostJob Deferring the execution of the post-job.
Tue, 31 Mar 2026 08:11:55 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 4  : DEFERRING. PostJob will run again after 30 min
Ended TaskManagerBootstrap with code 4
Tue Mar 31 08:41:58 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 09:12:00 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 09:42:03 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 10:12:05 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 10:42:08 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 11:12:11 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 11:42:13 AM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 12:12:17 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 12:42:19 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 01:12:21 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 01:42:22 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 02:12:25 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 02:42:27 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 03:12:30 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 03:42:33 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
Tue Mar 31 04:12:36 PM CEST 2026 dag_boostrap.sh DEFERRING. PostJob will run again after 30 min
```

## Comment (belforte, 2026-03-31T14:37:49Z)

@aspiringmind-code do you feel like helping with changing the script ? Your bash skills are vastly superior to mine, and it is good to have an exchange of ideas on what is the best strategy.

https://github.com/dmwm/CRABServer/blob/18b9ab757c1d5ce7268e0ee7b6f744516ebaa054/scripts/dagman/dag_bootstrap.sh#L26-L40

## Comment (belforte, 2026-03-31T16:21:20Z)

I have tentatively added some ugly bash in #9290 which should make sure PJ is run at least every 8 hours.
I am sure this could be done better.,

## Comment (aspiringmind-code, 2026-04-07T09:01:53Z)

@belforte Sure! I'd be happy to help.

## Comment (belforte, 2026-04-07T10:52:19Z)

it is also quite low in priority, esp. because the situation which triggered me to look at this was a real hopeless one (file lost from /store/temp !)
