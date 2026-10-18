# dmwm/CRABClient issue #5342: crab recover "fail w/o reason"

State: closed
Opened: 2024-10-25T16:12:18Z
Closed: 2024-10-29T19:30:52Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5342

## Opening post (belforte, 2024-10-25T16:12:18Z)

```console
belforte@lxplus825/bot> crab recover -d crab_20241024_131730/
Rucio client intialized for account belforte
step kill - task already killed
Command recover failed
belforte@lxplus825/bot> echo $?
28
belforte@lxplus825/bot> 
```
Not only that, but `crab.log` has no useful information either [1]

In addition, that  makes ClientValidation test fail.

But in this case the failure is simply because there are no failed jobs to recover, everything was successful [2]

- [x] conditions that cause command exit must be logged, e.g. in places like this https://github.com/dmwm/CRABClient/blob/d1457005ac93fd14ec53bf9911a32944b1dff69f/src/python/CRABClient/Commands/recover.py#L73-L74 Most likely leverage `stepExit()` for this as the comment already indicated. Unless @mapellidario knows some reason why this is a bad idea ! 
- [x] a message should be printed to console saying what's happened, it looks to me that `recover` never does this
- [x] we may want to reserve `crab` command to have a non-zero exit code for situation where something bad happens. Or otherwise rewrite ClientValidation 

[1]
```text
DEBUG 2024-10-25 16:12:55.619 UTC:       CRAB Client version: v3.240930
DEBUG 2024-10-25 16:12:55.619 UTC:       Running on: Linux lxplus825.cern.ch 4.18.0-553.22.1.el8_10.x86_64 #1 SMP Wed Sep 11 18:02:00 EDT 2024 x86_64 x86_64 x86_64 GNU/Linux
DEBUG 2024-10-25 16:12:55.619 UTC:       Not using Singularity
DEBUG 2024-10-25 16:12:55.619 UTC:       Operating System: Red Hat Enterprise Linux 8.10 (Ootpa)
DEBUG 2024-10-25 16:12:55.619 UTC:       Executing command: 'recover'
[...]

DEBUG 2024-10-25 16:12:59.621 UTC:       stepStatus() - status, failedJobs: []
INFO 2024-10-25 16:12:59.622 UTC:        step kill - task already killed
DEBUG 2024-10-25 16:12:59.622 UTC:       stepCheckKill() - status COMPLETED
DEBUG 2024-10-25 16:12:59.622 UTC:       stepCheckKill() - command None
DEBUG 2024-10-25 16:12:59.622 UTC:       stepCheckKill() - dagStatus COMPLETED
DEBUG 2024-10-25 16:12:59.622 UTC:       stepCheckKill() - dbStatus KILLED
ERROR 2024-10-25 16:12:59.622 UTC:       Command recover failed
ERROR 2024-10-25 16:12:59.622 UTC:       Caught ClientException exception
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.240930.00/bin/crab.py", line 152, in <module>
    client()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.240930.00/bin/crab.py", line 139, in __call__
    raise CommandFailedException("Command %s failed" % str(args[0]))
CRABClient.ClientExceptions.CommandFailedException: Command recover failed
```


[2]
```text

 echo $?
28
belforte@lxplus825/bot> crab status -d crab_20241024_131730/

Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20241024_131730
Task name:			241024_111731:cmsbot_crab_20241024_131730
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	KILLED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/241024_111731%3Acmsbot_crab_20241024_131730
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=241024_111731%3Acmsbot_crab_20241024_131730&from=1729765051000&to=now
Warning:			Task killed by crab recover on '2024-10-24 14:17:38.506361', by 'cmsbot'
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (10/10)
```

## Comment (belforte, 2024-10-25T18:58:34Z)

I decided to add a `logger.info` whenever there is a condition which leads to `FAILED`. It is more clear and flexible than do it in `stepExit()`

Now the existential question. If one types `recover` but there is nothing to do, do we end with exit code 0 ? Or with error ? 
Already `crab resubmit` has a non-zero exit code when all jobs succeeded.

But we do not /can not check `resubmit` in ClientValidation.

I guess it has been one of the two:
1. change semantics
2. remove from ClientValidation

## Comment (belforte, 2024-10-28T10:32:03Z)

I am leaning toward changing current semantics and go for:
* if the recover/resubmit can not be done because everything was fine, return SUCCESS
* while still return FAILED if e.g. there's a request to get log or output but no job completed yet

## Comment (mapellidario, 2024-10-28T10:50:01Z)

> a message should be printed to console saying what's happened, it looks to me that recover never does this

> I decided to add a logger.info whenever there is a condition which leads to FAILED. It is more clear and flexible than do it in stepExit()

oops, I would suggest to add [1] to `stepExit()` in order to print messages like this [2], i must have forgot to do it myself.

in general, yes it is not trivial to decide what should be considered a "success" and how to communicate it. I will trust your style and decisions :)

---

[1]

```python
logger.info(retval.get(msg, ""))
```

[2]

https://github.com/dmwm/CRABClient/blob/d1457005ac93fd14ec53bf9911a32944b1dff69f/src/python/CRABClient/Commands/recover.py#L405

## Comment (belforte, 2024-10-28T10:52:51Z)

thanks Dario !

## Comment (belforte, 2024-10-28T11:20:47Z)

how status is reported:
* a `retval` dictionary is passed to `stepExit` and `recover` returns reporting it to the caller `crab.py` 
* in `crab.py` an exception is raised if `retval['CommandStatus']` is not `SUCCES` https://github.com/dmwm/CRABClient/blob/d1457005ac93fd14ec53bf9911a32944b1dff69f/bin/crab.py#L137-L140

## Comment (belforte, 2024-10-28T11:30:56Z)

possible changes
- the `returnDict` dictionary needs to be documented
- `crab.py` could report and log `returnDict['msg']` if present (not all command report such key) ?
- could introduce  a new `CommandStatus` : `NOTACCEPTED` ?

hmm.. only the first one makes sense. And a comment in `crab.py` will do.
The "problem" is that `returnDict` content is free, other than the common `commandStatus` each command uses it differently. `recover` uses several other command which all return a dictionary which is passed along up to `crab.py`, even if not used.

## Comment (belforte, 2024-10-28T21:50:01Z)

There is no clean way to describe possible outcome with only SUCCESS and FAILED.
I ended up introducing a new 
`retval['commandStatus'] = "NothingToDo"`
which can be used to exit the series of steps early, but will be converted in `"SUCCESS"` when reported to `crab.py`

## Comment (belforte, 2024-10-29T19:27:33Z)

after these changes:

```console
belforte@lxplus826/TC3> crab recover -d crab_20241024_174428/
Rucio client intialized for account belforte
recover process prematurely exited during checkKill step
Tasks in status COMPLETED can not be recovered
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20241024_174428/crab.log
belforte@lxplus826/TC3> echo $?
0
belforte@lxplus826/TC3> 
```

## Comment (belforte, 2024-10-29T19:29:34Z)

I verified that `crab recover` still works on a task with failed jobs.
```console
belforte@lxplus826/TC3> crab recover -d crab_20241029_174810
Rucio client intialized for account belforte
WARNING - crab report - The original task had publication disabled. recovery strategy changed to notFinished
Will save lumi files into output directory /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20241029_174810/results
Summary from jobs in status 'finished':
  Number of files processed: 39
  Number of events read: 361900
  Number of events written in EDM files: 361900
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
  Warning: 'notFinished' lumis written to notFinishedLumis.json
           The 'notFinished' lumis were calculated as: the lumis to process minus the processed lumis.
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
crab submit - recovery task will process lumis contained in file config.Data.lumiMask=/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20241029_174810/results/notFinishedLumis.json
Will use CRAB configuration file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20241029_174810/debug_sandbox/debug/crabConfig.py
Sending the request to the server at cmsweb-test2.cern.ch
Success: Your task has been delivered to the dev CRAB3 server.
Task name: 241029_192234:belforte_crab_20241029_202228
Project dir: ./crab_20241029_202228
Please use ' crab status -d ./crab_20241029_202228 ' to check how the submission process proceeds.
crab recover - submitted recovery task 241029_192234:belforte_crab_20241029_202228
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20241029_174810/crab.log
belforte@lxplus826/TC3> 
```
