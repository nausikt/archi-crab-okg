# dmwm/CRABServer issue #8802: Overflow via JobRouter edits too many jobs

State: closed
Opened: 2024-11-19T15:48:18Z
Closed: 2024-11-22T15:22:06Z
Labels: Type: Bug, Status: In Progress, Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8802

## Opening post (belforte, 2024-11-19T15:48:18Z)

There is ample evidence that jobs which should not be routed, are instead routed.
Also there are jobs routed from European T1's which according to our monitoring run in the US.
We have disabled JobRouter daemon, but need to fix.

As a start will put JobRouter in "tagging mode": add a new classAd with the indication of where job would be routed, but do not edit `DESIRED_Sites`.

## Comment (belforte, 2024-11-19T16:13:43Z)

tag mode enabled in puppet qa via https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/288
now deployed on vocms059
**note**:  puppet agent will not star Job_Router daemon.  Needs and explicit `sudo condor_on --daemon Job_Router`

## Comment (belforte, 2024-11-19T16:16:45Z)

and the problem is immediately very clear, the table for the first job (KIT) has been applied to all of the following jobs, which were in Idle since some time, but targeting very different sites !!

```text
[root@vocms059 config.d]# condor_q -con HasBeenOverflowRouted -af:h JobUniverse jobstatus desired_sites desired_sites_orig new_sites
JobUniverse jobstatus desired_sites             desired_sites_orig        new_sites                      
5           1         T1_DE_KIT                 T1_DE_KIT                 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_ES_PIC                 T1_ES_PIC                 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_FR_CCIN2P3             T1_FR_CCIN2P3             T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_IT_CNAF                T1_IT_CNAF                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_RU_JINR                T1_RU_JINR                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_UK_RAL                 T1_UK_RAL                 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T1_US_FNAL                T1_US_FNAL                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_CH_CERN_HLT            T2_CH_CERN_HLT            T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_CH_CERN_P5             T2_CH_CERN_P5             T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_IN_TIFR                T2_IN_TIFR                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_IT_Rome                T2_IT_Rome                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_LB_HPC4L               T2_LB_HPC4L               T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_PK_NCP                 T2_PK_NCP                 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_TR_METU                T2_TR_METU                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T2_UK_SGrid_Bristol       T2_UK_SGrid_Bristol       T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_BG_UNI_SOFIA           T3_BG_UNI_SOFIA           T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_IN_TIFRCloud           T3_IN_TIFRCloud           T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_IT_Opportunistic_dodas T3_IT_Opportunistic_dodas T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_MX_Cinvestav           T3_MX_Cinvestav           T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_TW_TIDC                T3_TW_TIDC                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_US_FNALLPC             T3_US_FNALLPC             T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_US_Ookami              T3_US_Ookami              T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_US_Test                T3_US_Test                T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
5           1         T3_US_UMD                 T3_US_UMD                 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
[root@vocms059 config.d]# 

```

## Comment (belforte, 2024-11-19T17:41:39Z)

side notes, as I read with more care the current [JR config](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/files/crabschedd/90_jobrouter.config?ref_type=heads) I realize that
* `TargetUniverse = 5` is useless (at least)
* `SET RouteType "overflow"` is not needed (we only have one type)
* ` OverrideRoutingEntry = True` is not needed (it is the default)
* it may be good to add [JOB_ROUTER_NAME](https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#JOB_ROUTER_NAME) it seems that it may make it automatical to avoid recursive routing, so we do not need anymore ` (HasBeenOverflowRouted is undefined)`
* We could use a PRE table to put all common actions in a single place

## Comment (belforte, 2024-11-19T21:19:30Z)

I tried various simplifications and changes to `()` in an attempt to "fix the requirements", but no matter what I tried, all idle jobs are routed via the same route !

I [wrote](https://www-auth.cs.wisc.edu/lists/htcondor-users/2024-November/msg00076.shtml) to HTC support list

```text
Dear experts,

we (CMS-CRAB) have used JobRouter since years to edit queued jobs in CMS global pool to redirect then from busy sites to sites with possibly available slots, something that we call "overflow". Details of why and what happens to those jobs when they run do not matter, simply to introduce the name.

Alas we have been using the deprecated JOB_ROUTER_ENTRIES_CMD macro where custom script of ours was called to create routing on the fly So last month we rewrote our stuff using static routing table in the configuration file reproducing the same desiderata. But once put in production things started to go nuts and we had to disable.

Unfortunately we have no experience with the new configuration, and nobody else in CMS or glideinWms is using it.

We are running $CondorVersion: 23.9.6 2024-08-08 BuildID: 748275 PackageID: 23.9.6-1 GitSHA: dfdd9eaa $
and followed the example in https://htcondor.readthedocs.io/en/latest/grid-computing/job-router.html defining a list of mutually exclusive routes as in [1]

But once the daemon starts the first route is matched to all possible jobs, even if the Requirements = (DESIRED_SITES=="sitename") is not satisfied.

Some things work as expected i.e. the edit in place, attribute setting, and the route listed first in JOB_ROUTER_ROUTE_NAMES is clearly the one used first. But that first rout is also applied to jobs where DESIRED_SITES is a different string.

Basically all my idle jobs get the same value of NEW_SITES and I can change that by changing the order or routes in JOB_ROUTER_ROUTE_NAMES [2].

Can you spot something which we do wrong here ?

I also noted that while jobs are routed, the RoutedBy attributes is not set (ref https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#JOB_ROUTER_SOURCE_JOB_CONSTRAINT and https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#JOB_ROUTER_NAME )

Let us know if there's any more information which I can send.

Thanks!!!

Stefano


[1]

[root@vocms059 config.d]# pwd
/etc/condor/config.d
[root@vocms059 config.d]# cat 90_jobrouter.config
# Configuration file for the JobRouter
#
JOB_ROUTER_NAME = OverflowRouter

JOB_ROUTER_SOURCE_JOB_CONSTRAINT = ((JobUniverse==5) && (jobstatus==1))

# Static route names for each T1
JOB_ROUTER_ROUTE_NAMES =  T1_DE_KIT T1_IT_CNAF T1_UK_RAL T1_ES_PIC T1_FR_CCIN2P3

JOB_ROUTER_ROUTE_T1_DE_KIT @=rtkit
  Name = ["Overflow:T1_DE_KIT"](overflow:T1_DE_KIT)
  EditJobInPlace = True
  Requirements = (DESIRED_SITES=="T1_DE_KIT")
  SET NEW_SITES "T2_DE_DESY"
  SET HasBeenOverflowRouted True
@rtkit

JOB_ROUTER_ROUTE_T1_ES_PIC @=rtpic
  Name = ["Overflow:T1_ES_PIC"](overflow:T1_ES_PIC)
  EditJobInPlace = True
  Requirements = (DESIRED_SITES=="T1_ES_PIC")
  SET NEW_SITES "T2_ES_CIEMAT"
  SET HasBeenOverflowRouted True
@rtpic

JOB_ROUTER_ROUTE_T1_FR_CCIN2P3 @=rtin2p3
  Name = ["Overflow:T1_FR_CCIN2P3"](overflow:T1_FR_CCIN2P3)
  EditJobInPlace = True
  Requirements = (DESIRED_SITES=="T1_FR_CCIN2P3")
  SET NEW_SITES "T2_FR_GRIF,T2_FR_IPHC"
  SET HasBeenOverflowRouted True
@rtin2p3

JOB_ROUTER_ROUTE_T1_IT_CNAF @=rtcnaf
  Name = ["Overflow:T1_IT_CNAF"](overflow:T1_IT_CNAF)
  EditJobInPlace = True
  Requirements = (DESIRED_SITES=="T1_IT_CNAF")
  SET NEW_SITES "T2_IT_Pisa,T2_IT_Rome"
  SET HasBeenOverflowRouted True
@rtcnaf

JOB_ROUTER_ROUTE_T1_UK_RAL @=rtral
  Name = ["Overflow:T1_UK_RAL"](overflow:T1_UK_RAL)
  EditJobInPlace = True
  Requirements = (DESIRED_SITES=="T1_UK_RAL")
  SET NEW_SITES "T2_UK_London_IC,T2_UK_SGrid_RALPP"
  SET HasBeenOverflowRouted True
@rtral

# How often to poll the job queue to route jobs
JOB_ROUTER_POLLING_PERIOD = 5*60

# Start the Job Router
DAEMON_LIST = $(DAEMON_LIST) JOB_ROUTER
[root@vocms059 config.d]#

[2]

belforte@vocms059/HTCondor> condor_q -con HasBeenOverflowRouted -af:h jobstatus desired_sites  new_sites
jobstatus desired_sites             new_sites
1         T1_DE_KIT                 T2_DE_DESY
1         T1_ES_PIC                 T2_DE_DESY
1         T1_FR_CCIN2P3             T2_DE_DESY
1         T1_IT_CNAF                T2_DE_DESY
1         T1_UK_RAL                 T2_DE_DESY
1         T1_US_FNAL                T2_DE_DESY
1         T2_CH_CERN_HLT            T2_DE_DESY
1         T2_CH_CERN_P5             T2_DE_DESY
1         T2_IN_TIFR                T2_DE_DESY
1         T2_IT_Rome                T2_DE_DESY
1         T2_LB_HPC4L               T2_DE_DESY
1         T2_PK_NCP                 T2_DE_DESY
1         T2_TR_METU                T2_DE_DESY
1         T2_UK_SGrid_Bristol       T2_DE_DESY
1         T3_BG_UNI_SOFIA           T2_DE_DESY
1         T3_IN_TIFRCloud           T2_DE_DESY
1         T3_IT_Opportunistic_dodas T2_DE_DESY
1         T3_MX_Cinvestav           T2_DE_DESY
1         T3_TW_TIDC                T2_DE_DESY
1         T3_US_FNALLPC             T2_DE_DESY
1         T3_US_Ookami              T2_DE_DESY
1         T3_US_Test                T2_DE_DESY
1         T3_US_UMD                 T2_DE_DESY
1         T1_IT_CNAF                T2_DE_DESY
1         T1_IT_CNAF                T2_DE_DESY
1         T1_ES_PIC                 T2_DE_DESY
1         T1_FR_CCIN2P3             T2_DE_DESY
1         T1_UK_RAL                 T2_DE_DESY
1         T1_UK_RAL                 T2_DE_DESY
belforte@vocms059/HTCondor>
```

## Comment (belforte, 2024-11-20T08:28:51Z)

here's [answer](https://www-auth.cs.wisc.edu/lists/htcondor-users/2024-November/msg00077.shtml) from TJ (slightly edited with [tip](https://www-auth.cs.wisc.edu/lists/htcondor-users/2024-November/msg00079.shtml))
```text
 In the new syntax the way to set requirements for the route is to use REQUIREMENTS without an = after it.  The same for NAME, and UNIVERSE although NAME will default to the config knob suffix. 

Effects that are applied after the route has been matched, most of which can be expressions such as EditJobInPlace are still set using =,   but NAME, UNIVERSE and REQUIREMENTS are transform commands, Requirements = would be treated as a temporary variable and it would not affect the matching of the route to a job. 

If you run 

    condor_job_router_info you should see that your routes don't have any route REQUIREMENTS, and that the NAME of the route is not what you spacified by Name =, since the default route name is derived from the knob name.

So your routes should be

JOB_ROUTER_ROUTE_T1_DE_KIT @=rtkit
   NAME Overflow:T1_DE_KIT
   REQIREMENTS  (DESIRED_SITES=="T1_DE_KIT")
   EditJobInPlace = True
   SET NEW_SITES "T2_DE_DESY"
   SET HasBeenOverflowRouted True
@rtkit

Sorry about the confusion.   An editing pass to improve the clarity of the manual incorrectly added the =  after REQUIREMENTS in the documentation.  
```

## Comment (belforte, 2024-11-20T09:10:31Z)

useful info about JobRouter is also in https://indico.cern.ch/event/1059494/contributions/4532568/attachments/2315533/3941565/2021-09-24.htcondor-ce-5-jr-transforms.pdf

## Comment (belforte, 2024-11-20T20:21:12Z)

after several iterations of trial-and-error, I have finalized a configuration which looks good to me. Now put in puppet `qa` branch (i.e. vocms059) for more testing.
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/289

## Comment (belforte, 2024-11-20T20:24:38Z)

hopefully comments in the new config. file are explanatory. @aspiringmind-code have a look at your convenience and let me know if you think that it is clear enough:  https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/e1467de28a0b758e49bc7bb348626fdb11786f52/code/files/crabschedd/90_jobrouter.config

After some (quick) tests on vocms059 we can deploy on all schedd's in this tag mode. test more, and eventually turn on editing of DESIRED_Sites

## Comment (belforte, 2024-11-21T09:26:16Z)

things look good on vocms059. Will deploy new JR config in tagging mode on all HTC AccessPoints: https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/290

## Comment (belforte, 2024-11-21T16:43:34Z)

hopefully correct JR config file is now being deployed in tagging mode on all schedds by puppet
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/90_jobrouter_tag.config?ref_type
Once agent has run we need to do restart daemon manually
```
belforte@aiadm01/~> wassh -c glidein/crabschedd "sudo condor_on -daemon job_router"
```

## Comment (belforte, 2024-11-21T17:46:10Z)

OK. Running everywhere now.

## Comment (belforte, 2024-11-22T10:40:05Z)

I verified situation on our AP's with
```console

belforte@vocms059/~> condor_q -global -con hasbeenoverflowrouted -af desired_sites desired_sites_orig new_sites > ov

belforte@vocms059/~> wc -l ov
13111 ov
belforte@vocms059/~> cat ov|sort|uniq -c
   4580 T1_DE_KIT T1_DE_KIT T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH
      7 T1_DE_KIT T1_DE_KIT T2_DE_DESY
     27 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH T1_DE_KIT undefined
     32 T1_ES_PIC T1_ES_PIC T1_ES_PIC,T2_ES_CIEMAT,T2_ES_IFCA
      1 T1_ES_PIC,T2_ES_CIEMAT,T2_ES_IFCA T1_ES_PIC undefined
   4372 T1_FR_CCIN2P3 T1_FR_CCIN2P3 T1_FR_CCIN2P3,T2_FR_GRIF,T2_FR_IPHC
      4 T1_FR_CCIN2P3 T1_FR_CCIN2P3 T2_FR_GRIF,T2_FR_IPHC
      3 T1_FR_CCIN2P3,T2_FR_GRIF,T2_FR_IPHC T1_FR_CCIN2P3 undefined
   1863 T1_IT_CNAF T1_IT_CNAF T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome
     22 T1_IT_CNAF T1_IT_CNAF T2_IT_Pisa,T2_IT_Rome
      2 T1_IT_CNAF,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome T1_IT_CNAF undefined
   2068 T1_UK_RAL T1_UK_RAL T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP
    127 T1_UK_RAL T1_UK_RAL T2_UK_London_IC,T2_UK_SGrid_RALPP
      3 T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP T1_UK_RAL undefined
belforte@vocms059/~> cat ov|sort|uniq -c|grep undef
     27 T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH T1_DE_KIT undefined
      1 T1_ES_PIC,T2_ES_CIEMAT,T2_ES_IFCA T1_ES_PIC undefined
      3 T1_FR_CCIN2P3,T2_FR_GRIF,T2_FR_IPHC T1_FR_CCIN2P3 undefined
      2 T1_IT_CNAF,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome T1_IT_CNAF undefined
      3 T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP T1_UK_RAL undefined
belforte@vocms059/~> 
```
The few jobs with `NEW_SITES = undefined` are from previous running and `DESIRED_SITES` has been edited already to a list.

Looks all good to me

## Comment (belforte, 2024-11-22T10:42:15Z)

@aspiringmind-code what do you think ? Shall we go ahead and "activate" this ?

## Comment (aspiringmind-code, 2024-11-22T10:47:41Z)

Yes, sure! :)

## Comment (belforte, 2024-11-22T10:49:18Z)

OK. I will do

## Comment (belforte, 2024-11-22T13:38:25Z)

deployed on `qa` and tested on vocms059. OK. Moving to all AP's

## Comment (belforte, 2024-11-22T13:41:24Z)

merged changes in puppet `master` branch

## Comment (belforte, 2024-11-22T13:47:37Z)

waiting for puppet agent to run, I have reset the `hasbeenoverflowrouted` ad for all jobs
```console
belforte@aiadm01/~> wassh -c glidein/crabschedd "sudo condor_qedit -con hasbeenoverflowrouted hasbeenoverflowrouted=undefined"
crab-preprod-scd03.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
crab-sched-901.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
crab-sched-903.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
vocms0106.cern.ch: Set attribute "hasbeenoverflowrouted" for 155 matching jobs.
vocms0107.cern.ch: Set attribute "hasbeenoverflowrouted" for 12 matching jobs.
vocms0119.cern.ch: Set attribute "hasbeenoverflowrouted" for 152 matching jobs.
vocms0120.cern.ch: Set attribute "hasbeenoverflowrouted" for 397 matching jobs.
vocms0121.cern.ch: Set attribute "hasbeenoverflowrouted" for 384 matching jobs.
vocms0122.cern.ch: Set attribute "hasbeenoverflowrouted" for 10 matching jobs.
vocms0137.cern.ch: Set attribute "hasbeenoverflowrouted" for 1382 matching jobs.
vocms0144.cern.ch: Set attribute "hasbeenoverflowrouted" for 63 matching jobs.
vocms0155.cern.ch: Set attribute "hasbeenoverflowrouted" for 151 matching jobs.
vocms0194.cern.ch: Set attribute "hasbeenoverflowrouted" for 1547 matching jobs.
vocms0195.cern.ch: Set attribute "hasbeenoverflowrouted" for 1263 matching jobs.
vocms0196.cern.ch: Set attribute "hasbeenoverflowrouted" for 3117 matching jobs.
vocms0197.cern.ch: Set attribute "hasbeenoverflowrouted" for 1317 matching jobs.
vocms0198.cern.ch: Set attribute "hasbeenoverflowrouted" for 167 matching jobs.
vocms0199.cern.ch: Set attribute "hasbeenoverflowrouted" for 2722 matching jobs.
vocms059.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
vocms068.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
vocms069.cern.ch: 
   Failed to set attribute "hasbeenoverflowrouted" by constraint: ( (hasbeenoverflowrouted) )
   Queue transaction failed.  No attributes were set.
belforte@aiadm01/~> 
```

## Comment (belforte, 2024-11-22T15:21:57Z)

daemon started with `wassh -c glidein/crabschedd "sudo condor_on -daemon job_router"`
