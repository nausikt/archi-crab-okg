# dmwm/CRABClient issue #5430: crab recover fails on split-by-lumi-no-publication

State: open
Opened: 2026-09-01T15:42:05Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5430

## Opening post (belforte, 2026-09-01T15:42:05Z)

ref https://cms-talk.web.cern.ch/t/crab-recover-for-automatic-splitting/148004

```console
hwchung@cmslpc328 ~/nobackup/CMSSW_15_0_16/src/b2g/customNano/allAltCrabCfgs/crab_projects # crab recover -d crab_Name_customNano_WWto4Q_2024_2026JUL 
Collecting information about original task ...
Rucio client intialized for account chungh
WARNING - crab report - The original task had publication disabled. recovery strategy changed to notFinished
Warning:: Inconsistent/unusable information from cmsRun FJR's.
 Fall back to counting processed files from imput list. Counting of processed events is not possible
Will put report files in directory /uscms_data/d3/hwchung/CMSSW_15_0_16/src/b2g/customNano/allAltCrabCfgs/crab_projects/crab_Name_customNano_WWto4Q_2024_2026JUL/results
Summary from successful jobs (i.e. in status 'finished'):
  Number of files processed: 3299
  Number of events read: n/a
  Number of events written in EDM files: n/a
  Number of events written in TFileService files: n/a
  Number of events written in other type of files: n/a
  Processed lumis written to processedLumis.json
  Warning: 'notFinished' lumis written to notFinishedLumis.json
           The 'notFinished' lumis were calculated as: the lumis to process minus the processed lumis.
  Files to process written to filesToProcess.json
  Files processed by successful jobs written to processedFiles.json
  Files processed by failed jobs written to failedFiles.json
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
Prepare recovery task ...
ERROR: KeyError: 'notProcessedLumis'

 Look for more details in crab.log file /uscms_data/d3/hwchung/CMSSW_15_0_16/src/b2g/customNano/allAltCrabCfgs/crab_projects/crab_Name_customNano_WWto4Q_2024_2026JUL/crab.log
  If you can't figure out the problem, please send email to
    cmstalk+computing-tools@dovecotmta.cern.ch with the crab.log file or crab.log URL.
  Please use 'crab uploadlog' to upload the log file /uscms_data/d3/hwchung/CMSSW_15_0_16/src/b2g/customNano/allAltCrabCfgs/crab_projects/crab_Name_customNano_WWto4Q_2024_2026JUL/crab.log to the CRAB cache.
```

in crab.log
```text
INFO 2026-09-01 15:41:13.086 UTC: 	 Prepare recovery task ...
DEBUG 2026-09-01 15:41:13.086 UTC: 	 Retrieving username ...
DEBUG 2026-09-01 15:41:13.086 UTC: 	 Retrieving username from CRIC...
DEBUG 2026-09-01 15:41:13.955 UTC: 	 username is belforte
ERROR 2026-09-01 15:41:14.026 UTC: 	 Unhandled Exception!
ERROR 2026-09-01 15:41:14.026 UTC: 	 'notProcessedLumis'
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.260630.00/bin/crab.py", line 157, in <module>
    client()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.260630.00/bin/crab.py", line 142, in __call__
    returnDict = self.cmd()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.260630.00/lib/CRABClient/Commands/recover.py", line 127, in __call__
    retval = self.stepBuildLumiRecoveryInfo(taskReport)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.260630.00/lib/CRABClient/Commands/recover.py", line 566, in stepBuildLumiRecoveryInfo
    if not retval["notProcessedLumis"]:
KeyError: 'notProcessedLumis'
```

relevant code
https://github.com/dmwm/CRABClient/blob/970fabd75d6895b1434c9d4cca0b0ebeff426f4b/src/python/CRABClient/Commands/recover.py#L559-L566
