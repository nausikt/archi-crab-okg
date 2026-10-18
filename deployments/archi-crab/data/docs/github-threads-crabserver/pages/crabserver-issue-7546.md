# dmwm/CRABServer issue #7546: make sure old tasks are removed from condor queue

State: closed
Opened: 2023-02-21T14:35:08Z
Closed: 2023-02-23T08:10:28Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7546

## Opening post (belforte, 2023-02-21T14:35:08Z)

we have thousands of old task bootstrap jobs stuck in HOLD status in condor queues of all schedulers.
Dating back to 2020.
This should be harmless for condor.
But surely it is annoying and makes us so used to seeing so many held jobs that we may overlook problems.
See also this thread in MM : https://mattermost.web.cern.ch/cms-o-and-c/pl/7otyhpkhh3ni8gk3xpweuqh74e 

Removing those held jobs is a bit tricky since they have these classAds
```
LeaveJobInQueue = true
PeriodicHold = time() > CRAB_TaskEndTime
```
Meaning that after a `condor_rm` jobs stick in the queue and are kicked back from status X (flagged for deletion) to H (Hold).

I managed to get rid of those jobs with:
```
sudo condor_qedit -con  qdate\<1671000000 PeriodicHold=Null
sudo condor_qedit -con  qdate\<1671000000 LeaveJobInQueue=False
sudo condor_rm -con qdate\<1671000000 
```
where 1671000000 means `Wed Dec 14 07:40:00 CET 2022`,  I just picked some round number.

The question is why we leack jobs in hold status that way. Our cleanup procedure was supposed to take care.

## Comment (belforte, 2023-02-21T14:37:56Z)

I have cleaned all production schedulers except `vocms0106/107` so they can be used to investigate and fix the current cleanup procedure

## Comment (belforte, 2023-02-21T17:48:19Z)

The problem is not urgent, but it is more efficient to look now that I have things in mind.
IIUC (IIRC etc.) cleanup happens via [JobCleanup.py](https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/blob/master/JobCleanup.py) which by the way has a very nice documentation piece at the beginning, which is [run as a crontab](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/manifests/crabschedd.pp#L228-233) 

/data/srv/SubmissionInfrastructureScripts come from [vocmshtcondor module](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/blob/a6bc3819803eb1d6ecbf0dba73da8a62087786b0/code/manifests/structure.pp#L142-156) (thanks to @novicecpp for this hard-to-find tip)

And of course we should move that `JobCleanup.py` to our repository, it is  completely CRAB specific !

I guess the problem is then in [clearDagFromQueue](https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/blob/master/JobCleanup.py#L91-99) function
```python
def clearDagFromQueue(dagList, scheddObject):
    logging.info("List of ClusterIds to be cleared from the queue: %s" % dagList)
    #pprint.pprint(dagList)
    if DRYRUN:
	pass
	# scheddObject.edit(dagList, "LeaveJobInQueue_dryrun", 'False')
    else:
	scheddObject.edit(dagList, "LeaveJobInQueue", 'False')
        scheddObject.act(htcondor.JobAction.Remove, dagList) 

```

comparing with my by-hand procedure above it misses the part about removing the periodicHold which may cause the job to go into Hold before it is removed from the queue.

Maybe in earlier versions of condor removal from queue was faster, maybe it all depends on the mood of the day of the schedd (the schedd daemong give priorities to things which have to do with running jobs and does thing like Periodic* when load is low without any particular period). Maybe we added the periodicHold after we wrote JobCleanup. Maybe we simply made a mistake and did not test well enough.

I will look into changing the code in vocms0106 and see what happens after crontab has run again.

And ..yeah.. another thing to move to python3 before the `#!/usr/bin/python` at the top gives us problems

## Comment (belforte, 2023-02-21T18:04:32Z)

I was wrong :smile:
the [clearDagFromQueue](https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/blob/master/JobCleanup.py#L91-99) may actually be working. The problem [this line](https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/blob/master/JobCleanup.py#L106)
```python
        constraint = '( (JobUniverse =?= 7) && (TaskType=="ROOT") )'
```
which selects (w/o good reason) "primary dagmans" . While since automatic splitting came in we also have PROCESSING and TAIL dagmans.
Indeed, looking at old held jobs
```
belforte@vocms0106/crab> condor_q -con 'jobstatus==5&&qdate<1671000000' -af tasktype |sort|uniq -c
   3365 PROCESSING
   3582 TAIL
belforte@vocms0106/crab> 
```
held dagmans of type `ROOT` are from last month
```
belforte@vocms0106/crab> condor_q -con 'jobstatus==5&&tasktype=="ROOT"' -af qdate|head -4
1673716498
1673716535
1673716809
1673717108
belforte@vocms0106/crab> date -d @1673716498
Sat Jan 14 18:14:58 CET 2023
belforte@vocms0106/crab> 
```

## Comment (belforte, 2023-02-21T18:11:37Z)

indeed we are leaking a fraction of dagmans we run, not all of them . Given that each scheduler has only O(8k) held jobs.

## Comment (belforte, 2023-02-21T20:51:46Z)

all of this was known as of 5 years ago https://github.com/dmwm/CRABServer/issues/5691 sigh
:sob:

## Comment (belforte, 2023-02-21T21:13:06Z)

fix tested on vocms0106, all good. Making a PR on SI gitlab:
https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/merge_requests/61 for master branch
https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts/-/merge_requests/62 for qa branch

will close once those are merged

## Comment (belforte, 2023-02-22T14:04:39Z)

PR's in gitlab merged. Let's see if last scheduler `vocms0107` is going to be cleared next time crontab runs
```
belforte@vocms0106/crab> date
Wed Feb 22 15:04:19 CET 2023
belforte@vocms0106/crab> condor_status -sched -con 'machine=="vocms0107.cern.ch"'
Name                    Machine           RunningJobs   IdleJobs   HeldJobs

crab3@vocms0107.cern.ch vocms0107.cern.ch        6198       3213       8533
```

## Comment (belforte, 2023-02-23T08:10:28Z)

new crontab worked finely, held jobs went from 8K to 1K. Closing.
```
belforte@vocms0106/crab> date
Thu Feb 23 09:08:39 CET 2023
belforte@vocms0106/crab> condor_status -sched -con 'machine=="vocms0107.cern.ch"'
Name                    Machine           RunningJobs   IdleJobs   HeldJobs

crab3@vocms0107.cern.ch vocms0107.cern.ch        6528       1533       1216

                TotalRunningJobs      TotalIdleJobs      TotalHeldJobs

              
         Total              6528               1533               1216
belforte@vocms0106/crab> 
```
