# dmwm/CRABServer issue #8314: #744: Test dev CRABClient using prod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-04-03T20:18:29Z
Closed: 2024-04-04T09:08:34Z
URL: https://github.com/dmwm/CRABServer/issues/8314

## Opening post (cmsdmwmbot, 2024-04-03T20:18:29Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
Started at: 2024-04-03 22:18:29
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/744/)

## Comment (cmsdmwmbot, 2024-04-03T20:20:17Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240403_201844:cmsbot_crab_transferOutputs
240403_201845:cmsbot_crab_transferLogs
240403_201846:cmsbot_crab_activity
240403_201847:cmsbot_crab_inputFiles
240403_201847:cmsbot_crab_disableAutomaticOutputCollection
240403_201848:cmsbot_crab_outputFiles
240403_201849:cmsbot_crab_allowUndistributedCMSSW
240403_201850:cmsbot_crab_maxMemoryMB
240403_201851:cmsbot_crab_maxJobRuntimeMin
240403_201900:cmsbot_crab_numCores
240403_201901:cmsbot_crab_scriptExe
240403_201902:cmsbot_crab_scriptArgs
240403_201911:cmsbot_crab_sendVenvFolder
240403_201915:cmsbot_crab_sendExternalFolder
240403_201915:cmsbot_crab_inputDBS
240403_201916:cmsbot_crab_useParent
240403_201917:cmsbot_crab_secondaryInputDataset
240403_201918:cmsbot_crab_lumiMaskFile
240403_201919:cmsbot_crab_lumiMaskUrl
240403_201921:cmsbot_crab_outLFNDirBase
240403_201922:cmsbot_crab_runRange
240403_201931:cmsbot_crab_ignoreLocality
240403_201932:cmsbot_crab_userInputFiles
240403_201933:cmsbot_crab_whitelist
240403_201933:cmsbot_crab_blacklist
240403_201934:cmsbot_crab_ignoreGlobalBlacklist
240403_201951:cmsbot_crab_voRole
240403_201952:cmsbot_crab_voGroup
240403_201953:cmsbot_crab_scheddName
240403_201954:cmsbot_crab_collector
240403_201955:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
240403_201843:cmsbot_crab_20240403_221842
```

Finished at: 2024-04-03 22:19:56
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/744/console)

## Comment (cmsdmwmbot, 2024-04-03T20:43:49Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-04-03 22:43:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/518/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/518//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Getting input files into tmp dir /tmp/tmpt84013vv
Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is QUEUED


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
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


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Fatal error trying to connect to https://cmsweb.cern.ch:8443/crabserver/prod/task?subresource=webdirprx&workflow=240403_201843%3Acmsbot_crab_20240403_221842 using subresource=webdirprx&workflow=240403_201843%3Acmsbot_crab_20240403_221842.
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
Error Id: aab30273b4259e2645796d75fcecac10


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20240403_221842  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Your user certificate is going to expire in 13 days. See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#ObtainingCert 
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.
```

## Comment (cmsdmwmbot, 2024-04-03T20:44:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-04-03 22:44:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1004/console

```
RETRY TESTS:
outputFiles-check.sh 240403_201848:cmsbot_crab_outputFiles - 2
maxJobRuntimeMin-check.sh 240403_201851:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240403_201900:cmsbot_crab_numCores - 2
scriptExe-check.sh 240403_201901:cmsbot_crab_scriptExe - 2
secondaryInputDataset-check.sh 240403_201917:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 240403_201919:cmsbot_crab_lumiMaskUrl - 2
runRange-check.sh 240403_201922:cmsbot_crab_runRange - 2
ignoreLocality-check.sh 240403_201931:cmsbot_crab_ignoreLocality - 2
userInputFiles-check.sh 240403_201932:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240403_201933:cmsbot_crab_whitelist - 2

SUCCESSFUL TESTS:
maxMemoryMB-check.sh 240403_201850:cmsbot_crab_maxMemoryMB - 0
sendVenvFolder-check.sh 240403_201911:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201915:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201915:cmsbot_crab_inputDBS - 0
voRole-check.sh 240403_201951:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_201953:cmsbot_crab_scheddName - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201844:cmsbot_crab_transferOutputs - 1
transferLogs-check.sh 240403_201845:cmsbot_crab_transferLogs - 1
activity-check.sh 240403_201846:cmsbot_crab_activity - 1
inputFiles-check.sh 240403_201847:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240403_201847:cmsbot_crab_disableAutomaticOutputCollection - 1
allowUndistributedCMSSW-check.sh 240403_201849:cmsbot_crab_allowUndistributedCMSSW - 1
scriptArgs-check.sh 240403_201902:cmsbot_crab_scriptArgs - 1
useParent-check.sh 240403_201916:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 240403_201918:cmsbot_crab_lumiMaskFile - 1
outLFNDirBase-check.sh 240403_201921:cmsbot_crab_outLFNDirBase - 1
blacklist-check.sh 240403_201933:cmsbot_crab_blacklist - 1
ignoreGlobalBlacklist-check.sh 240403_201934:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240403_201952:cmsbot_crab_voGroup - 1
collector-check.sh 240403_201954:cmsbot_crab_collector - 1
extraJDL-check.sh 240403_201955:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:10:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2024-04-03 23:10:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1008/console

```
RETRY TESTS:
lumiMaskUrl-check.sh 240403_201919:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240403_201921:cmsbot_crab_outLFNDirBase - 2
userInputFiles-check.sh 240403_201932:cmsbot_crab_userInputFiles - 2
ignoreGlobalBlacklist-check.sh 240403_201934:cmsbot_crab_ignoreGlobalBlacklist - 2

SUCCESSFUL TESTS:
transferLogs-check.sh 240403_201845:cmsbot_crab_transferLogs - 0
activity-check.sh 240403_201846:cmsbot_crab_activity - 0
outputFiles-check.sh 240403_201848:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201849:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_201850:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_201851:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201900:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201901:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240403_201911:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201915:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201915:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240403_201917:cmsbot_crab_secondaryInputDataset - 0
runRange-check.sh 240403_201922:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201931:cmsbot_crab_ignoreLocality - 0
whitelist-check.sh 240403_201933:cmsbot_crab_whitelist - 0
voRole-check.sh 240403_201951:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_201953:cmsbot_crab_scheddName - 0
collector-check.sh 240403_201954:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201844:cmsbot_crab_transferOutputs - 1
inputFiles-check.sh 240403_201847:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240403_201847:cmsbot_crab_disableAutomaticOutputCollection - 1
scriptArgs-check.sh 240403_201902:cmsbot_crab_scriptArgs - 1
useParent-check.sh 240403_201916:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 240403_201918:cmsbot_crab_lumiMaskFile - 1
blacklist-check.sh 240403_201933:cmsbot_crab_blacklist - 1
voGroup-check.sh 240403_201952:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240403_201955:cmsbot_crab_extraJDL - 1
```

## Comment (cmsdmwmbot, 2024-04-03T21:41:13Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2024-04-03 23:41:12
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1012/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferLogs-check.sh 240403_201845:cmsbot_crab_transferLogs - 0
activity-check.sh 240403_201846:cmsbot_crab_activity - 0
outputFiles-check.sh 240403_201848:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240403_201849:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240403_201850:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240403_201851:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240403_201900:cmsbot_crab_numCores - 0
scriptExe-check.sh 240403_201901:cmsbot_crab_scriptExe - 0
sendVenvFolder-check.sh 240403_201911:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240403_201915:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240403_201915:cmsbot_crab_inputDBS - 0
secondaryInputDataset-check.sh 240403_201917:cmsbot_crab_secondaryInputDataset - 0
lumiMaskUrl-check.sh 240403_201919:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240403_201921:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240403_201922:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 240403_201931:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 240403_201932:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240403_201933:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 240403_201934:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 240403_201951:cmsbot_crab_voRole - 0
scheddName-check.sh 240403_201953:cmsbot_crab_scheddName - 0
collector-check.sh 240403_201954:cmsbot_crab_collector - 0

FAILED TESTS:
transferOutputs-check.sh 240403_201844:cmsbot_crab_transferOutputs - 1
inputFiles-check.sh 240403_201847:cmsbot_crab_inputFiles - 1
disableAutomaticOutputCollection-check.sh 240403_201847:cmsbot_crab_disableAutomaticOutputCollection - 1
scriptArgs-check.sh 240403_201902:cmsbot_crab_scriptArgs - 1
useParent-check.sh 240403_201916:cmsbot_crab_useParent - 1
lumiMaskFile-check.sh 240403_201918:cmsbot_crab_lumiMaskFile - 1
blacklist-check.sh 240403_201933:cmsbot_crab_blacklist - 1
voGroup-check.sh 240403_201952:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240403_201955:cmsbot_crab_extraJDL - 1
```
