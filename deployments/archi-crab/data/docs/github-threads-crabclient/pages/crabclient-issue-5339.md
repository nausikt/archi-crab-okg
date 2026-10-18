# dmwm/CRABClient issue #5339: client v3.240930 does not work with production TW v3.240904

State: closed
Opened: 2024-10-24T08:49:29Z
Closed: 2024-10-24T14:00:25Z
URL: https://github.com/dmwm/CRABClient/issues/5339

## Opening post (belforte, 2024-10-24T08:49:29Z)

when investigating https://cms-talk.web.cern.ch/t/cmssw-crab-ci-tests-are-failing-for-last-2-days/55653 we discovered that https://github.com/dmwm/CRABClient/issues/5332 only works with modified TW's CMSRunAnalysis.py as per https://github.com/dmwm/CRABServer/pull/8704

The problem is that after moving user's scram files in the `CMSSW_X_Y_Z` directory in the sandbox, the current TW code expands the sandbox "early", so creates a partial `CMSSW_X_Y_X` directory which confuses subsequent WMCore's `scram_project()`. The latter actually calls `scramv1 project` a.k.a. `cmsrel` and the problem can be very simply reproduced as follows where `sanbox.tar.gz` is the file sent to the job wrapper as e.g. retrieved by `crab preparelocal`

```
belforte@lxplus825/belforte> pwd
/tmp/belforte
belforte@lxplus825/belforte> ls
sandbox.tar.gz
belforte@lxplus825/belforte> tar xf sandbox.tar.gz 
belforte@lxplus825/belforte> ls
CMSSW_13_3_0/  PSet.pkl  PSet.py  PSetDump.py  sandbox.tar.gz
belforte@lxplus825/belforte> cmsrel CMSSW_13_3_0
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/bin/scram.py", line 114, in <module>
    main()
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/bin/scram.py", line 109, in main
    if not execcommand(args, opts):
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/bin/scram.py", line 103, in execcommand
    return eval('scram_commands.cmd_%s' % cmds[0])(args, opts)
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/SCRAM/Core/CMD.py", line 58, in cmd_project
    return process(args)
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/SCRAM/Core/Commands/project.py", line 71, in process
    return project_bootfromrelease(project.upper(), version, releasePath, opts)
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/SCRAM/Core/Commands/project.py", line 116, in project_bootfromrelease
    area = relarea.satellite(installdir, installname, symlink, Core().localarea())
  File "/cvmfs/cms.cern.ch/share/lcg/SCRAMV1/V3_00_77/SCRAM/Configuration/ConfigArea.py", line 182, in satellite
    utime(join(devconf, "Self.xml"))
FileNotFoundError: [Errno 2] No such file or directory
belforte@lxplus825/belforte> 
```

## Comment (belforte, 2024-10-24T09:07:04Z)

The problem surfaced when https://github.com/dmwm/CRABClient/releases/tag/v3.240930 was moved to `crab-prod` in IB on Oct 21.

After quick review with @aspiringmind-code , we decided to solve by deploying https://github.com/dmwm/CRABServer/releases/tag/v3.241017

No action on CRABClient, hopefully.

Obviously we need to do better at client validation. Clearly the new client was only tested with dev/preprod version of TW

## Comment (belforte, 2024-10-24T14:00:25Z)

updated TW (which is compatible with both old new client) was tested and deployed
https://cms-talk.web.cern.ch/t/production-taskworker-updated-to-v3-241017-stable/55985
