# dmwm/CRABServer issue #7770: implement Publisher for Rucio

State: closed
Opened: 2023-07-17T22:10:01Z
Closed: 2023-08-17T14:09:27Z
URL: https://github.com/dmwm/CRABServer/issues/7770

## Opening post (belforte, 2023-07-17T22:10:01Z)

now that we have a strategy and needed info in `transfersdb` table #7480 
it is time to actually change PublisherMaster and task_publish code.

Changes are likely large enough that I will go for new filenames and see later if PublisherMaster
could be made common.

I will add here non trivial work steps as I identify them

- [x] current code does not retrieve block name/status from DB . Need new SQL
https://github.com/dmwm/CRABServer/blob/2365939e2777e4afa2077f2c6b485b899c1facde/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L111
 #7777 

- [x] and new REST of course : now in [v3.230803](https://github.com/dmwm/CRABServer/releases/tag/v3.230803)
- [x] write new PublisherMasterRucio.py to prepare publisher files in new format (with block info) for TaskPublishRucio.py - now in [my branch](https://github.com/belforte/CRABServer/tree/PublisherForASOviaRucio-7480) 
- [x] write new TaskPublishRucio.py
- [x] test/debug
- [x] devise a way to deploy this new Publisher with minimal changes. Moved to #7836

## Comment (belforte, 2023-08-04T08:35:42Z)

About "devise a way to deploy this new Publisher with minimal changes":

Maybe have two directories in GH instead: `src/python/Publisher/schedd` and `src/python/Publisher/Rucio` ? and have all code (start/stop/run/....) identical but for definition of `$COMMAND_DIR` in https://github.com/dmwm/CRABServer/blob/master/src/script/Deployment/Publisher/start.sh ? 
Maybe more changes will be needed, will have to try

## Comment (belforte, 2023-08-07T15:47:28Z)

format of new Publisher_files
```python

            # TODO this shoudl be a function
            # prepare json to save, will be a list of blocks, one dictionary per block
            #
            # {'name':blockname,
            #    then a few parmeters common to the whole block (to the task! actuallY)
            #  'username', 'acquisitionera', 'swversion', globaltag', 'origin_site'
            # and finally a list of dictionariesx, one per file
            #    'files':[fileDict1, fileDict2,...] }
            # each fileDict has these keys, most values come straight from FileMetadata table
            # a (*) indicated values which in are obtained from info in transfersdb and now in block['filesInfo']
            # 'filetype', 'jobid', 'outdataset', 'inevents', 'publishname', 'lfn'
            # 'runlumi', 'adler32', 'cksum', 'filesize',
            # 'parents', 'state', 'created', 'destination'(*), 'source_lfn'(*)
            # info from FMD will be put in DBS (of course).
            # TODO 'state' appears unused. To be verifies
            # 'destination" will be put in DBS as origin_site
            # source_lfn" aka 'tmplfn' is needed to compute file name hash
            # so that the record in transferdb can be updated with publication
            # successful or not inside TaskPublishRUcio.py
            #
```

## Comment (belforte, 2023-08-10T17:00:49Z)

I have now something that works on the simple example:
```
belforte@lxplus803/wa> crab status -d crab_rucio_transfers_publication_test12_20230712_072245/
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/wa/crab_rucio_transfers_publication_test12_20230712_072245
Task name:			230712_052247:tseethon_crab_rucio_transfers_publication_test12_20230712_072245
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw03
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/230712_052247%3Atseethon_crab_rucio_transfers_publication_test12_20230712_072245
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=tseethon&var-task=230712_052247%3Atseethon_crab_rucio_transfers_publication_test12_20230712_072245&from=1689135768000&to=now
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (100/100)

Rucio Container:  user.tseethon:/GenericTTbar/tseethon-ruciotransfer-1689139365-94ba0e06145abd65ccb1d21786dc7e1d/USER
Tips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 

Publication status of 1 dataset(s):	done         		100.0% (100/100)
(from CRAB internal bookkeeping in transferdb)
```

I am sure that there are many use case (corner or not) which are not handled correctly, as usual dealing with errors and exceptions at the very least, then logging etc. etc.

## Comment (belforte, 2023-08-10T20:25:59Z)

develpment branch for this is now https://github.com/belforte/CRABServer/tree/PublisherForASOviaRucio-fix-7770

## Comment (belforte, 2023-08-10T21:19:03Z)

I decided to reformat a bit the TW and Publisher config. files, moving the parameters for REST interactions into their own section in order to simplify setup of `crabserver` object  via https://github.com/belforte/CRABServer/blob/b765a14cd9924d24a438e6282818173a05ec53f8/src/python/TaskWorker/WorkerUtilities.py#L13

changes will be anyhow backward compatible https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/101 and following two

## Comment (belforte, 2023-08-17T14:17:46Z)

merged and closed so that I get the "minimally working version" integrated, then will fix all use cases which were missed as test progress
