# dmwm/CRABServer issue #7671: refactor TapeRecallManager to fix pylint

State: closed
Opened: 2023-06-15T16:55:56Z
Closed: 2024-07-29T16:28:22Z
Labels: Status: Done, Priority: High, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7671

## Opening post (belforte, 2023-06-15T16:55:56Z)

current errors:
```

    src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py
        W0511, line 159: TODO this is also a candidate for TaskWorker/TaskUtils.py
        W0511, line 176: TODO this is duplicated in TaskWorker/Actions/TaskAction.py but it is not possible
        W0511, line 188: TODO this is also a candidate for TaskWorker/TaskUtils.py
        W0511, line 199: TODO this is also a candidate for TaskWorker/TaskUtils.py
        W0703, line 166 in TapeRecallManager.getTasks: Catching too general exception Exception
        W0201, line 38 in TapeRecallManager._execute: Attribute 'config' defined outside __init__
        W0201, line 139 in TapeRecallManager.init: Attribute 'restHost' defined outside __init__
        W0201, line 139 in TapeRecallManager.init: Attribute 'dbInstance' defined outside __init__
        C0103, line 36 in TapeRecallManager._execute: Method name "_execute" doesn't conform to '([a-z,a-zA-Z0-9]*$)|([_]{2}[a-z]+[_]{2}$)|([a-z,a-zA-Z0-9]*_$)' pattern
        C0209, line 59 in TapeRecallManager.handleKill: Formatting a regular string which could be a f-string
        C0209, line 80 in TapeRecallManager.handleRecall: Formatting a regular string which could be a f-string
        C0209, line 94 in TapeRecallManager.handleRecall: Formatting a regular string which could be a f-string
        C0103, line 217: Constant name "twconfig" doesn't conform to UPPER_CASE naming style

```

The bad ones (in bold in original) are W0201

should look at using a new class to properly use `__init__` as done in https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py

## Comment (belforte, 2024-06-28T16:59:07Z)

will do at same time as https://github.com/dmwm/CRABServer/issues/7989 since it relies in adding `TaskUtils.py` which is useful for both
