# dmwm/CRABServer issue #8215: #696: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-01T21:20:01Z
Closed: 2024-02-01T21:42:30Z
URL: https://github.com/dmwm/CRABServer/issues/8215

## Opening post (cmsdmwmbot, 2024-02-01T21:20:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-01 22:20:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/696/)

## Comment (cmsdmwmbot, 2024-02-01T21:22:20Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240201_212020:cmsbot_crab_transferOutputs
240201_212022:cmsbot_crab_transferLogs
240201_212024:cmsbot_crab_activity
240201_212025:cmsbot_crab_inputFiles
240201_212027:cmsbot_crab_disableAutomaticOutputCollection
240201_212029:cmsbot_crab_outputFiles
240201_212031:cmsbot_crab_allowUndistributedCMSSW
240201_212033:cmsbot_crab_maxMemoryMB
240201_212035:cmsbot_crab_maxJobRuntimeMin
240201_212037:cmsbot_crab_numCores
240201_212039:cmsbot_crab_scriptExe
240201_212041:cmsbot_crab_scriptArgs
240201_212043:cmsbot_crab_sendVenvFolder
240201_212123:cmsbot_crab_sendExternalFolder
240201_212125:cmsbot_crab_inputDBS
240201_212127:cmsbot_crab_useParent
240201_212130:cmsbot_crab_secondaryInputDataset
240201_212132:cmsbot_crab_lumiMaskFile
240201_212134:cmsbot_crab_lumiMaskUrl
240201_212137:cmsbot_crab_outLFNDirBase
240201_212139:cmsbot_crab_runRange
240201_212140:cmsbot_crab_ignoreLocality
240201_212142:cmsbot_crab_userInputFiles
240201_212144:cmsbot_crab_whitelist
240201_212146:cmsbot_crab_blacklist
240201_212148:cmsbot_crab_ignoreGlobalBlacklist
240201_212150:cmsbot_crab_voRole
240201_212152:cmsbot_crab_voGroup
240201_212154:cmsbot_crab_scheddName
240201_212156:cmsbot_crab_collector
240201_212158:cmsbot_crab_extraJDL
```

Finished at: 2024-02-01 22:21:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/696/console)

## Comment (belforte, 2024-02-01T21:42:30Z)

will fail. Bad TW image

## Comment (cmsdmwmbot, 2024-02-01T21:46:09Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-01 22:46:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/918/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240201_212020:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240201_212025:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240201_212027:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240201_212031:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240201_212043:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240201_212123:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240201_212125:cmsbot_crab_inputDBS - 0
useParent-check.sh 240201_212127:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240201_212130:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240201_212154:cmsbot_crab_scheddName - 0
collector-check.sh 240201_212156:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240201_212022:cmsbot_crab_transferLogs - 1
activity-check.sh 240201_212024:cmsbot_crab_activity - 1
outputFiles-check.sh 240201_212029:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240201_212033:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240201_212035:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240201_212037:cmsbot_crab_numCores - 1
scriptExe-check.sh 240201_212039:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240201_212041:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240201_212132:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240201_212134:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240201_212137:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240201_212139:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240201_212140:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240201_212142:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240201_212144:cmsbot_crab_whitelist - 1
blacklist-check.sh 240201_212146:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240201_212148:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240201_212150:cmsbot_crab_voRole - 1
voGroup-check.sh 240201_212152:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240201_212158:cmsbot_crab_extraJDL - 1
```
