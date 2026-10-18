# dmwm/CRABServer issue #9202: wrong SCRAM_ARCH used in StatusTracking in build pipeline

State: closed
Opened: 2025-10-02T12:21:29Z
Closed: 2025-10-13T06:47:22Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9202

## Opening post (belforte, 2025-10-02T12:21:29Z)

e.g. in https://gitlab.cern.ch/crab3/CRABServer/-/jobs/62477747/raw

(DEBUG) CMSSW_release=CMSSW_9_4_21
(DEBUG) SCRAM_ARCH=el8_amd64_gcc11

but our https://github.com/dmwm/CRABServer/blob/v3.251002/test/testingConfigs has
`CMSSW_release=CMSSW_9_4_21;SCRAM_ARCH=slc7_amd64_gcc630`

and indeed later on in the pipeline log

```

++ scramv1 project CMSSW_9_4_21
ERROR: Project "CMSSW" version "CMSSW_9_4_21" is not available for arch el8_amd64_gcc11.
       Please make sure you have used the correct name/version.
       You can run "scram list $projectname" to get the list of available versions.
+ ERR=true
statusTracking.sh script failed to run properly.
+ '[' true == true ']'
+ echo 'statusTracking.sh script failed to run properly.'
+ exit 1
Command fail with exit code 1 (1/10 attempted)
Unexpected error. Exit code: 1
```

other non-SL8 releases also fail, most likely for same reason

<img width="289" height="432" alt="Image" src="https://github.com/user-attachments/assets/1c3cad69-940d-45ca-9b5e-cc503b4bd358" />

## Comment (belforte, 2025-10-10T12:29:20Z)

@aspiringmind-code I leaave it to you to prioritize your issues, just please do not leave this for next year :-)

## Comment (aspiringmind-code, 2025-10-12T06:02:03Z)

@belforte Thanks for catching this. Fix done!

## Comment (aspiringmind-code, 2025-10-13T06:54:31Z)

Further problems in the status tracking will be followed in [Issue 9213](https://github.com/dmwm/CRABServer/issues/9213)
