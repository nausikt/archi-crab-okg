# dmwm/CRABServer issue #8353: use consistent policies for cleaning up WEB_DIR and SPOOL_DIR

State: closed
Opened: 2024-04-24T17:03:25Z
Closed: 2024-04-26T16:37:29Z
Labels: Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8353

## Opening post (belforte, 2024-04-24T17:03:25Z)

#### WEB_DIR:
in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/cleanup_home_grid.sh?ref_type=heads
we remove directories last changed  60 days ago or more
```
find /home/grid -maxdepth 2 -mindepth 2 -type d -ctime +60 > /tmp/oldtasks
```
#### SPOOL_DIR
in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/clean_condor_spool_dir.sh?ref_type=heads
we remove 14 days after task is over
By the way, we do not cleanup HC after 7 days since now it runs with owner `crabtw` like everything else, need to filter on e.g. `crab_userhn` or (better) on `CRAB_UserRole = "production"`
```bash

echo --- SPOOL DIR clean up
echo ----- HC files clean up
condor_q -all -const 'TaskType=?="ROOT" && Owner=?="cmsprd" && (time() - EnteredCurrentStatus > 7 * 86400)' -af Iwd | xargs rm -rfv
echo ---
echo "--- Clean up finished tasks or hold tasks if their status did not changed last 14d."

condor_q -all -const 'TaskType=?="ROOT" && (JobStatus=?=4 || JobStatus=?=5) && (time() - EnteredCurrentStatus > 14 * 86400)' -af Iwd | xargs rm -rfv
```

## Comment (belforte, 2024-04-24T17:04:37Z)

best IMHO is to have  only one script, only one test, and when remove SPOOL_DIR, remove WEB_DIR too

## Comment (belforte, 2024-04-24T21:33:44Z)

this is somehow urgent since we are close to critical in vocms0195 and doing bad overall
```
vocms0106 :  /dev/vdb       1008G  691G  267G  73% /home/grid
vocms0107 :  /dev/vdb       1008G  623G  335G  66% /home/grid
vocms0119 :  /dev/vdb       1008G  562G  395G  59% /home/grid
vocms0120 :  /dev/vdb       1008G  693G  265G  73% /home/grid
vocms0121 :  /dev/vdb       1008G  654G  304G  69% /home/grid
vocms0122 :  /dev/vdb       1008G  602G  356G  63% /home/grid
vocms0137 :  /dev/vdb       1008G  650G  308G  68% /home/grid
vocms0144 :  /dev/vdb       1008G  640G  318G  67% /home/grid
vocms0155 :  /dev/vdb       1008G  665G  292G  70% /home/grid
vocms0194 :  /dev/vdb       1008G  647G  310G  68% /home/grid
vocms0195 :  /dev/vdb       1008G  768G  190G  81% /home/grid
vocms0196 :  /dev/vdb       1008G  658G  300G  69% /home/grid
vocms0197 :  /dev/vdb       1008G  694G  263G  73% /home/grid
vocms0198 :  /dev/vdb       1008G  698G  260G  73% /home/grid
vocms0199 :  /dev/vdb       1008G  669G  288G  70% /home/grid
```

## Comment (belforte, 2024-04-26T15:41:56Z)

hmm... I got it all wrong !!!

## Comment (belforte, 2024-04-26T15:58:02Z)

the way things work is:
1. JobCleanup.py takes care of task end-of-life removing them from the queue and deleting spool and web dirs
2. The purpose of `cleanup_home_grid.sh` is unclear, possibly was put there to catch anything that slipped through, that's why it uses a safe 60d threshold
3. The purpose of `clean_condor_spool_dir.sh` is similarly unclear. It removes SPOOL_DIR very soon (two weeks afer task completed) and maybe it was put/kept there to take care of early cleanup of HammerCloud, which is fine, but should not be mixed

So I'd rather say that:
* HammerCloud nees to removed earlier, best would be to set an earlier `CRAB_TaskEndTime` classAd when we submit them
 and make no changes to `JobCleanup.py`. We can do some emergency cleanup by hand in the meanwhile.
* The reason to keep SPOOL_DIR around is to allow resubmission of failed tasks which are in HOLD status. It would make sense to remove e.g. job and postjob logs, but files needed for resubmission must be kept.

OTOH I am puzzled that we do not see problems because of early disappearance of SPOOL_DIR. Something more to understand?

## Comment (belforte, 2024-04-26T16:07:09Z)

In a way I am remembering, re-discovering, re-proposing the "old" plan from https://github.com/dmwm/CRABServer/issues/4681#issuecomment-302336451
!!

What I do not see is how `clean_condor_spool_dir.sh` came about

## Comment (belforte, 2024-04-26T16:30:36Z)

I was **REALLY** wrong. There is no crontab running the obsolete `clean_condor_spool_dir.sh` which was superseded by `JobCleanup.py`.

Yet I found WEB_DIRs with logs in it and symlink pointing to removed spool directories !
And `/var/log/crab/JobCleanup.log` only has lines about spool dir being removed, not home dir
<details><summary>Example</summary>

belforte@vocms0195/crab> head -20 JobCleanup.log 
2024-04-17 18:10:01,600:INFO:JobCleanup,162:-----------------------------------
2024-04-17 18:10:01,601:INFO:JobCleanup,163:JoubCleaner.py has been started at: 2024-04-17 18:10:01.601133, by username: root
2024-04-17 18:10:01,912:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/3401/0/cluster99863401.proc0.subproc0
2024-04-17 18:10:05,096:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/3790/0/cluster99863790.proc0.subproc0
2024-04-17 18:10:07,550:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/3468/0/cluster99863468.proc0.subproc0
2024-04-17 18:10:09,609:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/2439/0/cluster99862439.proc0.subproc0
2024-04-17 18:10:10,665:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/3442/0/cluster99863442.proc0.subproc0
2024-04-17 18:10:11,441:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/2441/0/cluster99862441.proc0.subproc0
2024-04-17 18:10:15,126:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/4966/0/cluster99864966.proc0.subproc0
2024-04-17 18:10:27,795:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/214/0/cluster99860214.proc0.subproc0
2024-04-17 18:10:29,636:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/3485/0/cluster99863485.proc0.subproc0
2024-04-17 18:10:30,331:INFO:JobCleanup,91:List of ClusterIds to be cleared from the queue: ['99863401.0', '99863790.0', '99863468.0', '99862439.0', '99863442.0', '99862441.0', '99864966.0', '99860214.0', '99863485.0']
2024-04-18 00:10:01,775:INFO:JobCleanup,162:-----------------------------------
2024-04-18 00:10:01,775:INFO:JobCleanup,163:JoubCleaner.py has been started at: 2024-04-18 00:10:01.775329, by username: root
2024-04-18 00:10:02,075:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/1619/0/cluster99871619.proc0.subproc0
2024-04-18 00:10:02,958:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/7830/0/cluster99877830.proc0.subproc0
2024-04-18 00:10:03,817:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/263/0/cluster99870263.proc0.subproc0
2024-04-18 00:10:06,665:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/102/0/cluster99870102.proc0.subproc0
2024-04-18 00:10:07,157:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/9294/0/cluster99869294.proc0.subproc0
2024-04-18 00:10:08,233:INFO:JobCleanup,81:Deleting spoolDir: /etc/condor/condor_local/spool/9650/0/cluster99869650.proc0.subproc0

</details>

## Comment (belforte, 2024-04-26T16:36:32Z)

OK, Finally I found it in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/JobCleanup.py?ref_type=heads#L56
```python
    homeDir="/home/grid/%s/%s"%(crabDag.task["Owner"], crabDag.task["Crab_ReqName"])
```
Now all tasks run with `Owner = crabtw` !! So that variable always points to non-existing directory names and all WEB_DIRs are only catched by the fall-back `cleanup_home_dir.sh` after 60 days.

Need to change to

```python
    homeDir="/home/grid/%s/%s"%(crabDag.task["CRAB_UserHN"], crabDag.task["Crab_ReqName"])
```

## Comment (belforte, 2024-04-26T16:37:29Z)

I better close this and open an ad-hoc issue w/o all the noise
