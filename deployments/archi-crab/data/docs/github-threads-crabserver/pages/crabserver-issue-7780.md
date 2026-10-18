# dmwm/CRABServer issue #7780: #446: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-07-20T14:14:02Z
Closed: 2023-07-21T13:27:54Z
URL: https://github.com/dmwm/CRABServer/issues/7780

## Opening post (cmsdmwmbot, 2023-07-20T14:14:02Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Configuration_Validation
Started at: 2023-07-20 16:14:02
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/446/)

## Comment (cmsdmwmbot, 2023-07-20T14:16:05Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230720_141420:cmsbot_crab_transferOutputs
230720_141422:cmsbot_crab_transferLogs
230720_141423:cmsbot_crab_activity
230720_141425:cmsbot_crab_inputFiles
230720_141426:cmsbot_crab_disableAutomaticOutputCollection
230720_141427:cmsbot_crab_outputFiles
230720_141429:cmsbot_crab_allowUndistributedCMSSW
230720_141430:cmsbot_crab_maxMemoryMB
230720_141431:cmsbot_crab_maxJobRuntimeMin
230720_141433:cmsbot_crab_numCores
230720_141434:cmsbot_crab_scriptExe
230720_141435:cmsbot_crab_scriptArgs
230720_141437:cmsbot_crab_sendPythonFolder
230720_141519:cmsbot_crab_sendExternalFolder
230720_141520:cmsbot_crab_inputDBS
230720_141521:cmsbot_crab_useParent
230720_141523:cmsbot_crab_secondaryInputDataset
230720_141524:cmsbot_crab_lumiMaskFile
230720_141526:cmsbot_crab_lumiMaskUrl
230720_141528:cmsbot_crab_outLFNDirBase
230720_141529:cmsbot_crab_runRange
230720_141531:cmsbot_crab_ignoreLocality
230720_141532:cmsbot_crab_userInputFiles
230720_141533:cmsbot_crab_whitelist
230720_141535:cmsbot_crab_blacklist
230720_141536:cmsbot_crab_ignoreGlobalBlacklist
230720_141537:cmsbot_crab_voRole
230720_141539:cmsbot_crab_voGroup
230720_141540:cmsbot_crab_scheddName
230720_141541:cmsbot_crab_collector
230720_141543:cmsbot_crab_extraJDL
```

Finished at: 2023-07-20 16:15:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/446/console)

## Comment (cmsdmwmbot, 2023-07-20T14:38:49Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-07-20 16:38:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/756/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 2
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T15:02:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-07-20 17:02:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/757/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T15:24:58Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2023-07-20 17:24:57
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/758/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (belforte, 2023-07-20T15:27:52Z)

whitelist test failed because DESY is currently blacklisted. Not a problem

## Comment (cmsdmwmbot, 2023-07-20T15:47:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 4. Will run again.
**Finished at:** 2023-07-20 17:47:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/759/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-20T16:09:00Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 4. Exceeded configured retries. If needed restart manually.
**Finished at:** 2023-07-20 18:08:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/760/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (cmsdmwmbot, 2023-07-21T10:22:52Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 4 out of 0. Test failed. Investigate manually
**Finished at:** 2023-07-21 12:22:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/766/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230720_141420:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230720_141422:cmsbot_crab_transferLogs - 0
activity-check.sh 230720_141423:cmsbot_crab_activity - 0
inputFiles-check.sh 230720_141425:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230720_141426:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230720_141427:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230720_141429:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230720_141430:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230720_141431:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230720_141433:cmsbot_crab_numCores - 0
scriptExe-check.sh 230720_141434:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230720_141435:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230720_141437:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230720_141519:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230720_141520:cmsbot_crab_inputDBS - 0
useParent-check.sh 230720_141521:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230720_141523:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230720_141524:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230720_141526:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230720_141528:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230720_141529:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230720_141531:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230720_141532:cmsbot_crab_userInputFiles - 0
blacklist-check.sh 230720_141535:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230720_141536:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230720_141537:cmsbot_crab_voRole - 0
voGroup-check.sh 230720_141539:cmsbot_crab_voGroup - 0
scheddName-check.sh 230720_141540:cmsbot_crab_scheddName - 0
collector-check.sh 230720_141541:cmsbot_crab_collector - 0
extraJDL-check.sh 230720_141543:cmsbot_crab_extraJDL - 0

FAILED TESTS:
whitelist-check.sh 230720_141533:cmsbot_crab_whitelist - 1
```

## Comment (belforte, 2023-07-21T13:27:54Z)

all OK
