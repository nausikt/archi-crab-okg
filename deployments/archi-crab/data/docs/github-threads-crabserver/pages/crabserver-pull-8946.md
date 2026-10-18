# dmwm/CRABServer pull request #8946: make maxWallTime work. Fix () in periodicRemoveReason

State: closed
Opened: 2025-02-26T18:17:01Z
Closed: 2025-02-27T12:26:48Z
Merged: 2025-02-27T12:26:48Z
URL: https://github.com/dmwm/CRABServer/pull/8946

## Opening post (belforte, 2025-02-26T18:17:01Z)

Looks like setting a max RunTime was not working since a long time :-(
Our CCV test checks the ad used for glidein matching, not the one which will kill long running jobs.
I suspect that when I wrote that test I had not understood how exactly this works

## Comment (cmsdmwmbot, 2025-02-26T18:19:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 73 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2387/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-02-26T18:20:36Z)

@aspiringmind-code since you have been picked to help me rewrite resubmission... I am afraid you will need to learn such details. Feel free to ask !

## Comment (belforte, 2025-02-26T19:48:50Z)

tested on https://cmsweb-test2.cern.ch/crabserver/ui/task/250226_182249%3Abelforte_crab_20250226_192242

## Comment (belforte, 2025-02-27T12:26:45Z)

thanks @aspiringmind-code for your review. Yup, you got it right.
I added some missing `()` in the periodicRemove expressions which I think were not correctly evaluated.
