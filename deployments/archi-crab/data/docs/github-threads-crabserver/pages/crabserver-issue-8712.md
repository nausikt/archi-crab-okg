# dmwm/CRABServer issue #8712: #837: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-09-20T17:40:41Z
Closed: 2024-09-23T21:04:25Z
URL: https://github.com/dmwm/CRABServer/issues/8712

## Opening post (cmsdmwmbot, 2024-09-20T17:40:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-09-20 19:40:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/837/)

## Comment (cmsdmwmbot, 2024-09-20T17:42:36Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240920_174100:cmsbot_crab_transferOutputs
240920_174103:cmsbot_crab_transferLogs
240920_174106:cmsbot_crab_activity
240920_174108:cmsbot_crab_inputFiles
240920_174110:cmsbot_crab_disableAutomaticOutputCollection
240920_174113:cmsbot_crab_outputFiles
240920_174116:cmsbot_crab_allowUndistributedCMSSW
240920_174118:cmsbot_crab_maxMemoryMB
240920_174120:cmsbot_crab_maxJobRuntimeMin
240920_174122:cmsbot_crab_numCores
240920_174125:cmsbot_crab_scriptExe
240920_174127:cmsbot_crab_scriptArgs
240920_174130:cmsbot_crab_sendVenvFolder
240920_174132:cmsbot_crab_sendExternalFolder
240920_174135:cmsbot_crab_inputDBS
240920_174137:cmsbot_crab_useParent
240920_174139:cmsbot_crab_secondaryInputDataset
240920_174142:cmsbot_crab_lumiMaskFile
240920_174144:cmsbot_crab_lumiMaskUrl
240920_174147:cmsbot_crab_outLFNDirBase
240920_174150:cmsbot_crab_runRange
240920_174152:cmsbot_crab_ignoreLocality
240920_174155:cmsbot_crab_userInputFiles
240920_174157:cmsbot_crab_whitelist
240920_174200:cmsbot_crab_blacklist
240920_174202:cmsbot_crab_ignoreGlobalBlacklist
240920_174205:cmsbot_crab_voRole
240920_174207:cmsbot_crab_voGroup
240920_174210:cmsbot_crab_scheddName
240920_174212:cmsbot_crab_collector
240920_174214:cmsbot_crab_extraJDL
```

Finished at: 2024-09-20 19:42:15
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/837/console)

## Comment (cmsdmwmbot, 2024-09-20T18:05:47Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-09-20 20:05:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1185/console

```
RETRY TESTS:
transferOutputs-check.sh 240920_174100:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240920_174103:cmsbot_crab_transferLogs - 2
activity-check.sh 240920_174106:cmsbot_crab_activity - 2
outputFiles-check.sh 240920_174113:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240920_174118:cmsbot_crab_maxMemoryMB - 2
lumiMaskUrl-check.sh 240920_174144:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_174150:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240920_174155:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240920_174157:cmsbot_crab_whitelist - 2
voRole-check.sh 240920_174205:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
sendVenvFolder-check.sh 240920_174130:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174132:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 240920_174137:cmsbot_crab_useParent - 0
collector-check.sh 240920_174212:cmsbot_crab_collector - 0

FAILED TESTS:
inputFiles-check.sh 240920_174108:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174110:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_174116:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240920_174120:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174122:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_174125:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240920_174127:cmsbot_crab_scriptArgs - 1
inputDBS-check.sh 240920_174135:cmsbot_crab_inputDBS - 1
secondaryInputDataset-check.sh 240920_174139:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174142:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_174147:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240920_174152:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240920_174200:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_174202:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_174207:cmsbot_crab_voGroup - 1
scheddName-check.sh 240920_174210:cmsbot_crab_scheddName - 1
extraJDL-check.sh 240920_174214:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-09-20T18:29:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-09-20 20:29:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1188/console

```
RETRY TESTS:
transferOutputs-check.sh 240920_174100:cmsbot_crab_transferOutputs - 2
activity-check.sh 240920_174106:cmsbot_crab_activity - 2
lumiMaskUrl-check.sh 240920_174144:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_174150:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240920_174103:cmsbot_crab_transferLogs - 0
outputFiles-check.sh 240920_174113:cmsbot_crab_outputFiles - 0
maxMemoryMB-check.sh 240920_174118:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240920_174130:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174132:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 240920_174137:cmsbot_crab_useParent - 0
userInputFiles-check.sh 240920_174155:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_174157:cmsbot_crab_whitelist - 0
voRole-check.sh 240920_174205:cmsbot_crab_voRole - 0
collector-check.sh 240920_174212:cmsbot_crab_collector - 0

FAILED TESTS:
inputFiles-check.sh 240920_174108:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174110:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_174116:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240920_174120:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174122:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_174125:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240920_174127:cmsbot_crab_scriptArgs - 1
inputDBS-check.sh 240920_174135:cmsbot_crab_inputDBS - 1
secondaryInputDataset-check.sh 240920_174139:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174142:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_174147:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240920_174152:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240920_174200:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_174202:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_174207:cmsbot_crab_voGroup - 1
scheddName-check.sh 240920_174210:cmsbot_crab_scheddName - 1
extraJDL-check.sh 240920_174214:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-09-20T18:53:15Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-09-20 20:53:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1190/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240920_174144:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240920_174150:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_174100:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_174103:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_174106:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_174113:cmsbot_crab_outputFiles - 0
maxMemoryMB-check.sh 240920_174118:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240920_174130:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174132:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 240920_174137:cmsbot_crab_useParent - 0
userInputFiles-check.sh 240920_174155:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_174157:cmsbot_crab_whitelist - 0
voRole-check.sh 240920_174205:cmsbot_crab_voRole - 0
collector-check.sh 240920_174212:cmsbot_crab_collector - 0

FAILED TESTS:
inputFiles-check.sh 240920_174108:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174110:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_174116:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240920_174120:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174122:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_174125:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240920_174127:cmsbot_crab_scriptArgs - 1
inputDBS-check.sh 240920_174135:cmsbot_crab_inputDBS - 1
secondaryInputDataset-check.sh 240920_174139:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174142:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_174147:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240920_174152:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240920_174200:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_174202:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_174207:cmsbot_crab_voGroup - 1
scheddName-check.sh 240920_174210:cmsbot_crab_scheddName - 1
extraJDL-check.sh 240920_174214:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-09-20T19:17:05Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2024-09-20 21:17:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1192/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240920_174144:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_174100:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_174103:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_174106:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_174113:cmsbot_crab_outputFiles - 0
maxMemoryMB-check.sh 240920_174118:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240920_174130:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174132:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 240920_174137:cmsbot_crab_useParent - 0
runRange-check.sh 240920_174150:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240920_174155:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_174157:cmsbot_crab_whitelist - 0
voRole-check.sh 240920_174205:cmsbot_crab_voRole - 0
collector-check.sh 240920_174212:cmsbot_crab_collector - 0

FAILED TESTS:
inputFiles-check.sh 240920_174108:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174110:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_174116:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240920_174120:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174122:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_174125:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240920_174127:cmsbot_crab_scriptArgs - 1
inputDBS-check.sh 240920_174135:cmsbot_crab_inputDBS - 1
secondaryInputDataset-check.sh 240920_174139:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174142:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_174147:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240920_174152:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240920_174200:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_174202:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_174207:cmsbot_crab_voGroup - 1
scheddName-check.sh 240920_174210:cmsbot_crab_scheddName - 1
extraJDL-check.sh 240920_174214:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-09-20T19:40:45Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 4 out of 4. Test failed. Investigate manually
**Finished at:** 2024-09-20 21:40:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1194/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240920_174100:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240920_174103:cmsbot_crab_transferLogs - 0
activity-check.sh 240920_174106:cmsbot_crab_activity - 0
outputFiles-check.sh 240920_174113:cmsbot_crab_outputFiles - 0
maxMemoryMB-check.sh 240920_174118:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240920_174130:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240920_174132:cmsbot_crab_sendExternalFolder - 0
useParent-check.sh 240920_174137:cmsbot_crab_useParent - 0
lumiMaskUrl-check.sh 240920_174144:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240920_174150:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240920_174155:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240920_174157:cmsbot_crab_whitelist - 0
voRole-check.sh 240920_174205:cmsbot_crab_voRole - 0
collector-check.sh 240920_174212:cmsbot_crab_collector - 0

FAILED TESTS:
inputFiles-check.sh 240920_174108:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240920_174110:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240920_174116:cmsbot_crab_allowUndistributedCMSSW - 1
maxJobRuntimeMin-check.sh 240920_174120:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240920_174122:cmsbot_crab_numCores - 1
scriptExe-check.sh 240920_174125:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240920_174127:cmsbot_crab_scriptArgs - 1
inputDBS-check.sh 240920_174135:cmsbot_crab_inputDBS - 1
secondaryInputDataset-check.sh 240920_174139:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240920_174142:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240920_174147:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240920_174152:cmsbot_crab_ignoreLocality - 1
blacklist-check.sh 240920_174200:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240920_174202:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240920_174207:cmsbot_crab_voGroup - 1
scheddName-check.sh 240920_174210:cmsbot_crab_scheddName - 1
extraJDL-check.sh 240920_174214:cmsbot_crab_extraJDL - 1
```
