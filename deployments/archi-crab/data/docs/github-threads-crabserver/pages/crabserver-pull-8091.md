# dmwm/CRABServer pull request #8091: Add new Rucio ASO test tasks for testsuite "Task_Submission_Status_Tracking"

State: closed
Opened: 2023-12-08T18:05:02Z
Closed: 2023-12-08T19:27:38Z
Merged: 2023-12-08T19:27:38Z
URL: https://github.com/dmwm/CRABServer/pull/8091

## Opening post (novicecpp, 2023-12-08T18:05:02Z)

(no text)

## Comment (cmsdmwmbot, 2023-12-08T18:15:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 45 comments to review
 * Pycodestyle check: succeeded
   * 116 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1782/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-12-08T19:27:23Z)

Merging. It should work out-of-the-box by https://github.com/dmwm/CRABServer/blob/0bf7e86b7263c22ea544d6b10fb85bfb49adcc67/test/container/testingScripts/taskSubmission.sh#L89C15-L89C15
(I have tested in my local Jenkins and it works fine.)
