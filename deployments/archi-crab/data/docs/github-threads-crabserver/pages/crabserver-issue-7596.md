# dmwm/CRABServer issue #7596: improve message from TW when (some) data is missing

State: closed
Opened: 2023-04-14T08:06:50Z
Closed: 2023-11-09T20:26:37Z
Labels: Type: Enhancement, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7596

## Opening post (belforte, 2023-04-14T08:06:50Z)

make sure that it is clear if problem is data not on disk or present at blacklisted sites etc. 
avoid list of blocks, but possible give users a command to obtain such list

Need a recent example to start, since some improvement was made lately by @novicecpp  already

## Comment (belforte, 2023-04-14T12:09:58Z)

from current master, for AOD on tape:
```
belforte@lxplus801/TC3> crab status 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230414_140653
Task name:			230414_120657:belforte_crab_20230414_140653
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	TAPERECALL
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/230414_120657%3Abelforte_crab_20230414_140653
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230414_120657%3Abelforte_crab_20230414_140653&from=1681470417000&to=now
Warning:			Task could not be submitted because not all blocks of dataset /DoubleMuon/Run2018B-12Nov2019_UL2018-v2/AOD are on DISK
				Will try to request a full disk copy for you. See
				 https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul
				A disk replica has been requested to Rucio (rule ID: 09aa915fe8b348baa70cd477a9a05dc2 )
				you can check progress via either of the following two commands:
				 rucio rule-info 09aa915fe8b348baa70cd477a9a05dc2
				 rucio list-rules user.crab_tape_recall:/TapeRecall/230414_120657.belforte_crab_20230414_140653/USER
				or simply check 'state' line in this page: https://cms-rucio-webui.cern.ch/rule?rule_id=09aa915fe8b348baa70cd477a9a05dc2
				This task will be automatically submitted as soon as the stage-out is completed.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230414_140653/crab.log
belforte@lxplus801/TC3> 
```

for a dataset partially on disk:
```
belforte@lxplus806/TC3> crab status 
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230415_145311
Task name:			230415_125316:belforte_crab_20230415_145311
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	TAPERECALL
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/230415_125316%3Abelforte_crab_20230415_145311
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230415_125316%3Abelforte_crab_20230415_145311&from=1681559597000&to=now
Warning:			Task could not be submitted because not all blocks of dataset /WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM are on DISK
				Will try to request a full disk copy for you. See
				 https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul
				A disk replica has been requested to Rucio (rule ID: e9e9b0be941948d5b976d740777d7091 )
				you can check progress via either of the following two commands:
				 rucio rule-info e9e9b0be941948d5b976d740777d7091
				 rucio list-rules user.crab_tape_recall:/TapeRecall/230415_125316.belforte_crab_20230415_145311/USER
				or simply check 'state' line in this page: https://cms-rucio-webui.cern.ch/rule?rule_id=e9e9b0be941948d5b976d740777d7091
				This task will be automatically submitted as soon as the stage-out is completed.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230415_145311/crab.log
belforte@lxplus806/TC3> 
```

## Comment (belforte, 2023-04-17T12:05:40Z)

the above ones are fine information-wise. But messages about Rucio can be shortened to
```
There's no full disk replica of dataset
 /DoubleMuon/Run2018B-12Nov2019_UL2018-v2/AOD 
A disk replica has been requested to Rucio, task will be automatically submitted once completed
you can check progress of Rucio rule 09aa915fe8b348baa70cd477a9a05dc2
in this page: https://cms-rucio-webui.cern.ch/rule?rule_id=09aa915fe8b348baa70cd477a9a05dc2
CRAB will wait up to 30 days, once data is on disk, files will be locked for 30 days
```
@mapellidario @novicecpp I  am still disturbed by such a long message and welcome suggestions. Thanks !

## Comment (belforte, 2023-04-19T22:19:29Z)

waiting to collect examples from other situations, like when blocks are at blacklisted sites

## Comment (belforte, 2023-08-17T10:28:20Z)

I am inclined to consider this closed and keep current message. Since it is build a piece at a time as execution progresses through DBSDataDiscovery and TapeRecall, there's no simple way to shorten.
Any additional info like how long it tries etc. can be put in the [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul)

## Comment (belforte, 2023-08-17T19:18:19Z)

Oh well. Here's and example of where things really stinks
```
belforte@lxplus812/TC3> crab status -d ./crab_20230817_210830
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230817_210830
Task name:			230817_190833:belforte_crab_20230817_210830
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw03
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/230817_190833%3Abelforte_crab_20230817_210830
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230817_190833%3Abelforte_crab_20230817_210830&from=1692295714000&to=now
Warning:			Some blocks are on TAPE only and will not be processed.
				There is no automatic recall from tape for data tier 'RAW' if 'Data.inputBlocks' is not provided.
				If you need the full dataset, contact Data Transfer team via cmstalk+computing-tools@dovecotmta.cern.ch
Warning:			3 blocks will be skipped because are not completely replicated on DISK: ['/MuonEG/Run2016B-v1/RAW#9da47a68-1682-11e6-8d9e-001e67ac06a0', '/MuonEG/Run2016B-v1/RAW#898359ee-1760-11e6-8d9e-001e67ac06a0', '/MuonEG/Run2016B-v1/RAW#cd4b1b62-13aa-11e6-a3f4-001e67ac06a0']
Warning:			block(s) {'/MuonEG/Run2016B-v1/RAW#86bc5e3e-1519-11e6-a3f4-001e67ac06a0'} present at ['T1_ES_PIC'] will be skipped because those sites are not in user white list
Failure message from server:	The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset '/MuonEG/Run2016B-v1/RAW'. (or at least for the part of the dataset that passed the lumi-mask and/or run-range selection).
				 Found 1 (out of 1) blocks present only at blacklisted sites. Global CRAB3 blacklist is {'T3_US_Brown', 'T3_CH_CERN_OpenData', 'T2_ES_IFCA', 'T3_RU_FIAN', 'T3_US_UMiss', 'T3_US_Princeton_ICSE', 'T3_US_ANL', 'T2_FR_GRIF', 'T3_US_OSG', 'T0_CH_CSCS_HPC', 'T3_IT_MIB', 'T2_BR_UERJ', 'T2_PT_NCG_Lisbon', 'T3_TW_NTU_HEP', 'T3_US_Anvil', 'T3_BY_NCPHEP', 'T2_GR_Ioannina', 'T3_UK_SGrid_Oxford', 'T3_US_Lancium', 'T3_US_JHU', 'T3_GR_IASA', 'T3_KR_KISTI', 'T2_CH_CSCS', 'T0_CH_CERN', 'T3_KR_UOS', 'T2_TR_METU', 'T3_US_Kansas', 'T3_US_MIT', 'T2_CH_CERN_P5', 'T3_US_NotreDame', 'T2_KR_KISTI', 'T3_CY_UCY', 'T3_IR_IPM', 'T3_FR_IPNL', 'T3_HR_IRB', 'T3_US_UCD', 'T3_CH_CERNBOX', 'T3_CH_CERN_HelixNebula', 'T3_US_Ookami', 'T3_US_Rutgers', 'T3_US_PSC', 'T3_US_NERSC', 'T3_US_SDSC', 'T2_UK_SGrid_
				[... message truncated to the first 1000 chars ...]
```
there is no point in trying to print the full blacklist which is so horrendously long. Maybe remove T3's. Only put number-of and a pointer to where the list is taken from

## Comment (belforte, 2023-08-17T19:19:00Z)

On console, with line-wrapping the message is really really bad
belforte@lxplus812/TC3> crab status -d ./crab_20230817_210830
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230817_210830
Task name:			230817_190833:belforte_crab_20230817_210830
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw03
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/230817_190833%3Abelforte_crab_20230817_210830
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=230817_190833%3Abelforte_crab_20230817_210830&from=1692295714000&to=now
Warning:			Some blocks are on TAPE only and will not be processed.
				There is no automatic recall from tape for data tier 'RAW' if 'Data.inputBlocks' is not provided.
				If you need the full dataset, contact Data Transfer team via cmstalk+computing-tools@dovecotmta.cern.ch
Warning:			3 blocks will be skipped because are not completely replicated on DISK: ['/MuonEG/Run2016B-v1/RAW#9da47a68-1682-11e6-8d9e-001e67ac06a0', '/MuonEG/Run2016B-v1/RAW#898359ee-1760-11e6-8d9e-001e67ac06a0', '/MuonEG/Run2016B-v1/RAW#cd4b1b62-13aa-11e6-a3f4-001e67ac06a0']
Warning:			block(s) {'/MuonEG/Run2016B-v1/RAW#86bc5e3e-1519-11e6-a3f4-001e67ac06a0'} present at ['T1_ES_PIC'] will be skipped because those sites are not in user white list
Failure message from server:	The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset '/MuonEG/Run2016B-v1/RAW'. (or at least for the part of the dataset that passed the lumi-mask and/or run-range selection).
				 Found 1 (out of 1) blocks present only at blacklisted sites. Global CRAB3 blacklist is {'T3_US_Brown', 'T3_CH_CERN_OpenData', 'T2_ES_IFCA', 'T3_RU_FIAN', 'T3_US_UMiss', 'T3_US_Princeton_ICSE', 'T3_US_ANL', 'T2_FR_GRIF', 'T3_US_OSG', 'T0_CH_CSCS_HPC', 'T3_IT_MIB', 'T2_BR_UERJ', 'T2_PT_NCG_Lisbon', 'T3_TW_NTU_HEP', 'T3_US_Anvil', 'T3_BY_NCPHEP', 'T2_GR_Ioannina', 'T3_UK_SGrid_Oxford', 'T3_US_Lancium', 'T3_US_JHU', 'T3_GR_IASA', 'T3_KR_KISTI', 'T2_CH_CSCS', 'T0_CH_CERN', 'T3_KR_UOS', 'T2_TR_METU', 'T3_US_Kansas', 'T3_US_MIT', 'T2_CH_CERN_P5', 'T3_US_NotreDame', 'T2_KR_KISTI', 'T3_CY_UCY', 'T3_IR_IPM', 'T3_FR_IPNL', 'T3_HR_IRB', 'T3_US_UCD', 'T3_CH_CERNBOX', 'T3_CH_CERN_HelixNebula', 'T3_US_Ookami', 'T3_US_Rutgers', 'T3_US_PSC', 'T3_US_NERSC', 'T3_US_SDSC', 'T2_UK_SGrid_
				[... message truncated to the first 1000 chars ...]

## Comment (belforte, 2023-11-08T09:22:41Z)

- [x] the blacklist must be short or be a pointer to a page, as is it is unusable for reading
- [x] the list of skipped blocks could be trimmed to the hash after the dataset name
   * on second thought I am printing fewer (3) blocks but keeping full name, to avoid people getting confused or reporting to us just an hash w/o the dataset part

## Comment (belforte, 2023-11-08T17:32:42Z)

new crab status output when available sites are blacklisted
```
belforte@lxplus800/TC3> crab status
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20231108_182823
Task name:			231108_172832:belforte_crab_20231108_182823
Grid scheduler - Task Worker:	N/A yet - crab-dev-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/231108_172832%3Abelforte_crab_20231108_182823
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=231108_172832%3Abelforte_crab_20231108_182823&from=1699460912000&to=now
Warning:			59 block(s) ['/SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD#008c34c9-1ea7-4615-87aa-8ef3099e7854', '/SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD#01ae2a04-40b1-4274-99c7-e60f75d97a57', '/SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD#070a6477-e4c7-4c51-83c2-3cd51f7504ab', '...'] present at ['T1_UK_RAL'] will be skipped because those sites are not in user white list
Failure message from server:	The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset '/SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD'. (or at least for the part of the dataset that passed the lumi-mask and/or run-range selection).
				 Found 59 (out of 59) blocks present only at blacklisted not-whitelisted, and/or non-accelerator sites.
				Global blacklist contain these T1/T2: ['T2_GR_Ioannina', 'T2_UK_London_Brunel', 'T2_UK_SGrid_Bristol', 'T2_CH_CERN_HLT', 'T2_CH_CERN_P5', 'T2_TW_NCHC', 'T2_FR_IPHC', 'T2_FR_GRIF_IRFU'] and 39 T3's
				 Full list at https://cmssst.web.cern.ch/cmssst/analysis/usableSites.json
				 User whitelist is {'T2_CH_CERN'}.
				
```
on the console:
![image](https://github.com/dmwm/CRABServer/assets/1837785/55da5c11-009b-4996-a464-67e87d724f0b)

## Comment (belforte, 2023-11-08T17:35:19Z)

I can't reproduce the `Warning: 3 blocks will be skipped because are not completely replicated on DISK:`message now, but am trimming that list to first 3 blocks as well.

## Comment (belforte, 2023-11-08T20:06:18Z)

I have also added a hint to use `crab checkdataset` to help figure out why some or all bloks are not accessible.

Anyhow we should be free of the long, truncated messages.
