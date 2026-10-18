# dmwm/CRABServer issue #9084: Check argument is integer for run_job.sh

State: closed
Opened: 2025-05-20T09:59:17Z
Closed: 2025-05-20T13:43:37Z
URL: https://github.com/dmwm/CRABServer/issues/9084

## Opening post (aspiringmind-code, 2025-05-20T09:59:17Z)

When running dryrun option with submit, while doing local execution, show an error message that the argument NUMJOB should be integer when running `sh run_job.sh NUMJOB` if not set properly
```

Dry run
Getting input files into tmp dir /tmp/vchakrav/tmpeszxywe7
Copying and preparing files for local execution in /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250520_113725/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute test run in local sub-directory of ./crab_20250520_113725
```

## Comment (belforte, 2025-05-20T13:13:10Z)

I am not sure I understand.
Do you mean that `run_job.sh` should print a warning and exit if NUMJOB is missing or not an integer ?
That'd be something to change in CRABClient.

## Comment (aspiringmind-code, 2025-05-20T13:43:37Z)

Oops...created in wrong repo. New issue in [CRABClient](https://github.com/dmwm/CRABClient/issues/5390)
