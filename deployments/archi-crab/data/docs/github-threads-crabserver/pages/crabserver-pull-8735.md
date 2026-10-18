# dmwm/CRABServer pull request #8735: Run spark cronjobs on ipynb directly

State: closed
Opened: 2024-10-08T20:42:51Z
Closed: 2024-10-11T15:33:25Z
Merged: 2024-10-11T15:33:25Z
URL: https://github.com/dmwm/CRABServer/pull/8735

## Opening post (novicecpp, 2024-10-08T20:42:51Z)

Fix https://github.com/dmwm/CRABServer/issues/7798

Instead running on py file where it need to copy the contents from Jupyter notebook back and forth between dev/PoC to prod, we make notebook files to be able to run as cronjobs instead. 
To debug those notebook files in the future, you simply copy to CERN's Jupyter and run it directly as notebook. 
When you finish fixing code, or creating a new one,  simply clean up notebook output and copy back to `crab-spark/notebooks`.

You need to be careful when crafting those notebooks though. But it is simply the template that you need to follow.

Note that this PR includes the fixes that work with the current setup we have with Monit team.

I will wrote it down the instruction after it merge to master tomorrow.

## Comment (novicecpp, 2024-10-08T20:45:50Z)

@belforte Stefano, I did not ask for a review from you this time and kinda force you to accept my approach. 
But, I can guarantee that you can revert this behavior back to a simple py file later if it does not work or you do not like it.

We can have some chat tomorrow in the meeting.

## Comment (cmsdmwmbot, 2024-10-08T21:14:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2189/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-09T12:18:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2191/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-11T15:33:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 71 comments to review
 * Pycodestyle check: succeeded
   * 33 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2196/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-10-11T15:34:50Z)

This PR is running daily in dev without any issue. 

I need to merge this to master first before I can put in production.
