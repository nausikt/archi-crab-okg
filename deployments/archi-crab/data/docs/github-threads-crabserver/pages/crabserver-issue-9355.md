# dmwm/CRABServer issue #9355: Kill jobs after too many ASO failures

State: closed
Opened: 2026-07-20T14:37:38Z
Closed: 2026-08-19T15:27:03Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9355

## Opening post (belforte, 2026-07-20T14:37:38Z)

Implement mechanism to automatically kill a task once a certain number of jobs have failed during ASO (Application Service Operations) failures.

## Objective
Reduce wasted CoreHR spent in jobs that eventually fail due to ASO issues by terminating tasks early when they exceed a failure threshold during ASO operations.

## Implementation Details
- Define a threshold for the number of ASO failures before killing a task in TaskWorkerConfig 
- Implement job termination logic when threshold is reached
- Send notification to user with appropriate status message explaining the task termination

## Comment (belforte, 2026-07-22T14:32:15Z)

I think best way is to use PostJob exit code 3 to halt the DAG.
- [x] introduce conde in PostJob to do this calling some ad-hoc method where we implement the stop algorithm
- [ ] look to extend this to `condor_rm` running jobs
- [x] handle in PostJob the uploading of Warning Message to task DB
- [x] **investigate what happens with happens to crab resubmit** (first thing to do)

## Comment (belforte, 2026-07-27T16:29:58Z)

If we abort the dag via PostJob exiting with code 3, DAG terminates and writes a RescueDag and is ready to be restarted by a `crab resubmit`. As the [doc](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-completion.html#stopping-the-dag-on-node-failure) says:
> f the return value for the specified node matches AbortExitValue, the DAG is immediately aborted, meaning that the DAG stops all currently running nodes, cleans up, writes a Rescue DAG, and exits

So I think the best is to also send a kill command to TW. So that task is set in KILLED status and further submissions require a new task.

It should be possible to emulate the client kill command via a POST from PostJob. This will also handle the messaging to the user.

## Comment (belforte, 2026-07-27T16:37:50Z)

PostJob already has an extensice (and of course a bit cryptic) machinery to collect exit codes in `error_summary.json` and  to count fatally FAILED JOBS IN `task_statistics.FATAL_ERROR` (IIUC). And then abort dag via `PostJob.check_abort_dag()`.

Maybe I can reuse this ?

hmm. I am not even sure that the old `PostJob.check_abort_dag()` works well, it uses files which are not protected against concurrent write.
So I am adding new methods, to keep it clean and safe. Following long tradition of software development practice.

## Comment (belforte, 2026-08-08T14:16:24Z)

I am introducing 3 new configuration paramenters:
```python
config.TaskWorker.maxFatalAsoNumber             # self explaining
config.TaskWorker.maxFatalAsoRelativeFraction   # fraction of fatal errors in ASO transfers completed so far
config.TaskWorker.maxFatalAsoAbsoluteFraction   # fraction of fatal errors in all jobs in the task
```

The rational is that we want to kill things early, but not to kill a large tasks on a transient.

They will be ANDed. Any can be made irrelevant by setting it to 0 so it is always True.
This should allows to experiment and find best strategy.
