# dmwm/CRABServer pull request #7789: TapeRecallManager acts task created by any TW. Fix #7788

State: closed
Opened: 2023-08-01T14:01:58Z
Closed: 2023-08-01T16:54:34Z
Merged: 2023-08-01T16:54:34Z
Labels: PR: do not merge
URL: https://github.com/dmwm/CRABServer/pull/7789

## Opening post (belforte, 2023-08-01T14:01:58Z)

(no text)

## Comment (cmsdmwmbot, 2023-08-01T14:04:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1633/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-01T14:47:22Z)

@mapellidario I am particularly intersted on your opinion on how I tried to solve the pylint complaints
```
W0201, line 38 in TapeRecallManager._execute: Attribute 'config' defined outside __init__
W0201, line 155 in TapeRecallManager.init: Attribute 'restHost' defined outside __init__
W0201, line 155 in TapeRecallManager.init: Attribute 'dbInstance' defined outside __init__ 
```
via https://github.com/dmwm/CRABServer/commit/4335bdb74de36c04da0bbf560f2773472db7e296
even if for some obscure reason that commit does not show up in this PR page yet. I hope it will at some point !

Let's not merge until that is finalized.

## Comment (belforte, 2023-08-01T14:51:07Z)

yeah.. I tested the new code on crab-prod-tw02 already :-)
But I still do not understand why https://github.com/dmwm/CRABServer/commit/4335bdb74de36c04da0bbf560f2773472db7e296 does not show up here

## Comment (mapellidario, 2023-08-01T15:15:03Z)

> I tested the new code on crab-prod-tw02 already

I imagined, but i never passed an "accept all" argument to SQL and needed to try it anyways :)

Regarding the solution for the pylint complain. 
There is a difference between "static class variables" [a] and "instance variables" [b]. See [1]. Your changes in https://github.com/dmwm/CRABServer/commit/4335bdb74de36c04da0bbf560f2773472db7e296 effectively changed `config`, `restHost` and `dbInstance` from "instance variables" to "static class variables".
Is this a problem? I do not think so. Since TapeRecallManager is likely a singleton (a single instance of the class will ever exist at any time), so it should not make any difference if those variable to be "static class var" or "instance var" . Moreover, your changes are consistent with the other variables (`pollingTime`, `rucioClient`, ...) in TapeRecallManager.py and in TapeRecallStatus.py.

So ok, all good for me

---

[1] https://stackoverflow.com/a/43921843

[a]

```python
class MyClass():
    my_static_class_var = None
```

[b]

```python
class MyClass():
    def __init__():
        self.my_instance_var = None
```

## Comment (belforte, 2023-08-01T15:26:47Z)

I tried to use `self.restHost` etc., i.e. solution [2] but could not find a way to add my own `__init__` while preserving the base class one as well.
I agree that here things are OK, bug generally speaking I would like to understand how to deal with such situations in a clean way.

I suspect that the trick in
https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/src/python/TaskWorker/Actions/Recurring/BaseRecurringAction.py#L7-L10
is surely fantastic but somehow conflicts with clean inheritance.

Anyhow, what troubles me is that my branch has 2 comimits, but this PR only has 1. Seems an issue inside GH :-(

## Comment (belforte, 2023-08-01T15:46:58Z)

test this please

## Comment (cmsdmwmbot, 2023-08-01T15:49:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1634/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-01T16:12:46Z)

Eventually I added one comment line and this forced GH to refresh the PR. 3 commits now !

## Comment (cmsdmwmbot, 2023-08-01T16:16:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1635/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-01T16:24:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1636/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-01T16:31:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1637/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-01T16:37:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 6 warnings
   * 1 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1638/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-01T16:54:11Z)

rebased and cleaned up. Let's merge
