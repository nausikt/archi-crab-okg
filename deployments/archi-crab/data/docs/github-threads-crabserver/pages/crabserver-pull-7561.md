# dmwm/CRABServer pull request #7561: in python3 print is a function

State: closed
Opened: 2023-03-06T15:15:02Z
Closed: 2023-03-09T18:04:49Z
Merged: 2023-03-09T18:04:49Z
URL: https://github.com/dmwm/CRABServer/pull/7561

## Opening post (belforte, 2023-03-06T15:15:02Z)

fix bug introduced by  https://github.com/dmwm/CRABServer/commit/b1d1dd2be11116b506aed6c0410553025537131a

## Comment (cmsdmwmbot, 2023-03-06T15:21:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1455/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-03-09T17:07:04Z)

Oh no, sorry! I fixed it in my debug branch [1] but forgot to backport it to the branch I used for the PR.

This fix is absolutely correct, thank you stefano! please merge it as you see fit! I can tag, build and deploy it next week.

[1] https://github.com/dmwm/CRABServer/compare/master...mapellidario:20230215_jobwr_dbg_2
