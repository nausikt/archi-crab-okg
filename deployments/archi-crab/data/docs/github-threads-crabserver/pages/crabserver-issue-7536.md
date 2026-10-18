# dmwm/CRABServer issue #7536: #375: Test GH CRABClient using preprod REST instance and CMSSW_12_6_0_pre4 CMSSW release

State: closed
Opened: 2023-02-15T20:27:55Z
Closed: 2023-02-17T11:49:30Z
URL: https://github.com/dmwm/CRABServer/issues/7536

## Opening post (cmsdmwmbot, 2023-02-15T20:27:55Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_12_6_0_pre4**
- SCRAM_ARCH: **el8_amd64_gcc10**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-02-15 21:27:54
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/375/)

## Comment (cmsdmwmbot, 2023-02-15T20:30:50Z)

Task submission for **Task_Submission_Status_Tracking** successfully ended.
```
230215_203003:cmsbot_crab_20230215_213002
230215_203004:cmsbot_crab_20230215_213004
230215_203006:cmsbot_crab_20230215_213005
230215_203008:cmsbot_crab_20230215_213007
230215_203009:cmsbot_crab_20230215_213008
230215_203029:cmsbot_crab_20230215_213010
```

Task submission for **Client_Configuration_Validation** successfully ended.
```
230215_202908:cmsbot_crab_transferOutputs
230215_202909:cmsbot_crab_transferLogs
230215_202911:cmsbot_crab_activity
230215_202912:cmsbot_crab_inputFiles
230215_202914:cmsbot_crab_disableAutomaticOutputCollection
230215_202915:cmsbot_crab_outputFiles
230215_202917:cmsbot_crab_allowUndistributedCMSSW
230215_202919:cmsbot_crab_maxMemoryMB
230215_202921:cmsbot_crab_maxJobRuntimeMin
230215_202922:cmsbot_crab_numCores
230215_202924:cmsbot_crab_scriptExe
230215_202925:cmsbot_crab_scriptArgs
230215_202927:cmsbot_crab_sendPythonFolder
230215_202934:cmsbot_crab_sendExternalFolder
230215_202936:cmsbot_crab_inputDBS
230215_202937:cmsbot_crab_useParent
230215_202939:cmsbot_crab_secondaryInputDataset
230215_202940:cmsbot_crab_lumiMaskFile
230215_202942:cmsbot_crab_lumiMaskUrl
230215_202944:cmsbot_crab_outLFNDirBase
230215_202946:cmsbot_crab_runRange
230215_202947:cmsbot_crab_ignoreLocality
230215_202949:cmsbot_crab_userInputFiles
230215_202950:cmsbot_crab_whitelist
230215_202952:cmsbot_crab_blacklist
230215_202953:cmsbot_crab_ignoreGlobalBlacklist
230215_202955:cmsbot_crab_voRole
230215_202956:cmsbot_crab_voGroup
230215_202958:cmsbot_crab_scheddName
230215_202959:cmsbot_crab_collector
230215_203001:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
230215_202906:cmsbot_crab_20230215_212904
```

Finished at: 2023-02-15 21:30:29
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/375/console)

## Comment (cmsdmwmbot, 2023-02-15T20:53:00Z)

**Test:** Client validation
**Result:** SUCCEEDED
**Finished at:** 2023-02-15 21:52:59
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/336/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/336//artifact/client-validation.log/*view*/
**Message:** All commands were executed successfully.

## Comment (cmsdmwmbot, 2023-02-15T20:53:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 21:53:46
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/579/console

```
RETRY TESTS:
maxJobRuntimeMin-check.sh 230215_202921:cmsbot_crab_maxJobRuntimeMin - 2
useParent-check.sh 230215_202937:cmsbot_crab_useParent - 2
secondaryInputDataset-check.sh 230215_202939:cmsbot_crab_secondaryInputDataset - 2
lumiMaskUrl-check.sh 230215_202942:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230215_202944:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230215_202946:cmsbot_crab_runRange - 2
userInputFiles-check.sh 230215_202949:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 230215_202950:cmsbot_crab_whitelist - 2
blacklist-check.sh 230215_202952:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230215_202908:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230215_202909:cmsbot_crab_transferLogs - 0
activity-check.sh 230215_202911:cmsbot_crab_activity - 0
inputFiles-check.sh 230215_202912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230215_202914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230215_202915:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230215_202917:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230215_202919:cmsbot_crab_maxMemoryMB - 0
numCores-check.sh 230215_202922:cmsbot_crab_numCores - 0
scriptExe-check.sh 230215_202924:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230215_202925:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230215_202927:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230215_202934:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230215_202936:cmsbot_crab_inputDBS - 0
lumiMaskFile-check.sh 230215_202940:cmsbot_crab_lumiMaskFile - 0
ignoreLocality-check.sh 230215_202947:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 230215_202953:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230215_202955:cmsbot_crab_voRole - 0
voGroup-check.sh 230215_202956:cmsbot_crab_voGroup - 0
scheddName-check.sh 230215_202958:cmsbot_crab_scheddName - 0
collector-check.sh 230215_202959:cmsbot_crab_collector - 0
extraJDL-check.sh 230215_203001:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-15T21:17:54Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-15 22:17:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/580/console

```
RETRY TESTS:
secondaryInputDataset-check.sh 230215_202939:cmsbot_crab_secondaryInputDataset - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230215_202908:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230215_202909:cmsbot_crab_transferLogs - 0
activity-check.sh 230215_202911:cmsbot_crab_activity - 0
inputFiles-check.sh 230215_202912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230215_202914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230215_202915:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230215_202917:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230215_202919:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230215_202921:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230215_202922:cmsbot_crab_numCores - 0
scriptExe-check.sh 230215_202924:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230215_202925:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230215_202927:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230215_202934:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230215_202936:cmsbot_crab_inputDBS - 0
useParent-check.sh 230215_202937:cmsbot_crab_useParent - 0
lumiMaskFile-check.sh 230215_202940:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230215_202942:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230215_202944:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230215_202946:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230215_202947:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230215_202949:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230215_202950:cmsbot_crab_whitelist - 0
blacklist-check.sh 230215_202952:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230215_202953:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230215_202955:cmsbot_crab_voRole - 0
voGroup-check.sh 230215_202956:cmsbot_crab_voGroup - 0
scheddName-check.sh 230215_202958:cmsbot_crab_scheddName - 0
collector-check.sh 230215_202959:cmsbot_crab_collector - 0
extraJDL-check.sh 230215_203001:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-15T21:34:49Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-02-15 22:34:45
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/433/console

```
{'TN': '230215_203003:cmsbot_crab_20230215_213002', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 19, 'finished': 977, 'transferring': 1, 'running': 3}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_203004:cmsbot_crab_20230215_213004', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 5, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_203006:cmsbot_crab_20230215_213005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_203008:cmsbot_crab_20230215_213007', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203009:cmsbot_crab_20230215_213008', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 7, 'finished': 91, 'running': 2}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_203029:cmsbot_crab_20230215_213010', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-02-15T21:41:48Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 2 out of 4. Test is done.
**Finished at:** 2023-02-15 22:41:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/581/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230215_202908:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230215_202909:cmsbot_crab_transferLogs - 0
activity-check.sh 230215_202911:cmsbot_crab_activity - 0
inputFiles-check.sh 230215_202912:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230215_202914:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230215_202915:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230215_202917:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230215_202919:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230215_202921:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230215_202922:cmsbot_crab_numCores - 0
scriptExe-check.sh 230215_202924:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230215_202925:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230215_202927:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230215_202934:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230215_202936:cmsbot_crab_inputDBS - 0
useParent-check.sh 230215_202937:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230215_202939:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230215_202940:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230215_202942:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230215_202944:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230215_202946:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230215_202947:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230215_202949:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230215_202950:cmsbot_crab_whitelist - 0
blacklist-check.sh 230215_202952:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230215_202953:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230215_202955:cmsbot_crab_voRole - 0
voGroup-check.sh 230215_202956:cmsbot_crab_voGroup - 0
scheddName-check.sh 230215_202958:cmsbot_crab_scheddName - 0
collector-check.sh 230215_202959:cmsbot_crab_collector - 0
extraJDL-check.sh 230215_203001:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (cmsdmwmbot, 2023-02-15T22:38:05Z)

**Test:** Task Submission Status Tracking
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-02-15 23:38:04
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/435/console

```
{'TN': '230215_203003:cmsbot_crab_20230215_213002', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 22, 'finished': 978}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203004:cmsbot_crab_20230215_213004', 'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6, 'running': 1}, 'combinedStatus': 'SUBMITTED'}
{'TN': '230215_203006:cmsbot_crab_20230215_213005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_203008:cmsbot_crab_20230215_213007', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203009:cmsbot_crab_20230215_213008', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 9, 'finished': 91}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203029:cmsbot_crab_20230215_213010', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (cmsdmwmbot, 2023-02-15T23:40:43Z)

**Test:** Task Submission Status Tracking
**Result:** FAILED
**Attempt:** 2 out of 4. Test failed. Investigate manually
**Finished at:** 2023-02-16 00:40:42
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/436/console

```
{'TN': '230215_203003:cmsbot_crab_20230215_213002', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 22, 'finished': 978}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203004:cmsbot_crab_20230215_213004', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 7}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_203006:cmsbot_crab_20230215_213005', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'combinedStatus': 'COMPLETED'}
{'TN': '230215_203008:cmsbot_crab_20230215_213007', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 1, 'finished': 9}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203009:cmsbot_crab_20230215_213008', 'dbStatus': u'SUBMITTED', 'testResult': 'TestFailed', 'jobsPerStatus': {'failed': 9, 'finished': 91}, 'combinedStatus': 'FAILED'}
{'TN': '230215_203029:cmsbot_crab_20230215_213010', 'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'combinedStatus': 'COMPLETED'}
```

## Comment (novicecpp, 2023-02-16T18:29:31Z)

For task [230215_203003:cmsbot_crab_20230215_213002](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=230215_203003:cmsbot_crab_20230215_213002&from=1676489409000&to=now&var-site=All&var-schedd=059&var-cmsUserId=&var-current_url=https:%2F%2Fmonit-grafana.cern.ch%2Fd%2FcmsTMDetail%2Fcms_task_monitoring&var-task_str=cmsbot_crab_20230215_213002&var-status=All&var-crabid=All&var-rest_host=https:%2F%2Fcmsweb.cern.ch) and other tasks that failed in this test, it got 2  errors:
- `8001` https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/230215_203003:cmsbot_crab_20230215_213002/job_out.933.0.txt
```
== CMSSW: An exception of category 'SiteLocalConfigService' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing input source of type PoolSource
== CMSSW:    [2] edm::SiteLocalConfigService::storageDescriptionPath()
== CMSSW: Exception Message:
== CMSSW: Fail to convert path to the storage description, /cvmfs/cms.cern.ch/SITECONF/local/../storage.json, to the canonical absolute path. Path exists?
```
- 50664 https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/230215_203003:cmsbot_crab_20230215_213002/job_out.887.0.txt
```
======== Figuring out long exit code of the job for condor_chirp ========
/srv/condor_exec.exe: line 63: python: command not found
==== Failed to load the long exit code from jobReport.json.887. Falling back to short exit code ====
```

@mapellidario I am not sure if both error is relate to your jobwrapper and your new PR in https://github.com/dmwm/CRABServer/pull/7510.
Could you help me verify this?

## Comment (novicecpp, 2023-02-16T18:34:01Z)

I am not sure if the first error is resolved by your new jobwrapper or not. What I understand for the second error is it will be gone after your PR is merged.

## Comment (belforte, 2023-02-17T10:24:43Z)

this one
```
== CMSSW: Fail to convert path to the storage description, /cvmfs/cms.cern.ch/SITECONF/local/../storage.json, to the canonical absolute path. Path exists?
```
seems to me a problem with the execution site, at least for the job you pointed to. Let me look at full picture.

While this
```
/srv/condor_exec.exe: line 63: python: command not found
```
is IMHO a problem on our side, we should not call `python` in there but only execute `condor_chirp` and let gWMS wrapper do the work as per https://mattermost.web.cern.ch/cms-o-and-c/pl/k4ez7d396if77jmehrj31jzfer

## Comment (belforte, 2023-02-17T10:29:19Z)

btw
```
     

======== Figuring out long exit code of the job for condor_chirp ========
/srv/condor_exec.exe: line 63: python: command not found
==== Failed to load the long exit code from jobReport.json.887. Falling back to short exit code ====
```

is not an error !! And it is not the reason jobs failed. For the scope of this test/validation/release... we should ignore this chirping failures.
I will look later at why jobs failed with 50664

## Comment (belforte, 2023-02-17T10:37:38Z)

To cut long storu short, please use CMSSW_11 or CMSSW_12_(<6) for validation, so we separate things due to coming change of Site Configuration from old xml file to new `storage.json` deployment.
E.g. in the first task you pointed to, the errors with SITECONF (exit code 8001) are all from jobs running at IRFU (a little used site where new config. may not be fully debugged yet) or at RWTH (where I see that config. files in /cvmfs/cms.cern.ch/SITECONF/T2_DE_RWTH/JobConfig have been changed today !)

## Comment (belforte, 2023-02-17T10:49:16Z)

the second job which @novicecpp pointed to, which failed with exit code 50664, hit the 1 hour running time limit specified in the configuration. Indicating that something (likely data access) went stuck in the execution. Usually a resubmission fixes this.
Telling flags:
1. last line of job stdout: `Job Running time in seconds:  3601`
2. from the [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes): `50664 - Application terminated by wrapper because using too much Wall Clock time `. Also from [cmsweb](https://cmsweb.cern.ch:8443/exitcodes/50664) also [via curl](https://github.com/vkuznet/CMSExitCodes#readme)

## Comment (novicecpp, 2023-02-17T11:08:45Z)

> the second job which @novicecpp pointed to, which failed with exit code 50664, hit the 1 hour running time limit specified in the configuration. Indicating that something (likely data access) went stuck in the execution. Usually a resubmission fixes this. Telling flags:
> 
>     1. last line of job stdout: `Job Running time in seconds:  3601`
> 
>     2. from the [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes): `50664 - Application terminated by wrapper because using too much Wall Clock time `. Also from [cmsweb](https://cmsweb.cern.ch:8443/exitcodes/50664) also [via curl](https://github.com/vkuznet/CMSExitCodes#readme)

Ops, I am sorry. 
I was confuse it with jobwrapper's issue, completely ignore what does exit code 50664 mean.
Could/Should we improve job's log to point out that it exceed execution time?

## Comment (belforte, 2023-02-17T11:09:27Z)

we should add a resubmit step to Jenkins. I do not find an issue with that. But there are so many open issues about Jenkins that we need to cleanup.

## Comment (belforte, 2023-02-17T11:17:08Z)

>  Could/Should we improve job's log to point out that it exceed execution time?

hmm... `crab status --verboseError` does that.  Are you saying that we should have an explicit line at the bottom of job stdout ?
yes, @mapellidario  can take care as part of https://github.com/dmwm/CRABServer/issues/7529 and take similar care for jobs killed by using too much RAM.
But the best thing we can do, given that "hang during I/O and hit max time" is sadly frequent, is to add an automatic resubmission by PostJob (part of famous: improve retry policies)

I leave it to you guys to update/open GH issues as proper.

## Comment (novicecpp, 2023-02-17T11:49:30Z)

I still have some questions about new `storage.json`  but let discuss in MM.
Thanks Stefano for looking at it!

Well, all failed jobs is just transient. Everything works fine.
