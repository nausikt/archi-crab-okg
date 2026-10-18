# dmwm/CRABServer issue #9031: tasks were submitted even schedulers already saturated.

State: open
Opened: 2025-04-03T13:06:59Z
URL: https://github.com/dmwm/CRABServer/issues/9031

## Opening post (nausikt, 2025-04-03T13:06:59Z)

When schedds were saturated, somehow tasks still submitted there thus created number of idle tasks as we can see [here](
https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&from=1743588054945&to=1743649757699&viewPanel=115)

ref: https://cms-talk.web.cern.ch/t/tasks-with-submitfailed-or-stuck-after-being-submitted/121750

Stefano:
- even we've functionality of "do not submit if all schedd's are saturated" why it's happened in this case.
- we should have user requests queue in the DB and enforce fair share scheduling.

Example Task that try to submitted to one of saturated schedd.
```
2025-04-02 23:29:01,273:DEBUG:DagmanSubmitter:Try to submit 250402_212720:borzari_crab_sigJecJerNoMet_AMSB_Wino200GeV_ctau1000cm_2022 to [crab3@vocms0119.cern.ch](mailto:crab3@vocms0119.cern.ch) for the 1 time.
2025-04-02 23:29:01,274:DEBUG:DagmanSubmitter:Getting schedd object
2025-04-02 23:29:01,586:DEBUG:DagmanSubmitter:Got schedd object
2025-04-02 23:29:01,586:DEBUG:DagmanSubmitter:Finally submitting to the schedd
2025-04-02 23:29:01,789:DEBUG:DagmanSubmitter:Condor cluster ID returned from submit is: 120772537
```

## Comment (belforte, 2025-04-08T09:52:04Z)

I looked at TW log for the first task indicated in user's report. and that was a RESUBMIT, not a SUBMIT.
We do not limit RESUBMIT even if schedd is saturated. And it bypasses task scheduling.
Difficult/impossible to say if all those tasks in Idle were resubmit or failure to enforce the limit on submit.

## Comment (belforte, 2025-04-16T12:42:31Z)

Let's assume that it was all RESUBMIT until we can catch a real "mistake" in action and dig into it. We do not have any simple way to stop "RESUBMIT". Maybe we can close new submission before the limit is reached to have some breathing room in the scheduler. Sort of a "watermark" instead of a "limit".
@aspiringmind-code @sinonkt what do you think ? It is easy to do but we have another configuration constant to track, even if we were to hardcode it.
