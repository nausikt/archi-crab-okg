# dmwm/CRABServer pull request #7641: refactor requestTapeRecall and accept dataset name. Fix #7603

State: closed
Opened: 2023-05-24T08:24:28Z
Closed: 2023-05-25T08:38:22Z
Merged: 2023-05-25T08:38:22Z
URL: https://github.com/dmwm/CRABServer/pull/7641

## Opening post (belforte, 2023-05-24T08:24:28Z)

in the end the relevant change for #7603 is all in this line
https://github.com/dmwm/CRABServer/blob/a3e00c4bde7ba5bb27ed959d8b6802ba461acc7f/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L314

everything else is a refactoring of requestTapeRecall to be more modular and readable and to accept a string (dataset name) as an alternative to a list of blocks.

#TODO
I tried and so far failed to move requestTapeRecall  to a separate file. Too many dependencies from things in the `self` of DBSDataDiscovery and so far no clear use case outside here.

## Comment (cmsdmwmbot, 2023-05-24T08:27:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 4 warnings
   * 68 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1526/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-05-24T08:28:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 4 warnings
   * 68 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1527/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-05-24T08:36:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 4 warnings
   * 68 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1528/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-05-24T08:54:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 4 warnings
   * 67 comments to review
 * Pycodestyle check: succeeded
   * 63 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1529/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-05-24T15:29:53Z)

>  Also, if you do not plan to split taperecall into module later, consider to hide logger and crabserver back to self.

I know that this is "halfway". I'd like to split it, but am not sure how. Ideally some code could be shared with a future "tape recall" command, but that will call for more arguments, so maybe I should make a dictionary of args... Lots of "thought in progress". There's more refactoring that would be good here, since this file is too long and hard to read. I'd like to do as part of "add locking of input data".

## Comment (cmsdmwmbot, 2023-05-24T15:44:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 20 warnings and errors that must be fixed
   * 7 warnings
   * 165 comments to review
 * Pycodestyle check: succeeded
   * 207 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1530/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-05-25T08:38:01Z)

thanks, merging
