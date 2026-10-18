# dmwm/CRABServer issue #8774: automatic splitting fails in TW v3.241107

State: closed
Opened: 2024-11-07T15:49:45Z
Closed: 2024-11-08T08:22:53Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8774

## Opening post (belforte, 2024-11-07T15:49:45Z)

```
Problem handling 241107_153134:belforte_crab_20241107_163129 because of 'avgEvtsPerLumi' failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 98, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 1216, in execute
    info, params, inputFiles, splitterResult = self.executeInternal(*args, **kw)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanCreator.py", line 1202, in executeInternal
    splittingSummary.addJobs(jobs)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Splitter.py", line 165, in addJobs
    avgEventsPerLumi = sum([f['avgEvtsPerLumi'] for f in job['input_files']])/float(len(job['input_files']))
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Splitter.py", line 165, in <listcomp>
    avgEventsPerLumi = sum([f['avgEvtsPerLumi'] for f in job['input_files']])/float(len(job['input_files']))
KeyError: 'avgEvtsPerLumi'
```

at first sight I moved splittingSummary in DagmanCreator but it does not work for automatic splitting.

https://github.com/dmwm/CRABServer/blob/97f447747265684589ac1f5be773eed80de02239/src/python/TaskWorker/Actions/DagmanCreator.py#L1199-L1204

## Comment (belforte, 2024-11-07T16:26:43Z)

and the problem is from these lines 
https://github.com/dmwm/CRABServer/blob/97f447747265684589ac1f5be773eed80de02239/src/python/TaskWorker/Actions/Splitter.py#L163-L168

## Comment (belforte, 2024-11-07T16:35:02Z)

indeed in this case the `<class 'WMCore.DataStructs.File.File'>` object `f` does not have the key 'avgEvtsPerLumi' [1]
Same for the other 4 jobs here (automatic splitting creates the 5 probe jobs in the Splitting action in TW using FileBased splitting [2])

Yet `'avgEvtsPerLumi'` is present also in WMCore/JobSplitting/FileBased.py

[1] 
```
(Pdb) jobs[0,'input_files',0].keys()
dict_keys(['lfn', 'size', 'events', 'checksums', 'runs', 'merged', 'last_event', 'first_event', 'locations', 'parents', 'block', 'workflow'])
(Pdb) 
```

[2]
https://github.com/dmwm/CRABServer/blob/97f447747265684589ac1f5be773eed80de02239/src/python/TaskWorker/Actions/Splitter.py#L44-L51

## Comment (belforte, 2024-11-07T16:48:27Z)

I am curious if we see same problem in a simple FileBased split. 
hmm.. same CI pipeline where automatic splitting failed has this task with used FileSplitting and submitted finely
https://cmsweb-testbed.cern.ch/crabserver/ui/task/241107_130406%3Acrabint1_crab_20241107_140406

TW log has no error and `splitter-summary.json` was created w/o problems
```text
crab3@crab-preprod-tw01:/data/srv/tmp/_241107_130406:crabint1_crab_20241107_1404065_e7f1jo$ cat splitting-summary.json 
{"algo": "FileBased", "total_jobs": 10, "total_lumis": 0, "total_events": 200100, "max_lumis": 0, "max_events": 24000, "avg_lumis": 0.0, "avg_events": 20010.0, "min_lumis": 0, "min_events": 1800, "total_files": 10, "max_files": 1, "avg_files": 1.0, "min_files": 1}
```

## Comment (belforte, 2024-11-07T17:09:45Z)

OK. Found.
When using FileBased splitting in the configuration, a different part of splitterSumary code is used
https://github.com/dmwm/CRABServer/blob/97f447747265684589ac1f5be773eed80de02239/src/python/TaskWorker/Actions/Splitter.py#L156-L169

so solution should be simply to add `automatic` to the `if` in line 156

## Comment (belforte, 2024-11-07T17:12:33Z)

that way it submits fine

## Comment (belforte, 2024-11-07T17:15:01Z)

all in all this is not surprising, since splittingSummary was previously used only during `submit --dryryun` and CRAB Client says
```console
belforte@lxplus831/TC3> crab submit --dryrun auto.py 
Will use CRAB configuration file auto.py
The 'dryrun' option is not compatible with the 'Automatic' splitting mode (default).
```

Simply I thought that maybe splitting-summary could be useful more in general and decided to always create it !
