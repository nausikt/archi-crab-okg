# dmwm/CRABServer issue #8176: #676: Test dev CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-12T14:18:44Z
Closed: 2024-01-12T15:17:37Z
URL: https://github.com/dmwm/CRABServer/issues/8176

## Opening post (cmsdmwmbot, 2024-01-12T14:18:44Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2024-01-12 15:18:43
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/676/)

## Comment (cmsdmwmbot, 2024-01-12T14:23:41Z)

Something went wrong during task submission. Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/676/console). None of the downstream jobs were triggered.

## Comment (belforte, 2024-01-12T15:17:37Z)

submission of RucioASO tests was failing with dev client. See #8179
