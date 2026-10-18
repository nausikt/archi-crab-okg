# dmwm/CRABServer issue #8293: #728: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-15T20:27:22Z
Closed: 2024-03-15T21:34:39Z
URL: https://github.com/dmwm/CRABServer/issues/8293

## Opening post (cmsdmwmbot, 2024-03-15T20:27:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2024-03-15 21:27:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/728/)

## Comment (cmsdmwmbot, 2024-03-15T20:29:47Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240315_202741:cmsbot_crab_transferOutputs
240315_202743:cmsbot_crab_transferLogs
240315_202745:cmsbot_crab_activity
240315_202747:cmsbot_crab_inputFiles
240315_202749:cmsbot_crab_disableAutomaticOutputCollection
240315_202751:cmsbot_crab_outputFiles
240315_202753:cmsbot_crab_allowUndistributedCMSSW
240315_202755:cmsbot_crab_maxMemoryMB
240315_202757:cmsbot_crab_maxJobRuntimeMin
240315_202759:cmsbot_crab_numCores
240315_202801:cmsbot_crab_scriptExe
240315_202803:cmsbot_crab_scriptArgs
240315_202806:cmsbot_crab_sendVenvFolder
240315_202849:cmsbot_crab_sendExternalFolder
240315_202851:cmsbot_crab_inputDBS
240315_202853:cmsbot_crab_useParent
240315_202855:cmsbot_crab_secondaryInputDataset
240315_202857:cmsbot_crab_lumiMaskFile
240315_202859:cmsbot_crab_lumiMaskUrl
240315_202902:cmsbot_crab_outLFNDirBase
240315_202904:cmsbot_crab_runRange
240315_202906:cmsbot_crab_ignoreLocality
240315_202908:cmsbot_crab_userInputFiles
240315_202910:cmsbot_crab_whitelist
240315_202912:cmsbot_crab_blacklist
240315_202915:cmsbot_crab_ignoreGlobalBlacklist
240315_202917:cmsbot_crab_voRole
240315_202919:cmsbot_crab_voGroup
240315_202921:cmsbot_crab_scheddName
240315_202923:cmsbot_crab_collector
240315_202925:cmsbot_crab_extraJDL
```

Finished at: 2024-03-15 21:29:26
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/728/console)

## Comment (cmsdmwmbot, 2024-03-15T20:54:02Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-03-15 21:54:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/978/console

```
RETRY TESTS:
outputFiles-check.sh 240315_202751:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240315_202755:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240315_202757:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240315_202801:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240315_202803:cmsbot_crab_scriptArgs - 2
useParent-check.sh 240315_202853:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 240315_202859:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240315_202904:cmsbot_crab_runRange - 2
whitelist-check.sh 240315_202910:cmsbot_crab_whitelist - 2
blacklist-check.sh 240315_202912:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240315_202741:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240315_202743:cmsbot_crab_transferLogs - 0
activity-check.sh 240315_202745:cmsbot_crab_activity - 0
inputFiles-check.sh 240315_202747:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240315_202749:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240315_202753:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240315_202759:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240315_202806:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240315_202849:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240315_202851:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240315_202855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240315_202857:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240315_202902:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240315_202906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240315_202908:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240315_202915:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240315_202917:cmsbot_crab_voRole - 0
voGroup-check.sh 240315_202919:cmsbot_crab_voGroup - 0
scheddName-check.sh 240315_202921:cmsbot_crab_scheddName - 0
collector-check.sh 240315_202923:cmsbot_crab_collector - 0
extraJDL-check.sh 240315_202925:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-03-15T21:19:51Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-03-15 22:19:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/979/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240315_202741:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240315_202743:cmsbot_crab_transferLogs - 0
activity-check.sh 240315_202745:cmsbot_crab_activity - 0
inputFiles-check.sh 240315_202747:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240315_202749:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240315_202751:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240315_202753:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240315_202755:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240315_202757:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240315_202759:cmsbot_crab_numCores - 0
scriptExe-check.sh 240315_202801:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240315_202803:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240315_202806:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240315_202849:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240315_202851:cmsbot_crab_inputDBS - 0
useParent-check.sh 240315_202853:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240315_202855:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240315_202857:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240315_202859:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240315_202902:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240315_202904:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240315_202906:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240315_202908:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240315_202910:cmsbot_crab_whitelist - 0
blacklist-check.sh 240315_202912:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240315_202915:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240315_202917:cmsbot_crab_voRole - 0
voGroup-check.sh 240315_202919:cmsbot_crab_voGroup - 0
scheddName-check.sh 240315_202921:cmsbot_crab_scheddName - 0
collector-check.sh 240315_202923:cmsbot_crab_collector - 0
extraJDL-check.sh 240315_202925:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-03-15T21:34:39Z)

ALL OK
