# dmwm/CRABServer issue #8736: report of quota used by crab_input is wrong

State: closed
Opened: 2024-10-10T22:37:25Z
Closed: 2024-11-21T14:00:40Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8736

## Opening post (belforte, 2024-10-10T22:37:25Z)

this code can not work for crab_input account.  I am not sure if it is currently used to populate grafana panel or not. If yes I am very surprised that it give a sensible 21PB. I expect that most rules for crab_input are OK, not REPLICATING/SUSPENDED/STUCK 
https://github.com/dmwm/CRABServer/blob/98bdaa7e08045c771cf961d5364be53ee67e7819/src/python/RucioUtils.py#L117-L128

## Comment (belforte, 2024-10-10T22:40:33Z)

@aspiringmind-code I lost track a bit of what you are working atm so am not sure where to put this in your priority list.
In a way, we may not need this anymore since we have [Panos' dashboard](https://monit-grafana.cern.ch/goto/SLzfkekNR?orgId=11). In another way, it is good for you to learn about Rucio.

I start to fear that you are working on too many things at same time

## Comment (aspiringmind-code, 2024-10-14T09:10:29Z)

This is a small fix, so no worries about priority. I've added all the states the rucio rule can be in the list.
