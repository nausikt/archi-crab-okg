# dmwm/CRABServer issue #7769: Publication is broken when using Rucio container as  input dataset

State: closed
Opened: 2023-07-17T21:05:59Z
Closed: 2024-01-25T12:28:55Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7769

## Opening post (belforte, 2023-07-17T21:05:59Z)

with e.g.
```
config.Data.inputDataset = cms:/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM
```
TaskWorker part works and jobs run but `taskPublish.py` fails because it tries to insert that in DBS as input dataset
```
2023-07-17 22:50:29,099:INFO:PublisherMaster,696:TaskPublishScript done : b'DBS Server error: [{\'error\': {\'reason\': "DBSError Code:114 Description:DBS validation error when wrong pattern is provided Function:dbs.validator.Check Message:unable to match \'dataset\' value \'cms:/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM\' Error: invalid parameter(s)"
```

I guess we can start by disabling publication in this case. Because in general we have no way to ensure that this rucio container maps to a dataset properly described in DBS `prod/global`.


Stick to
 * Publication in DBS requires input data in DBS.

## Comment (belforte, 2024-01-19T20:35:51Z)

.hmm... all in all.. if data processing produces valid FJRs and we have metadata for DBS.. why not simply stripping the initial scope in this case ?
@dciangot what do you think ?

## Comment (dciangot, 2024-01-19T20:40:19Z)

I think it will not hurt to disable it. If your input is from Rucio and not from DBS, It might be reasonable to say "I'm sorry, I can't do it".

Either way is fine, stripping out scope can be a solution, but it really depends on having strong use cases for that I think.

## Comment (belforte, 2024-01-19T20:43:01Z)

supporting is at least clear. DIsabling I am not sure if to do in client or in server, where exactly, how to communicate... too many decisions !
Let me try the easy way (stripping) and see if it works

## Comment (belforte, 2024-01-24T19:04:00Z)

fix tested OK on publisher_schedd.  Need to verity on Publisher_rucio

## Comment (belforte, 2024-01-25T08:47:24Z)

OK with Publisher_Rucio as well
