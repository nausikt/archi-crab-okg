# dmwm/CRABServer issue #9105: Automatic Reporting of bad input file broken since November

State: closed
Opened: 2025-06-03T15:52:39Z
Closed: 2025-06-05T13:18:10Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9105

## Opening post (belforte, 2025-06-03T15:52:39Z)

A bug was introduced (by me) during "improvement" in #8801

Line 447 is wrong in here
https://github.com/dmwm/CRABServer/blob/760bad67b5fcdef2ce9641399fbe700c6e980ff7/src/python/TaskWorker/Actions/RetryJob.py#L446-L453

clearly it should have been
```python
 if "Fatal Root Error:" in line:
```

Clearly I did not test well enough.

I found this by running PostJOb with pdb on https://cms-talk.web.cern.ch/t/3-files-are-damaged-in-this-dataset-doublemuon-run2016g-ul2016-miniaodv2-v1-miniaod/125539/4

## Comment (belforte, 2025-06-03T19:35:28Z)

there is at least another problem
```
Tue, 03 Jun 2025 21:33:39 CEST(+0200):INFO:RetryJob Corrupted input file found
Tue, 03 Jun 2025 21:33:39 CEST(+0200):DEBUG:RetryJob == CMSSW:       [a] Fatal Root Error: @SUB=TStorageFactoryFile::Init
Tue, 03 Jun 2025 21:33:39 CEST(+0200):INFO:RetryJob RSE: T2_US_MIT - ec: 8028 - file: /store/data/Run2016G/DoubleMuon/MINIAOD/UL2016_MiniAODv2-v1/70000/164CEA6B-A5DF-6544-96A5-B034A21E832F.root
Tue, 03 Jun 2025 21:33:39 CEST(+0200):ERROR:RetryJob check_corrupted_file raised an exception:
'>' not supported between instances of 'str' and 'int'
Ignore and go on
```

## Comment (belforte, 2025-06-03T19:50:37Z)

that comes from here
https://github.com/dmwm/CRABServer/blob/760bad67b5fcdef2ce9641399fbe700c6e980ff7/src/python/TaskWorker/Actions/RetryJob.py#L500-L503

I can't see a reason why I decided to put `count` as a string rather than as an integer in the JSON file. Which should have helped avoid such mistake.

## Comment (belforte, 2025-06-03T19:55:15Z)

once this is fixed, need to follow up in https://its.cern.ch/jira/browse/CMSTRANSF-1024?focusedId=6811491&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6811491

## Comment (belforte, 2025-06-03T20:42:51Z)

other problems coming up. Work In Progress.

## Comment (belforte, 2025-06-03T20:57:47Z)

there was inconsistency in key name for the `corruptionMessage` dictionary
https://github.com/dmwm/CRABServer/blob/760bad67b5fcdef2ce9641399fbe700c6e980ff7/src/python/TaskWorker/Actions/RetryJob.py#L475-L476
vs.
https://github.com/dmwm/CRABServer/blob/760bad67b5fcdef2ce9641399fbe700c6e980ff7/src/python/TaskWorker/Actions/RetryJob.py#L512-L513

and a bad indentation, `reportBadInputFile` must be called once per job, not once per line
