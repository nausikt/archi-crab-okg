# dmwm/CRABServer issue #8334: #754: Test prod CRABClient using test12 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-04-12T11:23:29Z
Closed: 2024-04-12T13:48:47Z
URL: https://github.com/dmwm/CRABServer/issues/8334

## Opening post (cmsdmwmbot, 2024-04-12T11:23:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test12**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-04-12 13:23:28
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/754/)

## Comment (cmsdmwmbot, 2024-04-12T11:26:40Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
240412_112533:cmsbot_crab_20240412_132532
240412_112535:cmsbot_crab_20240412_132534
240412_112537:cmsbot_crab_20240412_132537
240412_112539:cmsbot_crab_20240412_132539
240412_112541:cmsbot_crab_20240412_132541
240412_112601:cmsbot_crab_20240412_132543
240412_112604:cmsbot_crab_rucio_transfers_20240412_132602
240412_112606:cmsbot_crab_rucio_transfers_group_20240412_132605
240412_112609:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240412_132607
240412_112612:cmsbot_crab_rucio_transfers_nopublication_20240412_132611
240412_112615:cmsbot_crab_rucio_transfers_withnoneedm_20240412_132614
240412_112618:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240412_132617
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
240412_112426:cmsbot_crab_transferOutputs
240412_112428:cmsbot_crab_transferLogs
240412_112430:cmsbot_crab_activity
240412_112432:cmsbot_crab_inputFiles
240412_112434:cmsbot_crab_disableAutomaticOutputCollection
240412_112436:cmsbot_crab_outputFiles
240412_112438:cmsbot_crab_allowUndistributedCMSSW
240412_112440:cmsbot_crab_maxMemoryMB
240412_112442:cmsbot_crab_maxJobRuntimeMin
240412_112444:cmsbot_crab_numCores
240412_112446:cmsbot_crab_scriptExe
240412_112448:cmsbot_crab_scriptArgs
240412_112451:cmsbot_crab_sendVenvFolder
240412_112453:cmsbot_crab_sendExternalFolder
240412_112455:cmsbot_crab_inputDBS
240412_112457:cmsbot_crab_useParent
240412_112459:cmsbot_crab_secondaryInputDataset
240412_112501:cmsbot_crab_lumiMaskFile
240412_112503:cmsbot_crab_lumiMaskUrl
240412_112507:cmsbot_crab_outLFNDirBase
240412_112509:cmsbot_crab_runRange
240412_112511:cmsbot_crab_ignoreLocality
240412_112513:cmsbot_crab_userInputFiles
240412_112515:cmsbot_crab_whitelist
240412_112518:cmsbot_crab_blacklist
240412_112520:cmsbot_crab_ignoreGlobalBlacklist
240412_112522:cmsbot_crab_voRole
240412_112524:cmsbot_crab_voGroup
240412_112526:cmsbot_crab_scheddName
240412_112528:cmsbot_crab_collector
240412_112530:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240412_112423:cmsbot_crab_20240412_132422
```

Finished at: 2024-04-12 13:26:19
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/754/console)

## Comment (cmsdmwmbot, 2024-04-12T11:48:17Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-12 13:48:16
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/857/console

```
{'TN': '240412_112533:cmsbot_crab_20240412_132532', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112535:cmsbot_crab_20240412_132534', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112537:cmsbot_crab_20240412_132537', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112539:cmsbot_crab_20240412_132539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112541:cmsbot_crab_20240412_132541', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112601:cmsbot_crab_20240412_132543', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112604:cmsbot_crab_rucio_transfers_20240412_132602', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112606:cmsbot_crab_rucio_transfers_group_20240412_132605', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112609:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240412_132607', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112612:cmsbot_crab_rucio_transfers_nopublication_20240412_132611', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112615:cmsbot_crab_rucio_transfers_withnoneedm_20240412_132614', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112618:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240412_132617', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-04-12T11:50:11Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-04-12 13:50:10
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/528/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/528//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpnhkgmqd0
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is SUBMITFAILED


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-test12.cern.ch:8443/crabserver/devthree/task?subresource=webdirprx&workflow=240412_112423%3Acmsbot_crab_20240412_132422 using subresource=webdirprx&workflow=240412_112423%3Acmsbot_crab_20240412_132422.
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
Error Id: 26e3daae98447ae5ceffc379b6be34c1


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240412_132422  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Your user certificate is going to expire in 4 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task has not been submitted to the Grid scheduler yet. Not printing job information. 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-04-12T11:50:27Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-12 13:50:26
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1030/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
 none

FAILED TESTS:
transferOutputs-check.sh 240412_112426:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240412_112428:cmsbot_crab_transferLogs - 1
activity-check.sh 240412_112430:cmsbot_crab_activity - 1
inputFiles-check.sh 240412_112432:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240412_112434:cmsbot_crab_disableAutomaticOutputCollection - 1
outputFiles-check.sh 240412_112436:cmsbot_crab_outputFiles - 1
allowUndistributedCMSSW-check.sh 240412_112438:cmsbot_crab_allowUndistributedCMSSW - 1
maxMemoryMB-check.sh 240412_112440:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 240412_112442:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 240412_112444:cmsbot_crab_numCores - 1
scriptExe-check.sh 240412_112446:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240412_112448:cmsbot_crab_scriptArgs - 1
sendVenvFolder-check.sh 240412_112451:cmsbot_crab_sendVenvFolder - 1
sendExternalFolder-check.sh 240412_112453:cmsbot_crab_sendExternalFolder - 1
inputDBS-check.sh 240412_112455:cmsbot_crab_inputDBS - 1
useParent-check.sh 240412_112457:cmsbot_crab_useParent - 1
secondaryInputDataset-check.sh 240412_112459:cmsbot_crab_secondaryInputDataset - 1
lumiMaskFile-check.sh 240412_112501:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 240412_112503:cmsbot_crab_lumiMaskUrl - 1
outLFNDirBase-check.sh 240412_112507:cmsbot_crab_outLFNDirBase - 1
runRange-check.sh 240412_112509:cmsbot_crab_runRange - 1
ignoreLocality-check.sh 240412_112511:cmsbot_crab_ignoreLocality - 1
userInputFiles-check.sh 240412_112513:cmsbot_crab_userInputFiles - 1
whitelist-check.sh 240412_112515:cmsbot_crab_whitelist - 1
blacklist-check.sh 240412_112518:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240412_112520:cmsbot_crab_ignoreGlobalBlacklist - 1
voRole-check.sh 240412_112522:cmsbot_crab_voRole - 1
voGroup-check.sh 240412_112524:cmsbot_crab_voGroup - 1
scheddName-check.sh 240412_112526:cmsbot_crab_scheddName - 1
collector-check.sh 240412_112528:cmsbot_crab_collector - 1
extraJDL-check.sh 240412_112530:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-04-12T12:05:07Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 5. Will run again.
**Finished at:** 2024-04-12 14:05:06
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/858/console

```
{'TN': '240412_112533:cmsbot_crab_20240412_132532', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112535:cmsbot_crab_20240412_132534', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112537:cmsbot_crab_20240412_132537', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112539:cmsbot_crab_20240412_132539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112541:cmsbot_crab_20240412_132541', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112601:cmsbot_crab_20240412_132543', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112604:cmsbot_crab_rucio_transfers_20240412_132602', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112606:cmsbot_crab_rucio_transfers_group_20240412_132605', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112609:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240412_132607', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112612:cmsbot_crab_rucio_transfers_nopublication_20240412_132611', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112615:cmsbot_crab_rucio_transfers_withnoneedm_20240412_132614', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112618:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240412_132617', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```

## Comment (cmsdmwmbot, 2024-04-12T12:53:12Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 2 out of 5. Will run again.
**Finished at:** 2024-04-12 14:53:11
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/859/console

```
{'TN': '240412_112533:cmsbot_crab_20240412_132532', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112535:cmsbot_crab_20240412_132534', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112537:cmsbot_crab_20240412_132537', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112539:cmsbot_crab_20240412_132539', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112541:cmsbot_crab_20240412_132541', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112601:cmsbot_crab_20240412_132543', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112604:cmsbot_crab_rucio_transfers_20240412_132602', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112606:cmsbot_crab_rucio_transfers_group_20240412_132605', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112609:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240412_132607', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112612:cmsbot_crab_rucio_transfers_nopublication_20240412_132611', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112615:cmsbot_crab_rucio_transfers_withnoneedm_20240412_132614', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
{'TN': '240412_112618:cmsbot_crab_rucio_transfers_withnoneedm_nopublication_20240412_132617', 'testResult': 'TestResubmitted', 'dbStatus': 'SUBMITFAILED', 'combinedStatus': 'SUBMITFAILED', 'jobsPerStatus': {}, 'publication (fail/tdb/DBS)': 'None'}
```
