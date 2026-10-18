# dmwm/CRABClient issue #5300: CRAB incorrectly following symlink in sandbox creation

State: closed
Opened: 2024-04-02T21:38:25Z
Closed: 2024-04-03T19:47:38Z
Labels: enhancement, In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5300

## Opening post (kpedro88, 2024-04-02T21:38:25Z)

Linktime optimization is a new speedup enabled in CMSSW_13_0_X and higher. It adds a directory `$CMSSW_BASE/external/${SCRAM_ARCH}/objs-base`, which is a symbolic link to `$CMSSW_RELEASE_BASE/objs/${SCRAM_ARCH}`. CRAB is following the symbolic link when creating the sandbox and adding all the files in that directory, which can exceed the allowed tarball size of 120 MB. Instead, the symlink should be preserved to avoid duplicating these contents from the release base.

## Comment (caleb-james-smith, 2024-04-02T21:45:00Z)

For example, using https://github.com/cms-egamma/EgammaAnalysis-TnPTreeProducer, for Run 3:
```
cmsrel CMSSW_13_3_1
cd CMSSW_13_3_1/src
cmsenv
git clone -b Run3_13X git@github.com:cms-egamma/EgammaAnalysis-TnPTreeProducer.git EgammaAnalysis/TnPTreeProducer
scram b -j8
```
and attempting crab submission:
```
cd EgammaAnalysis/TnPTreeProducer/crab
python3 tnpCrabSubmit.py
```
is giving this error:
```
Finished importing CMSSW configuration ../python/TnPTreeProducer_cfg.py
Failed submitting task: Impossible to upload the sandbox tarball.
Error message: Error: input tarball size 120 MB exceeds maximum allowed limit of 120 MB
largest 5 files are:
sandbox content sorted by size[Bytes]:
27024496	external/slc7_amd64_gcc12/objs-base/ValidationHGCalValidationAuto.obj
21093232	external/slc7_amd64_gcc12/objs-base/SimG4CMSCaloPlugins.obj
 7683944	external/slc7_amd64_gcc12/objs-base/SimG4CMSCalo.obj
 7249312	external/slc7_amd64_gcc12/objs-base/SimG4CMSTestBeamPlugins.obj
 6601152	external/slc7_amd64_gcc12/objs-base/ValidationGeometry.obj
see crab.log file for full list of tarball contetnt.
More details can be found in /uscms_data/d3/caleb/KU_SUSY_Run3/CMS_EGamma/CMSSW_13_3_1/src/EgammaAnalysis/TnPTreeProducer/crab/crab_2024-04-02/crab_2023_Run2023C_0v1/crab.log
```

## Comment (kpedro88, 2024-04-02T21:46:38Z)

This seems to be caused by the presence of `config.JobType.sendExternalFolder = True` in the CRAB config. I think the symlink handling here should be fixed, otherwise this flag will always overload the sandbox in 13_0_X and higher.

## Comment (kpedro88, 2024-04-02T21:59:10Z)

In fact, it's probably a good rule of thumb for sandbox creation that any symlink pointing to a path starting from `$CMSSW_RELEASE_BASE` should be preserved rather than followed.

## Comment (belforte, 2024-04-02T22:27:01Z)

Thanks for reporting, and providing a nice solution.
The problem is that when creating sandbox the decision to follow or not symlinks is a global flag to the  `tar` command.  When I implemented preserving symlinks for `venv` I had to effectively build the tarball twice with two different options and combine. I am possibly simply ignorant here, but do not know how to make a decision on a file-by-file base.

Could this be attacked from CMSSW side ? When cmsRun runs, it knows about `$SCRAM_ARCH` and `$CMSSW_RELEASE_BASE`, why does it need a symlink pointing to the latter in `$CMSSW_BASE` ?

What is the role of the `external` folder ? I could handle like `venv`, will it do ? Or could users put any sort of thing there ? including links to files outside `$CMSSW_BASE` ?

## Comment (kpedro88, 2024-04-02T22:33:38Z)

Other things can go in `external` that would need to be copied. @smuzaffar would have to comment about why this particular folder from `$CMSSW_RELEASE_BASE` is symlinked where it is.

I think you'll have to do something similar to `venv` for `external`: copy everything excluding `objs-base` entirely, then combine with a tarball just containing the symlink. It's a bit clunky, but maybe at this point it can at least be generalized in case of future such issues. (i.e., find all symlinks that should be preserved, directly exclude them from the initial tarball, then append the preserved links to the tarball.)

## Comment (belforte, 2024-04-02T22:34:23Z)

it is unfortunate that we did not discover this yet. Something is clearly wrong in our and Shahzad validation. He makes sure that crab submit works for every release :-(

## Comment (belforte, 2024-04-02T22:42:36Z)

well.. Caleb's task was just "at the bar"
 `input tarball size 120 MB exceeds maximum allowed limit of 120 MB`
 
 with my simple test  I get a 107 MB sandbox. So we know why it was not spotted yet.
 
 @caleb-james-smith can you work around this for a while by removing
 `config.JobType.sendExternalFolder = True`
?

## Comment (smuzaffar, 2024-04-03T04:33:51Z)

Hi, in most cases contents under `cmssw/external` are not needed at runtime (unless you have setup extra tools in your dev area and in that case those tools should also be bundled in the sandbox).  Contents under  `external/slc7_amd64_gcc12/objs-base/` are for the objects file needed to build the Big Simulation plugin. These are only needed at build time ( `scram build`) and these are not needed at rumtime.

## Comment (belforte, 2024-04-03T08:58:33Z)

thanks @smuzaffar for explaining. Would it make sense then to put pointers to `objs_base` objects in a different directory ? I am still puzzled that `scram b` can't find `$CMSSW_RELEASE_BASE/objs/${SCRAM_ARCH}` and needs to be pointed to it.... but if a pointer is needed.. .why there ? maybe it was less work for `scram` but clearly it makes sandbox preparation more complex. "most cases" is not something that can be coded.

## Comment (smuzaffar, 2024-04-03T09:31:41Z)

@belforte , this is part of build rules each cmssw release use. It has been there since Sep 2014 (https://github.com/cms-sw/cmssw-config/pull/28). I can fix it for new release cycles (14.1.X and above) but existsing releases (e.g already installed on cvmfs) or new releases for old release cycles will still use old build rules. 

For crab, I think a simple workaround/soultion (which should work for all releases) could be that if `config.JobType.sendExternalFolder = True` is used then crab just exclude `objs-base` and `objs-full` from tar (note there could be two symlinks one for patch release objs and one for full release objs). Or crab can add a configuration parameter so that user can exclude any directory. All crab needs to do is to pass `--exclude` to tar command :-)

## Comment (smuzaffar, 2024-04-03T09:50:56Z)

@belforte , any specific reason to open tarfile with [dereference=True](https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/JobType/UserTarball.py#L116) ?

## Comment (belforte, 2024-04-03T10:34:24Z)

thanks for the tip Shahzad. Very good. I will do it.
You do not need to change the build process for this.

About `dereference=True` the reason is that users may have things in there which are symbolic links to other places in their directories, so that it works locally, but links would not be resolved on grid nodes, so we ship the destination file. Nobody thought at the time that some links would point to files which are already in the release or elsewhere in CMSSW_BASE. That is very old stuff.. as often the case I suspect that it was done because there was somebody with that problem and decision (not my me) was to accommodate rather than say "sorry pal, if you want a file, put the file there, not a link to it".

## Comment (caleb-james-smith, 2024-04-03T13:25:58Z)

Hi @belforte.

Yes, @kpedro88 suggested this workaround for my use case:
Change `config.JobType.sendExternalFolder = True` to `config.JobType.sendExternalFolder = False`.

Before this change, my crab submissions were failing for all datasets with this error:
```
Error message: Error: input tarball size 120 MB exceeds maximum allowed limit of 120 MB
```

After this change, my crab submissions worked for all the datasets I am running, for example:
```
time python3 tnpCrabSubmit.py

Finished importing CMSSW configuration ../python/TnPTreeProducer_cfg.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 240402_215012:caleb_crab_2023_Run2023C_0v1
Project dir: crab_2024-04-02/crab_2023_Run2023C_0v1
Please use ' crab status -d crab_2024-04-02/crab_2023_Run2023C_0v1 ' to check how the submission process proceeds.
```

## Comment (caleb-james-smith, 2024-04-03T13:31:39Z)

@belforte, I was also surprised that the tarball size was equal to the limit size:
```
Error message: Error: input tarball size 120 MB exceeds maximum allowed limit of 120 MB
```
My first interpretation was that it was not a coincidence, but that the size stopped growing once it hit the limit...
But if the tarball is created independently of the size limit, is it just a coincidence that my tarball is the same size as the limit?

## Comment (belforte, 2024-04-03T13:41:58Z)

it was a coincidence. tarball is created, then measured :-)

Thanks for confirming that you have a workaraound. Takes some pressure off having a fix in CRABClient. I will implement what Kevin and Shahzad suggested but will take time for this to be in production.
