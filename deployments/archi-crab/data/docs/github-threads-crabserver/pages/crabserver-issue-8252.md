# dmwm/CRABServer issue #8252: print message associated to gfal-copy errcode in cmscp.py

State: open
Opened: 2024-02-19T10:19:17Z
Labels: Type: Enhancement, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/8252

## Opening post (belforte, 2024-02-19T10:19:17Z)

cmscp.py should use python's `os.strerror()` on the Gfal2 return code so that we have some human text in cases like the on below

overall gfal-copy error reporting needs a full re-write, but that's for WMCore

see https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3760973

starting point is this from some job stdout
```
ERROR:root:Exception During Stage Out:
Command exited non-zero, ExitCode:110
Output: stdout: Thu Feb 8 23:26:08 EET 2024
Copying 4492440451 bytes
file:///srv/RAW2DIGI_L1Reco_RECO_trackRechitsAdded.root =>
davs://eoscms.cern.ch:443/eos/cms/store/group/phys_heavyions/rchudasa/e2e/Tau/Tau_Run2018D_RAW-AOD-multithread/240208_082349/0000/RAW2DIGI_L1Reco_RECO_trackRechitsAdded_110.root
gfal-copy exit status: 110
ERROR: gfal-copy exited with 110
Cleaning up failed file:
Fri Feb 9 00:06:38 EET 2024
davs://eoscms.cern.ch:443/eos/cms/store/group/phys_heavyions/rchudasa/e2e/Tau/Tau_Run2018D_RAW-AOD-multithread/240208_082349/0000/RAW2DIGI_L1Reco_RECO_trackRechitsAdded_110.root
DELETED
```
