# dmwm/CRABClient issue #5291: crab checkfile bug in last commit for #5824

State: closed
Opened: 2024-02-11T16:48:06Z
Closed: 2024-02-15T16:59:40Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5291

## Opening post (belforte, 2024-02-11T16:48:06Z)

Command now exit w/o checking replica locaiton and integrity
This `return` at line 73 needs to be indented
https://github.com/dmwm/CRABClient/blob/c971c1dcb6f2768a2b952f8f84788b4f7e14958d/src/python/CRABClient/Commands/checkfile.py#L64-L73


```
belforte@lxplus806/TC3> crab --version
CRAB client v3.240110
belforte@lxplus806/TC3> crab checkfile --lfn   /store/hidata/PARun2016C/PAMinimumBias19/AOD/PromptReco-v1/000/286/069/00000/121568BB-63B9-E611-BA0A-02163E014256.root            
Rucio client intialized for account belforte
looking up LFN in DBS prod/global
  file status in DBS is VALID
  file belongs to:
    dataset: /PAMinimumBias19/PARun2016C-PromptReco-v1/AOD
    block:   /PAMinimumBias19/PARun2016C-PromptReco-v1/AOD#d4498174-b959-11e6-91fa-001e67abf228
Check information in Rucio
  LFN found in Rucio with matching block/dataset parentage
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus806/TC3> crab checkfile --checksum --lfn   /store/hidata/PARun2016C/PAMinimumBias19/AOD/PromptReco-v1/000/286/069/00000/121568BB-63B9-E611-BA0A-02163E014256.root
Rucio client intialized for account belforte
Beware, several GB of disk space on /tmp are needed for checking replica cheksum(s)
If you do not have them, create the TMPDIR enviromental variable
and point it to an existing directory of your choice

looking up LFN in DBS prod/global
  file status in DBS is VALID
  file belongs to:
    dataset: /PAMinimumBias19/PARun2016C-PromptReco-v1/AOD
    block:   /PAMinimumBias19/PARun2016C-PromptReco-v1/AOD#d4498174-b959-11e6-91fa-001e67abf228
Check information in Rucio
  LFN found in Rucio with matching block/dataset parentage
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus806/TC3> 
```
