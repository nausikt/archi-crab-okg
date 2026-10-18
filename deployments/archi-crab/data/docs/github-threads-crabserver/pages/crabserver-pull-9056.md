# dmwm/CRABServer pull request #9056: remove use of old TaskType ad. Fix #8617

State: closed
Opened: 2025-04-24T16:17:52Z
Closed: 2025-04-29T14:34:56Z
Merged: 2025-04-29T14:34:56Z
URL: https://github.com/dmwm/CRABServer/pull/9056

## Opening post (belforte, 2025-04-24T16:17:52Z)

(no text)

## Comment (cmsdmwmbot, 2025-04-24T16:23:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 102 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2442/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-29T09:45:59Z)

@aspiringmind-code I suspect that you do not know what this is about, but it may be a way to get to read some HTCondor constrain expressions. I do no think I have syntax errors in there, though. So am rather confident of merging and test in preprod. But as usual in the spirit of "all changes should get a second set of eyes..."

## Comment (belforte, 2025-04-29T14:34:53Z)

thanks @aspiringmind-code 

The `=?=` [operator](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-operators) is an extension of `==` to deal with the situation where the classAd may be missing (UNDEFINED). I am not sure it that could happen. Maybe original developers wanted to protect against the presence of jobs non-from-CRAB where our Ad's would be missing. Or maybe someone just got into the habit of adding the `?` to be on the safe side. When I changed the Ad name from `TaskType` to `CRAB_DAGType`  I was afraid of changing.

Usually classAd comparisons are case-insensitive, but same same [link](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-operators) says
```
String comparisons are case insensitive for most operators. The only exceptions are the operators =?= and =!=, which do case sensitive comparisons assuming both sides are strings.
```
which I must confess is new to me. I was believing that all comparisons are case insensitive !
