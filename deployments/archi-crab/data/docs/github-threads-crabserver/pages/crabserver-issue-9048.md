# dmwm/CRABServer issue #9048: correctly report DAG status for automatic splitting

State: closed
Opened: 2025-04-15T15:24:52Z
Closed: 2025-04-24T08:21:44Z
Labels: Type: Bug, Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9048

## Opening post (belforte, 2025-04-15T15:24:52Z)

current code is "tentative" and was not verified on largish automatic splitting tasks with subtasks

## Comment (belforte, 2025-04-16T20:33:34Z)

i made one test and DAG Status in DB was COMPLETED while processing dag was still runngin. Of course "now" jobs completed and things are consistent. I need to catch it in the act (hold the dagman ?) to find what was going on. Most likelt status parsing stops at first dag (the probe jobs) w/o checking the various subdags.

## Comment (belforte, 2025-04-17T08:41:26Z)

indeed:
https://github.com/dmwm/CRABServer/blob/d41808afcb7b0ed687aeaef508227c0b5e693cf1/scripts/task_process/cache_status_new.py#L536-L537

## Comment (belforte, 2025-04-17T08:53:43Z)

example of an automatic split task where the main dag, which contains the probes, has completed, and the processing dag is running
```console
belforte@vocms0199/~> condor_q -con jobuniverse==7\&\&crab_reqname==\"250417_071512:sewuchte_crab_XtoHH_MX_1000To4000_PU200\"


-- Schedd: crab3@vocms0199.cern.ch : <188.184.116.22:4080?... @ 04/17/25 10:51:58
 ID          OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD
81549101.0   crabtw          4/17 09:16   0+00:00:00 C  10   0.0 dag_bootstrap_startup.sh RunJobs.d
81553146.0   crabtw          4/17 09:52   0+00:59:20 R  10   0.7 condor_dagman -p 0 -f -l . -Lockfi

Total for query: 0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended 
Total for all users: 36701 jobs; 3210 completed, 7479 removed, 22344 idle, 3668 running, 0 held, 0 suspended

belforte@vocms0199/~>  condor_q 81553146.0 -af cmd
/bin/condor_dagman
belforte@vocms0199/~> condor_q 81553146.0 -af arguments
-p 0 -f -l . -Lockfile RunJobs0.subdag.lock -Dag RunJobs0.subdag -MaxIdle 1000 -MaxPre 20 -MaxPost 10 -DoRecov -CsdVersion $CondorVersion:' '24.0.6' '2025-03-05' 'BuildID:' '790851' 'PackageID:' '24.0.6-1' '$ -dagman /bin/condor_dagman -AutoRescue 0 -DoRescueFrom 0
belforte@vocms0199/~> 
```

## Comment (belforte, 2025-04-17T10:49:32Z)

I walked new `cache_status.py` with `pdb` through the automatic splitting task above and I found that it would correctly report status as RUNNING to DB.

Once current transition is over, I think we can remove the lines 536-537 as per https://github.com/dmwm/CRABServer/issues/9048#issuecomment-2812197458., put in canary and see how it goes.
