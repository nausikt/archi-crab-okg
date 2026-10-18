# dmwm/CRABServer issue #8516: #811: Test dev CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-06-19T13:06:04Z
Closed: 2024-06-19T14:22:41Z
URL: https://github.com/dmwm/CRABServer/issues/8516

## Opening post (cmsdmwmbot, 2024-06-19T13:06:04Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-06-19 15:06:03
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/811/)

## Comment (cmsdmwmbot, 2024-06-19T13:07:24Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240619_130630:cmsbot_crab_transferOutputs
240619_130631:cmsbot_crab_transferLogs
240619_130631:cmsbot_crab_activity
240619_130633:cmsbot_crab_inputFiles
240619_130634:cmsbot_crab_disableAutomaticOutputCollection
240619_130636:cmsbot_crab_outputFiles
240619_130637:cmsbot_crab_allowUndistributedCMSSW
240619_130638:cmsbot_crab_maxMemoryMB
240619_130639:cmsbot_crab_maxJobRuntimeMin
240619_130641:cmsbot_crab_numCores
240619_130642:cmsbot_crab_scriptExe
240619_130643:cmsbot_crab_scriptArgs
240619_130645:cmsbot_crab_sendVenvFolder
240619_130647:cmsbot_crab_sendExternalFolder
240619_130648:cmsbot_crab_inputDBS
240619_130648:cmsbot_crab_useParent
240619_130649:cmsbot_crab_secondaryInputDataset
240619_130650:cmsbot_crab_lumiMaskFile
240619_130651:cmsbot_crab_lumiMaskUrl
240619_130653:cmsbot_crab_outLFNDirBase
240619_130653:cmsbot_crab_runRange
240619_130654:cmsbot_crab_ignoreLocality
240619_130655:cmsbot_crab_userInputFiles
240619_130656:cmsbot_crab_whitelist
240619_130657:cmsbot_crab_blacklist
240619_130658:cmsbot_crab_ignoreGlobalBlacklist
240619_130659:cmsbot_crab_voRole
240619_130659:cmsbot_crab_voGroup
240619_130700:cmsbot_crab_scheddName
240619_130701:cmsbot_crab_collector
240619_130702:cmsbot_crab_extraJDL
```

Finished at: 2024-06-19 15:07:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/811/console)

## Comment (cmsdmwmbot, 2024-06-19T13:32:05Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-19 15:32:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1133/console

```
RETRY TESTS:
transferLogs-check.sh 240619_130631:cmsbot_crab_transferLogs - 2
lumiMaskUrl-check.sh 240619_130651:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240619_130653:cmsbot_crab_runRange - 2
whitelist-check.sh 240619_130656:cmsbot_crab_whitelist - 2
blacklist-check.sh 240619_130657:cmsbot_crab_blacklist - 2
voGroup-check.sh 240619_130659:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_130630:cmsbot_crab_transferOutputs - 0
activity-check.sh 240619_130631:cmsbot_crab_activity - 0
inputFiles-check.sh 240619_130633:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_130634:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_130636:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_130637:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_130638:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_130639:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_130641:cmsbot_crab_numCores - 0
scriptExe-check.sh 240619_130642:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240619_130643:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_130645:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_130647:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_130648:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_130648:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240619_130649:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_130650:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240619_130653:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240619_130654:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_130655:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240619_130658:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240619_130659:cmsbot_crab_voRole - 0
scheddName-check.sh 240619_130700:cmsbot_crab_scheddName - 0
collector-check.sh 240619_130701:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_130702:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-19T13:56:12Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-19 15:56:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1136/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240619_130630:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240619_130631:cmsbot_crab_transferLogs - 0
activity-check.sh 240619_130631:cmsbot_crab_activity - 0
inputFiles-check.sh 240619_130633:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240619_130634:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240619_130636:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240619_130637:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240619_130638:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240619_130639:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240619_130641:cmsbot_crab_numCores - 0
scriptExe-check.sh 240619_130642:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240619_130643:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240619_130645:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240619_130647:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240619_130648:cmsbot_crab_inputDBS - 0
useParent-check.sh 240619_130648:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240619_130649:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240619_130650:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240619_130651:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240619_130653:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240619_130653:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240619_130654:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240619_130655:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240619_130656:cmsbot_crab_whitelist - 0
blacklist-check.sh 240619_130657:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240619_130658:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240619_130659:cmsbot_crab_voRole - 0
voGroup-check.sh 240619_130659:cmsbot_crab_voGroup - 0
scheddName-check.sh 240619_130700:cmsbot_crab_scheddName - 0
collector-check.sh 240619_130701:cmsbot_crab_collector - 0
extraJDL-check.sh 240619_130702:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-06-19T14:22:41Z)

OK
