# dmwm/CRABClient issue #5206: report user Rucio quota in crab status

State: closed
Opened: 2023-08-31T14:25:29Z
Closed: 2023-10-19T20:48:18Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5206

## Opening post (belforte, 2023-08-31T14:25:29Z)

as discussed in chat with @dciangot 

whenever a task is using RUCIO-ASO, crab status must check quota
on the target RSE and aggressively warn user in case it gets tull (or close to).
Stageout for current job will be halted, status reporting may look
inconsistent and files on temp may get lost.

@novicecpp any comment ?

## Comment (novicecpp, 2023-08-31T14:39:05Z)

Look like we need to integrate rucio client into crabclient :)

. 

Could you elaborate `Stageout for current job will be halted, status reporting may look inconsistent and files on temp may get lost.` part? 

I saw something strange when "EOS quota" is full. Some datasets/files is gone from container. (I cannot said for sure because I just ignored it and submitted new tasks instead. I do not expect to encounter this problem for production).

## Comment (belforte, 2023-08-31T15:10:27Z)

> I saw something strange when "EOS quota" is full. Some datasets/files is gone from container.

exactly that ! Diego understand how this happens. Indeed it gets self-fixed once quota is  freed.

## Comment (belforte, 2023-08-31T15:13:36Z)

> Look like we need to integrate rucio client into crabclient :)

my thought too, but
- we can only do for cmssw 12+
- there is no guaranteed that python3 from cmssw and python3 needed by rucio stay compatible long term
- pffffff pffff pfffff why can't we agree on same compilers and interpreter for all those activities ?

## Comment (novicecpp, 2023-08-31T15:18:33Z)

`curl`?

## Comment (belforte, 2023-10-03T19:03:40Z)

on hold waiting for a decision on CRABClient vs. Rucio API in https://github.com/cms-sw/cmsdist/issues/8737

## Comment (belforte, 2023-10-18T22:40:13Z)

now that we have settled on using python Rucio client for CMSSW_11 + (and possibly look at 10_6, see https://github.com/dmwm/CRABClient/issues/5221#issuecomment-1761472537 ) it is time to do this.

## Comment (belforte, 2023-10-19T20:40:50Z)

examples of new output :
**all ok**
```
Status on the scheduler:	SUBMITTED
You have 10/10 GBytes available as Rucio quota at site T3_IT_Trieste

Jobs status:                    idle         		100.0% (10/10)
```

**below  RUCIO_QUOTA_WARNING_GB**
```
to be available. Jobs may not find a site where to run. CRAB has changed this value to 2750 minutes.
Status on the scheduler:	SUBMITTED
You have 2/10 GBytes available as Rucio quota at site T3_IT_Trieste
Warning: This may be not enough for your output, leading to problems. Consider cleaning up

Jobs status:                    idle         		100.0% (10/10)
```

**below RUCIO_QUOTA_MINIMUM_GB**
```
Status on the scheduler:	SUBMITTED
You have 0/10 GBytes available as Rucio quota at site T3_IT_Trieste
ALARM: Not enough space at ASO destination 
 This very dangerous. Your output stageout will get stuck.
 status information will be stale and could be misleading
 YOU MUST CLEANUP YOUR RUCIO SPACE IMMEDIATELY (remove some rules):

Jobs status:                    idle         		100.0% (10/10)
```

Also some red color.
Used quota is printed and warning/alarms added only "if relevant" i.e. the task was submitted and it is not complted. Nothing will be printed for completed tasks. 
We may want to also do the same for KILLED tasks... anyhow, that kind of fine polishing may come.
I think this addresses what was requested.

The two thresholds RUCIO_QUOTA_MINIMUM_GB and RUCIO_QUOTA_WARNING_GB are now in ClientUtilitiers, I will move them to ServerUtilities so they can be use consistently in TW as well.
