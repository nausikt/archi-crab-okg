# dmwm/CRABServer pull request #9280: Refactor test pipeline

State: closed
Opened: 2026-03-19T11:37:59Z
Closed: 2026-03-24T17:52:35Z
URL: https://github.com/dmwm/CRABServer/pull/9280

## Opening post (belforte, 2026-03-19T11:37:59Z)

this brings in extensive changes to test pipeline aimed to
* adapt to changes in CRAB (e.g. new status `Running`)
* ensure that test always and only fail when there's real errors (of course this is an open ended task)
* terse reports, yet allow for ` -o ci.variable="VERBOSE=0|1|2|3" 
* always wait for tasks to be completed even if sleep step was not long enough
* readable, synoptic, view of test status printed at the end of each iteration
* add CMSSW_15 to what we test
* always use CMSSW_15 (and python3) to run scripts which do not require `crab submit`

Still todo: review matrix for release validation (fewer tests, remove allow_failure)

## Comment (belforte, 2026-03-19T11:40:34Z)

I suspect that there are too many changes to review this by looking at diff of all scripts.
Maybe you can clone/tag and try yourself  to get a feeling ?

## Comment (cmsdmwmbot, 2026-03-19T11:41:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2753/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-19T14:03:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2754/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-19T14:23:02Z)

I do not see any "elegant" way to remove last pylint complain, i.e. replace `eval` with something else
```
cicd/gitlab/st/statusTracking.py

    W0123, line 48 in parse_result: Use of eval 
```
I need to change `["string"]` to `string`. But stripping quotes and brackets by brute force seems horrible, also if by any chance CRABClient is fixed to report `"string"` instead, the `eval` should still work. 
But if someone has a suggestion, I will gladly implement it.

## Comment (cmsdmwmbot, 2026-03-19T16:19:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2755/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-19T17:11:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2756/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-19T17:35:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2757/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2026-03-23T09:51:01Z)

> But if someone has a suggestion, I will gladly implement it.

How about using `ast.literal_eval` ?
```
import ast
outdataset = (
    ast.literal_eval(task['outdatasets'])[0]
    if task['outdatasets'] else None
)
```

## Comment (belforte, 2026-03-24T14:59:31Z)

thanks a lot @aspiringmind-code for having had the stamina to go through all of this and for your very good suggestions. I will make a new commit addressing those.

## Comment (belforte, 2026-03-24T17:52:35Z)

Alas not. Since in the meanwhile I had made other changes to handle Status Tracking as well, I will fix these in that branch and close this PR !
Thanks again.
