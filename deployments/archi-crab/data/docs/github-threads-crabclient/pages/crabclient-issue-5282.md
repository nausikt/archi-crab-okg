# dmwm/CRABClient issue #5282: wrong byte to TB conversion in checkdataset

State: closed
Opened: 2024-01-10T09:38:51Z
Closed: 2024-01-10T10:52:32Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5282

## Opening post (belforte, 2024-01-10T09:38:51Z)

```
belforte@lxplus811/TC3> crab-dev checkdataset --dataset /EGamma/Run2018D-UL2018_MiniAODv2_GT36-v3/MINIAOD
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

Rucio client intialized for account belforte
dataset status in DBS is: VALID
dataset size is: 30832 TB
```

but it should be 30.8 TB !!
