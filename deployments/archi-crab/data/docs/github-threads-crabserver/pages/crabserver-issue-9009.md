# dmwm/CRABServer issue #9009: CCV test fails for CMSSW_7_6_7

State: closed
Opened: 2025-03-19T17:41:20Z
Closed: 2025-03-27T13:12:40Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9009

## Opening post (belforte, 2025-03-19T17:41:20Z)

see #9005 and #9008 

we "reproducibly" get
```
SUCCESSFUL TESTS:
outputFiles-check.sh 250319_160605:cmsbot_crab_outputFiles - 0
inputDBS-check.sh 250319_160618:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 250319_160620:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250319_160621:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 250319_160622:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250319_160623:cmsbot_crab_runRange - 0
userInputFiles-check.sh 250319_160624:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250319_160625:cmsbot_crab_whitelist - 0

FAILED TESTS:
transferOutputs-check.sh 250319_160557:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 250319_160558:cmsbot_crab_transferLogs - 1
activity-check.sh 250319_160559:cmsbot_crab_activity - 1
inputFiles-check.sh 250319_160602:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 250319_160602:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 250319_160606:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 250319_160607:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 250319_160607:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 250319_160610:cmsbot_crab_numCores - 1
scriptExe-check.sh 250319_160611:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250319_160612:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 250319_160615:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 250319_160618:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 250319_160619:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 250319_160624:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 250319_160626:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 250319_160627:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 250319_160627:cmsbot_crab_voRole - 1
voGroup-check.sh 250319_160628:cmsbot_crab_voGroup - 1
scheddName-check.sh 250319_160629:cmsbot_crab_scheddName - 1
collector-check.sh 250319_160629:cmsbot_crab_collector - 1
extraJDL-check.sh 250319_160630:cmsbot_crab_extraJDL - 1

RETRY TESTS:
 none
```

why ?

## Comment (belforte, 2025-03-19T17:43:41Z)

hmm... seems "easy":
```
Warning:			Task could not be submitted because not all blocks of dataset /GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO are on DISK
				Will request a full disk copy for you. See
				 https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul
				A disk replica has been requested to Rucio.  Check progress via:
				  rucio rule-info 19a7ef52d19c446f8dc92ad39b859f9c
```

since that CMSSW release needs an ancient dataset to read, we should ask DM to keep it on disk forever.  It is only  171 GB !

## Comment (belforte, 2025-03-20T11:28:12Z)

automatic tape recall nicely completed.
now that dataset is on disk all test succeeded except `blacklist`. This is simply because the dataset was placed at T2_ES_CIEMAT [1] but
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/test/makeTests.py#L557-L559

so task failed to be submitted.

[1]
```console
belforte@lxplus804/TC3> crab checkdataset --dataset  /GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO
Rucio client intialized for account belforte
dataset status in DBS is: VALID
dataset size is: 171 GB
Checking disk availability of dataset: /GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO
 only fully available (i.e. complete) block replicas are considered 
dataset has 1 blocks
Check blocks availabiliyt on disk
dataset is on tape at: {'T0_CH_CERN_Tape'}
   0 blocks have  0 disk replicas
   1 blocks have  1 disk replicas
 Dataset is fully available

 Block locations:
         T2_ES_CIEMAT hosts   1 blocks

```

## Comment (belforte, 2025-03-20T12:15:50Z)

we should ask DM to make one copy at CERN and one at FNAL.

## Comment (belforte, 2025-03-20T12:32:30Z)

OTOH there is hope that use of CMSSW_7_x has finally went to none

![Image](https://github.com/user-attachments/assets/5452f99c-f043-4388-9fef-b311272b45cf)

from https://monit-grafana.cern.ch/goto/g5IUA92Hg?orgId=11

Maybe simply stop validating ?

## Comment (belforte, 2025-03-20T15:46:29Z)

@aspiringmind-code when you happen to be at CERN together  with someone from DataTransfer, can you kindly ask for this dataset to be placed on disk ? The can use same "category" as for the current HammerCloud datset `/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM`

## Comment (aspiringmind-code, 2025-03-25T13:16:15Z)

[CMSTRANSF JIRA](https://its.cern.ch/jira/browse/CMSTRANSF-1128) ticket created to address this issue.

## Comment (belforte, 2025-03-27T11:55:17Z)

note: see the [CMSTRANSF JIRA](https://its.cern.ch/jira/browse/CMSTRANSF-1128) ticket, that dataset has some buggy rules in Rucio which prevents DM from keeping it at CERN. Easier solution is to use a different dataset
