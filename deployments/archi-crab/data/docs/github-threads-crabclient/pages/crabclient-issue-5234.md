# dmwm/CRABClient issue #5234: create a crab checkfile command

State: closed
Opened: 2023-10-19T14:42:12Z
Closed: 2023-11-27T13:36:34Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5234

## Opening post (belforte, 2023-10-19T14:42:12Z)

it should
* find file in DBS and Rucio
* check for valid, has parent, was lost, is info consistent
* find location(s) in Rucio
* validate file replicas (needs gfal-* usual fork + scram unsetenv)
   * exist ?
   * is corrupted ? (copy + check adler32)

What else ?
@mapellidario @novicecpp @dciangot @KatyEllis please add requirements, desires...

## Comment (novicecpp, 2023-10-19T15:35:28Z)

find location(s) in Rucio -> also report tape sites.

## Comment (belforte, 2023-11-22T23:13:05Z)

Examples of command output

```
belforte@lxplus800/TC3> crab checkfile --lfn /store/data/Run2018C/ParkingBPH3/MINIAOD/UL2018_MiniAODv2-v1/2430000/04CC33F8-79E3-9E4F-8276-1BA15D065942.root --checksum
Rucio client intialized for account belforte
looking up LFN in DBS prod/global
  file status in DBS is VALID
  file belongs to:
    dataset: /ParkingBPH3/Run2018C-UL2018_MiniAODv2-v1/MINIAOD
    block:   /ParkingBPH3/Run2018C-UL2018_MiniAODv2-v1/MINIAOD#6c885590-655a-4016-b8db-aaaa428df5a2
Check information in Rucio
  LFN found in Rucio with matching block/dataset parentage
LFN has a tape replica at T1_FR_CCIN2P3_Tape
LFN has 1 disk replicas
List of disk replicas. Check that file exists and has correct size:
      RSE          status
T2_US_Florida    something wrong
Replica size at remote side is wrong. 844103680 vs. 3651095971  Needs to be invalidated
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
```

or
```
belforte@lxplus800/TC3> crab checkfile --lfn /store/data/Run2018D/Charmonium/MINIAOD/UL2018_MiniAODv2-v1/240000/05F76188-4601-6A4C-AE98-45115A3068E5.root --checksum
Rucio client intialized for account belforte
looking up LFN in DBS prod/global
  file status in DBS is VALID
  file belongs to:
    dataset: /Charmonium/Run2018D-UL2018_MiniAODv2-v1/MINIAOD
    block:   /Charmonium/Run2018D-UL2018_MiniAODv2-v1/MINIAOD#f51e61a1-cd4e-408c-9413-9d16638bd561
Check information in Rucio
  LFN found in Rucio with matching block/dataset parentage
LFN has a tape replica at T0_CH_CERN_Tape
LFN has 2 disk replicas
List of disk replicas. Check that file exists and has correct size:
      RSE          status
T1_US_FNAL_Disk      OK
T2_IN_TIFR           OK

Check of Adler32 checksum for each disk replica
verify checksum for replica at T1_US_FNAL_Disk. copy file...compute Adler32 checksum...Done
T1_US_FNAL_Disk      OK
verify checksum for replica at T2_IN_TIFR. copy file...compute Adler32 checksum...Done
T2_IN_TIFR       something wrong
Remote replica has wrong checksum. df557b32 vs. b838db91  Needs to be invalidated
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus800/TC3> 
```
