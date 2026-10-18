# dmwm/CRABServer issue #9059: report exit code for jobs which will be automatically retried

State: closed
Opened: 2025-04-29T15:32:11Z
Closed: 2025-05-09T10:18:00Z
Labels: Type: Enhancement, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/9059

## Opening post (belforte, 2025-04-29T15:32:11Z)

Currently crab status does not show the exit code for failed jobs which will be retried, only when job is terminally failed the exit code is added to the status cache and displayed.

It would be better if CRAB status reports the exit code of the failed job, if we can do w/o confusing users !

Code to change is in here
https://github.com/dmwm/CRABServer/blob/1d41fa3554c92583a3ad2c03036e74f9d24f83eb/scripts/task_process/cache_status.py#L226-L230

DAG nodes go in `failed` only when all automatic retries have been exhausted.

Need some way to consistently reproduce so that I can compare `crab status` output "across  changes"

## Comment (belforte, 2025-04-29T15:33:17Z)

put high in priority because if I wait I will forget how `cache_status.py` works !!

## Comment (belforte, 2025-04-29T19:41:57Z)

at first sight the fix is to change
```python
if 'State' in statedict and statedict['State'] == 'failed' and jobid in data: 
```
to
```python
if 'State' in statedict and statedict['State'] in ['cooloff', 'failed'] and jobid in data: 
```

## Comment (belforte, 2025-04-29T19:43:50Z)

take this chance to also show that exit status was 0 for jobs in transferring ? which now reports `Unknown`
Or keep it like this to signal that we are waiting for the transfer exit code ?


```text
ips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 

No publication information (publication has been disabled in the CRAB configuration file)

Extended Job Status Table:

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
   1 transferring T1_UK_RAL               0:14:45        821         83          0          0    0:03:40         Unknown
   2 transferring T1_DE_KIT               0:17:22       1234         75          0          0    0:03:41         Unknown
   3 transferring T1_DE_KIT               0:10:59       1226         80          1          0    1:00:09         Unknown
   4 transferring T1_DE_KIT               0:14:47       1258         86          0          0    0:03:41         Unknown
   5 transferring T1_RU_JINR              0:17:30        737         64          0          0    0:03:38         Unknown
   6 transferring T1_RU_JINR              0:14:26        730         57          0          0    0:03:40         Unknown
   7 transferring T1_DE_KIT               0:15:58       1224         73          0          0    0:03:41         Unknown
   8 transferring T1_RU_JINR              0:15:18        733         42          0          0    0:03:38         Unknown
   9 transferring T1_DE_KIT               0:16:27        811         74          0          0    0:03:41         Unknown
  10 transferring T1_DE_KIT               0:13:32       1235         66          0          0    0:03:39         Unknown

Warning: the max jobs runtime is less than 30% of the task requested value (60 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Summary of run jobs:
 * Memory: 737MB min, 1258MB max, 1001MB ave
 * Runtime: 0:10:59 min, 0:17:30 max, 0:15:06 ave
 * CPU eff: 42% min, 86% max, 70% ave
 * Waste: 1:33:11 (38% of total)

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250429_183410/crab.log
belforte@lxplus807/TC3> 
```

## Comment (belforte, 2025-05-01T11:00:02Z)

number of retries is wrong in crab status when job finally fails
```text
Extended Job Status Table:

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
   1 failed       T2_CH_CERN              0:04:14         81          0          2          0    0:07:27            8028
```
it should be 3 retries, not 2 ! Given that it was reported as 2 already when the last retry had to be done
```text

 Job State        Most Recent Site        Runtime   Mem (MB)      CPU %    Retries   Restarts      Waste       Exit Code
   1 toRetry      T2_CH_CERN              0:03:15          0          0          2          0    0:02:12         Unknown
```

Of course there's the usual ambiguity whether we count 1 job + N retries or call every iteration a retry.

The 2 comes from `cache_status.py` and is there both in new and old version of the cache file.

## Comment (belforte, 2025-05-01T17:17:30Z)

hmm... need also to catch when jobs was resubmitted and status is `idle` instead of `cooloff`. What do we want when status is `running` ? "unknwown" or "exit code from last try" ?

## Comment (belforte, 2025-05-01T17:18:27Z)

maybe change in  crab status output the last column from 'Exit Code' to `Last Exit Code` ?

## Comment (belforte, 2025-05-02T13:00:58Z)

I found that things still work by removing the check on ` staatedict['State'] ` in https://github.com/dmwm/CRABServer/blob/1d41fa3554c92583a3ad2c03036e74f9d24f83eb/scripts/task_process/cache_status.py#L227

ExitCode is correctly reported as Unknown initially and then set to the last job attempt. We will make this clear in `crab status` as indicated in previous comment.

## Comment (belforte, 2025-05-07T19:16:28Z)

There is a bug. See https://github.com/dmwm/CRABClient/issues/5389

## Comment (belforte, 2025-05-07T19:52:10Z)

these two codes are not equivalent :-(

![Image](https://github.com/user-attachments/assets/214d7254-2557-4b2f-9d64-dfd3a69fdeb8)

https://github.com/dmwm/CRABServer/pull/9061/files#diff-4cd2ad45dbb4fde4b826893461177ff6ca028a36bdc6127977c76bb0d5acf54eL226-R231

@aspiringmind-code  I have added comments in the code to clarify what the code should do, hopefully clarifying the issue. See the commit above.
I will like advice on how to fix, I find the old format very confusing (I like to blame that for the mistake !)
```
    for jobid, statedict in nodes.items():
        if 'State' in statedict and statedict['State'] == 'failed' and jobid in data:
            # pick error info from last retry (SB: AFAICT only last retry is listed anyhow)
            for key in data[jobid]:
                statedict['Error'] = data[jobid,key]
```
note that I had changed `data` to `fjrReports` in an attempt to clarify.

Let's share the suffering for not having noticed this when looking at the code :-)

## Comment (aspiringmind-code, 2025-05-08T15:58:27Z)

How about we use max() to replace the inner loop and keep the outer loop as is?
```
    # Iterate over all jobs in `nodes` that are also present in `fjrReports`.
    for jobid, statedict in nodes.items():
        if jobid in fjrReports:
            # Find the last retry attempt by taking the maximum key (retry number).
            last_retry = max(fjrReports[jobid], key=int)  # Get the latest retry (largest key).            
            # Set the error summary from the last retry attempt.
            statedict['Error'] = fjrReports[jobid,last_retry]
```

## Comment (belforte, 2025-05-08T16:05:20Z)

thanks @aspiringmind-code . Let me digest this a a bit. There is already code which makes sure that only last retry is present
https://github.com/dmwm/CRABServer/blob/d0705282d25a832422fa92c6eb513370f5e1dc0b/scripts/task_process/cache_status.py#L455-L462

Maybe the original developer wanted to be double sure

I am not familiar with that `max(.., key=int)` will it cast the retry which now is a string into an int ? Not that >10 retries are possible atm, but... one never knows.

## Comment (belforte, 2025-05-08T16:15:12Z)

this appears to do, but I find it ugly and not clear
```python
 list(fjrReports[jobid].values())[0]
```

```
>>> jobid='2'      
>>> fjrReports
{'2': {'0': [5, 'Error while running CMSSW:\n', {}]}}
>>> error = list(fjrReports[jobid].values())[0]
>>> error
[5, 'Error while running CMSSW:\n', {}]
>>> 
```

## Comment (belforte, 2025-05-08T16:22:04Z)

OTOH, there's possibly no alternative to turning the `{'0': [5, 'Error while running CMSSW:\n', {}]}` dictionary into a list, pretty much as the original was doing by iterating over the dictionary content
```python
for retry in fjrReports[jobid]:
    nodes[jobid,'Error'] = fjrReports[jobid,retry]
```

## Comment (belforte, 2025-05-08T16:43:48Z)

after reading https://docs.python.org/3/library/functions.html#max your solution is indeed very elegant. I guess I did not realize that a dictionary is an iterable https://docs.python.org/3/glossary.html#term-iterable
🙇
