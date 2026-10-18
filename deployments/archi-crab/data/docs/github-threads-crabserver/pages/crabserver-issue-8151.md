# dmwm/CRABServer issue #8151: #658: Test dev CRABClient using preprod REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2024-01-11T17:39:27Z
Closed: 2024-01-11T19:57:09Z
URL: https://github.com/dmwm/CRABServer/issues/8151

## Opening post (cmsdmwmbot, 2024-01-11T17:39:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:39:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/658/)

## Comment (cmsdmwmbot, 2024-01-11T17:41:01Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173952:cmsbot_crab_transferOutputs
240111_173953:cmsbot_crab_transferLogs
240111_173954:cmsbot_crab_activity
240111_173956:cmsbot_crab_inputFiles
240111_173957:cmsbot_crab_disableAutomaticOutputCollection
240111_174000:cmsbot_crab_outputFiles
240111_174001:cmsbot_crab_allowUndistributedCMSSW
240111_174002:cmsbot_crab_maxMemoryMB
240111_174003:cmsbot_crab_maxJobRuntimeMin
240111_174005:cmsbot_crab_numCores
240111_174006:cmsbot_crab_scriptExe
240111_174007:cmsbot_crab_scriptArgs
240111_174009:cmsbot_crab_sendVenvFolder
240111_174014:cmsbot_crab_sendExternalFolder
240111_174015:cmsbot_crab_inputDBS
240111_174016:cmsbot_crab_useParent
240111_174017:cmsbot_crab_secondaryInputDataset
240111_174018:cmsbot_crab_lumiMaskFile
240111_174019:cmsbot_crab_lumiMaskUrl
240111_174028:cmsbot_crab_outLFNDirBase
240111_174029:cmsbot_crab_runRange
240111_174030:cmsbot_crab_ignoreLocality
240111_174031:cmsbot_crab_userInputFiles
240111_174032:cmsbot_crab_whitelist
240111_174033:cmsbot_crab_blacklist
240111_174034:cmsbot_crab_ignoreGlobalBlacklist
240111_174035:cmsbot_crab_voRole
240111_174036:cmsbot_crab_voGroup
240111_174037:cmsbot_crab_scheddName
240111_174038:cmsbot_crab_collector
240111_174039:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_173951:cmsbot_crab_20240111_183948
```

Finished at: 2024-01-11 18:40:40
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/658/console)

## Comment (cmsdmwmbot, 2024-01-11T18:06:34Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-11 19:06:33
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/475/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/475//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183948  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-11T18:11:37Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:11:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/852/console

```
RETRY TESTS:
outputFiles-check.sh 240111_174000:cmsbot_crab_outputFiles - 2
lumiMaskUrl-check.sh 240111_174019:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_174029:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240111_174031:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240111_174032:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_174033:cmsbot_crab_blacklist - 2
voRole-check.sh 240111_174035:cmsbot_crab_voRole - 2
extraJDL-check.sh 240111_174039:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173953:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173954:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173956:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173957:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_174001:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174002:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174003:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174005:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174006:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174007:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174009:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174014:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174018:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_174028:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_174030:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 240111_174034:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240111_174036:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174037:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174038:cmsbot_crab_collector - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:35:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:35:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/861/console

```
RETRY TESTS:
outputFiles-check.sh 240111_174000:cmsbot_crab_outputFiles - 2
userInputFiles-check.sh 240111_174031:cmsbot_crab_userInputFiles - 2
blacklist-check.sh 240111_174033:cmsbot_crab_blacklist - 2
voRole-check.sh 240111_174035:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173953:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173954:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173956:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173957:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_174001:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174002:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174003:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174005:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174006:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174007:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174009:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174014:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174018:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174019:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_174028:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174029:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174030:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240111_174032:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174034:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 240111_174036:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174037:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174038:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:00:26Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 20:00:25
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/869/console

```
RETRY TESTS:
blacklist-check.sh 240111_174033:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173953:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173954:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173956:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173957:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174000:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174001:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174002:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174003:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174005:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174006:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174007:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174009:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174014:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174018:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174019:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_174028:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174029:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174030:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174031:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174032:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174034:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174035:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174036:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174037:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174038:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:21:52Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:21:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/875/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173952:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173953:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173954:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173956:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173957:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174000:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174001:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174002:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174003:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174005:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174006:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174007:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174009:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174014:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174015:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174016:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174017:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174018:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174019:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_174028:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174029:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174030:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174031:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174032:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174033:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174034:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174035:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174036:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174037:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174038:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174039:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:55:53Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 20:55:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/481/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/481//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (belforte, 2024-01-11T19:56:56Z)

all OK
