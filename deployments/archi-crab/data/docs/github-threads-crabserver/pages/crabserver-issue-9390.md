# dmwm/CRABServer issue #9390: add a classAd to flag when IgnoreLocality is used and propagate to MONIT

State: closed
Opened: 2026-08-20T20:04:35Z
Closed: 2026-08-24T21:45:16Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9390

## Opening post (belforte, 2026-08-20T20:04:35Z)

we need to be able to easily see whether given jobs/tasks used IgnoreLocality or not, and to select based on that in OS/Grafana.

Will introduce a new classAd CRAB_IgnoreLocality = True/False to reflect the task table column task['tm_ignore_locality']

## Comment (belforte, 2026-08-20T20:05:52Z)

ref https://cms-talk.web.cern.ch/t/wasted-cpu-time-corehours-in-crab/147739/10

## Comment (belforte, 2026-08-24T19:54:09Z)

hmm
`        jobSubmit['My.CRAB_IgnoreLocality'] = classad.quote(task['tm_ignore_locality'])`
leads to 
`CRAB_IgnoreLocality = "F"` or ` = "T" `
Which may not be the best for OS

## Comment (belforte, 2026-08-24T20:03:55Z)

should use correct True/False expression for classAds
e.g. we have
https://github.com/dmwm/CRABServer/blob/1da960d47eac79e91d3d623945a46b6098186e96/src/python/TaskWorker/Actions/DagmanCreator.py#L346
and
https://github.com/dmwm/CRABServer/blob/1da960d47eac79e91d3d623945a46b6098186e96/src/python/TaskWorker/Actions/DagmanCreator.py#L400

`0` and `1` are OK since they will be mapped to `False/True` in the spider's code
https://github.com/dmwm/cms-htcondor-es/blob/b1c8998e08702ca230831d10cf7910c9dd33cd8d/src/htcondor_es/convert_to_json.py#L1380-L1381

## Comment (belforte, 2026-08-24T20:14:15Z)

also `jobSubmit['My.CRAB_IgnoreLocality']=True` or `=False` will do. And is more clear ! 
The classAd will be "true" or "false" but when extracted in python API it returns "True" or "False" (the python booleans).

```
>>> ad={}
>>> import classad2 as classad
>>> ad=classad.ClassAd()
>>> 
>>> ad['test']=True
>>> print(ad)

    [
        test = true
    ]
>>> ad['test']
True
>>> 
```

## Comment (belforte, 2026-08-24T21:43:36Z)

But of course I had forgotten that ` jobSubmit['My.CRAB_IgnoreLocality']` is an `htcondor.Submit()` object where values must always be assigned as string !!
So:
```python
jobSubmit['My.CRAB_IgnoreLocality'] = "true" if task['tm_ignore_locality'] == 'T' else "false"
```
