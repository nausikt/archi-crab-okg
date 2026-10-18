# dmwm/CRABServer issue #9008: #954: Test dev CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2025-03-19T16:05:44Z
Closed: 2025-03-31T08:30:39Z
URL: https://github.com/dmwm/CRABServer/issues/9008

## Opening post (cmsdmwmbot, 2025-03-19T16:05:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2025-03-19 17:05:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/954/)

## Comment (cmsdmwmbot, 2025-03-19T16:06:52Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_160556:cmsbot_crab_20250319_170554
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250319_160557:cmsbot_crab_transferOutputs
250319_160558:cmsbot_crab_transferLogs
250319_160559:cmsbot_crab_activity
250319_160602:cmsbot_crab_inputFiles
250319_160602:cmsbot_crab_disableAutomaticOutputCollection
250319_160605:cmsbot_crab_outputFiles
250319_160606:cmsbot_crab_allowUndistributedCMSSW
250319_160607:cmsbot_crab_maxMemoryMB
250319_160607:cmsbot_crab_maxJobRuntimeMin
250319_160610:cmsbot_crab_numCores
250319_160611:cmsbot_crab_scriptExe
250319_160612:cmsbot_crab_scriptArgs
250319_160615:cmsbot_crab_sendVenvFolder
250319_160618:cmsbot_crab_sendExternalFolder
250319_160618:cmsbot_crab_inputDBS
250319_160619:cmsbot_crab_useParent
250319_160620:cmsbot_crab_secondaryInputDataset
250319_160621:cmsbot_crab_lumiMaskFile
250319_160622:cmsbot_crab_outLFNDirBase
250319_160623:cmsbot_crab_runRange
250319_160624:cmsbot_crab_ignoreLocality
250319_160624:cmsbot_crab_userInputFiles
250319_160625:cmsbot_crab_whitelist
250319_160626:cmsbot_crab_blacklist
250319_160627:cmsbot_crab_ignoreGlobalBlacklist
250319_160627:cmsbot_crab_voRole
250319_160628:cmsbot_crab_voGroup
250319_160629:cmsbot_crab_scheddName
250319_160629:cmsbot_crab_collector
250319_160630:cmsbot_crab_extraJDL
```

Finished at: 2025-03-19 17:06:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/954/console)

## Comment (cmsdmwmbot, 2025-03-19T16:28:06Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-03-19 17:28:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/619/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/619//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-03-19T16:28:16Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-03-19 17:28:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1287/console

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

## Comment (belforte, 2025-03-19T17:25:46Z)

so this failed twice. Also in test 952 #9005 

I will investigate. I think that it may be "as simple as" some check relies on crab client command like `getlog` that do not work in older python2. But if that's the case we should not try them. And I believe that test used to work !

## Comment (belforte, 2025-03-19T17:44:12Z)

this looks simple. See: https://github.com/dmwm/CRABServer/issues/9009

## Comment (belforte, 2025-03-19T17:45:42Z)

input dataset was not on disk. Is there now https://cms-rucio-webui.cern.ch/rule?rule_id=19a7ef52d19c446f8dc92ad39b859f9c
so I will submit this again: #9010

## Comment (belforte, 2025-03-20T10:27:51Z)

new round of Jenkins failed because after 20min most DAGMAns were still in the bootstrap phase. Let's try with preprod TW, which is nicely empty https://github.com/dmwm/CRABServer/issues/9011
