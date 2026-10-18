# dmwm/CRABServer issue #7692: #402: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-28T23:50:40Z
Closed: 2023-06-29T20:16:19Z
URL: https://github.com/dmwm/CRABServer/issues/7692

## Opening post (cmsdmwmbot, 2023-06-28T23:50:40Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-29 01:50:39
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/402/)

## Comment (cmsdmwmbot, 2023-06-28T23:52:56Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230628_235058:cmsbot_crab_transferOutputs
230628_235101:cmsbot_crab_transferLogs
230628_235102:cmsbot_crab_activity
230628_235103:cmsbot_crab_inputFiles
230628_235105:cmsbot_crab_disableAutomaticOutputCollection
230628_235106:cmsbot_crab_outputFiles
230628_235107:cmsbot_crab_allowUndistributedCMSSW
230628_235109:cmsbot_crab_maxMemoryMB
230628_235110:cmsbot_crab_maxJobRuntimeMin
230628_235111:cmsbot_crab_numCores
230628_235113:cmsbot_crab_scriptExe
230628_235114:cmsbot_crab_scriptArgs
230628_235115:cmsbot_crab_sendPythonFolder
230628_235157:cmsbot_crab_sendExternalFolder
230628_235158:cmsbot_crab_inputDBS
230628_235200:cmsbot_crab_useParent
230628_235201:cmsbot_crab_secondaryInputDataset
230628_235202:cmsbot_crab_lumiMaskFile
230628_235204:cmsbot_crab_lumiMaskUrl
230628_235219:cmsbot_crab_outLFNDirBase
230628_235221:cmsbot_crab_runRange
230628_235222:cmsbot_crab_ignoreLocality
230628_235223:cmsbot_crab_userInputFiles
230628_235224:cmsbot_crab_whitelist
230628_235226:cmsbot_crab_blacklist
230628_235227:cmsbot_crab_ignoreGlobalBlacklist
230628_235228:cmsbot_crab_voRole
230628_235230:cmsbot_crab_voGroup
230628_235231:cmsbot_crab_scheddName
230628_235232:cmsbot_crab_collector
230628_235234:cmsbot_crab_extraJDL
```

Finished at: 2023-06-29 01:52:35
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/402/console)

## Comment (cmsdmwmbot, 2023-06-29T00:15:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 02:15:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/627/console

```
RETRY TESTS:
useParent-check.sh 230628_235200:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 230628_235204:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230628_235221:cmsbot_crab_runRange - 2
whitelist-check.sh 230628_235224:cmsbot_crab_whitelist - 2
blacklist-check.sh 230628_235226:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230628_235227:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230628_235228:cmsbot_crab_voRole - 2
voGroup-check.sh 230628_235230:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230628_235058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230628_235101:cmsbot_crab_transferLogs - 0
activity-check.sh 230628_235102:cmsbot_crab_activity - 0
inputFiles-check.sh 230628_235103:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230628_235105:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230628_235107:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230628_235109:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230628_235110:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230628_235111:cmsbot_crab_numCores - 0
sendPythonFolder-check.sh 230628_235115:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230628_235157:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230628_235158:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 230628_235201:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230628_235202:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230628_235219:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230628_235222:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230628_235223:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 230628_235231:cmsbot_crab_scheddName - 0
collector-check.sh 230628_235232:cmsbot_crab_collector - 0
extraJDL-check.sh 230628_235234:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230628_235106:cmsbot_crab_outputFiles - 1
scriptExe-check.sh 230628_235113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230628_235114:cmsbot_crab_scriptArgs - 1
```

## Comment (cmsdmwmbot, 2023-06-29T00:37:03Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-29 02:37:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/628/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230628_235058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230628_235101:cmsbot_crab_transferLogs - 0
activity-check.sh 230628_235102:cmsbot_crab_activity - 0
inputFiles-check.sh 230628_235103:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230628_235105:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 230628_235107:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230628_235109:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230628_235110:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230628_235111:cmsbot_crab_numCores - 0
sendPythonFolder-check.sh 230628_235115:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230628_235157:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230628_235158:cmsbot_crab_inputDBS - 0
useParent-check.sh 230628_235200:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230628_235201:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230628_235202:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230628_235204:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230628_235219:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230628_235221:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230628_235222:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230628_235223:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230628_235224:cmsbot_crab_whitelist - 0
blacklist-check.sh 230628_235226:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230628_235227:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230628_235228:cmsbot_crab_voRole - 0
voGroup-check.sh 230628_235230:cmsbot_crab_voGroup - 0
scheddName-check.sh 230628_235231:cmsbot_crab_scheddName - 0
collector-check.sh 230628_235232:cmsbot_crab_collector - 0
extraJDL-check.sh 230628_235234:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 230628_235106:cmsbot_crab_outputFiles - 1
scriptExe-check.sh 230628_235113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230628_235114:cmsbot_crab_scriptArgs - 1
```
