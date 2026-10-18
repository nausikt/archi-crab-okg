# dmwm/CRABServer issue #8730: #845: Test GH CRABClient using prod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-10-01T09:52:51Z
Closed: 2024-10-10T22:42:36Z
URL: https://github.com/dmwm/CRABServer/issues/8730

## Opening post (cmsdmwmbot, 2024-10-01T09:52:51Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **prod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**
- CRABServer_tag: **v3.240904**

**Tests started:**

- [ ] Client_Validation
Started at: 2024-10-01 11:52:50
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/845/)

## Comment (cmsdmwmbot, 2024-10-01T09:53:37Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
241001_095316:cmsbot_crab_20241001_115315
```

Finished at: 2024-10-01 11:53:16
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/845/console)

## Comment (cmsdmwmbot, 2024-10-01T10:17:55Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2024-10-01 12:17:53
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/548/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/548//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20241001_115315  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Command recover failed


TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=241001_095316:cmsbot_crab_20241001_115315  --instance=prod  
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20241001_115315/.requestcache not created, because it already exists.
Rucio client intialized for account cmsbot
step kill - task already killed
Command recover failed
```
