# dmwm/CRABServer issue #8208: Event processing broken in last PR

State: closed
Opened: 2024-01-30T21:33:35Z
Closed: 2024-01-31T19:53:59Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8208

## Opening post (belforte, 2024-01-30T21:33:35Z)

after PR #8198 cmsRun does not run on any event and no output file is produced.

## Comment (belforte, 2024-01-30T22:03:13Z)

with new code in the PSet after tweaking
```
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(0)
```
white before it was `input = cms.untracked.int32(-1)`

## Comment (belforte, 2024-01-30T22:08:05Z)

which comes from Tweaking. This should be -1 but with new code is 0
```
> ==== Tweak PSet at Tue Jan 30 21:57:35 2024 UTC ====
502c501
< Set attribute process.maxEvents.input to cms.untracked.int32(-1)
---
> Set attribute process.maxEvents.input to cms.untracked.int32(0)
507,509c506,509
< ==== Tweak PSet Done at Tue Jan 30 21:56:57 2024 UTC ====
```

## Comment (belforte, 2024-01-30T22:12:15Z)

Note the difference in parameter dump from CMSRunAnalysis.py

**OLD**
```
==== Parameters Dump at Tue Jan 30 21:56:50 2024 UTC ===
archiveJob:     sandbox.tar.gz
runDir:         /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20240130_225403/local
sourceURL:      https://cmsweb-test2.cern.ch/S3/crabcache_dev
jobNumber:      1
cmsswVersion:   CMSSW_13_3_0
scramArch:      el8_amd64_gcc12
inputFile       job_input_file_list_1.txt
outFiles:       {}
runAndLumis:    job_lumis_1.json
lheInputFiles:  False
firstEvent:     None
firstLumi:      None
eventsPerLumi:  None
lastEvent:      None
firstRun:       None
seeding:        AutomaticSeeding
userFiles:      None
oneEventMode:   0
scriptExe:      SIMPLE-SCRIPT.sh
scriptArgs:     []
maxRuntime:     -1
===================
```

**NEW**
```
==== Parameters Dump at Tue Jan 30 21:57:29 2024 UTC ===
archiveJob:     sandbox.tar.gz
sourceURL:      https://cmsweb-test2.cern.ch/S3/crabcache_dev
jobNumber:      1
cmsswVersion:   CMSSW_13_3_0
scramArch:      el8_amd64_gcc12
inputFile       job_input_file_list_1.txt
outFiles:       {}
runAndLumis:    job_lumis_1.json
lheInputFiles:  False
firstEvent:     0
firstLumi:      None
eventsPerLumi:  None
lastEvent:      -1
firstRun:       None
seeding:        AutomaticSeeding
userFiles:      None
oneEventMode:   0
scriptExe:      SIMPLE-SCRIPT.sh
scriptArgs:     ['exitCode=666', 'gotArgs=Yes']
maxRuntime:     -1
===================
```

Let's ignore difference in `scriptArgs`. I had to remove them for OLD in order to be able to use preparelocal

## Comment (belforte, 2024-01-31T13:52:50Z)

with above commit
```
==== CMSRunAnalysis.py STARTING at Wed Jan 31 13:39:10 2024 UTC ====
Local time : Wed Jan 31 14:39:10 2024
==== Parameters Dump at Wed Jan 31 13:39:10 2024 UTC ===
archiveJob:     sandbox.tar.gz
sourceURL:      https://cmsweb-test2.cern.ch/S3/crabcache_dev
jobNumber:      1
cmsswVersion:   CMSSW_13_3_0
scramArch:      el8_amd64_gcc12
inputFile       job_input_file_list_1.txt
outFiles:       {}
runAndLumis:    job_lumis_1.json
lheInputFiles:  False
firstEvent:     None
firstLumi:      None
eventsPerLumi:  None
lastEvent:      None
firstRun:       None
seeding:        AutomaticSeeding
userFiles:      None
oneEventMode:   0
scriptExe:      SIMPLE-SCRIPT.sh
scriptArgs:     ['exitCode=666', 'gotArgs=Yes']
maxRuntime:     -1
===================

```
