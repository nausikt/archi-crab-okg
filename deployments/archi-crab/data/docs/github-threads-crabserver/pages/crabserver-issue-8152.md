# dmwm/CRABServer issue #8152: #659: Test dev CRABClient using preprod REST instance and CMSSW_8_0_36 CMSSW release

State: closed
Opened: 2024-01-11T17:41:09Z
Closed: 2024-01-11T19:59:14Z
URL: https://github.com/dmwm/CRABServer/issues/8152

## Opening post (cmsdmwmbot, 2024-01-11T17:41:09Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_8_0_36**
- SCRAM_ARCH: **slc7_amd64_gcc530**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:41:09
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/659/)

## Comment (cmsdmwmbot, 2024-01-11T17:42:58Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_174129:cmsbot_crab_transferOutputs
240111_174131:cmsbot_crab_transferLogs
240111_174133:cmsbot_crab_activity
240111_174136:cmsbot_crab_inputFiles
240111_174139:cmsbot_crab_disableAutomaticOutputCollection
240111_174142:cmsbot_crab_outputFiles
240111_174144:cmsbot_crab_allowUndistributedCMSSW
240111_174146:cmsbot_crab_maxMemoryMB
240111_174148:cmsbot_crab_maxJobRuntimeMin
240111_174151:cmsbot_crab_numCores
240111_174153:cmsbot_crab_scriptExe
240111_174155:cmsbot_crab_scriptArgs
240111_174158:cmsbot_crab_sendVenvFolder
240111_174204:cmsbot_crab_sendExternalFolder
240111_174205:cmsbot_crab_inputDBS
240111_174207:cmsbot_crab_useParent
240111_174209:cmsbot_crab_secondaryInputDataset
240111_174211:cmsbot_crab_lumiMaskFile
240111_174212:cmsbot_crab_lumiMaskUrl
240111_174215:cmsbot_crab_outLFNDirBase
240111_174216:cmsbot_crab_runRange
240111_174217:cmsbot_crab_ignoreLocality
240111_174218:cmsbot_crab_userInputFiles
240111_174221:cmsbot_crab_whitelist
240111_174223:cmsbot_crab_blacklist
240111_174225:cmsbot_crab_ignoreGlobalBlacklist
240111_174228:cmsbot_crab_voRole
240111_174230:cmsbot_crab_voGroup
240111_174232:cmsbot_crab_scheddName
240111_174234:cmsbot_crab_collector
240111_174236:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_174127:cmsbot_crab_20240111_184124
```

Finished at: 2024-01-11 18:42:37
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/659/console)

## Comment (cmsdmwmbot, 2024-01-11T18:07:48Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-11 19:07:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/476/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/476//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_184124  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-11T18:12:44Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:12:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/853/console

```
RETRY TESTS:
transferOutputs-check.sh 240111_174129:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240111_174131:cmsbot_crab_transferLogs - 2
activity-check.sh 240111_174133:cmsbot_crab_activity - 2
maxMemoryMB-check.sh 240111_174146:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240111_174148:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240111_174153:cmsbot_crab_scriptExe - 2
lumiMaskUrl-check.sh 240111_174212:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240111_174215:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240111_174216:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_174221:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_174223:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 240111_174225:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240111_174136:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174139:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174142:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174144:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240111_174151:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_174155:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174158:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174204:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174205:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174207:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174209:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174211:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240111_174217:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174218:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240111_174228:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174230:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174232:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174234:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174236:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:37:06Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:37:05
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/862/console

```
RETRY TESTS:
outLFNDirBase-check.sh 240111_174215:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240111_174216:cmsbot_crab_runRange - 2
blacklist-check.sh 240111_174223:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174129:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174131:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174133:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174136:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174139:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174142:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174144:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174146:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174148:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174151:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174153:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174155:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174158:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174204:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174205:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174207:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174209:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174211:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174212:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240111_174217:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174218:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174221:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174225:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174228:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174230:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174232:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174234:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174236:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:01:57Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 20:01:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/870/console

```
RETRY TESTS:
blacklist-check.sh 240111_174223:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174129:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174131:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174133:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174136:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174139:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174142:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174144:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174146:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174148:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174151:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174153:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174155:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174158:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174204:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174205:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174207:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174209:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174211:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174212:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_174215:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174216:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174217:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174218:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174221:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_174225:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174228:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174230:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174232:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174234:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174236:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:23:17Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:23:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/876/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_174129:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_174131:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_174133:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_174136:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_174139:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_174142:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_174144:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_174146:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_174148:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_174151:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_174153:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_174155:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_174158:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_174204:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_174205:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_174207:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_174209:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_174211:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_174212:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_174215:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_174216:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_174217:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_174218:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_174221:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_174223:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_174225:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_174228:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_174230:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_174232:cmsbot_crab_scheddName - 0
collector-check.sh 240111_174234:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_174236:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:57:21Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 20:57:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/482/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/482//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (belforte, 2024-01-11T19:59:14Z)

All OK
