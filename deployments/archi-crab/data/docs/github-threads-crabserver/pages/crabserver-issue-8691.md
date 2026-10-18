# dmwm/CRABServer issue #8691: #832: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-04T19:09:14Z
Closed: 2024-10-10T22:43:01Z
URL: https://github.com/dmwm/CRABServer/issues/8691

## Opening post (cmsdmwmbot, 2024-09-04T19:09:14Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-04 21:09:14
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/832/)

## Comment (cmsdmwmbot, 2024-09-04T19:11:15Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240904_190936:cmsbot_crab_transferOutputs
240904_190939:cmsbot_crab_transferLogs
240904_190941:cmsbot_crab_activity
240904_190944:cmsbot_crab_inputFiles
240904_190947:cmsbot_crab_disableAutomaticOutputCollection
240904_190949:cmsbot_crab_outputFiles
240904_190952:cmsbot_crab_allowUndistributedCMSSW
240904_190954:cmsbot_crab_maxMemoryMB
240904_190957:cmsbot_crab_maxJobRuntimeMin
240904_190959:cmsbot_crab_numCores
240904_191002:cmsbot_crab_scriptExe
240904_191004:cmsbot_crab_scriptArgs
240904_191007:cmsbot_crab_sendVenvFolder
240904_191010:cmsbot_crab_sendExternalFolder
240904_191012:cmsbot_crab_inputDBS
240904_191015:cmsbot_crab_useParent
240904_191017:cmsbot_crab_secondaryInputDataset
240904_191020:cmsbot_crab_lumiMaskFile
240904_191023:cmsbot_crab_lumiMaskUrl
240904_191026:cmsbot_crab_outLFNDirBase
240904_191029:cmsbot_crab_runRange
240904_191031:cmsbot_crab_ignoreLocality
240904_191034:cmsbot_crab_userInputFiles
240904_191036:cmsbot_crab_whitelist
240904_191039:cmsbot_crab_blacklist
240904_191041:cmsbot_crab_ignoreGlobalBlacklist
240904_191044:cmsbot_crab_voRole
240904_191046:cmsbot_crab_voGroup
240904_191048:cmsbot_crab_scheddName
240904_191051:cmsbot_crab_collector
240904_191053:cmsbot_crab_extraJDL
```

Finished at: 2024-09-04 21:10:54
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/832/console)

## Comment (cmsdmwmbot, 2024-09-04T19:37:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-04 21:37:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1169/console

```
RETRY TESTS:
transferLogs-check.sh 240904_190939:cmsbot_crab_transferLogs - 2
activity-check.sh 240904_190941:cmsbot_crab_activity - 2
numCores-check.sh 240904_190959:cmsbot_crab_numCores - 2
scriptArgs-check.sh 240904_191004:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240904_191015:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 240904_191023:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240904_191029:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240904_191034:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240904_191036:cmsbot_crab_whitelist - 2
blacklist-check.sh 240904_191039:cmsbot_crab_blacklist - 2
voGroup-check.sh 240904_191046:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240904_190936:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240904_190944:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240904_190947:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240904_190949:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240904_190952:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240904_190954:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240904_190957:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240904_191002:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240904_191007:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240904_191010:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240904_191012:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240904_191017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240904_191020:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240904_191026:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240904_191031:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240904_191041:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240904_191044:cmsbot_crab_voRole - 0
scheddName-check.sh 240904_191048:cmsbot_crab_scheddName - 0
collector-check.sh 240904_191051:cmsbot_crab_collector - 0
extraJDL-check.sh 240904_191053:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-09-04T20:03:25Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-09-04 22:03:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1170/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240904_190936:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240904_190939:cmsbot_crab_transferLogs - 0
activity-check.sh 240904_190941:cmsbot_crab_activity - 0
inputFiles-check.sh 240904_190944:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240904_190947:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240904_190949:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240904_190952:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240904_190954:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240904_190957:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240904_190959:cmsbot_crab_numCores - 0
scriptExe-check.sh 240904_191002:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240904_191004:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240904_191007:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240904_191010:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240904_191012:cmsbot_crab_inputDBS - 0
useParent-check.sh 240904_191015:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240904_191017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240904_191020:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240904_191023:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240904_191026:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240904_191029:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240904_191031:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240904_191034:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240904_191036:cmsbot_crab_whitelist - 0
blacklist-check.sh 240904_191039:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240904_191041:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240904_191044:cmsbot_crab_voRole - 0
voGroup-check.sh 240904_191046:cmsbot_crab_voGroup - 0
scheddName-check.sh 240904_191048:cmsbot_crab_scheddName - 0
collector-check.sh 240904_191051:cmsbot_crab_collector - 0
extraJDL-check.sh 240904_191053:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
