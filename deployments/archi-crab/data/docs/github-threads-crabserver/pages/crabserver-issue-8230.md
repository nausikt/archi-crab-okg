# dmwm/CRABServer issue #8230: tasks stuck in QUEUED if Rucio quota check fails

State: closed
Opened: 2024-02-05T08:09:34Z
Closed: 2024-02-13T15:31:27Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8230

## Opening post (belforte, 2024-02-05T08:09:34Z)

CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240205_090454
Task name:			240205_080458:belforte_crab_20240205_090454
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	QUEUED on command SUBMIT
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240205_080458%3Abelforte_crab_20240205_090454
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=240205_080458%3Abelforte_crab_20240205_090454&from=1707116699000&to=now
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20240205_090454/crab.log

in TW log:
```
Starting <TaskWorker.Actions.StageoutCheck.StageoutCheck object at 0x7ff96ff20fd0> on 240205_080458:belforte_crab_20240205_090454
Checking Rucio quota from account belforte.
Problem handling 240205_080458:belforte_crab_20240205_090454 because of RSE does not exist.
Details: RSE 'T2_CH_CERNBOX' cannot be found in vo 'def' failure, traceback follows
Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/Handler.py", line 86, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/StageoutCheck.py", line 87, in execute
    quotaCheck = isEnoughRucioQuota(self.rucioClient, self.task['tm_asyncdest'], rucioAccount)
  File "/data/repos/CRABServer/src/python/ServerUtilities.py", line 1097, in isEnoughRucioQuota
    quotas = list(rucioClient.get_local_account_usage(account, site))
  File "/data/srv/TaskManager/v3.240122-42ae10d09d91cac3852a0ea083265c73/slc7_amd64_gcc630/external/py3-rucio-clients/1.29.10/lib/python3.8/site-packages/rucio/client/accountclient.py", line 327, in get_local_account_usage
    raise exc_cls(exc_msg)
rucio.common.exception.RSENotFound: RSE does not exist.
Details: RSE 'T2_CH_CERNBOX' cannot be found in vo 'def'
```
