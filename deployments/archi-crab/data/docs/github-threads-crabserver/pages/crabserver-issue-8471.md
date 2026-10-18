# dmwm/CRABServer issue #8471: resubmission fails after changing to use of submitObject 

State: closed
Opened: 2024-06-04T07:30:13Z
Closed: 2024-06-10T10:36:33Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8471

## Opening post (belforte, 2024-06-04T07:30:13Z)

see https://github.com/dmwm/CRABServer/issues/8469#issuecomment-2146803990
error is
```
  File "/data/srv/TaskManager/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/slc7_amd64_gcc630/cms/crabtaskworker/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/lib/python3.8/site-packages/TaskWorker/Actions/DagmanResubmitter.py", line 95, in executeInternal
    schedd.edit(rootConst, "HoldKillSig", 'SIGKILL')
  File "/data/srv/TaskManager/v3.240603-c9fbdc0538bd0008e8fe4e772eece824/slc7_amd64_gcc630/external/py3-htcondor/10.2.3/lib/python3.8/site-packages/htcondor/_lock.py", line 70, in wrapper
    rv = func(*args, **kwargs)
htcondor.HTCondorIOError: Unable to edit jobs matching constraint

```

## Comment (belforte, 2024-06-04T07:34:44Z)

task details
```
belforte@lxplus807/bot> crab status crab_20240604_001652/
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab_20240604_001652
Task name:			240603_221653:cmsbot_crab_20240604_001652
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	RESUBMITFAILED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/240603_221653%3Acmsbot_crab_20240604_001652
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=cmsbot&var-task=240603_221653%3Acmsbot_crab_20240604_001652&from=1717449413000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Failure message from server:	The CRAB server backend was not able to resubmit the task, because the Grid scheduler answered with an error. This is probably a temporary glitch. Please try again later. If the error persists send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch. Error reason: Unable to edit jobs matching constraint
Status on the 
```

## Comment (belforte, 2024-06-04T07:40:56Z)

the dag bootstrap job is odd on schedd side
```

belforte@vocms059/T> condor_q -con 'jobuniverse==7 && CRAB_ReqName =?= "240603_221653:cmsbot_crab_20240604_001652"' -l|grep TaskType
CMS_TaskType = "cmsRun"
CRAB_DashboardTaskType = "analysis"
TaskType = ROOT
belforte@vocms059/T> condor_q -con 'jobuniverse==7 && CRAB_ReqName =?= "240603_221653:cmsbot_crab_20240604_001652"' -af tasktype
[ ClusterId = 9616428; ProcId = 0; tasktype = ROOT ]
belforte@vocms059/T> 
```

## Comment (belforte, 2024-06-04T07:43:12Z)

other jobs in scheduler universe show the expected value
```

belforte@vocms059/T> condor_q -con 'jobuniverse==7' -af:h tasktype crab_reqname|head
tasktype   crab_reqname                                                                         
ROOT       240429_195435:tseethon_crab_20240429_215435                                          
ROOT       240429_195438:tseethon_crab_20240429_215437                                          
ROOT       240429_195439:tseethon_crab_20240429_215439                                          
ROOT       240429_195441:tseethon_crab_20240429_215441                                          
ROOT       240429_195443:tseethon_crab_20240429_215442                                          
ROOT       240429_195446:tseethon_crab_20240429_215444                                          
ROOT       240429_195449:tseethon_crab_rucio_transfers_20240429_215447                          
ROOT       240429_195451:tseethon_crab_rucio_transfers_group_20240429_215450                    
ROOT       240429_195454:tseethon_crab_rucio_transfers_manyedm_nopublication_20240429_215452    
belforte@vocms059/T> 

```

## Comment (belforte, 2024-06-04T08:48:31Z)

this time I can't reprouce the problem with a simple submission on the scheduler. All in all other tasks are fine, so the problem is tied to using submitObject.

## Comment (belforte, 2024-06-04T11:13:26Z)

as usual these days, I ended up writing to HTCondor folks
https://lists.cs.wisc.edu/archive/htcondor-users/2024-June/msg00017.shtml

```
Dear experts,
sorry to report a new problem when migrating CMS CRAB to submit via
 schedd.submit(submitObject,...)

We add custom classAds to jobs for use in glideinWMS (which still works)
and we also add one which we use later on to use as a constrain
in condor_q, condor_qedit and other commads.

The latter thing fails. I have managed to reproduce to the problem
to a simple test using local submission with python bindings.

Hopefully lines below are self-explaining, if not, ask me.
Note in particular the output of
 condor_q 9620532 -af:h StefanoAd CRAB_TT
And of course the fact that condor_q -con .. does not select any job

Things look as expected if I put same info in a JDL file and do a plain
condor_submit test.jdl and also if I construct the htcondor.submit()
object passing the full jdl to it via ("""jdl lines"""). There are other
oddities,like if in the example below I change 'ROOT' to 'ROT' output
is different and while -con still fails, condor_q -af returns uniformly
"undefined". I can of course change ROOT to a different string in our code, but it would be good to have a rational.

Our "old way" was to use schedd.submit(classAds,...)
and things were OK.

If you prefer to move this to some more interactive channel
(our GH ?) tell me as well.

Thanks a lot
Stefano

belforte@vocms059/T> condor_version
$CondorVersion: 23.0.4 2024-02-08 BuildID: 712251 PackageID: 23.0.4-1 $
$CondorPlatform: x86_64_AlmaLinux9 $

belforte@vocms059/T> cat mytest.py
import htcondor

schedd = htcondor.Schedd()

jdl = htcondor.Submit()
jdl['Universe']   = "scheduler"
jdl['Executable'] = "None"
jdl['Log'] = "myTest.log"

jdl['+StefanoAd'] = "TestString"
jdl['+CRAB_TT'] = "ROOT"

print(jdl)

res = schedd.submit(jdl, count=1)
print(res.cluster())

belforte@vocms059/T> python3 mytest.py
Universe = scheduler
Executable = None
Log = myTest.log
MY.StefanoAd = TestString
MY.CRAB_TT = ROOT

9620532

belforte@vocms059/T> condor_q 9620532 -l|grep StefanoAd
StefanoAd = TestString
belforte@vocms059/T> condor_q 9620532 -l|grep CRAB_TT
CRAB_TT = ROOT
belforte@vocms059/T> condor_q 9620532 -af:h StefanoAd CRAB_TT
StefanoAd CRAB_TT
undefined [ ClusterId = 9620532; ProcId = 0; CRAB_TT = ROOT; StefanoAd = TestString ]

belforte@vocms059/T> condor_q -con 'StefanoAd=="TestString"'


-- Schedd: [crab3@vocms059.cern.ch](mailto:crab3@vocms059.cern.ch) : <188.184.103.189:4080?... @ 06/04/24 12:46:59
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD

Total for query: 0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
Total for all users: 79 jobs; 3 completed, 0 removed, 0 idle, 76 running, 0 held, 0 suspended

belforte@vocms059/T> condor_q -con 'CRAB_TT=="ROOT"'


-- Schedd: [crab3@vocms059.cern.ch](mailto:crab3@vocms059.cern.ch) : <188.184.103.189:4080?... @ 06/04/24 12:47:16
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD

Total for query: 0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
Total for all users: 79 jobs; 3 completed, 0 removed, 0 idle, 76 running, 0 held, 0 suspended

belforte@vocms059/T>
```

## Comment (belforte, 2024-06-05T08:06:44Z)

here's ToddM explanation/clarification
```


On 04/06/2024 18:36, Todd L Miller via HTCondor-users wrote:
>> jdl['+StefanoAd'] = "TestString"
>> jdl['+CRAB_TT'] = "ROOT"
> 
>      Note that this sets the ClassAd expression StefanoAd to the ClassAd 
> attribute reference TestString, not the _string_ "TestString",
> which given the name, is probably not what you're expecting.  Likewise, 
> CRAB_TT is being set to the attribute reference ROOT, which happens to 
> be magical.  I'm not sure why this works in the JDL, but perhaps there's 
> more magic in the parser there than I thought.
> 
> - ToddM
```

## Comment (belforte, 2024-06-10T10:36:33Z)

things were  a bit tricky to do right, since DagmanSubmitter fills many attributes from the `info` dictionary created by DagmanCreator where most attributes already have `""...""` around them.  So a "classad.quote them all" fails.

I have moved development of this to a new branch https://github.com/dmwm/CRABServer/tree/modernize_HTC
where  I will push from https://github.com/belforte/CRABServer/tree/modernize_HTC
