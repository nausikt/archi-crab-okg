# dmwm/CRABServer issue #8312: #742: Test GH CRABClient using prod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-04-03T20:14:25Z
Closed: 2024-04-04T09:08:34Z
URL: https://github.com/dmwm/CRABServer/issues/8312

## Opening post (cmsdmwmbot, 2024-04-03T20:14:25Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-04-03 22:14:25
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/742/)

## Comment (cmsdmwmbot, 2024-04-03T20:17:32Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240403_201446:cmsbot_crab_transferOutputs
240403_201447:cmsbot_crab_transferLogs
240403_201449:cmsbot_crab_activity
240403_201452:cmsbot_crab_inputFiles
240403_201454:cmsbot_crab_disableAutomaticOutputCollection
240403_201457:cmsbot_crab_outputFiles
240403_201459:cmsbot_crab_allowUndistributedCMSSW
240403_201501:cmsbot_crab_maxMemoryMB
240403_201519:cmsbot_crab_maxJobRuntimeMin
240403_201522:cmsbot_crab_numCores
240403_201524:cmsbot_crab_scriptExe
240403_201542:cmsbot_crab_scriptArgs
240403_201553:cmsbot_crab_sendVenvFolder
240403_201557:cmsbot_crab_sendExternalFolder
240403_201558:cmsbot_crab_inputDBS
240403_201600:cmsbot_crab_useParent
240403_201610:cmsbot_crab_secondaryInputDataset
240403_201612:cmsbot_crab_lumiMaskFile
240403_201630:cmsbot_crab_lumiMaskUrl
240403_201633:cmsbot_crab_outLFNDirBase
240403_201635:cmsbot_crab_runRange
240403_201636:cmsbot_crab_ignoreLocality
240403_201638:cmsbot_crab_userInputFiles
240403_201640:cmsbot_crab_whitelist
240403_201651:cmsbot_crab_blacklist
240403_201700:cmsbot_crab_ignoreGlobalBlacklist
240403_201702:cmsbot_crab_voRole
240403_201705:cmsbot_crab_voGroup
240403_201707:cmsbot_crab_scheddName
240403_201708:cmsbot_crab_collector
240403_201710:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240403_201444:cmsbot_crab_20240403_221443
```

Finished at: 2024-04-03 22:17:11
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/742/console)

## Comment (cmsdmwmbot, 2024-04-03T20:41:29Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-04-03 22:41:28
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/517/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/517//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221443  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 2 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-04-03T20:42:11Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-03 22:42:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1003/console

```
RETRY TESTS:
useParent-check.sh 240403_201600:cmsbot_crab_useParent - 2
lumiMaskFile-check.sh 240403_201612:cmsbot_crab_lumiMaskFile - 2
outLFNDirBase-check.sh 240403_201633:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240403_201635:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240403_201638:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240403_201640:cmsbot_crab_whitelist - 2
ignoreGlobalBlacklist-check.sh 240403_201700:cmsbot_crab_ignoreGlobalBlacklist - 2
voRole-check.sh 240403_201702:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_201446:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240403_201452:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201459:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240403_201519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201522:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201524:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201542:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201553:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_201558:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240403_201610:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 240403_201636:cmsbot_crab_ignoreLocality - 0
voGroup-check.sh 240403_201705:cmsbot_crab_voGroup - 0
collector-check.sh 240403_201708:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201710:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferLogs-check.sh 240403_201447:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201449:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 240403_201454:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240403_201457:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240403_201501:cmsbot_crab_maxMemoryMB - 1
sendExternalFolder-check.sh 240403_201557:cmsbot_crab_sendExternalFolder - 1
lumiMaskUrl-check.sh 240403_201630:cmsbot_crab_lumiMaskUrl - 1
blacklist-check.sh 240403_201651:cmsbot_crab_blacklist - 1
scheddName-check.sh 240403_201707:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:07:46Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-03 23:07:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1007/console

```
RETRY TESTS:
transferLogs-check.sh 240403_201447:cmsbot_crab_transferLogs - 2
outputFiles-check.sh 240403_201457:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240403_201501:cmsbot_crab_maxMemoryMB - 2
lumiMaskUrl-check.sh 240403_201630:cmsbot_crab_lumiMaskUrl - 2
whitelist-check.sh 240403_201640:cmsbot_crab_whitelist - 2
ignoreGlobalBlacklist-check.sh 240403_201700:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_201446:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240403_201452:cmsbot_crab_inputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201459:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240403_201519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201522:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201524:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201542:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201553:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201557:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201558:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_201600:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_201610:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240403_201612:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240403_201633:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_201635:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201636:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240403_201638:cmsbot_crab_userInputFiles - 0
voRole-check.sh 240403_201702:cmsbot_crab_voRole - 0
voGroup-check.sh 240403_201705:cmsbot_crab_voGroup - 0
collector-check.sh 240403_201708:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201710:cmsbot_crab_extraJDL - 0

FAILED TESTS:
activity-check.sh 240403_201449:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 240403_201454:cmsbot_crab_disableAutomaticOutputCollection - 1
blacklist-check.sh 240403_201651:cmsbot_crab_blacklist - 1
scheddName-check.sh 240403_201707:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:35:25Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-04-03 23:35:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1011/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240403_201630:cmsbot_crab_lumiMaskUrl - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_201446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240403_201447:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240403_201452:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240403_201457:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201459:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_201501:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_201519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201522:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201524:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201542:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201553:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201557:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201558:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_201600:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_201610:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240403_201612:cmsbot_crab_lumiMaskFile - 0
outLFNDirBase-check.sh 240403_201633:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_201635:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201636:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240403_201638:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240403_201640:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201700:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201702:cmsbot_crab_voRole - 0
voGroup-check.sh 240403_201705:cmsbot_crab_voGroup - 0
collector-check.sh 240403_201708:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201710:cmsbot_crab_extraJDL - 0

FAILED TESTS:
activity-check.sh 240403_201449:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 240403_201454:cmsbot_crab_disableAutomaticOutputCollection - 1
blacklist-check.sh 240403_201651:cmsbot_crab_blacklist - 1
scheddName-check.sh 240403_201707:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2024-04-03T22:16:33Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-04 00:16:32
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1015/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240403_201446:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 240403_201447:cmsbot_crab_transferLogs - 0
inputFiles-check.sh 240403_201452:cmsbot_crab_inputFiles - 0
outputFiles-check.sh 240403_201457:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201459:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_201501:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_201519:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201522:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201524:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201542:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201553:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201557:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201558:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_201600:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_201610:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240403_201612:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240403_201630:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240403_201633:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_201635:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201636:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240403_201638:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240403_201640:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201700:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201702:cmsbot_crab_voRole - 0
voGroup-check.sh 240403_201705:cmsbot_crab_voGroup - 0
collector-check.sh 240403_201708:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201710:cmsbot_crab_extraJDL - 0

FAILED TESTS:
activity-check.sh 240403_201449:cmsbot_crab_activity - 1
disableAutomaticOutputCollection-check.sh 240403_201454:cmsbot_crab_disableAutomaticOutputCollection - 1
blacklist-check.sh 240403_201651:cmsbot_crab_blacklist - 1
scheddName-check.sh 240403_201707:cmsbot_crab_scheddName - 1
```
