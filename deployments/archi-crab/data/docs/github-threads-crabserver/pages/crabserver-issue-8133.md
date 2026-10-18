# dmwm/CRABServer issue #8133: #644: Test dev CRABClient using preprod REST instance and CMSSW_9_4_21 CMSSW release

State: closed
Opened: 2023-12-20T09:28:27Z
Closed: 2023-12-20T11:30:55Z
URL: https://github.com/dmwm/CRABServer/issues/8133

## Opening post (cmsdmwmbot, 2023-12-20T09:28:27Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **dev**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_9_4_21**
- SCRAM_ARCH: **slc7_amd64_gcc630**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2023-12-20 10:28:27
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/644/)

## Comment (cmsdmwmbot, 2023-12-20T09:29:03Z)

Something went wrong during task submission. Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/644/console). None of the downstream jobs were triggered.

## Comment (mapellidario, 2023-12-20T11:30:55Z)

seems to be related to https://github.com/dmwm/CRABServer/issues/8127, which is understood and fixed. closing
