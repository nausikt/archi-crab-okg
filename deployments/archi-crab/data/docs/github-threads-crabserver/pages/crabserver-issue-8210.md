# dmwm/CRABServer issue #8210: #692: Test prod CRABClient using test2 REST instance and CMSSW_13_0_2 CMSSW release

State: closed
Opened: 2024-01-31T14:04:32Z
Closed: 2024-01-31T15:07:26Z
URL: https://github.com/dmwm/CRABServer/issues/8210

## Opening post (cmsdmwmbot, 2024-01-31T14:04:32Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **prod**
- REST_Instance: **test2**
- CMSSW_release: **CMSSW_13_0_2**
- SCRAM_ARCH: **el8_amd64_gcc11**

**Tests started:**

- [ ] Client_Configuration_Validation
Started at: 2024-01-31 15:04:31
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/692/)

## Comment (cmsdmwmbot, 2024-01-31T14:06:52Z)

Task submission for **Client_Configuration_Validation** successfully ended.
```
240131_140451:cmsbot_crab_transferOutputs
240131_140454:cmsbot_crab_transferLogs
240131_140456:cmsbot_crab_activity
240131_140458:cmsbot_crab_inputFiles
240131_140500:cmsbot_crab_disableAutomaticOutputCollection
240131_140502:cmsbot_crab_outputFiles
240131_140504:cmsbot_crab_allowUndistributedCMSSW
240131_140506:cmsbot_crab_maxMemoryMB
240131_140508:cmsbot_crab_maxJobRuntimeMin
240131_140510:cmsbot_crab_numCores
240131_140512:cmsbot_crab_scriptExe
240131_140514:cmsbot_crab_scriptArgs
240131_140516:cmsbot_crab_sendVenvFolder
240131_140556:cmsbot_crab_sendExternalFolder
240131_140558:cmsbot_crab_inputDBS
240131_140600:cmsbot_crab_useParent
240131_140602:cmsbot_crab_secondaryInputDataset
240131_140604:cmsbot_crab_lumiMaskFile
240131_140606:cmsbot_crab_lumiMaskUrl
240131_140609:cmsbot_crab_outLFNDirBase
240131_140611:cmsbot_crab_runRange
240131_140612:cmsbot_crab_ignoreLocality
240131_140614:cmsbot_crab_userInputFiles
240131_140616:cmsbot_crab_whitelist
240131_140618:cmsbot_crab_blacklist
240131_140620:cmsbot_crab_ignoreGlobalBlacklist
240131_140622:cmsbot_crab_voRole
240131_140624:cmsbot_crab_voGroup
240131_140626:cmsbot_crab_scheddName
240131_140628:cmsbot_crab_collector
240131_140630:cmsbot_crab_extraJDL
```

Finished at: 2024-01-31 15:06:31
Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/692/console)

## Comment (belforte, 2024-01-31T15:07:26Z)

CCV test does not run. Try again.
