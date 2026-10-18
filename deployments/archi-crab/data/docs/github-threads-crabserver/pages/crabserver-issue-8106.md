# dmwm/CRABServer issue #8106: #622: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-12-15T22:44:28Z
Closed: 2023-12-16T16:25:10Z
URL: https://github.com/dmwm/CRABServer/issues/8106

## Opening post (cmsdmwmbot, 2023-12-15T22:44:28Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-15 23:44:27
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/622/)

## Comment (cmsdmwmbot, 2023-12-15T22:46:57Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
231215_224447:cmsbot_crab_transferOutputs
231215_224449:cmsbot_crab_transferLogs
231215_224451:cmsbot_crab_activity
231215_224453:cmsbot_crab_inputFiles
231215_224455:cmsbot_crab_disableAutomaticOutputCollection
231215_224457:cmsbot_crab_outputFiles
231215_224459:cmsbot_crab_allowUndistributedCMSSW
231215_224501:cmsbot_crab_maxMemoryMB
231215_224503:cmsbot_crab_maxJobRuntimeMin
231215_224505:cmsbot_crab_numCores
231215_224507:cmsbot_crab_scriptExe
231215_224509:cmsbot_crab_scriptArgs
231215_224511:cmsbot_crab_sendVenvFolder
231215_224600:cmsbot_crab_sendExternalFolder
231215_224602:cmsbot_crab_inputDBS
231215_224604:cmsbot_crab_useParent
231215_224606:cmsbot_crab_secondaryInputDataset
231215_224608:cmsbot_crab_lumiMaskFile
231215_224610:cmsbot_crab_lumiMaskUrl
231215_224613:cmsbot_crab_outLFNDirBase
231215_224615:cmsbot_crab_runRange
231215_224617:cmsbot_crab_ignoreLocality
231215_224619:cmsbot_crab_userInputFiles
231215_224621:cmsbot_crab_whitelist
231215_224623:cmsbot_crab_blacklist
231215_224625:cmsbot_crab_ignoreGlobalBlacklist
231215_224627:cmsbot_crab_voRole
231215_224629:cmsbot_crab_voGroup
231215_224631:cmsbot_crab_scheddName
231215_224633:cmsbot_crab_collector
231215_224635:cmsbot_crab_extraJDL
```

Finished at: 2023-12-15 23:46:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/622/console)

## Comment (cmsdmwmbot, 2023-12-15T23:10:37Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2023-12-16 00:10:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/791/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 231215_224447:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 231215_224449:cmsbot_crab_transferLogs - 1
activity-check.sh 231215_224451:cmsbot_crab_activity - 1
inputFiles-check.sh 231215_224453:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 231215_224455:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 231215_224457:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 231215_224459:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 231215_224501:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 231215_224503:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 231215_224505:cmsbot_crab_numCores - 1
scriptExe-check.sh 231215_224507:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 231215_224509:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 231215_224511:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 231215_224600:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 231215_224602:cmsbot_crab_inputDBS - 1
useParent-check.sh 231215_224604:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 231215_224606:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 231215_224608:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 231215_224610:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 231215_224613:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 231215_224615:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 231215_224617:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 231215_224619:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 231215_224621:cmsbot_crab_whitelist - 1
blacklist-check.sh 231215_224623:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 231215_224625:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 231215_224627:cmsbot_crab_voRole - 1
voGroup-check.sh 231215_224629:cmsbot_crab_voGroup - 1
scheddName-check.sh 231215_224631:cmsbot_crab_scheddName - 1
collector-check.sh 231215_224633:cmsbot_crab_collector - 1
extraJDL-check.sh 231215_224635:cmsbot_crab_extraJDL - 1
```
