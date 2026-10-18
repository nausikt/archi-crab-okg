# dmwm/CRABClient issue #5381: crab recover fail with "task QUEUE" during check kill step

State: closed
Opened: 2025-03-19T17:35:58Z
Closed: 2025-08-20T10:10:13Z
Labels: bug, HighPrio, On Hold
URL: https://github.com/dmwm/CRABClient/issues/5381

## Opening post (belforte, 2025-03-19T17:35:58Z)

in one occasion Jenkins CV failed with this log (note that crab recover is issued twice):
```
____________
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20250319_154958  
TEST_RESULT: OK                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Collecting information about original task ...
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['transferring']
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20250319_154958/crab.log
____________

____________
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=250319_145001:cmsbot_crab_20250319_154958  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20250319_154958/.requestcache not created, because it already exists.
Collecting information about original task ...
The server answered with an error.
Server answered with: Execution error
Reason is: You cannot kill a task if it is in the QUEUED status
Error Id: 5436557501f9ac496c9b006b5b6ebd46
```

Notes:
* we usually do not see this because tasks have completed but the time recover is issued. And indded the first test completed with OK properly writing "ll the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['transferring']", yet it oddily wrote it in the checkKill step. Did it issue a kill before ?
* issuing the command again (supposedly to check the different syntax, a bit useless IMHO) we got
```
Collecting information about original task ...
The server answered with an error.
Server answered with: Execution error
Reason is: You cannot kill a task if it is in the QUEUED status
```
* is that message referring to a kill isssued in the previous command ? Or did recovery really try to issue a kill again ? 

FYI @sinonkt

## Comment (belforte, 2025-05-21T14:16:52Z)

I reviewed the code. Findings:
1. recover alwasys go through the `stepKill`
2. but if status is QUEUED on command KILL, exits the step w/o issuing a `crab kill`

Conclusion is that I have no clue and can not reproduce. The best that we can do is to change `crab recover` to `crab --debug recover` so to have more logging in case this happens again.

Until there is more info. Put this on hold.

Moreover, we do not test recover anymore since moving to gitlab pipeline. Need to recover consistency with old tests there.

## Comment (belforte, 2025-05-21T14:31:17Z)

related issues in CRABServer repo:
1. add back `crab recover` to tests: https://github.com/dmwm/CRABServer/issues/9086
2. add `--debug` option: https://github.com/dmwm/CRABServer/issues/9087

## Comment (belforte, 2025-08-20T10:10:13Z)

We have not seen this lately. Maybe it was simply an earlier version of `crab recover`. Let's close.
