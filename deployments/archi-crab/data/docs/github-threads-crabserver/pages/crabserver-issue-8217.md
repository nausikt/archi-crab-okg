# dmwm/CRABServer issue #8217: #698: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-02T08:34:52Z
Closed: 2024-02-02T09:48:26Z
URL: https://github.com/dmwm/CRABServer/issues/8217

## Opening post (cmsdmwmbot, 2024-02-02T08:34:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-02 09:34:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/698/)

## Comment (cmsdmwmbot, 2024-02-02T08:37:19Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240202_083510:cmsbot_crab_transferOutputs
240202_083513:cmsbot_crab_transferLogs
240202_083515:cmsbot_crab_activity
240202_083517:cmsbot_crab_inputFiles
240202_083519:cmsbot_crab_disableAutomaticOutputCollection
240202_083521:cmsbot_crab_outputFiles
240202_083523:cmsbot_crab_allowUndistributedCMSSW
240202_083525:cmsbot_crab_maxMemoryMB
240202_083527:cmsbot_crab_maxJobRuntimeMin
240202_083529:cmsbot_crab_numCores
240202_083531:cmsbot_crab_scriptExe
240202_083532:cmsbot_crab_scriptArgs
240202_083535:cmsbot_crab_sendVenvFolder
240202_083617:cmsbot_crab_sendExternalFolder
240202_083619:cmsbot_crab_inputDBS
240202_083621:cmsbot_crab_useParent
240202_083623:cmsbot_crab_secondaryInputDataset
240202_083625:cmsbot_crab_lumiMaskFile
240202_083627:cmsbot_crab_lumiMaskUrl
240202_083635:cmsbot_crab_outLFNDirBase
240202_083637:cmsbot_crab_runRange
240202_083639:cmsbot_crab_ignoreLocality
240202_083641:cmsbot_crab_userInputFiles
240202_083643:cmsbot_crab_whitelist
240202_083645:cmsbot_crab_blacklist
240202_083647:cmsbot_crab_ignoreGlobalBlacklist
240202_083649:cmsbot_crab_voRole
240202_083651:cmsbot_crab_voGroup
240202_083653:cmsbot_crab_scheddName
240202_083655:cmsbot_crab_collector
240202_083657:cmsbot_crab_extraJDL
```

Finished at: 2024-02-02 09:36:58
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/698/console)

## Comment (cmsdmwmbot, 2024-02-02T09:01:07Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-02 10:01:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/922/console

```
RETRY TESTS:
transferLogs-check.sh 240202_083513:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 240202_083521:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240202_083527:cmsbot_crab_maxJobRuntimeMin - 2
lumiMaskUrl-check.sh 240202_083627:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240202_083637:cmsbot_crab_runRange - 2
whitelist-check.sh 240202_083643:cmsbot_crab_whitelist - 2
blacklist-check.sh 240202_083645:cmsbot_crab_blacklist - 2
voRole-check.sh 240202_083649:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_083510:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240202_083517:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_083519:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240202_083523:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240202_083535:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_083617:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_083619:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_083621:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_083623:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240202_083653:cmsbot_crab_scheddName - 0
collector-check.sh 240202_083655:cmsbot_crab_collector - 0

FAILED TESTS:
activity-check.sh 240202_083515:cmsbot_crab_activity - 1
maxMemoryMB-check.sh 240202_083525:cmsbot_crab_maxMemoryMB - 1
numCores-check.sh 240202_083529:cmsbot_crab_numCores - 1
scriptExe-check.sh 240202_083531:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240202_083532:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240202_083625:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240202_083635:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240202_083639:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240202_083641:cmsbot_crab_userInputFiles - 1
ignoreGlobalBlacklist-check.sh 240202_083647:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240202_083651:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240202_083657:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-02-02T09:26:27Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-02 10:26:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/923/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240202_083510:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240202_083513:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240202_083517:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240202_083519:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240202_083521:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240202_083523:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240202_083535:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240202_083617:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240202_083619:cmsbot_crab_inputDBS - 0
useParent-check.sh 240202_083621:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240202_083623:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240202_083627:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240202_083637:cmsbot_crab_runRange - 0
whitelist-check.sh 240202_083643:cmsbot_crab_whitelist - 0
blacklist-check.sh 240202_083645:cmsbot_crab_blacklist - 0
voRole-check.sh 240202_083649:cmsbot_crab_voRole - 0
scheddName-check.sh 240202_083653:cmsbot_crab_scheddName - 0
collector-check.sh 240202_083655:cmsbot_crab_collector - 0

FAILED TESTS:
activity-check.sh 240202_083515:cmsbot_crab_activity - 1
maxMemoryMB-check.sh 240202_083525:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240202_083527:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240202_083529:cmsbot_crab_numCores - 1
scriptExe-check.sh 240202_083531:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240202_083532:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240202_083625:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240202_083635:cmsbot_crab_outLFNDirBase - 1
ignoreLocality-check.sh 240202_083639:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240202_083641:cmsbot_crab_userInputFiles - 1
ignoreGlobalBlacklist-check.sh 240202_083647:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240202_083651:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240202_083657:cmsbot_crab_extraJDL - 1
```
