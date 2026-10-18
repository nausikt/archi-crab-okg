# dmwm/CRABServer issue #8089: resubmission of successful jobs only works while Dagman is running

State: closed
Opened: 2023-12-06T17:58:27Z
Closed: 2024-01-11T17:21:32Z
Labels: Type: Documentation, Priority: Medium, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8089

## Opening post (belforte, 2023-12-06T17:58:27Z)

properly verify.
Why failed jobs can be resubmitted also later ?

If possible fix. Otherwise document.
Connects to https://github.com/dmwm/CRABClient/issues/5273

## Comment (belforte, 2023-12-08T19:12:43Z)

maybe "as simple" as: if some jobs fail there's a Rescue DAG which we can trigger into action. But if will only contain failed nodes. ANd possibly the DAG stays in HOLD.

Once the `dagman_bootstrap` job has exited the HTCondor queue, there is not way to restarting. A new `condor_submit` is needed.

It will be nice to complement this with pointers to the code.
But maybe for the time being is enough for closing on "document that successful jobs can only be resubmitted when task is running". After that... there is `crab recovery` and/or `crab clone`.

Anyhow I am not sure that there are really important use cases where successful jobs needs to be resubmitted !

User report in https://cms-talk.web.cern.ch/t/crab-resubmit-force-not-working/32482/6 was something like "I can't believe that those jobs were successful and I want to try again". Nope !

## Comment (belforte, 2023-12-11T18:42:11Z)

in the meanwhile, here's a pointer to DAGMAN documentation
https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-resubmit-failed.html
and to DagmanResubmitter code
https://github.com/dmwm/CRABServer/blob/39aef1a1eccf893b1a2d9aea9e85956565c1f81c/src/python/TaskWorker/Actions/DagmanResubmitter.py#L97-L113
and to AdjustSites.py which edits dagman logs
https://github.com/dmwm/CRABServer/blob/39aef1a1eccf893b1a2d9aea9e85956565c1f81c/scripts/AdjustSites.py#L458-L486

## Comment (belforte, 2024-01-11T17:21:32Z)

there's already a follow up in  https://github.com/dmwm/CRABClient/issues/5273 where this was resolved by adding a warning.
As definitive solution, we will deprecate resubmission of successful jobs https://github.com/dmwm/CRABClient/issues/5285
