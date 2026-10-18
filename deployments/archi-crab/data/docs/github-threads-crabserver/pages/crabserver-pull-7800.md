# dmwm/CRABServer pull request #7800: Fix 7799

State: closed
Opened: 2023-08-07T12:10:58Z
Closed: 2023-08-07T15:14:50Z
Merged: 2023-08-07T15:14:50Z
URL: https://github.com/dmwm/CRABServer/pull/7800

## Opening post (belforte, 2023-08-07T12:10:58Z)

(no text)

## Comment (cmsdmwmbot, 2023-08-07T12:16:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 60 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1643/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-07T12:54:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 60 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1644/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-07T13:06:46Z)

I started inheriting from TaskActions, but in the end it is not the correct abstractions, brings a lot of stuff in `self` which is not needed and makes things hard to understand. Of course one could still change. Maybe there should be a better name than RucioAction to indicate that this is not an action to perform on a `task` object .

I am staying out of `ServerUtilities.py` because we use it also in CRABClient, so have to keep it py2 compatible. In a way this is a first step over moving elsewhere code which is not needed by the Client. A long overdue cleanup, Again I have been debating a bit in my head `src/pythone/WorkerUtilities.py` vs. `src/python/TaskWorker/WorkerUtilities,py` vs. other names....
Ideally one should have started by renaming `ServerUtilities.py` to `CommonClientServerUtilities.py` and create a new `ServerUtilities.py`.  But pushing the change in CRABClient takes time and renaming all imports would be a pain.

My apologies for not having discussed this strategy first. I am certainly open to change here. Whatever minimizes works while at least not increasing confusion !

## Comment (novicecpp, 2023-08-07T14:32:10Z)

Ok, I see. Then, I think this PR is fine.
We can discuss refactoring `ServerUtilities.py` later in https://github.com/dmwm/CRABServer/issues/7765.
