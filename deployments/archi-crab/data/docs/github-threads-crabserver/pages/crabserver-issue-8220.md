# dmwm/CRABServer issue #8220: #701: Test prod CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-02-02T11:41:07Z
Closed: 2024-02-02T14:46:47Z
URL: https://github.com/dmwm/CRABServer/issues/8220

## Opening post (cmsdmwmbot, 2024-02-02T11:41:07Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-02-02 12:41:06
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/701/)

## Comment (cmsdmwmbot, 2024-02-02T11:42:57Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_114126:cmsbot_crab_transferOutputs
240202_114128:cmsbot_crab_transferLogs
240202_114131:cmsbot_crab_activity
240202_114133:cmsbot_crab_inputFiles
240202_114135:cmsbot_crab_disableAutomaticOutputCollection
240202_114137:cmsbot_crab_outputFiles
240202_114139:cmsbot_crab_allowUndistributedCMSSW
240202_114141:cmsbot_crab_maxMemoryMB
240202_114143:cmsbot_crab_maxJobRuntimeMin
240202_114145:cmsbot_crab_numCores
240202_114147:cmsbot_crab_scriptExe
240202_114150:cmsbot_crab_scriptArgs
240202_114152:cmsbot_crab_sendVenvFolder
240202_114159:cmsbot_crab_sendExternalFolder
240202_114201:cmsbot_crab_inputDBS
240202_114203:cmsbot_crab_useParent
240202_114205:cmsbot_crab_secondaryInputDataset
240202_114207:cmsbot_crab_lumiMaskFile
240202_114209:cmsbot_crab_lumiMaskUrl
240202_114212:cmsbot_crab_outLFNDirBase
240202_114214:cmsbot_crab_runRange
240202_114216:cmsbot_crab_ignoreLocality
240202_114218:cmsbot_crab_userInputFiles
240202_114220:cmsbot_crab_whitelist
240202_114222:cmsbot_crab_blacklist
240202_114225:cmsbot_crab_ignoreGlobalBlacklist
240202_114227:cmsbot_crab_voRole
240202_114229:cmsbot_crab_voGroup
240202_114231:cmsbot_crab_scheddName
240202_114233:cmsbot_crab_collector
240202_114235:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 12:42:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/701/console)

## Comment (cmsdmwmbot, 2024-02-02T12:09:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 13:09:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/928/console

```
RETRY TESTS:
transferLogs-check.sh 240202_114128:cmsbot_crab_transferLogs - 2
activity-check.sh 240202_114131:cmsbot_crab_activity - 2
outputFiles-check.sh 240202_114137:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240202_114141:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240202_114143:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 240202_114209:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240202_114212:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240202_114214:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240202_114218:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240202_114220:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114126:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240202_114133:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114135:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240202_114139:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240202_114145:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114147:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114150:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114152:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114159:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114201:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114203:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114205:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114207:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240202_114216:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 240202_114222:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_114225:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114227:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114229:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114231:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114233:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114235:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-02-02T12:33:27Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-02-02 13:33:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/933/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_114126:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_114128:cmsbot_crab_transferLogs - 0
activity-check.sh 240202_114131:cmsbot_crab_activity - 0
inputFiles-check.sh 240202_114133:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_114135:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_114137:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_114139:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240202_114141:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240202_114143:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240202_114145:cmsbot_crab_numCores - 0
scriptExe-check.sh 240202_114147:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240202_114150:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240202_114152:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_114159:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_114201:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_114203:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_114205:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240202_114207:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240202_114209:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240202_114212:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240202_114214:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240202_114216:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240202_114218:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240202_114220:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_114222:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240202_114225:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240202_114227:cmsbot_crab_voRole - 0
voGroup-check.sh 240202_114229:cmsbot_crab_voGroup - 0
scheddName-check.sh 240202_114231:cmsbot_crab_scheddName - 0
collector-check.sh 240202_114233:cmsbot_crab_collector - 0
extraJDL-check.sh 240202_114235:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-02-02T14:46:47Z)

OK
