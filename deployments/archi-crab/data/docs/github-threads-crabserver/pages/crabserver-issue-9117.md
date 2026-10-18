# dmwm/CRABServer issue #9117: when using ASO/Rucio too many files are published

State: closed
Opened: 2025-07-03T15:54:13Z
Closed: 2025-07-08T13:23:21Z
Labels: Type: Bug, Status: Done, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/9117

## Opening post (belforte, 2025-07-03T15:54:13Z)

one of our pipeline tests now returns:
```
belforte@lxplus804/crabint1> crab status -d crab_rucio_transfers_withnoneedm_20250630_120430/
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/crabint1/crab_rucio_transfers_withnoneedm_20250630_120430
Task name:			250630_100432:crabint1_crab_rucio_transfers_withnoneedm_20250630_120430
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw04
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/250630_100432%3Acrabint1_crab_rucio_transfers_withnoneedm_20250630_120430
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250630_100432%3Acrabint1_crab_rucio_transfers_withnoneedm_20250630_120430&from=1751274272000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_IT_Rome', 'T2_IT_Pisa']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (10/10)

Transfer container's name:	/GenericTTbar/crabint1-ruciotransfers-1751277870-94ba0e06145abd65ccb1d21786dc7e1d_TRANSFER.bc6fb57d/USER
Transfer container's rule:	https://cms-rucio-webui.cern.ch/rule?rule_id=e39c4859c1ef4bc19de57b47cfead807

Tips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 

Publication status of 1 dataset(s):	done         		200.0% (20/10)
(from CRAB internal bookkeeping in transferdb)
					unsubmitted  		-100.0% (-10/10)

```

While this does not happen when using ASO/FTS

The point is that there are two output files per job, one is not EDM and should not be published. Ideed this is reported at submittions time:
`Warning: The following output files will not be published, as they are not EDM files: ['\''miniaodfake.root'\'']`

So I think that somehow my latest changes to Rucio vs. Publisher made the extra files to be published, so confusing crab status count, and I do not know with what metadata !

FYI @aspiringmind-code

## Comment (belforte, 2025-07-04T07:37:00Z)

indeed both files end up on DBS
https://cmsweb.cern.ch:8443/das/request?instance=prod/phys03&input=file+dataset%3D%2FGenericTTbar%2Fcrabint1-ruciotransfers-1751277870-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER

and the `miniaodfake_X.root` ones have no parents, no lumis, no run info !

at least there are two blocks, naming is highly supsicious though:
```
/FakeDataset/fakefile-FakePublish-bc6fb57d3a397994ae798441918bee38_miniaodfake.root/USER#57b98859-3a31-43fb-ab20-2876835a2c8b
/GenericTTbar/crabint1-ruciotransfers-1751277870-94ba0e06145abd65ccb1d21786dc7e1d/USER#708e91a5-b8ff-4821-b9a3-f8f485f7bba1
```
The latter has the desired output files, the former has 10 files but DAS is unable to list them
https://cmsweb.cern.ch:8443/das/request?input=block%3D%2FFakeDataset%2Ffakefile-FakePublish-bc6fb57d3a397994ae798441918bee38_miniaodfake.root%2FUSER%2357b98859-3a31-43fb-ab20-2876835a2c8b&instance=prod/phys03

I susspect that the dot in the block name is not accepted by DAS [1], odd that it was added in DBS !

[1]
```
dasgoclient --query 'block block=/FakeDataset/fakefile-FakePublish-bc6fb57d3a397994ae798441918bee38_miniaodfake.root/USER#57b98859-3a31-43fb-ab20-2876835a2c8'
Validation error: unmatched block pattern
```

bloody mess !!

## Comment (belforte, 2025-07-07T21:23:57Z)

the dot is allowed in the ProcessedDS field in WMCore/Lexicon. So the odd DAS failures is... strange.
But e.g. `dasgoclient` "happily refuses that dot"
```
belforte@lxplus9105/TC3> dasgoclient --query 'dataset dataset=/A/B/USER'
/A/B/USER
belforte@lxplus9105/TC3> dasgoclient --query 'dataset dataset=/A/B.C/USER'
Validation error: unmatched dataset pattern
belforte@lxplus9105/TC3>
```

## Comment (belforte, 2025-07-07T21:29:38Z)

anyhow this clearly means that I "overdid" things in https://github.com/dmwm/CRABServer/issues/9094#issuecomment-2967626331
Now ASO/Rucio sets publish flag for all files which it transfers. It should do it only for those which will go into the Publish container.

## Comment (belforte, 2025-07-07T21:33:33Z)

So I put at top priority because it is better to do it now that I have things reasonably fresh in memory

## Comment (belforte, 2025-07-07T21:44:09Z)

IIUC this may be as simple as 
* do not update publish flag in REST if primary dataset is `/FakeDataset`
   * why was previous code updating the block info ? maybe an oversight ? maybe intentionally to avoid "if" ?

## Comment (belforte, 2025-07-07T21:52:41Z)

all in all it may be OK to keep the file/dataset association in filetransfersdb for all files, so I can keep "updateRest" as is and only filter out non-edm files in https://github.com/dmwm/CRABServer/blob/724ae2642f3a55b4d3acafed551700e414b918dd/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L279-L287

simply create a new `fileDocs` list with only the files wich should go in DBS

## Comment (oljemark, 2025-07-15T19:09:06Z)

Hi, @belforte . Was the data-aset typoed member variable name used somewhere else in dmwm, or were you intending to use dataset?

## Comment (belforte, 2025-07-20T14:13:11Z)

thanka @oljemark it was a stupid typo. 
I merged your commit in https://github.com/dmwm/CRABServer/pull/9135

(sorry for delay, I was away)
