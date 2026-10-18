# dmwm/CRABServer issue #8150: #657: Test dev CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release

State: closed
Opened: 2024-01-11T17:38:13Z
Closed: 2024-01-11T19:56:01Z
URL: https://github.com/dmwm/CRABServer/issues/8150

## Opening post (cmsdmwmbot, 2024-01-11T17:38:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:38:11
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/657/)

## Comment (cmsdmwmbot, 2024-01-11T17:39:19Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173825:cmsbot_crab_transferOutputs
240111_173826:cmsbot_crab_transferLogs
240111_173827:cmsbot_crab_activity
240111_173828:cmsbot_crab_inputFiles
240111_173829:cmsbot_crab_disableAutomaticOutputCollection
240111_173830:cmsbot_crab_outputFiles
240111_173831:cmsbot_crab_allowUndistributedCMSSW
240111_173832:cmsbot_crab_maxMemoryMB
240111_173832:cmsbot_crab_maxJobRuntimeMin
240111_173833:cmsbot_crab_numCores
240111_173834:cmsbot_crab_scriptExe
240111_173835:cmsbot_crab_scriptArgs
240111_173836:cmsbot_crab_sendVenvFolder
240111_173840:cmsbot_crab_sendExternalFolder
240111_173841:cmsbot_crab_inputDBS
240111_173842:cmsbot_crab_useParent
240111_173843:cmsbot_crab_secondaryInputDataset
240111_173844:cmsbot_crab_lumiMaskFile
240111_173845:cmsbot_crab_lumiMaskUrl
240111_173847:cmsbot_crab_outLFNDirBase
240111_173848:cmsbot_crab_runRange
240111_173849:cmsbot_crab_ignoreLocality
240111_173850:cmsbot_crab_userInputFiles
240111_173851:cmsbot_crab_whitelist
240111_173851:cmsbot_crab_blacklist
240111_173852:cmsbot_crab_ignoreGlobalBlacklist
240111_173853:cmsbot_crab_voRole
240111_173854:cmsbot_crab_voGroup
240111_173855:cmsbot_crab_scheddName
240111_173856:cmsbot_crab_collector
240111_173857:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_173824:cmsbot_crab_20240111_183823
```

Finished at: 2024-01-11 18:38:58
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/657/console)

## Comment (cmsdmwmbot, 2024-01-11T18:05:17Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-11 19:05:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/474/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/474//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183823  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-11T18:10:18Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:10:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/851/console

```
RETRY TESTS:
outputFiles-check.sh 240111_173830:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240111_173832:cmsbot_crab_maxJobRuntimeMin - 2
scriptExe-check.sh 240111_173834:cmsbot_crab_scriptExe - 2
useParent-check.sh 240111_173842:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 240111_173843:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240111_173845:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240111_173848:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_173851:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173851:cmsbot_crab_blacklist - 2
voRole-check.sh 240111_173853:cmsbot_crab_voRole - 2
voGroup-check.sh 240111_173854:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173826:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173827:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173828:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173829:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173831:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173832:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240111_173833:cmsbot_crab_numCores - 0
scriptArgs-check.sh 240111_173835:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173836:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173840:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173841:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 240111_173844:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240111_173847:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_173849:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173850:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173852:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240111_173855:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173856:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173857:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:34:35Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:34:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/860/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 240111_173832:cmsbot_crab_maxJobRuntimeMin - 2
whitelist-check.sh 240111_173851:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173851:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173826:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173827:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173828:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173830:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173831:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173832:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 240111_173833:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173834:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173835:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173836:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173840:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173841:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173842:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173843:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173844:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173845:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173847:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173848:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173849:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173850:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173852:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173853:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173854:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173855:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173856:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173857:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:59:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-01-11 19:59:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/868/console

```
RETRY TESTS:
blacklist-check.sh 240111_173851:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173826:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173827:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173828:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173830:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173831:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173832:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173832:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173833:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173834:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173835:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173836:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173840:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173841:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173842:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173843:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173844:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173845:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173847:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173848:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173849:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173850:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173851:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240111_173852:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173853:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173854:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173855:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173856:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173857:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:20:27Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 3 out of 4. Test is done.
**Finished at:** 2024-01-11 20:20:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/874/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173825:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173826:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173827:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173828:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173829:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173830:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173831:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173832:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173832:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173833:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173834:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173835:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173836:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173840:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173841:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173842:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173843:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173844:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173845:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173847:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173848:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173849:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173850:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173851:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173851:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173852:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173853:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173854:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173855:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173856:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173857:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:52:03Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 20:52:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/479/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/479//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (belforte, 2024-01-11T19:56:01Z)

all OK
