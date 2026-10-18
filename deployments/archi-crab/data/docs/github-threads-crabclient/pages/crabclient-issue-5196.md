# dmwm/CRABClient issue #5196: add $CMSSW_BASE/config/SCRAM/hooks to the sandbox

State: closed
Opened: 2023-05-15T14:49:13Z
Closed: 2023-06-12T11:32:10Z
Labels: Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5196

## Opening post (belforte, 2023-05-15T14:49:13Z)

see https://cms-talk.web.cern.ch/t/sandbox-questions/24063/3

- [x] change the code
- [x] update documentation : https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_are_the_files_CRAB_adds_to

## Comment (kpedro88, 2023-05-15T16:07:24Z)

Just to be completely accurate, the directory name is `$CMSSW_BASE/config/SCRAM/hooks` (plural hooks).

Also, some older versions of CMSSW will not have this directory by default. This is expected, so the sandboxing code should just move on if it can't find the directory.

## Comment (belforte, 2023-06-09T14:19:02Z)

@smuzaffar I presume that this OK with you as well and that there can not be any adverse effect. In case.. let me know.

## Comment (smuzaffar, 2023-06-10T21:10:55Z)

@belforte , yes this is fine.

## Comment (belforte, 2023-06-14T17:44:48Z)

@kpedro88 the dev version of CRABClient now in Integration Build now has the fix for this and for venv subdirectory #5197 .
I tested the change, but will nevertheless very much appreciate if you give it a try too and confirm that solves your need. If there's something to change or add, better to do it before it goes to mainstream production as the time to push changes there is O(1 month).

Please let me know. Thanks

You can use the new version with
```bash
source /cvmfs/cms-ib.cern.ch/latest/cmsset_default.sh
crab-dev ...
```

(see also [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CMSCrabClient#Using_CRABClient_from_nightly_CM) )

## Comment (kpedro88, 2023-07-05T14:31:10Z)

@belforte thanks, everything appears to work in my latest test! I'll update the [cms-sw.github.io](http://cms-sw.github.io/) docs now.

## Comment (belforte, 2023-07-05T16:46:46Z)

thanks Kevin. Please note that now `crab-dev` in the main CVMFS has been updated, no need to use `cms-ib`
