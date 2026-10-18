# dmwm/CRABServer issue #8833: #899: Test dev CRABClient using preprod REST instance and CMSSW_10_6_26 CMSSW release

State: closed
Opened: 2024-11-26T08:45:27Z
Closed: 2024-11-26T14:18:52Z
URL: https://github.com/dmwm/CRABServer/issues/8833

## Opening post (cmsdmwmbot, 2024-11-26T08:45:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_6_26**
- SCRAM_ARCH: **slc7_amd64_gcc700**

**Tests started:**

- [x] Client_Validation
- [x] Client_Configuration_Validation
Started at: 2024-11-26 09:45:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/899/)

## Comment (cmsdmwmbot, 2024-11-26T08:46:33Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
241126_084547:cmsbot_crab_transferOutputs
241126_084548:cmsbot_crab_transferLogs
241126_084549:cmsbot_crab_activity
241126_084550:cmsbot_crab_inputFiles
241126_084550:cmsbot_crab_disableAutomaticOutputCollection
241126_084551:cmsbot_crab_outputFiles
241126_084552:cmsbot_crab_allowUndistributedCMSSW
241126_084553:cmsbot_crab_maxMemoryMB
241126_084553:cmsbot_crab_maxJobRuntimeMin
241126_084554:cmsbot_crab_numCores
241126_084555:cmsbot_crab_scriptExe
241126_084556:cmsbot_crab_scriptArgs
241126_084556:cmsbot_crab_sendVenvFolder
241126_084557:cmsbot_crab_sendExternalFolder
241126_084558:cmsbot_crab_inputDBS
241126_084559:cmsbot_crab_useParent
241126_084559:cmsbot_crab_secondaryInputDataset
241126_084600:cmsbot_crab_lumiMaskFile
241126_084601:cmsbot_crab_lumiMaskUrl
241126_084602:cmsbot_crab_outLFNDirBase
241126_084603:cmsbot_crab_runRange
241126_084604:cmsbot_crab_ignoreLocality
241126_084605:cmsbot_crab_userInputFiles
241126_084606:cmsbot_crab_whitelist
241126_084606:cmsbot_crab_blacklist
241126_084607:cmsbot_crab_ignoreGlobalBlacklist
241126_084608:cmsbot_crab_voRole
241126_084609:cmsbot_crab_voGroup
241126_084609:cmsbot_crab_scheddName
241126_084610:cmsbot_crab_collector
241126_084611:cmsbot_crab_extraJDL
```

Task submission for **Client_Validation_Suite** successfully ended.
```
241126_084546:cmsbot_crab_20241126_094545
```

Finished at: 2024-11-26 09:46:11
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/899/console)

## Comment (cmsdmwmbot, 2024-11-26T09:13:48Z)

**Test:** Client configuration validation
**Result:** FULL-STATUS-UNKNOWN
**Attempt:** 0 out of 4. Will run again.
**Finished at:** 2024-11-26 10:13:47
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1251/console

```
RETRY TESTS:
maxMemoryMB-check.sh 241126_084553:cmsbot_crab_maxMemoryMB - 2
maxJobRuntimeMin-check.sh 241126_084553:cmsbot_crab_maxJobRuntimeMin - 2
numCores-check.sh 241126_084554:cmsbot_crab_numCores - 2
scriptExe-check.sh 241126_084555:cmsbot_crab_scriptExe - 2
scriptArgs-check.sh 241126_084556:cmsbot_crab_scriptArgs - 2
lumiMaskFile-check.sh 241126_084600:cmsbot_crab_lumiMaskFile - 2
lumiMaskUrl-check.sh 241126_084601:cmsbot_crab_lumiMaskUrl - 2
outLFNDirBase-check.sh 241126_084602:cmsbot_crab_outLFNDirBase - 2
runRange-check.sh 241126_084603:cmsbot_crab_runRange - 2
userInputFiles-check.sh 241126_084605:cmsbot_crab_userInputFiles - 2
whitelist-check.sh 241126_084606:cmsbot_crab_whitelist - 2
blacklist-check.sh 241126_084606:cmsbot_crab_blacklist - 2

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_084547:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_084548:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_084549:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_084550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_084550:cmsbot_crab_disableAutomaticOutputCollection - 0
allowUndistributedCMSSW-check.sh 241126_084552:cmsbot_crab_allowUndistributedCMSSW - 0
sendVenvFolder-check.sh 241126_084556:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_084557:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_084558:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_084559:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_084559:cmsbot_crab_secondaryInputDataset - 0
ignoreLocality-check.sh 241126_084604:cmsbot_crab_ignoreLocality - 0
ignoreGlobalBlacklist-check.sh 241126_084607:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_084608:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_084609:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_084609:cmsbot_crab_scheddName - 0
collector-check.sh 241126_084610:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_084611:cmsbot_crab_extraJDL - 0

FAILED TESTS:
outputFiles-check.sh 241126_084551:cmsbot_crab_outputFiles - 1
```

## Comment (cmsdmwmbot, 2024-11-26T09:18:16Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-26 10:18:14
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/577/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/577//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab checkwrite  --site=T2_CH_CERN  --proxy=/tmp/x509up_u501  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Will check write permission in the default location /store/user/<username>
Validating LFN /store/user/cmsbot...
LFN /store/user/cmsbot is valid.
Will use `gfal-copy`, `gfal-rm` commands for checking write permissions
Will check write permission in /store/user/cmsbot on site T2_CH_CERN
Will use PFN: davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp

Attempting to create (dummy) directory crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a and copy (dummy) file 9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp to /store/user/cmsbot

Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -p -v -t 180 file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp'
Please wait...
Failed running copy command
  Stdout:
    Copying 85 bytes file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp
    event: [1732612071815] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
    event: [1732612071815] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp
    event: [1732612071815] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
    event: [1732612071815] BOTH   http_plugin	PREPARE:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp
    event: [1732612071882] BOTH   http_plugin	PREPARE:EXIT	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp
    event: [1732612071882] BOTH   http_plugin	TRANSFER:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_100750_9822da66-e76b-4da6-a404-1a4b04e0c39a/9822da66-e76b-4da6-a404-1a4b04e0c39a.tmp
    event: [1732612071883] BOTH   http_plugin	TRANSFER:TYPE	streamed
    WARNING Copy failed with mode streamed: Connection timed out (destination)
    WARNING When trying to clean the destination: DavPosix::unlink  Result HTTP 500 : Unexpected server error: 500  after 1 attempts
    event: [1732612252155] DEST   http_plugin	CLEANUP	5
    event: [1732612252155] BOTH   http_plugin	TRANSFER:EXIT	ERROR: Copy failed (streamed). Last attempt: Connection timed out (destination)
    
  Stderr:
    gfal-copy error: 8 (Exec format error) - TRANSFER ERROR: Copy failed (streamed). Last attempt: Connection timed out (destination)
    

Checkwrite Result:
Unable to check write permission in /store/user/cmsbot on site T2_CH_CERN
Please try again later or contact the site administrators sending them the 'crab checkwrite' output as printed above.
Note: You cannot write to a site if you did not ask permission.
Additional diagnostic info for CERN EOS
== id ==>:
uid=501(cmsbld) gid=501(cmsbld) groups=501(cmsbld),65534
== voms-proxy-info -all ==>:
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=2695253535
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC compliant proxy
strength  : 2048 bits
path      : /tmp/x509up_u501
timeleft  : 191:56:50
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/country/Role=NULL/Capability=NULL
attribute : /cms/country/ch/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
timeleft  : 191:56:50
uri       : voms-cms-auth.app.cern.ch:15000
WARNING uberftp command not found. To get additional diagnostic info
 log on lxplus, get a proxy and execute:
 uberftp eoscmsftp.cern.ch pwd

Command checkwrite failed


TEST_COMMAND: crab checkwrite  --site=T2_CH_CERN  --proxy=/tmp/x509up_u501  --checksum=yes  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account cmsbot
Will check write permission in the default location /store/user/<username>
Validating LFN /store/user/cmsbot...
LFN /store/user/cmsbot is valid.
Will use `gfal-copy`, `gfal-rm` commands for checking write permissions
Will check write permission in /store/user/cmsbot on site T2_CH_CERN
Will use PFN: davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp

Attempting to create (dummy) directory crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26 and copy (dummy) file 960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp to /store/user/cmsbot

Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -p -v -t 180 -K ADLER32 file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp'
Please wait...
Failed running copy command
  Stdout:
    WARNING (SEToken) Could not retrieve any token for davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    WARNING (SEToken) Could not retrieve any token for davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    Copying 85 bytes file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    event: [1732612256542] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
    event: [1732612256542] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    event: [1732612256542] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
    event: [1732612256542] BOTH   http_plugin	PREPARE:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    event: [1732612256542] SOURCE http_plugin	CHECKSUM:ENTER	
    event: [1732612256543] SOURCE http_plugin	CHECKSUM:EXIT	
    WARNING (SEToken) Could not retrieve any token for davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101055_960b703e-6a74-4b16-8ae4-8eabc941cf26/960b703e-6a74-4b16-8ae4-8eabc941cf26.tmp
    
  Stderr:
    gfal-copy error: 5 (Input/output error) - DESTINATION OVERWRITE   Result HTTP 500 : Unexpected server error: 500  after 1 attempts
    

Checkwrite Result:
Unable to check write permission in /store/user/cmsbot on site T2_CH_CERN
Please try again later or contact the site administrators sending them the 'crab checkwrite' output as printed above.
Note: You cannot write to a site if you did not ask permission.
Additional diagnostic info for CERN EOS
== id ==>:
uid=501(cmsbld) gid=501(cmsbld) groups=501(cmsbld),65534
== voms-proxy-info -all ==>:
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=2695253535
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC compliant proxy
strength  : 2048 bits
path      : /tmp/x509up_u501
timeleft  : 191:56:46
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/country/Role=NULL/Capability=NULL
attribute : /cms/country/ch/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
timeleft  : 191:56:46
uri       : voms-cms-auth.app.cern.ch:15000
WARNING uberftp command not found. To get additional diagnostic info
 log on lxplus, get a proxy and execute:
 uberftp eoscmsftp.cern.ch pwd

Command checkwrite failed
```

## Comment (cmsdmwmbot, 2024-11-26T09:36:57Z)

**Test:** Client configuration validation
**Result:** SUCCEEDED
**Attempt:** 1 out of 4. Test is done.
**Finished at:** 2024-11-26 10:36:56
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1252/console

```
RETRY TESTS:
 none

SUCCESSFUL TESTS:
transferOutputs-check.sh 241126_084547:cmsbot_crab_transferOutputs - 0
transferLogs-check.sh 241126_084548:cmsbot_crab_transferLogs - 0
activity-check.sh 241126_084549:cmsbot_crab_activity - 0
inputFiles-check.sh 241126_084550:cmsbot_crab_inputFiles - 0
disableAutomaticOutputCollection-check.sh 241126_084550:cmsbot_crab_disableAutomaticOutputCollection - 0
outputFiles-check.sh 241126_084551:cmsbot_crab_outputFiles - 0
allowUndistributedCMSSW-check.sh 241126_084552:cmsbot_crab_allowUndistributedCMSSW - 0
maxMemoryMB-check.sh 241126_084553:cmsbot_crab_maxMemoryMB - 0
maxJobRuntimeMin-check.sh 241126_084553:cmsbot_crab_maxJobRuntimeMin - 0
numCores-check.sh 241126_084554:cmsbot_crab_numCores - 0
scriptExe-check.sh 241126_084555:cmsbot_crab_scriptExe - 0
scriptArgs-check.sh 241126_084556:cmsbot_crab_scriptArgs - 0
sendVenvFolder-check.sh 241126_084556:cmsbot_crab_sendVenvFolder - 0
sendExternalFolder-check.sh 241126_084557:cmsbot_crab_sendExternalFolder - 0
inputDBS-check.sh 241126_084558:cmsbot_crab_inputDBS - 0
useParent-check.sh 241126_084559:cmsbot_crab_useParent - 0
secondaryInputDataset-check.sh 241126_084559:cmsbot_crab_secondaryInputDataset - 0
lumiMaskFile-check.sh 241126_084600:cmsbot_crab_lumiMaskFile - 0
lumiMaskUrl-check.sh 241126_084601:cmsbot_crab_lumiMaskUrl - 0
outLFNDirBase-check.sh 241126_084602:cmsbot_crab_outLFNDirBase - 0
runRange-check.sh 241126_084603:cmsbot_crab_runRange - 0
ignoreLocality-check.sh 241126_084604:cmsbot_crab_ignoreLocality - 0
userInputFiles-check.sh 241126_084605:cmsbot_crab_userInputFiles - 0
whitelist-check.sh 241126_084606:cmsbot_crab_whitelist - 0
blacklist-check.sh 241126_084606:cmsbot_crab_blacklist - 0
ignoreGlobalBlacklist-check.sh 241126_084607:cmsbot_crab_ignoreGlobalBlacklist - 0
voRole-check.sh 241126_084608:cmsbot_crab_voRole - 0
voGroup-check.sh 241126_084609:cmsbot_crab_voGroup - 0
scheddName-check.sh 241126_084609:cmsbot_crab_scheddName - 0
collector-check.sh 241126_084610:cmsbot_crab_collector - 0
extraJDL-check.sh 241126_084611:cmsbot_crab_extraJDL - 0

FAILED TESTS:
 none
```

## Comment (belforte, 2024-11-26T14:18:52Z)

EOS glitch
