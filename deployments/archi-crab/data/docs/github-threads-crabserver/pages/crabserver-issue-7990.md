# dmwm/CRABServer issue #7990: undefined var in TapeRecallManager

State: closed
Opened: 2023-11-01T20:47:30Z
Closed: 2023-11-01T21:13:37Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7990

## Opening post (belforte, 2023-11-01T20:47:30Z)

```
belforte@crab-prod-tw01/recurring> tail TapeRecallManager_231101-1946.log
2023-11-01 19:46:07,195:ERROR:BaseRecurringAction:Error while runnig recurring action.
2023-11-01 19:46:07,196:ERROR:BaseRecurringAction:local variable 'mag' referenced before assignment
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/slc7_amd64_gcc630/cms/crabtaskworker/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/lib/python3.8/site-packages/TaskWorker/Actions/Recurring/BaseRecurringAction.py", line 35, in execute
    self._execute(config, task)
  File "/data/srv/TaskManager/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/slc7_amd64_gcc630/cms/crabtaskworker/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/lib/python3.8/site-packages/TaskWorker/Actions/Recurring/TapeRecallManager.py", line 46, in _execute
    self.handleRecall()
  File "/data/srv/TaskManager/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/slc7_amd64_gcc630/cms/crabtaskworker/v3.231016-8dba9cdb724991c8853a7928fe5a3b4a/lib/python3.8/site-packages/TaskWorker/Actions/Recurring/TapeRecallManager.py", line 141, in handleRecall
    mag += (f"This recall has lasted {waitDays} already and it is > {okFraction}% complete")
UnboundLocalError: local variable 'mag' referenced before assignment
belforte@crab-prod-tw01/recurring> 

```
