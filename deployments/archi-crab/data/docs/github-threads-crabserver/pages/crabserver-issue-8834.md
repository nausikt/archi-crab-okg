# dmwm/CRABServer issue #8834: #900: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-11-26T08:46:41Z
Closed: 2024-11-26T10:58:50Z
URL: https://github.com/dmwm/CRABServer/issues/8834

## Opening post (cmsdmwmbot, 2024-11-26T08:46:41Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
Started at: 2024-11-26 09:46:40
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/900/)

## Comment (cmsdmwmbot, 2024-11-26T08:47:25Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241126_084704:cmsbot_crab_20241126_094702
```

Finished at: 2024-11-26 09:47:04
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/900/console)

## Comment (cmsdmwmbot, 2024-11-26T09:30:29Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-11-26 10:30:27
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/578/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/578//artifact/client-validation.log/*view*/
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
Will use PFN: davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp

Attempting to create (dummy) directory crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25 and copy (dummy) file 1c966c0e-da94-415c-9f8a-6c609f050d25.tmp to /store/user/cmsbot

Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -p -v -t 180 file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp'
Please wait...
Failed running copy command
  Stdout:
    Copying 85 bytes file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp
    event: [1732612735854] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
    event: [1732612735854] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp
    event: [1732612735854] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
    event: [1732612735854] BOTH   http_plugin	PREPARE:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp
    event: [1732612735922] BOTH   http_plugin	PREPARE:EXIT	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp
    event: [1732612735922] BOTH   http_plugin	TRANSFER:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_101853_1c966c0e-da94-415c-9f8a-6c609f050d25/1c966c0e-da94-415c-9f8a-6c609f050d25.tmp
    event: [1732612735922] BOTH   http_plugin	TRANSFER:TYPE	streamed
    WARNING Copy failed with mode streamed: Connection timed out (destination)
    event: [1732612916258] DEST   http_plugin	CLEANUP	0
    event: [1732612916258] BOTH   http_plugin	TRANSFER:EXIT	ERROR: Copy failed (streamed). Last attempt: Connection timed out (destination)
    
  Stderr:
    gfal-copy error: 8 (Exec format error) - TRANSFER ERROR: Copy failed (streamed). Last attempt: Connection timed out (destination)
    

Checkwrite Result:
Unable to check write permission in /store/user/cmsbot on site T2_CH_CERN
Please try again later or contact the site administrators sending them the 'crab checkwrite' output as printed above.
Note: You cannot write to a site if you did not ask permission.
Additional diagnostic info for CERN EOS
== id ==>:
uid=501(cmsbld) gid=501(cmsbld) groups=501(cmsbld),65534(nobody)
== voms-proxy-info -all ==>:
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=4015866037
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC compliant proxy
strength  : 2048 bits
path      : /tmp/x509up_u501
timeleft  : 191:56:48
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/country/Role=NULL/Capability=NULL
attribute : /cms/country/ch/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
timeleft  : 191:56:48
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
Will use PFN: davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp

Attempting to create (dummy) directory crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e and copy (dummy) file 6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp to /store/user/cmsbot

Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -p -v -t 180 -K ADLER32 file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp'
Please wait...
Failed running copy command
  Stdout:
    Copying 85 bytes file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp
    event: [1732612921816] BOTH   GFAL2:CORE:COPY	LIST:ENTER	
    event: [1732612921816] BOTH   GFAL2:CORE:COPY	LIST:ITEM	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp
    event: [1732612921816] BOTH   GFAL2:CORE:COPY	LIST:EXIT	
    event: [1732612921816] BOTH   http_plugin	PREPARE:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp
    event: [1732612921816] SOURCE http_plugin	CHECKSUM:ENTER	
    event: [1732612921816] SOURCE http_plugin	CHECKSUM:EXIT	
    event: [1732612921883] BOTH   http_plugin	PREPARE:EXIT	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp
    event: [1732612921883] BOTH   http_plugin	TRANSFER:ENTER	file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp => davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20241126_102200_6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e/6c5f1046-0f5f-4fcb-b6bc-9d98b818cf1e.tmp
    event: [1732612921883] BOTH   http_plugin	TRANSFER:TYPE	streamed
    WARNING Copy failed with mode streamed: (Neon): SSL handshake failed: Connection timed out during SSL handshake (destination)
    
  Stderr:
    Command timed out after 180 seconds!
    

Checkwrite Result:
Unable to check write permission in /store/user/cmsbot on site T2_CH_CERN
Please try again later or contact the site administrators sending them the 'crab checkwrite' output as printed above.
Note: You cannot write to a site if you did not ask permission.
Additional diagnostic info for CERN EOS
== id ==>:
uid=501(cmsbld) gid=501(cmsbld) groups=501(cmsbld),65534(nobody)
== voms-proxy-info -all ==>:
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=4015866037
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC compliant proxy
strength  : 2048 bits
path      : /tmp/x509up_u501
timeleft  : 191:53:13
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/country/Role=NULL/Capability=NULL
attribute : /cms/country/ch/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
timeleft  : 191:53:13
uri       : voms-cms-auth.app.cern.ch:15000
WARNING uberftp command not found. To get additional diagnostic info
 log on lxplus, get a proxy and execute:
 uberftp eoscmsftp.cern.ch pwd

Command checkwrite failed
```

## Comment (belforte, 2024-11-26T10:58:50Z)

EOS upgrade ?
