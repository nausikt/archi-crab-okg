# dmwm/CRABServer issue #8651: schedulers - implement automatic reboot

State: open
Opened: 2024-08-26T15:18:18Z
Labels: Type: Enhancement, Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8651

## Opening post (mapellidario, 2024-08-26T15:18:18Z)

## intro

We want to automatically reboot all crab schedulers at least once a year.

## prerequisite

We should figure out how to be nice to HammerCloud on schedd restart if we want to automatically reboot our schedds: https://github.com/dmwm/CRABServer/issues/7410

## implementation

We had a brainstorming session in udine and so far the simplest thing that we could think of is

- move the list of enabled schedds that TW should use from gitlab to puppet.
- every schedd in the list should have a new parameter alongside the current "enabled: 0/1", and it should be the desired date of schedd reboot. make sure that there is no overlap in these dates! If you want to be fancy, you could also have a list of dates, in order to accommodate for multiple reboots per year.
- TW reads the configuration and if the "(current time - reboot time) < 1week", then TW should stop using that schedd
- add a daily cronjob to the schedd. if the "(current time - reboot time) < 2d" (using 2 days with a daily cronjob should avoid negative results, maybe they can be a problem in a bash script) then reboot the schedd. the reboot procedure should be
    - hold all the running dagmans, specifying "schedd reboot" as hold reason
    - condor_off
    - reboot
    - (condor_on should be automatic)
    - add a systemctl service unit, systemctl timer, hourly cronjob, whatever system you like, that releases all the hold dagmans that match the "schedd reboot" hold reason

## Comment (belforte, 2024-08-26T17:02:36Z)

spam/fishingh/trojan... is  coming here too :-(  Is there something that we can do ?

## Comment (belforte, 2024-08-26T17:05:34Z)

I used github "report" option. But would be better if we could prevent

## Comment (belforte, 2024-08-26T18:55:12Z)

@aspiringmind-code  @novicecpp  @mapellidario  not so bad. This is from GH. 
```
Our review of the account(s) and/or content named in your report has concluded. We have determined that one or more violations of GitHub’s Terms of Service have occurred and have taken appropriate action in response.
```

## Comment (belforte, 2026-02-11T09:24:19Z)

couple of notes from #8879 

We can do via a crontab (in puppet) which stops submissions to Vanilla pool, holds al jobs, wa and reboots. Ned to syncronize with TW putting in drain the weel before. Proposal: have hiera variable with list of reboot dates placed in TW config and parsed by TW code and placed in scheduler disk and parsed by crontab.
