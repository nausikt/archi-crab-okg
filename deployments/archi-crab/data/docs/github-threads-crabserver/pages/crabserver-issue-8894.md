# dmwm/CRABServer issue #8894: #929: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-01-27T23:48:28Z
Closed: 2025-01-28T22:21:55Z
URL: https://github.com/dmwm/CRABServer/issues/8894

## Opening post (cmsdmwmbot, 2025-01-27T23:48:28Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2025-01-28 00:48:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/929/)

## Comment (cmsdmwmbot, 2025-01-27T23:50:47Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
250127_234847:cmsbot_crab_transferOutputs
250127_234850:cmsbot_crab_transferLogs
250127_234853:cmsbot_crab_activity
250127_234857:cmsbot_crab_inputFiles
250127_234901:cmsbot_crab_disableAutomaticOutputCollection
250127_234905:cmsbot_crab_outputFiles
250127_234908:cmsbot_crab_allowUndistributedCMSSW
250127_234911:cmsbot_crab_maxMemoryMB
250127_234914:cmsbot_crab_maxJobRuntimeMin
250127_234919:cmsbot_crab_numCores
250127_234922:cmsbot_crab_scriptExe
250127_234925:cmsbot_crab_scriptArgs
250127_234929:cmsbot_crab_sendVenvFolder
250127_234933:cmsbot_crab_sendExternalFolder
250127_234936:cmsbot_crab_inputDBS
250127_234940:cmsbot_crab_useParent
250127_234943:cmsbot_crab_secondaryInputDataset
250127_234946:cmsbot_crab_lumiMaskFile
250127_234949:cmsbot_crab_lumiMaskUrl
250127_234953:cmsbot_crab_outLFNDirBase
250127_234956:cmsbot_crab_runRange
250127_234959:cmsbot_crab_ignoreLocality
250127_235003:cmsbot_crab_userInputFiles
250127_235006:cmsbot_crab_whitelist
250127_235009:cmsbot_crab_blacklist
250127_235012:cmsbot_crab_ignoreGlobalBlacklist
250127_235016:cmsbot_crab_voRole
250127_235019:cmsbot_crab_scheddName
250127_235022:cmsbot_crab_collector
250127_235025:cmsbot_crab_extraJDL
```

Finished at: 2025-01-28 00:50:25
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/929/console)

## Comment (cmsdmwmbot, 2025-01-28T00:49:53Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2025-01-28 01:49:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1266/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250127_234847:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250127_234850:cmsbot_crab_transferLogs - 0
activity-check.sh 250127_234853:cmsbot_crab_activity - 0
inputFiles-check.sh 250127_234857:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250127_234901:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250127_234905:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250127_234908:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 250127_234929:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250127_234933:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250127_234936:cmsbot_crab_inputDBS - 0
useParent-check.sh 250127_234940:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250127_234943:cmsbot_crab_secondaryInputDataset - 0
outLFNDirBase-check.sh 250127_234953:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 250127_234959:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250127_235003:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250127_235006:cmsbot_crab_whitelist - 0
blacklist-check.sh 250127_235009:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250127_235012:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250127_235016:cmsbot_crab_voRole - 0
scheddName-check.sh 250127_235019:cmsbot_crab_scheddName - 0
collector-check.sh 250127_235022:cmsbot_crab_collector - 0
extraJDL-check.sh 250127_235025:cmsbot_crab_extraJDL - 0

FAILED TESTS:
maxMemoryMB-check.sh 250127_234911:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 250127_234914:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 250127_234919:cmsbot_crab_numCores - 1
scriptExe-check.sh 250127_234922:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250127_234925:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 250127_234946:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 250127_234949:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 250127_234956:cmsbot_crab_runRange - 1

RETRY TESTS:
 none
```

## Comment (belforte, 2025-01-28T22:21:55Z)

problems understood, fix in progress
