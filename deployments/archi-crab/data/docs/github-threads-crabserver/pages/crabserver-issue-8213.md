# dmwm/CRABServer issue #8213: #695: Test GH CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-01-31T16:39:03Z
Closed: 2024-01-31T19:53:24Z
URL: https://github.com/dmwm/CRABServer/issues/8213

## Opening post (cmsdmwmbot, 2024-01-31T16:39:03Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-01-31 17:39:03
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/695/)

## Comment (cmsdmwmbot, 2024-01-31T16:41:01Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240131_163924:cmsbot_crab_transferOutputs
240131_163926:cmsbot_crab_transferLogs
240131_163928:cmsbot_crab_activity
240131_163929:cmsbot_crab_inputFiles
240131_163931:cmsbot_crab_disableAutomaticOutputCollection
240131_163933:cmsbot_crab_outputFiles
240131_163935:cmsbot_crab_allowUndistributedCMSSW
240131_163937:cmsbot_crab_maxMemoryMB
240131_163939:cmsbot_crab_maxJobRuntimeMin
240131_163940:cmsbot_crab_numCores
240131_163942:cmsbot_crab_scriptExe
240131_163944:cmsbot_crab_scriptArgs
240131_163946:cmsbot_crab_sendVenvFolder
240131_163953:cmsbot_crab_sendExternalFolder
240131_163955:cmsbot_crab_inputDBS
240131_163957:cmsbot_crab_useParent
240131_163959:cmsbot_crab_secondaryInputDataset
240131_164001:cmsbot_crab_lumiMaskFile
240131_164003:cmsbot_crab_lumiMaskUrl
240131_164020:cmsbot_crab_outLFNDirBase
240131_164021:cmsbot_crab_runRange
240131_164023:cmsbot_crab_ignoreLocality
240131_164025:cmsbot_crab_userInputFiles
240131_164027:cmsbot_crab_whitelist
240131_164029:cmsbot_crab_blacklist
240131_164030:cmsbot_crab_ignoreGlobalBlacklist
240131_164032:cmsbot_crab_voRole
240131_164034:cmsbot_crab_voGroup
240131_164036:cmsbot_crab_scheddName
240131_164038:cmsbot_crab_collector
240131_164039:cmsbot_crab_extraJDL
```

Finished at: 2024-01-31 17:40:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/695/console)

## Comment (cmsdmwmbot, 2024-01-31T17:06:33Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-31 18:06:31
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/914/console

```
RETRY TESTS:
maxMemoryMB-check.sh 240131_163937:cmsbot_crab_maxMemoryMB - 2
useParent-check.sh 240131_163957:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240131_163959:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240131_164003:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240131_164020:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240131_164021:cmsbot_crab_runRange - 2
whitelist-check.sh 240131_164027:cmsbot_crab_whitelist - 2
blacklist-check.sh 240131_164029:cmsbot_crab_blacklist - 2
voGroup-check.sh 240131_164034:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_163924:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240131_163926:cmsbot_crab_transferLogs - 0
activity-check.sh 240131_163928:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_163929:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_163931:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_163933:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_163935:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240131_163939:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_163940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_163942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_163944:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_163946:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_163953:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_163955:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240131_164001:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240131_164023:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240131_164025:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240131_164030:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_164032:cmsbot_crab_voRole - 0
scheddName-check.sh 240131_164036:cmsbot_crab_scheddName - 0
collector-check.sh 240131_164038:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_164039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-31T17:31:04Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-01-31 18:31:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/916/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240131_163924:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240131_163926:cmsbot_crab_transferLogs - 0
activity-check.sh 240131_163928:cmsbot_crab_activity - 0
inputFiles-check.sh 240131_163929:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240131_163931:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240131_163933:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240131_163935:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240131_163937:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240131_163939:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240131_163940:cmsbot_crab_numCores - 0
scriptExe-check.sh 240131_163942:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240131_163944:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240131_163946:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240131_163953:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240131_163955:cmsbot_crab_inputDBS - 0
useParent-check.sh 240131_163957:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240131_163959:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240131_164001:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240131_164003:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240131_164020:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240131_164021:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240131_164023:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240131_164025:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240131_164027:cmsbot_crab_whitelist - 0
blacklist-check.sh 240131_164029:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240131_164030:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240131_164032:cmsbot_crab_voRole - 0
voGroup-check.sh 240131_164034:cmsbot_crab_voGroup - 0
scheddName-check.sh 240131_164036:cmsbot_crab_scheddName - 0
collector-check.sh 240131_164038:cmsbot_crab_collector - 0
extraJDL-check.sh 240131_164039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-31T19:53:24Z)

all OK
