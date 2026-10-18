# dmwm/CRABClient pull request #5384: make submit dryrun work with TW v3.250401 Fix #5383

State: closed
Opened: 2025-04-09T15:21:35Z
Closed: 2025-04-09T15:26:52Z
Merged: 2025-04-09T15:26:51Z
URL: https://github.com/dmwm/CRABClient/pull/5384

## Opening post (belforte, 2025-04-09T15:21:35Z)

after this:
```console
belforte@lxplus813/TC3> crab submit --dryrun 
Will use CRAB configuration file crabConfig.py
Importing CMSSW configuration dummyanalyzer.py
Finished importing CMSSW configuration dummyanalyzer.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 250409_151806:belforte_crab_20250409_171801
Project dir: ./crab_20250409_171801
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: NEW
Please wait...
Task status: UPLOADED

Dry run
Getting input files into tmp dir /tmp/belforte/tmpk4p3vqb_
Copying and preparing files for local execution in /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_171801/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute rest run in local sub-directory of ./crab_20250409_171801
Executing test, please wait...
Last trial took only 9.5 seconds. We are trying now with 216 events
Last trial took only 16.7 seconds. We are trying now with 932 events

Using LumiBased splitting
Task consists of 30 jobs to process 300 lumis
The longest job will process 10 lumis, with an estimated processing time of 1 minutes
The average job will process 10 lumis, with an estimated processing time of 1 minutes
The shortest job will process 10 lumis, with an estimated processing time of 1 minutes
The estimated memory requirement is 1248 MB

Timing quantities given below are ESTIMATES. Keep in mind that external factors
such as transient file-access delays can reduce estimate reliability.

For ~480 minute jobs, use:
Data.unitsPerJob = 3459
You will need to submit a new task

Dry run requested: task paused
To continue processing, use 'crab proceed'

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_171801/crab.log
belforte@lxplus813/TC3> 
```

## Comment (cmsdmwmbot, 2025-04-09T15:23:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 2 warnings
   * 109 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1106/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-09T15:24:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 2 warnings
   * 109 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1107/artifact/artifacts/PullRequestReport.html
