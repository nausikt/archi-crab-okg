# dmwm/CRABClient pull request #5188: add src/**/python to user sandbox

State: closed
Opened: 2023-02-17T11:28:32Z
Closed: 2023-02-27T11:56:39Z
Merged: 2023-02-27T11:56:39Z
URL: https://github.com/dmwm/CRABClient/pull/5188

## Opening post (mapellidario, 2023-02-17T11:28:32Z)

Fixes #5187

### status

tested:

- [x]  https://cmsweb-test11.cern.ch/crabserver/ui/task/230217_111711%3Admapelli_crab_20230217_121708

### description

This PR simply adds to the sandbox all the `python`  directories that are recursively found under `$CMSSW_BASE/src`. 

I have two questions for @belforte :

- [x] should we clean the comments and variable names? I mean, if we send the `python` directories maybe we should stop referring to those directories as "data". this is just cosmetic, i am not even sure i am willing to risk renaming variables and comments more than necessary
- [x] should we stop supporting the `Jobtype.sendPythonFolder` option? I am not sure how much this change makes it irrelevant. Maybe this is more for cmssw people to decide

## Comment (cmsdmwmbot, 2023-02-17T11:34:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 1 warnings
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 29 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/928/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-23T08:19:51Z)

sorry @mapellidario for revieweing so late. Feel free to merge and build new client

## Comment (belforte, 2023-02-23T08:23:51Z)

I thought I had replied to questions above, looks like not. So:
> should we clean the comments and variable names?

  sure, thanks
> should we stop supporting the Jobtype.sendPythonFolder option?

 I think not, that's `$CMSSW_BASE/python` IIRC, while here you are adding `$CMSSW_BASE/src/<whatever>//python/`

## Comment (cmsdmwmbot, 2023-02-27T11:47:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 1 warnings
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 29 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/929/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-02-27T11:56:27Z)

> I think not, that's $CMSSW_BASE/python IIRC, while here you are adding $CMSSW_BASE/src/<whatever>//python/

Yeah, you are right. `$CMSSW_BASE/python` will still be populated in all the cmssw version older than 12_6, so it makes sense to keep it. thanks!

I added some comments, my changes feel pretty safe, I will merge them myself and will run some tests on them.

Thanks for the review!

## Comment (belforte, 2023-02-27T12:05:34Z)

AH !! I did not know that with CMSSW_12_6 they change the way user python scripts are managed ! Seems a large change for a mid-series version. Oh well... 
Honestly I did not know what exactly has to go in $CMSSW_BASE/python, we made it optional to include it simply in fear that users put all kind of junk there, but if people put there only what `scram` needs, we may be safe by removing the option and simplify things a bit.
If you get a chance to talk with Shahzad, maybe you can clarify ?
