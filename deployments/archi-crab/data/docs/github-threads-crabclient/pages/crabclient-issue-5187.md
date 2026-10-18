# dmwm/CRABClient issue #5187: Add src/*/*/python to the user sandbox

State: closed
Opened: 2023-02-17T10:30:28Z
Closed: 2023-02-27T11:56:46Z
Labels: enhancement, HighPrio, In Progress
URL: https://github.com/dmwm/CRABClient/issues/5187

## Opening post (mapellidario, 2023-02-17T10:30:28Z)

### description

The change https://github.com/cms-sw/cmsdist/pull/7865 stopped creating symlinks that CRABClient relied upon when the parameter `JobType.sendPythonFolder` is set to `True` in user task config.

### proposed solution

Shahzad on CMSTalk suggested to always add `src/*/*/python` and `src/*/*/interface` to the user sandbox [1].

We already add `src/**/interface` https://github.com/dmwm/CRABClient/blob/b1d3d94c9ba5e2209f9687af21c34278e23804d8/src/python/CRABClient/JobType/UserTarball.py#L163

I suggest to simply add `python` to that line. A PR is on its way.

----

fyi: @rgerosa 

[1] https://cms-talk.web.cern.ch/t/missing-symbolic-links-in-cmssw-base-python/20403/35?u=dmapelli

## Comment (belforte, 2023-02-17T10:56:05Z)

to be clear, after this change, the sandbxox will contain all directories named `python`, `data` or `interface` in the tree below `$CMSSW_BASE/src`. Not rescricted to `src/*/*/python`

## Comment (belforte, 2023-02-17T11:01:16Z)

Dario, please update the documentation as well https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_are_the_files_CRAB_adds_to

## Comment (rgerosa, 2023-02-17T11:01:20Z)

Thanks a lot for handling this! As a crab user (not developer), I guess it would be also fine to keep the inclusion of `src/*/*/python` optional (i.e. that can be activated via the `sendPythonFilter` option). My use case was rather peculiar, as I am running multiple cmsRun instances inside a single job and not just the PSet one. This means that for most of the user the inclusion of `src/*/*/python` is probably not 100% necessary. However, I leave you the final decision of course  ... just wanted to add my 2 cents on the table :).

## Comment (belforte, 2023-02-17T11:04:36Z)

Thanks @rgerosa 
I think we are safe by adding python subdirs under `src`, hopefully there's no junk in there. We need to have these lists because tarring up all of $CMSSW_BASE would bring in all sort of things.
In the end, if the tarball is too big, submission is refused and user has to cleanup, but we try to limit those occurrences
