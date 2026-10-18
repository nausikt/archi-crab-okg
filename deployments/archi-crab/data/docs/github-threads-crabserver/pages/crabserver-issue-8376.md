# dmwm/CRABServer issue #8376: not all files transferred by Rucio are published

State: open
Opened: 2024-05-03T09:25:29Z
Labels: Type: Bug, Priority: Medium, RUCIO, Publisher
URL: https://github.com/dmwm/CRABServer/issues/8376

## Opening post (belforte, 2024-05-03T09:25:29Z)

moving here from #8244

## Comment (belforte, 2024-05-03T09:30:56Z)

I move  here relevant comments from #8244. Keep things in a single place.

**Stefano**
 I get unexptected problems with Rucio ASO. It looks like files are added to a block after it was closed,
so Publisher tries to put it twice in DBS and fails.
example: https://cmsweb-testbed.cern.ch/crabserver/ui/task/240502_145418%3Acmsbot_crab_rucio_transfers_group_20240502_165417
I do not know where the problem exactly comes from.
I looked at `transfer_rucio.log` in the scheduler, but it is too verbose to follow and I do not find a line which says when block was marked as completed so that adding new files must stop.

Code in this area has not changes since a long time, so I do not know why almost one out two tasks fails now.
But I will need @novicecpp help to debug.

**Wa**
@belforte Could you please provide error logs (with timestamp) from Publisher_rucio?

**Stefano**
on crab-preprod-tw01
`/data/container/Publisher_rucio/logs/tasks/cmsbot/240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417.log`

relevant lines for block `3f17ded7-ceac-44fa-a84a-45218d81df55`
```
2024-05-02 17:29:29,178:INFO: Found 18 files not already present in DBS which will be published.
2024-05-02 17:29:29,367:INFO: PUBSTAT: Nfiles=  18, lumis=      0, blockSize=17KB  , time=1714663769, status=OK, task=240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417
2024-05-02 17:29:29,367:INFO: Publish OK   for Block: /GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#3f17ded7-ceac-44fa-a84a-45218d81df55
```

```
2024-05-02 17:59:28,779:INFO: Found 2 files not already present in DBS which will be published.
2024-05-02 17:59:28,859:ERROR: Error when publishing /GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#3f17ded7-ceac-44fa-a84a-45218d81df55
2024-05-02 17:59:28,860:ERROR: FAILING BLOCK DUE TO HTTP Error 400: DBSError Code:128 Description:Not defined Function:dbs.bulkblocks.checkBlockExist Message:Block /GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#3f17ded7-ceac-44fa-a84a-45218d81df55 already exists Error: nil SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1714665568.8595989.txt
2024-05-02 17:59:28,861:INFO: PUBSTAT: Nfiles=   2, lumis=      0, blockSize=2KB   , time=1714665568, status=FAIL, task=240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417
2024-05-02 17:59:28,861:ERROR: Publish FAIL for Block: /GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#3f17ded7-ceac-44fa-a84a-45218d81df55
2024-05-02 17:59:28,861:INFO: Marking 2 file(s) as failed
2024-05-02 17:59:28,994:ERROR: Failed to insert block in DBS. Block Dump saved
```

same failure in that log/task for block `679ff9f5-f5fe-434e-9614-f28c955b40ba`

Maybe we have some race codition where publisher runs wile ASO is updating info. But current failure rate is too much for that !
https://github.com/dmwm/CRABServer/issues/8370
https://github.com/dmwm/CRABServer/issues/8373

hmmm... eventually that task is reported as 100% published. in crab status,
```text
belforte@lxplus803/bot> crab status |egrep 'Task name'\|'Publication status'
Task name:			240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417
Publication status of 1 dataset(s):	done         		100.0% (40/40)
belforte@lxplus803/bot> 
```
yet DBS only has 36 files
https://cmsweb.cern.ch/das/request?input=%2FGenericTTbar%2Frucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER&instance=prod%2Fphys03

which makes me fear that this could have gone un-noticed


**Wa**
FYI, if you grep `fileDocs to update block completion` from [transfer_rucio.log](https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417/SPOOL_DIR/task_process/transfer_rucio.log), you will see only 2 lines with non-empty lists. This [line](https://github.com/belforte/CRABServer/blob/eb8d1e5378f70f5f29ca5cd555f483fe3d58beed/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L56) will print list of fileDocs before update block completion to REST via `/filetransfers?subresource=updateRucioInfo`.

And the list lengths are also consistent with the number of files per rucio dataset:
- first update: [679ff9f5-f5fe-434e-9614-f28c955b40ba](https://cms-rucio-webui.cern.ch/did?scope=group.crab_test&name=/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER%23679ff9f5-f5fe-434e-9614-f28c955b40ba):19, [3f17ded7-ceac-44fa-a84a-45218d81df55](https://cms-rucio-webui.cern.ch/did?scope=group.crab_test&name=/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER%233f17ded7-ceac-44fa-a84a-45218d81df55):20
- second update: [2b1a4fcd-9157-4576-a19f-073ca59a7d8d](https://cms-rucio-webui.cern.ch/did?scope=group.crab_test&name=/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER%232b1a4fcd-9157-4576-a19f-073ca59a7d8d):1

That means there is no file added to the rucio dataset after it closed.

Timestamp also indicate that Publisher was running after rucio dataset was closed and updated to REST (Rucio ASO last REST update: `2024-05-02 17:11:07,210` vs Publisher_schedd start: `2024-05-02 17:29:27,308`)

I might be wrong. I will dig it more tomorrow.

## Comment (belforte, 2024-05-03T09:41:22Z)

I looked at block `/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#679ff9f5-f5fe-434e-9614-f28c955b40ba`

The files missing in [DBS](https://cmsweb.cern.ch/das/request?instance=prod/phys03&input=file+block%3D%2FGenericTTbar%2Frucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER%23679ff9f5-f5fe-434e-9614-f28c955b40ba)  are
 *  `output_21`
 *  `output_27`

when comparing  e.g. `rucio list-files group.crab_test:/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#679ff9f5-f5fe-434e-9614-f28c955b40ba --csv |cut -d'/' -f11|cut -d, -f1` with `dasgoclient --query 'file block=/GenericTTbar/rucio-ruciotransfers-1714661657-94ba0e06145abd65ccb1d21786dc7e1d/USER#679ff9f5-f5fe-434e-9614-f28c955b40ba instance=prod/phys03'|cut -d'/' -f11|sort`

for the other block  `3f17ded7-ceac-44fa-a84a-45218d81df55`  the missing files are
* `output_10`
* `output_6`

Looking in trasnfersDB now those files are all OK. 
 
I looked for lines in `transfers_rucio.log` where e.g. output_10 and output_11 are not mentioned together, but there's nothing suspicious there either. In agreement with "nothing was added to blocks after they were closed" as Wa said.

Do we have to fear that ASO was updating to_publish flag in transfersdb at the same time as Publisher was running ?

## Comment (belforte, 2024-05-03T10:58:13Z)

I submited another ST test and waiting until all transfers were completed before starting Publisher. Everything fine. So we clearly have a race condition to pinpoint.  Maybe back to "have a singe DB transaction which marks the block as complete once all files have been marked as to-publish".   I am not sure that currently we are safe in that respect.

## Comment (novicecpp, 2024-05-03T19:54:32Z)

Just random discovery.

PostJob was updating `filetransfersdb.tm_publish` while Publisher was running. 
- Publisher started at: `2024-05-02 17:29:27,308`
- [postjob.11.0.txt](https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417/postjob.11.0.txt) finished at `17:29:09`.
- [postjob.10.0.txt](https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240502_145418:cmsbot_crab_rucio_transfers_group_20240502_165417/postjob.10.0.txt), the missing file in the same block, finished at `17:29:37`.

My guess is that, at the time Publisher was running, Publisher only saw 8/10 files that had `tm_publish=1`, while `tm_block_complete` was already updated for all files in the block to `OK` by Rucio ASO. So, the Publisher noticed the `tm_block_complete` was `OK` and decided to publish all those 8 files.

## Comment (belforte, 2024-05-05T13:58:56Z)

ho my !!
We surely have too many actors here ! We need to review.

## Comment (belforte, 2024-05-06T07:54:55Z)

places where `filetransfer` is referenced (other then REST interface or SQL), and type oh http query
* PostJob  - POST
* FTS_Transfers - POST (irrelevant here)
* ASO/Rucio/Actions
   * RegisterReplicas  - only via updateToREST - POST
   * MonitorLockStatus- only via updateToREST - POST
* Publisher - POST + GET
   * PublisherMaster-  POST : select files with transfer DONE and publication NEW and set publication to ACQUIRED
   * PublisherMaster - GET : retrieve those files
   * PublisherMaster - POST : mark failed files
   * PublisherUtils - POST : markGood, markFailed

N.B. updateToREST is in ASO/Rucio/utils and only does POST

## Comment (belforte, 2024-05-06T08:12:21Z)

I have been believing that `publish` status for each file was under control of ASO/Rucio, since that's the one in control of filling blocks and marking them as complete, but of course FTS_Transfers did not touch publication flags in transfersdb since it only cared about transfers. Sounds like we missed this big difference. Or maybe said "we should update PostJob" and never did.

I will reconstruct what PJ do. @novicecpp can you summarize for me in a couple lines what ASO/Rucio does ? Does it only mark the block as complete and fill the block name in the file entry in filetrasfersdb ?

## Comment (belforte, 2024-05-06T08:21:24Z)

PostJOb does this
https://github.com/dmwm/CRABServer/blob/033af370bf8a3c8affdb7acf13bfc7dc38d74174/src/python/TaskWorker/Actions/PostJob.py#L2200-L2214

Then there are calls via updateOrInsertDoc that I need to review

in this context `updateOrInsertDoc` is used in the PostJob-ASO part to set `tm_publish` to   0/1 (False/True) and if True to set `tm_publication_state` to NEW (to NOT REQUIRED if False).
There is only one call to updateOrInsertDoc in PostJob, the doc is inserted the first time PostJob runs, and it is updated when the transfer is completed.
updateOrInsertDoc is tricky to properly asses since the POST api to filtransfersdb requires a lot of params to be indicated every time even if they are not changing, so I am not 100% sure that there is not something else.

Anyhow this clearly indicates that 
1. ASO/Rucio runs every 5 min
2. ASO/Rucio marks files as transferred, and adds block info
3. when block is full, ASO/Rucio marks all file in the block with block_complete=True
4. PostJob runs every 30 min
5. Once a file is marked as transferred, PostJon will mark it with Publish=True
6. Publisher runs every 30 min
7. Publisher picks all files with Publiish=True, sort by block, and if one file in one block has complete=True, publishes it
8. Once a block is published in DBS, it can't be changed any more

And indeed there's ample room for the race which @novicecpp found: a block can be marked as closed before PostJob has marked all files with Publish=True.

Wa, can you confirm the ASO/Rucio part ? I did not check the code

## Comment (belforte, 2024-05-06T13:38:02Z)

If the above story is the correct one, I think that ASO/Rucio should simply set `publish=1` for all files in the block before setting `tm_block_complete`= True. We can even leave PostJob as it, it will not do any harm to set `tm+publish` to true again.

One of the problem with this filetransersdb handling is that it still suffers of the old ASO on CouchDB. All those "doc" names, those API's which require a complete "document" , the 1K lines in PostJob/ASOServerJob class.

## Comment (novicecpp, 2024-05-07T07:17:53Z)

> And indeed there's ample room for the race which @novicecpp found: a block can be marked as closed before PostJob has marked all files with Publish=True.

Yes. That is what I am understanding.

> If the above story is the correct one, I think that ASO/Rucio should simply set publish=1 for all files in the block before setting tm_block_complete= True. We can even leave PostJob as it, it will not do any harm to set tm+publish to true again.

I am not sure if set "tm_publish" in ASO is good. I mean, I like the simplicity of this idea. However, I also like the intention of current code that 1) Act as barrier between job and the Publisher, guarantee that nothing will change after `tm_publication` flag is set, 2) Like you said, ASO only cared about transfers.

If not urgent, let me take some time to think about it.

## Comment (belforte, 2024-05-07T09:05:41Z)

we also need to make sure that FileMetaData is uploaded before the file is declared ready to be published. I will look

## Comment (belforte, 2024-05-22T10:53:52Z)

I did check FIleMetaData, those are uploaded as soon as job completes, in PostJob's first run before it passes the control to ASO. We are OK there.

## Comment (belforte, 2024-05-22T10:54:08Z)

@novicecpp did you have any chance to think about this ?

## Comment (novicecpp, 2024-05-23T06:50:13Z)

Would you mind to let Publisher talk to rucio?

Basically, count the DIDs in closed dataset from rucio side and compare with number of entry you get from database where `tm_publish=1`.

## Comment (belforte, 2024-05-23T08:31:18Z)

interesting, let me thing about it for a bit

## Comment (belforte, 2024-05-27T10:40:13Z)

I thought about it, and I do not like it. It makes the process even more spread out with three servers involved. It opens up to troubles whenever one of them is changed in the future.
The publisher should get a list of completed blocks, including the content.
And in current design the only service who knows about the whole block is ASO.

In a way, before introducing Rucio, everything was file-based in the scheduler and it made sense to keep ASO to "transer only" and higher level decisions in PostJob. But when we introduce Rucio-baded-ASO, we need a container/dataset-based flow. And we do that in ASO. 

But we must worry about files which need to be transferred but not published. I am not sure ASO has the info..
But if it does, maybe PublisherRucio could work out of Rucio info, eventually getting rid of filetransfersdb table :-)
this would require a lot of changes though. IN a away setting  to-publish flag for files in there is a step in that direction.

## Comment (novicecpp, 2024-05-27T12:56:23Z)

Hmm...per block...
Maybe Rucio ASO simply update status to rest once all files in the block are completed, instead of individual file (1 block/request to avoid race condition).

Let's me try it tomorrow.

## Comment (belforte, 2024-05-27T13:12:18Z)

isn't that what we are doing now ? The problem is that when it does it PostJob may not have set publish flag for all files. Therefore Publiher has to wait for all PostJobs to run, but there is no simply protocol for that, back to compare file list from transfersdb and Rucio.

## Comment (novicecpp, 2024-05-27T13:43:22Z)

Ah, I see. Thanks for pointing out. 
Back to thinking again.

## Comment (belforte, 2024-05-27T16:04:51Z)

it will help me to recap how things work in more detail:
* PublisherRucio
   * uses one SQL query in filetransfersdb to find all files with `tm_publish=1` and `tm_publication_status=NEW` and set `tm_publication_status=ACQUIRED`. Then it select all the `ACQUIRED` and group by task.
   * forks one slave for each task
   * the slave goes through all files, looks for `tm_block_complete = OK` and creates a list of corresponding block names
   * then with same list of iles, fills a list of files for each completed block, retrieves FMD for each file and publishes the block

* PostJob
  * if jobs is successful[1],  hand it to ASO [2]. Then polls ASO status every 30min [3]
  * when transfer is completed [4]
  * upload input and output FileMetaData [5]
  * set in `transfersdb` : `publish=1` and `publication_status=NEW` [6]
  * exit and do not ask Dagman to rerun the PJ [7]
 
So **I was wrong** in  https://github.com/dmwm/CRABServer/issues/8376#issuecomment-2124500392 . FMD are only uploaded when PJ detects "transfer complete", and files can't be published until FMD are available, so we can  not trigger Publisher before PostJob has completed.

[1] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2021

[2] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2150

[3] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2151-L2153

[4] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2175

[5] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2177
 https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2188

[6] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2201-L2220

[7] https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/PostJob.py#L2225

## Comment (belforte, 2024-05-27T21:16:33Z)

translation in English of the above comment: setting publish flag in ASO (RucioTransfer) will not work. I have no quick solution in mind.
And we may have to go for getting file list from Rucio in the Publisher, compare with the one from trasnfersdb and wait for agreement.

Or modify the PostJob and do the FMD upload earlier. I think that the rational for current design was "in case ASO fails, do not waste REST resources for FMD" which is liketly to be a few % effect in the total number of calls, anyhow. But changing the PostJob is always a risky operation.

A more drastic alternative: ASO somehow detects if PJ has run and only sets block_is_complete flag when PJ's for all files in the block have run. Requires somehow to keep monitoring blocks for which it has nothing more to do in Rucio, separating `block closed` from `block complete`.  Effectively means that ASO polls transfersdb. Pretty ugly.

## Comment (novicecpp, 2024-05-28T07:37:11Z)

What about count the block_is_complete row in Publisher, if its equal to acquire files?
This is the first idea that come from my mind but not 100% sure if it safe. But look like it is because we update all rows in filetransferdb in single batch. Even there is the fail job the count query should catch `block_is_complete=yes` only.

## Comment (belforte, 2024-05-28T08:37:54Z)

that'd be a new SQL and would require querying "all of" transfersdb, well maybe  we can out a"since". If we want to go that way we may also review the fact that we have two columns meaning similar thing: tm_publish and tm_publish_state.

May not be really better than asking Rucio. Or we can add in transfersdb the info on how many files in each block, either a new column or reuse block_completed changing from YES/NO to 0/N.

But I all in all unhappy with the trasnsfer-then-upload-FMD. What happens if the latter fails ? E.g. REST down for a day. Do we keep waiting forever ? Current PJ will give up and resubmit.. If we delay handing a job to ASO until everything is ready, it may  be cleaner.

The more I tinnk about it, the more I am lead to desire a new block-based component. The fact that PostJob is job based is always an obstacle. Well...maybe that can be part of the Publisher !

## Comment (belforte, 2024-05-28T08:42:12Z)

sorry for using this to thinking out loud, in the end I think I re-discovered your suggestion to check all files in a completed block in the Publisher.
Maybe we should add a block table in Oracle.

## Comment (belforte, 2024-05-28T13:38:23Z)

Let me try to spec that new table. 

A new row is created by RucioTransfer when it created a new block id
columns:
-  taskname
 - blockname
 - open/closed (from Rucio POV)
 - to be published (Y/N) (or do we only put blocks which needs to be published in this table ?)
 - number of files in Rucio dataset (uploaded when block gets closed in Rucio)
 - number of files ready to be published according to PJ (incremented  by each PJ, need an atomic SQL)
 - completed (Y/N) to indicate that those two numbers are equal. But I am not sure if it is possible/efficient  to do this

I presume we need to define primary key. I am not sure if taskname or blockname. Maybe have an index on both ?

## Comment (belforte, 2024-05-29T20:09:00Z)

well... thinking more about it, that may be nice in an other life.
But we want a solution before. I guess I better go for the initial suggestion of checking Rucio dataset content in Publsher and wait until it agrees with list of files from transfersdb.

## Comment (novicecpp, 2024-06-06T10:01:32Z)

Conclusion from our meeting: 
- Short term: Publisher queries Rucio and ensure consistency - moved to #8491 
- Longer term: add a block table in Oracle and have RUcioTransfet + PostJob cooperate to put proper information in there so Publisher only queries that and fletransfersdb tables

## Comment (belforte, 2024-06-12T15:01:24Z)

keep it open while thinking if "Longer term" option above is really a sensible option.
In the end the information is in Rucio, and easy to get. If the only thing we gain is to query one DB instead of two, it may not be worth.

## Comment (belforte, 2024-06-12T15:01:37Z)

reduce priority
