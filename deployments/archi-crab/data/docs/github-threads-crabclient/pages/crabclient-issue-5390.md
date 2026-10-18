# dmwm/CRABClient issue #5390: Check argument is integer for run_job.sh

State: closed
Opened: 2025-05-20T13:43:01Z
Closed: 2025-05-22T08:38:52Z
Labels: Done
URL: https://github.com/dmwm/CRABClient/issues/5390

## Opening post (aspiringmind-code, 2025-05-20T13:43:01Z)

When running dryrun option with submit, while doing local execution, show an error message that the argument NUMJOB should be integer when running `sh run_job.sh NUMJOB` if not set properly.
```
Dry run
Getting input files into tmp dir /tmp/vchakrav/tmpeszxywe7
Copying and preparing files for local execution in /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250520_113725/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute test run in local sub-directory of ./crab_20250520_113725
```

## Comment (belforte, 2025-05-20T13:48:20Z)

@aspiringmind-code your bash skills are superior to mine. Can you suggest how to change these lines ?
I could possiblly handle 'make sure $1 is present' but ensuring an integer is beyond me.

https://github.com/dmwm/CRABClient/blob/673eae270d71b8e4d28ed858ba37d65d8ca49960/src/python/CRABClient/Commands/preparelocal.py#L117-L129

## Comment (aspiringmind-code, 2025-05-21T07:40:10Z)

We can add something like `[[ "$1" =~ ^[0-9]+$ ]] || { echo "Usage: $0 <numeric job_id>"; exit 1; }` to indicate the usage of the script on failure.
