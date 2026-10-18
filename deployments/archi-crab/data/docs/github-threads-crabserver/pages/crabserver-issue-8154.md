# dmwm/CRABServer issue #8154: #661: Test dev CRABClient using preprod REST instance and CMSSW_7_1_29 CMSSW release

State: closed
Opened: 2024-01-11T17:45:24Z
Closed: 2024-01-11T19:51:56Z
URL: https://github.com/dmwm/CRABServer/issues/8154

## Opening post (cmsdmwmbot, 2024-01-11T17:45:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_7_1_29**
- SCRAM_ARCH: **slc6_amd64_gcc481**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:45:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/661/)

## Comment (cmsdmwmbot, 2024-01-11T17:47:10Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_174539:cmsbot_crab_transferOutputs
240111_174540:cmsbot_crab_transferLogs
240111_174541:cmsbot_crab_activity
240111_174543:cmsbot_crab_inputFiles
240111_174544:cmsbot_crab_disableAutomaticOutputCollection
240111_174546:cmsbot_crab_outputFiles
240111_174547:cmsbot_crab_allowUndistributedCMSSW
240111_174547:cmsbot_crab_maxMemoryMB
240111_174548:cmsbot_crab_maxJobRuntimeMin
240111_174550:cmsbot_crab_numCores
240111_174551:cmsbot_crab_scriptExe
240111_174552:cmsbot_crab_scriptArgs
240111_174554:cmsbot_crab_sendVenvFolder
240111_174633:cmsbot_crab_sendExternalFolder
240111_174634:cmsbot_crab_inputDBS
240111_174635:cmsbot_crab_useParent
240111_174635:cmsbot_crab_secondaryInputDataset
240111_174636:cmsbot_crab_lumiMaskFile
240111_174639:cmsbot_crab_outLFNDirBase
240111_174640:cmsbot_crab_runRange
240111_174641:cmsbot_crab_ignoreLocality
240111_174641:cmsbot_crab_userInputFiles
240111_174642:cmsbot_crab_whitelist
240111_174643:cmsbot_crab_blacklist
240111_174644:cmsbot_crab_ignoreGlobalBlacklist
240111_174645:cmsbot_crab_voRole
240111_174646:cmsbot_crab_voGroup
240111_174647:cmsbot_crab_scheddName
240111_174647:cmsbot_crab_collector
240111_174648:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_174538:cmsbot_crab_20240111_184536
```

Finished at: 2024-01-11 18:46:49
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/661/console)

## Comment (cmsdmwmbot, 2024-01-11T18:08:56Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 19:08:55
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/478/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/478//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-01-11T18:14:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:14:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/855/console

```
RETRY TESTS:
transferOutputs-check.sh 240111_174539:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240111_174540:cmsbot_crab_transferLogs - 2
activity-check.sh 240111_174541:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 240111_174544:cmsbot_crab_disableAutomaticOutputCollection - 2
maxMemoryMB-check.sh 240111_174547:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240111_174548:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240111_174550:cmsbot_crab_numCores - 2
scriptExe-check.sh 240111_174551:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240111_174552:cmsbot_crab_scriptArgs - 2
blacklist-check.sh 240111_174643:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240111_174644:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240111_174645:cmsbot_crab_voRole - 2
voGroup-check.sh 240111_174646:cmsbot_crab_voGroup - 2
extraJDL-check.sh 240111_174648:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240111_174543:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240111_174546:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174547:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240111_174554:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174634:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174635:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174636:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174639:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174641:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174641:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174642:cmsbot_crab_whitelist - 0
scheddName-check.sh 240111_174647:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174647:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:38:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:38:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/864/console

```
RETRY TESTS:
activity-check.sh 240111_174541:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 240111_174547:cmsbot_crab_maxMemoryMB - 2
numCores-check.sh 240111_174550:cmsbot_crab_numCores - 2
voRole-check.sh 240111_174645:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174539:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174540:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240111_174543:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174544:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174546:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174547:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240111_174548:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240111_174551:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174552:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174554:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174634:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174635:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174636:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174639:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174641:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174641:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174642:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174643:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174644:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240111_174646:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174647:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174647:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174648:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:03:55Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 20:03:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/872/console

```
RETRY TESTS:
numCores-check.sh 240111_174550:cmsbot_crab_numCores - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174539:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174540:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174541:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174543:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174544:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174546:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174547:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174547:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174548:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 240111_174551:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174552:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174554:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174634:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174635:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174636:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174639:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174641:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174641:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174642:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174643:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174644:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174645:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174646:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174647:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174647:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174648:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:25:09Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:25:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/878/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174539:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174540:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174541:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174543:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174544:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174546:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174547:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174547:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174548:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174550:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174551:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174552:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174554:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174633:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174634:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174635:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174635:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174636:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174639:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174640:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174641:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174641:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174642:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174643:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174644:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174645:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174646:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174647:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174647:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174648:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-01-11T19:51:20Z)

all OK
