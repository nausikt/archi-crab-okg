# dmwm/CRABServer issue #8996: #942: Test GH CRABClient using preprod REST instance and CMSSW_11_3_4 CMSSW release

State: closed
Opened: 2025-03-19T08:31:27Z
Closed: 2025-03-19T15:24:33Z
URL: https://github.com/dmwm/CRABServer/issues/8996

## Opening post (cmsdmwmbot, 2025-03-19T08:31:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_11_3_4**
- SCRAM_ARCH: **slc7_amd64_gcc900**
- CRABServer_tag: **v3.250310**

**Tests started:**

- [x] Client_Validation
Started at: 2025-03-19 09:31:26
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/942/)

## Comment (cmsdmwmbot, 2025-03-19T08:32:16Z)

Task submission for **Client_Validation_Suite** successfully ended.
```
250319_083154:cmsbot_crab_20250319_093150
```

Finished at: 2025-03-19 09:31:55
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/942/console)

## Comment (cmsdmwmbot, 2025-03-19T08:56:21Z)

**Test:** Client validation
**Result:** FAILED
**Finished at:** 2025-03-19 09:56:19
**Test log:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/608/console
**All executed commands:** https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/608//artifact/client-validation.log/*view*/
**Message:** Some CRABClient commands failed. Find failed commands below:
```
TEST_COMMAND: crab checkwrite  --site=T2_CH_CERN  --proxy=/tmp/x509up_u501  
^[[33;1m2025-03-19 09:54:15,868	WARNING	Waiting 0.5s due to reason: server returned 503 ^[[0m
^[[33;1m2025-03-19 09:54:16,374	WARNING	Waiting 1.0s due to reason: server returned 503 ^[[0m
^[[33;1m2025-03-19 09:54:18,052	WARNING	Waiting 0.25s due to reason: server returned 503 ^[[0m
^[[33;1m2025-03-19 09:54:18,308	WARNING	Waiting 0.5s due to reason: server returned 503 ^[[0m
^[[33;1m2025-03-19 09:54:18,815	WARNING	Waiting 1.0s due to reason: server returned 503 ^[[0m
TEST_RESULT: FAILED                                                                                 
TEST_MESSAGE:
Rucio client could not be intialized, some funcionalities may not work
Will check write permission in the default location /store/user/<username>
Validating LFN /store/user/cmsbot...
LFN /store/user/cmsbot is valid.
Will use `gfal-copy`, `gfal-rm` commands for checking write permissions
Will check write permission in /store/user/cmsbot on site T2_CH_CERN
An unknown exception occurred.
Details: no error information passed (http status code: 503)
Command checkwrite failed
```

## Comment (nausikt, 2025-03-19T15:24:33Z)

Succeed with this attempt #9002
