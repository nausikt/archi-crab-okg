# dmwm/CRABServer issue #8206: #690: Test prod CRABClient using test2 REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2024-01-30T20:47:06Z
Closed: 2024-01-31T13:58:10Z
URL: https://github.com/dmwm/CRABServer/issues/8206

## Opening post (cmsdmwmbot, 2024-01-30T20:47:06Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-01-30 21:47:05
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/690/)

## Comment (cmsdmwmbot, 2024-01-30T20:48:19Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240130_204721:cmsbot_crab_transferOutputs
240130_204722:cmsbot_crab_transferLogs
240130_204723:cmsbot_crab_activity
240130_204725:cmsbot_crab_inputFiles
240130_204726:cmsbot_crab_disableAutomaticOutputCollection
240130_204728:cmsbot_crab_outputFiles
240130_204729:cmsbot_crab_allowUndistributedCMSSW
240130_204730:cmsbot_crab_maxMemoryMB
240130_204731:cmsbot_crab_maxJobRuntimeMin
240130_204733:cmsbot_crab_numCores
240130_204733:cmsbot_crab_scriptExe
240130_204734:cmsbot_crab_scriptArgs
240130_204736:cmsbot_crab_sendVenvFolder
240130_204741:cmsbot_crab_sendExternalFolder
240130_204743:cmsbot_crab_inputDBS
240130_204744:cmsbot_crab_useParent
240130_204744:cmsbot_crab_secondaryInputDataset
240130_204745:cmsbot_crab_lumiMaskFile
240130_204746:cmsbot_crab_lumiMaskUrl
240130_204748:cmsbot_crab_outLFNDirBase
240130_204749:cmsbot_crab_runRange
240130_204750:cmsbot_crab_ignoreLocality
240130_204751:cmsbot_crab_userInputFiles
240130_204752:cmsbot_crab_whitelist
240130_204752:cmsbot_crab_blacklist
240130_204753:cmsbot_crab_ignoreGlobalBlacklist
240130_204754:cmsbot_crab_voRole
240130_204755:cmsbot_crab_voGroup
240130_204756:cmsbot_crab_scheddName
240130_204757:cmsbot_crab_collector
240130_204758:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240130_204720:cmsbot_crab_20240130_214718
```

Finished at: 2024-01-30 21:47:58
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/690/console)

## Comment (cmsdmwmbot, 2024-01-30T21:14:09Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-01-30 22:14:08
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/504/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/504//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpyRw51n
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is NEW


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-test2.cern.ch:8443/crabserver/dev/task?subresource=webdirprx&workflow=240130_204720%3Acmsbot_crab_20240130_214718 using subresource=webdirprx&workflow=240130_204720%3Acmsbot_crab_20240130_214718.
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
Error Id: fbcd2172479b3b79b1e8ba529fe707a2


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240130_214718  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-01-30T21:19:23Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-01-30 22:19:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/901/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 240130_204744:cmsbot_crab_secondaryInputDataset - 2

SUCCESSFUL TESTS:
useParent-check.sh 240130_204744:cmsbot_crab_useParent - 0
scheddName-check.sh 240130_204756:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204757:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240130_204721:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240130_204722:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204723:cmsbot_crab_activity - 1
inputFiles-check.sh 240130_204725:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240130_204726:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240130_204728:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240130_204729:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240130_204730:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204731:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204733:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204733:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204734:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240130_204736:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240130_204741:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_204743:cmsbot_crab_inputDBS - 1
lumiMaskFile-check.sh 240130_204745:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204746:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204748:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204749:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204750:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204751:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204752:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204752:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204753:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204754:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204755:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204758:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T21:43:03Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-01-30 22:43:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/904/console

```
RETRY TESTS:
transferOutputs-check.sh 240130_204721:cmsbot_crab_transferOutputs - 2
transferLogs-check.sh 240130_204722:cmsbot_crab_transferLogs - 2
activity-check.sh 240130_204723:cmsbot_crab_activity - 2
disableAutomaticOutputCollection-check.sh 240130_204726:cmsbot_crab_disableAutomaticOutputCollection - 2

SUCCESSFUL TESTS:
inputFiles-check.sh 240130_204725:cmsbot_crab_inputFiles - 0
useParent-check.sh 240130_204744:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_204744:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_204756:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204757:cmsbot_crab_collector - 0

FAILED TESTS:
outputFiles-check.sh 240130_204728:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240130_204729:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240130_204730:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204731:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204733:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204733:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204734:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240130_204736:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240130_204741:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240130_204743:cmsbot_crab_inputDBS - 1
lumiMaskFile-check.sh 240130_204745:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204746:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204748:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204749:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204750:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204751:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204752:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204752:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204753:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204754:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204755:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204758:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-01-30T22:07:03Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-01-30 23:07:02
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/907/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240130_204721:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240130_204725:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240130_204726:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240130_204729:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240130_204736:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240130_204741:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240130_204743:cmsbot_crab_inputDBS - 0
useParent-check.sh 240130_204744:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240130_204744:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240130_204756:cmsbot_crab_scheddName - 0
collector-check.sh 240130_204757:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240130_204722:cmsbot_crab_transferLogs - 1
activity-check.sh 240130_204723:cmsbot_crab_activity - 1
outputFiles-check.sh 240130_204728:cmsbot_crab_outputFiles - 1
maxMemoryMB-check.sh 240130_204730:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240130_204731:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240130_204733:cmsbot_crab_numCores - 1
scriptExe-check.sh 240130_204733:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240130_204734:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 240130_204745:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240130_204746:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240130_204748:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240130_204749:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240130_204750:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240130_204751:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240130_204752:cmsbot_crab_whitelist - 1
blacklist-check.sh 240130_204752:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240130_204753:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240130_204754:cmsbot_crab_voRole - 1
voGroup-check.sh 240130_204755:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240130_204758:cmsbot_crab_extraJDL - 1
```
