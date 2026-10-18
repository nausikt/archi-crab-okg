# dmwm/CRABServer issue #7690: #401: Test prod CRABClient using preprod REST instance and CMSSW_12_6_4 CMSSW release

State: closed
Opened: 2023-06-28T08:57:44Z
Closed: 2023-07-08T15:40:48Z
URL: https://github.com/dmwm/CRABServer/issues/7690

## Opening post (cmsdmwmbot, 2023-06-28T08:57:44Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 1 out of 4. Will run again.
**Finished at:** 2023-06-28 10:57:43
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/625/console

```
RETRY TESTS:
blacklist-check.sh 230628_080900:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 230628_080804:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 230628_080808:cmsbot_crab_transferLogs - 0
activity-check.sh 230628_080817:cmsbot_crab_activity - 0
inputFiles-check.sh 230628_080819:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 230628_080822:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 230628_080824:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 230628_080825:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 230628_080827:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 230628_080829:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 230628_080831:cmsbot_crab_numCores - 0
scriptExe-check.sh 230628_080833:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 230628_080834:cmsbot_crab_scriptArgs - 0
sendPythonFolder-check.sh 230628_080835:cmsbot_crab_sendPythonFolder - 0
sendExternalFolder-check.sh 230628_080843:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 230628_080845:cmsbot_crab_inputDBS - 0
useParent-check.sh 230628_080846:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 230628_080847:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 230628_080849:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 230628_080851:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 230628_080853:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 230628_080855:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 230628_080856:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 230628_080858:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 230628_080859:cmsbot_crab_whitelist - 0
ignoreGlobalBlacklist-check.sh 230628_080902:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 230628_080903:cmsbot_crab_voRole - 0
voGroup-check.sh 230628_080905:cmsbot_crab_voGroup - 0
scheddName-check.sh 230628_080906:cmsbot_crab_scheddName - 0
collector-check.sh 230628_080908:cmsbot_crab_collector - 0
extraJDL-check.sh 230628_080909:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```
