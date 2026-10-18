# dmwm/CRABServer issue #8032: #561: Test GH CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-11-30T11:17:00Z
Closed: 2023-11-30T14:40:07Z
URL: https://github.com/dmwm/CRABServer/issues/8032

## Opening post (cmsdmwmbot, 2023-11-30T11:17:00Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
231130_111638:cmsbot_crab_20231130_121636
```

Finished at: 2023-11-30 12:16:39
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/561/console)

## Comment (cmsdmwmbot, 2023-11-30T11:40:37Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2023-11-30 12:40:36
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/429/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/429//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Getting input files into tmp dir /tmp/tmpz5kzijho
Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=webdirprx&workflow=231130_111638%3Acmsbot_crab_20231130_121636 using subresource=webdirprx&workflow=231130_111638%3Acmsbot_crab_20231130_121636.
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
Error Id: 812c0b738e9edd5f10ca0dc8c6955e6b


TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.
Error: Status information is unavailable, will not proceed with the report. Try again a few minutes later if the task has just been submitted.


TEST_COMMAND: crab getlog  --quantity=2  --short --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=webdirprx&workflow=231130_111638%3Acmsbot_crab_20231130_121636 using subresource=webdirprx&workflow=231130_111638%3Acmsbot_crab_20231130_121636.
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
Error Id: 973cd62df01e1c94e9537f7ba1a0379c


TEST_COMMAND: crab getlog  --quantity=2   --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --xrootd --jobids=2,3  --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=1  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.


TEST_COMMAND: crab getoutput  --quantity=3  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir   --checksum=no  --proxy=/tmp/x509up_u501  --dir=crab_20231130_121636  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
Error while getting status information. Got:
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB' 
Cannot retrieve job list from the status command.
```
