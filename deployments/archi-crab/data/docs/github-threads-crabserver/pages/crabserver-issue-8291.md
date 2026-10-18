# dmwm/CRABServer issue #8291: #726: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-03-15T19:53:22Z
Closed: 2024-03-15T20:11:29Z
URL: https://github.com/dmwm/CRABServer/issues/8291

## Opening post (cmsdmwmbot, 2024-03-15T19:53:22Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-03-15 20:53:21
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/726/)

## Comment (cmsdmwmbot, 2024-03-15T19:55:51Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240315_195341:cmsbot_crab_transferOutputs
240315_195344:cmsbot_crab_transferLogs
240315_195346:cmsbot_crab_activity
240315_195348:cmsbot_crab_inputFiles
240315_195350:cmsbot_crab_disableAutomaticOutputCollection
240315_195352:cmsbot_crab_outputFiles
240315_195354:cmsbot_crab_allowUndistributedCMSSW
240315_195356:cmsbot_crab_maxMemoryMB
240315_195359:cmsbot_crab_maxJobRuntimeMin
240315_195401:cmsbot_crab_numCores
240315_195403:cmsbot_crab_scriptExe
240315_195405:cmsbot_crab_scriptArgs
240315_195407:cmsbot_crab_sendVenvFolder
240315_195453:cmsbot_crab_sendExternalFolder
240315_195455:cmsbot_crab_inputDBS
240315_195457:cmsbot_crab_useParent
240315_195459:cmsbot_crab_secondaryInputDataset
240315_195501:cmsbot_crab_lumiMaskFile
240315_195503:cmsbot_crab_lumiMaskUrl
240315_195506:cmsbot_crab_outLFNDirBase
240315_195508:cmsbot_crab_runRange
240315_195510:cmsbot_crab_ignoreLocality
240315_195513:cmsbot_crab_userInputFiles
240315_195515:cmsbot_crab_whitelist
240315_195517:cmsbot_crab_blacklist
240315_195519:cmsbot_crab_ignoreGlobalBlacklist
240315_195521:cmsbot_crab_voRole
240315_195523:cmsbot_crab_voGroup
240315_195525:cmsbot_crab_scheddName
240315_195527:cmsbot_crab_collector
240315_195529:cmsbot_crab_extraJDL
```

Finished at: 2024-03-15 20:55:30
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/726/console)

## Comment (belforte, 2024-03-15T20:11:29Z)

bad scheduler config. try again

## Comment (cmsdmwmbot, 2024-03-15T20:18:54Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-03-15 21:18:52
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/977/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
scheddName-check.sh 240315_195525:cmsbot_crab_scheddName - 0
collector-check.sh 240315_195527:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240315_195341:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240315_195344:cmsbot_crab_transferLogs - 1
activity-check.sh 240315_195346:cmsbot_crab_activity - 1
inputFiles-check.sh 240315_195348:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240315_195350:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240315_195352:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240315_195354:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240315_195356:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240315_195359:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240315_195401:cmsbot_crab_numCores - 1
scriptExe-check.sh 240315_195403:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240315_195405:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240315_195407:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240315_195453:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240315_195455:cmsbot_crab_inputDBS - 1
useParent-check.sh 240315_195457:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240315_195459:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240315_195501:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240315_195503:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240315_195506:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240315_195508:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240315_195510:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240315_195513:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240315_195515:cmsbot_crab_whitelist - 1
blacklist-check.sh 240315_195517:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240315_195519:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240315_195521:cmsbot_crab_voRole - 1
voGroup-check.sh 240315_195523:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240315_195529:cmsbot_crab_extraJDL - 1
```
