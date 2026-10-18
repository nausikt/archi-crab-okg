# dmwm/CRABServer issue #8803: #880: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-21T11:18:56Z
Closed: 2024-11-25T20:16:33Z
URL: https://github.com/dmwm/CRABServer/issues/8803

## Opening post (cmsdmwmbot, 2024-11-21T11:18:56Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-21 12:18:55
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/880/)

## Comment (cmsdmwmbot, 2024-11-21T11:21:39Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241121_111927:cmsbot_crab_transferOutputs
241121_111930:cmsbot_crab_transferLogs
241121_111934:cmsbot_crab_activity
241121_111938:cmsbot_crab_inputFiles
241121_111942:cmsbot_crab_disableAutomaticOutputCollection
241121_111946:cmsbot_crab_outputFiles
241121_111949:cmsbot_crab_allowUndistributedCMSSW
241121_111952:cmsbot_crab_maxMemoryMB
241121_111956:cmsbot_crab_maxJobRuntimeMin
241121_112000:cmsbot_crab_numCores
241121_112004:cmsbot_crab_scriptExe
241121_112007:cmsbot_crab_scriptArgs
241121_112011:cmsbot_crab_sendVenvFolder
241121_112015:cmsbot_crab_sendExternalFolder
241121_112018:cmsbot_crab_inputDBS
241121_112022:cmsbot_crab_useParent
241121_112026:cmsbot_crab_secondaryInputDataset
241121_112029:cmsbot_crab_lumiMaskFile
241121_112033:cmsbot_crab_lumiMaskUrl
241121_112038:cmsbot_crab_outLFNDirBase
241121_112041:cmsbot_crab_runRange
241121_112045:cmsbot_crab_ignoreLocality
241121_112048:cmsbot_crab_userInputFiles
241121_112052:cmsbot_crab_whitelist
241121_112056:cmsbot_crab_blacklist
241121_112059:cmsbot_crab_ignoreGlobalBlacklist
241121_112103:cmsbot_crab_voRole
241121_112106:cmsbot_crab_voGroup
241121_112110:cmsbot_crab_scheddName
241121_112114:cmsbot_crab_collector
241121_112117:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241121_111922:cmsbot_crab_20241121_121920
```

Finished at: 2024-11-21 12:21:17
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/880/console)

## Comment (cmsdmwmbot, 2024-11-21T11:45:41Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-21 12:45:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/571/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/571//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241121_121920  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'killed', 'finished', 'failed'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241121_121920/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241121_111922:cmsbot_crab_20241121_121920  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241121_121920/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241121_121920/crab.log
```

## Comment (cmsdmwmbot, 2024-11-21T11:46:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-21 12:46:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1235/console

```
RETRY TESTS:
transferLogs-check.sh 241121_111930:cmsbot_crab_transferLogs - 2
activity-check.sh 241121_111934:cmsbot_crab_activity - 2
outputFiles-check.sh 241121_111946:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241121_111952:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241121_111956:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241121_112000:cmsbot_crab_numCores - 2
scriptArgs-check.sh 241121_112007:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 241121_112033:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241121_112038:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241121_112041:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241121_112048:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241121_112052:cmsbot_crab_whitelist - 2
blacklist-check.sh 241121_112056:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241121_112059:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241121_112103:cmsbot_crab_voRole - 2
voGroup-check.sh 241121_112106:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241121_111927:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241121_111938:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241121_111942:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241121_111949:cmsbot_crab_allowUndistributedCMSSW - 0
scriptExe-check.sh 241121_112004:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 241121_112011:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241121_112015:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241121_112018:cmsbot_crab_inputDBS - 0
useParent-check.sh 241121_112022:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241121_112026:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241121_112029:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241121_112045:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241121_112110:cmsbot_crab_scheddName - 0
collector-check.sh 241121_112114:cmsbot_crab_collector - 0
extraJDL-check.sh 241121_112117:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-21T12:11:39Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-21 13:11:37
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1236/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241121_111927:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241121_111930:cmsbot_crab_transferLogs - 0
activity-check.sh 241121_111934:cmsbot_crab_activity - 0
inputFiles-check.sh 241121_111938:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241121_111942:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241121_111946:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241121_111949:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241121_111952:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241121_111956:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241121_112000:cmsbot_crab_numCores - 0
scriptExe-check.sh 241121_112004:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241121_112007:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241121_112011:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241121_112015:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241121_112018:cmsbot_crab_inputDBS - 0
useParent-check.sh 241121_112022:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241121_112026:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241121_112029:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241121_112033:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241121_112038:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241121_112041:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241121_112045:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241121_112048:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241121_112052:cmsbot_crab_whitelist - 0
blacklist-check.sh 241121_112056:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241121_112059:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241121_112103:cmsbot_crab_voRole - 0
voGroup-check.sh 241121_112106:cmsbot_crab_voGroup - 0
scheddName-check.sh 241121_112110:cmsbot_crab_scheddName - 0
collector-check.sh 241121_112114:cmsbot_crab_collector - 0
extraJDL-check.sh 241121_112117:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-25T20:16:33Z)

usual problem with crab recover issued too soon
