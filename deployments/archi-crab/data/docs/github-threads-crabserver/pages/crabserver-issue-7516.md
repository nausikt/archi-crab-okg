# dmwm/CRABServer issue #7516: pass existing $SITECONFIG_PATH to process running CMSSW

State: closed
Opened: 2023-02-01T15:34:25Z
Closed: 2023-02-26T14:19:19Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7516

## Opening post (belforte, 2023-02-01T15:34:25Z)

see
https://ggus.eu/index.php?mode=ticket_info&ticket_id=160313

since new jobwrapper may take a while to be deployed, we should push an urgent fix to https://github.com/dmwm/CRABServer/blob/65e3b434420299f8ee4a232c405d46323a4c7c40/scripts/CMSRunAnalysis.py#L642
along the lines of e.g. https://github.com/dmwm/CRABServer/blob/65e3b434420299f8ee4a232c405d46323a4c7c40/scripts/CMSRunAnalysis.py#L640

## Comment (belforte, 2023-02-02T22:13:15Z)

should check this at a couple suspected sites (besides KIT,  but IIUC it does not always happen at KIT), see https://cms-talk.web.cern.ch/t/crab-job-8001-exit-code-on-t2-ch-cern/19942/6

## Comment (mapellidario, 2023-02-26T14:19:19Z)

After having deployed the new jobwrapper, this is solved.

check for example this [job](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230224_153009:dmapelli_crab_20230224_162926_jobwr/job_out.1.0.txt), where I dump the environment where `cmsRun` is executed in: 

```plaintext
== CMSSW: SITECONFIG_PATH=/cvmfs/cms.cern.ch/SITECONF/local
```
