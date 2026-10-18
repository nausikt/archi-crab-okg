# dmwm/CRABServer issue #7754: Document how sandboxes are expanded in WN

State: closed
Opened: 2023-07-13T10:26:43Z
Closed: 2024-09-20T10:02:53Z
Labels: Type: Documentation, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7754

## Opening post (belforte, 2023-07-13T10:26:43Z)

- [x] find the proper place
- [x] document what's done now (in /srv + $CMSSW_BASE)
- [x] document new way aftre #7705 is done

## Comment (belforte, 2024-09-16T15:39:54Z)

current situation:
1. name of "sandbox" is passes a argument to the HTC jobs as "-a sandbox.tar.gz"
2. both "sanbox.tar.gz" and "CMSRunAnalysis.tar.gz" are placed on job wrappers cwd (/srv) by HTCondor using "transfer_input_files"
1. [gWMS-CMSRunAnalysis.sh](]https://github.com/dmwm/CRABServer/blob/master/scripts/gWMS-CMSRunAnalysis.sh) it is a very thin wrapper which dumps ads, chirps exit codes and calls CMSRunAnalysis.sh and cmscp.py. The latter copied output to local /store/user/temp  and it is not relevant here
3. [CMSRunAnalysis.sh](https://github.com/dmwm/CRABServer/blob/master/scripts/CMSRunAnalysis.sh) sets up environment (including python) then
   1. untar   CMSRunAnalysis.tar.gz 
   2. adds CRAB3.zip and WMCore.zip to PYTHONPATH
   4. runs  CMSRunAnalysis.py 
4. [CMSRunAnalysis.py]() , then
   1. parses -a argument into local variable archiveJob (which evaluates to "sandbox.tar.gz")
   1. calls [prepSandbox()](https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/scripts/CMSRunAnalysis.py#L375)
      * untars the "archiveJob" file in current "cwd" (/srv) and also expand any tar file found in there
   3. initializes WMCore and SCRAM
   5. calls [extractUserSandbox()](https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/scripts/CMSRunAnalysis.py#L392)
      * cd CMSSW_....
      * expand here ../archiveJob , but not tarfiles which may be in there
      * move up PSet* to /srv and set /srv again as cwd 
   6. performs PSet tweaking
   7. runs cmsRun or script_exe

## Comment (belforte, 2024-09-17T16:51:18Z)

I moved the "description part" above to  [CRAB Job Wrapper](https://cmscrab.docs.cern.ch/crab-design/crab-job-wrapper.html) in our MD doc.

The details of what `prepSandbox` and `extractUserSandbox` do, belong to the source code and I wlll move them there, possibly also changing names and taking care of the duplication of PSet.*

## Comment (belforte, 2024-09-20T10:02:53Z)

done
