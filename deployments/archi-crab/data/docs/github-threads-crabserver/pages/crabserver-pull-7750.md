# dmwm/CRABServer pull request #7750: move DataRecall and DataLock to separate file

State: closed
Opened: 2023-07-12T14:59:58Z
Closed: 2023-07-17T07:55:59Z
Merged: 2023-07-17T07:55:59Z
URL: https://github.com/dmwm/CRABServer/pull/7750

## Opening post (belforte, 2023-07-12T14:59:58Z)

This is a first step toward https://github.com/dmwm/CRABServer/issues/7733
At this time I'd like to have feedback on the separation of code in two files, the class definition/use etc.

Maybe a single class should be better ? I am not very happy with two classes which only differ on the name of the Rucio account they use internally. But this is the first time I create classes, with inheritance as well.. so I am sure I did in a way which could be vastly improved.

This is supposed not to change functionality wrt what is in v3.230712 and I have done some limited testing using the internal `main()` method. 

Once we have settled on the design, I will tackle remaining pylint issues, which looks straighforward.

Thanks !

## Comment (cmsdmwmbot, 2023-07-12T15:02:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 17 warnings and errors that must be fixed
   * 5 warnings
   * 67 comments to review
 * Pycodestyle check: succeeded
   * 83 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1591/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-07-13T11:29:53Z)

Your changes in general look really nice and clean. I like it a lot!

## Comment (belforte, 2023-07-13T12:31:58Z)

OK. I will reduce to one class. I do not like all those `__init__` (and did not find the way to use `super`)
Thanks !

## Comment (cmsdmwmbot, 2023-07-14T21:55:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 5 warnings
   * 68 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1598/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T22:34:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 14 warnings and errors that must be fixed
   * 5 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1599/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T22:42:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 14 warnings and errors that must be fixed
   * 5 warnings
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1600/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T22:48:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 5 warnings
   * 40 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1601/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T22:52:05Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 warnings
   * 39 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1602/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T23:27:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 20 warnings and errors that must be fixed
   * 8 warnings
   * 121 comments to review
 * Pycodestyle check: succeeded
   * 202 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1603/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-07-14T23:48:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 4 warnings
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 202 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1604/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-15T00:02:17Z)

DBSDataDiscovery is very good pylint-wise now.
But since I moved one constant to ServerUtilities, there are tons of complaints from that.
WIll have a quick look

## Comment (belforte, 2023-07-15T00:59:16Z)

Can not do much about ServerUtilities because it needs to run in Client too (python2).

We should separate in a different file things common to client. Then it will be safe to touch.

## Comment (cmsdmwmbot, 2023-07-15T01:01:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 4 warnings
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 202 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1605/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-15T01:25:08Z)

DBSDataDIscovery is now down to one only pylint warngin, which I do not know how to solve !
```
R0201, line 64 in DBSDataDiscovery.keepOnlyDiskRSEs: Method could be a function
```
simply removing `self` in args and use, did not work.

## Comment (cmsdmwmbot, 2023-07-15T01:26:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 3 warnings
   * 96 comments to review
 * Pycodestyle check: succeeded
   * 200 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1606/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-15T01:32:39Z)

time to rebase and squash

## Comment (belforte, 2023-07-15T01:37:59Z)

Now I need to test for good. And possibly close this and make a new PR once it works and with a simpler commit history.
Anyhow review for "proper designa and style" can be done.
I know I have a lot of spaces to fix for pep-8 in DBDDataDiscovery. Will do.

## Comment (cmsdmwmbot, 2023-07-15T01:38:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 3 warnings
   * 96 comments to review
 * Pycodestyle check: succeeded
   * 200 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1607/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-16T10:28:42Z)

Jenkins tests
- [x] #7763
- [x] #7764

## Comment (belforte, 2023-07-16T14:13:56Z)

No harm to standard functionalities. Will make a separate ad-hoc test for tapeRecall

## Comment (cmsdmwmbot, 2023-07-17T07:59:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1608/artifact/artifacts/PullRequestReport.html
