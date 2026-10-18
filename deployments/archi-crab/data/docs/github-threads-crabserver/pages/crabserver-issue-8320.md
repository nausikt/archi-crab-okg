# dmwm/CRABServer issue #8320: #749: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-05T14:26:26Z
Closed: 2024-04-05T15:20:40Z
URL: https://github.com/dmwm/CRABServer/issues/8320

## Opening post (cmsdmwmbot, 2024-04-05T14:26:26Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-04-05 16:26:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/749/)

## Comment (cmsdmwmbot, 2024-04-05T14:28:57Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240405_142721:cmsbot_crab_transferOutputs
240405_142723:cmsbot_crab_transferLogs
240405_142725:cmsbot_crab_activity
240405_142728:cmsbot_crab_inputFiles
240405_142730:cmsbot_crab_disableAutomaticOutputCollection
240405_142732:cmsbot_crab_outputFiles
240405_142734:cmsbot_crab_allowUndistributedCMSSW
240405_142737:cmsbot_crab_maxMemoryMB
240405_142739:cmsbot_crab_maxJobRuntimeMin
240405_142741:cmsbot_crab_numCores
240405_142743:cmsbot_crab_scriptExe
240405_142746:cmsbot_crab_scriptArgs
240405_142748:cmsbot_crab_sendVenvFolder
240405_142751:cmsbot_crab_sendExternalFolder
240405_142753:cmsbot_crab_inputDBS
240405_142755:cmsbot_crab_useParent
240405_142757:cmsbot_crab_secondaryInputDataset
240405_142759:cmsbot_crab_lumiMaskFile
240405_142801:cmsbot_crab_lumiMaskUrl
240405_142811:cmsbot_crab_outLFNDirBase
240405_142813:cmsbot_crab_runRange
240405_142815:cmsbot_crab_ignoreLocality
240405_142817:cmsbot_crab_userInputFiles
240405_142819:cmsbot_crab_whitelist
240405_142822:cmsbot_crab_blacklist
240405_142824:cmsbot_crab_ignoreGlobalBlacklist
240405_142826:cmsbot_crab_voRole
240405_142828:cmsbot_crab_voGroup
240405_142830:cmsbot_crab_scheddName
240405_142833:cmsbot_crab_collector
240405_142835:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240405_142710:cmsbot_crab_20240405_162708
```

Finished at: 2024-04-05 16:28:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/749/console)

## Comment (cmsdmwmbot, 2024-04-05T14:52:11Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-05 16:52:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/524/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/524//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-05T14:52:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-05 16:52:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1022/console

```
RETRY TESTS:
outputFiles-check.sh 240405_142732:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240405_142737:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240405_142739:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 240405_142746:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 240405_142801:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240405_142811:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240405_142813:cmsbot_crab_runRange - 2
whitelist-check.sh 240405_142819:cmsbot_crab_whitelist - 2
blacklist-check.sh 240405_142822:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240405_142824:cmsbot_crab_ignoreGlobalBlacklist - 2
voGroup-check.sh 240405_142828:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240405_142721:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240405_142723:cmsbot_crab_transferLogs - 0
activity-check.sh 240405_142725:cmsbot_crab_activity - 0
inputFiles-check.sh 240405_142728:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240405_142730:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240405_142734:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240405_142741:cmsbot_crab_numCores - 0
scriptExe-check.sh 240405_142743:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240405_142748:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240405_142751:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240405_142753:cmsbot_crab_inputDBS - 0
useParent-check.sh 240405_142755:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240405_142757:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240405_142759:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240405_142815:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240405_142817:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240405_142826:cmsbot_crab_voRole - 0
scheddName-check.sh 240405_142830:cmsbot_crab_scheddName - 0
collector-check.sh 240405_142833:cmsbot_crab_collector - 0
extraJDL-check.sh 240405_142835:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-04-05T15:17:01Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-04-05 17:17:00
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1025/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240405_142721:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240405_142723:cmsbot_crab_transferLogs - 0
activity-check.sh 240405_142725:cmsbot_crab_activity - 0
inputFiles-check.sh 240405_142728:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240405_142730:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240405_142732:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240405_142734:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240405_142737:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240405_142739:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240405_142741:cmsbot_crab_numCores - 0
scriptExe-check.sh 240405_142743:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240405_142746:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240405_142748:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240405_142751:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240405_142753:cmsbot_crab_inputDBS - 0
useParent-check.sh 240405_142755:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240405_142757:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240405_142759:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240405_142801:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240405_142811:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240405_142813:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240405_142815:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240405_142817:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240405_142819:cmsbot_crab_whitelist - 0
blacklist-check.sh 240405_142822:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240405_142824:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240405_142826:cmsbot_crab_voRole - 0
voGroup-check.sh 240405_142828:cmsbot_crab_voGroup - 0
scheddName-check.sh 240405_142830:cmsbot_crab_scheddName - 0
collector-check.sh 240405_142833:cmsbot_crab_collector - 0
extraJDL-check.sh 240405_142835:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-04-05T15:20:40Z)

OK
