# dmwm/CRABServer pull request #9228: Refactoring resubmission

State: closed
Opened: 2025-11-14T11:26:11Z
Closed: 2025-11-17T13:45:42Z
Merged: 2025-11-17T13:45:42Z
URL: https://github.com/dmwm/CRABServer/pull/9228

## Opening post (aspiringmind-code, 2025-11-14T11:26:11Z)

Fix #6270 
Major Changes include:
1. Shifting to Auto Rescue mode from Recovery
2. Deleting old defer_info files on re-submission
3. finished_jobs are tallied using crab_retry instead of dag_retry
4. No need to edit RunJobs.dag.nodes.log file or any rescue file or change PostScriptExitStatus
5. Unless Exit clause in RETRY and abort dag statements removed from dag fragment
6. Some logging added

## Comment (cmsdmwmbot, 2025-11-14T11:30:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 492 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2666/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-11-14T11:41:29Z)

What a milestone ! :rocket:
Let me read the code now !

## Comment (cmsdmwmbot, 2025-11-17T08:23:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 492 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2668/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-11-17T09:05:54Z)

@belforte I have addressed the comments, incorporated the changes and restored UNLESS-EXIT 2. Thanks for the review. Please do a final review and let me know if there are further queries/concerns.

## Comment (belforte, 2025-11-17T10:25:12Z)

Thanks @aspiringmind-code . This looks good now. I believe that we can merge, test more, and address issues as they come.

## Comment (belforte, 2025-11-17T11:29:07Z)

I opened #9232 and #9231 to followup on cleanups discussed here

## Comment (aspiringmind-code, 2025-11-17T13:45:22Z)

Thanks!
