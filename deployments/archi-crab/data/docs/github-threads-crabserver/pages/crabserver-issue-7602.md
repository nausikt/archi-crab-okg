# dmwm/CRABServer issue #7602: job wrapper wrongly sleeps 1 min at and of  all jobs

State: closed
Opened: 2023-04-17T17:14:53Z
Closed: 2023-04-19T11:34:25Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7602

## Opening post (belforte, 2023-04-17T17:14:53Z)

something likely changed recently to make job wrapper add some sleep time at the end of jobs regardless of their running time.

Could be that now we reuse bash wrapper also for local stageout and there's a new count for that ?

## Comment (belforte, 2023-04-17T17:16:43Z)

see also https://mattermost.web.cern.ch/cms-o-and-c/pl/a7xqexcpo3yn3gxphtoiohutuy
where Marco nicely pointed to relevant code
https://github.com/dmwm/CRABServer/blob/bf0a465167412b9d24b121aaa64785869951c453/scripts/gWMS-CMSRunAnalysis.sh#L29-L45

## Comment (belforte, 2023-04-17T17:25:46Z)

at first looks this is because `submit_env.sh` also sets `START_TIME` and it is called by `cmscp.py`

Maybe fix is as simple as using in `gWMS..` a less generic env. var. name.
