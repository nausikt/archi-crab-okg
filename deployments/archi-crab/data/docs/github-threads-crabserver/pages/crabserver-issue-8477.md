# dmwm/CRABServer issue #8477: #798: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-06-04T20:26:10Z
Closed: 2024-06-06T13:47:46Z
URL: https://github.com/dmwm/CRABServer/issues/8477

## Opening post (cmsdmwmbot, 2024-06-04T20:26:10Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-06-04 22:26:10
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/798/)

## Comment (cmsdmwmbot, 2024-06-04T20:28:45Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240604_202753:cmsbot_crab_20240604_222752
240604_202755:cmsbot_crab_20240604_222754
240604_202757:cmsbot_crab_20240604_222756
240604_202759:cmsbot_crab_20240604_222759
240604_202801:cmsbot_crab_20240604_222801
240604_202805:cmsbot_crab_20240604_222803
240604_202808:cmsbot_crab_rucio_transfers_20240604_222807
240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810
240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812
240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815
240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819
240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240604_202644:cmsbot_crab_transferOutputs
240604_202646:cmsbot_crab_transferLogs
240604_202648:cmsbot_crab_activity
240604_202650:cmsbot_crab_inputFiles
240604_202652:cmsbot_crab_disableAutomaticOutputCollection
240604_202654:cmsbot_crab_outputFiles
240604_202657:cmsbot_crab_allowUndistributedCMSSW
240604_202659:cmsbot_crab_maxMemoryMB
240604_202701:cmsbot_crab_maxJobRuntimeMin
240604_202703:cmsbot_crab_numCores
240604_202706:cmsbot_crab_scriptExe
240604_202708:cmsbot_crab_scriptArgs
240604_202710:cmsbot_crab_sendVenvFolder
240604_202712:cmsbot_crab_sendExternalFolder
240604_202714:cmsbot_crab_inputDBS
240604_202716:cmsbot_crab_useParent
240604_202719:cmsbot_crab_secondaryInputDataset
240604_202721:cmsbot_crab_lumiMaskFile
240604_202723:cmsbot_crab_lumiMaskUrl
240604_202726:cmsbot_crab_outLFNDirBase
240604_202728:cmsbot_crab_runRange
240604_202731:cmsbot_crab_ignoreLocality
240604_202733:cmsbot_crab_userInputFiles
240604_202735:cmsbot_crab_whitelist
240604_202737:cmsbot_crab_blacklist
240604_202739:cmsbot_crab_ignoreGlobalBlacklist
240604_202741:cmsbot_crab_voRole
240604_202743:cmsbot_crab_voGroup
240604_202745:cmsbot_crab_scheddName
240604_202748:cmsbot_crab_collector
240604_202750:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240604_202632:cmsbot_crab_20240604_222631
```

Finished at: 2024-06-04 22:28:23
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/798/console)

## Comment (cmsdmwmbot, 2024-06-04T20:49:43Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-06-04 22:49:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/974/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-06-04T20:52:23Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-06-04 22:52:22
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/540/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/540//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Getting input files into tmp dir /tmp/tmpcqk169et
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is QUEUED


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=webdirprx&workflow=240604_202632%3Acmsbot_crab_20240604_222631 using subresource=webdirprx&workflow=240604_202632%3Acmsbot_crab_20240604_222631.
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
Error Id: fbcef9d9c9120ae33228c6533989e21a


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240604_222631  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-06-04T20:53:04Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-06-04 22:53:03
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1106/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240604_202644:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240604_202646:cmsbot_crab_transferLogs - 1
activity-check.sh 240604_202648:cmsbot_crab_activity - 1
inputFiles-check.sh 240604_202650:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240604_202652:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240604_202654:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240604_202657:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240604_202659:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240604_202701:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240604_202703:cmsbot_crab_numCores - 1
scriptExe-check.sh 240604_202706:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240604_202708:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240604_202710:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240604_202712:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240604_202714:cmsbot_crab_inputDBS - 1
useParent-check.sh 240604_202716:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240604_202719:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240604_202721:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240604_202723:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240604_202726:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240604_202728:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240604_202731:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240604_202733:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240604_202735:cmsbot_crab_whitelist - 1
blacklist-check.sh 240604_202737:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240604_202739:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240604_202741:cmsbot_crab_voRole - 1
voGroup-check.sh 240604_202743:cmsbot_crab_voGroup - 1
scheddName-check.sh 240604_202745:cmsbot_crab_scheddName - 1
collector-check.sh 240604_202748:cmsbot_crab_collector - 1
extraJDL-check.sh 240604_202750:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-06-04T21:06:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-06-04 23:06:40
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/975/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-06-04T21:52:41Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-06-04 23:52:39
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/976/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-06-04T23:23:42Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 3 out of 5. Will run again.
**Finished at:** 2024-06-05 01:23:41
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/977/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-06-05T01:25:39Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 4 out of 5. Will run again.
**Finished at:** 2024-06-05 03:25:38
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/978/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestRunning', 'dbStatus': 'QUEUED', 'combinedStatus': 'QUEUED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-06-05T03:27:20Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 5 out of 5. Exceeded configured retries. If needed restart manually.
**Finished at:** 2024-06-05 05:27:18
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/979/console

```
{'TN': '240604_202753:cmsbot_crab_20240604_222752', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202755:cmsbot_crab_20240604_222754', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202757:cmsbot_crab_20240604_222756', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202759:cmsbot_crab_20240604_222759', 'testResult': 'TestRunning', 'dbStatus': 'QUEUED', 'combinedStatus': 'QUEUED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202801:cmsbot_crab_20240604_222801', 'testResult': 'TestRunning', 'dbStatus': 'QUEUED', 'combinedStatus': 'QUEUED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202805:cmsbot_crab_20240604_222803', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202808:cmsbot_crab_rucio_transfers_20240604_222807', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202810:cmsbot_crab_rucio_transfers_group_20240604_222810', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202813:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240604_222812', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202817:cmsbot_crab_rucio_transfers_nopublication_20240604_222815', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202820:cmsbot_crab_rucio_transfers_withnoneedm_20240604_222819', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240604_202823:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240604_222822', 'testResult': 'TestRunning', 'dbStatus': 'NEW', 'combinedStatus': 'NEW', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (belforte, 2024-06-06T13:47:46Z)

my last change did not work :-)
