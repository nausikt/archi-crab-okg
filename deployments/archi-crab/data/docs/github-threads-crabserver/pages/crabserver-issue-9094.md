# dmwm/CRABServer issue #9094: Publisher_Rucio disagrees with Rucio on block content

State: closed
Opened: 2025-05-23T16:57:58Z
Closed: 2025-06-16T14:52:27Z
Labels: Type: Bug, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/9094

## Opening post (belforte, 2025-05-23T16:57:58Z)

I just hit the opposite problem to #8491 

When task is killed, PostJobs do not run anymore, Rucio closed the datasets/blocks with all files transferred at that point, but the publish flag in transersdb will never be updated.

So we end up with more files in Rucio then in filetransfersdb and Publisher waits forever for things to become consistent.

My current thinking is that this is all crazy. Since now Rucio is in full control of the block content, there is no point for the publish flag.

This was sort of due to lazyness. We should have a new API to retrieve files which have `block_complete='OK'` and leave entirely to ASO/Rucio the control, "complementing" https://github.com/dmwm/CRABServer/blob/5175d23489ad7b07e7fd5324e33c2220b6d23fab/src/python/CRABInterface/RESTFileTransfers.py#L101

Or maybe at the time that ASO/Rucio updates file record in filetransfersdb, also set the publish value.
I.e. change
https://github.com/dmwm/CRABServer/blob/5175d23489ad7b07e7fd5324e33c2220b6d23fab/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L255
and
https://github.com/dmwm/CRABServer/blob/5175d23489ad7b07e7fd5324e33c2220b6d23fab/src/python/CRABInterface/RESTFileTransfers.py#L185

## Comment (belforte, 2025-05-23T16:58:50Z)

@aspiringmind-code let's talk about this, I need advice before I do such changed

## Comment (belforte, 2025-05-26T13:07:24Z)

I am starting to think that when using Rucio there is no need to keep running the PostJob. I believe that it is only needed to resubmit in case of failure. But I still need to be sure of when exactly metadata are uploaded.

## Comment (belforte, 2025-05-26T13:16:50Z)

PostJob logic is (see https://github.com/dmwm/CRABServer/blob/5175d23489ad7b07e7fd5324e33c2220b6d23fab/src/python/TaskWorker/Actions/PostJob.py#L2129 and following):
1. call PerformTransfers
2. if it returns 4: defer (returns 4 to Dagman)
3. if it return error or exception (returns 2 (retry me) or 3 (call it failed) to Dagman
4. else (returns 0) upload input and output metadata, publication flag  and exit (return 0 to Dagman)

![Image](https://github.com/user-attachments/assets/5ef9ae6c-d7ea-4153-ab14-89a321ce6a5a)

## Comment (belforte, 2025-05-26T13:23:32Z)

When using Rucio it could upload the metadata submit to ASO and return 0 to Dagman. No matter what happens later, no resubmission is possible.

But we need to modify `cache_status.py` so that it takes into account the transfer status, not only the status from Dagman. Or jobs will be labelled as "completed" even if still in transfer.

Of course we may argue that once things are in Rucio hands, CRAB job is over and indeed jobs is completed successfully.

That will surely save code and effort. Maybe only put this in the documentation ?

We could also change CRAB Client to pick transfer status from Rucio, rather than from HTC AP. So can still offer synoptic view including publication. `crab status` surely has become complicated with time and may use a good cleanup. Possibly at the same time as we remove the code which parses "Dag nodes".

Of keep Rucio handling in `task_process/RUCIO_Transfers.py` and in there write  a JSON summary which `cache_status.py` can parse w/o adding Rucio calls in there.

## Comment (belforte, 2025-05-26T13:53:24Z)

side note about `publication flag` update in PostJob
https://github.com/dmwm/CRABServer/blob/5175d23489ad7b07e7fd5324e33c2220b6d23fab/src/python/TaskWorker/Actions/PostJob.py#L2186
as soon as we decide to change PostJob when using Rucio, this could be done by RUCIO_Transfer at the same time it sets  block_complete='OK'. This will also simplify Publisher since it will only retrieve from the DB files in completed blocks.

## Comment (belforte, 2025-05-28T13:39:12Z)

I need to look at metadata uploading. It would be much simpler if we could avoid "if Rucio" and do all the uploads in any case as soon as job is successful and control handed to ASO.

## Comment (belforte, 2025-06-03T09:44:54Z)

metadata are inserted in FileMetaData table using LFN as key. Therefore
 * input FMD can be uploaded as soon as job completes OK.
 * output FMD key does not change if jobs is retried, so maybe we can upload that as well.
 * A drawback I see is to upload useless records if the job ultimately fails during ASO.  But we periodically clean up FMD table.
 * **BUT** FMD contains file checksum. If job is retried, checksum changes !  Also outtmplocation will change. 
 * current API allows to change outtmplfn and outlfn in the FMD, nut not checksums. But it looks easy to add in DataFileMetadata.py

## Comment (belforte, 2025-06-04T13:44:11Z)

I am leaning toward leaving current code unchanged for ASO-FTS and do things differently only for ASO-Rucio where we are sure that there are no resubmissions of successful jobs.

## Comment (belforte, 2025-06-09T15:08:47Z)

Changing of the publish flag in filetransfersdb has to be done in Rucio, since in the PostJob it depends on ASO to succeed and the `delayed_publicationflag_update` to be turned from False to True. I suspect that that extra logic is an overkill, would only make sense in case of mulitple outputs where only some failed, but if the job is retried, the wrong checksum will be in DBS, Of course chance of this are extremely small, and those checksums are very unlikely to be ever used. Anyhow as usual I am leaving the current part "as is".

## Comment (belforte, 2025-06-09T16:05:50Z)

hmm... maybe  I got it wrong, `delayed_publicationflag_update` is set to True during `inject_to_aso()`. Need to test, may I can keep it in PostJob after uploading of output file MD. BTW also uploading of OutputMD only makes sense if publication is not disabled, looks like this was overlooked in PostJob.

## Comment (belforte, 2025-06-10T09:10:38Z)

The code which I put in does the following:

* only PostJob is changed
* very small changes in any case (better comments and log messages, capturing publish flag updating in a method)
* always upload input metadata before handing control to ASO
* introduce `self.useAsoRucio` and when true upload output metadata and set publish flag to True right after triggering ASO work (in first PJ iteration)
* keep the PJ running also for ASO-Rucio so that job status is reported the same way as it is now.
* no changes to Publisher

I tested in simple tasks. More to come

## Comment (belforte, 2025-06-11T13:06:30Z)

The above sort of works.
But when I killed a test task I ended up with a file inserted in a closed Rucio dataset, with an OK lock, but which was not updated in transfersdb, block name and blockStatus=OK are missing, even if publish flag was set to True by PostJob. So Pubisher finds again that number of acquired files does not match what's in Rucio dataset and waits forever.

In a way it looks like a bug in ASO/Rucio. But it is suspicious that it only appeared after I did changes in https://github.com/dmwm/CRABServer/pull/9089

Maybe I introduced a situation not foreseen by original developer (Wa) ?

## Comment (belforte, 2025-06-11T14:31:59Z)

notes to myself

 in #9089 I am closing current Rucio dataset when task is killed, but that's a dataset in the TRANSFER container
`user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f_TRANSFER.07e63004/USER`


Starting point is from looking at Publisher with pdb circa line https://github.com/dmwm/CRABServer/blob/a2e8f430abddc59915bc97bae60a0dd11b5555fa/src/python/Publisher/PublisherMasterRucio.py#L296

```
(Pdb) blockName
'/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f/USER#180f2cd1-2a14-4a22-9f54-04fe29c9d4cf'
(Pdb) countOfAcquiredFilesInBlock
22
(Pdb) countOfFilesInRucioDataset
24
```
so there are 2 files in that Rucio Dataset which were not acquired by Publisher.

looking at the dataset content
```console

belforte@lxplus996/~> rucio did content list --did user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f/USER#180f2cd1-2a14-4a22-9f54-04fe29c9d4cf --short
user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133512/0000/kk_100.root
user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133512/0000/kk_139.root
user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133536/0000/kk_149.root
user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133536/0000/kk_153.root
user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133536/0000/kk_169.root
...
```

**The first two file are from a different task ! `250610_133512` vs. `250610_133536`**
**This should not happen**

In the Publisher I separate files by task and hence I find only 22 file !!

Looking at parentage in Rucio for a couple of files in that list, they come from different transfer datasets:
```console
belforte@lxplus996/~> rucio did show --parent -d user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133512/0000/kk_100.root
+-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
| SCOPE:NAME                                                                                                                                            | [DID TYPE]   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------|
| user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f/USER#180f2cd1-2a14-4a22-9f54-04fe29c9d4cf                   | DATASET      |
| user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f_TRANSFER.668c22cc/USER#07db1211-1867-4e7e-8340-3d6fc411c807 | DATASET      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
belforte@lxplus996/~> rucio did show --parent -d user.belforte:/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-Test-250609/250610_133536/0000/kk_149.root
+-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
| SCOPE:NAME                                                                                                                                            | [DID TYPE]   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------|
| user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f/USER#180f2cd1-2a14-4a22-9f54-04fe29c9d4cf                   | DATASET      |
| user.belforte:/GenericTTbar/belforte-Stefano-Test-250609-5e829523c2eebdfafa0bc0ee3560a36f_TRANSFER.07e63004/USER#228e4963-884a-4371-af1b-7dd6fae8038c | DATASET      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
belforte@lxplus996/~> 
```

## Comment (belforte, 2025-06-11T15:26:56Z)

I fear that two tasks running at same time got confused and step on each other feet.
Maybe ASO/Rucio adds replicas to Publish container sort of "progressively" while having an open dataset there, instead of "moving closed datasets" ?

## Comment (belforte, 2025-06-11T15:27:54Z)

I will test running a killing a single task to check that things are otherwise OK.

## Comment (belforte, 2025-06-11T15:47:58Z)

files from different tasks in same Rucio-dataset/DBS-blocks will be very confusing anyhow and may even lead to other problems since those files go in different disk directories. So if problem is confirmed I do not think that changing Publisher is an option

## Comment (belforte, 2025-06-12T10:06:47Z)

INdeed, IIUC the ASO/Rucio code, transferred files are added to Publish container "independently of the dataset they are in the transfer container", using code in
https://github.com/dmwm/CRABServer/blob/a2e8f430abddc59915bc97bae60a0dd11b5555fa/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L201
which relies on
https://github.com/dmwm/CRABServer/blob/a2e8f430abddc59915bc97bae60a0dd11b5555fa/src/python/ASO/Rucio/Actions/BuildDBSDataset.py#L96
to decide if use a currently open dataset or create a new one, using current status and content in Rucio as bookkeeping.
So once  a task has opened a dataset, another can also use it, until it is time to close.

I am wondering how I did not spot this last year !!

## Comment (belforte, 2025-06-12T13:12:00Z)

Never the less, I do not like my solution because for various reasons (including crashes) there can be files with publish flag set to True but without the DBS block name and status=OK in filetransfersdb. They will be acquired but not published by Publisher, so we will "leak" files in Acquired.

Must keep metadata uploading done before transfer is over, but setting of publish flag has to be done inside ASO/Rucio at the same time as setting publication flag.

## Comment (belforte, 2025-06-12T17:13:50Z)

so above [summary](https://github.com/dmwm/CRABServer/issues/9094#issuecomment-2958310206) will be changed to


*   always upload input metadata before handing control to ASO
*   introduce self.useAsoRucio and when true
    * upload output metadata  right after triggering ASO work (in first PJ iteration)
    *  do not and set publish flag to True in PostJob
*   keep the PJ running also for ASO-Rucio so that job status is reported the same way as it is now.
*  in ASO/Rucio/Actions/MonitorLockStatus/updateREESTFileDocsBlockCompletionInfo also set  publish flag to True 
*   no changes to Publisher

## Comment (belforte, 2025-06-16T12:50:08Z)

the above appears to work now.
The remaining problem is that after a `crab kill`, all jobs in transfer are listed as failed because PostJob did not complete the the "wait for transfer" cycle, but Rucio will still transfer files and ASO-Rucio will close blocks and trigger publishing.
So my test ended up with published files from failed jobs. I am not sure if this is only bad looking or will also give problems for a possible `crab recover`. In my test all jobs were failed, so `crab recover` refused to recover. But realistically that's an extreme case.

I will consolidate work here for the time being.

## Comment (belforte, 2025-06-18T10:23:54Z)

closing note: in one example I verified that kill + recovery gets the full sample analysed and published. The "problem" is that some jobs are listed as failed in crab status even if everything is fine and output is published.
I have no good idea how to address that.
@dciangot suggestions welcome
