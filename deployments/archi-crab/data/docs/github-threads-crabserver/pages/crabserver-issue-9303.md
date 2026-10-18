# dmwm/CRABServer issue #9303: taskPublish stuck

State: closed
Opened: 2026-04-22T14:38:25Z
Closed: 2026-04-22T16:52:54Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9303

## Opening post (belforte, 2026-04-22T14:38:25Z)

task 
https://cmsweb.cern.ch/crabserver/ui/task/260418_214941%3Amilin_crab_run2025G_Jan26_397954_v8_v2

no progress logged in 1.5 hours !
I kill the process, and does the same at next iteration.
From master log
```
2026-04-22 14:58:15,036:INFO:master:acquired_files: WARN  2222 : 260418_214941:milin_crab_run2025G_Jan26_397954_v8_v2
2026-04-22 15:03:45,517:INFO:master:PID 935786 will work on task 260418_214941:milin_crab_run2025G_Jan26_397954_v8_v2
```

tail of taskPublish log
```
2026-04-22 15:03:56,803:INFO: Start new iteration on taskname:  260418_214941:milin_crab_run2025G_Jan26_397954_v8_v2
Get files to publish
2026-04-22 15:03:56,843:INFO: Will publish user files in /JetMET0/milin-CRAB3_Analysis_2025G_397954_v8-00000000000000000000000000000000/USER
2026-04-22 15:03:56,843:INFO: Will connect to CRAB service: prod
2026-04-22 15:03:56,843:INFO: Will connect to CRAB REST via: https://cmsweb.cern.ch/crabserver/prod
2026-04-22 15:03:56,872:INFO: inputDataset: /JetMET0/Run2025G-PromptReco-v1/AOD
2026-04-22 15:03:56,872:INFO: DBS Source API URL: https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader
2026-04-22 15:03:56,873:INFO: DBS Global API URL: https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader
2026-04-22 15:03:56,873:INFO: DBS Destination API URL: https://cmsweb-prod.cern.ch/dbs/prod/phys03/DBSWriter
2026-04-22 15:03:56,873:INFO: DBS Destination read API URL: https://cmsweb-prod.cern.ch/dbs/prod/phys03/DBSReader
2026-04-22 15:03:56,873:INFO: DBS Migration API URL: https://cmsweb-prod.cern.ch/dbs/prod/phys03/DBSMigrate
2026-04-22 15:03:56,873:INFO: inputDataset: /JetMET0/Run2025G-PromptReco-v1/AOD
2026-04-22 15:03:56,922:INFO: Dataset /JetMET0/milin-CRAB3_Analysis_2025G_397954_v8-00000000000000000000000000000000/USER already contains 93 files (93 valid, 0 invalid).
2026-04-22 15:03:56,952:INFO: Output dataset config: {'dataset': '/JetMET0/milin-CRAB3_Analysis_2025G_397954_v8-00000000000000000000000000000000/USER', 'processed_ds_name': 'milin-CRAB3_Analysis_2025G_397954_v8-00000000000000000000000000000000', 'data_tier_name': 'USER', 'dataset_access_type': 'VALID', 'physics_group_name': 'CRAB3', 'last_modification_date': 1776863036}
[crab3@crab-prod-tw01 processes]$ date
Wed Apr 22 04:33:13 PM CEST 2026
[crab3@crab-prod-tw01 processes]$ 
```

I do not know it it is related, but DBS Migration server had odd messages about that dataset, like
```
[2026-04-22 08:09:51.344719155 +0000 UTC m=+2904.031899684] migrate.go:1119: insert block dump record failed with DBSError Code:128 Description:Not defined Function:dbs.bulkblocks.checkBlockExist Message:Block /JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 already exists Error: nil
[2026-04-22 08:09:51.393973243 +0000 UTC m=+2904.081153787] migrate.go:1378: update migration request 6499526 to status 3
```

If the block already exists (at destination I presume), why did it set it to status 3 = error, rather than 4 = exists in DB ?
https://github.com/dmwm/dbs2go/blob/964e2e45e510af2852d1e5ff4e89018a991490d5/dbs/migrate.go#L48-L65

status 3 means it gets retried and eventyally set to 9

```
belforte@vocms0755/dbs-logs> grep "6499526 to"  dbs2go-phys03-migratio*.log-20260422
dbs2go-phys03-migration-644c89d6cb-rvbn9.log-20260422:[2026-04-22 08:10:23.257140175 +0000 UTC m=+5556.053575592] migrate.go:1378: update migration request 6499526 to status 1
dbs2go-phys03-migration-644c89d6cb-rvbn9.log-20260422:[2026-04-22 08:10:30.368651523 +0000 UTC m=+5563.165086940] migrate.go:1378: update migration request 6499526 to status 3
dbs2go-phys03-migration-644c89d6cb-rvbn9.log-20260422:[2026-04-22 08:11:23.654446037 +0000 UTC m=+5616.450881454] migrate.go:1378: update migration request 6499526 to status 1
dbs2go-phys03-migration-644c89d6cb-rvbn9.log-20260422:[2026-04-22 08:11:24.921014543 +0000 UTC m=+5617.717449960] migrate.go:1378: update migration request 6499526 to status 3
dbs2go-phys03-migration-694ff69b48-tmsd4.log-20260422:[2026-04-22 08:09:48.920184766 +0000 UTC m=+2901.607365308] migrate.go:1378: update migration request 6499526 to status 1
dbs2go-phys03-migration-694ff69b48-tmsd4.log-20260422:[2026-04-22 08:09:51.393973243 +0000 UTC m=+2904.081153787] migrate.go:1378: update migration request 6499526 to status 3
dbs2go-phys03-migration-694ff69b48-tmsd4.log-20260422:[2026-04-22 08:10:49.886143633 +0000 UTC m=+2962.573324164] migrate.go:1378: update migration request 6499526 to status 1
dbs2go-phys03-migration-694ff69b48-tmsd4.log-20260422:[2026-04-22 08:10:51.602646326 +0000 UTC m=+2964.289826859] migrate.go:1378: update migration request 6499526 to status 3
dbs2go-phys03-migration-694ff69b48-tmsd4.log-20260422:[2026-04-22 08:11:49.898859751 +0000 UTC m=+3022.586040282] migrate.go:1378: update migration request 6499526 to status 9
belforte@vocms0755/dbs-logs> 
```

FYI @todor-ivanov

## Comment (belforte, 2026-04-22T15:28:47Z)

I have saved the input json file in ` /data/srv/Publisher_files/MILIN-DBG.json` so that I can blacklist this task as well and then run taskPublish with debugger.
```text
2026-04-22 15:03:56,122:DEBUG:slave:FMDATA: retrieved data for 2 files
2026-04-22 15:03:56,122:DEBUG:slave:FMDATA: retrieved: 0 MB in 0 sec for 260418_214941:milin_crab_run2025G_Jan26_397954_v8_v2
2026-04-22 15:03:56,122:INFO:slave:Got filemetadata for 2222 LFNs
2026-04-22 15:03:56,668:DEBUG:slave:Unitarity check: active_:2222 toPublish:2222 toFail:0
2026-04-22 15:03:56,683:INFO:slave:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260418_214941:milin_crab_run2025G_Jan26_397954_v8_v2
```

## Comment (belforte, 2026-04-22T16:02:01Z)

hmm..  code gets stuck in
```
152  	    (localParentBlocks, globalParentBlocks) = findParentBlocks(
153  	        toPublish, DBSApis=DBSApis, logger=logger, verbose=verbose)
```

## Comment (belforte, 2026-04-22T16:10:21Z)

I start to suspect that problem is with the delays introduced in recent PR #9300 
with many operations being "loop on files" and 2K files... script duration gets ... long.
I reduced to `[0.001-0.01]` sec and it made it to the end of ` findParentBlocks)` . Now trying to do next steps after removing delays.

## Comment (belforte, 2026-04-22T16:16:21Z)

ouch:
```
Have to migrate 1 blocks from https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader to https://cmsweb-prod.cern.ch:8443/dbs/prod/phys03/DBSReader.
Submitting 1 block migration requests to DBS3 ...
DBS Server error: [{'error': {'reason': 'migration request /JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 is already exist in DB with id=6499987' .....
Migration request refused by server.
Migration refusal reason: migration request /JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 is already exist in DB with id=6499987
Existing migration id=6499987 is terminally failed (status=9)Delete it and try again at next iteration
Migration of /JetMET0/Run2025G-PromptReco-v1/AOD failed. Not publishing any files.
```

## Comment (belforte, 2026-04-22T16:31:53Z)

That is the same block as noted above which leads to this error in migration server
```
[2026-04-22 08:09:51.344719155 +0000 UTC m=+2904.031899684] migrate.go:1119: insert block dump record failed with DBSError Code:128 Description:Not defined Function:dbs.bulkblocks.checkBlockExist Message:Block /JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 already exists Error: nil
[2026-04-22 08:09:51.393973243 +0000 UTC m=+2904.081153787] migrate.go:1378: update migration request 6499526 to status 3
```

and, looking in DBS, reason is sort of "obvious" : **The block is present in `phys03` but with no files !**
```
belforte@lxplus802/TC3> dasgoclient --query 'block block=/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 instance=prod/phys03'   
/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258
belforte@lxplus802/TC3> dasgoclient --query 'file block=/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 instance=prod/phys03'
belforte@lxplus802/TC3> 
```
while in `global` there are 184 files
```
belforte@lxplus802/TC3> dasgoclient --query 'block block=/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 instance=prod/global'
/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258
belforte@lxplus802/TC3> dasgoclient --query 'file block=/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258 instance=prod/global'|wc -l
184
belforte@lxplus802/TC3> 
```

I had seen this "empty block in phys03", i.e. "block migrated w/o its files" already in the past, but it seems that I never reported it. It clearly indicates a problem in migration server. @todor-ivanov

We can not publish this until the situation in phys03 is fixed, which may be impossible. Surely it is not good that this keeps happening . But I am pessimistic about a solution

## Comment (belforte, 2026-04-22T16:51:51Z)

@nausikt can you kindly revert #9300 ?
It makes Publisher slow w/o any reason/benefit. I think that what you saw was simply that DBS Migration pods were restarting contiuously due to the OOMKiller, which possibly explains the odd "empty json" message.
All in all code worked for years w/o any delay, thanks of course to the strong concurrency capability of the server rewrite in glolang,
It was a difficult and confused situation, I not blaming anybody, it was fine to apply whatever mitigation appeared useful, but now we do not need it and I'd rather like Publisher go back to completing its cycle in a decent time.

## Comment (belforte, 2026-04-22T16:52:54Z)

I do not see anything else to learn from this particular incident. So am closing. If I missed something we can of course re-open
