# dmwm/CRABServer issue #8828: #894: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-11-25T22:10:24Z
Closed: 2024-11-26T08:42:16Z
URL: https://github.com/dmwm/CRABServer/issues/8828

## Opening post (cmsdmwmbot, 2024-11-25T22:10:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**
- CRABServer_tag: **v3.241125**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-25 23:10:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/894/)

## Comment (cmsdmwmbot, 2024-11-25T22:11:54Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241125_221057:cmsbot_crab_transferOutputs
241125_221058:cmsbot_crab_transferLogs
241125_221058:cmsbot_crab_activity
241125_221101:cmsbot_crab_inputFiles
241125_221102:cmsbot_crab_disableAutomaticOutputCollection
241125_221105:cmsbot_crab_outputFiles
241125_221105:cmsbot_crab_allowUndistributedCMSSW
241125_221106:cmsbot_crab_maxMemoryMB
241125_221107:cmsbot_crab_maxJobRuntimeMin
241125_221110:cmsbot_crab_numCores
241125_221110:cmsbot_crab_scriptExe
241125_221111:cmsbot_crab_scriptArgs
241125_221116:cmsbot_crab_sendVenvFolder
241125_221119:cmsbot_crab_sendExternalFolder
241125_221120:cmsbot_crab_inputDBS
241125_221120:cmsbot_crab_useParent
241125_221121:cmsbot_crab_secondaryInputDataset
241125_221122:cmsbot_crab_lumiMaskFile
241125_221123:cmsbot_crab_lumiMaskUrl
241125_221124:cmsbot_crab_outLFNDirBase
241125_221125:cmsbot_crab_runRange
241125_221126:cmsbot_crab_ignoreLocality
241125_221126:cmsbot_crab_userInputFiles
241125_221127:cmsbot_crab_whitelist
241125_221128:cmsbot_crab_blacklist
241125_221128:cmsbot_crab_ignoreGlobalBlacklist
241125_221129:cmsbot_crab_voRole
241125_221130:cmsbot_crab_voGroup
241125_221130:cmsbot_crab_scheddName
241125_221131:cmsbot_crab_collector
241125_221132:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241125_221056:cmsbot_crab_20241125_231053
```

Finished at: 2024-11-25 23:11:32
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/894/console)

## Comment (cmsdmwmbot, 2024-11-25T22:33:10Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-25 23:33:09
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1240/console

```
RETRY TESTS:
transferLogs-check.sh 241125_221058:cmsbot_crab_transferLogs - 2
activity-check.sh 241125_221058:cmsbot_crab_activity - 2
outputFiles-check.sh 241125_221105:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 241125_221107:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241125_221110:cmsbot_crab_numCores - 2
scriptExe-check.sh 241125_221110:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241125_221111:cmsbot_crab_scriptArgs - 2
useParent-check.sh 241125_221120:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 241125_221122:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241125_221123:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241125_221124:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241125_221125:cmsbot_crab_runRange - 2
whitelist-check.sh 241125_221127:cmsbot_crab_whitelist - 2
blacklist-check.sh 241125_221128:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241125_221128:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241125_221129:cmsbot_crab_voRole - 2
voGroup-check.sh 241125_221130:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221057:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241125_221101:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221102:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241125_221105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_221106:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 241125_221116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221120:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 241125_221121:cmsbot_crab_secondaryInputDataset - 0
userInputFiles-check.sh 241125_221126:cmsbot_crab_userInputFiles - 0
scheddName-check.sh 241125_221130:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221131:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221132:cmsbot_crab_extraJDL - 0

FAILED TESTS:
ignoreLocality-check.sh 241125_221126:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-11-25T22:34:17Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-25 23:34:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/573/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/573//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241125_231053  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['transferring']
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231053/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241125_221056:cmsbot_crab_20241125_231053  --instance=preprod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241125_231053/.requestcache not created, because it already exists.
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state (set(['failed', 'finished', 'killed'])). You have ['transferring']
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241125_231053/crab.log
```

## Comment (cmsdmwmbot, 2024-11-25T22:55:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-11-25 23:55:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1243/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 241125_221123:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241125_221124:cmsbot_crab_outLFNDirBase - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221057:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_221058:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_221058:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_221101:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221102:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_221105:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_221105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_221106:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_221107:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_221110:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_221110:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_221111:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_221116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221120:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_221120:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_221121:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_221122:cmsbot_crab_lumiMaskFile - 0
runRange-check.sh 241125_221125:cmsbot_crab_runRange - 0
userInputFiles-check.sh 241125_221126:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_221127:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_221128:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_221128:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_221129:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_221130:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_221130:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221131:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221132:cmsbot_crab_extraJDL - 0

FAILED TESTS:
ignoreLocality-check.sh 241125_221126:cmsbot_crab_ignoreLocality - 1
```

## Comment (cmsdmwmbot, 2024-11-25T23:17:26Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-11-26 00:17:24
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1246/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241125_221057:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241125_221058:cmsbot_crab_transferLogs - 0
activity-check.sh 241125_221058:cmsbot_crab_activity - 0
inputFiles-check.sh 241125_221101:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241125_221102:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241125_221105:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241125_221105:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241125_221106:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241125_221107:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241125_221110:cmsbot_crab_numCores - 0
scriptExe-check.sh 241125_221110:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241125_221111:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241125_221116:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241125_221119:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241125_221120:cmsbot_crab_inputDBS - 0
useParent-check.sh 241125_221120:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241125_221121:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241125_221122:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241125_221123:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241125_221124:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241125_221125:cmsbot_crab_runRange - 0
userInputFiles-check.sh 241125_221126:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241125_221127:cmsbot_crab_whitelist - 0
blacklist-check.sh 241125_221128:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241125_221128:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241125_221129:cmsbot_crab_voRole - 0
voGroup-check.sh 241125_221130:cmsbot_crab_voGroup - 0
scheddName-check.sh 241125_221130:cmsbot_crab_scheddName - 0
collector-check.sh 241125_221131:cmsbot_crab_collector - 0
extraJDL-check.sh 241125_221132:cmsbot_crab_extraJDL - 0

FAILED TESTS:
ignoreLocality-check.sh 241125_221126:cmsbot_crab_ignoreLocality - 1
```

## Comment (belforte, 2024-11-26T08:39:23Z)

failure was a submission problem with Rucio client https://github.com/rucio/rucio/issues/7185
