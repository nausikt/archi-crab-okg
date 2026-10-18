# dmwm/CRABServer issue #7694: #403: Test dev CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-06-29T14:37:39Z
Closed: 2023-06-29T20:15:39Z
URL: https://github.com/dmwm/CRABServer/issues/7694

## Opening post (cmsdmwmbot, 2023-06-29T14:37:39Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-06-29 16:37:38
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/403/)

## Comment (cmsdmwmbot, 2023-06-29T14:40:05Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
230629_143815:cmsbot_crab_transferOutputs
230629_143817:cmsbot_crab_transferLogs
230629_143819:cmsbot_crab_activity
230629_143820:cmsbot_crab_inputFiles
230629_143821:cmsbot_crab_disableAutomaticOutputCollection
230629_143822:cmsbot_crab_outputFiles
230629_143824:cmsbot_crab_allowUndistributedCMSSW
230629_143825:cmsbot_crab_maxMemoryMB
230629_143826:cmsbot_crab_maxJobRuntimeMin
230629_143827:cmsbot_crab_numCores
230629_143829:cmsbot_crab_scriptExe
230629_143830:cmsbot_crab_scriptArgs
230629_143831:cmsbot_crab_sendPythonFolder
230629_143920:cmsbot_crab_sendExternalFolder
230629_143921:cmsbot_crab_inputDBS
230629_143922:cmsbot_crab_useParent
230629_143924:cmsbot_crab_secondaryInputDataset
230629_143925:cmsbot_crab_lumiMaskFile
230629_143926:cmsbot_crab_lumiMaskUrl
230629_143929:cmsbot_crab_outLFNDirBase
230629_143930:cmsbot_crab_runRange
230629_143931:cmsbot_crab_ignoreLocality
230629_143933:cmsbot_crab_userInputFiles
230629_143934:cmsbot_crab_whitelist
230629_143935:cmsbot_crab_blacklist
230629_143936:cmsbot_crab_ignoreGlobalBlacklist
230629_143938:cmsbot_crab_voRole
230629_143939:cmsbot_crab_voGroup
230629_143940:cmsbot_crab_scheddName
230629_143942:cmsbot_crab_collector
230629_143943:cmsbot_crab_extraJDL
```

Finished at: 2023-06-29 16:39:44
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/403/console)

## Comment (cmsdmwmbot, 2023-06-29T15:01:52Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2023-06-29 17:01:51
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/629/console

```
RETRY TESTS:
numCores-check.sh 230629_143827:cmsbot_crab_numCores - 2
lumiMaskFile-check.sh 230629_143925:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 230629_143926:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 230629_143929:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 230629_143930:cmsbot_crab_runRange - 2
whitelist-check.sh 230629_143934:cmsbot_crab_whitelist - 2
blacklist-check.sh 230629_143935:cmsbot_crab_blacklist - 2
voRole-check.sh 230629_143938:cmsbot_crab_voRole - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_143815:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_143817:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_143819:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_143820:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_143821:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_143822:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_143824:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_143825:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_143826:cmsbot_crab_maxJobRuntimeMin - 0
scriptExe-check.sh 230629_143829:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230629_143831:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_143920:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_143921:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_143922:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_143924:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 230629_143931:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_143933:cmsbot_crab_userInputFiles - 0
ignoreGlobalBlacklist-check.sh 230629_143936:cmsbot_crab_ignoreGlobalBlacklist - 0
voGroup-check.sh 230629_143939:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_143940:cmsbot_crab_scheddName - 0
collector-check.sh 230629_143942:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_143943:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230629_143830:cmsbot_crab_scriptArgs - 1
```

## Comment (cmsdmwmbot, 2023-06-29T15:23:51Z)

**Test:** Client configuration validation
**Result:** FAILED
**Attempt:** 1 out of 4. Test failed. Investigate manually
**Finished at:** 2023-06-29 17:23:49
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/630/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 230629_143815:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230629_143817:cmsbot_crab_transferLogs - 0
activity-check.sh 230629_143819:cmsbot_crab_activity - 0
inputFiles-check.sh 230629_143820:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230629_143821:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230629_143822:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230629_143824:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230629_143825:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230629_143826:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230629_143827:cmsbot_crab_numCores - 0
scriptExe-check.sh 230629_143829:cmsbot_crab_scriptExe - 0
sendPythonFolder-check.sh 230629_143831:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230629_143920:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230629_143921:cmsbot_crab_inputDBS - 0
useParent-check.sh 230629_143922:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230629_143924:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230629_143925:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230629_143926:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230629_143929:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230629_143930:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230629_143931:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230629_143933:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230629_143934:cmsbot_crab_whitelist - 0
blacklist-check.sh 230629_143935:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 230629_143936:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230629_143938:cmsbot_crab_voRole - 0
voGroup-check.sh 230629_143939:cmsbot_crab_voGroup - 0
scheddName-check.sh 230629_143940:cmsbot_crab_scheddName - 0
collector-check.sh 230629_143942:cmsbot_crab_collector - 0
extraJDL-check.sh 230629_143943:cmsbot_crab_extraJDL - 0

FAILED TESTS:
scriptArgs-check.sh 230629_143830:cmsbot_crab_scriptArgs - 1
```

## Comment (belforte, 2023-06-29T19:31:41Z)

scriptArgs test failed.
error is odd an unusual, in [job stdout](https://cmsweb.cern.ch:8443/scheddmon/0195/cmsbot/230629_143830:cmsbot_crab_scriptArgs/job_out.1.0.txt)
```
== CMSSW: ============ SB CMSRUN starting =================
== CMSSW: ====== arg checking: $1 = 1exitCode=666
== CMSSW: ====== arg checking: $2 = gotArgs=Yes
== CMSSW: ====== arg checking: $3 =
== CMSSW: ============ SB CMSRUN finished =================
```
the first arg line should have been:
```
== CMSSW: ====== arg checking: $1 = exitCode=666
```
given that in the same log we have
```
+ python3 CMSRunAnalysis.py -r /srv -a sandbox.tar.gz [...] --scriptExe=SIMPLE-SCRIPT.sh --scriptArgs=["exitCode=666", "gotArgs=Yes"]' 
```
and
```
scriptArgs:     ["exitCode=666", "gotArgs=Yes"]
```

more investigation is needed

## Comment (belforte, 2023-06-29T19:37:11Z)

testing via preparelocal fails miserably with some problem in "double quote escaping" area. so that we end with 
```
 python3 CMSRunAnalysis.py [...] --scriptArgs=[\"\"exitCode=666\"\",' '\"\"gotArgs=Yes\"\"]'
```
and that fails to load as a Json
```
Expecting value: line 1 column 2 (char 1)
ERROR: Traceback follows:
 Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 658, in <module>
    f"{' '.join(json.loads(options.scriptArgs))}"
```

I submitted same test to prod TW: https://github.com/dmwm/CRABServer/issues/7695

## Comment (belforte, 2023-06-29T19:53:07Z)

production TW works 
https://cmsweb.cern.ch:8443/scheddmon/0155/cmsbot/230629_193615:cmsbot_crab_scriptArgs/job_out.1.0.txt
has the expected content

```
== CMSSW: ============ SB CMSRUN starting =================
== CMSSW: ====== arg checking: $1 = 1
== CMSSW: ====== arg checking: $2 = exitCode=666
== CMSSW: ====== arg checking: $3 = gotArgs=Yes
== CMSSW: ============ SB CMSRUN finished =================
```

## Comment (belforte, 2023-06-29T20:09:23Z)

Problem should have happened when [changing](https://github.com/dmwm/CRABServer/pull/7681/files#diff-f3e914fc7aec95cdce05f5f70c6ea588bc5ab861e029b46c309b28086c7d7297R663-R664)
https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/scripts/CMSRunAnalysis.py#L652-L653 to
```python
 cmd += os.getcwd() + f"/{options.scriptExe} {options.jobNumber}" +\
                   f"{' '.join(json.loads(options.scriptArgs))}"
```
indeed the  `" "` separating jobNumber fron scritpArgs got lost :-(
