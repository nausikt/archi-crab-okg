# dmwm/CRABServer pull request #8697: Fix #8661 changing local account usage to tape recall usage in quota report

State: closed
Opened: 2024-09-17T09:05:13Z
Closed: 2024-09-17T11:07:02Z
Merged: 2024-09-17T11:07:02Z
URL: https://github.com/dmwm/CRABServer/pull/8697

## Opening post (aspiringmind-code, 2024-09-17T09:05:13Z)

changing local account usage to tape recall usage in quota report
See https://github.com/dmwm/CRABServer/issues/8661

## Comment (cmsdmwmbot, 2024-09-17T09:09:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2168/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-17T09:44:49Z)

nice work to have "discovered" `getTapeRecallUsage`.

## Comment (belforte, 2024-09-17T09:53:51Z)

please also fix pylint warnings, even if not due to your changes, let's take chances like this to slowly improve code quality. A campaign to fix all code base is too much, but we should aim for 'all checks passed' as much as possible. So we avoid not noticing new problems amid the existing noise.

## Comment (cmsdmwmbot, 2024-09-17T10:21:34Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 17 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2169/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-17T13:03:23Z)

generally speaking it is more correct to wait before merging, or the reviewer to check that changes addressed the comments. It is not a good practice to merge with non-approved reviews.

## Comment (aspiringmind-code, 2024-09-17T13:23:27Z)

@belforte  Sorry for the hurry. As the changes requested were not major, I merged without disturbing you again. I will be more thorough going forward :)
