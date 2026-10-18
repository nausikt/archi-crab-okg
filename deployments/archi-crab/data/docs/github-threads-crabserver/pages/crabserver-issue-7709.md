# dmwm/CRABServer issue #7709: #418: Test dev CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-30T21:05:56Z
Closed: 2023-06-30T23:14:48Z
URL: https://github.com/dmwm/CRABServer/issues/7709

## Opening post (cmsdmwmbot, 2023-06-30T21:05:56Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-30 23:05:55
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/418/)

## Comment (cmsdmwmbot, 2023-06-30T21:07:24Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230630_210614:cmsbot_crab_transferOutputs
230630_210615:cmsbot_crab_transferLogs
230630_210617:cmsbot_crab_activity
230630_210618:cmsbot_crab_inputFiles
230630_210619:cmsbot_crab_disableAutomaticOutputCollection
230630_210621:cmsbot_crab_outputFiles
230630_210622:cmsbot_crab_allowUndistributedCMSSW
230630_210623:cmsbot_crab_maxMemoryMB
230630_210625:cmsbot_crab_maxJobRuntimeMin
230630_210626:cmsbot_crab_numCores
230630_210627:cmsbot_crab_scriptExe
230630_210628:cmsbot_crab_scriptArgs
230630_210630:cmsbot_crab_sendPythonFolder
230630_210638:cmsbot_crab_sendExternalFolder
230630_210639:cmsbot_crab_inputDBS
230630_210640:cmsbot_crab_useParent
230630_210641:cmsbot_crab_secondaryInputDataset
230630_210643:cmsbot_crab_lumiMaskFile
230630_210645:cmsbot_crab_lumiMaskUrl
230630_210647:cmsbot_crab_outLFNDirBase
230630_210649:cmsbot_crab_runRange
230630_210650:cmsbot_crab_ignoreLocality
230630_210651:cmsbot_crab_userInputFiles
230630_210653:cmsbot_crab_whitelist
230630_210655:cmsbot_crab_blacklist
230630_210656:cmsbot_crab_ignoreGlobalBlacklist
230630_210657:cmsbot_crab_voRole
230630_210658:cmsbot_crab_voGroup
230630_210700:cmsbot_crab_scheddName
230630_210701:cmsbot_crab_collector
230630_210702:cmsbot_crab_extraJDL
```

Finished at: 2023-06-30 23:07:03
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/418/console)

## Comment (cmsdmwmbot, 2023-06-30T21:29:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-30 23:29:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/666/console

```
RETRY TESTS:
scriptArgs-check.sh 230630_210628:cmsbot_crab_scriptArgs - 2
runRange-check.sh 230630_210649:cmsbot_crab_runRange - 2
whitelist-check.sh 230630_210653:cmsbot_crab_whitelist - 2
blacklist-check.sh 230630_210655:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 230630_210656:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 230630_210657:cmsbot_crab_voRole - 2
voGroup-check.sh 230630_210658:cmsbot_crab_voGroup - 2
extraJDL-check.sh 230630_210702:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_210614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_210615:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230630_210618:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230630_210622:cmsbot_crab_allowUndistributedCMSSW - 0
sendPythonFolder-check.sh 230630_210630:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_210638:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_210639:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 230630_210650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_210651:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 230630_210700:cmsbot_crab_scheddName - 0
collector-check.sh 230630_210701:cmsbot_crab_collector - 0

FAILED TESTS:
activity-check.sh 230630_210617:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230630_210619:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230630_210621:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230630_210623:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230630_210625:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230630_210626:cmsbot_crab_numCores - 1
scriptExe-check.sh 230630_210627:cmsbot_crab_scriptExe - 1
useParent-check.sh 230630_210640:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230630_210641:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230630_210643:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230630_210645:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230630_210647:cmsbot_crab_outLFNDirBase - 1
```

## Comment (cmsdmwmbot, 2023-06-30T21:53:05Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-30 23:53:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/668/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230630_210614:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230630_210615:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 230630_210618:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 230630_210622:cmsbot_crab_allowUndistributedCMSSW - 0
scriptArgs-check.sh 230630_210628:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230630_210630:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230630_210638:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230630_210639:cmsbot_crab_inputDBS - 0
runRange-check.sh 230630_210649:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230630_210650:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230630_210651:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230630_210653:cmsbot_crab_whitelist - 0
scheddName-check.sh 230630_210700:cmsbot_crab_scheddName - 0
collector-check.sh 230630_210701:cmsbot_crab_collector - 0

FAILED TESTS:
activity-check.sh 230630_210617:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 230630_210619:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 230630_210621:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 230630_210623:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 230630_210625:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 230630_210626:cmsbot_crab_numCores - 1
scriptExe-check.sh 230630_210627:cmsbot_crab_scriptExe - 1
useParent-check.sh 230630_210640:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 230630_210641:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 230630_210643:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 230630_210645:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 230630_210647:cmsbot_crab_outLFNDirBase - 1
blacklist-check.sh 230630_210655:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 230630_210656:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 230630_210657:cmsbot_crab_voRole - 1
voGroup-check.sh 230630_210658:cmsbot_crab_voGroup - 1
extraJDL-check.sh 230630_210702:cmsbot_crab_extraJDL - 1
```
