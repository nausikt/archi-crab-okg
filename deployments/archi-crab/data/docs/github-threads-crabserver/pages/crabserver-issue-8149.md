# dmwm/CRABServer issue #8149: #656: Test dev CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-01-11T17:36:44Z
Closed: 2024-01-11T19:55:21Z
URL: https://github.com/dmwm/CRABServer/issues/8149

## Opening post (cmsdmwmbot, 2024-01-11T17:36:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-01-11 18:36:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/656/)

## Comment (cmsdmwmbot, 2024-01-11T17:38:04Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240111_173705:cmsbot_crab_transferOutputs
240111_173706:cmsbot_crab_transferLogs
240111_173707:cmsbot_crab_activity
240111_173709:cmsbot_crab_inputFiles
240111_173710:cmsbot_crab_disableAutomaticOutputCollection
240111_173712:cmsbot_crab_outputFiles
240111_173713:cmsbot_crab_allowUndistributedCMSSW
240111_173713:cmsbot_crab_maxMemoryMB
240111_173714:cmsbot_crab_maxJobRuntimeMin
240111_173716:cmsbot_crab_numCores
240111_173717:cmsbot_crab_scriptExe
240111_173718:cmsbot_crab_scriptArgs
240111_173720:cmsbot_crab_sendVenvFolder
240111_173726:cmsbot_crab_sendExternalFolder
240111_173727:cmsbot_crab_inputDBS
240111_173728:cmsbot_crab_useParent
240111_173729:cmsbot_crab_secondaryInputDataset
240111_173730:cmsbot_crab_lumiMaskFile
240111_173731:cmsbot_crab_lumiMaskUrl
240111_173732:cmsbot_crab_outLFNDirBase
240111_173733:cmsbot_crab_runRange
240111_173734:cmsbot_crab_ignoreLocality
240111_173735:cmsbot_crab_userInputFiles
240111_173736:cmsbot_crab_whitelist
240111_173737:cmsbot_crab_blacklist
240111_173738:cmsbot_crab_ignoreGlobalBlacklist
240111_173739:cmsbot_crab_voRole
240111_173740:cmsbot_crab_voGroup
240111_173740:cmsbot_crab_scheddName
240111_173741:cmsbot_crab_collector
240111_173742:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240111_173704:cmsbot_crab_20240111_183702
```

Finished at: 2024-01-11 18:37:43
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/656/console)

## Comment (cmsdmwmbot, 2024-01-11T18:03:35Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-11 19:03:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/473/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/473//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240111_183702  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-11T18:09:13Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-11 19:09:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/850/console

```
RETRY TESTS:
outputFiles-check.sh 240111_173712:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240111_173713:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240111_173714:cmsbot_crab_maxJobRuntimeMin - 2
useParent-check.sh 240111_173728:cmsbot_crab_useParent - 2
lumiMaskUrl-check.sh 240111_173731:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240111_173732:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240111_173733:cmsbot_crab_runRange - 2
whitelist-check.sh 240111_173736:cmsbot_crab_whitelist - 2
blacklist-check.sh 240111_173737:cmsbot_crab_blacklist - 2
voRole-check.sh 240111_173739:cmsbot_crab_voRole - 2
voGroup-check.sh 240111_173740:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173705:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173706:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173707:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173709:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173710:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240111_173713:cmsbot_crab_allowUndistributedCMSSW - 0
numCores-check.sh 240111_173716:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173717:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173718:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173726:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173727:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240111_173729:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173730:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 240111_173734:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173735:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 240111_173738:cmsbot_crab_ignoreGlobalBlacklist - 0
scheddName-check.sh 240111_173740:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173741:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:33:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-11 19:33:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/859/console

```
RETRY TESTS:
runRange-check.sh 240111_173733:cmsbot_crab_runRange - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173705:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173706:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173707:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173709:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173710:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173712:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173713:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173713:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173714:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173716:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173717:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173718:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173726:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173727:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173728:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173729:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173730:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173731:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173732:cmsbot_crab_outLFNDirBase - 0
ignoreLocality-check.sh 240111_173734:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173735:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173736:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173737:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173738:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173739:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173740:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173740:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173741:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T18:57:46Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2024-01-11 19:57:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/867/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240111_173705:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240111_173706:cmsbot_crab_transferLogs - 0
activity-check.sh 240111_173707:cmsbot_crab_activity - 0
inputFiles-check.sh 240111_173709:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240111_173710:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240111_173712:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240111_173713:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240111_173713:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240111_173714:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240111_173716:cmsbot_crab_numCores - 0
scriptExe-check.sh 240111_173717:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240111_173718:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240111_173720:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240111_173726:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240111_173727:cmsbot_crab_inputDBS - 0
useParent-check.sh 240111_173728:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240111_173729:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240111_173730:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240111_173731:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240111_173732:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240111_173733:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240111_173734:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240111_173735:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240111_173736:cmsbot_crab_whitelist - 0
blacklist-check.sh 240111_173737:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 240111_173738:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240111_173739:cmsbot_crab_voRole - 0
voGroup-check.sh 240111_173740:cmsbot_crab_voGroup - 0
scheddName-check.sh 240111_173740:cmsbot_crab_scheddName - 0
collector-check.sh 240111_173741:cmsbot_crab_collector - 0
extraJDL-check.sh 240111_173742:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-01-11T19:54:31Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-01-11 20:54:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/480/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/480//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (belforte, 2024-01-11T19:55:21Z)

all OK
