# dmwm/CRABServer issue #7707: #417: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-30T15:59:01Z
Closed: 2023-06-30T17:21:46Z
URL: https://github.com/dmwm/CRABServer/issues/7707

## Opening post (cmsdmwmbot, 2023-06-30T15:59:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-06-30 17:59:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/417/)

## Comment (cmsdmwmbot, 2023-06-30T16:01:01Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_155918:cmsbot_crab_transferOutputs
230630_155919:cmsbot_crab_transferLogs
230630_155921:cmsbot_crab_activity
230630_155922:cmsbot_crab_inputFiles
230630_155923:cmsbot_crab_disableAutomaticOutputCollection
230630_155925:cmsbot_crab_outputFiles
230630_155926:cmsbot_crab_allowUndistributedCMSSW
230630_155927:cmsbot_crab_maxMemoryMB
230630_155928:cmsbot_crab_maxJobRuntimeMin
230630_155930:cmsbot_crab_numCores
230630_155931:cmsbot_crab_scriptExe
230630_155932:cmsbot_crab_scriptArgs
230630_155933:cmsbot_crab_sendPythonFolder
230630_160013:cmsbot_crab_sendExternalFolder
230630_160015:cmsbot_crab_inputDBS
230630_160016:cmsbot_crab_useParent
230630_160018:cmsbot_crab_secondaryInputDataset
230630_160019:cmsbot_crab_lumiMaskFile
230630_160021:cmsbot_crab_lumiMaskUrl
230630_160023:cmsbot_crab_outLFNDirBase
230630_160024:cmsbot_crab_runRange
230630_160026:cmsbot_crab_ignoreLocality
230630_160027:cmsbot_crab_userInputFiles
230630_160029:cmsbot_crab_whitelist
230630_160030:cmsbot_crab_blacklist
230630_160032:cmsbot_crab_ignoreGlobalBlacklist
230630_160033:cmsbot_crab_voRole
230630_160034:cmsbot_crab_voGroup
230630_160036:cmsbot_crab_scheddName
230630_160037:cmsbot_crab_collector
230630_160039:cmsbot_crab_extraJDL
```

Finished at: 2023-06-30 18:00:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/417/console)

## Comment (cmsdmwmbot, 2023-06-30T16:27:34Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-30 18:27:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/661/console

```
RETRY TESTS:
outputFiles-check.sh 230630_155925:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 230630_155928:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskFile-check.sh 230630_160019:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230630_160021:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230630_160023:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230630_160024:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 230630_160026:cmsbot_crab_ignoreLocality - 2
whitelist-check.sh 230630_160029:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_160030:cmsbot_crab_blacklist - 2
voRole-check.sh 230630_160033:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155918:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_155919:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_155921:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_155922:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_155923:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230630_155926:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_155927:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230630_155930:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_155931:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_155932:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_155933:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_160013:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_160015:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_160016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_160018:cmsbot_crab_secondaryInputDataset - 0
userInputFiles-check.sh 230630_160027:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230630_160032:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230630_160034:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_160036:cmsbot_crab_scheddName - 0
collector-check.sh 230630_160037:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_160039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-30T16:54:30Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-30 18:54:29
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/663/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230630_155928:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 230630_160021:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230630_160023:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230630_160024:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155918:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_155919:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_155921:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_155922:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_155923:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_155925:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_155926:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_155927:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230630_155930:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_155931:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_155932:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_155933:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_160013:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_160015:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_160016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_160018:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_160019:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230630_160026:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_160027:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_160029:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_160030:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_160032:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_160033:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_160034:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_160036:cmsbot_crab_scheddName - 0
collector-check.sh 230630_160037:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_160039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-06-30T17:20:53Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-06-30 19:20:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/665/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_155918:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_155919:cmsbot_crab_transferLogs - 0
activity-check.sh 230630_155921:cmsbot_crab_activity - 0
inputFiles-check.sh 230630_155922:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230630_155923:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230630_155925:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230630_155926:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230630_155927:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230630_155928:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230630_155930:cmsbot_crab_numCores - 0
scriptExe-check.sh 230630_155931:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230630_155932:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_155933:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_160013:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_160015:cmsbot_crab_inputDBS - 0
useParent-check.sh 230630_160016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230630_160018:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230630_160019:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230630_160021:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230630_160023:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230630_160024:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_160026:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_160027:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_160029:cmsbot_crab_whitelist - 0
blacklist-check.sh 230630_160030:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230630_160032:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230630_160033:cmsbot_crab_voRole - 0
voGroup-check.sh 230630_160034:cmsbot_crab_voGroup - 0
scheddName-check.sh 230630_160036:cmsbot_crab_scheddName - 0
collector-check.sh 230630_160037:cmsbot_crab_collector - 0
extraJDL-check.sh 230630_160039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2023-06-30T17:21:46Z)

all OK
