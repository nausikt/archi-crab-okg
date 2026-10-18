# dmwm/CRABServer issue #8626: ZeroDivisionError from TapeRecallManager.py

State: closed
Opened: 2024-08-16T09:04:04Z
Closed: 2024-08-19T17:14:45Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8626

## Opening post (novicecpp, 2024-08-16T09:04:04Z)

I found it while scrolling at TW logs: 
```
2024-08-16 10:42:17,752:INFO:TapeRecallManager,119:Rule 6b6464d4a4e44cee98738bca29b68a37 is INJECT
2024-08-16 10:42:17,752:ERROR:BaseRecurringAction,38:Error while runnig recurring action.
2024-08-16 10:42:17,753:ERROR:BaseRecurringAction,39:integer division or modulo by zero
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Recurring/BaseRecurringAction.py", line 35, in execute
    self._execute(config, task)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Recurring/TapeRecallManager.py", line 46, in _execute
    self.handleRecall()
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Recurring/TapeRecallManager.py", line 137, in handleRecall
    okFraction = ok * 100 // total
ZeroDivisionError: integer division or modulo by zero
```

## Comment (belforte, 2024-08-16T09:44:15Z)

thanks

## Comment (belforte, 2024-08-16T12:46:54Z)

to have total=0 it must be a rule with no locks (no ok, no rep, no stuck). interesting.

AH.. the rule was still in INJECTING. That explains. I will add a check on rule status.
