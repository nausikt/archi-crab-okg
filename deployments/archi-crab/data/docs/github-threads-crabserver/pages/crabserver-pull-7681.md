# dmwm/CRABServer pull request #7681: Cleanup cms run analysis.py

State: closed
Opened: 2023-06-27T16:57:14Z
Closed: 2023-07-04T07:51:23Z
Merged: 2023-07-04T07:51:23Z
URL: https://github.com/dmwm/CRABServer/pull/7681

## Opening post (belforte, 2023-06-27T16:57:14Z)

this is an "exercise" in getting rid of pylint complains "in bold in the summary".
There's only one left about using `optparse` which is now deprecated [1]. But at a first quick look I think that replacing it with the new `argparse` is not trivial, so let's wait until this is desperately needed. There are many places were we use `optparse` in CRAB. 

[1]
from [the Doc](https://docs.python.org/3.10/library/optparse.html?highlight=optparse#module-optparse)

Deprecated since version 3.2: The [optparse](https://docs.python.org/3.10/library/optparse.html?highlight=optparse#module-optparse) module is deprecated and will not be developed further; development will continue with the [argparse](https://docs.python.org/3.10/library/argparse.html#module-argparse) module.

## Comment (cmsdmwmbot, 2023-06-27T17:05:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 14 warnings
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1554/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T17:27:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 14 warnings
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1555/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T21:13:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
 * Pycodestyle check: succeeded
   * 73 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1556/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T21:22:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 14 warnings
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1557/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T21:37:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 14 warnings
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1558/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T21:45:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 14 warnings
   * 120 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1559/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T21:53:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 14 warnings
   * 114 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1560/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T22:42:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 14 warnings
   * 114 comments to review
 * Pycodestyle check: succeeded
   * 70 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1561/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T22:52:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 14 warnings
   * 51 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1562/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-27T22:58:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 14 warnings
   * 51 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1563/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-27T23:09:10Z)

besides removing one function https://github.com/dmwm/CRABServer/pull/7681/commits/856ac04009f2f7cc3041774a78b0b3d5b4af5f74 the pylint chages are many so
submitted a few Jenkins to do an initial validation of "not broken". 

- [ ] #7682
- [ ] #7683 
- [ ] #7684
- [ ] #7685

## Comment (belforte, 2023-06-28T08:09:18Z)

Most Client Config.Validation tests failed. Investigating. Looks like I overdid it !
```
 Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 761, in <module>
    with open('jobReportExtract.pickle', 'wb', encoding='utf-8') as of:
ValueError: binary mode doesn't take an encoding argument
```

## Comment (cmsdmwmbot, 2023-06-28T23:50:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 51 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1564/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-29T12:53:50Z)

Jenkins after the fix #7692 
3 failures, investigating

## Comment (belforte, 2023-06-29T13:00:05Z)

problem was https://github.com/dmwm/CRABServer/pull/7681/commits/856ac04009f2f7cc3041774a78b0b3d5b4af5f74
that prepSandbox is needed to place a user script in the current directory, one step above $CMSSW_BASE !

Here's a sketch :
```
/srv                --> cwd. ScriptExe needs to be here
 /srv/CMSSW_13_1_0  --> $CMSSW_BASE: sandbox files picked from "user SCRAM tree" needs to be here
```
FYI @mapellidario 

this is consistent with description of `inputFiles` configuration parameter in twiki:
```
The input files will be placed in the working directory where the users' application (e.g. cmsRun) is launched 
```

The problem as I understand it now is that in `sandbox.tar.gz` we mix "scram" things and `inputFiles` taken from different places and archive both as "at same level", e.g. this
```
config.JobType.inputFiles = ['kh.tar', 'kh2.tgz', 'kh3.tar.gz']
```
picks files from the directory where `crab submit` is ran (could be anywhere) and in the sandbox we have
```
lib/
lib/slc7_amd64_gcc11/
biglib/
biglib/slc7_amd64_gcc11/
kh.tar
kh2.tgz
kh3.tar.gz
PSet.py
PSet.pkl
PSetDump.py
```
Now some files need to be placed in `/srv` on the WN, some in `/srv/CMSSW_x_y_x`
Current code places expands the sandbox in both places. Ugly, but works.


I do not see a simple way to put each file "only where it is needed" w/o using two tar files. One for `$CMSSW_BASE/...`, one for `/srv`. Maybe those can still be combined in a single sandbox etc. but code changes are needed at least both on client and job wrapper.

A simpler possibility is maybe to modify https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/scripts/CMSRunAnalysis.py#L385 to put needed files in $CMSSW_BASE and do w/o https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/scripts/CMSRunAnalysis.py#L407. But I am not sure if we have a good way of marking which files need to go in $CMSSW_BASE. An explicit list will quickly get obsolete and/or loose client/server syncronization

@mapellidario what do you think ? We need some good idea here !

## Comment (belforte, 2023-06-29T14:33:29Z)

I will revert https://github.com/dmwm/CRABServer/commit/856ac04009f2f7cc3041774a78b0b3d5b4af5f74 and make a PR with only the cleanup for pylint. Will move to ad hoc issue the "expand sandbox only once in one only place".

No wonder that I was always confused as to where the sandbox files go, they go in two places but are only needed in one !
To add to confusion `PSet` is moved from `$CMSSW_BASE` to `/srv` in https://github.com/dmwm/CRABServer/blob/2c31e26c5903fbce0bcbe68f1217ed150ea043bf/scripts/CMSRunAnalysis.py#L414-L415 even if it was there already !

## Comment (belforte, 2023-06-29T14:37:52Z)

new Jenkins : https://github.com/dmwm/CRABServer/issues/7694

## Comment (cmsdmwmbot, 2023-06-29T14:37:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 15 warnings
   * 59 comments to review
 * Pycodestyle check: succeeded
   * 68 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1566/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-29T14:47:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 69 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1567/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-29T20:12:22Z)

https://github.com/dmwm/CRABServer/issues/7694 failed on scriptArgs test (see https://github.com/dmwm/CRABServer/issues/7694#issuecomment-1613746943)
Try again after https://github.com/dmwm/CRABServer/pull/7681/commits/ab67e779cca36f9ebaffdedb1ab8a5f7b239f45d

## Comment (cmsdmwmbot, 2023-06-29T20:13:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 69 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1568/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-29T20:16:58Z)

New Jenkins test:  https://github.com/dmwm/CRABServer/issues/7696

## Comment (belforte, 2023-06-29T20:31:23Z)

scriptArgs is OK now. Submit full set of Jenkins.

- [x] https://github.com/dmwm/CRABServer/issues/7697
- [x] https://github.com/dmwm/CRABServer/issues/7698
- [x]  https://github.com/dmwm/CRABServer/issues/7703
- [x] https://github.com/dmwm/CRABServer/issues/7699
- [x] https://github.com/dmwm/CRABServer/issues/7700
- [x]  https://github.com/dmwm/CRABServer/issues/7701
- [x]  https://github.com/dmwm/CRABServer/issues/7702

## Comment (belforte, 2023-06-30T09:09:47Z)

WOW. All Jenkins tests completed successfully.
A couple problems were found and solved, thanks Jenkins.
This PR is ready to be merged

## Comment (belforte, 2023-06-30T15:51:42Z)

@mapellidario now that I understand a bit better what's happenig here, I will try to remove reference to WMTasskSpace while keeping sanbox untarring in the two places. IN cleanup spirit.

## Comment (cmsdmwmbot, 2023-06-30T15:53:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 67 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1569/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T20:49:48Z)

quick validation (only CCV)
- [x] #7706 
- [x] #7707

## Comment (cmsdmwmbot, 2023-06-30T20:55:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1571/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-06-30T21:03:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1572/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T21:06:46Z)

hopefully final, other than merging with https://github.com/dmwm/CRABServer/pull/7708 (still to be validated).
Running a couple more Jenkins CCV (as a way to eercise job wrapper on different configs)
- [ ] #7709 
- [ ] #7710


all failed. Code was mixed with a bugged version of https://github.com/dmwm/CRABServer/pull/7708.

Need to reset things

## Comment (cmsdmwmbot, 2023-06-30T23:10:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 15 warnings
   * 54 comments to review
 * Pycodestyle check: succeeded
   * 66 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1576/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T23:14:01Z)

new tests
- [x] #7711
- [x] #7712

## Comment (belforte, 2023-07-03T13:56:05Z)

thanks Dario. Yes, no need to close explicitly. But.. why make a call to `os.utime` at all ? And now that you made me look better, is this `logCMSSWSaved.txt` used anywhere ?  What is the purpose of those lines ? Some leftover from previous refactoring ?

OK `logCMSSWSaved.txt` is used here (earlier I only looked in python files)
https://github.com/dmwm/CRABServer/blob/fc50785a5f851448d415d93c1e27cdc00675e40c/scripts/CMSRunAnalysis.sh#L17

But the time is never checked, only file existence !
