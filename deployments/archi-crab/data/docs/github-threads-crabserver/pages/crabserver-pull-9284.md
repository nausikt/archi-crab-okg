# dmwm/CRABServer pull request #9284: Refactor status tracking

State: closed
Opened: 2026-03-24T21:14:15Z
Closed: 2026-03-29T14:52:34Z
URL: https://github.com/dmwm/CRABServer/pull/9284

## Opening post (belforte, 2026-03-24T21:14:15Z)

This includes:
* what previously introduced in #9280 
* resolution of Vijay's comments in there
* refactoring of StatusTracking tests for clean log and full error catching
* reduced amount of testing for oldish CMSSW versions

**CAVEATS**
after this is tested still need to
 * remove hack which allows to test `release` pipeline in my dev w/o creating a new v3.xxxx tag
 * remove `allow to fail`
 * tune sleep (very short now to speed up testing
 * better logging, comments, doc....

## Comment (cmsdmwmbot, 2026-03-24T21:18:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2759/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-24T21:19:18Z)

@aspiringmind-code I did not squeeze commits yet so you can see the ones which address your comments on #9280 . In the spirit of not dragging this on too long, I suggest that you have a quick look at "strategy", then I squash, merge to master and we solve problems as they come.
I am testing this branch now in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/14365152 and of course will work on any issue which arises from that. Feel free to wait for a successful test pipeline (at least), although we know that successful test does not mean good test and failed test may mean "job failed on grid" or "submission failed due to Rucio or whatever other crap..." sigh.

## Comment (cmsdmwmbot, 2026-03-24T21:29:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 241 comments to review
 * Pycodestyle check: succeeded
   * 178 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2760/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-24T21:33:42Z)

OH MY... I must have made a mess when merging my branches. I lost the changes to run on a reduced set of CMSSW releases and to skip CCV and ST for older ones. Tomorrow....

## Comment (belforte, 2026-03-29T14:52:34Z)

several things were not right, and fixing this branch was too much chaos.
I made a new clean PR
