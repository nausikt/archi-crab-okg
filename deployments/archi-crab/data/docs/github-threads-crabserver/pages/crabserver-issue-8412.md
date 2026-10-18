# dmwm/CRABServer issue #8412: #780: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-05-16T08:19:31Z
Closed: 2024-05-16T13:20:05Z
URL: https://github.com/dmwm/CRABServer/issues/8412

## Opening post (cmsdmwmbot, 2024-05-16T08:19:31Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-05-16 10:19:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/780/)

## Comment (cmsdmwmbot, 2024-05-16T08:21:23Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240516_081952:cmsbot_crab_transferOutputs
240516_081956:cmsbot_crab_transferLogs
240516_081958:cmsbot_crab_activity
240516_082000:cmsbot_crab_inputFiles
240516_082003:cmsbot_crab_disableAutomaticOutputCollection
240516_082005:cmsbot_crab_outputFiles
240516_082007:cmsbot_crab_allowUndistributedCMSSW
240516_082009:cmsbot_crab_maxMemoryMB
240516_082011:cmsbot_crab_maxJobRuntimeMin
240516_082014:cmsbot_crab_numCores
240516_082016:cmsbot_crab_scriptExe
240516_082018:cmsbot_crab_scriptArgs
240516_082020:cmsbot_crab_sendVenvFolder
240516_082022:cmsbot_crab_sendExternalFolder
240516_082024:cmsbot_crab_inputDBS
240516_082027:cmsbot_crab_useParent
240516_082029:cmsbot_crab_secondaryInputDataset
240516_082031:cmsbot_crab_lumiMaskFile
240516_082034:cmsbot_crab_lumiMaskUrl
240516_082037:cmsbot_crab_outLFNDirBase
240516_082039:cmsbot_crab_runRange
240516_082042:cmsbot_crab_ignoreLocality
240516_082044:cmsbot_crab_userInputFiles
240516_082046:cmsbot_crab_whitelist
240516_082048:cmsbot_crab_blacklist
240516_082051:cmsbot_crab_ignoreGlobalBlacklist
240516_082053:cmsbot_crab_voRole
240516_082055:cmsbot_crab_voGroup
240516_082057:cmsbot_crab_scheddName
240516_082059:cmsbot_crab_collector
240516_082101:cmsbot_crab_extraJDL
```

Finished at: 2024-05-16 10:21:02
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/780/console)

## Comment (cmsdmwmbot, 2024-05-16T08:47:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-05-16 10:47:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1065/console

```
RETRY TESTS:
transferLogs-check.sh 240516_081956:cmsbot_crab_transferLogs - 2
activity-check.sh 240516_081958:cmsbot_crab_activity - 2
outputFiles-check.sh 240516_082005:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240516_082009:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240516_082011:cmsbot_crab_maxJobRuntimeMin - 2
secondaryInputDataset-check.sh 240516_082029:cmsbot_crab_secondaryInputDataset - 2
lumiMaskFile-check.sh 240516_082031:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240516_082034:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240516_082039:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240516_082042:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240516_082044:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240516_082046:cmsbot_crab_whitelist - 2
blacklist-check.sh 240516_082048:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_081952:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240516_082000:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_082003:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240516_082007:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240516_082014:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_082016:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_082018:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_082020:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_082022:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_082024:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_082027:cmsbot_crab_useParent - 0
outLFNDirBase-check.sh 240516_082037:cmsbot_crab_outLFNDirBase - 0
ignoreGlobalBlacklist-check.sh 240516_082051:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_082053:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_082055:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_082057:cmsbot_crab_scheddName - 0
collector-check.sh 240516_082059:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_082101:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-05-16T09:12:31Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-05-16 11:12:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1066/console

```
RETRY TESTS:
transferLogs-check.sh 240516_081956:cmsbot_crab_transferLogs - 2
lumiMaskUrl-check.sh 240516_082034:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240516_082039:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_081952:cmsbot_crab_transferOutputs - 0
activity-check.sh 240516_081958:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_082000:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_082003:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240516_082007:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_082009:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_082011:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_082014:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_082016:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_082018:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_082020:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_082022:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_082024:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_082027:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240516_082029:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240516_082031:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240516_082037:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240516_082042:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_082044:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240516_082046:cmsbot_crab_whitelist - 0
blacklist-check.sh 240516_082048:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240516_082051:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_082053:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_082055:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_082057:cmsbot_crab_scheddName - 0
collector-check.sh 240516_082059:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_082101:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240516_082005:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-05-16T09:38:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-05-16 11:38:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1067/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240516_082034:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_081952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240516_081956:cmsbot_crab_transferLogs - 0
activity-check.sh 240516_081958:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_082000:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_082003:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240516_082007:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_082009:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_082011:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_082014:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_082016:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_082018:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_082020:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_082022:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_082024:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_082027:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240516_082029:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240516_082031:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240516_082037:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240516_082042:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_082044:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240516_082046:cmsbot_crab_whitelist - 0
blacklist-check.sh 240516_082048:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240516_082051:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_082053:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_082055:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_082057:cmsbot_crab_scheddName - 0
collector-check.sh 240516_082059:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_082101:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240516_082005:cmsbot_crab_outputFiles - 1
runRange-check.sh 240516_082039:cmsbot_crab_runRange - 1
```

## Comment (cmsdmwmbot, 2024-05-16T10:06:07Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-05-16 12:06:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1068/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240516_081952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240516_081956:cmsbot_crab_transferLogs - 0
activity-check.sh 240516_081958:cmsbot_crab_activity - 0
inputFiles-check.sh 240516_082000:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240516_082003:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240516_082007:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240516_082009:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240516_082011:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240516_082014:cmsbot_crab_numCores - 0
scriptExe-check.sh 240516_082016:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240516_082018:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240516_082020:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240516_082022:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240516_082024:cmsbot_crab_inputDBS - 0
useParent-check.sh 240516_082027:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240516_082029:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240516_082031:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240516_082034:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240516_082037:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240516_082042:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240516_082044:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240516_082046:cmsbot_crab_whitelist - 0
blacklist-check.sh 240516_082048:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240516_082051:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240516_082053:cmsbot_crab_voRole - 0
voGroup-check.sh 240516_082055:cmsbot_crab_voGroup - 0
scheddName-check.sh 240516_082057:cmsbot_crab_scheddName - 0
collector-check.sh 240516_082059:cmsbot_crab_collector - 0
extraJDL-check.sh 240516_082101:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 240516_082005:cmsbot_crab_outputFiles - 1
runRange-check.sh 240516_082039:cmsbot_crab_runRange - 1
```

## Comment (belforte, 2024-05-16T13:20:05Z)

outputFiles error is expected. runRange has a read error at DESY
