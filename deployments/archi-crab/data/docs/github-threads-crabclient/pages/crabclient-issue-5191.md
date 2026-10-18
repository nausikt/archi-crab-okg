# dmwm/CRABClient issue #5191: implement crab checkdataset

State: closed
Opened: 2023-04-03T12:13:22Z
Closed: 2023-04-03T16:54:57Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5191

## Opening post (belforte, 2023-04-03T12:13:22Z)

should be based on
https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/CheckDiskAvailability.py

plan:
modity crab checkwrite (which already talks to Rucio) to wget the script on the fly from GH and run it

## Comment (belforte, 2023-04-03T16:50:48Z)

in my local branch
```
belforte@lxplus774/LOCAL> crab checkdataset --dataset /SingleMuon/Run2016G-21Feb2020_UL2016-v1/AOD
Checking disk availability of dataset: /SingleMuon/Run2016G-21Feb2020_UL2016-v1/AOD
 only fully available (i.e. complete) block replicas are considered 
dataset has 225 blocks
Checking blocks availabiliyt on disk ...
  block: 225
   4 blocks have  0 disk replicas *THESE BLOCKS WILL NOT BE ACCESSIBLE*
  30 blocks have  1 disk replicas
 187 blocks have  2 disk replicas
   4 blocks have  3 disk replicas
 Only 221/225 are available

 Block locations:
 T2_IN_TIFR      hosts 201 blocks
 T2_RU_JINR      hosts 211 blocks
 T2_IT_Pisa      hosts   2 blocks
 T2_IT_Rome      hosts   1 blocks
 T1_RU_JINR_Disk hosts   1 blocks

AFTER APPLYING CRAB SITE BLACKLIST:
   4 blocks have  0 disk replicas *THESE BLOCKS WILL NOT BE ACCESSIBLE*
  30 blocks have  1 disk replicas
 187 blocks have  2 disk replicas
   4 blocks have  3 disk replicas
 Only 221/225 are available

Rules on this dataset:
NONE

Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/LOCAL/crab.log
belforte@lxplus774/LOCAL> 

```
