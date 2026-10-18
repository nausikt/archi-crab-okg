# dmwm/CRABServer pull request #7523: support in REST for dbs_blockname, block_complete

State: closed
Opened: 2023-02-03T13:14:54Z
Closed: 2023-02-06T12:58:30Z
Merged: 2023-02-06T12:58:30Z
URL: https://github.com/dmwm/CRABServer/pull/7523

## Opening post (belforte, 2023-02-03T13:14:54Z)

(no text)

## Comment (belforte, 2023-02-03T13:15:56Z)

tested on cmswen-test2 in GH mode #7520

## Comment (cmsdmwmbot, 2023-02-03T13:18:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 4 warnings
   * 74 comments to review
 * Pycodestyle check: succeeded
   * 133 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1410/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-03T14:34:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 74 comments to review
 * Pycodestyle check: succeeded
   * 133 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1411/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-05T17:03:22Z)

thanks @novicecpp . Let's not discuss here the role of new API's, I only wanted to check that I did not do something obviously wrong, main concern is of course backward compatibility, if new API do not work it is not a problem, but if we break current stuff it is a big problem.
