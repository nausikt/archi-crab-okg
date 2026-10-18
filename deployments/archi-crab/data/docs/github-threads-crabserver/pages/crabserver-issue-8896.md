# dmwm/CRABServer issue #8896: #930: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2025-01-28T22:19:53Z
Closed: 2025-01-29T08:23:10Z
URL: https://github.com/dmwm/CRABServer/issues/8896

## Opening post (cmsdmwmbot, 2025-01-28T22:19:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2025-01-28 23:19:51
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/930/)

## Comment (cmsdmwmbot, 2025-01-28T22:22:35Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250128_222037:cmsbot_crab_20250128_232035
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
250128_222041:cmsbot_crab_transferOutputs
250128_222044:cmsbot_crab_transferLogs
250128_222047:cmsbot_crab_activity
250128_222051:cmsbot_crab_inputFiles
250128_222054:cmsbot_crab_disableAutomaticOutputCollection
250128_222057:cmsbot_crab_outputFiles
250128_222100:cmsbot_crab_allowUndistributedCMSSW
250128_222103:cmsbot_crab_maxMemoryMB
250128_222106:cmsbot_crab_maxJobRuntimeMin
250128_222110:cmsbot_crab_numCores
250128_222113:cmsbot_crab_scriptExe
250128_222116:cmsbot_crab_scriptArgs
250128_222119:cmsbot_crab_sendVenvFolder
250128_222122:cmsbot_crab_sendExternalFolder
250128_222125:cmsbot_crab_inputDBS
250128_222128:cmsbot_crab_useParent
250128_222131:cmsbot_crab_secondaryInputDataset
250128_222134:cmsbot_crab_lumiMaskFile
250128_222138:cmsbot_crab_lumiMaskUrl
250128_222142:cmsbot_crab_outLFNDirBase
250128_222145:cmsbot_crab_runRange
250128_222148:cmsbot_crab_ignoreLocality
250128_222151:cmsbot_crab_userInputFiles
250128_222154:cmsbot_crab_whitelist
250128_222157:cmsbot_crab_blacklist
250128_222200:cmsbot_crab_ignoreGlobalBlacklist
250128_222204:cmsbot_crab_voRole
250128_222207:cmsbot_crab_scheddName
250128_222210:cmsbot_crab_collector
250128_222213:cmsbot_crab_extraJDL
```

Finished at: 2025-01-28 23:22:13
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/930/console)

## Comment (cmsdmwmbot, 2025-01-28T22:46:01Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2025-01-28 23:45:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/597/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/597//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2025-01-28T22:46:41Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2025-01-28 23:46:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1267/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250128_222041:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250128_222044:cmsbot_crab_transferLogs - 0
activity-check.sh 250128_222047:cmsbot_crab_activity - 0
inputFiles-check.sh 250128_222051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250128_222054:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250128_222057:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250128_222100:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250128_222103:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250128_222106:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250128_222110:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 250128_222119:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250128_222122:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250128_222125:cmsbot_crab_inputDBS - 0
useParent-check.sh 250128_222128:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 250128_222134:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 250128_222148:cmsbot_crab_ignoreLocality - 0
blacklist-check.sh 250128_222157:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250128_222200:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 250128_222207:cmsbot_crab_scheddName - 0
collector-check.sh 250128_222210:cmsbot_crab_collector - 0
extraJDL-check.sh 250128_222213:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptExe-check.sh 250128_222113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250128_222116:cmsbot_crab_scriptArgs - 1

RETRY TESTS:
secondaryInputDataset-check.sh 250128_222131:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 250128_222138:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 250128_222142:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 250128_222145:cmsbot_crab_runRange - 2
userInputFiles-check.sh 250128_222151:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 250128_222154:cmsbot_crab_whitelist - 2
voRole-check.sh 250128_222204:cmsbot_crab_voRole - 2
```

## Comment (cmsdmwmbot, 2025-01-28T23:10:50Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2025-01-29 00:10:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1268/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250128_222041:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250128_222044:cmsbot_crab_transferLogs - 0
activity-check.sh 250128_222047:cmsbot_crab_activity - 0
inputFiles-check.sh 250128_222051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250128_222054:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250128_222057:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250128_222100:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250128_222103:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250128_222106:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250128_222110:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 250128_222119:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250128_222122:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250128_222125:cmsbot_crab_inputDBS - 0
useParent-check.sh 250128_222128:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250128_222131:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250128_222134:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250128_222138:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250128_222142:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 250128_222148:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250128_222151:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250128_222154:cmsbot_crab_whitelist - 0
blacklist-check.sh 250128_222157:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250128_222200:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250128_222204:cmsbot_crab_voRole - 0
scheddName-check.sh 250128_222207:cmsbot_crab_scheddName - 0
collector-check.sh 250128_222210:cmsbot_crab_collector - 0
extraJDL-check.sh 250128_222213:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptExe-check.sh 250128_222113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250128_222116:cmsbot_crab_scriptArgs - 1

RETRY TESTS:
runRange-check.sh 250128_222145:cmsbot_crab_runRange - 2
```

## Comment (cmsdmwmbot, 2025-01-28T23:34:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2025-01-29 00:34:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1269/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250128_222041:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250128_222044:cmsbot_crab_transferLogs - 0
activity-check.sh 250128_222047:cmsbot_crab_activity - 0
inputFiles-check.sh 250128_222051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250128_222054:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250128_222057:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250128_222100:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250128_222103:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250128_222106:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250128_222110:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 250128_222119:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250128_222122:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250128_222125:cmsbot_crab_inputDBS - 0
useParent-check.sh 250128_222128:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250128_222131:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250128_222134:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250128_222138:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250128_222142:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 250128_222148:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250128_222151:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250128_222154:cmsbot_crab_whitelist - 0
blacklist-check.sh 250128_222157:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250128_222200:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250128_222204:cmsbot_crab_voRole - 0
scheddName-check.sh 250128_222207:cmsbot_crab_scheddName - 0
collector-check.sh 250128_222210:cmsbot_crab_collector - 0
extraJDL-check.sh 250128_222213:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptExe-check.sh 250128_222113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250128_222116:cmsbot_crab_scriptArgs - 1

RETRY TESTS:
runRange-check.sh 250128_222145:cmsbot_crab_runRange - 2
```

## Comment (cmsdmwmbot, 2025-01-28T23:58:51Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2025-01-29 00:58:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1270/console

```
SUCCESSFUL TESTS:
transferOutputs-check.sh 250128_222041:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 250128_222044:cmsbot_crab_transferLogs - 0
activity-check.sh 250128_222047:cmsbot_crab_activity - 0
inputFiles-check.sh 250128_222051:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 250128_222054:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 250128_222057:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 250128_222100:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 250128_222103:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 250128_222106:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 250128_222110:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 250128_222119:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 250128_222122:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 250128_222125:cmsbot_crab_inputDBS - 0
useParent-check.sh 250128_222128:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 250128_222131:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 250128_222134:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 250128_222138:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 250128_222142:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 250128_222145:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 250128_222148:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 250128_222151:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 250128_222154:cmsbot_crab_whitelist - 0
blacklist-check.sh 250128_222157:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 250128_222200:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 250128_222204:cmsbot_crab_voRole - 0
scheddName-check.sh 250128_222207:cmsbot_crab_scheddName - 0
collector-check.sh 250128_222210:cmsbot_crab_collector - 0
extraJDL-check.sh 250128_222213:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptExe-check.sh 250128_222113:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250128_222116:cmsbot_crab_scriptArgs - 1

RETRY TESTS:
 none
```

## Comment (belforte, 2025-01-29T08:22:56Z)

as expected  only script* tests failed
