# dmwm/CRABServer issue #8351: investigate running more than 200 tasks on one scheduler

State: closed
Opened: 2024-04-24T10:18:45Z
Closed: 2026-04-13T10:29:30Z
Labels: Type: Enhancement, Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8351

## Opening post (belforte, 2024-04-24T10:18:45Z)

* it is an old limit, current hardware may support more
* as far as Stefano knows, it is controlled by this in `/etc/condor/config.d/82_cms_schedd_crabschedd_generic.config`
```
START_SCHEDULER_UNIVERSE = (TotalSchedulerJobsRunning < 200) && ((ShadowsRunning is undefined) || (ShadowsRunning < .95*$(MAX_JOBS_RUNNING)))
```
* Stefano tried, and failed, to increase by adding a modified `START_SCHEDULER_UNIVERSE` in `/etc/condor/config.d/99_local_tweaks.config` with
```
START_SCHEDULER_UNIVERSE = (TotalSchedulerJobsRunning < 250) && ((ShadowsRunning is undefined) || (ShadowsRunning < .95*$(MAX_JOBS_RUNNING)))
```

TO DO
- [x] find why adding to `99_local_tweaks` failed even after schedd stop/start given that
 ```
belforte@vocms0106/config.d> condor_config_val START_SCHEDULER_UNIVERSE
(TotalSchedulerJobsRunning < 250) && ((ShadowsRunning is undefined) || (ShadowsRunning < .95*15000))
```

- [x] missing that. Try by editing directly `82_cms_schedd_crabschedd_generic`
- [x] overload one production scheduler with real work and see if we can push further

- [x] decide on new policy if any, knowing that
   * a larger limit may give more flexibility to deal with short-lived crisis
   *having too many tasks active at same time will make them run slower as they compete for CPU

## Comment (aspiringmind-code, 2026-01-19T09:13:04Z)

The trick was to change MAX_RUNNING_SCHEDULER_JOBS_PER_OWNER as well, as suggested by Marco.
vocms0120 was overloaded and the limit set to 250 was hit on 19/11/2025.
Policy can be changed going forward if need arises. For now, 200 limit is ok.

## Comment (belforte, 2026-01-19T10:06:13Z)

Well... we know how to increase the limit now, but have no data to tell us if we can run with a higher limit or not. Still need to "overload one production scheduler with real work and see if we can push further", when we tried Nov/Dec 2025 we had to stop due to full spool disk, but do not know for certain if the disk overuse was due to too many tasks vs. too many tasks in a short time or whether we may have problems with memory or I/O. Which makes this more challenging than a simple policy change.

## Comment (belforte, 2026-04-13T10:46:25Z)

thanks for closing @aspiringmind-code , but wouldn't it be better to close with a summary of the investigation ? Can we run more than 200 tasks, or not ?

## Comment (aspiringmind-code, 2026-04-13T13:03:00Z)

@belforte Oops clicked close issue instead of close with comment.
We tried to increase max-running-dagmans to 250 and run the VM "continuously", but it looks like that we hit I/O limits on condor spool disk.  The sched vocms0197 was suffering from high load and condor daemon had been (automatically) restarting with frequent scheduler crashes and loss of corresponding monitoring.
Best to stick to 200 limit.
