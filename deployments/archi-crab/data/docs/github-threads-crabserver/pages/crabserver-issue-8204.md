# dmwm/CRABServer issue #8204: #688: Test prod CRABClient using test2 REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2024-01-30T20:43:30Z
Closed: 2024-01-31T13:58:09Z
URL: https://github.com/dmwm/CRABServer/issues/8204

## Opening post (cmsdmwmbot, 2024-01-30T20:43:30Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_12_6_4**
- SCRAM_ARCH: **el8_amd64_gcc10**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:43:30
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/688/)

## Comment (cmsdmwmbot, 2024-01-30T20:45:44Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_204415:cmsbot_crab_transferOutputs
240130_204417:cmsbot_crab_transferLogs
240130_204419:cmsbot_crab_activity
240130_204421:cmsbot_crab_inputFiles
240130_204423:cmsbot_crab_disableAutomaticOutputCollection
240130_204425:cmsbot_crab_outputFiles
240130_204427:cmsbot_crab_allowUndistributedCMSSW
240130_204429:cmsbot_crab_maxMemoryMB
240130_204431:cmsbot_crab_maxJobRuntimeMin
240130_204433:cmsbot_crab_numCores
240130_204435:cmsbot_crab_scriptExe
240130_204437:cmsbot_crab_scriptArgs
240130_204439:cmsbot_crab_sendVenvFolder
240130_204448:cmsbot_crab_sendExternalFolder
240130_204450:cmsbot_crab_inputDBS
240130_204452:cmsbot_crab_useParent
240130_204454:cmsbot_crab_secondaryInputDataset
240130_204456:cmsbot_crab_lumiMaskFile
240130_204458:cmsbot_crab_lumiMaskUrl
240130_204501:cmsbot_crab_outLFNDirBase
240130_204503:cmsbot_crab_runRange
240130_204505:cmsbot_crab_ignoreLocality
240130_204507:cmsbot_crab_userInputFiles
240130_204508:cmsbot_crab_whitelist
240130_204510:cmsbot_crab_blacklist
240130_204512:cmsbot_crab_ignoreGlobalBlacklist
240130_204514:cmsbot_crab_voRole
240130_204516:cmsbot_crab_voGroup
240130_204518:cmsbot_crab_scheddName
240130_204520:cmsbot_crab_collector
240130_204522:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_204413:cmsbot_crab_20240130_214412
```

Finished at: 2024-01-30 21:45:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/688/console)

## Comment (cmsdmwmbot, 2024-01-30T21:09:55Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-30 22:09:54
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/502/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/502//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpeb3_4ome
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is NEW


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-test2.cern.ch:8443/crabserver/dev/task?subresource=webdirprx&workflow=240130_204413%3Acmsbot_crab_20240130_214412 using subresource=webdirprx&workflow=240130_204413%3Acmsbot_crab_20240130_214412.
exit code from curl = 0
HTTP code/reason = 500/Internal Server Error .  stdout:
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
    <title>500 Internal Server Error</title>
    <style type="text/css">
    #powered_by {
        margin-top: 20px;
        border-top: 2px solid black;
        font-style: italic;
    }

    #traceback {
        color: red;
    }
    </style>
</head>
    <body>
        <h2>500 Internal Server Error</h2>
        <p>Execution error</p>
        <pre id="traceback"></pre>
    <div id="powered_by">
      <span>
        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.8.0</a>
      </span>
    </div>
    </body>
</html>

The server answered with an error.
Server answered with: Execution error
Reason is: Webdir not set in the database. Cannot build proxied webdir
Error Id: b2c3519732fef6ff57851563e56a9f55


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214412  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-01-30T21:13:23Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 22:13:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/898/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
allowUndistributedCMSSW-check.sh 240130_204427:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204439:cmsbot_crab_sendVenvFolder - 0

FAILED TESTS:
transferOutputs-check.sh 240130_204415:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240130_204417:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204419:cmsbot_crab_activity - 1
inputFiles-check.sh 240130_204421:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240130_204423:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240130_204425:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204429:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204431:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204433:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204435:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204437:cmsbot_crab_scriptArgs - 1
sendExternalFolder-check.sh 240130_204448:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_204450:cmsbot_crab_inputDBS - 1
useParent-check.sh 240130_204452:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240130_204454:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240130_204456:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204458:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204501:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204503:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204505:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204507:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204508:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204510:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204512:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204514:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204516:cmsbot_crab_voGroup - 1
scheddName-check.sh 240130_204518:cmsbot_crab_scheddName - 1
collector-check.sh 240130_204520:cmsbot_crab_collector - 1
extraJDL-check.sh 240130_204522:cmsbot_crab_extraJDL - 1
```
