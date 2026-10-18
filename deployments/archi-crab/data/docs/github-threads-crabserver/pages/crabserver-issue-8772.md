# dmwm/CRABServer issue #8772: #872: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-07T11:47:58Z
Closed: 2024-11-18T14:57:00Z
URL: https://github.com/dmwm/CRABServer/issues/8772

## Opening post (cmsdmwmbot, 2024-11-07T11:47:58Z)

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
Started at: 2024-11-07 12:47:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/872/)

## Comment (cmsdmwmbot, 2024-11-07T11:50:40Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241107_114827:cmsbot_crab_transferOutputs
241107_114830:cmsbot_crab_transferLogs
241107_114834:cmsbot_crab_activity
241107_114838:cmsbot_crab_inputFiles
241107_114842:cmsbot_crab_disableAutomaticOutputCollection
241107_114846:cmsbot_crab_outputFiles
241107_114850:cmsbot_crab_allowUndistributedCMSSW
241107_114853:cmsbot_crab_maxMemoryMB
241107_114857:cmsbot_crab_maxJobRuntimeMin
241107_114901:cmsbot_crab_numCores
241107_114905:cmsbot_crab_scriptExe
241107_114909:cmsbot_crab_scriptArgs
241107_114912:cmsbot_crab_sendVenvFolder
241107_114916:cmsbot_crab_sendExternalFolder
241107_114919:cmsbot_crab_inputDBS
241107_114923:cmsbot_crab_useParent
241107_114927:cmsbot_crab_secondaryInputDataset
241107_114930:cmsbot_crab_lumiMaskFile
241107_114934:cmsbot_crab_lumiMaskUrl
241107_114939:cmsbot_crab_outLFNDirBase
241107_114942:cmsbot_crab_runRange
241107_114946:cmsbot_crab_ignoreLocality
241107_114949:cmsbot_crab_userInputFiles
241107_114953:cmsbot_crab_whitelist
241107_114957:cmsbot_crab_blacklist
241107_115000:cmsbot_crab_ignoreGlobalBlacklist
241107_115004:cmsbot_crab_voRole
241107_115007:cmsbot_crab_voGroup
241107_115011:cmsbot_crab_scheddName
241107_115015:cmsbot_crab_collector
241107_115018:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241107_114823:cmsbot_crab_20241107_124821
```

Finished at: 2024-11-07 12:50:19
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/872/console)

## Comment (cmsdmwmbot, 2024-11-07T12:14:42Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-07 13:14:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/566/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/566//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241107_124821  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_124821/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241107_114823:cmsbot_crab_20241107_124821  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241107_124821/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241107_124821/crab.log
```

## Comment (cmsdmwmbot, 2024-11-07T12:15:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-07 13:15:20
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1224/console

```
RETRY TESTS:
transferLogs-check.sh 241107_114830:cmsbot_crab_transferLogs - 2
activity-check.sh 241107_114834:cmsbot_crab_activity - 2
outputFiles-check.sh 241107_114846:cmsbot_crab_outputFiles - 2
numCores-check.sh 241107_114901:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 241107_114930:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241107_114934:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241107_114939:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241107_114942:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241107_114949:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241107_114953:cmsbot_crab_whitelist - 2
blacklist-check.sh 241107_114957:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241107_115000:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241107_115004:cmsbot_crab_voRole - 2
voGroup-check.sh 241107_115007:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241107_114827:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241107_114838:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241107_114842:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241107_114850:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241107_114853:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241107_114857:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 241107_114905:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241107_114909:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241107_114912:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241107_114916:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241107_114919:cmsbot_crab_inputDBS - 0
useParent-check.sh 241107_114923:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241107_114927:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241107_114946:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241107_115011:cmsbot_crab_scheddName - 0
collector-check.sh 241107_115015:cmsbot_crab_collector - 0
extraJDL-check.sh 241107_115018:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-07T12:39:41Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-07 13:39:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1225/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241107_114827:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241107_114830:cmsbot_crab_transferLogs - 0
activity-check.sh 241107_114834:cmsbot_crab_activity - 0
inputFiles-check.sh 241107_114838:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241107_114842:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241107_114846:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241107_114850:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241107_114853:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241107_114857:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241107_114901:cmsbot_crab_numCores - 0
scriptExe-check.sh 241107_114905:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241107_114909:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241107_114912:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241107_114916:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241107_114919:cmsbot_crab_inputDBS - 0
useParent-check.sh 241107_114923:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241107_114927:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241107_114930:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241107_114934:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241107_114939:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241107_114942:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241107_114946:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241107_114949:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241107_114953:cmsbot_crab_whitelist - 0
blacklist-check.sh 241107_114957:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241107_115000:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241107_115004:cmsbot_crab_voRole - 0
voGroup-check.sh 241107_115007:cmsbot_crab_voGroup - 0
scheddName-check.sh 241107_115011:cmsbot_crab_scheddName - 0
collector-check.sh 241107_115015:cmsbot_crab_collector - 0
extraJDL-check.sh 241107_115018:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
