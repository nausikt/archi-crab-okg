# dmwm/CRABClient pull request #5269: all crab commands that require a projdir can be called with --task=

State: closed
Opened: 2023-12-01T13:08:47Z
Closed: 2023-12-01T13:11:21Z
Merged: 2023-12-01T13:11:21Z
URL: https://github.com/dmwm/CRABClient/pull/5269

## Opening post (mapellidario, 2023-12-01T13:08:47Z)

Fixes #5268 

### status

Tested and approved in https://github.com/dmwm/CRABClient/pull/5250#issuecomment-1836046811

### Interface

first execution

```plaintext
Singularity> crab status --task=231031_085905:sesanche_crab_QCD_Pt800to1000_Mu5 --proxy=$X509_USER_PROXY
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_QCD_Pt800to1000_Mu5 folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_QCD_Pt800to1000_Mu5
Rucio client intialized for account dmapelli
CRAB project directory:         /home/dario/crab/local/z-submitted/crab_QCD_Pt800to1000_Mu5
Task name:                      231031_085905:sesanche_crab_QCD_Pt800to1000_Mu5
[...]
```

Second time: crab remake returns a warning, crab status runs properly. Of course, you can run crab status on the directory created automatically by remake under the hood.

```plaintext
Singularity> crab status --task=231031_085905:sesanche_crab_QCD_Pt800to1000_Mu5 --proxy=$X509_USER_PROXY
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Error: crab_QCD_Pt800to1000_Mu5/.requestcache not created, because it already exists.
Rucio client intialized for account dmapelli
CRAB project directory:         /home/dario/crab/local/z-submitted/crab_QCD_Pt800to1000_Mu5
Task name:                      231031_085905:sesanche_crab_QCD_Pt800to1000_Mu5
[...]
Singularity> crab status -d crab_QCD_Pt800to1000_Mu5 --proxy=$X509_USER_PROXY
Rucio client intialized for account dmapelli
CRAB project directory:         /home/dario/crab/local/z-submitted/crab_QCD_Pt800to1000_Mu5
Task name:                      231031_085905:sesanche_crab_QCD_Pt800to1000_Mu5
```

## Comment (mapellidario, 2023-12-01T13:11:15Z)

Since already approved, merging myself
