# dmwm/CRABServer issue #7711: #420: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-30T23:11:16Z
Closed: 2023-07-01T12:13:32Z
URL: https://github.com/dmwm/CRABServer/issues/7711

## Opening post (cmsdmwmbot, 2023-06-30T23:11:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2023-07-01 01:11:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/420/)

## Comment (cmsdmwmbot, 2023-06-30T23:13:17Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_231138:cmsbot_crab_transferOutputs
230630_231139:cmsbot_crab_transferLogs
230630_231140:cmsbot_crab_activity
230630_231142:cmsbot_crab_inputFiles
230630_231143:cmsbot_crab_disableAutomaticOutputCollection
230630_231144:cmsbot_crab_outputFiles
230630_231146:cmsbot_crab_allowUndistributedCMSSW
230630_231147:cmsbot_crab_maxMemoryMB
230630_231149:cmsbot_crab_maxJobRuntimeMin
230630_231150:cmsbot_crab_numCores
230630_231151:cmsbot_crab_scriptExe
230630_231153:cmsbot_crab_scriptArgs
230630_231154:cmsbot_crab_sendPythonFolder
230630_231232:cmsbot_crab_sendExternalFolder
230630_231233:cmsbot_crab_inputDBS
230630_231235:cmsbot_crab_useParent
230630_231237:cmsbot_crab_secondaryInputDataset
230630_231238:cmsbot_crab_lumiMaskFile
230630_231239:cmsbot_crab_lumiMaskUrl
230630_231241:cmsbot_crab_outLFNDirBase
230630_231243:cmsbot_crab_runRange
230630_231244:cmsbot_crab_ignoreLocality
230630_231245:cmsbot_crab_userInputFiles
230630_231246:cmsbot_crab_whitelist
230630_231247:cmsbot_crab_blacklist
230630_231249:cmsbot_crab_ignoreGlobalBlacklist
230630_231250:cmsbot_crab_voRole
230630_231251:cmsbot_crab_voGroup
230630_231252:cmsbot_crab_scheddName
230630_231254:cmsbot_crab_collector
230630_231255:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230630_231136:cmsbot_crab_20230701_011135
```

Finished at: 2023-07-01 01:12:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/420/console)

## Comment (cmsdmwmbot, 2023-06-30T23:34:13Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-07-01 01:34:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/356/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/356//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-06-30T23:34:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-01 01:34:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/670/console

```
RETRY TESTS:
useParent-check.sh 230630_231235:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230630_231237:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 230630_231238:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230630_231239:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230630_231241:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230630_231243:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230630_231244:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 230630_231245:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230630_231246:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_231247:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_231138:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_231139:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_231140:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_231142:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231144:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231146:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231147:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231149:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_231150:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_231151:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_231153:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231154:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231233:cmsbot_crab_inputDBS - 0

FAILED TESTS:
ignoreGlobalBlacklist-check.sh 230630_231249:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230630_231250:cmsbot_crab_voRole - 1
voGroup-check.sh 230630_231251:cmsbot_crab_voGroup - 1
scheddName-check.sh 230630_231252:cmsbot_crab_scheddName - 1
collector-check.sh 230630_231254:cmsbot_crab_collector - 1
extraJDL-check.sh 230630_231255:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2023-06-30T23:56:39Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-01 01:56:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/672/console

```
RETRY TESTS:
useParent-check.sh 230630_231235:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230630_231237:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230630_231239:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230630_231243:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230630_231245:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230630_231246:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_231247:cmsbot_crab_blacklist - 2
voRole-check.sh 230630_231250:cmsbot_crab_voRole - 2
voGroup-check.sh 230630_231251:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_231138:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_231139:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_231140:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_231142:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231144:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231146:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231147:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231149:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_231150:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_231151:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_231153:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231154:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231233:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 230630_231238:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230630_231241:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230630_231244:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230630_231249:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 230630_231252:cmsbot_crab_scheddName - 0
collector-check.sh 230630_231254:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_231255:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-07-01T00:19:10Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-07-01 02:19:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/674/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_231138:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_231139:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_231140:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_231142:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_231143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_231144:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_231146:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_231147:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_231149:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_231150:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_231151:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_231153:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_231154:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_231232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_231233:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_231235:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_231237:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_231238:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_231239:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_231241:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_231243:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_231244:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_231245:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_231246:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_231247:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_231249:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_231250:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_231251:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_231252:cmsbot_crab_scheddName - 0
collector-check.sh 230630_231254:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_231255:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-07-01T12:13:32Z)

all OK
