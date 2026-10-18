# dmwm/CRABServer pull request #9106: fix bugs in reporting of corrupted files

State: closed
Opened: 2025-06-03T22:47:09Z
Closed: 2025-06-05T13:18:09Z
Merged: 2025-06-05T13:18:09Z
Labels: To be tested
URL: https://github.com/dmwm/CRABServer/pull/9106

## Opening post (belforte, 2025-06-03T22:47:09Z)

fix #9105

## Comment (belforte, 2025-06-03T22:50:08Z)

@aspiringmind-code clearly I should asked for a review when I committed #8801  !

That said, do not sped too much time on this, since it is not critical, the problem is that it is hard to test, one needs to find truncated files first !

## Comment (cmsdmwmbot, 2025-06-03T22:51:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2488/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-06-04T08:50:28Z)

thanks for quick review

## Comment (belforte, 2025-06-04T08:51:24Z)

I will test anyhow. As soon as cmsweb-test2 is working again

## Comment (belforte, 2025-06-05T13:18:05Z)

I can't test since the truncated files from the user report which triggered my investigation are fixed now :-(

let's merge and see how it goes, all this code is wrapper in `try..except pass` anyhow, so at worse it does not report, just like it was doing in last 6 months :-(
