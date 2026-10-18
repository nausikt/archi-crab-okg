# dmwm/CRABServer issue #8758: #858: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-31T16:45:04Z
Closed: 2024-11-01T08:29:50Z
URL: https://github.com/dmwm/CRABServer/issues/8758

## Opening post (cmsdmwmbot, 2024-10-31T16:45:04Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-10-31 17:45:03
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/858/)

## Comment (cmsdmwmbot, 2024-10-31T16:47:18Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241031_164529:cmsbot_crab_transferOutputs
241031_164532:cmsbot_crab_transferLogs
241031_164535:cmsbot_crab_activity
241031_164538:cmsbot_crab_inputFiles
241031_164541:cmsbot_crab_disableAutomaticOutputCollection
241031_164544:cmsbot_crab_outputFiles
241031_164547:cmsbot_crab_allowUndistributedCMSSW
241031_164550:cmsbot_crab_maxMemoryMB
241031_164553:cmsbot_crab_maxJobRuntimeMin
241031_164556:cmsbot_crab_numCores
241031_164559:cmsbot_crab_scriptExe
241031_164601:cmsbot_crab_scriptArgs
241031_164604:cmsbot_crab_sendVenvFolder
241031_164607:cmsbot_crab_sendExternalFolder
241031_164611:cmsbot_crab_inputDBS
241031_164614:cmsbot_crab_useParent
241031_164616:cmsbot_crab_secondaryInputDataset
241031_164619:cmsbot_crab_lumiMaskFile
241031_164622:cmsbot_crab_lumiMaskUrl
241031_164625:cmsbot_crab_outLFNDirBase
241031_164628:cmsbot_crab_runRange
241031_164631:cmsbot_crab_ignoreLocality
241031_164634:cmsbot_crab_userInputFiles
241031_164636:cmsbot_crab_whitelist
241031_164639:cmsbot_crab_blacklist
241031_164642:cmsbot_crab_ignoreGlobalBlacklist
241031_164645:cmsbot_crab_voRole
241031_164648:cmsbot_crab_voGroup
241031_164650:cmsbot_crab_scheddName
241031_164653:cmsbot_crab_collector
241031_164656:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241031_164526:cmsbot_crab_20241031_174525
```

Finished at: 2024-10-31 17:46:57
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/858/console)

## Comment (cmsdmwmbot, 2024-10-31T17:12:20Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-10-31 18:12:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1211/console

```
RETRY TESTS:
transferLogs-check.sh 241031_164532:cmsbot_crab_transferLogs - 2
activity-check.sh 241031_164535:cmsbot_crab_activity - 2
outputFiles-check.sh 241031_164544:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 241031_164550:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241031_164553:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241031_164556:cmsbot_crab_numCores - 2
scriptExe-check.sh 241031_164559:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241031_164601:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241031_164619:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241031_164622:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241031_164625:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241031_164628:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 241031_164631:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 241031_164634:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241031_164636:cmsbot_crab_whitelist - 2
blacklist-check.sh 241031_164639:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241031_164642:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241031_164645:cmsbot_crab_voRole - 2
voGroup-check.sh 241031_164648:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241031_164529:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 241031_164538:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241031_164541:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241031_164547:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 241031_164604:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241031_164607:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241031_164611:cmsbot_crab_inputDBS - 0
useParent-check.sh 241031_164614:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241031_164616:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 241031_164650:cmsbot_crab_scheddName - 0
collector-check.sh 241031_164653:cmsbot_crab_collector - 0
extraJDL-check.sh 241031_164656:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-31T17:12:38Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-31 18:12:34
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/554/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/554//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241031_174525  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'finished', 'killed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241031_174525/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241031_164526:cmsbot_crab_20241031_174525  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241031_174525/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'finished', 'killed'}). You have dict_keys(['transferring'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241031_174525/crab.log
```

## Comment (cmsdmwmbot, 2024-10-31T17:37:23Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-10-31 18:37:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1212/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241031_164529:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241031_164532:cmsbot_crab_transferLogs - 0
activity-check.sh 241031_164535:cmsbot_crab_activity - 0
inputFiles-check.sh 241031_164538:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241031_164541:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241031_164544:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241031_164547:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241031_164550:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241031_164553:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241031_164556:cmsbot_crab_numCores - 0
scriptExe-check.sh 241031_164559:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241031_164601:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241031_164604:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241031_164607:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241031_164611:cmsbot_crab_inputDBS - 0
useParent-check.sh 241031_164614:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241031_164616:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241031_164619:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241031_164622:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241031_164625:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241031_164628:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241031_164631:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241031_164634:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241031_164636:cmsbot_crab_whitelist - 0
blacklist-check.sh 241031_164639:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241031_164642:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241031_164645:cmsbot_crab_voRole - 0
voGroup-check.sh 241031_164648:cmsbot_crab_voGroup - 0
scheddName-check.sh 241031_164650:cmsbot_crab_scheddName - 0
collector-check.sh 241031_164653:cmsbot_crab_collector - 0
extraJDL-check.sh 241031_164656:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-10-31T22:20:57Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-31 23:20:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/555/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/555//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20241031_174525  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Getting input files into tmp dir /tmp/tmplx0auh0o
Can only execute from tasks in status SUBMITTED or UPLOADED. Current status is KILLED


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241031_174525  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
All the jobs of the original task failed. Better investigate and submit it again than recover.
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241031_174525/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241031_164526:cmsbot_crab_20241031_174525  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241031_174525/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
All the jobs of the original task failed. Better investigate and submit it again than recover.
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241031_174525/crab.log
```

## Comment (belforte, 2024-11-01T08:29:50Z)

CV failed due to jobs not completed when it ran. try again in new test
