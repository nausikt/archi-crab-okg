# dmwm/CRABServer issue #8782: #878: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-11T14:40:58Z
Closed: 2024-11-11T16:55:05Z
URL: https://github.com/dmwm/CRABServer/issues/8782

## Opening post (cmsdmwmbot, 2024-11-11T14:40:58Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-11-11 15:40:57
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/878/)

## Comment (cmsdmwmbot, 2024-11-11T14:43:38Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241111_144121:cmsbot_crab_transferOutputs
241111_144125:cmsbot_crab_transferLogs
241111_144136:cmsbot_crab_activity
241111_144139:cmsbot_crab_inputFiles
241111_144143:cmsbot_crab_disableAutomaticOutputCollection
241111_144146:cmsbot_crab_outputFiles
241111_144150:cmsbot_crab_allowUndistributedCMSSW
241111_144154:cmsbot_crab_maxMemoryMB
241111_144157:cmsbot_crab_maxJobRuntimeMin
241111_144201:cmsbot_crab_numCores
241111_144205:cmsbot_crab_scriptExe
241111_144208:cmsbot_crab_scriptArgs
241111_144212:cmsbot_crab_sendVenvFolder
241111_144216:cmsbot_crab_sendExternalFolder
241111_144219:cmsbot_crab_inputDBS
241111_144223:cmsbot_crab_useParent
241111_144227:cmsbot_crab_secondaryInputDataset
241111_144230:cmsbot_crab_lumiMaskFile
241111_144234:cmsbot_crab_lumiMaskUrl
241111_144238:cmsbot_crab_outLFNDirBase
241111_144242:cmsbot_crab_runRange
241111_144245:cmsbot_crab_ignoreLocality
241111_144249:cmsbot_crab_userInputFiles
241111_144252:cmsbot_crab_whitelist
241111_144256:cmsbot_crab_blacklist
241111_144259:cmsbot_crab_ignoreGlobalBlacklist
241111_144303:cmsbot_crab_voRole
241111_144306:cmsbot_crab_voGroup
241111_144310:cmsbot_crab_scheddName
241111_144313:cmsbot_crab_collector
241111_144317:cmsbot_crab_extraJDL
```

Finished at: 2024-11-11 15:43:17
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/878/console)

## Comment (cmsdmwmbot, 2024-11-11T15:07:29Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-11 16:07:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1232/console

```
RETRY TESTS:
scriptArgs-check.sh 241111_144208:cmsbot_crab_scriptArgs - 2
secondaryInputDataset-check.sh 241111_144227:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 241111_144234:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241111_144238:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241111_144242:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241111_144249:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241111_144252:cmsbot_crab_whitelist - 2
blacklist-check.sh 241111_144256:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241111_144121:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241111_144125:cmsbot_crab_transferLogs - 0
activity-check.sh 241111_144136:cmsbot_crab_activity - 0
inputFiles-check.sh 241111_144139:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241111_144143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241111_144146:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241111_144150:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241111_144154:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241111_144157:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241111_144201:cmsbot_crab_numCores - 0
scriptExe-check.sh 241111_144205:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 241111_144212:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241111_144216:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241111_144219:cmsbot_crab_inputDBS - 0
useParent-check.sh 241111_144223:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 241111_144230:cmsbot_crab_lumiMaskFile - 0

FAILED TESTS:
ignoreLocality-check.sh 241111_144245:cmsbot_crab_ignoreLocality - 1
ignoreGlobalBlacklist-check.sh 241111_144259:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 241111_144303:cmsbot_crab_voRole - 1
voGroup-check.sh 241111_144306:cmsbot_crab_voGroup - 1
scheddName-check.sh 241111_144310:cmsbot_crab_scheddName - 1
collector-check.sh 241111_144313:cmsbot_crab_collector - 1
extraJDL-check.sh 241111_144317:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-11-11T15:31:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-11 16:31:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1233/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 241111_144234:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 241111_144242:cmsbot_crab_runRange - 2
whitelist-check.sh 241111_144252:cmsbot_crab_whitelist - 2
blacklist-check.sh 241111_144256:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241111_144121:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241111_144125:cmsbot_crab_transferLogs - 0
activity-check.sh 241111_144136:cmsbot_crab_activity - 0
inputFiles-check.sh 241111_144139:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241111_144143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241111_144146:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241111_144150:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241111_144154:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241111_144157:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241111_144201:cmsbot_crab_numCores - 0
scriptExe-check.sh 241111_144205:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241111_144208:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241111_144212:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241111_144216:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241111_144219:cmsbot_crab_inputDBS - 0
useParent-check.sh 241111_144223:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241111_144227:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241111_144230:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 241111_144238:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 241111_144245:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241111_144249:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 241111_144259:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241111_144303:cmsbot_crab_voRole - 0
voGroup-check.sh 241111_144306:cmsbot_crab_voGroup - 0
scheddName-check.sh 241111_144310:cmsbot_crab_scheddName - 0
collector-check.sh 241111_144313:cmsbot_crab_collector - 0
extraJDL-check.sh 241111_144317:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-11T15:55:39Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-11-11 16:55:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1234/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241111_144121:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241111_144125:cmsbot_crab_transferLogs - 0
activity-check.sh 241111_144136:cmsbot_crab_activity - 0
inputFiles-check.sh 241111_144139:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241111_144143:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241111_144146:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241111_144150:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241111_144154:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241111_144157:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241111_144201:cmsbot_crab_numCores - 0
scriptExe-check.sh 241111_144205:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241111_144208:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241111_144212:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241111_144216:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241111_144219:cmsbot_crab_inputDBS - 0
useParent-check.sh 241111_144223:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241111_144227:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241111_144230:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241111_144234:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241111_144238:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241111_144242:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241111_144245:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241111_144249:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241111_144252:cmsbot_crab_whitelist - 0
blacklist-check.sh 241111_144256:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241111_144259:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241111_144303:cmsbot_crab_voRole - 0
voGroup-check.sh 241111_144306:cmsbot_crab_voGroup - 0
scheddName-check.sh 241111_144310:cmsbot_crab_scheddName - 0
collector-check.sh 241111_144313:cmsbot_crab_collector - 0
extraJDL-check.sh 241111_144317:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-11T16:55:05Z)

OK
