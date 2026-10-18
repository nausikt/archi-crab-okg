# dmwm/CRABServer issue #8319: #748: Test dev CRABClient using prod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-04-04T10:06:10Z
Closed: 2024-04-04T11:23:35Z
URL: https://github.com/dmwm/CRABServer/issues/8319

## Opening post (cmsdmwmbot, 2024-04-04T10:06:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-04 12:06:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/748/)

## Comment (cmsdmwmbot, 2024-04-04T10:07:25Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240404_100629:cmsbot_crab_transferOutputs
240404_100630:cmsbot_crab_transferLogs
240404_100631:cmsbot_crab_activity
240404_100633:cmsbot_crab_inputFiles
240404_100634:cmsbot_crab_disableAutomaticOutputCollection
240404_100634:cmsbot_crab_outputFiles
240404_100636:cmsbot_crab_allowUndistributedCMSSW
240404_100636:cmsbot_crab_maxMemoryMB
240404_100638:cmsbot_crab_maxJobRuntimeMin
240404_100639:cmsbot_crab_numCores
240404_100640:cmsbot_crab_scriptExe
240404_100641:cmsbot_crab_scriptArgs
240404_100642:cmsbot_crab_sendVenvFolder
240404_100645:cmsbot_crab_sendExternalFolder
240404_100645:cmsbot_crab_inputDBS
240404_100646:cmsbot_crab_useParent
240404_100647:cmsbot_crab_secondaryInputDataset
240404_100648:cmsbot_crab_lumiMaskFile
240404_100651:cmsbot_crab_lumiMaskUrl
240404_100653:cmsbot_crab_outLFNDirBase
240404_100654:cmsbot_crab_runRange
240404_100655:cmsbot_crab_ignoreLocality
240404_100656:cmsbot_crab_userInputFiles
240404_100657:cmsbot_crab_whitelist
240404_100658:cmsbot_crab_blacklist
240404_100659:cmsbot_crab_ignoreGlobalBlacklist
240404_100700:cmsbot_crab_voRole
240404_100701:cmsbot_crab_voGroup
240404_100702:cmsbot_crab_scheddName
240404_100702:cmsbot_crab_collector
240404_100703:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240404_100628:cmsbot_crab_20240404_120627
```

Finished at: 2024-04-04 12:07:04
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/748/console)

## Comment (cmsdmwmbot, 2024-04-04T10:30:53Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-04 12:30:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/523/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/523//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-04T10:31:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-04 12:31:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1020/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240404_100651:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240404_100654:cmsbot_crab_runRange - 2
whitelist-check.sh 240404_100657:cmsbot_crab_whitelist - 2
blacklist-check.sh 240404_100658:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_100629:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240404_100630:cmsbot_crab_transferLogs - 0
activity-check.sh 240404_100631:cmsbot_crab_activity - 0
inputFiles-check.sh 240404_100633:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_100634:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240404_100634:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240404_100636:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240404_100636:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240404_100638:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240404_100639:cmsbot_crab_numCores - 0
scriptExe-check.sh 240404_100640:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240404_100641:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240404_100642:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_100645:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_100645:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_100646:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_100647:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240404_100648:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240404_100653:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240404_100655:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240404_100656:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240404_100659:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240404_100700:cmsbot_crab_voRole - 0
voGroup-check.sh 240404_100701:cmsbot_crab_voGroup - 0
scheddName-check.sh 240404_100702:cmsbot_crab_scheddName - 0
collector-check.sh 240404_100702:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_100703:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-04T10:55:32Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-04 12:55:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1021/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240404_100629:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240404_100630:cmsbot_crab_transferLogs - 0
activity-check.sh 240404_100631:cmsbot_crab_activity - 0
inputFiles-check.sh 240404_100633:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240404_100634:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240404_100634:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240404_100636:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240404_100636:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240404_100638:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240404_100639:cmsbot_crab_numCores - 0
scriptExe-check.sh 240404_100640:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240404_100641:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240404_100642:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240404_100645:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240404_100645:cmsbot_crab_inputDBS - 0
useParent-check.sh 240404_100646:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240404_100647:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240404_100648:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240404_100651:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240404_100653:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240404_100654:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240404_100655:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240404_100656:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240404_100657:cmsbot_crab_whitelist - 0
blacklist-check.sh 240404_100658:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240404_100659:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240404_100700:cmsbot_crab_voRole - 0
voGroup-check.sh 240404_100701:cmsbot_crab_voGroup - 0
scheddName-check.sh 240404_100702:cmsbot_crab_scheddName - 0
collector-check.sh 240404_100702:cmsbot_crab_collector - 0
extraJDL-check.sh 240404_100703:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-04-04T11:23:35Z)

OK
