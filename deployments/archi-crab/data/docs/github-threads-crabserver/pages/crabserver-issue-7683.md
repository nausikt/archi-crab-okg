# dmwm/CRABServer issue #7683: #397: Test prod CRABClient using test2 REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2023-06-27T23:03:52Z
Closed: 2023-06-29T20:16:17Z
URL: https://github.com/dmwm/CRABServer/issues/7683

## Opening post (cmsdmwmbot, 2023-06-27T23:03:52Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-28 01:03:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/397/)

## Comment (cmsdmwmbot, 2023-06-27T23:07:20Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230627_230534:cmsbot_crab_transferOutputs
230627_230537:cmsbot_crab_transferLogs
230627_230539:cmsbot_crab_activity
230627_230542:cmsbot_crab_inputFiles
230627_230545:cmsbot_crab_disableAutomaticOutputCollection
230627_230547:cmsbot_crab_outputFiles
230627_230550:cmsbot_crab_allowUndistributedCMSSW
230627_230552:cmsbot_crab_maxMemoryMB
230627_230555:cmsbot_crab_maxJobRuntimeMin
230627_230558:cmsbot_crab_numCores
230627_230600:cmsbot_crab_scriptExe
230627_230603:cmsbot_crab_scriptArgs
230627_230606:cmsbot_crab_sendPythonFolder
230627_230613:cmsbot_crab_sendExternalFolder
230627_230616:cmsbot_crab_inputDBS
230627_230619:cmsbot_crab_useParent
230627_230621:cmsbot_crab_secondaryInputDataset
230627_230624:cmsbot_crab_lumiMaskFile
230627_230627:cmsbot_crab_lumiMaskUrl
230627_230630:cmsbot_crab_outLFNDirBase
230627_230633:cmsbot_crab_runRange
230627_230636:cmsbot_crab_ignoreLocality
230627_230638:cmsbot_crab_userInputFiles
230627_230641:cmsbot_crab_whitelist
230627_230643:cmsbot_crab_blacklist
230627_230646:cmsbot_crab_ignoreGlobalBlacklist
230627_230648:cmsbot_crab_voRole
230627_230651:cmsbot_crab_voGroup
230627_230653:cmsbot_crab_scheddName
230627_230656:cmsbot_crab_collector
230627_230658:cmsbot_crab_extraJDL
```

Finished at: 2023-06-28 01:06:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/397/console)

## Comment (cmsdmwmbot, 2023-06-27T23:31:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-28 01:31:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/616/console

```
RETRY TESTS:
transferOutputs-check.sh 230627_230534:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 230627_230537:cmsbot_crab_transferLogs - 2
activity-check.sh 230627_230539:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 230627_230545:cmsbot_crab_disableAutomaticOutputCollection - 2
outputFiles-check.sh 230627_230547:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 230627_230552:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 230627_230555:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 230627_230558:cmsbot_crab_numCores - 2
scriptExe-check.sh 230627_230600:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 230627_230603:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 230627_230624:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230627_230627:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230627_230630:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230627_230633:cmsbot_crab_runRange - 2
whitelist-check.sh 230627_230641:cmsbot_crab_whitelist - 2
blacklist-check.sh 230627_230643:cmsbot_crab_blacklist - 2
voRole-check.sh 230627_230648:cmsbot_crab_voRole - 2
extraJDL-check.sh 230627_230658:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230542:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230550:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230606:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230613:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230616:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_230653:cmsbot_crab_scheddName - 0
collector-check.sh 230627_230656:cmsbot_crab_collector - 0

FAILED TESTS:
useParent-check.sh 230627_230619:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230627_230621:cmsbot_crab_secondaryInputDataset - 1
ignoreLocality-check.sh 230627_230636:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_230638:cmsbot_crab_userInputFiles - 1
ignoreGlobalBlacklist-check.sh 230627_230646:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 230627_230651:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2023-06-27T23:55:17Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-28 01:55:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/620/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
inputFiles-check.sh 230627_230542:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230627_230550:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230627_230606:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230627_230613:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230627_230616:cmsbot_crab_inputDBS - 0
scheddName-check.sh 230627_230653:cmsbot_crab_scheddName - 0
collector-check.sh 230627_230656:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 230627_230534:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 230627_230537:cmsbot_crab_transferLogs - 1
activity-check.sh 230627_230539:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230627_230545:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230627_230547:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230627_230552:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230627_230555:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230627_230558:cmsbot_crab_numCores - 1
scriptExe-check.sh 230627_230600:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 230627_230603:cmsbot_crab_scriptArgs - 1
useParent-check.sh 230627_230619:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230627_230621:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230627_230624:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230627_230627:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230627_230630:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 230627_230633:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 230627_230636:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 230627_230638:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 230627_230641:cmsbot_crab_whitelist - 1
blacklist-check.sh 230627_230643:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230627_230646:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230627_230648:cmsbot_crab_voRole - 1
voGroup-check.sh 230627_230651:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230627_230658:cmsbot_crab_extraJDL - 1
```
