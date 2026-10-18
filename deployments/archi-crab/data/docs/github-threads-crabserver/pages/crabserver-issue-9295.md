# dmwm/CRABServer issue #9295: extend Overflow via JobRouting

State: closed
Opened: 2026-04-09T16:23:16Z
Closed: 2026-06-29T12:51:18Z
Labels: Type: Enhancement, Status: In Progress, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9295

## Opening post (belforte, 2026-04-09T16:23:16Z)

we do overflow via HTCondor JobRouter via the file [/etc/condor/config.d/90_jobrouter.config](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/90_jobrouter.config?ref_type=heads) in our AP's

That currently covers:
 * when input dataset is present ONLY at one European T1, add same country T2's to `DESIRED_SITES

Recently we have found that sometimes user jobs stay queued for a long time due to lack or CPU at T1's in cases like
* dataset has 2 disk replicas, both at T1's
* job list as DESIRED_SITES T1_US_FNAL and T3_US_FNALLPC (a uses case not covered by overflow via frontend group in gWms [1] ). in particular when users are accessing MINIAOD*
   * Note: T3_US_FNALLPC is always added for all datasets at T1_US_FNAL_Disk, as per CRIC list of  [Allowed Sites](https://cms-cric.cern.ch/cms/storageunit/detail/T1_US_FNAL_Disk/)
   * the above combined with [1] means that jobs which target datasets at FNAL are never overflown inside US.

A partial mitigation  should have come from having increased analysis fraction at T1's by 10%.

Following the discusssion with CompOps in [CMSTRANSF-1323](https://its.cern.ch/jira/browse/CMSTRANSF-1323) we should extend the overflow routes to cover those as well.

Also consider the use case
* dataset has 2 disk replicas: one at T1, one at T2.
in that case we end up with the T1 replica being unused, so we may consider overflow for those as well.

I do not know it is makes any difference to limit to dataset being MINIADO*, it is very rare that an other dataset is present at 2 sites. But we may not want to bother with NANO* which presently have 5 replicas.

 [1] https://mattermost.web.cern.ch/cms-o-and-c/pl/jtf5ose3xbnw3ybdiaj453by6h

## Comment (nausikt, 2026-04-09T16:30:27Z)

The ticket was extremely rich, will make sure i properly digested it.🫠
*P.S. let me know if there is anything i could be of any help.*

## Comment (belforte, 2026-04-09T16:45:24Z)

No need for you to loose sleep on this Krittin. I think I will take of this myself w/o problems.
Maybe a good chance to exercise Claude again. Vijay already gave it a try using AI, but got a file with a not-proper syntax which made testing a nightmare and I gave up. Alas that was discussed in 1-1 chat.

For my use I am pasting here the proposed addition, the important bits are the use of `regext` and `strcat`
```
JOB_ROUTER_ROUTE_MULTI_T1 @=multi_t1
  REQUIREMENTS regexp("T1_.*T1_", DESIRED_SITES)

  SET DESIRED_SITES = strcat(
    DESIRED_SITES,

    ifThenElse(regexp("T1_DE_", DESIRED_SITES),
      ",T2_DE_DESY,T2_DE_RWTH", ""),

    ifThenElse(regexp("T1_ES_", DESIRED_SITES),
      ",T2_ES_CIEMAT,T2_ES_IFCA", ""),

    ifThenElse(regexp("T1_IT_", DESIRED_SITES),
      ",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""),

    ifThenElse(regexp("T1_FR_", DESIRED_SITES),
      ",T2_FR_GRIF,T2_FR_IPHC", ""),

    ifThenElse(regexp("T1_UK_", DESIRED_SITES),
      ",T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", "")
  )

@multi_t1
```

## Comment (belforte, 2026-04-09T16:53:53Z)

more notes from the MM chat
``` inside the multi-line tags @multit1..@multit1 every config. statement has to be a single line.``` 
`\` helps !
e.g. (from Vijay):
```
SET DESIRED_SITES = strcat( \
  ifThenElse(isUndefined(DESIRED_SITES), "", DESIRED_SITES), \
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), ",T2_DE_DESY,T2_DE_RWTH", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), ",T2_ES_CIEMAT,T2_ES_IFCA", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), ",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), ",T2_FR_GRIF,T2_FR_IPHC", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), ",T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), ",T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin", "") \
)
```

and here's my last attempt to the `90_jobrouter.config` when I tried
```
# Configuration file for the JobRouter
# 

# Specifiy a global Requirements expression that must be true for all newly routed jobs,
# in addition to any Requirements specified within a routing table entry
#
JOB_ROUTER_SOURCE_JOB_CONSTRAINT =           ( \
    (JobUniverse==5) \
 && (jobstatus==1) \
 && (CRAB_UserHN != "sciaba") \
 && (HasBeenOverflowRouted is undefined) \
 && (CMS_ALLOW_OVERFLOW == "True") \
 && (time() - EnteredCurrentStatus > 1200) \
                                             )

# define a pre-route transform that does the transforms all routes should do
# After experimenting we found that EditJobInPlace and UNIVERSE directives
# do not work if places here. They need to be replicated inside each T1-specific route
#
JOB_ROUTER_PRE_ROUTE_TRANSFORM_NAMES = Defaults

JOB_ROUTER_TRANSFORM_Defaults @=jrd
  SET HasBeenOverflowRouted True
  EVALSET LastRouted time()
  EVALSET DESIRED_SITES_Orig = DESIRED_SITES
@jrd


# Static route names for each T1 (since they are exclusive
# order does not matter, use alphabetic here)
#
JOB_ROUTER_ROUTE_NAMES = T1_DE_KIT T1_ES_PIC T1_FR_CCIN2P3 T1_IT_CNAF T1_UK_RAL MULTI_T1

JOB_ROUTER_ROUTE_T1_DE_KIT @=rtkit
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_DE_KIT")
  SET DESIRED_SITES "T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH"
@rtkit

JOB_ROUTER_ROUTE_T1_ES_PIC @=rtpic
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_ES_PIC")
  SET DESIRED_SITES "T1_ES_PIC,T2_ES_CIEMAT,T2_ES_IFCA"
@rtpic

JOB_ROUTER_ROUTE_T1_FR_CCIN2P3 @=rtin2p3
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_FR_CCIN2P3")
  SET DESIRED_SITES "T1_FR_CCIN2P3,T2_FR_GRIF,T2_FR_IPHC"
@rtin2p3

JOB_ROUTER_ROUTE_T1_IT_CNAF @=rtcnaf
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_IT_CNAF")
  SET DESIRED_SITES "T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome"
@rtcnaf

JOB_ROUTER_ROUTE_T1_UK_RAL @=rtral
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_UK_RAL")
  SET DESIRED_SITES "T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP"
@rtral

JOB_ROUTER_ROUTE_MULTI_T1 @=multit1
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS regexp("T1_.*T1_", DESIRED_SITES)

  SET DESIRED_SITES = strcat(DESIRED_SITES,ifThenElse(regexp("T1_DE_", DESIRED_SITES),",T2_DE_DESY,T2_DE_RWTH", ""), ifThenElse(regexp("T1_ES_", DESIRED_SITES),",T2_ES_CIEMAT,T2_ES_IFCA", ""),ifThenElse(regexp("T1_IT_", DESIRED_SITES),",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""),ifThenElse(regexp("T1_FR_", DESIRED_SITES),",T2_FR_GRIF,T2_FR_IPHC", ""),ifThenElse(regexp("T1_UK_", DESIRED_SITES),",T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", ""),ifThenElse(regexp("T1_US_", DESIRED_SITES),"T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin,", ""))

@multit1

# How often to poll the job queue to route jobs
#
JOB_ROUTER_POLLING_PERIOD = 5*60

# Start the Job Router
# Reminder: you must restart HTCondor for changes to DAEMON_LIST to take effect.
# e.g. condor_off -daemon job_router; condor_on -daemon job_router
#
DAEMON_LIST = $(DAEMON_LIST) JOB_ROUTER
```


**The problem back then was that misconfigured jobrouted file ended up in hundreds of jobs having DESIRED_SITES set to null string.**

**This time I need a careful test program !**

## Comment (belforte, 2026-04-13T16:44:37Z)

I have added these two routes to `90_jobrouter.config` on vocms0198, The AP with the most idle jobs.
I had already tested the T1_US_FNAL route by using it in "tag mode", like the MULTI_T1 here.
Will let it run for a bit and then start pushing to AP's.
Too bad we do not have a way to roll out the change "one AP at a time".
But we can fully enable/disable overflow on an VM by VM basis with `enable_overflow` in VM-specific YAML file

```

# need a route for FNAL because many jobs matching it match also T3_US_FNALLPC and
# gWms-group-based overflow in the US does not work for those
JOB_ROUTER_ROUTE_T1_US_FNAL @=rtfnal
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  # matches jobs which target T1_FNAL and FNALLPC but do not have already an US Tier2 site
  REQUIREMENTS  (regexp("T3_US_FNALLPC",DESIRED_SITES)&&regexp("T1_US_FNAL",DESIRED_SITES)&&!regexp("T2_US",DESIRED_SITES))
  SET DESIRED_SITES strcat(DESIRED_SITES, "T2_US_Caltech,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin")
@rtfnal

JOB_ROUTER_ROUTE_MULTI_T1 @=multit1
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS regexp("T1_.*T1_", DESIRED_SITES)

  SET MT1_SITES = strcat( \
  ifThenElse(isUndefined(DESIRED_SITES), "", DESIRED_SITES), \
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), ",T2_DE_DESY,T2_DE_RWTH", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), ",T2_ES_CIEMAT,T2_ES_IFCA", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), ",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), ",T2_FR_GRIF,T2_FR_IPHC", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), ",T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), ",T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin", "") \
)

@multit1
```

## Comment (belforte, 2026-04-13T16:55:19Z)

Multi_t1 table looks good, but I will not do more changes until tomorrow.

## Comment (belforte, 2026-04-14T08:55:07Z)

did not really work since. In spite of testing I made a mess and not there are job on vocms0198 like this,
which are not matching
```
belforte@vocms0198/~> condor_q 141476738 -l|grep -i "desired_sites = "
DESIRED_SITES = strcat(DESIRED_SITES,"T2_US_Caltech,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin")
 belforte@vocms0198/~> condor_q 141476738 -af desired_sites

belforte@vocms0198/~> 
```
so for the time being I have done
`[root@vocms0198 config.d]# condor_off --daemon job_router`

I will try to find out what's happened and fix the table. Luckily we know how to revert
```
belforte@vocms0198/~> condor_q 141476738 -l|grep -i "desired_sites_orig"
DESIRED_SITES_Orig = "T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC"
```

## Comment (belforte, 2026-04-14T09:27:32Z)

I have hopefully corrected the situation with
```
[root@vocms0198 belforte]# condor_qedit -con 'jobuniverse==5&&jobstatus==1&&HasBeenOverflowRouted&&regexp("T3_US_FNALLPC",desired_sites_orig)&&regexp("T1_US_FNAL",desired_sites_orig)' DESIRED_SITES=DESIRED_SITES_Orig
Set attribute "DESIRED_SITES" for 5552 matching jobs.
[root@vocms0198 belforte]# 
```

## Comment (belforte, 2026-04-14T17:41:27Z)

I am triying to test/validate the `strcat` via condor_qedit, but am stuck on a very odd behavior
```
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_qedit 1641601.0 desired_sites="123"
Set attribute "desired_sites" for 1 matching jobs.
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_q 1641601.0 -af desired_sites
123
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_qedit 1641601.0 desired_sites="abba"
Set attribute "desired_sites" for 1 matching jobs.
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_q 1641601.0 -af desired_sites
undefined
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_version
$CondorVersion: 25.0.3 2025-10-31 BuildID: 847298 PackageID: 25.0.3-1 GitSHA: dc94bfbb $
$CondorPlatform: x86_64_AlmaLinux9 $
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ 
```

## Comment (belforte, 2026-04-14T17:50:32Z)

I asked for help again : https://www-auth.cs.wisc.edu/lists/htcondor-users/2026-April/msg00030.shtml

## Comment (belforte, 2026-04-14T23:53:17Z)

stupid shell quoting problem. condor_qedit works fine

Yet, the solution still escapes me. I wrote more in that thread in condor user list

## Comment (belforte, 2026-04-15T08:20:20Z)

I believe that I have found the solution to this in JobRouter context.
Use EVALSET, not SET !
i.e.

I should not use:
`SET DESIRED_SITES=strcat(DESIRED_SITES,",...")`
which replaces the DESIRED_SITES ad with a recursive expression,

but:
`EVALSET DESIRED_SITES=strcat(DESIRED_SITES,","...")`
which evaluates the RHS to a string using current value of the ad
and then sets the ad to the new string. See [ref](https://htcondor.readthedocs.io/en/latest/grid-computing/job-router.html#routing-mechanism)

After I changed JR table to
` EVALSET DESIRED_SITES strcat(DESIRED_SITES, "T2_US_Caltech,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin")`
I get
```console
[crabtw@vocms069 cluster1641599.proc0.subproc0]$ condor_q 1641602 -l|grep 'DESIRED_SITES ='
DESIRED_SITES = "T1_US_FNAL,T3_US_FNALLPCT2_US_Caltech,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin"
```

## Comment (belforte, 2026-04-15T13:42:13Z)

A look at `T1_FNAL + T3_FNALLPC` situation, list jobs in the whole pool right now which target both sites and are not MINI*. Using this command:
```text
 condor_q -global -con 'jobuniverse==5&&jobstatus==1&&cms_submissiontool=="CRAB"&&regexp("T1_US_FNAL",desired_sites)&&regexp("T3_US_FNALLPC",desired_sites)&&!regexp("MINIAOD",desired_cmsdataset)' -af desired_cmsdataset desired_sites |sort|uniq -c|sort -n
```
output
```
      1 /ScoutingPFRun3/Run2024G-v1/HLTSCOUT T1_DE_KIT,T1_ES_PIC,T1_FR_CCIN2P3,T1_IT_CNAF,T1_PL_NCBJ,T1_RU_JINR,T1_UK_RAL,T1_US_FNAL,T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CSCS,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FR_GRIF,T2_FR_IPHC,T2_HU_Budapest,T2_IN_TIFR,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_LB_HPC4L,T2_LV_HPCNET,T2_PL_Cyfronet,T2_PT_NCG_Lisbon,T2_RU_JINR,T2_TR_METU,T2_UA_KIPT,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_DOMA,T3_CN_Nanjing,T3_CN_THU,T3_ES_Oviedo,T3_HU_Debrecen,T3_IN_IOPB,T3_IT_Bologna,T3_IT_Perugia,T3_IT_Trieste,T3_KR_KNU,T3_MX_Cinvestav,T3_RU_MEPhI,T3_UK_London_RHUL,T3_UK_SGrid_Oxford,T3_UK_ScotGrid_GLA,T3_US_Baylor,T3_US_Colorado,T3_US_FIT,T3_US_FNALLPC,T3_US_FNALWILSON,T3_US_ORNL,T3_US_OSU,T3_US_PuertoRico,T3_US_Rice,T3_US_Rutgers,T3_US_UMD,T3_US_VC3_NotreDame
     11 /Muon1/Run2024I-PromptReco-v1/AOD T1_RU_JINR,T1_US_FNAL,T3_US_FNALLPC
     16 /Muon0/Run2024D-2024CDEReprocessing-v1/AOD T1_US_FNAL,T3_US_FNALLPC
     34 /Muon1/Run2024E-2024CDEReprocessing-v1/AOD T1_US_FNAL,T3_US_FNALLPC
    133 /STARLIGHT_5p36TeV_2024Run3/anstahll-coh_rho_direct_dipi_STARLIGHT_5p36TeV_2024Run3_RAW_2026_04_13-ad04e77d87f2d87530d63f9a51dd2920/USER T1_DE_KIT,T1_ES_PIC,T1_FR_CCIN2P3,T1_IT_CNAF,T1_PL_NCBJ,T1_RU_JINR,T1_UK_RAL,T1_US_FNAL,T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CSCS,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FR_GRIF,T2_FR_IPHC,T2_HU_Budapest,T2_IN_TIFR,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_LB_HPC4L,T2_LV_HPCNET,T2_PL_Cyfronet,T2_PT_NCG_Lisbon,T2_RU_JINR,T2_TR_METU,T2_UA_KIPT,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_DOMA,T3_CN_Nanjing,T3_CN_THU,T3_ES_Oviedo,T3_HU_Debrecen,T3_IN_IOPB,T3_IT_Bologna,T3_IT_Perugia,T3_IT_Trieste,T3_KR_KNU,T3_MX_Cinvestav,T3_RU_MEPhI,T3_UK_London_RHUL,T3_UK_SGrid_Oxford,T3_UK_ScotGrid_GLA,T3_US_Baylor,T3_US_Colorado,T3_US_FIT,T3_US_FNALLPC,T3_US_FNALWILSON,T3_US_ORNL,T3_US_OSU,T3_US_PuertoRico,T3_US_Rice,T3_US_Rutgers,T3_US_UMD,T3_US_VC3_NotreDame
    137 /Muon1/Run2024E-2024CDEReprocessing-v1/AOD T1_ES_PIC,T1_US_FNAL,T3_US_FNALLPC
    179 /Muon1/Run2025F-PromptJMENano-v1/NANOAOD T1_FR_CCIN2P3,T1_US_FNAL,T2_BR_SPRACE,T2_HU_Budapest,T2_RU_JINR,T2_UA_KIPT,T3_US_FNALLPC
    220 /Muon1/Run2024E-2024CDEReprocessing-v1/AOD T1_RU_JINR,T1_US_FNAL,T3_US_FNALLPC
    379 /Muon1/Run2024I-PromptReco-v1/AOD T1_US_FNAL,T3_US_FNALLPC
    870 /Muon1/Run2024H-PromptReco-v1/AOD T1_US_FNAL,T3_US_FNALLPC
   1000 /Cosmics/Commissioning2025-PromptReco-v2/AOD T1_US_FNAL,T3_US_FNALLPC
   1088 /Muon1/Run2024F-PromptReco-v1/AOD T1_US_FNAL,T3_US_FNALLPC
   1562 /ScoutingPFRun3/Run2024I-v1/HLTSCOUT T1_US_FNAL,T3_US_FNALLPC
belforte@vocms0198/~> 
```
given the above I am tempted to set the FNAL route to use 
```
 REQUIREMENTS  (DESIRED_SITES=="T1_US_FNAL,T3_FNAL_LPC")&&!regexp("MINI",DESIRED_CMSDATASET)
```

and maybe add `regexp("MINI",DESIRED_CMSDATASET)` to the MULTI_T1 route ?
Currently the only non-MINI targeted by CRAB jobs with two T1's in the list are these tiers:
```
condor_q -global -con 'jobuniverse==5&&jobstatus==1&&cms_submissiontool=="CRAB"&&regexp("T1_.*T1_.*",desired_sites)&&!regexp("MINIAOD",desired_cmsdataset)' -af desired_cmsdataset |cut -d'/' -f 4|sort|uniq -c|sort -n
      1 AODSIM
    147 NANOAOD
    373 AOD
   1493 RAW-RECO
```
The 'AOD' (non MINI) and RAW are almost all replicated at just JINR+another T1.

This suggest to use for the MULTI_T1 route:
 ```
 REQUIREMENTS (regexp("T1_.*T1_", DESIRED_SITES)&&!regex("NANO",desired_cmsdataset))
```

## Comment (belforte, 2026-04-15T16:52:28Z)

hmm... maybe not exactly, I want to avoid that US T2s are added twice, by the FNAL route and by the MULTI_T1 route. Having a site name repeated in the ad does not break matching (IIUC) but can confuse monitoring and us !
E.g. where do we want to handle these jobs ?


|`#`jobs|desired_cmsdataset|desired_sites|
|-- |-- | -- |
| 205 | /EGamma0/Run2026B-ZElectron-PromptReco-v1/RAW-RECO | T1_IT_CNAF,T1_US_FNAL,T3_US_FNALLPC |
| 87 | /EGamma1/Run2026B-ZElectron-PromptReco-v1/RAW-RECO | T1_FR_CCIN2P3,T1_IT_CNAF |

## Comment (belforte, 2026-04-17T15:29:42Z)

given the improved understanding of when FNALLPC is added to FNAL (comment at the top), I am leaning toward

* if `desired_sites=="T1_US_FNAL,T3_US_FNALLPC"` then add US T'2s
* if `desired_sites contains 2  or more T1's  and no T2's` then add T2's from the T1 countries

May leave some out (a MINI at one T1 and one T2), but should cover most and combined with 10% at T1's may be OK,

I do not see yet how to craft an HTC classAd contraint which selects "one T1 and one T2".

## Comment (belforte, 2026-04-17T16:37:44Z)

as usual, I asked for help at https://www-auth.cs.wisc.edu/lists/htcondor-users/2026-April/msg00040.shtml

## Comment (belforte, 2026-04-19T00:42:21Z)

I managed by asking Claude !
<details>
You're right, I apologize for the confusion. Let me provide a working solution.

The most reliable way to match exactly N occurrences is to explicitly ensure there are N occurrences AND no more:

## **Working pattern for exactly N occurrences:**

```perl
/^(?:(?!string).)*(?:string(?:(?!string).)*){N-1}string(?:(?!string).)*$/
```

But that's quite complex. Here's a **simpler and more practical approach**:

```perl
/^([^s]|s(?!tring))*string([^s]|s(?!tring))*string([^s]|s(?!tring))*string([^s]|s(?!tring))*$/
```

**However, the cleanest solution for exactly 3 occurrences of "ERROR":**

```perl
/^((?!ERROR).)*ERROR((?!ERROR).)*ERROR((?!ERROR).)*ERROR((?!ERROR).)*$/
```

### **Pattern explanation:**
- `((?!ERROR).)*` - Match any character that's NOT the start of "ERROR"
- `ERROR` - Match the literal string
- Repeat this pattern exactly N times
- The negative lookahead `(?!ERROR)` ensures we don't accidentally skip over occurrences

### **HTCondor example for exactly 3 "ERROR" strings:**
```
regexp("^((?!ERROR).)*ERROR((?!ERROR).)*ERROR((?!ERROR).)*ERROR((?!ERROR).)*$", LogMessage)
```

This should now correctly match only when there are exactly 3 occurrences of "ERROR".
</details>


@aspiringmind-code since you are a fan of regular expressions, you may find this interesting

Here's how asking for `T1.*T1.*` returns also jobs which taraget more than 2 Tier1's
```console
belforte@vocms0198/~> condor_q -con 'regexp("T1.*T1.*", desired_sites)' -af desired_sites|sort|uniq -c
   1098 T1_DE_KIT,T1_ES_PIC
     38 T1_DE_KIT,T1_ES_PIC,T1_FR_CCIN2P3,T1_IT_CNAF,T1_PL_NCBJ,T1_RU_JINR,T1_UK_RAL,T1_US_FNAL,T2_DE_DESY,T2_DE_RWTH,T2_ES_CIEMAT,T2_ES_IFCA,T2_FR_GRIF,T2_FR_IPHC,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin
     78 T1_DE_KIT,T1_FR_CCIN2P3
      4 T1_DE_KIT,T1_FR_CCIN2P3,T2_IT_Bari
      1 T1_DE_KIT,T1_FR_CCIN2P3,T2_US_Florida
      4 T1_DE_KIT,T1_RU_JINR,T1_UK_RAL,T1_US_FNAL,T2_BE_IIHE,T2_BE_UCL,T2_CN_Beijing,T2_DE_DESY,T2_DE_RWTH,T2_ES_CIEMAT,T2_FR_GRIF,T2_HU_Budapest,T2_KR_KISTI,T2_US_Florida,T2_US_Purdue,T2_US_Wisconsin,T3_KR_KNU,T3_US_FNALLPC,T3_US_Rutgers
    143 T1_DE_KIT,T1_US_FNAL,T2_BE_IIHE,T3_US_FNALLPC
    720 T1_DE_KIT,T1_US_FNAL,T3_US_FNALLPC
      4 T1_ES_PIC,T1_US_FNAL,T3_ES_PIC_BSC,T3_US_FNALLPC
      2 T1_ES_PIC,T1_US_FNAL,T3_US_FNALLPC
      2 T1_FR_CCIN2P3,T1_IT_CNAF,T2_US_Florida
      1 T1_FR_CCIN2P3,T1_IT_CNAF,T2_US_Vanderbilt
      4 T1_FR_CCIN2P3,T1_US_FNAL,T2_US_Caltech,T3_US_FNALLPC
   2053 T1_FR_CCIN2P3,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
   2576 T1_FR_CCIN2P3,T1_US_FNAL,T3_US_FNALLPC
    135 T1_IT_CNAF,T1_PL_NCBJ
    255 T1_IT_CNAF,T1_US_FNAL,T2_US_Vanderbilt,T2_US_Wisconsin,T3_US_FNALLPC
   1440 T1_IT_CNAF,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
   1003 T1_IT_CNAF,T1_US_FNAL,T3_US_FNALLPC
    926 T1_UK_RAL,T1_US_FNAL,T2_US_Vanderbilt,T2_US_Wisconsin,T3_US_FNALLPC
   3240 T1_UK_RAL,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
belforte@vocms0198/~> 
```
and here's how to ask for exactly two Tier1 using [negative lookahead  assertions](https://www.pcre.org/current/doc/html/pcre2pattern.html#SEC19) in the regexp . Note this from HTC doc:
... utilize regular expressions as defined and supported by the PCRE library. See http://www.pcre.org/ for complete documentation of regular expressions....

```console
belforte@vocms0198/~> condor_q -con 'regexp("^((*nla:T1).)*T1((*nla:T1).)*T1((*nla:T1).)*$", desired_sites)' -af desired_sites|sort|uniq -c
   1098 T1_DE_KIT,T1_ES_PIC
     78 T1_DE_KIT,T1_FR_CCIN2P3
      4 T1_DE_KIT,T1_FR_CCIN2P3,T2_IT_Bari
      1 T1_DE_KIT,T1_FR_CCIN2P3,T2_US_Florida
    143 T1_DE_KIT,T1_US_FNAL,T2_BE_IIHE,T3_US_FNALLPC
    720 T1_DE_KIT,T1_US_FNAL,T3_US_FNALLPC
      4 T1_ES_PIC,T1_US_FNAL,T3_ES_PIC_BSC,T3_US_FNALLPC
      2 T1_ES_PIC,T1_US_FNAL,T3_US_FNALLPC
      2 T1_FR_CCIN2P3,T1_IT_CNAF,T2_US_Florida
      1 T1_FR_CCIN2P3,T1_IT_CNAF,T2_US_Vanderbilt
      4 T1_FR_CCIN2P3,T1_US_FNAL,T2_US_Caltech,T3_US_FNALLPC
   2053 T1_FR_CCIN2P3,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
   2576 T1_FR_CCIN2P3,T1_US_FNAL,T3_US_FNALLPC
    135 T1_IT_CNAF,T1_PL_NCBJ
    255 T1_IT_CNAF,T1_US_FNAL,T2_US_Vanderbilt,T2_US_Wisconsin,T3_US_FNALLPC
   1440 T1_IT_CNAF,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
   1003 T1_IT_CNAF,T1_US_FNAL,T3_US_FNALLPC
    926 T1_UK_RAL,T1_US_FNAL,T2_US_Vanderbilt,T2_US_Wisconsin,T3_US_FNALLPC
   3240 T1_UK_RAL,T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC
belforte@vocms0198/~> 
```

## Comment (belforte, 2026-04-19T01:03:54Z)

and (again just on `vocms098`) here's the data tier for jobs which target execatly one T1 and one T2 
```console
belforte@vocms0198/~> condor_q -con 'regexp("^((*nla:T1).)*T1((*nla:T1).)*$", desired_sites)&&regexp("^((*nla:T2).)*T2((*nla:T2).)*$", desired_sites)' -af desired_sites 'split(desired_cmsdataset,"/")[2]'|sort|uniq -c|sort -n
      1 T1_DE_KIT,T2_US_MIT MINIAOD
      1 T1_FR_CCIN2P3,T2_US_Vanderbilt AOD
      1 T1_US_FNAL,T2_ES_CIEMAT,T3_US_FNALLPC MINIAODSIM
      3 T1_US_FNAL,T2_CH_CERN,T3_US_FNALLPC MINIAODSIM
      4 T1_IT_CNAF,T2_UK_London_IC,T3_UK_London_RHUL,T3_UK_SGrid_Oxford,T3_UK_ScotGrid_GLA MINIAOD
     11 T1_US_FNAL,T2_IT_Bari,T3_US_FNALLPC MINIAOD
     12 T1_US_FNAL,T2_ES_CIEMAT,T3_US_FNALLPC MINIAOD
     12 T1_US_FNAL,T2_US_Purdue,T3_US_FNALLPC MINIAODSIM
     14 T1_FR_CCIN2P3,T2_US_Florida MINIAOD
    178 T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC MINIAOD
    341 T1_IT_CNAF,T2_US_Vanderbilt MINIAOD
    576 T1_FR_CCIN2P3,T2_ES_CIEMAT MINIAOD
   1211 T1_FR_CCIN2P3,T2_US_Caltech MINIAOD
belforte@vocms0198/~> 
```
of course T1_US_FNAL always brings T3_US_FNALLPC, as discussed. The UK T3's thing is curious but it is the same thing, those T3's are defined as processing nodes for IC_London in [CRIC](https://cms-cric.cern.ch/cms/storageunit/detail/T2_UK_London_IC/)

## Comment (belforte, 2026-04-19T01:15:16Z)

full picture
```console
belforte@vocms0198/~> condor_q -g -con 'regexp("^((*nla:T1).)*T1((*nla:T1).)*$", desired_sites)&&regexp("^((*nla:T2).)*T2((*nla:T2).)*$", desired_sites)' -af desired_sites 'split(desired_cmsdataset,"/")[2]'|sort|uniq -c|sort -n > /tmp/t1t2
belforte@vocms0198/~> wc /tmp/t1t2
  88  265 4634 /tmp/t1t2
belforte@vocms0198/~> grep -c MINIAODSIM /tmp/t1t2
20
belforte@vocms0198/~> grep -c "MINIAOD$" /tmp/t1t2
57
belforte@vocms0198/~> grep -c " AOD$" /tmp/t1t2
6
belforte@vocms0198/~> grep -c -v "AOD" /tmp/t1t2
5
belforte@vocms0198/~> 
```
i.e. 88 different set of sites/dataset, 57 MINIAOD, 20 MINIAODSIM, 6 AOD and 5 other tiers (RTAW_RECO, HLTSCOUT)

Combinations wth more than 1K jobs:
```
   1058 T1_DE_KIT,T2_US_Vanderbilt MINIAOD
   1108 T1_FR_CCIN2P3,T2_US_MIT MINIAOD
   1225 T1_IT_CNAF,T2_US_Vanderbilt MINIAODSIM
   1258 T1_FR_CCIN2P3,T2_US_Florida MINIAOD
   1311 T1_UK_RAL,T2_US_Vanderbilt MINIAOD
   1328 T1_FR_CCIN2P3,T2_BR_SPRACE MINIAOD
   1350 T1_FR_CCIN2P3,T2_IT_Bari MINIAOD
   1358 T1_FR_CCIN2P3,T2_US_Wisconsin MINIAOD
   1445 T1_DE_KIT,T2_US_UCSD MINIAOD
   1546 T1_US_FNAL,T2_IT_Legnaro,T3_US_FNALLPC MINIAOD
   1565 T1_DE_KIT,T2_DE_DESY MINIAOD
   1652 T1_US_FNAL,T2_IT_Bari,T3_US_FNALLPC MINIAOD
   1743 T1_FR_CCIN2P3,T2_DE_DESY MINIAOD
   2067 T1_FR_CCIN2P3,T2_ES_CIEMAT MINIAOD
   2514 T1_US_FNAL,T2_UK_London_IC,T3_UK_London_RHUL,T3_UK_SGrid_Oxford,T3_UK_ScotGrid_GLA,T3_US_FNALLPC MINIAOD
   2515 T1_US_FNAL,T2_BE_UCL,T3_US_FNALLPC MINIAOD
   2743 T1_IT_CNAF,T2_US_Caltech MINIAOD
   3076 T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC MINIAOD
   3498 T1_US_FNAL,T2_BE_IIHE,T3_US_FNALLPC MINIAOD
   4221 T1_IT_CNAF,T2_US_Vanderbilt MINIAOD
   4282 T1_US_FNAL,T2_US_Vanderbilt,T3_US_FNALLPC MINIAOD
   6039 T1_FR_CCIN2P3,T2_US_Vanderbilt MINIAOD
   7467 T1_FR_CCIN2P3,T2_US_Caltech MINIAOD
```

## Comment (belforte, 2026-04-21T18:06:02Z)

the above is "too full", includes WMA as well. Restricing to CRAB
```
belforte@vocms0198/~> condor_q -g -con 'cms_submissiontool=="crab"&&jobuniverse==5&&regexp("^((*nla:T1).)*T1((*nla:T1).)*$", desired_sites)&&regexp("^((*nla:T2).)*T2((*nla:T2).)*$", desired_sites)' -af desired_sites desired_cmsdataset > /tmp/t1t2

belforte@vocms0198/~> cat /tmp/t1t2 |sort|uniq -c|sort -n|grep -c  "/AOD$"
13
belforte@vocms0198/~> cat /tmp/t1t2 |sort|uniq -c|sort -n|grep -c  "/AODSIM$"
0
belforte@vocms0198/~> cat /tmp/t1t2 |sort|uniq -c|sort -n|grep -c  "/MINIAODSIM$"
37
belforte@vocms0198/~> cat /tmp/t1t2 |sort|uniq -c|sort -n|grep -c  "/MINIAOD$"
114
belforte@vocms0198/~> 
```
And the NON-*AOD* are mostly RAW_RECO (for which the reason for a second site is not clear) and HLTSCOUT
```
belforte@vocms0198/~> cat /tmp/t1t2 |sort|uniq -c|sort -n|grep -v AOD
      1 T1_DE_KIT,T2_IT_Pisa /Muon0/Run2026C-ZMu-PromptReco-v1/RAW-RECO
      3 T1_DE_KIT,T2_PL_Cyfronet /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
      3 T1_DE_KIT,T2_PT_NCG_Lisbon /Muon0/Run2026C-ZMu-PromptReco-v1/RAW-RECO
      4 T1_DE_KIT,T2_US_MIT /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
      5 T1_DE_KIT,T2_UK_London_Brunel,T3_UK_London_QMUL /Muon1/Run2026B-ZMu-PromptReco-v1/RAW-RECO
     11 T1_DE_KIT,T2_AT_Vienna /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
     31 T1_DE_KIT,T2_FI_HIP /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
     59 T1_DE_KIT,T2_IT_Pisa /Muon1/Run2026B-ZMu-PromptReco-v1/RAW-RECO
     64 T1_DE_KIT,T2_PT_NCG_Lisbon /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
    102 T1_DE_KIT,T2_IT_Pisa /Muon0/Run2026B-ZMu-PromptReco-v1/RAW-RECO
    177 T1_UK_RAL,T2_HU_Budapest /EGamma3/Run2025G-EGMJME-PromptReco-v1/RAW-RECO
   4606 T1_DE_KIT,T2_US_Vanderbilt /ScoutingPFRun3/Run2024F-v1/HLTSCOUT
belforte@vocms0198/~> 
```

## Comment (belforte, 2026-04-30T15:25:42Z)

So I will add 3 routes
|desired_sites | change|
|- | -|
|T1_US_FNAL,T3_US_FNALLPC | add all US_T2's  (*) |
| two T1's (exclusive) and no T2 | add all T2's  (*) in same countries as those two T1's |
| one T1 and one T2 (exclusive)(**) | add al T2's (*) in same countries as the T1 |

(*) **Note:** T2_US_Vanderbilt is neved added 
(**) **Note:** this covers also cases like T1_US_FNAL, T2_X_Y, T3_US_FNALLPC

## Comment (belforte, 2026-04-30T15:50:54Z)

I have created a new `90_jobrouter.config` file with the new routes, tested it on vocms069` with ad-hoc crafted jobs,  and placed it in [dev branch](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/tree/dev?ref_type=heads) in our puppet repository. 

AP's which take configs from that branch, (i.e.  in `crabdev` foreman environment) are:  `crab-sched-903` (always there) and this two which I just added  `vocms069`  

Next:
- [x] run a few more tests on 069 using crab submit with various site lists
- [x] port change to `qa`
- [x] put one production AP in `qa` and watch - `vocms0198`

## Comment (belforte, 2026-05-04T16:49:22Z)

I let JobRouter make one round on vocms198, then stopped it.
It routed 736 jobs, which look OK.
* before
```[root@vocms0198 belforte]# condor_q -con HasBeenOverflowRouted -af desired_sites_orig|sort|uniq -c
    223 T1_DE_KIT,T1_US_FNAL,T3_US_FNALLPC
    277 T1_FR_CCIN2P3,T1_US_FNAL,T3_US_FNALLPC
    163 T1_IT_CNAF,T2_US_Vanderbilt
     64 T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC
      9 T1_US_FNAL,T2_ES_CIEMAT,T3_US_FNALLPC
```
* after
```
[root@vocms0198 belforte]# condor_q -con HasBeenOverflowRouted -af desired_sites|sort|uniq -c
    223 T1_DE_KIT,T1_US_FNAL,T3_US_FNALLPC,T2_DE_DESY,T2_DE_RWTH,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin
    277 T1_FR_CCIN2P3,T1_US_FNAL,T3_US_FNALLPC,T2_FR_GRIF,T2_FR_IPHC,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin
    163 T1_IT_CNAF,T2_US_Vanderbilt,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome
     64 T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin
      9 T1_US_FNAL,T2_ES_CIEMAT,T3_US_FNALLPC,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin
```

## Comment (belforte, 2026-05-04T17:37:56Z)

I  then restarted the JobRouter, it added 500 more jobs to the routes 
```
[root@vocms0198 belforte]# condor_q -con HasBeenOverflowRouted -af desired_sites_orig|sort|uniq -c
    482 T1_DE_KIT,T1_US_FNAL,T3_US_FNALLPC
    518 T1_FR_CCIN2P3,T1_US_FNAL,T3_US_FNALLPC
    163 T1_IT_CNAF,T2_US_Vanderbilt
     64 T1_US_FNAL,T2_DE_DESY,T3_US_FNALLPC
      9 T1_US_FNAL,T2_ES_CIEMAT,T3_US_FNALLPC
```

Overall count of routes matched
```
belforte@vocms0198/~> cat /var/log/condor/JobRouterLog|grep route=|cut -d= -f 3|cut -d')' -f1|sort|uniq -c
   2333 T1_DE_KIT
   1597 T1_ES_PIC
     19 T1_FR_CCIN2P3
   6089 T1_IT_CNAF
    236 T1_T2
   1000 TWO_T1
```

everything looks good !

## Comment (belforte, 2026-05-04T20:30:56Z)

THere is only one thing which is not fully satisfactory.
It appears that JR routes 500 job max per route at every iteration, but never pauses "because it has routed many" and keeps doing it every 5 min effectively routing all possible jobs in a short amount of time.
I have elaborated a bit on that in
https://mattermost.web.cern.ch/cms-o-and-c/pl/7jx1u8jczpd6tcxsak4if5a3uo

But I suspect that since we decide what to route based on `DESIRED_Sites` and change it in doing the route, routed jobs will simply not be counted anymore next time. If that's the case there's nothing that we can do.

OTOH, in this situation there is no point hurriedly routing everything in chunks of 500 every 5 min, better stick  with default (100) or even lower to 50 and reduce frequency to e.g. twice an hour. The idea is to give more time for jobs to run at sites in the original list (i.e. where data are) and only as "last resort" let them overflow. In this spirit I would also increase the required idle time from 20min to something like 4 hours.
I welcome criticism, comments, suggestions @aspiringmind-code @nausikt 

FOr the time being I keep https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/90_jobrouter.config?ref_type=heads enabled only in vocms0198, so we can check how it goes now that backlog is digested.

## Comment (belforte, 2026-05-04T21:49:56Z)

this is what got routed today,  selecting in JobRouterLog lines like
`05/04/26 18:42:03 JobRouter (src=142940583.0,route=T1_T2): Done editing job.`

```console
belforte@vocms0198/~> grep 05/04/26 /var/log/condor/JobRouterLog|grep route=|cut -d= -f 3|cut -d')' -f1|sort|uniq -c
    236 T1_T2
   2986 TWO_T1
belforte@vocms0198/~> 
```

## Comment (belforte, 2026-05-05T13:03:36Z)

so far so good.
a tentative dashboard to check on things is at https://monit-grafana.cern.ch/goto/3zRDe3TDR?orgId=11
here's a screenshot (only jobs from `vocms0198`)

<img width="1459" height="714" alt="Image" src="https://github.com/user-attachments/assets/a95ff305-99b2-4358-8d94-cc89acba678d" />

## Comment (belforte, 2026-05-05T15:05:14Z)

A different view, where I compare total jobs running  at a T1, CRAB jobs at that T1, and CRAB jobs running at local T2's and reading from that T1. I do not have a way to visualize production jobs running at T2's and reading from T1's

<img width="1449" height="701" alt="Image" src="https://github.com/user-attachments/assets/40cf646a-dfc6-4680-ad1b-6405a503feaa" />

## Comment (belforte, 2026-05-06T19:19:28Z)

Today I enabled also vocms0106 to use new routes. See https://its.cern.ch/jira/browse/CMSTRANSF-1323?focusedId=7334295&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-7334295 and other comments around that.

Here's what got routed there in last days
```
belforte@vocms0106/~> for i in 1 2 3 4 5 6; do echo 05/0$i/26; grep 05/0$i/26  /var/log/condor/JobRouterLog|grep route=|cut -d= -f 3|cut -d')' -f1|sort|uniq -c; done
05/01/26
05/02/26
   4833 T1_IT_CNAF
05/03/26
    120 T1_DE_KIT
    102 T1_ES_PIC
    138 T1_FR_CCIN2P3
     36 T1_IT_CNAF
     65 T1_UK_RAL
05/04/26
05/05/26
05/06/26
    232 T1_DE_KIT
   6055 T1_T2
    720 TWO_T1
belforte@vocms0106/~> 
```

## Comment (belforte, 2026-05-08T08:01:29Z)

so far so good. Thousand of jobs overflew but nobody complained (new routes were added to 0198 on May 4, to 0106 on May 6

<img width="1443" height="709" alt="Image" src="https://github.com/user-attachments/assets/471e41e6-3dad-46d9-a9b9-724cd744353b" />

## Comment (belforte, 2026-05-08T08:04:59Z)

I would like to investigate using HTCodor [concurrency limits](https://htcondor.readthedocs.io/en/latest/admin-manual/cm-configuration.html#concurrency-limits) to put a max on number of overflown jobs for each T1

## Comment (belforte, 2026-05-11T16:04:59Z)

I have asked @mmascher to add these to ITB negotiator so we can try things out
```
T1_DE_KIT_CRAB_OVERFLOW_LIMIT = 20
T1_ES_PIC_CRAB_OVERFLOW_LIMIT = 20
T1_FR_CCIN2P3_CRAB_OVERFLOW_LIMIT = 20
T1_IT_CNAF_CRAB_OVERFLOW_LIMIT = 20
T1_UK_RAL_CRAB_OVERFLOW_LIMIT = 20
T1_US_FNAL_CRAB_OVERFLOW_LIMIT = 20 
```

## Comment (drkovalskyi, 2026-05-12T05:14:41Z)

Isn't 20 too low for T1 site? CERN and FNAL are handling all production premixing. I think the limits should be in the order of 1k if not 10k.

## Comment (belforte, 2026-05-12T08:03:18Z)

thanks for being alert @drkovalskyi  !! Yes, I fully agree. Those limits at 20 are for the Integration Test Bed negotiator to make it easy for me to test with a few jobs and make sure we get syntax right and understand how it works. When we'll set limits in the global pool we'll be realistic (and get T1's to sign off).

## Comment (belforte, 2026-05-19T09:41:11Z)

monitoring [fixed](https://monit-grafana.cern.ch/goto/rQoE1i1DR?orgId=11) and concurrency limits work (thanks to @mmascher ), tested in ITB (on vocms069)
New routing table is now in dev branch https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/dev/code/files/crabschedd/90_jobrouter.config?ref_type=heads
also pasted below for easy reference.
The amount of concurrent resource (overflow from a specific T1) is set as
 - 2 when one T1 has the data
 - 1 when two T1's have the data, since jobs are more or less half as likely to hit either
That splitting of overflow accounting is of course imperfect, but I do not see a way to do better, consumption has to
be declared when job is submitted, but which resource is used is only known when the job is matched.

We should now set limits in global pool negotiator and then deploy new routes.

```text
# Configuration file for the JobRouter
# 

# Specifiy a global Requirements expression that must be true for all newly routed jobs,
# in addition to any Requirements specified within a routing table entry
#
JOB_ROUTER_SOURCE_JOB_CONSTRAINT =           ( \
    (JobUniverse==5) \
 && (jobstatus==1) \
 && (CRAB_UserHN != "sciaba") \
 && (HasBeenOverflowRouted is undefined) \
 && (CMS_ALLOW_OVERFLOW == "True") \
 && (time() - EnteredCurrentStatus > 3600) \
                                             )


# define a pre-route transform that does the transforms all routes should do
# After experimenting we found that EditJobInPlace and UNIVERSE directives
# do not work if places here. They need to be replicated inside each T1-specific route
#
JOB_ROUTER_PRE_ROUTE_TRANSFORM_NAMES = Defaults

JOB_ROUTER_TRANSFORM_Defaults @=jrd
  SET HasBeenOverflowRouted True
  EVALSET LastRouted time()
  EVALSET DESIRED_SITES_Orig = DESIRED_SITES
@jrd


# Static route names for each T1 (since they are exclusive
# order does not matter, use alphabetic here)
#
JOB_ROUTER_ROUTE_NAMES = T1_DE_KIT T1_ES_PIC T1_FR_CCIN2P3 T1_IT_CNAF T1_UK_RAL T1_US_FNAL TWO_T1 T1_T2

JOB_ROUTER_ROUTE_T1_DE_KIT @=rtkit
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_DE_KIT")
  SET DESIRED_SITES "T1_DE_KIT,T2_DE_DESY,T2_DE_RWTH"
  SET ConcurrencyLimits = "T1_DE_KIT_CRAB_OVERFLOW:2"
@rtkit

JOB_ROUTER_ROUTE_T1_ES_PIC @=rtpic
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_ES_PIC")
  SET DESIRED_SITES "T1_ES_PIC,T2_ES_CIEMAT,T2_ES_IFCA"
  SET ConcurrencyLimits = "T1_ES_PIC_CRAB_OVERFLOW:2"
@rtpic

JOB_ROUTER_ROUTE_T1_FR_CCIN2P3 @=rtin2p3
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_FR_CCIN2P3")
  SET DESIRED_SITES "T1_FR_CCIN2P3,T2_FR_GRIF,T2_FR_IPHC"
  SET ConcurrencyLimits = "T1_FR_CCIN2P3_CRAB_OVERFLOW:2"
@rtin2p3

JOB_ROUTER_ROUTE_T1_IT_CNAF @=rtcnaf
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_IT_CNAF")
  SET DESIRED_SITES "T1_IT_CNAF,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome"
  SET ConcurrencyLimits = "T1_IT_CNAF_CRAB_OVERFLOW:2"
@rtcnaf

JOB_ROUTER_ROUTE_T1_UK_RAL @=rtral
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_UK_RAL")
  SET DESIRED_SITES "T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_RALPP"
  SET ConcurrencyLimits = "T1_UK_RAL_CRAB_OVERFLOW:2"
@rtral

# in order to complete overflow for T1's, need a route for FNAL
# because all jobs matching it match also T3_US_FNALLPC and
# gideinWms group-based overflow in the US does not work for those
JOB_ROUTER_ROUTE_T1_US_FNAL @=rtfnal
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS  (DESIRED_SITES=="T1_US_FNAL,T3_US_FNALLPC")
  EVALSET DESIRED_SITES = join("," ,{DESIRED_SITES, "T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin"})
  SET ConcurrencyLimits = "T1_US_FNAL_CRAB_OVERFLOW:2"
@rtfnal

# then two routes to help jobs which access MINI* which often have
# two replicas but one of them is very likely a T1
#
# a route for jobs which target exactly two T1's (and no T2)
# see https://github.com/dmwm/CRABServer/issues/9295 for nla: (negative lookahead asserion)
JOB_ROUTER_ROUTE_TWO_T1 @=twot1
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS regexp("^((*nla:T1).)*T1((*nla:T1).)*T1((*nla:T1).)*$",DESIRED_SITES)&&!regexp(".*T2.*",DESIRED_SITES)

  EVALSET DESIRED_SITES = strcat( DESIRED_SITES, \
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), ",T2_DE_DESY,T2_DE_RWTH", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), ",T2_ES_CIEMAT,T2_ES_IFCA", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), ",T2_FR_GRIF,T2_FR_IPHC", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), ",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), ",T2_UK_London_IC,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), ",T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin", "") \
)
  EVALSET  ConcurrencyLimits = strcat( \ 
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), "T1_DE_KIT_CRAB_OVERFLOW:1,", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), "T1_ES_PIC_CRAB_OVERFLOW:1,", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), "T1_FR_CCIN2P3_CRAB_OVERFLOW:1,", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), "T1_IT_CNAF_CRAB_OVERFLOW:1,", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), "T1_UK_RAL_CRAB_OVERFLOW:1,", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), "T1_US_FNAL_CRAB_OVERFLOW:1", "") \
)
@twot1

# and a route for jobs which target exactly one T1 and one T2
JOB_ROUTER_ROUTE_T1_T2 @=t1t2
  MaxJobs = 1000
  MaxIdleJobs = 500
  EditJobInPlace = True
  UNIVERSE 5
  REQUIREMENTS regexp("^((*nla:T1).)*T1((*nla:T1).)*$",DESIRED_SITES)&&regexp("^((*nla:T2).)*T2((*nla:T2).)*$",DESIRED_SITES)

  EVALSET DESIRED_SITES = strcat( DESIRED_SITES, \
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), ",T2_DE_DESY,T2_DE_RWTH", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), ",T2_ES_CIEMAT,T2_ES_IFCA", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), ",T2_FR_GRIF,T2_FR_IPHC", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), ",T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), ",T2_UK_London_IC,T2_UK_SGrid_RALPP,T2_UK_London_Brunel", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), ",T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Wisconsin", "") \
)
 EVALSET  ConcurrencyLimits = strcat( \
  ifThenElse(regexp("T1_DE_", DESIRED_SITES), "T1_DE_KIT_CRAB_OVERFLOW:2", ""), \
  ifThenElse(regexp("T1_ES_", DESIRED_SITES), "T1_ES_PIC_CRAB_OVERFLOW:2", ""), \
  ifThenElse(regexp("T1_FR_", DESIRED_SITES), "T1_FR_CCIN2P3_CRAB_OVERFLOW:2", ""), \
  ifThenElse(regexp("T1_IT_", DESIRED_SITES), "T1_IT_CNAF_CRAB_OVERFLOW:2", ""), \
  ifThenElse(regexp("T1_UK_", DESIRED_SITES), "T1_UK_RAL_CRAB_OVERFLOW:2", ""), \
  ifThenElse(regexp("T1_US_", DESIRED_SITES), "T1_US_FNAL_CRAB_OVERFLOW:2", "") \
)
@t1t2

# How often to poll the job queue to route jobs
#
JOB_ROUTER_POLLING_PERIOD = 10*60

# Start the Job Router
# Reminder: you must restart HTCondor for changes to DAEMON_LIST to take effect.
# e.g. condor_off -daemon job_router; condor_on -daemon job_router
#
DAEMON_LIST = $(DAEMON_LIST) JOB_ROUTER
```

## Comment (belforte, 2026-06-29T12:51:18Z)

The new route is now in operation in all CRAB AP's wich concurrency limits set in the negotiator to limit at 1K overflow jobs per T1. Everything is working nicely.
