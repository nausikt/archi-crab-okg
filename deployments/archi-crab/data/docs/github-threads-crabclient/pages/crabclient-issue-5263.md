# dmwm/CRABClient issue #5263: checkdataset output fromat broken in last commit

State: closed
Opened: 2023-11-30T15:16:31Z
Closed: 2023-12-04T11:05:25Z
Labels: bug, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5263

## Opening post (belforte, 2023-11-30T15:16:31Z)

```
crabbelforte@lxplus801/TC3> CLOCAL 
belforte@lxplus801/TC3> crab checkdataset --dataset  /WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
Rucio client intialized for account belforte
Checking disk availability of dataset: /WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
 only fully available (i.e. complete) block replicas are considered 
dataset has 7 blocks
Check blocks availabiliyt on disk
   0 blocks have  0 disk replicas
   6 blocks have  1 disk replicas
   1 blocks have  8 disk replicas
 Dataset is fully available

 Block locations:
            T3_KR_UOS hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks  *SITE BLACKLISTED IN CRAB*
           T2_DE_DESY hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks
        T2_US_Caltech hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks
            T2_FI_HIP hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks
           T2_FR_GRIF hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks
         T2_BR_SPRACE hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks
           T3_FR_IPNL hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks  *SITE BLACKLISTED IN CRAB*
           T2_DE_RWTH hosts {'T3_KR_UOS': 7, 'T2_DE_DESY': 1, 'T2_US_Caltech': 1, 'T2_FI_HIP': 1, 'T2_FR_GRIF': 1, 'T2_BR_SPRACE': 1, 'T3_FR_IPNL': 1, 'T2_DE_RWTH': 1} blocks

AFTER APPLYING CRAB SITE BLACKLIST:
   6 blocks have  0 disk replicas *THESE BLOCKS WILL NOT BE ACCESSIBLE*
   1 blocks have  6 disk replicas
 Only 1/7 are available

```

## Comment (belforte, 2023-12-01T11:06:17Z)

at the same time
- [x]  fix this, current `crab-prod/dev` should not have this traceback
( `CRAB client v3.231030` )
```
belforte@lxplus801/TC3> crab-dev checkdataset --dataset /a/b/c
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account belforte
Failed to execute CheckDatasetAvailability.py. Contact support
  Stdout:
    Checking disk availability of dataset: /a/b/c
     only fully available (i.e. complete) block replicas are considered 
    
  Stderr:
    Traceback (most recent call last):
      File "checkDiskAvailability.py", line 212, in <module>
        main()
      File "checkDiskAvailability.py", line 48, in main
        scope, dataset, blocks = get_inputs(rucio)
      File "checkDiskAvailability.py", line 150, in get_inputs
        dss = rucio.list_content(scope, dataset)
      File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/didclient.py", line 327, in list_content
        raise exc_cls(exc_msg)
    rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
    Details: Data identifier 'cms:/a/b/c' not found
    
Command checkdataset failed
belforte@lxplus801/TC3>
```
- [x] print which site has the dataset on tape
- [x] print dataset status in DBS
- [x] print dataset size
