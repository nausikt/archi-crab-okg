# dmwm/CRABClient issue #5299: make it clear when user's config has an error

State: closed
Opened: 2024-03-31T12:45:56Z
Closed: 2025-06-24T13:30:52Z
Labels: enhancement, Support, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5299

## Opening post (belforte, 2024-03-31T12:45:56Z)

the user only got this at the console
```
Importing CMSSW configuration crab_configs_singleLep2016UL/runFWLJMet_shifts_XX1400H800.py
ERROR: IndexError: list index out of range
```

while the log is more clear, but nobody looks at it
```
DEBUG 2024-03-31 00:13:01.694 UTC: 	 self.config.JobType.psetName: crab_configs_singleLep2016UL/runFWLJMet_shifts_XX1400H200.py
INFO 2024-03-31 00:13:01.694 UTC: 	 Importing CMSSW configuration crab_configs_singleLep2016UL/runFWLJMet_shifts_XX1400H200.py
ERROR 2024-03-31 00:13:01.877 UTC: 	 Unhandled Exception!
ERROR 2024-03-31 00:13:01.877 UTC: 	 list index out of range
Traceback (most recent call last):
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02830/share/cms/crab-dev/v3.240216.00/bin/crab.py", line 152, in <module>
    client()
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02830/share/cms/crab-dev/v3.240216.00/bin/crab.py", line 137, in __call__
    returnDict = self.cmd()
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02830/share/cms/crab-dev/v3.240216.00/lib/CRABClient/Commands/submit.py", line 107, in __call__
    dummy_inputfiles, jobconfig = plugjobtype.run(filecacheurl)
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02830/share/cms/crab-dev/v3.240216.00/lib/CRABClient/JobType/Analysis.py", line 92, in run
    userConfig=self.config.JobType.psetName)
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02830/share/cms/crab-dev/v3.240216.00/lib/CRABClient/JobType/CMSSWConfig.py", line 87, in __init__
    self.fullConfig = imp.load_module(cfgBaseName, configFile, pathname, description)
  File "/uscms_data/d3/fsimpson/scratch/CMSSW_10_6_29/src/FWLJMET/LJMet/CRAB3/crab_configs_singleLep2016UL/runFWLJMet_shifts_XX1400H200.py", line 172, in <module>
    process.GlobalTag = GlobalTag(process.GlobalTag, "", "106X_mcRun2_asymptotic_v17" )
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_29/python/Configuration/AlCa/GlobalTag.py", line 113, in GlobalTag
    record     = entry[1]
IndexError: list index out of range
ERROR 2024-03-31 00:13:01.878 UTC: 	 ERROR: IndexError: list index out of range
ERROR 2024-03-31 00:13:01.878 UTC: 	 
	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
ERROR 2024-03-31 00:13:01.878 UTC: 	 	Client Version: v3.240216
```

We should print that info to the console when an exception happens importing user's config.

## Comment (belforte, 2025-06-23T17:13:48Z)

CRAB Client does an intricate dance with stdout and logger in order to send all messages to log file, and I could not find a way to print traceback to console.
Best I could do is to add a couple lines to stdout and improve a bit the final message about asking help
```console
belforte@lxplus800/TC3> crab submit 
Will use CRAB configuration file crabConfig.py
Importing CMSSW configuration dummyanalyzer.py
ERROR: python exception inside CMSSW configuration file dummyanalyzer
 name 'b' is not defined
ERROR: NameError: name 'b' is not defined

 Look for more details in crab.log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250623_191128/crab.log
  If you can't figure out the problem, please send email to
	cmstalk+computing-tools@dovecotmta.cern.ch with the crab.log file or crab.log URL.
  Please use 'crab uploadlog' to upload the log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250623_191128/crab.log to the CRAB cache.
belforte@lxplus800/TC3> 
```

while the log has the gory details
```text
DEBUG 2025-06-23 17:11:30.662 UTC: 	 self.config.JobType.psetName: dummyanalyzer.py
INFO 2025-06-23 17:11:30.662 UTC: 	 Importing CMSSW configuration dummyanalyzer.py
ERROR 2025-06-23 17:11:30.759 UTC: 	 ERROR: python exception inside CMSSW configuration file dummyanalyzer
 name 'b' is not defined
ERROR 2025-06-23 17:11:30.762 UTC: 	 Unhandled Exception!
ERROR 2025-06-23 17:11:30.762 UTC: 	 name 'b' is not defined
Traceback (most recent call last):
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 157, in <module>
    client()
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 142, in __call__
    returnDict = self.cmd()
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/Commands/submit.py", line 108, in __call__
    dummy_inputfiles, jobconfig = plugjobtype.run(filecacheurl)
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/Analysis.py", line 92, in run
    self.cmsswCfg = CMSSWConfig(config=self.config, logger=self.logger,
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py", line 89, in __init__
    raise e
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py", line 85, in __init__
    self.fullConfig = load_module(cfgBaseName, modRef)
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/__init__.py", line 38, in load_module
    return imp.load_module(moduleName, moduleObj[0],
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-4612d00f9f0430a19291545f1e47b4a4/lib/python3.9/imp.py", line 234, in load_module
    return load_source(name, filename, file)
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-4612d00f9f0430a19291545f1e47b4a4/lib/python3.9/imp.py", line 171, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 711, in _load
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/afs/cern.ch/work/b/belforte/CRAB3/TC3/dummyanalyzer.py", line 5, in <module>
    a=b
NameError: name 'b' is not defined
ERROR 2025-06-23 17:11:30.763 UTC: 	 ERROR: NameError: name 'b' is not defined
ERROR 2025-06-23 17:11:30.763 UTC: 	 
 Look for more details in crab.log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250623_191128/crab.log
ERROR 2025-06-23 17:11:30.763 UTC: 	   If you can't figure out the problem, please send email to
ERROR 2025-06-23 17:11:30.763 UTC: 	 	cmstalk+computing-tools@dovecotmta.cern.ch with the crab.log file or crab.log URL.
ERROR 2025-06-23 17:11:30.763 UTC: 	   Please use 'crab uploadlog' to upload the log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250623_191128/crab.log to the CRAB cache.
```

## Comment (aspiringmind-code, 2025-06-24T08:06:19Z)

> CRAB Client does an intricate dance with stdout and logger in order to send all messages to log file, and I could not find a way to print traceback to console. 

Did you try using `traceback.print_exception(exc_type, exc_value, tback, file=sys.__stderr__)` at the end of `log_exception` near line 118? 
`sys.__stderr__` is the original terminal — not redirected by initLoggers().
So this guarantees the traceback shows in the shell even if the loggers only write to a file.

## Comment (belforte, 2025-06-24T08:21:48Z)

😲 
**THANK YOU**

## Comment (belforte, 2025-06-24T09:43:29Z)

thanks @aspiringmind-code .  console output now is as desired. [1]
But I preferred to add this explicit traceback only in this case where the problem is clearly in the user file, rather than doing every time if I were to put it in the `CRABClient/log_exception` method. Somehow sticking to the original idea that user errors are handled and "clearly reported", while uncaught exceptions indicate a bug and are better kept inside log only, so that users
 1. are not confused
 2. are encouraged to send us full log, so we can understand, rather than just one or two lines

[1]
```console
belforte@lxplus800/TC3> crab submit 
Will use CRAB configuration file crabConfig.py
Importing CMSSW configuration dummyanalyzer.py
ERROR: python exception inside CMSSW configuration file dummyanalyzer
 name 'b' is not defined
Traceback (most recent call last):
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py", line 88, in __init__
    self.fullConfig = load_module(cfgBaseName, modRef)
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/__init__.py", line 38, in load_module
    return imp.load_module(moduleName, moduleObj[0],
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-4612d00f9f0430a19291545f1e47b4a4/lib/python3.9/imp.py", line 234, in load_module
    return load_source(name, filename, file)
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-4612d00f9f0430a19291545f1e47b4a4/lib/python3.9/imp.py", line 171, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 711, in _load
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/afs/cern.ch/work/b/belforte/CRAB3/TC3/dummyanalyzer.py", line 5, in <module>
    a=b
NameError: name 'b' is not defined
ERROR: NameError: name 'b' is not defined

 Look for more details in crab.log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250624_113656/crab.log
  If you can't figure out the problem, please send email to
	cmstalk+computing-tools@dovecotmta.cern.ch with the crab.log file or crab.log URL.
  Please use 'crab uploadlog' to upload the log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250624_113656/crab.log to the CRAB cache.
belforte@lxplus800/TC3> 
```

## Comment (aspiringmind-code, 2025-06-24T10:13:53Z)

Understood, thanks!
