# dmwm/CRABServer pull request #7526: Allow use different cert for rucio client

State: closed
Opened: 2023-02-09T15:04:18Z
Closed: 2023-02-24T17:05:32Z
Merged: 2023-02-24T17:05:32Z
URL: https://github.com/dmwm/CRABServer/pull/7526

## Opening post (novicecpp, 2023-02-09T15:04:18Z)

By specify `config.Services.Rucio_cert` and `config.Services.Rucio_key` in [TaskWorkerConfig.py](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb)

## Comment (cmsdmwmbot, 2023-02-09T15:08:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 warnings
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1417/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-09T15:13:36Z)

I am curious, what is the use case for needing a different cert for Rucio client and TW other work like talking with REST (I guess) ?

## Comment (belforte, 2023-02-20T15:02:20Z)

@novicecpp what do we do with this ? if it is useful, I have no problems, but if not, let's keep code "simpler"

## Comment (novicecpp, 2023-02-20T17:38:57Z)

Yes, it is still useful to me. But keep it for a week before merging into master. I need to look into puppet code which may have a simpler way to do it.

## Comment (novicecpp, 2023-02-24T17:05:24Z)

I am merging this. Still looking for better solution.
