# dmwm/CRABServer issue #8145: #653: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-11T17:29:16Z
Closed: 2024-01-11T19:44:33Z
URL: https://github.com/dmwm/CRABServer/issues/8145

## Opening post (cmsdmwmbot, 2024-01-11T17:29:16Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:29:15
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/653/)

## Comment (cmsdmwmbot, 2024-01-11T17:32:14Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173000:cmsbot_crab_transferOutputs
240111_173002:cmsbot_crab_transferLogs
240111_173005:cmsbot_crab_activity
240111_173007:cmsbot_crab_inputFiles
240111_173009:cmsbot_crab_disableAutomaticOutputCollection
240111_173012:cmsbot_crab_outputFiles
240111_173014:cmsbot_crab_allowUndistributedCMSSW
240111_173016:cmsbot_crab_maxMemoryMB
240111_173018:cmsbot_crab_maxJobRuntimeMin
240111_173020:cmsbot_crab_numCores
240111_173022:cmsbot_crab_scriptExe
240111_173025:cmsbot_crab_scriptArgs
240111_173027:cmsbot_crab_sendVenvFolder
240111_173115:cmsbot_crab_sendExternalFolder
240111_173117:cmsbot_crab_inputDBS
240111_173119:cmsbot_crab_useParent
240111_173122:cmsbot_crab_secondaryInputDataset
240111_173124:cmsbot_crab_lumiMaskFile
240111_173126:cmsbot_crab_lumiMaskUrl
240111_173129:cmsbot_crab_outLFNDirBase
240111_173131:cmsbot_crab_runRange
240111_173133:cmsbot_crab_ignoreLocality
240111_173135:cmsbot_crab_userInputFiles
240111_173137:cmsbot_crab_whitelist
240111_173139:cmsbot_crab_blacklist
240111_173141:cmsbot_crab_ignoreGlobalBlacklist
240111_173143:cmsbot_crab_voRole
240111_173145:cmsbot_crab_voGroup
240111_173147:cmsbot_crab_scheddName
240111_173149:cmsbot_crab_collector
240111_173151:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_172955:cmsbot_crab_20240111_182952
```

Finished at: 2024-01-11 18:31:52
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/653/console)

## Comment (cmsdmwmbot, 2024-01-11T17:54:59Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 18:54:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/470/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/470//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T17:58:09Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 18:58:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/847/console

```
RETRY TESTS:
lumiMaskFile-check.sh 240111_173124:cmsbot_crab_lumiMaskFile - 2
runRange-check.sh 240111_173131:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_173137:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173139:cmsbot_crab_blacklist - 2
voRole-check.sh 240111_173143:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173000:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173002:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173005:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173007:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173009:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173014:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173016:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173018:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173020:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_173025:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173027:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173115:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173117:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173119:cmsbot_crab_useParent - 0
ignoreLocality-check.sh 240111_173133:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173135:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173141:cmsbot_crab_ignoreGlobalBlacklist - 0
extraJDL-check.sh 240111_173151:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240111_173012:cmsbot_crab_outputFiles - 1
scriptExe-check.sh 240111_173022:cmsbot_crab_scriptExe - 1
secondaryInputDataset-check.sh 240111_173122:cmsbot_crab_secondaryInputDataset - 1
lumiMaskUrl-check.sh 240111_173126:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240111_173129:cmsbot_crab_outLFNDirBase - 1
voGroup-check.sh 240111_173145:cmsbot_crab_voGroup - 1
scheddName-check.sh 240111_173147:cmsbot_crab_scheddName - 1
collector-check.sh 240111_173149:cmsbot_crab_collector - 1
```

## Comment (cmsdmwmbot, 2024-01-11T18:21:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:21:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/856/console

```
RETRY TESTS:
outputFiles-check.sh 240111_173012:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 240111_173022:cmsbot_crab_scriptExe - 2
secondaryInputDataset-check.sh 240111_173122:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240111_173126:cmsbot_crab_lumiMaskUrl - 2
voRole-check.sh 240111_173143:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173000:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173002:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173005:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173007:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173009:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173014:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173016:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173018:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173020:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_173025:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173027:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173115:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173117:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173119:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 240111_173124:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_173129:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173131:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173133:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173135:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173137:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173139:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173141:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240111_173145:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173147:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173149:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173151:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:45:44Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 19:45:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/865/console

```
RETRY TESTS:
outputFiles-check.sh 240111_173012:cmsbot_crab_outputFiles - 2
scriptExe-check.sh 240111_173022:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240111_173126:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173000:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173002:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173005:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173007:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173009:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173014:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173016:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173018:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173020:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_173025:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173027:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173115:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173117:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173119:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173122:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173124:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_173129:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173131:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173133:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173135:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173137:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173139:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173141:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173143:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173145:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173147:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173149:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173151:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:09:51Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:09:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/873/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173000:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173002:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173005:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173007:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173009:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173012:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173014:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173016:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173018:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173020:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173022:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173025:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173027:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173115:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173117:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173119:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173122:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173124:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173126:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173129:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173131:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173133:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173135:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173137:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173139:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173141:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173143:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173145:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173147:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173149:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173151:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T19:44:33Z)

all OK
