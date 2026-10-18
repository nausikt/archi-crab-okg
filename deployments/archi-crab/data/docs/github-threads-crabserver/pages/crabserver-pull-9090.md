# dmwm/CRABServer pull request #9090: add quick PostJob defer for Rucio-ASO. Fix #9079

State: closed
Opened: 2025-05-22T08:08:06Z
Closed: 2025-05-26T14:18:15Z
Merged: 2025-05-26T14:18:15Z
URL: https://github.com/dmwm/CRABServer/pull/9090

## Opening post (belforte, 2025-05-22T08:08:06Z)

(no text)

## Comment (cmsdmwmbot, 2025-05-22T08:10:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2467/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-22T16:46:04Z)

looks like it does not work, I get in Dagman log
```
05/22/25 16:56:48 POST Script of node Job844 failed with status 1
```
so the job gets resubmitted.

## Comment (belforte, 2025-05-22T19:25:32Z)

problem is
```
dag_bootstrap.sh: line 22: /4: syntax error: operand expected (error token is "/4")
```
yet.. I tested this :-(

## Comment (belforte, 2025-05-22T19:26:30Z)

ouch... `defers` vs. `defer`  :sob: :scream: 
https://github.com/dmwm/CRABServer/blob/e646aa7ec2887fc8e9f6911fd15e7ff33931f8ae/scripts/dag_bootstrap.sh#L22

## Comment (cmsdmwmbot, 2025-05-22T19:33:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2475/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-23T09:35:33Z)

thanks for reading Vijay !
I would not have hard-to-understand code if possible !
did you look at the table https://github.com/dmwm/CRABServer/issues/9079#issuecomment-2887210722
I will be happy to add more comments, any hint ?

I went for a probability to skip calling python, because I could not think of a simple algorithmic way.
Maybe I did not try hard enough. As usual I welcome suggestions to improve.

## Comment (aspiringmind-code, 2025-05-23T09:40:40Z)

Yes the table was helpful. I suggest we can add in comments: "prob = defers / 4  A random integer is drawn from [1, prob] The PostJob only runs if the random draw equals 1. So the chance that test == 1 is:
 P(run) = 1 / prob = 1 / (defers / 4) = 4 / defers" It's not hard to understand. I like it in fact.

## Comment (belforte, 2025-05-23T10:20:28Z)

I tried to make it more clear, and put a "protection" against breaking it unintentionally, since relying on some other script log message is fragile.

@aspiringmind-code please have a new look, and check for typos since I can't rely on pylint here

## Comment (cmsdmwmbot, 2025-05-23T10:21:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 292 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2478/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-05-23T10:55:30Z)

Looks great!

## Comment (cmsdmwmbot, 2025-05-23T12:20:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 292 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2480/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-26T13:44:31Z)

I have tested this as much as I could . Do you want to review more @aspiringmind-code ? Or may I merge ?

## Comment (aspiringmind-code, 2025-05-26T13:48:33Z)

Please feel free to merge. LGTM!
