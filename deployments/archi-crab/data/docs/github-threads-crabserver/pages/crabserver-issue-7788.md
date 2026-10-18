# dmwm/CRABServer issue #7788: make TapeRecallManager work for any TW name

State: closed
Opened: 2023-08-01T13:59:50Z
Closed: 2023-08-01T16:54:36Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7788

## Opening post (belforte, 2023-08-01T13:59:50Z)

Current TapeRecallManager only acts on tasks submitted by same TW as it runs on.
This may marginally help when running multiple TW in parallel, so we can use same exact configuration for recurring actions.
But when we simply switch TasskWorker, like we did recently, tasks put in recall by previous TW were left un-managed.

Since we usually only run one TW, it is better to make TapeRecallManager independent of the TW name.
Even if we end up running two instances at same time, there should be no problem, at worst, in case of race, a task status is set to same `NEW` or `KILLED` value twice in a row.
