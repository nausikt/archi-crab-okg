# dmwm/CRABServer issue #8343: #757: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-18T12:00:06Z
Closed: 2024-04-18T13:05:24Z
URL: https://github.com/dmwm/CRABServer/issues/8343

## Opening post (cmsdmwmbot, 2024-04-18T12:00:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-18 14:00:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/757/)

## Comment (cmsdmwmbot, 2024-04-18T12:02:20Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240418_120035:cmsbot_crab_transferOutputs
240418_120047:cmsbot_crab_transferLogs
240418_120050:cmsbot_crab_activity
240418_120052:cmsbot_crab_inputFiles
240418_120054:cmsbot_crab_disableAutomaticOutputCollection
240418_120057:cmsbot_crab_outputFiles
240418_120059:cmsbot_crab_allowUndistributedCMSSW
240418_120101:cmsbot_crab_maxMemoryMB
240418_120104:cmsbot_crab_maxJobRuntimeMin
240418_120106:cmsbot_crab_numCores
240418_120108:cmsbot_crab_scriptExe
240418_120111:cmsbot_crab_scriptArgs
240418_120113:cmsbot_crab_sendVenvFolder
240418_120116:cmsbot_crab_sendExternalFolder
240418_120118:cmsbot_crab_inputDBS
240418_120121:cmsbot_crab_useParent
240418_120123:cmsbot_crab_secondaryInputDataset
240418_120125:cmsbot_crab_lumiMaskFile
240418_120128:cmsbot_crab_lumiMaskUrl
240418_120131:cmsbot_crab_outLFNDirBase
240418_120133:cmsbot_crab_runRange
240418_120136:cmsbot_crab_ignoreLocality
240418_120138:cmsbot_crab_userInputFiles
240418_120141:cmsbot_crab_whitelist
240418_120143:cmsbot_crab_blacklist
240418_120146:cmsbot_crab_ignoreGlobalBlacklist
240418_120148:cmsbot_crab_voRole
240418_120151:cmsbot_crab_voGroup
240418_120153:cmsbot_crab_scheddName
240418_120156:cmsbot_crab_collector
240418_120158:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240418_120032:cmsbot_crab_20240418_140030
```

Finished at: 2024-04-18 14:01:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/757/console)

## Comment (cmsdmwmbot, 2024-04-18T12:26:52Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-18 14:26:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/531/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/531//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-18T12:28:14Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-18 14:28:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1035/console

```
RETRY TESTS:
activity-check.sh 240418_120050:cmsbot_crab_activity - 2
scriptExe-check.sh 240418_120108:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240418_120111:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 240418_120125:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240418_120128:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240418_120131:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240418_120133:cmsbot_crab_runRange - 2
whitelist-check.sh 240418_120141:cmsbot_crab_whitelist - 2
blacklist-check.sh 240418_120143:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240418_120035:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240418_120047:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240418_120052:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240418_120054:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240418_120059:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240418_120101:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240418_120104:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240418_120106:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240418_120113:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240418_120116:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240418_120118:cmsbot_crab_inputDBS - 0
useParent-check.sh 240418_120121:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240418_120123:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240418_120136:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240418_120138:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240418_120146:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240418_120148:cmsbot_crab_voRole - 0
voGroup-check.sh 240418_120151:cmsbot_crab_voGroup - 0
scheddName-check.sh 240418_120153:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240418_120158:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240418_120057:cmsbot_crab_outputFiles - 1
collector-check.sh 240418_120156:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-04-18T12:53:46Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-18 14:53:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1036/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240418_120035:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240418_120047:cmsbot_crab_transferLogs - 0
activity-check.sh 240418_120050:cmsbot_crab_activity - 0
inputFiles-check.sh 240418_120052:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240418_120054:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240418_120059:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240418_120101:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240418_120104:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240418_120106:cmsbot_crab_numCores - 0
scriptExe-check.sh 240418_120108:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240418_120111:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240418_120113:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240418_120116:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240418_120118:cmsbot_crab_inputDBS - 0
useParent-check.sh 240418_120121:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240418_120123:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240418_120125:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240418_120128:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240418_120131:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240418_120133:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240418_120136:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240418_120138:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240418_120141:cmsbot_crab_whitelist - 0
blacklist-check.sh 240418_120143:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240418_120146:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240418_120148:cmsbot_crab_voRole - 0
voGroup-check.sh 240418_120151:cmsbot_crab_voGroup - 0
scheddName-check.sh 240418_120153:cmsbot_crab_scheddName - 0
extraJDL-check.sh 240418_120158:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240418_120057:cmsbot_crab_outputFiles - 1
collector-check.sh 240418_120156:cmsbot_crab_collector - 1
```

## Comment (belforte, 2024-04-18T13:05:24Z)

failures appear some transient thing. Test was OK
