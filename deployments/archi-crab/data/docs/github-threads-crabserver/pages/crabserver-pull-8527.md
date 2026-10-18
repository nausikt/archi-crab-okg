# dmwm/CRABServer pull request #8527: Add ChildWorker module

State: closed
Opened: 2024-06-26T12:46:12Z
Closed: 2024-06-28T11:02:12Z
Merged: 2024-06-28T11:02:12Z
URL: https://github.com/dmwm/CRABServer/pull/8527

## Opening post (novicecpp, 2024-06-26T12:46:12Z)

Fix https://github.com/dmwm/CRABServer/issues/8428

New `ChildWorker` module to spawn the child process from slave to run [work()](https://github.com/dmwm/CRABServer/blob/40a796ffe3d1c7b1b2cddf6a6e74c3b08e2b5a3a/src/python/TaskWorker/Worker.py#L94-L120) (for example, `handleNewTask` in [Handler.py#L153](https://github.com/dmwm/CRABServer/blob/43a8454abec4059ae5b2804b4efe8e77553d1f38/src/python/TaskWorker/Actions/Handler.py#L153)).

The module can handle timeout (via SIGALARM), coredump, normal error. Then, propagate errors in form of exception back to slave, and to the caller properly.

This mode(?) is behind the feature flags `config.FeatureFlags.childWorker`, can enable it from TW config file.
The TW config will have additional lines:

```python
config.section_("FeatureFlags")
config.FeatureFlags.childWorker = True
config.FeatureFlags.childWorkerTimeout = 3600 # 1 hours
```

## Comment (cmsdmwmbot, 2024-06-26T12:51:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2031/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-06-26T14:57:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2032/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-26T16:00:53Z)

shouldn't we then move to `FeatureFlags` config section other parameters related to how it works internally ? nslaves, polling, max_retry, retry_interval...

## Comment (novicecpp, 2024-06-26T16:23:08Z)

I put it behind feature flags so we can easily turn it off and purge it later if it does not work. I plan to move to the TaskWorker section later if we enable it permanently.

And nslaves, `polling, max_retry, retry_interval...` variable does not affect how the ChildWorker works except SequentialWorker where it needs to fall back to a single process for debugging with pdb.

I can move it back to the usual TaskWorker section if you do not like it.

## Comment (belforte, 2024-06-26T16:35:04Z)

Beautiful !! Thanks.
Yes, we can unify config. parameters later.

Only one comment, just like you pass `logger.name` around, could there be a simple way to pass also the logger formatter string ?
Add to future `/src/utils/TW/twUtils.py` ?

## Comment (belforte, 2024-06-26T16:59:52Z)

good point (about sequential test)

## Comment (cmsdmwmbot, 2024-06-26T17:05:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 1 warnings
   * 44 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2033/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-06-28T11:05:04Z)

Sorry Stefano, forgot to answer your question.

> Only one comment, just like you pass logger.name around, could there be a simple way to pass also the logger formatter string ?
Add to future /src/utils/TW/twUtils.py ?

I do not know the good way, but now I do not need it anymore (see [the comments in module doc](https://github.com/dmwm/CRABServer/pull/8527/files#diff-285767db147fab2ebee07ea76526755172cacc8cd8836e3e7b921f4b78d1fcdaR12-R21)).

## Comment (belforte, 2024-06-28T11:26:18Z)

thanks for the explaining the logger situation !
