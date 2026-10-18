# dmwm/CRABServer issue #7660: bug found in taperecall

State: closed
Opened: 2023-06-12T09:27:11Z
Closed: 2023-06-15T07:46:53Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/7660

## Opening post (mapellidario, 2023-06-12T09:27:11Z)

Wa found a bug in taperecall, looking at the logs

`/data/container/TaskWorker/logs/tasks/dwalter/230612_073229:dwalter_crab_Muon_Run2022D_357705.log ` [1]


---

[1]

<details>

```plaintext
2023-06-12 09:32:50,771:DEBUG:Worker:Process-3: SUBMIT work on 230612_073229:dwalter_crab_Muon_Run2022D_357705 completed in 8 seconds: Status: ERROR
Error = Problem handling 230612_073229:dwalter_crab_Muon_Run2022D_357705 because of local variable 'msg' referenced before assignment failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 85, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 103, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 332, in executeInternal
    self.requestTapeRecall(dataToRecall=dataToRecall, sizeToRecall=totalSizeBytes,
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 434, in requestTapeRecall
    self.requestRucioTapeRecall(dataToRecall, sizeToRecall, tapeLocations, msgHead=msg)
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 505, in requestRucioTapeRecall
    self.setTaskToTapeRecall(taskname=self.taskName, ruleId=ruleId,
  File "/data/srv/TaskManager/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/slc7_amd64_gcc630/cms/crabtaskworker/v3.230602-4d5d11d8ec1192e19dfb007ecbdb30fc/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 639, in setTaskToTapeRecall
    raise TaskWorkerException(msg)
UnboundLocalError: local variable 'msg' referenced before assignment
```

</details>

## Comment (belforte, 2023-06-12T09:34:49Z)

sorry

## Comment (novicecpp, 2023-06-12T09:49:26Z)

Thanks Dario. A New tag is coming.

## Comment (novicecpp, 2023-06-12T10:34:59Z)

It is fine, Stefano. Let's focus on how to improve this.

I saw three things:
- Unit test: especially when we do refactor stuff. It will ensure that the new refactor code behaves like the old one.
- Pylint: we have too many errors/warnings in the pylint report, making us skip reading entirely. Shall we start fixing it?
- Identify errors of "submitfailed" in monitoring.

What do you guys think?

Note that the alert we set up is working really well. I got a message from https://mattermost.web.cern.ch/cms-o-and-c/pl/bextnuzj7jnb7bouwyzkg3q48w and went to [the last failure 60m ago](https://cmsweb.cern.ch/crabserver/prod/task?subresource=lastfailures&minutes=60) in case something broke. Unfortunately, it broke :)

## Comment (belforte, 2023-06-12T10:40:50Z)

* I did not get the alert mail :man_shrugging: . Also my MatterMost client was stuck after changing wifi from home to office.. oh well
* we've talked about unit tests for years.. let's see your concrete example from your RT refactoring and try to figure out how much effort we are talking about
* pylint: yes ! For sure there are things marked in bold which we can live with. Did it pick the missing `msg` this time ?

## Comment (novicecpp, 2023-06-12T10:55:41Z)

pylint: I am not sure because the report is now gone. But it looks like it was picked because it reported "20 warnings and errors that must be fixed" in [here](https://github.com/dmwm/CRABServer/pull/7641#issuecomment-1561413541), usually not more than 5.

## Comment (belforte, 2023-06-15T07:45:45Z)

@novicecpp shall we close (again) this and move pylint to a new issue ?

## Comment (novicecpp, 2023-06-15T07:46:53Z)

Sure. Thanks.
