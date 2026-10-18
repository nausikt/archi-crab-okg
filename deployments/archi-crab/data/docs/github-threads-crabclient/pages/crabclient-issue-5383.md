# dmwm/CRABClient issue #5383: crab submit --dryrun fails with No such file or directory: 'JobArgs-1.json'

State: closed
Opened: 2025-04-09T13:55:00Z
Closed: 2025-04-09T15:26:53Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5383

## Opening post (belforte, 2025-04-09T13:55:00Z)

see https://github.com/dmwm/CRABServer/issues/9039

current crab client v3.250318 fails with
```text
Getting input files into tmp dir /tmp/belforte/tmpgsfz43sw
Copying and preparing files for local execution in /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_142311/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute rest run in local sub-directory of ./crab_20250409_142311
Executing test, please wait...
ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'JobArgs-1.json'
```

the client log:
```text
INFO 2025-04-09 13:49:03.805 UTC: 	 Copying and preparing files for local execution in /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_154757/local
DEBUG 2025-04-09 13:49:03.953 UTC: 	 Executing command :
 cd /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250409_154757/local; tar xf CMSRunAnalysis.tar.gz
DEBUG 2025-04-09 13:49:04.044 UTC: 	 output : 
 error: 
 retcode : 0
DEBUG 2025-04-09 13:49:04.044 UTC: 	 Creating run_job.sh file
INFO 2025-04-09 13:49:04.047 UTC: 	 go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
INFO 2025-04-09 13:49:04.048 UTC: 	 Execute rest run in local sub-directory of ./crab_20250409_154757
INFO 2025-04-09 13:49:04.049 UTC: 	 Executing test, please wait...
ERROR 2025-04-09 13:49:04.052 UTC: 	 Unhandled Exception!
ERROR 2025-04-09 13:49:04.052 UTC: 	 [Errno 2] No such file or directory: 'JobArgs-1.json'
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/bin/crab.py", line 157, in <module>
    client()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/bin/crab.py", line 142, in __call__
    returnDict = self.cmd()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/lib/CRABClient/Commands/submit.py", line 168, in __call__
    self.printDryRunResults(*self.executeTestRun(filecacheurl, uniquerequestname, projDir))
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/lib/CRABClient/Commands/submit.py", line 445, in executeTestRun
    setCMSRunAnalysisOpts(events=events)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/lib/CRABClient/Commands/submit.py", line 548, in setCMSRunAnalysisOpts
    with open('JobArgs-1.json', 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'JobArgs-1.json'
ERROR 2025-04-09 13:49:04.057 UTC: 	 ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'JobArgs-1.json'
ERROR 2025-04-09 13:49:04.057 UTC: 
```

## Comment (belforte, 2025-04-09T14:12:04Z)

OTOH, `cd .../local + sh run_job.sh 1` works.
