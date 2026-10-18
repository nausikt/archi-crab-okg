# dmwm/CRABServer pull request #8431: beware extra spaces in accelerator_jdl too

State: closed
Opened: 2024-05-27T08:24:56Z
Closed: 2024-05-27T08:25:33Z
Merged: 2024-05-27T08:25:33Z
URL: https://github.com/dmwm/CRABServer/pull/8431

## Opening post (belforte, 2024-05-27T08:24:56Z)

(no text)

## Comment (cmsdmwmbot, 2024-05-27T08:27:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2000/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-05-28T06:10:41Z)

Do we really need this PR? Because `accelerator_jdl` is constructed by `DagmanCreator.py`

https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/src/python/TaskWorker/Actions/DagmanCreator.py#L507-L522

## Comment (belforte, 2024-05-28T07:10:14Z)

then we do not need it. My apologies for not having looked up where that is created.

## Comment (novicecpp, 2024-05-28T07:19:29Z)

No need to apologize and sorry for using strong word.
I was wondering if you seen something that it didn't see here :-)

## Comment (belforte, 2024-05-28T07:29:32Z)

which strong word ?
Anyhow  we do not need the effort to revert this, that code will anyhow change with #8336
