# dmwm/CRABServer issue #8100: All tasks with a user dataset as an input dataset fail to submit in latest prod (v3.231214)

State: closed
Opened: 2023-12-15T05:03:09Z
Closed: 2023-12-15T09:47:20Z
URL: https://github.com/dmwm/CRABServer/issues/8100

## Opening post (novicecpp, 2023-12-15T05:03:09Z)

Example task: https://cmsweb.cern.ch/crabserver/ui/task/231214_220917%3Abcho_crab_step2_GEMTnP_TTbar
Error logs (from `/data/container/TaskWorker/logs/tasks/bcho/231214_220917:bcho_crab_step2_GEMTnP_TTbar.log` in `crab-prod-tw01`):
```
2023-12-14 23:10:07,177:ERROR:Handler:Problem handling 231214_220917:bcho_crab_step2_GEMTnP_TTbar because of local variable 'partialLocationsMap' referenced before assignment failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/slc7_amd64_gcc630/cms/crabtaskworker/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 86, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/slc7_amd64_gcc630/cms/crabtaskworker/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 110, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/slc7_amd64_gcc630/cms/crabtaskworker/v3.231214-cb7a07945859cb5ccc4af98a0484c1d8/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 312, in executeInternal
    self.keepOnlyDiskRSEs(partialLocationsMap)
UnboundLocalError: local variable 'partialLocationsMap' referenced before assignment
```

This bug was introduced in PR [#8001](https://github.com/dmwm/CRABServer/pull/8001).

## Comment (novicecpp, 2023-12-15T05:26:19Z)

I think put `partialLocationsMap = {}` before [line 192](https://github.com/belforte/CRABServer/blob/94a11eb7bf795a1f344efb64fe0cea7c960386ff/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L192) should fix. I need to test and reread the code to confirm there will be no side effect.

## Comment (novicecpp, 2023-12-15T07:10:18Z)

All `possibly unbound` reported from [pyright](https://github.com/microsoft/pyright):
```
[thanayut@localhost Actions]$ pyright DBSDataDiscovery.py | grep --color 'possibly unbound'
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:267:81 - error: "secondaryBlocks" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:278:43 - error: "secondaryBlocks" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:280:81 - error: "scope" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:300:30 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:302:43 - error: "secondaryLocationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:306:33 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:311:31 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:312:31 - error: "partialLocationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:314:28 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:324:33 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:325:33 - error: "partialLocationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:326:25 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:326:47 - error: "partialLocationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:347:38 - error: "secondaryBlocksWithLocation" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:386:62 - error: "locations" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:386:72 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
  /home/thanayut/myhome/coding/cern/fork/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py:408:39 - error: "locationsMap" is possibly unbound (reportUnboundVariable)
```

For `locationsMap` and `partialLocationsMap`, I have checked with the code using it and pretty sure it ok to fix by define default value before line 192. For other value I blindly do the same and will test it with testsuite later.

## Comment (belforte, 2023-12-15T21:48:24Z)

We need to understand why this test did not catch the problem
https://github.com/dmwm/CRABServer/blob/eafa9ddbf0f068b5e0056b3068a9f42939012ed9/test/makeTests.py#L305-L317

## Comment (belforte, 2023-12-15T22:02:27Z)

OK. CCV fails to submit because we deprecated `sendPythonFolder`. Why was this not noticed ? 
Anyhow, let's fix #8104

## Comment (belforte, 2023-12-15T23:04:47Z)

hmm... CCV was not run since October :-(
![image](https://github.com/dmwm/CRABServer/assets/1837785/243bc876-84fd-43e7-902b-c0b2d9cbea9a)

## Comment (novicecpp, 2023-12-18T03:37:29Z)

My bad. I did not know I should run CCV too. **"Client"** in *"**Client**_Configuration_Validation"* threw me off, thought it wasn't related to the Server code."
