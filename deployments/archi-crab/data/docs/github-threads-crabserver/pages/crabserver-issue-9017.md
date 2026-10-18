# dmwm/CRABServer issue #9017: #957: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2025-03-27T12:36:02Z
Closed: 2025-03-31T08:29:37Z
URL: https://github.com/dmwm/CRABServer/issues/9017

## Opening post (cmsdmwmbot, 2025-03-27T12:36:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2025-03-27 13:36:01
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/957/)

## Comment (cmsdmwmbot, 2025-03-27T12:38:11Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
250327_123619:cmsbot_crab_transferOutputs
250327_123622:cmsbot_crab_transferLogs
250327_123625:cmsbot_crab_activity
250327_123630:cmsbot_crab_inputFiles
250327_123633:cmsbot_crab_disableAutomaticOutputCollection
250327_123638:cmsbot_crab_outputFiles
250327_123641:cmsbot_crab_allowUndistributedCMSSW
250327_123643:cmsbot_crab_maxMemoryMB
250327_123646:cmsbot_crab_maxJobRuntimeMin
250327_123651:cmsbot_crab_numCores
250327_123654:cmsbot_crab_scriptExe
250327_123657:cmsbot_crab_scriptArgs
250327_123702:cmsbot_crab_sendVenvFolder
250327_123707:cmsbot_crab_sendExternalFolder
250327_123708:cmsbot_crab_inputDBS
250327_123711:cmsbot_crab_useParent
250327_123714:cmsbot_crab_secondaryInputDataset
250327_123717:cmsbot_crab_lumiMaskFile
250327_123721:cmsbot_crab_outLFNDirBase
250327_123722:cmsbot_crab_runRange
250327_123725:cmsbot_crab_ignoreLocality
250327_123725:cmsbot_crab_userInputFiles
250327_123728:cmsbot_crab_whitelist
250327_123732:cmsbot_crab_blacklist
250327_123734:cmsbot_crab_ignoreGlobalBlacklist
250327_123737:cmsbot_crab_voRole
250327_123740:cmsbot_crab_voGroup
250327_123743:cmsbot_crab_scheddName
250327_123746:cmsbot_crab_collector
250327_123749:cmsbot_crab_extraJDL
```

Finished at: 2025-03-27 13:37:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/957/console)

## Comment (cmsdmwmbot, 2025-03-27T12:59:43Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-03-27 13:59:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1290/console

```
SUCCESSFUL TESTS:
outputFiles-check.sh 250327_123638:cmsbot_crab_outputFiles - 0
inputDBS-check.sh 250327_123708:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 250327_123714:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250327_123717:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 250327_123721:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250327_123722:cmsbot_crab_runRange - 0
userInputFiles-check.sh 250327_123725:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250327_123728:cmsbot_crab_whitelist - 0

FAILED TESTS:
transferOutputs-check.sh 250327_123619:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 250327_123622:cmsbot_crab_transferLogs - 1
activity-check.sh 250327_123625:cmsbot_crab_activity - 1
inputFiles-check.sh 250327_123630:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 250327_123633:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 250327_123641:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 250327_123643:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 250327_123646:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 250327_123651:cmsbot_crab_numCores - 1
scriptExe-check.sh 250327_123654:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250327_123657:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 250327_123702:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 250327_123707:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 250327_123711:cmsbot_crab_useParent - 1
ignoreLocality-check.sh 250327_123725:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 250327_123732:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 250327_123734:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 250327_123737:cmsbot_crab_voRole - 1
voGroup-check.sh 250327_123740:cmsbot_crab_voGroup - 1
scheddName-check.sh 250327_123743:cmsbot_crab_scheddName - 1
collector-check.sh 250327_123746:cmsbot_crab_collector - 1
extraJDL-check.sh 250327_123749:cmsbot_crab_extraJDL - 1

RETRY TESTS:
 none
```
