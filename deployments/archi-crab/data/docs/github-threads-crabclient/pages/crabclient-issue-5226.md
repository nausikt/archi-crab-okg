# dmwm/CRABClient issue #5226: error(s) in last PR

State: closed
Opened: 2023-10-17T21:39:27Z
Closed: 2023-10-17T21:53:14Z
URL: https://github.com/dmwm/CRABClient/issues/5226

## Opening post (belforte, 2023-10-17T21:39:27Z)

I must have done something wrong since using master HEAD now

`crab tasks  --days=1`  works (I had tested this wen committing)

But `crab tasks  --days=1  --status=HOLDING` fails !! (thanks [Jenkins](https://github.com/dmwm/CRABServer/issues/7950#issuecomment-1767201615) ! )

```
belforte@lxplus810/TC3> crab tasks  --days=1  --status=HOLDING 
No tasks found from 2023-10-16 until 2023-10-17 with status HOLDING
ERROR: TypeError: list indices must be integers or slices, not str
```

while the production version 
```
belforte@lxplus810/TC3> crab tasks  --days=1  --status=HOLDING 
No tasks found from 2023-10-16 until 2023-10-17 with status HOLDING
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus810/TC3> 
```

`crab.log` reports
```
ERROR 2023-10-17 21:36:06.538 UTC: 	 Unhandled Exception!
ERROR 2023-10-17 21:36:06.538 UTC: 	 list indices must be integers or slices, not str
Traceback (most recent call last):
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 158, in <module>
    client()
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 144, in __call__
    if returnDict['commandStatus'] != 'SUCCESS':
TypeError: list indices must be integers or slices, not str

```

## Comment (belforte, 2023-10-17T21:41:04Z)

I must have missed something, becasue in this case the API returns an empty list instead of the expected dictionary
```
belforte@lxplus810/TC3> ./TestAPI.py tasks  --days=1  --status=HOLDING
testing:  tasks
No tasks found from 2023-10-16 until 2023-10-17 with status HOLDING
command returned:
[]
belforte@lxplus810/TC3> 
```

I guess there are multiple `return` statements in `tasks.py` and I did not take care of all of them.
