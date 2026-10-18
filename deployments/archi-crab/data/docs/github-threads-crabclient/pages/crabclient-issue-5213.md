# dmwm/CRABClient issue #5213: allow CRABClient to use Rucio python client API

State: closed
Opened: 2023-10-05T15:52:32Z
Closed: 2023-10-09T22:58:16Z
Labels: enhancement, In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5213

## Opening post (belforte, 2023-10-05T15:52:32Z)

see
https://github.com/cms-sw/cmsdist/issues/8737

Reporting conclusion here:

* CRABClient will use, on whichever OS it runs, the Rucio client for that arch as setup by 
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
```

* We will make sure that cmssw environment is not only changed during the execution of CRABClient commands (a forked subprocess in the end as per https://github.com/dmwm/CRABClient/blob/master/bin/crab

* We will restrict use of Rucio python client inside CRAB to CMSSW releases where it works, and too bad for people stuck in SL6 era.
  * initial very simple testing indicates that CMSSW_10_6_x is OK, so UL is covered, thanks Matti.
  * but for using that we need to switch to using python3 for CRABClient in there (currently there's a problem with pycurl)
