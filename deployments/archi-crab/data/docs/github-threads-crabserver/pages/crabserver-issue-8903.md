# dmwm/CRABServer issue #8903: #932: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-01-29T21:40:22Z
Closed: 2025-01-29T23:40:40Z
URL: https://github.com/dmwm/CRABServer/issues/8903

## Opening post (cmsdmwmbot, 2025-01-29T21:40:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-01-29 22:40:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/932/)

## Comment (cmsdmwmbot, 2025-01-29T21:42:29Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250129_214037:cmsbot_crab_20250129_224035
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250129_214040:cmsbot_crab_transferOutputs
250129_214043:cmsbot_crab_transferLogs
250129_214046:cmsbot_crab_activity
250129_214049:cmsbot_crab_inputFiles
250129_214052:cmsbot_crab_disableAutomaticOutputCollection
250129_214055:cmsbot_crab_outputFiles
250129_214058:cmsbot_crab_allowUndistributedCMSSW
250129_214101:cmsbot_crab_maxMemoryMB
250129_214104:cmsbot_crab_maxJobRuntimeMin
250129_214107:cmsbot_crab_numCores
250129_214110:cmsbot_crab_scriptExe
250129_214113:cmsbot_crab_scriptArgs
250129_214116:cmsbot_crab_sendVenvFolder
250129_214119:cmsbot_crab_sendExternalFolder
250129_214122:cmsbot_crab_inputDBS
250129_214125:cmsbot_crab_useParent
250129_214128:cmsbot_crab_secondaryInputDataset
250129_214131:cmsbot_crab_lumiMaskFile
250129_214134:cmsbot_crab_lumiMaskUrl
250129_214137:cmsbot_crab_outLFNDirBase
250129_214140:cmsbot_crab_runRange
250129_214143:cmsbot_crab_ignoreLocality
250129_214146:cmsbot_crab_userInputFiles
250129_214149:cmsbot_crab_whitelist
250129_214152:cmsbot_crab_blacklist
250129_214155:cmsbot_crab_ignoreGlobalBlacklist
250129_214158:cmsbot_crab_voRole
250129_214201:cmsbot_crab_scheddName
250129_214204:cmsbot_crab_collector
250129_214207:cmsbot_crab_extraJDL
```

Finished at: 2025-01-29 22:42:07
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/932/console)

## Comment (cmsdmwmbot, 2025-01-29T22:05:49Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-01-29 23:05:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/599/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/599//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-01-29T22:06:45Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2025-01-29 23:06:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1272/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_214040:cmsbot_crab_transferOutputs - 0
activity-check.sh 250129_214046:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_214049:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_214052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_214055:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_214058:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250129_214101:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 250129_214116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_214119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_214122:cmsbot_crab_inputDBS - 0
outLFNDirBase-check.sh 250129_214137:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 250129_214143:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 250129_214201:cmsbot_crab_scheddName - 0
collector-check.sh 250129_214204:cmsbot_crab_collector - 0

FAILED TESTS:
 none

RETRY TESTS:
transferLogs-check.sh 250129_214043:cmsbot_crab_transferLogs - 2
maxJobRuntimeMin-check.sh 250129_214104:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 250129_214107:cmsbot_crab_numCores - 2
scriptExe-check.sh 250129_214110:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 250129_214113:cmsbot_crab_scriptArgs - 2
useParent-check.sh 250129_214125:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 250129_214128:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 250129_214131:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 250129_214134:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 250129_214140:cmsbot_crab_runRange - 2
userInputFiles-check.sh 250129_214146:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 250129_214149:cmsbot_crab_whitelist - 2
blacklist-check.sh 250129_214152:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 250129_214155:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 250129_214158:cmsbot_crab_voRole - 2
extraJDL-check.sh 250129_214207:cmsbot_crab_extraJDL - 2
```

## Comment (cmsdmwmbot, 2025-01-29T22:31:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2025-01-29 23:31:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1274/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_214040:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250129_214043:cmsbot_crab_transferLogs - 0
activity-check.sh 250129_214046:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_214049:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_214052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_214055:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_214058:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250129_214101:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250129_214104:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250129_214107:cmsbot_crab_numCores - 0
scriptExe-check.sh 250129_214110:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250129_214113:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250129_214116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_214119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_214122:cmsbot_crab_inputDBS - 0
useParent-check.sh 250129_214125:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250129_214128:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 250129_214137:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 250129_214143:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250129_214146:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 250129_214152:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250129_214155:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250129_214158:cmsbot_crab_voRole - 0
scheddName-check.sh 250129_214201:cmsbot_crab_scheddName - 0
collector-check.sh 250129_214204:cmsbot_crab_collector - 0
extraJDL-check.sh 250129_214207:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
lumiMaskFile-check.sh 250129_214131:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 250129_214134:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 250129_214140:cmsbot_crab_runRange - 2
whitelist-check.sh 250129_214149:cmsbot_crab_whitelist - 2
```

## Comment (cmsdmwmbot, 2025-01-29T22:55:34Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2025-01-29 23:55:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1276/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250129_214040:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250129_214043:cmsbot_crab_transferLogs - 0
activity-check.sh 250129_214046:cmsbot_crab_activity - 0
inputFiles-check.sh 250129_214049:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250129_214052:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250129_214055:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250129_214058:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250129_214101:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250129_214104:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250129_214107:cmsbot_crab_numCores - 0
scriptExe-check.sh 250129_214110:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 250129_214113:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 250129_214116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250129_214119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250129_214122:cmsbot_crab_inputDBS - 0
useParent-check.sh 250129_214125:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250129_214128:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250129_214131:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250129_214134:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250129_214137:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250129_214140:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250129_214143:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250129_214146:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250129_214149:cmsbot_crab_whitelist - 0
blacklist-check.sh 250129_214152:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250129_214155:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250129_214158:cmsbot_crab_voRole - 0
scheddName-check.sh 250129_214201:cmsbot_crab_scheddName - 0
collector-check.sh 250129_214204:cmsbot_crab_collector - 0
extraJDL-check.sh 250129_214207:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none

RETRY TESTS:
 none
```

## Comment (belforte, 2025-01-29T23:40:40Z)

all OK
