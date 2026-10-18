# dmwm/CRABServer issue #7642: #390: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2023-05-24T10:23:57Z
Closed: 2023-05-24T14:55:59Z
URL: https://github.com/dmwm/CRABServer/issues/7642

## Opening post (cmsdmwmbot, 2023-05-24T10:23:57Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Validation
- [ ] Client_Configuration_Validation
- [ ] Task_Submission_Status_Tracking

Started at: 2023-05-24 12:23:56
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/390/)

## Comment (cmsdmwmbot, 2023-05-24T10:25:11Z)

Something went wrong during task submission. Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/390/console). None of the downstream jobs were triggered.

## Comment (belforte, 2023-05-24T14:55:53Z)

test  code needed to be updated https://github.com/dmwm/CRABServer/commit/902f56c9c123ccce94f02ca9bf16b0131a43eccb
