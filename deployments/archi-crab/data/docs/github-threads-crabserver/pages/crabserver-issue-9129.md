# dmwm/CRABServer issue #9129: Dagman Resubmitter uses deprecated resubmit numcores option in checkMemoryWallTime

State: closed
Opened: 2025-07-10T21:15:10Z
Closed: 2025-07-14T09:55:54Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9129

## Opening post (aspiringmind-code, 2025-07-10T21:15:10Z)

Problem discovered by pipeline failure.
```
Task name:			250710_124508:crabint1_crab_20250710_144505
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw03
Status on the CRAB server:	RESUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/250710_124508%3Acrabint1_crab_20250710_144505
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250710_124508%3Acrabint1_crab_20250710_144505&from=1752147908000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_IT_Rome', 'T2_ES_IFCA', 'T2_IT_Pisa']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Failure message from server:	Problem handling 250710_124508:crabint1_crab_20250710_144505 because of 'resubmit_numcores' failure, traceback follows
				Traceback (most recent call last):
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 96, in executeAction
				    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanResubmitter.py", line 123, in execute
				    self.executeInternal(*args, **kwargs)
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanResubmitter.py", line 60, in executeInternal
				    checkMemoryWalltime(task, 'resubmit', self.logger, self.uploadWarning)
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanSubmitter.py", line 159, in checkMemoryWalltime
				    ncores = task[cmd+'_numcores']
				KeyError: 'resubmit_numcores'
```

The problem is that DagmanResubmitter relies on checkMemoryWallTime function of DagmanSubmitter script. The resubmitter should not have the resubmit_numcores option as it has been deprecated while submitter must continue to have the option.
See [here](https://github.com/aspiringmind-code/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/src/python/TaskWorker/Actions/DagmanResubmitter.py#L60) and the note in [here](https://github.com/aspiringmind-code/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/src/python/TaskWorker/Actions/DagmanSubmitter.py#L147C1-L159C35)

@belforte Should I make a copy of the checkMemoryWalltime function in Dagmanresubmitter without the numcores option?

## Comment (belforte, 2025-07-11T08:46:34Z)

hmm  isn't is enough to replace
```
ncores = task[cmd+'_numcores']
```
with `ncores = task['tm_numcores']` ?

## Comment (belforte, 2025-07-11T09:01:58Z)

In a way it is not-elegant to have this method. Why single out memory and wall time for validation ? But let's not change too much

## Comment (aspiringmind-code, 2025-07-14T09:54:10Z)

Thanks @belforte  for the one line solution!
