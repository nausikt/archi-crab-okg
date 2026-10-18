# dmwm/CRABServer issue #7120: Activate TapeRecall for blocks partially on disk

State: closed
Opened: 2022-03-14T12:50:14Z
Closed: 2022-03-14T17:30:42Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7120

## Opening post (belforte, 2022-03-14T12:50:14Z)

On 14/03/2022 12:04, David Walter via CMS talk wrote:
> thanks for the quick reply, here is a task name:
> Task name: 220314_082639:dwalter_crab_SingleMuon_Run2017B

log says :
2022-03-14 09:27:38,550:WARNING:DataDiscovery:10 blocks will be skipped because are not completely replicated on DISK: ['/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#e565cbf0-596b-472a-bfdf-d0e41bd1a2b8', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#dba469b6-ca6d-42fb-ab4b-a22854a41be7', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#332d2cfd-20fa-408c-b7b6-761596db3a45', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#c7f799d9-4734-4472-9eef-feb8b66ceafa', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#7cb95b52-5acb-4d49-9593-e56ca6adec07', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#a6a8152c-f352-46f6-aa96-034d5256ffd3', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#e12b3820-b6af-4a44-9df9-1429b2771c80', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#a6aa0de8-f4b2-493d-8de2-920f402c6941', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#51db6f42-e47f-434b-8814-6f339d3dad11', '/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#870266bb-b0b1-4760-a579-7608e93e3366']


I have to suspect that CRAB code deals with blocks w/o disk location, but not with blocks partially on disk.
This will required a bit of time to be verified and then a patch and a new CRAB server release.

## Comment (belforte, 2022-03-14T13:09:01Z)

example of situation for one of those blocks:
```
belforte@lxplus753/~> rucio list-dataset-replicas cms:/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#dba469b6-ca6d-42fb-ab4b-a22854a41be7

DATASET: cms:/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD#dba469b6-ca6d-42fb-ab4b-a22854a41be7
+-----------------+---------+---------+
| RSE             |   FOUND |   TOTAL |
|-----------------+---------+---------|
| T1_IT_CNAF_Tape |      38 |      38 |
| T2_IT_Pisa      |      29 |      38 |
| T1_RU_JINR_Disk |      10 |      38 |
| T2_IT_Rome      |       0 |      38 |
+-----------------+---------+---------+
belforte@lxplus753/~> 

```

## Comment (belforte, 2022-03-14T13:15:32Z)

better look at this immedaitely before that dataset is fully replicated and I can't trace code anymore

## Comment (belforte, 2022-03-14T16:30:44Z)

Logic of queries to Rucio was OK. The bug comes from these lines
https://github.com/dmwm/CRABServer/blob/d6fe22eeab537c5eceaf583b3df8ef744405a9f5/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L395-L400
`blocksWithLocation` in there is created as a pointer to the `locationsMap` dictionary so when tape RSE's are dropped, they are dropped from both `locationsMap` and `blocksWithLocation` so that this `if statement` is ineffective
https://github.com/dmwm/CRABServer/blob/d6fe22eeab537c5eceaf583b3df8ef744405a9f5/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L409

## Comment (belforte, 2022-03-14T17:00:01Z)

@mapellidario has provided a more precise explanation, which explains why I did not find this problem in the initial testing (I thought it was because of blocks partially on disk rather than only on tape, but indeed the debugging which I just did showed that the incomplete disk replicas of those blocks were simply skipped and treated like blocks on tape).
https://github.com/dmwm/CRABServer/pull/7121#issuecomment-1067056285
