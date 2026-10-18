# dmwm/CRABServer issue #8311: #741: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-03T20:11:24Z
Closed: 2024-04-04T09:08:34Z
URL: https://github.com/dmwm/CRABServer/issues/8311

## Opening post (cmsdmwmbot, 2024-04-03T20:11:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-04-03 22:11:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/741/)

## Comment (cmsdmwmbot, 2024-04-03T20:14:16Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240403_201149:cmsbot_crab_transferOutputs
240403_201151:cmsbot_crab_transferLogs
240403_201155:cmsbot_crab_activity
240403_201157:cmsbot_crab_inputFiles
240403_201159:cmsbot_crab_disableAutomaticOutputCollection
240403_201201:cmsbot_crab_outputFiles
240403_201203:cmsbot_crab_allowUndistributedCMSSW
240403_201205:cmsbot_crab_maxMemoryMB
240403_201225:cmsbot_crab_maxJobRuntimeMin
240403_201227:cmsbot_crab_numCores
240403_201229:cmsbot_crab_scriptExe
240403_201231:cmsbot_crab_scriptArgs
240403_201234:cmsbot_crab_sendVenvFolder
240403_201252:cmsbot_crab_sendExternalFolder
240403_201254:cmsbot_crab_inputDBS
240403_201304:cmsbot_crab_useParent
240403_201306:cmsbot_crab_secondaryInputDataset
240403_201308:cmsbot_crab_lumiMaskFile
240403_201310:cmsbot_crab_lumiMaskUrl
240403_201321:cmsbot_crab_outLFNDirBase
240403_201326:cmsbot_crab_runRange
240403_201328:cmsbot_crab_ignoreLocality
240403_201330:cmsbot_crab_userInputFiles
240403_201332:cmsbot_crab_whitelist
240403_201334:cmsbot_crab_blacklist
240403_201336:cmsbot_crab_ignoreGlobalBlacklist
240403_201346:cmsbot_crab_voRole
240403_201348:cmsbot_crab_voGroup
240403_201350:cmsbot_crab_scheddName
240403_201352:cmsbot_crab_collector
240403_201354:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240403_201146:cmsbot_crab_20240403_221145
```

Finished at: 2024-04-03 22:13:55
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/741/console)

## Comment (cmsdmwmbot, 2024-04-03T20:39:05Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-04-03 22:39:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/516/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/516//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221145  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
The job with id 3 is not in a valid state to retrieve output files
```

## Comment (cmsdmwmbot, 2024-04-03T20:39:21Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-03 22:39:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1002/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 240403_201306:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240403_201310:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240403_201326:cmsbot_crab_runRange - 2
whitelist-check.sh 240403_201332:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
disableAutomaticOutputCollection-check.sh 240403_201159:cmsbot_crab_disableAutomaticOutputCollection - 0
numCores-check.sh 240403_201227:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201229:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201231:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201234:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_201254:cmsbot_crab_inputDBS - 0
ignoreLocality-check.sh 240403_201328:cmsbot_crab_ignoreLocality - 0
collector-check.sh 240403_201352:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201354:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201149:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240403_201151:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201155:cmsbot_crab_activity - 1
inputFiles-check.sh 240403_201157:cmsbot_crab_inputFiles - 1
outputFiles-check.sh 240403_201201:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240403_201203:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240403_201205:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240403_201225:cmsbot_crab_maxJobRuntimeMin - 1
sendExternalFolder-check.sh 240403_201252:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 240403_201304:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 240403_201308:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240403_201321:cmsbot_crab_outLFNDirBase - 1
userInputFiles-check.sh 240403_201330:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240403_201334:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240403_201336:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240403_201346:cmsbot_crab_voRole - 1
voGroup-check.sh 240403_201348:cmsbot_crab_voGroup - 1
scheddName-check.sh 240403_201350:cmsbot_crab_scheddName - 1
```

## Comment (cmsdmwmbot, 2024-04-03T20:49:36Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2024-04-03 22:49:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/520/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/520//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2024-04-03T21:04:45Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-03 23:04:44
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1006/console

```
RETRY TESTS:
runRange-check.sh 240403_201326:cmsbot_crab_runRange - 2
voGroup-check.sh 240403_201348:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
disableAutomaticOutputCollection-check.sh 240403_201159:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240403_201201:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201203:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240403_201225:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201227:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201229:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201231:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201234:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_201254:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240403_201306:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240403_201310:cmsbot_crab_lumiMaskUrl - 0
ignoreLocality-check.sh 240403_201328:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240403_201332:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201346:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_201350:cmsbot_crab_scheddName - 0
collector-check.sh 240403_201352:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201354:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201149:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240403_201151:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201155:cmsbot_crab_activity - 1
inputFiles-check.sh 240403_201157:cmsbot_crab_inputFiles - 1
maxMemoryMB-check.sh 240403_201205:cmsbot_crab_maxMemoryMB - 1
sendExternalFolder-check.sh 240403_201252:cmsbot_crab_sendExternalFolder - 1
useParent-check.sh 240403_201304:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 240403_201308:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240403_201321:cmsbot_crab_outLFNDirBase - 1
userInputFiles-check.sh 240403_201330:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240403_201334:cmsbot_crab_blacklist - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:30:36Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 4. Will run again.
**Finished at:** 2024-04-03 23:30:35
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1010/console

```
RETRY TESTS:
outLFNDirBase-check.sh 240403_201321:cmsbot_crab_outLFNDirBase - 2
voGroup-check.sh 240403_201348:cmsbot_crab_voGroup - 2

SUCCESSFUL TESTS:
disableAutomaticOutputCollection-check.sh 240403_201159:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240403_201201:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201203:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240403_201225:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201227:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201229:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201231:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201234:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_201254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_201304:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_201306:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240403_201310:cmsbot_crab_lumiMaskUrl - 0
runRange-check.sh 240403_201326:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201328:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240403_201332:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201346:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_201350:cmsbot_crab_scheddName - 0
collector-check.sh 240403_201352:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201354:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201149:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240403_201151:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201155:cmsbot_crab_activity - 1
inputFiles-check.sh 240403_201157:cmsbot_crab_inputFiles - 1
maxMemoryMB-check.sh 240403_201205:cmsbot_crab_maxMemoryMB - 1
sendExternalFolder-check.sh 240403_201252:cmsbot_crab_sendExternalFolder - 1
lumiMaskFile-check.sh 240403_201308:cmsbot_crab_lumiMaskFile - 1
userInputFiles-check.sh 240403_201330:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240403_201334:cmsbot_crab_blacklist - 1
```

## Comment (cmsdmwmbot, 2024-04-03T22:06:47Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 3 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-04 00:06:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1014/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
disableAutomaticOutputCollection-check.sh 240403_201159:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240403_201201:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201203:cmsbot_crab_allowUndistributedCMSSW - 0
maxJobRuntimeMin-check.sh 240403_201225:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201227:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201229:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 240403_201231:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 240403_201234:cmsbot_crab_sendVenvFolder - 0
inputDBS-check.sh 240403_201254:cmsbot_crab_inputDBS - 0
useParent-check.sh 240403_201304:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240403_201306:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240403_201310:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240403_201321:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_201326:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201328:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240403_201332:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201336:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201346:cmsbot_crab_voRole - 0
voGroup-check.sh 240403_201348:cmsbot_crab_voGroup - 0
scheddName-check.sh 240403_201350:cmsbot_crab_scheddName - 0
collector-check.sh 240403_201352:cmsbot_crab_collector - 0
extraJDL-check.sh 240403_201354:cmsbot_crab_extraJDL - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201149:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240403_201151:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201155:cmsbot_crab_activity - 1
inputFiles-check.sh 240403_201157:cmsbot_crab_inputFiles - 1
maxMemoryMB-check.sh 240403_201205:cmsbot_crab_maxMemoryMB - 1
sendExternalFolder-check.sh 240403_201252:cmsbot_crab_sendExternalFolder - 1
lumiMaskFile-check.sh 240403_201308:cmsbot_crab_lumiMaskFile - 1
userInputFiles-check.sh 240403_201330:cmsbot_crab_userInputFiles - 1
blacklist-check.sh 240403_201334:cmsbot_crab_blacklist - 1
```
