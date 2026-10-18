# dmwm/CRABServer issue #8216: #697: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-02-01T21:41:01Z
Closed: 2024-02-02T09:47:58Z
URL: https://github.com/dmwm/CRABServer/issues/8216

## Opening post (cmsdmwmbot, 2024-02-01T21:41:01Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-02-01 22:41:00
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/697/)

## Comment (cmsdmwmbot, 2024-02-01T21:43:30Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240201_214121:cmsbot_crab_transferOutputs
240201_214123:cmsbot_crab_transferLogs
240201_214125:cmsbot_crab_activity
240201_214127:cmsbot_crab_inputFiles
240201_214129:cmsbot_crab_disableAutomaticOutputCollection
240201_214131:cmsbot_crab_outputFiles
240201_214133:cmsbot_crab_allowUndistributedCMSSW
240201_214135:cmsbot_crab_maxMemoryMB
240201_214137:cmsbot_crab_maxJobRuntimeMin
240201_214139:cmsbot_crab_numCores
240201_214141:cmsbot_crab_scriptExe
240201_214143:cmsbot_crab_scriptArgs
240201_214145:cmsbot_crab_sendVenvFolder
240201_214232:cmsbot_crab_sendExternalFolder
240201_214234:cmsbot_crab_inputDBS
240201_214236:cmsbot_crab_useParent
240201_214238:cmsbot_crab_secondaryInputDataset
240201_214240:cmsbot_crab_lumiMaskFile
240201_214242:cmsbot_crab_lumiMaskUrl
240201_214245:cmsbot_crab_outLFNDirBase
240201_214248:cmsbot_crab_runRange
240201_214250:cmsbot_crab_ignoreLocality
240201_214252:cmsbot_crab_userInputFiles
240201_214254:cmsbot_crab_whitelist
240201_214256:cmsbot_crab_blacklist
240201_214258:cmsbot_crab_ignoreGlobalBlacklist
240201_214300:cmsbot_crab_voRole
240201_214302:cmsbot_crab_voGroup
240201_214304:cmsbot_crab_scheddName
240201_214306:cmsbot_crab_collector
240201_214308:cmsbot_crab_extraJDL
```

Finished at: 2024-02-01 22:43:09
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/697/console)

## Comment (cmsdmwmbot, 2024-02-01T22:06:51Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-02-01 23:06:50
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/919/console

```
RETRY TESTS:
outputFiles-check.sh 240201_214131:cmsbot_crab_outputFiles - 2
maxMemoryMB-check.sh 240201_214135:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 240201_214137:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 240201_214139:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 240201_214240:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 240201_214242:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 240201_214245:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 240201_214248:cmsbot_crab_runRange - 2
userInputFiles-check.sh 240201_214252:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 240201_214254:cmsbot_crab_whitelist - 2
blacklist-check.sh 240201_214256:cmsbot_crab_blacklist - 2
voRole-check.sh 240201_214300:cmsbot_crab_voRole - 2
extraJDL-check.sh 240201_214308:cmsbot_crab_extraJDL - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 240201_214121:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240201_214127:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240201_214129:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 240201_214133:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 240201_214145:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240201_214232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240201_214234:cmsbot_crab_inputDBS - 0
useParent-check.sh 240201_214236:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240201_214238:cmsbot_crab_secondaryInputDataset - 0
scheddName-check.sh 240201_214304:cmsbot_crab_scheddName - 0
collector-check.sh 240201_214306:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240201_214123:cmsbot_crab_transferLogs - 1
activity-check.sh 240201_214125:cmsbot_crab_activity - 1
scriptExe-check.sh 240201_214141:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240201_214143:cmsbot_crab_scriptArgs - 1
ignoreLocality-check.sh 240201_214250:cmsbot_crab_ignoreLocality - 1
ignoreGlobalBlacklist-check.sh 240201_214258:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240201_214302:cmsbot_crab_voGroup - 1
```

## Comment (cmsdmwmbot, 2024-02-01T22:31:31Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-01 23:31:30
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/920/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240201_214121:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240201_214127:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240201_214129:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240201_214131:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240201_214133:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240201_214135:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240201_214137:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240201_214139:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240201_214145:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240201_214232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240201_214234:cmsbot_crab_inputDBS - 0
useParent-check.sh 240201_214236:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240201_214238:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240201_214240:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240201_214242:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240201_214245:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240201_214248:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240201_214252:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240201_214254:cmsbot_crab_whitelist - 0
blacklist-check.sh 240201_214256:cmsbot_crab_blacklist - 0
voRole-check.sh 240201_214300:cmsbot_crab_voRole - 0
scheddName-check.sh 240201_214304:cmsbot_crab_scheddName - 0
collector-check.sh 240201_214306:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240201_214123:cmsbot_crab_transferLogs - 1
activity-check.sh 240201_214125:cmsbot_crab_activity - 1
scriptExe-check.sh 240201_214141:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240201_214143:cmsbot_crab_scriptArgs - 1
ignoreLocality-check.sh 240201_214250:cmsbot_crab_ignoreLocality - 1
ignoreGlobalBlacklist-check.sh 240201_214258:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240201_214302:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240201_214308:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-02-02T00:09:50Z)

odd errors in uploading info to ASO DB for direct stageout

## Comment (cmsdmwmbot, 2024-02-02T08:37:49Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 0 out of 4. Test failed. Investigate manually
**Finished at:** 2024-02-02 09:37:48
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/921/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 240201_214121:cmsbot_crab_transferOutputs - 0
inputFiles-check.sh 240201_214127:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 240201_214129:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 240201_214131:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 240201_214133:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 240201_214135:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 240201_214137:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 240201_214139:cmsbot_crab_numCores - 0
sendVenvFolder-check.sh 240201_214145:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 240201_214232:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 240201_214234:cmsbot_crab_inputDBS - 0
useParent-check.sh 240201_214236:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 240201_214238:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 240201_214240:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 240201_214242:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 240201_214245:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 240201_214248:cmsbot_crab_runRange - 0
userInputFiles-check.sh 240201_214252:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 240201_214254:cmsbot_crab_whitelist - 0
blacklist-check.sh 240201_214256:cmsbot_crab_blacklist - 0
voRole-check.sh 240201_214300:cmsbot_crab_voRole - 0
scheddName-check.sh 240201_214304:cmsbot_crab_scheddName - 0
collector-check.sh 240201_214306:cmsbot_crab_collector - 0

FAILED TESTS:
transferLogs-check.sh 240201_214123:cmsbot_crab_transferLogs - 1
activity-check.sh 240201_214125:cmsbot_crab_activity - 1
scriptExe-check.sh 240201_214141:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 240201_214143:cmsbot_crab_scriptArgs - 1
ignoreLocality-check.sh 240201_214250:cmsbot_crab_ignoreLocality - 1
ignoreGlobalBlacklist-check.sh 240201_214258:cmsbot_crab_ignoreGlobalBlacklist - 1
voGroup-check.sh 240201_214302:cmsbot_crab_voGroup - 1
extraJDL-check.sh 240201_214308:cmsbot_crab_extraJDL - 1
```

## Comment (belforte, 2024-02-02T08:42:38Z)

I restared CCV and got again same failures, so it was not a REST gltch...pfff
Have submitted a new CCV test, but I fear something is wrong in PostJob

## Comment (belforte, 2024-02-02T09:33:52Z)

got a bunch of failures again https://github.com/dmwm/CRABServer/issues/8217
running PJ with debug looks like it fails when file was stageout directly (job runs at same site as destination) since there is nothing for ASO todo.
But this is nothing new

## Comment (belforte, 2024-02-02T09:38:15Z)

problem comes from changing this line
https://github.com/dmwm/CRABServer/blob/b0bbfa37e47af042600053819dfeb3ef6d8539b4/src/python/TaskWorker/Actions/PostJob.py#L522
to
```python
if not self.docs_in_transfer:
```
That variable is set to `False` or to `None` to indicate different situations :
https://github.com/dmwm/CRABServer/blob/b0bbfa37e47af042600053819dfeb3ef6d8539b4/src/python/TaskWorker/Actions/PostJob.py#L522-L527

The bug came from trying to please `pylint`  ...pfff...
