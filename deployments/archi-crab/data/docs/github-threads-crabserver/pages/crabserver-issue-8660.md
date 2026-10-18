# dmwm/CRABServer issue #8660: test JobRouter on HTC 23.9

State: closed
Opened: 2024-08-28T09:44:02Z
Closed: 2024-09-01T16:59:55Z
Labels: Status: Done, Area: HTCondor, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8660

## Opening post (belforte, 2024-08-28T09:44:02Z)

needs to set config. param 
[JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES](https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES) to True

see
https://htcondor.readthedocs.io/en/latest/version-history/feature-versions-23-x.html#version-23-9-6

## Comment (belforte, 2024-08-28T15:01:48Z)

since update do 23.8 was [failing](https://github.com/dmwm/CRABServer/issues/8572#issuecomment-2256774150) due to HTC bug fixed in 23.9, I have tried to move `crab-sched-901` to 23.9.6
But it did not work, with a "never seen before" error

I have asked in SI MatterMost...let's see 
https://mattermost.web.cern.ch/cms-o-and-c/pl/4nmxj6z33i8dzj4p84nry4bmkw

## Comment (belforte, 2024-08-28T15:07:37Z)

I also wrote to Madison
https://lists.cs.wisc.edu/archive/htcondor-users/2024-August/msg00115.shtml

## Comment (belforte, 2024-08-29T09:52:42Z)

Probelm with update fixed by Florian, adding the `condor-upgrade-check` package to the htcondor module in puppet
https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/commit/f527fde555ec574ff6acd4e34e558251e6c8bc51
```text
[root@crab-sched-901 ~]# condor_version
$CondorVersion: 23.9.6 2024-08-08 BuildID: 748275 PackageID: 23.9.6-1 GitSHA: dfdd9eaa $
$CondorPlatform: x86_64_AlmaLinux9 $
[root@crab-sched-901 ~]# 
```

## Comment (belforte, 2024-09-01T16:15:05Z)

I tested this JobRouter on crab-sched-901 and indeed `/var/log/condor/JobRouterLog` went from
```text
09/01/24 17:50:28 Following source schedd (SCHEDD1): /etc/condor/condor_local/spool/job_queue.log
09/01/24 17:50:28 Destination schedd (SCHEDD2) not configured, using source schedd as destintation also
09/01/24 17:50:28 JobRouter WARNING: JOB_ROUTER_ENTRIES_CMD are deprecated and will be removed for V24 of HTCondor. New configuration
09/01/24 17:50:28                    syntax for the job router is defined using JOB_ROUTER_ROUTE_NAMES and JOB_ROUTER_ROUTE_<name>.
09/01/24 17:50:28              Note: The removal will occur during the lifetime of the HTCondor V23 feature series.
09/01/24 17:50:28 JobRouter WARNING: one or more of JOB_ROUTER_ENTRIES, JOB_ROUTER_ENTRIES_FILE or JOB_ROUTER_ENTRIES_CMD are defined but will be ignored because JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES is false
09/01/24 17:50:28 JobRouter WARNING: none of JOB_ROUTER_ROUTE_NAMES, JOB_ROUTER_ENTRIES, JOB_ROUTER_ENTRIES_FILE, or JOB_ROUTER_ENTRIES_CMD are defined, so job routing will not take place.

```
to
```text
09/01/24 18:11:06 Routes will be matched in hashtable order because JOB_ROUTER_ROUTE_NAMES was not configured.
09/01/24 18:11:06 JobRouter: Checking for candidate jobs. routing table is:
Route Name               Source      Submitted/Max        Idle/Max     Throttle Recent: Started Succeeded Failed
09/01/24 18:11:06 SECMAN: FAILED: Received "DENIED" from server for user crabschedd_crab-sched-901@cern.ch using method IDTOKENS.
09/01/24 18:11:06 ERROR: SECMAN:2010:Received "DENIED" from server for user crabschedd_crab-sched-901@cern.ch using method IDTOKENS.
09/01/24 18:11:06 Failed to send update to collector vocms4100.cern.ch:9620.
09/01/24 18:11:06 Will avoid querying collector vocms4100.cern.ch:9620 <[2001:1458:301:47::100:12]:9620?alias=vocms4100.cern.ch> for 1s if an alternative succeeds.
09/01/24 18:11:07 SECMAN: FAILED: Received "DENIED" from server for user crabschedd_crab-sched-901@cern.ch using method IDTOKENS.
09/01/24 18:11:07 ERROR: SECMAN:2010:Received "DENIED" from server for user crabschedd_crab-sched-901@cern.ch using method IDTOKENS.
09/01/24 18:11:07 Failed to send update to collector cmssrvz02.fnal.gov:9620.
09/01/24 18:11:07 Will avoid querying collector cmssrvz02.fnal.gov:9620 <[2620:6a:0:8421::cc]:9620?alias=cmssrvz02.fnal.gov> for 74s if an alternative succeeds.
```

which is same as for schdulers running 23.0.8 l

```text 
09/01/24 18:09:03 SECMAN: FAILED: Received "DENIED" from server for user crabschedd_vocms0194@cern.ch using method IDTOKENS.
09/01/24 18:09:03 ERROR: SECMAN:2010:Received "DENIED" from server for user crabschedd_vocms0194@cern.ch using method IDTOKENS.
09/01/24 18:09:03 Failed to send update to collector vocms4100.cern.ch:9620.
09/01/24 18:09:03 Will avoid querying collector vocms4100.cern.ch:9620 <[2001:1458:301:47::100:12]:9620?alias=vocms4100.cern.ch> for 2s if an alternative succeeds.
09/01/24 18:09:04 SECMAN: FAILED: Received "DENIED" from server for user crabschedd_vocms0194@cern.ch using method IDTOKENS.
09/01/24 18:09:04 ERROR: SECMAN:2010:Received "DENIED" from server for user crabschedd_vocms0194@cern.ch using method IDTOKENS.
09/01/24 18:09:04 Failed to send update to collector cmssrvz02.fnal.gov:9620.
09/01/24 18:09:04 Will avoid querying collector cmssrvz02.fnal.gov:9620 <[2620:6a:0:8421::cc]:9620?alias=cmssrvz02.fnal.gov> for 77s if an alternative succeeds.
09/01/24 18:09:10 Following source schedd (SCHEDD1): /etc/condor/condor_local/spool/job_queue.log
09/01/24 18:09:10 Destination schedd (SCHEDD2) not configured, using source schedd as destintation also
09/01/24 18:09:10 JobRouter WARNING: JOB_ROUTER_ENTRIES_CMD are deprecated and will be removed for V24 of HTCondor. New configuration
09/01/24 18:09:10                    syntax for the job router is defined using JOB_ROUTER_ROUTE_NAMES and JOB_ROUTER_ROUTE_<name>.
09/01/24 18:09:10              Note: The removal will occur during the lifetime of the HTCondor V23 feature series.
09/01/24 18:09:12 Routes will be matched in hashtable order because JOB_ROUTER_ROUTE_NAMES was not configured.
09/01/24 18:09:12 JobRouter: Checking for candidate jobs. routing table is:
Route Name               Source      Submitted/Max        Idle/Max     Throttle Recent: Started Succeeded Failed
belforte@vocms0194/~> 
```

## Comment (belforte, 2024-09-01T16:47:09Z)

I submitted 1K jobs targeting T1_UK_RAL, and things work as expected:
```text
[root@crab-sched-901 crab]# tail -20  JobAutoTuner.log 
2024-09-01 18:26:06,686:INFO:JobAutoTuner,107:=================== An Overflow object instance start! ===================
2024-09-01 18:26:06,734:INFO:JobAutoTuner,272:=========================================================================
2024-09-01 18:41:06,272:INFO:JobAutoTuner,260:============  JobAutoTuner-py3 starting ==============
2024-09-01 18:41:06,272:INFO:JobAutoTuner,263:-------------------- Routes added by Overflow.py  --------------------
2024-09-01 18:41:06,272:INFO:JobAutoTuner,107:=================== An Overflow object instance start! ===================
2024-09-01 18:41:06,310:INFO:JobAutoTuner,167:A new Route has been added:  
    [
        Name = "Overflow: 240901_162000:belforte_crab_20240901_181954"; 
        Requirements = ((target.Crab_ReqName == "240901_162000:belforte_crab_20240901_181954") && (HasBeenOverflowRouted is undefined)); 
        set_RouteType = "overflow"; 
        EditJobInPlace = true; 
        TargetUniverse = 5; 
        set_DESIRED_SITES = "T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP"; 
        eval_set_LastRouted = time(); 
        OverrideRoutingEntry = true; 
        set_DESIRED_SITES_Diff = "T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP"; 
        set_DESIRED_SITES_Orig = "T1_UK_RAL"; 
        set_HasBeenOverflowRouted = true
    ]
2024-09-01 18:41:06,341:INFO:JobAutoTuner,272:=========================================================================
```

condor is editing them a bit at a time
```
[root@crab-sched-901 crab]# condor_q -con 'crab_reqname=="240901_162000:belforte_crab_20240901_181954"' -af desired_sites|sort|uniq -c
    900 T1_UK_RAL
    100 T1_UK_RAL,T2_UK_London_Brunel,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP
      2 undefined
[root@crab-sched-901 crab]# 
```

## Comment (belforte, 2024-09-01T16:57:50Z)

everyting is fine

## Comment (belforte, 2024-09-01T16:59:55Z)

adding 
```
JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES = True
```
to file `/etc/condor/config` works as expected

## Comment (belforte, 2024-09-02T08:33:24Z)

here's Grafana showing how those 1K jobs have been re-routed
![image](https://github.com/user-attachments/assets/2e2c1605-70ee-44dc-8b3f-fba49e6a4bc3)
