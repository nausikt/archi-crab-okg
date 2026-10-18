# dmwm/CRABServer issue #8761: #862: Test dev CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-01T12:36:13Z
Closed: 2024-11-01T14:27:48Z
URL: https://github.com/dmwm/CRABServer/issues/8761

## Opening post (cmsdmwmbot, 2024-11-01T12:36:13Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-01 13:36:12
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/862/)

## Comment (cmsdmwmbot, 2024-11-01T12:38:20Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241101_123634:cmsbot_crab_transferOutputs
241101_123637:cmsbot_crab_transferLogs
241101_123640:cmsbot_crab_activity
241101_123643:cmsbot_crab_inputFiles
241101_123645:cmsbot_crab_disableAutomaticOutputCollection
241101_123648:cmsbot_crab_outputFiles
241101_123651:cmsbot_crab_allowUndistributedCMSSW
241101_123654:cmsbot_crab_maxMemoryMB
241101_123656:cmsbot_crab_maxJobRuntimeMin
241101_123659:cmsbot_crab_numCores
241101_123702:cmsbot_crab_scriptExe
241101_123705:cmsbot_crab_scriptArgs
241101_123708:cmsbot_crab_sendVenvFolder
241101_123710:cmsbot_crab_sendExternalFolder
241101_123713:cmsbot_crab_inputDBS
241101_123716:cmsbot_crab_useParent
241101_123719:cmsbot_crab_secondaryInputDataset
241101_123722:cmsbot_crab_lumiMaskFile
241101_123727:cmsbot_crab_lumiMaskUrl
241101_123730:cmsbot_crab_outLFNDirBase
241101_123733:cmsbot_crab_runRange
241101_123735:cmsbot_crab_ignoreLocality
241101_123738:cmsbot_crab_userInputFiles
241101_123740:cmsbot_crab_whitelist
241101_123743:cmsbot_crab_blacklist
241101_123745:cmsbot_crab_ignoreGlobalBlacklist
241101_123748:cmsbot_crab_voRole
241101_123750:cmsbot_crab_voGroup
241101_123753:cmsbot_crab_scheddName
241101_123756:cmsbot_crab_collector
241101_123758:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241101_123631:cmsbot_crab_20241101_133630
```

Finished at: 2024-11-01 13:37:59
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/862/console)

## Comment (cmsdmwmbot, 2024-11-01T13:02:28Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-01 14:02:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/558/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/558//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241101_133630  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'finished', 'killed', 'failed'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241101_123631:cmsbot_crab_20241101_133630  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241101_133630/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
In order to recover a task, all the jobs need to be in a terminal state ({'failed', 'killed', 'finished'}). You have dict_keys(['transferring', 'finished'])
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/crab.log
```

## Comment (cmsdmwmbot, 2024-11-01T13:04:19Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-01 14:04:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1214/console

```
RETRY TESTS:
activity-check.sh 241101_123640:cmsbot_crab_activity - 2
outputFiles-check.sh 241101_123648:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 241101_123656:cmsbot_crab_maxJobRuntimeMin - 2
scriptArgs-check.sh 241101_123705:cmsbot_crab_scriptArgs - 2
lumiMaskUrl-check.sh 241101_123727:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241101_123730:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241101_123733:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241101_123738:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241101_123740:cmsbot_crab_whitelist - 2
blacklist-check.sh 241101_123743:cmsbot_crab_blacklist - 2
ignoreGlobalBlacklist-check.sh 241101_123745:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 241101_123748:cmsbot_crab_voRole - 2
voGroup-check.sh 241101_123750:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241101_123634:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241101_123637:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 241101_123643:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241101_123645:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241101_123651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241101_123654:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 241101_123659:cmsbot_crab_numCores - 0
scriptExe-check.sh 241101_123702:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 241101_123708:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241101_123710:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241101_123713:cmsbot_crab_inputDBS - 0
useParent-check.sh 241101_123716:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241101_123719:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241101_123722:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 241101_123735:cmsbot_crab_ignoreLocality - 0
scheddName-check.sh 241101_123753:cmsbot_crab_scheddName - 0
collector-check.sh 241101_123756:cmsbot_crab_collector - 0
extraJDL-check.sh 241101_123758:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-01T13:29:43Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-01 14:29:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1216/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241101_123634:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241101_123637:cmsbot_crab_transferLogs - 0
activity-check.sh 241101_123640:cmsbot_crab_activity - 0
inputFiles-check.sh 241101_123643:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241101_123645:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241101_123648:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241101_123651:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241101_123654:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241101_123656:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241101_123659:cmsbot_crab_numCores - 0
scriptExe-check.sh 241101_123702:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241101_123705:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241101_123708:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241101_123710:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241101_123713:cmsbot_crab_inputDBS - 0
useParent-check.sh 241101_123716:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241101_123719:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241101_123722:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241101_123727:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241101_123730:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241101_123733:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241101_123735:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241101_123738:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241101_123740:cmsbot_crab_whitelist - 0
blacklist-check.sh 241101_123743:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241101_123745:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241101_123748:cmsbot_crab_voRole - 0
voGroup-check.sh 241101_123750:cmsbot_crab_voGroup - 0
scheddName-check.sh 241101_123753:cmsbot_crab_scheddName - 0
collector-check.sh 241101_123756:cmsbot_crab_collector - 0
extraJDL-check.sh 241101_123758:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2024-11-01T14:21:20Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-01 15:21:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/559/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/559//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20241101_133630  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Getting input files into tmp dir /tmp/tmpl8wn627s
Can only execute from tasks in status SUBMITTED or UPLOADED. Current status is KILLED


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241101_133630  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Will save lumi files into output directory /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results
Summary from jobs in status 'finished':
  Number of files processed: 1
  Number of events read: 600
  Number of events written in EDM files: 600
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
Summary from output datasets in DBS:
  Number of events:
    /GenericTTbar/cmsbot-CRAB3_analysis-2411-94ba0e06145abd65ccb1d21786dc7e1d/USER: 6600
  Output datasets lumis written to outputDatasetsLumis.json
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
stepReport() - all lumis have been published in the output dataset. crab recover will exit
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
recover process prematurely exited during report step
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/crab.log


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241101_123631:cmsbot_crab_20241101_133630  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241101_133630/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
Will save lumi files into output directory /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results
Summary from jobs in status 'finished':
  Number of files processed: 1
  Number of events read: 600
  Number of events written in EDM files: 600
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
Summary from output datasets in DBS:
  Number of events:
    /GenericTTbar/cmsbot-CRAB3_analysis-2411-94ba0e06145abd65ccb1d21786dc7e1d/USER: 6600
  Output datasets lumis written to outputDatasetsLumis.json
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
stepReport() - all lumis have been published in the output dataset. crab recover will exit
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
recover process prematurely exited during report step
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/crab.log
```

## Comment (belforte, 2024-11-01T14:27:41Z)

CV failures is a bug in client https://github.com/dmwm/CRABClient/issues/5344
