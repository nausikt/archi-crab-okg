# dmwm/CRABServer issue #8490: #803: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-12T10:00:37Z
Closed: 2024-06-12T10:02:50Z
URL: https://github.com/dmwm/CRABServer/issues/8490

## Opening post (cmsdmwmbot, 2024-06-12T10:00:37Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-06-12 12:00:36
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/803/)

## Comment (cmsdmwmbot, 2024-06-12T10:02:24Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240612_100058:cmsbot_crab_transferOutputs
240612_100100:cmsbot_crab_transferLogs
240612_100102:cmsbot_crab_activity
240612_100104:cmsbot_crab_inputFiles
240612_100106:cmsbot_crab_disableAutomaticOutputCollection
240612_100108:cmsbot_crab_outputFiles
240612_100110:cmsbot_crab_allowUndistributedCMSSW
240612_100113:cmsbot_crab_maxMemoryMB
240612_100115:cmsbot_crab_maxJobRuntimeMin
240612_100117:cmsbot_crab_numCores
240612_100119:cmsbot_crab_scriptExe
240612_100121:cmsbot_crab_scriptArgs
240612_100123:cmsbot_crab_sendVenvFolder
240612_100125:cmsbot_crab_sendExternalFolder
240612_100127:cmsbot_crab_inputDBS
240612_100129:cmsbot_crab_useParent
240612_100131:cmsbot_crab_secondaryInputDataset
240612_100133:cmsbot_crab_lumiMaskFile
240612_100136:cmsbot_crab_lumiMaskUrl
240612_100139:cmsbot_crab_outLFNDirBase
240612_100141:cmsbot_crab_runRange
240612_100143:cmsbot_crab_ignoreLocality
240612_100145:cmsbot_crab_userInputFiles
240612_100147:cmsbot_crab_whitelist
240612_100149:cmsbot_crab_blacklist
240612_100151:cmsbot_crab_ignoreGlobalBlacklist
240612_100153:cmsbot_crab_voRole
240612_100156:cmsbot_crab_voGroup
240612_100158:cmsbot_crab_scheddName
240612_100200:cmsbot_crab_collector
240612_100202:cmsbot_crab_extraJDL
```

Finished at: 2024-06-12 12:02:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/803/console)

## Comment (belforte, 2024-06-12T10:02:50Z)

my bad, this can't work

## Comment (cmsdmwmbot, 2024-06-12T10:27:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-12 12:27:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1114/console

```
RETRY TESTS:
transferLogs-check.sh 240612_100100:cmsbot_crab_transferLogs - 2
maxMemoryMB-check.sh 240612_100113:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240612_100115:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240612_100117:cmsbot_crab_numCores - 2
lumiMaskUrl-check.sh 240612_100136:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240612_100141:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240612_100145:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240612_100147:cmsbot_crab_whitelist - 2
blacklist-check.sh 240612_100149:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240612_100058:cmsbot_crab_transferOutputs - 0
activity-check.sh 240612_100102:cmsbot_crab_activity - 0
inputFiles-check.sh 240612_100104:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240612_100106:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240612_100108:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240612_100110:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 240612_100119:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240612_100121:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240612_100123:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240612_100125:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240612_100127:cmsbot_crab_inputDBS - 0
useParent-check.sh 240612_100129:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240612_100131:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240612_100133:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240612_100139:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240612_100143:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240612_100151:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240612_100153:cmsbot_crab_voRole - 0
voGroup-check.sh 240612_100156:cmsbot_crab_voGroup - 0
scheddName-check.sh 240612_100158:cmsbot_crab_scheddName - 0
collector-check.sh 240612_100200:cmsbot_crab_collector - 0
extraJDL-check.sh 240612_100202:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-06-12T10:51:42Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-06-12 12:51:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1115/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240612_100058:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240612_100100:cmsbot_crab_transferLogs - 0
activity-check.sh 240612_100102:cmsbot_crab_activity - 0
inputFiles-check.sh 240612_100104:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240612_100106:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240612_100108:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240612_100110:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240612_100113:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240612_100115:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240612_100117:cmsbot_crab_numCores - 0
scriptExe-check.sh 240612_100119:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240612_100121:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240612_100123:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240612_100125:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240612_100127:cmsbot_crab_inputDBS - 0
useParent-check.sh 240612_100129:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240612_100131:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240612_100133:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240612_100136:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240612_100139:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240612_100141:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240612_100143:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240612_100145:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240612_100147:cmsbot_crab_whitelist - 0
blacklist-check.sh 240612_100149:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240612_100151:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240612_100153:cmsbot_crab_voRole - 0
voGroup-check.sh 240612_100156:cmsbot_crab_voGroup - 0
scheddName-check.sh 240612_100158:cmsbot_crab_scheddName - 0
collector-check.sh 240612_100200:cmsbot_crab_collector - 0
extraJDL-check.sh 240612_100202:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
