# dmwm/CRABServer issue #8340: #755: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-16T11:57:25Z
Closed: 2024-04-16T12:49:55Z
URL: https://github.com/dmwm/CRABServer/issues/8340

## Opening post (cmsdmwmbot, 2024-04-16T11:57:25Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-04-16 13:57:24
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/755/)

## Comment (cmsdmwmbot, 2024-04-16T12:00:57Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240416_115946:cmsbot_crab_20240416_135946
240416_115949:cmsbot_crab_20240416_135948
240416_115951:cmsbot_crab_20240416_135950
240416_115953:cmsbot_crab_20240416_135953
240416_115955:cmsbot_crab_20240416_135955
240416_120017:cmsbot_crab_20240416_135957
240416_120020:cmsbot_crab_rucio_transfers_20240416_140018
240416_120022:cmsbot_crab_rucio_transfers_group_20240416_140022
240416_120026:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_140024
240416_120029:cmsbot_crab_rucio_transfers_nopublication_20240416_140027
240416_120032:cmsbot_crab_rucio_transfers_withnoneedm_20240416_140031
240416_120036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_140034
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240416_115833:cmsbot_crab_transferOutputs
240416_115835:cmsbot_crab_transferLogs
240416_115837:cmsbot_crab_activity
240416_115839:cmsbot_crab_inputFiles
240416_115842:cmsbot_crab_disableAutomaticOutputCollection
240416_115844:cmsbot_crab_outputFiles
240416_115846:cmsbot_crab_allowUndistributedCMSSW
240416_115848:cmsbot_crab_maxMemoryMB
240416_115850:cmsbot_crab_maxJobRuntimeMin
240416_115853:cmsbot_crab_numCores
240416_115855:cmsbot_crab_scriptExe
240416_115857:cmsbot_crab_scriptArgs
240416_115859:cmsbot_crab_sendVenvFolder
240416_115902:cmsbot_crab_sendExternalFolder
240416_115904:cmsbot_crab_inputDBS
240416_115907:cmsbot_crab_useParent
240416_115909:cmsbot_crab_secondaryInputDataset
240416_115911:cmsbot_crab_lumiMaskFile
240416_115914:cmsbot_crab_lumiMaskUrl
240416_115917:cmsbot_crab_outLFNDirBase
240416_115920:cmsbot_crab_runRange
240416_115922:cmsbot_crab_ignoreLocality
240416_115925:cmsbot_crab_userInputFiles
240416_115927:cmsbot_crab_whitelist
240416_115929:cmsbot_crab_blacklist
240416_115931:cmsbot_crab_ignoreGlobalBlacklist
240416_115934:cmsbot_crab_voRole
240416_115937:cmsbot_crab_voGroup
240416_115939:cmsbot_crab_scheddName
240416_115941:cmsbot_crab_collector
240416_115943:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240416_115823:cmsbot_crab_20240416_135820
```

Finished at: 2024-04-16 14:00:36
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/755/console)

## Comment (cmsdmwmbot, 2024-04-16T12:23:15Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-16 14:23:13
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/860/console

```
{'TN': '240416_115946:cmsbot_crab_20240416_135946', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115949:cmsbot_crab_20240416_135948', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115951:cmsbot_crab_20240416_135950', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115953:cmsbot_crab_20240416_135953', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115955:cmsbot_crab_20240416_135955', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120017:cmsbot_crab_20240416_135957', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120020:cmsbot_crab_rucio_transfers_20240416_140018', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120022:cmsbot_crab_rucio_transfers_group_20240416_140022', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120026:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_140024', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120029:cmsbot_crab_rucio_transfers_nopublication_20240416_140027', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120032:cmsbot_crab_rucio_transfers_withnoneedm_20240416_140031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_140034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-04-16T12:25:52Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-04-16 14:25:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/529/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/529//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpywpx50nt
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is SUBMITFAILED


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=webdirprx&workflow=240416_115823%3Acmsbot_crab_20240416_135820 using subresource=webdirprx&workflow=240416_115823%3Acmsbot_crab_20240416_135820.
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
Error Id: 3581220b2ddaea01bb8a315f3abc934e


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240416_135820  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-04-16T12:26:24Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-16 14:26:23
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1031/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240416_115833:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240416_115835:cmsbot_crab_transferLogs - 1
activity-check.sh 240416_115837:cmsbot_crab_activity - 1
inputFiles-check.sh 240416_115839:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240416_115842:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240416_115844:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240416_115846:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240416_115848:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240416_115850:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240416_115853:cmsbot_crab_numCores - 1
scriptExe-check.sh 240416_115855:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240416_115857:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240416_115859:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240416_115902:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240416_115904:cmsbot_crab_inputDBS - 1
useParent-check.sh 240416_115907:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240416_115909:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240416_115911:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240416_115914:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240416_115917:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240416_115920:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240416_115922:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240416_115925:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240416_115927:cmsbot_crab_whitelist - 1
blacklist-check.sh 240416_115929:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240416_115931:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240416_115934:cmsbot_crab_voRole - 1
voGroup-check.sh 240416_115937:cmsbot_crab_voGroup - 1
scheddName-check.sh 240416_115939:cmsbot_crab_scheddName - 1
collector-check.sh 240416_115941:cmsbot_crab_collector - 1
extraJDL-check.sh 240416_115943:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-04-16T12:39:18Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-16 14:39:17
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/861/console

```
{'TN': '240416_115946:cmsbot_crab_20240416_135946', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115949:cmsbot_crab_20240416_135948', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115951:cmsbot_crab_20240416_135950', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115953:cmsbot_crab_20240416_135953', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_115955:cmsbot_crab_20240416_135955', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120017:cmsbot_crab_20240416_135957', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120020:cmsbot_crab_rucio_transfers_20240416_140018', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120022:cmsbot_crab_rucio_transfers_group_20240416_140022', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120026:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240416_140024', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120029:cmsbot_crab_rucio_transfers_nopublication_20240416_140027', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120032:cmsbot_crab_rucio_transfers_withnoneedm_20240416_140031', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240416_120036:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240416_140034', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```
