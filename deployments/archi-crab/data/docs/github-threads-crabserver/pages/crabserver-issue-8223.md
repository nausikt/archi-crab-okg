# dmwm/CRABServer issue #8223: #704: Test prod CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release

State: closed
Opened: 2024-02-02T11:48:29Z
Closed: 2024-02-02T14:48:08Z
URL: https://github.com/dmwm/CRABServer/issues/8223

## Opening post (cmsdmwmbot, 2024-02-02T11:48:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_6_7**
- SCRAM_ARCH: **slc6_amd64_gcc493**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-02 12:48:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/704/)

## Comment (cmsdmwmbot, 2024-02-02T11:50:19Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_114846:cmsbot_crab_transferOutputs
240202_114848:cmsbot_crab_transferLogs
240202_114850:cmsbot_crab_activity
240202_114854:cmsbot_crab_inputFiles
240202_114856:cmsbot_crab_disableAutomaticOutputCollection
240202_114859:cmsbot_crab_outputFiles
240202_114901:cmsbot_crab_allowUndistributedCMSSW
240202_114904:cmsbot_crab_maxMemoryMB
240202_114906:cmsbot_crab_maxJobRuntimeMin
240202_114910:cmsbot_crab_numCores
240202_114912:cmsbot_crab_scriptExe
240202_114914:cmsbot_crab_scriptArgs
240202_114917:cmsbot_crab_sendVenvFolder
240202_114924:cmsbot_crab_sendExternalFolder
240202_114925:cmsbot_crab_inputDBS
240202_114928:cmsbot_crab_useParent
240202_114930:cmsbot_crab_secondaryInputDataset
240202_114932:cmsbot_crab_lumiMaskFile
240202_114935:cmsbot_crab_outLFNDirBase
240202_114936:cmsbot_crab_runRange
240202_114938:cmsbot_crab_ignoreLocality
240202_114939:cmsbot_crab_userInputFiles
240202_114941:cmsbot_crab_whitelist
240202_114944:cmsbot_crab_blacklist
240202_114946:cmsbot_crab_ignoreGlobalBlacklist
240202_114948:cmsbot_crab_voRole
240202_114950:cmsbot_crab_voGroup
240202_114953:cmsbot_crab_scheddName
240202_114955:cmsbot_crab_collector
240202_114957:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 12:49:58
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/704/console)

## Comment (cmsdmwmbot, 2024-02-02T12:12:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:12:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/931/console

```
RETRY TESTS:
transferLogs-check.sh 240202_114848:cmsbot_crab_transferLogs - 2
activity-check.sh 240202_114850:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 240202_114904:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240202_114906:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240202_114910:cmsbot_crab_numCores - 2
scriptExe-check.sh 240202_114912:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_114914:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240202_114928:cmsbot_crab_useParent - 2
blacklist-check.sh 240202_114944:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_114946:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_114948:cmsbot_crab_voRole - 2
voGroup-check.sh 240202_114950:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240202_114957:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114846:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240202_114854:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114856:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114859:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114901:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240202_114917:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114925:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240202_114930:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114932:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_114935:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114936:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114938:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114939:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114941:cmsbot_crab_whitelist - 0
scheddName-check.sh 240202_114953:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114955:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:37:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-02-02 13:37:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/936/console

```
RETRY TESTS:
activity-check.sh 240202_114850:cmsbot_crab_activity - 2
scriptExe-check.sh 240202_114912:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240202_114914:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 240202_114944:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240202_114946:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240202_114948:cmsbot_crab_voRole - 2
voGroup-check.sh 240202_114950:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114846:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114848:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240202_114854:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114856:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114859:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114901:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114904:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114906:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114910:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240202_114917:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114925:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114928:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114930:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114932:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_114935:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114936:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114938:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114939:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114941:cmsbot_crab_whitelist - 0
scheddName-check.sh 240202_114953:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114955:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114957:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:59:05Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-02-02 13:59:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/938/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114846:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114848:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114850:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114854:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114856:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114859:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114901:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114904:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114906:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114910:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114912:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114914:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114917:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114924:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114925:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114928:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114930:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114932:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240202_114935:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114936:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114938:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114939:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114941:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_114944:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_114946:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114948:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114950:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114953:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114955:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114957:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-02-02T14:48:08Z)

OK
