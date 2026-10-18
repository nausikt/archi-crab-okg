# dmwm/CRABClient issue #5280: wrong message from checkfile command

State: closed
Opened: 2024-01-08T15:19:54Z
Closed: 2024-01-10T14:16:00Z
Labels: bug, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5280

## Opening post (belforte, 2024-01-08T15:19:54Z)

when file is INVALID in DBS should not complain that it is not found in Rucio !
```
belforte@lxplus811/TC3> crab-dev checkfile --lfn /store/data/Run2018D/MuonEG/MINIAOD/UL2018_MiniAODv2-v1/240000/98CD4815-6676-FC4E-80C2-F3B9972B1284.root
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account belforte
looking up LFN in DBS prod/global
  file status in DBS is INVALID
  file belongs to:
    dataset: /MuonEG/Run2018D-UL2018_MiniAODv2-v1/MINIAOD
    block:   /MuonEG/Run2018D-UL2018_MiniAODv2-v1/MINIAOD#265af4fb-4a18-44a8-92c5-7e47416c89f8
Check information in Rucio
LFN not found in Rucio or otherwise not properly stored in Rucio
Details: LFN not found in Rucio
ERROR: most likely file was deleted but non invalidated in DBS
Command checkfile failed
belforte@lxplus811/TC3> 


```
