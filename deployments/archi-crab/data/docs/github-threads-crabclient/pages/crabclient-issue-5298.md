# dmwm/CRABClient issue #5298: crab status must still print info even w/o Rucio client

State: closed
Opened: 2024-03-15T22:12:22Z
Closed: 2024-04-16T20:12:38Z
Labels: bug, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5298

## Opening post (belforte, 2024-03-15T22:12:22Z)

In this case I was trying to look at a job from another user (cmsbot), but still Rucio client may fail for many reasons and it will be good to still print all other relevant info. I am not even user what exactly it is used for, other then checking user quota.

```
belforte@lxplus803/bot> crab status crab_rucio_transfers_20240315_214047
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_rucio_transfers_20240315_214047
Task name:			240315_204049:cmsbot_crab_rucio_transfers_20240315_214047
Grid scheduler - Task Worker:	crab3@crab-sched-901.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/240315_204049%3Acmsbot_crab_rucio_transfers_20240315_214047
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240315_204049%3Acmsbot_crab_rucio_transfers_20240315_214047&from=1710531649000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_FR_GRIF', 'T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Status on the scheduler:	SUBMITTED
Cannot initialize Rucio Client.
belforte@lxplus803/bot> 
```

## Comment (belforte, 2024-03-29T10:56:35Z)

I can't reproduce the problem with code in master branch. Closing

## Comment (belforte, 2024-04-09T15:31:31Z)

I can't reproduce that exact error, but it still happens that
* Rucio client is initialized even if it will not be used
* If Rucio fails, crab status exit badly

see e.g.  https://cms-talk.web.cern.ch/t/problem-with-crab/38815?u=belforte
