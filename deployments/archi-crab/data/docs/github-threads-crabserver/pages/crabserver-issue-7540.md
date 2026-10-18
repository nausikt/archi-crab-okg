# dmwm/CRABServer issue #7540: Failure message on submitfailed sometimes contains an awful traceback

State: closed
Opened: 2023-02-17T11:35:32Z
Closed: 2023-02-17T13:00:00Z
Labels: Type: Bug, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/7540

## Opening post (mapellidario, 2023-02-17T11:35:32Z)

A user reported that he is not able to understand why his job submission failed because the TW only reports an awful traceback instead of a meaningful message [1]

[1] https://cms-talk.web.cern.ch/t/crab-submitfailed-python-local-variable-problem/20417

## Comment (mapellidario, 2023-02-17T11:44:13Z)

found the problem in `/data/container/TaskWorker/logs/processes/proc.c3id_5.pid_30435.txt.2023-02-16`

```plaintext
023-02-16 20:20:18,467:DEBUG:Handler:Starting <TaskWorker.Actions.StageoutCheck.StageoutCheck object at 0x7f9d2215aee0> on 230216_191933:mkovac_crab_TnP_L1
2023-02-16 20:20:18,738:INFO:ServerUtilities:Will use GFAL2 commands for checking write permissions
2023-02-16 20:20:18,742:INFO:StageoutCheck:Will check stageout at T2_CH_CERNBOX
2023-02-16 20:20:18,743:WARNING:RucioUtils:Try Rucio lfn2pn with operation third_party_copy_write
2023-02-16 20:20:18,812:WARNING:RucioUtils:Rucio lfn2pfn resolution for third_party_copy_write failed with:
RSE does not exist.
Details: RSE 'T2_CH_CERNBOX' cannot be found in vo 'def'
Try next one.
2023-02-16 20:20:18,869:INFO:ServerUtilities:Warning: Failed to delete file 230216191933mkovaccrabn1_crab3check.tmp
2023-02-16 20:20:18,896:ERROR:Handler:Problem handling 230216_191933:mkovac_crab_TnP_L1 because of local variable 'ex' referenced before assignment failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/slc7_amd64_gcc630/cms/crabtaskworker/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 80, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/slc7_amd64_gcc630/cms/crabtaskworker/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/lib/python3.8/site-packages/TaskWorker/Actions/StageoutCheck.py", line 99, in execute
    pfn = getWritePFN(self.rucioClient, siteName=self.task['tm_asyncdest'], lfn=lfn, operations=['third_party_copy_write'], logger=self.logger)
  File "/data/srv/TaskManager/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/slc7_amd64_gcc630/cms/crabtaskworker/v3.221109-f8ed2a1c40e907142ff2393b48c2538a/lib/python3.8/site-packages/RucioUtils.py", line 64, in getWritePFN
    msg += ' with exception :\n%s' % str(ex)
UnboundLocalError: local variable 'ex' referenced before assignment
```

## Comment (mapellidario, 2023-02-17T12:34:44Z)

In python3, Exceptions go out of scope when the loop exits

```plaintext
[crab3@crab-dev-tw02 TaskManager]$ python3
Python 3.8.2 (default, Jan 22 2021, 17:57:37)
[GCC 6.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> for i in range(1):
...     try:
...         raise
...     except Exception as ex:
...         print(ex)
...         print(dir())
...
No active exception to reraise
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'ex', 'i']
>>> print(dir())
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'i']
>>>
```

So we can not access directly the exception at line 64 in [1], we need to save the exception content in a "proxy" variable.

[1]

https://github.com/dmwm/CRABServer/blob/9e822e562a3200c2eacebb5f93d66ca2b17d3583/src/python/RucioUtils.py#L53-L65

## Comment (belforte, 2023-02-17T12:48:28Z)

could we simply break out of all loops at line 61 by moving line 65 there ? Ah.. no. Need to try all operations in case one is OK. Maybe simply remove line 64 ? Given that we can have multiple operations failing with possibly different errors...
