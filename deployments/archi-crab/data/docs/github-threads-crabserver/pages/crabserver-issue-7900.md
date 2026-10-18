# dmwm/CRABServer issue #7900: Improve msg to user for TapeRecall progress

State: closed
Opened: 2023-10-09T12:15:51Z
Closed: 2023-10-09T14:28:18Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7900

## Opening post (belforte, 2023-10-09T12:15:51Z)

looking at this example
```
belforte@lxplus804/dbru> crab status crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe/
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/dbru/crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe
Task name:			230922_221352:dbruschi_crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	FAILED
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/230922_221352%3Adbruschi_crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=dbruschi&var-task=230922_221352%3Adbruschi_crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe&from=1695417232000&to=now
Warning:			Data recall from tape in progress: ok/all = 6814/6816 = 99.97065727699531%
				Rucio rule details at https://cms-rucio-webui.cern.ch/rule?rule_id=9d6fe088c12c45e3bc63526e64299902
Failure message from server:	Tape recall request did not complete in 15 days.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/dbru/crab_DYJetsToMuMu_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_MCPostVFPTagAndProbe/crab.log
belforte@lxplus804/dbru> 

```
the rule is still in Rucio https://cms-rucio-webui.cern.ch/rule?rule_id=9d6fe088c12c45e3bc63526e64299902 
and 16-days old now.
![image](https://github.com/dmwm/CRABServer/assets/1837785/b83f688d-a899-4e99-8d94-2f38e39a6b39)

We should:
- [x] remove the rule when we fail the task because of timeout
- [x] print completion % with one decimal only
- [x] tell user explicitly when completion is > 95% and datatier is *SIM to consider giving up, same for data at 99%

## Comment (belforte, 2023-10-09T12:16:32Z)

set to top since if I don't do it now, I will never do. It is just a tail of latest work on this topic.

## Comment (belforte, 2023-10-09T12:30:00Z)

My bad. First item is useless.
Originally I left rule around when task is failed thinking that it may still complete and this would help in case e.g. the user resubmits the same task (as the usually do).
https://github.com/dmwm/CRABServer/blob/264f2cdd2293361aca0a0d99c5546230561be2dc/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L94-L99

All rules have expiration, so any rule will expire one month after last task requesting it was submitted. There is no need to cleanup ! I will add a comment in the source.

## Comment (belforte, 2023-10-09T14:28:18Z)

solved via https://github.com/dmwm/CRABServer/pull/7901
