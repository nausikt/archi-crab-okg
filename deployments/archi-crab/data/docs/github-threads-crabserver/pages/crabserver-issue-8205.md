# dmwm/CRABServer issue #8205: #689: Test prod CRABClient using test2 REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-01-30T20:45:53Z
Closed: 2024-01-31T13:58:10Z
URL: https://github.com/dmwm/CRABServer/issues/8205

## Opening post (cmsdmwmbot, 2024-01-30T20:45:53Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:45:52
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/689/)

## Comment (cmsdmwmbot, 2024-01-30T20:46:58Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_204608:cmsbot_crab_transferOutputs
240130_204609:cmsbot_crab_transferLogs
240130_204610:cmsbot_crab_activity
240130_204611:cmsbot_crab_inputFiles
240130_204611:cmsbot_crab_disableAutomaticOutputCollection
240130_204612:cmsbot_crab_outputFiles
240130_204613:cmsbot_crab_allowUndistributedCMSSW
240130_204614:cmsbot_crab_maxMemoryMB
240130_204615:cmsbot_crab_maxJobRuntimeMin
240130_204615:cmsbot_crab_numCores
240130_204616:cmsbot_crab_scriptExe
240130_204617:cmsbot_crab_scriptArgs
240130_204618:cmsbot_crab_sendVenvFolder
240130_204621:cmsbot_crab_sendExternalFolder
240130_204623:cmsbot_crab_inputDBS
240130_204624:cmsbot_crab_useParent
240130_204625:cmsbot_crab_secondaryInputDataset
240130_204625:cmsbot_crab_lumiMaskFile
240130_204626:cmsbot_crab_lumiMaskUrl
240130_204628:cmsbot_crab_outLFNDirBase
240130_204629:cmsbot_crab_runRange
240130_204630:cmsbot_crab_ignoreLocality
240130_204630:cmsbot_crab_userInputFiles
240130_204631:cmsbot_crab_whitelist
240130_204632:cmsbot_crab_blacklist
240130_204633:cmsbot_crab_ignoreGlobalBlacklist
240130_204633:cmsbot_crab_voRole
240130_204634:cmsbot_crab_voGroup
240130_204635:cmsbot_crab_scheddName
240130_204636:cmsbot_crab_collector
240130_204637:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_204608:cmsbot_crab_20240130_214606
```

Finished at: 2024-01-30 21:46:37
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/689/console)

## Comment (cmsdmwmbot, 2024-01-30T21:12:49Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-30 22:12:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/503/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/503//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214606  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-01-30T21:18:27Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-30 22:18:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/900/console

```
RETRY TESTS:
scriptExe-check.sh 240130_204616:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 240130_204617:cmsbot_crab_scriptArgs - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204608:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204611:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204611:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_204613:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204618:cmsbot_crab_sendVenvFolder - 0

FAILED TESTS:
transferLogs-check.sh 240130_204609:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204610:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_204612:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204614:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204615:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204615:cmsbot_crab_numCores - 1
sendExternalFolder-check.sh 240130_204621:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_204623:cmsbot_crab_inputDBS - 1
useParent-check.sh 240130_204624:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240130_204625:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240130_204625:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204626:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204628:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204629:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204630:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204630:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204631:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204632:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204633:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204633:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204634:cmsbot_crab_voGroup - 1
scheddName-check.sh 240130_204635:cmsbot_crab_scheddName - 1
collector-check.sh 240130_204636:cmsbot_crab_collector - 1
extraJDL-check.sh 240130_204637:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T21:41:59Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-30 22:41:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/903/console

```
RETRY TESTS:
extraJDL-check.sh 240130_204637:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204608:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204611:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204611:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_204613:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204618:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_204621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_204623:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_204624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_204625:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_204635:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204636:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_204609:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204610:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_204612:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204614:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204615:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204615:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204616:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204617:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240130_204625:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204626:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204628:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204629:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204630:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204630:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204631:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204632:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204633:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204633:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204634:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-01-30T22:05:59Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 23:05:58
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/906/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204608:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204611:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204611:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_204613:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204618:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_204621:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_204623:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_204624:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_204625:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_204635:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204636:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_204609:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204610:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_204612:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204614:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204615:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204615:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204616:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204617:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240130_204625:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204626:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204628:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204629:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204630:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204630:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204631:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204632:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204633:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204633:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204634:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204637:cmsbot_crab_extraJDL - 1
```
