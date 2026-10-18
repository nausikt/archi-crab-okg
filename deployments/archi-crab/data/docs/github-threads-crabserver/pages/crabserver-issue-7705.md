# dmwm/CRABServer issue #7705: fix sandbox use in job wrapper

State: closed
Opened: 2023-06-30T10:18:35Z
Closed: 2024-09-30T11:55:10Z
Labels: Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7705

## Opening post (belforte, 2023-06-30T10:18:35Z)

currently `sandbox.tar.gz` is expanded in two places (see  https://github.com/dmwm/CRABServer/pull/7681#issuecomment-1613144037 and comment below that)
1. `/srv` : so that e.g. `scriptExe` and additional `userFiles` are found where needed and as documented in [FAQ](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#How_are_the_inputFiles_handled_i)
2. `/srv/CMSSW_X_Y_Z` so that "scram subdirectories" picked frome `$CMSSW_BASE` on submission host are placed in corresponding directories

Furthermore, `PSet.py` and `PSet.pkl` are moved up from `/srv/CMSSW_X_Y_Z` to `/srv` because that's the current directory where `cmsRun` command is executed. This overrides the ones places in `/srv` in step 1. 

<strike>
We also have a real problem (**bug**) : new code to expand user tar files https://github.com/dmwm/CRABServer/issues/7661 only does that in `/srv/CMSSW_X_Y_Z`, while user may expect this to be happen in `/srv`
</strike> 
**NO**: reviewing the above one year later, user tar files are expanded in /srv, not /srv/CMSSW_X_Y_Z.  So I am not sure if anything is needed, aside good documentation so that we avoid going through things again.<br><br>


We should expand the sandbox only once and place each file in the right place !

## Comment (belforte, 2023-06-30T16:38:50Z)

This is not particularly urgent at this point. But I'd rather do the cleanup sooner than later, to do it when we have things clear in memory and so that we also fix documentation and will never be confused again

## Comment (mapellidario, 2023-07-03T12:01:02Z)

Instead of using multiple tar archives, which would require some changes, we can use a single archive, but change the directory where files are put inside of it. This would still require changes in both the client and the jobwr, but hopefully they will be a bit less invasive.
For example, we could use `tarfile.add(..., arcname="srv/" + filename )` for the files that should go in `/srv` and `tarfile.add(..., arcname="cmssbase/" + filename )` for the files that need to go to `srv/CMSSW_X_Y_Z`. in `CMSRunAnalysis.py:prepSandbox` we can extract the archive and then move all the directories from the archive to the desired final path.

## Comment (mapellidario, 2023-07-03T12:02:18Z)

> We also have a real problem (bug) : new code to expand user tar files https://github.com/dmwm/CRABServer/issues/7661 only does that in /srv/CMSSW_X_Y_Z, while user may expect this to be happen in /srv

Maybe I am missing something, but why dont you execute the same extract command twice, both in `prepSandbox` and `extractUserSandbox`? are you waiting to for the cleanup and do not want to add any "dirty" fixes?

## Comment (belforte, 2023-07-03T12:50:02Z)

neat idea, thanks. Indeed that way we can also easily make a backward compatible TW and avoid disruption.

As to the second comment, indeed now I expand tar files only in `/srv`  . But we need to change things a bit and only expand user sandbox after CMSSW_X_Y_Z directory has been created so we do all things in one place.

## Comment (belforte, 2023-07-03T13:18:19Z)

let's map into things to do:
- [x] modify TW to do sandbox expansion in only one place in the code after CMSSW_X_Y_Z exists and remove prepSandbox 
- [ ] expand in a temporary directory
- [ ] if files appear with a flat structure, put them all both in `/srv` and `/srv/CMSSW_X_Y_Z` (do not use explitic `/srv` string, of course, define a name for `job's starting directory` like e.g. `topdir` and use it consistently)
- [ ] if files from sandbox are organized as `cmssw_base/..`. + `topdir/....` put each set in the proper place
- [ ] expand tar files placed in `topdir`
- [ ] modify CRAB client to archive files in the two `cmssw_base`and `topdir` directories
- [ ] once old client is gone (also from PRE), cleanup wrapper to remove backward compatibility

Note added on Sept 20: all actions listed above are not needed. Once we "`tarfile.add(..., arcname="cmssbase/" + filename )` for the files that need to go to `srv/CMSSW_X_Y_Z`." as @mapellidario cleverly pointed out in https://github.com/dmwm/CRABServer/issues/7705#issuecomment-1618096011 , expansion inside `CMSSW_X_Y_Z` will be taken care of by the current iterative expansion of `sandbox.tar.gz`

## Comment (belforte, 2024-09-12T16:50:10Z)

of course I have now forgotten everything... and will need to re-learn :-)

## Comment (belforte, 2024-09-16T16:37:16Z)

after re-reading the issue and the code and a first attempt a documentation in https://github.com/dmwm/CRABServer/issues/7754#issuecomment-2353270108 
I am leaning toward

* fix the documentation and leave code as is

## Comment (belforte, 2024-09-18T15:54:04Z)

Well  `CRAB3.zip` is not sent to the WN. No reason to reference it in the JobWrapper !
https://github.com/dmwm/CRABServer/blob/b3b26dbd3c8aa617e6a0e03b6cfe8f23a5fc3c97/scripts/CMSRunAnalysis.sh#L57

## Comment (belforte, 2024-09-19T16:51:52Z)

About the "sandbox expanded in two places".
I will start by removing https://github.com/dmwm/CRABServer/blob/3c8607f723248dff957d6146a25162d8f8128fbb/scripts/CMSRunAnalysis.py#L375
and incorporating the functionality in https://github.com/dmwm/CRABServer/blob/3c8607f723248dff957d6146a25162d8f8128fbb/scripts/CMSRunAnalysis.py#L392

so that at least things will be clear.

Also it means that expansion is done after CMSSW_X_Y_Z has been created, opening the way for a "do it once".
BEst option looks to me at some point to modify sandboxing in client so that $CMSSW_BASE is tarred into a CMSSW_X_Y_Z directory and then all files will automatically go in the proper place when the sandbox is iteratively expanded
https://github.com/dmwm/CRABServer/blob/3c8607f723248dff957d6146a25162d8f8128fbb/scripts/CMSRunAnalysis.py#L381-L387
