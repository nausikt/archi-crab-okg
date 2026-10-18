# dmwm/CRABServer issue #7718: Non-EDM outputs do not have checksums in transfers.txt which required by Rucio.

State: closed
Opened: 2023-07-06T08:28:10Z
Closed: 2023-07-19T08:38:58Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7718

## Opening post (novicecpp, 2023-07-06T08:28:10Z)

File-to-transfer items in `transfers.txt` are updated by `PostJob.py`, which contains checksums `PostJob.py` read from json FJR. 
But for the non-EDM files (including logs when `logsTransfer=True`), JobWrapper does not calculate checksums and puts them in FJR. So `PostJob.py` use [placeholder checksums](https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/TaskWorker/Actions/PostJob.py#L2697) instead and passes to `transfers.txt`.

This break Rucio ASO because adler32 checksums is required for [add_replica](https://github.com/rucio/rucio/blob/85bb8a9e93f9515b5868e96349a59984eb63a110/lib/rucio/client/replicaclient.py#L238) API.

It does not break FTS ASO because we never pass any checksums to FTS jobs ([FTS_Transfers.py#L247-L342](https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/scripts/task_process/FTS_Transfers.py#L247-L342)).

## Comment (novicecpp, 2023-07-06T08:31:07Z)

Original discussion on MatterMost (Thanks Stefano for great explanation).

**Q:**

I tried to copy task [230613_131234:christok_crab_ChargedHiggsToHW_HToTauTau_M_700_MH2_M_200_1L](https://cmsweb.cern.ch/crabserver/ui/task/230613_131234:christok_crab_ChargedHiggsToHW_HToTauTau_M_700_MH2_M_200_1L) to run in test12 with my custom crabclient.
I found that copied tasks run in test12, especially tasks that have non-edm files, always had adler32 hash to 0 even though fjr json report correct hash (example [postjob](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230628_071411:tseethon_crab_copyoftask_notedmfile_test12_20230628_091312/postjob.3.0.txt) logs).

**A:**

[Job](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230628_071411:tseethon_crab_copyoftask_notedmfile_test12_20230628_091312/job_out.3.0.txt) has two output files `jettoolbox.root` and `miniaod2tree.root`.
In the [fjr](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230628_071411:tseethon_crab_copyoftask_notedmfile_test12_20230628_091312/job_fjr.3.0.json) both are listed but only the former has values for the checksums (adler32 and cksum). The [PostJob](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230628_071411:tseethon_crab_copyoftask_notedmfile_test12_20230628_091312/postjob.3.0.txt) only refers to `miniaod2tree.root`. At this point it makes sense that adler32 and cksum are 0 in PostJob, but I still can not say why:
1) second file does not have cksum values in FJR
2) PostJob only works on second file

I think the solution to mistery in the what happened on the grid node (note [1])
It looks that this task had an inusual [configuration](https://cmsweb.cern.ch:8443/scheddmon/0122/christok/230613_131234:christok_crab_ChargedHiggsToHW_HToTauTau_M_700_MH2_M_200_1L/debug/crabConfig.py) [2] (skip EDM output from cmsRUn and only take a non-EDM file) and it is possible that simply in this case we do not have adler32/cksum from cmsRun (we do not compute those with "CRAB" code).

We need to keep in mind that non-EDM files are special, e.g. we do not publish them in DBS. And I believe that we
only use checksum to store them in DBS. Differently from file size, the checksums do not go in FILETRANSFERSDB. I am not sure that we send them to FTS in current ASO. It is also possible that if we do, and send 0, nobody on our side ever notices and FTS ignores it. All things to check.

Indeed already the original [PostJob](https://cmsweb.cern.ch:8443/scheddmon/0122/christok/230613_131234:christok_crab_ChargedHiggsToHW_HToTauTau_M_700_MH2_M_200_1L/postjob.3.0.txt) has these lines

```
Tue, 13 Jun 2023 17:02:48 CEST(+0200):INFO:PostJob ASO job description: {'_id': '49bb163ba3505509828c029b790fcad9fe9da538072e7d2d7edffb78',
 'checksums': {'adler32': '0', 'cksum': '0'},
 'dbs_url': 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader',
 'destination': 'T3_US_FNALLPC',
 'destination_lfn': '/store/user/christok/CRAB3_TransferData/multicrab-SingleLepton-CMSSW10_6_29-Run2018ABCD-dataVersion2018_106XUL-20Jun2022/ChargedHiggsToHW_HToTauTau_M-700_MH2_M-200_1L_TuneCP5_13TeV-amcatnlo_pythia8/crab_ChargedHiggsToHW_HToTauTau_M_700_MH2_M_200_1L/230613_131234/0000/miniaod2tree_3.root',
And e.g. for log files, which we move via FTS, we have fake hardcode values https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/src/python/TaskWorker/Actions/PostJob.py#L2316
```

Sorry for long, multiply edited, message. We should probably follow up in some better way.

[1] this lines are "curious"
```
== JOB AD: CRAB_EDMOutputFiles = {  }
== JOB AD: CRAB_AdditionalOutputFiles = { "miniaod2tree.root" }
```
[2]
```
config.JobType.outputFiles = ['miniaod2tree.root']
config.JobType.disableAutomaticOutputCollection = True

## Comment (novicecpp, 2023-07-19T08:38:58Z)

Done
