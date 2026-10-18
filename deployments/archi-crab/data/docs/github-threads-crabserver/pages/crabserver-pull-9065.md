# dmwm/CRABServer pull request #9065: ignore current site availability when creating ASO rule

State: closed
Opened: 2025-05-07T14:46:43Z
Closed: 2025-05-09T15:38:39Z
Merged: 2025-05-09T15:38:39Z
URL: https://github.com/dmwm/CRABServer/pull/9065

## Opening post (belforte, 2025-05-07T14:46:43Z)

fix #9064

## Comment (cmsdmwmbot, 2025-05-07T14:48:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2447/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-07T15:27:41Z)

let me test this

## Comment (belforte, 2025-05-07T15:29:10Z)

VIjay, let me test this first, sorry

## Comment (belforte, 2025-05-09T15:38:15Z)

I could not test because it was committed on top of a master before #9067 where `crab status` was failing.
Now all sites where we can send data via Rucio are green, so can not check the "ignore availability", but did check that things are not broken. https://github.com/dmwm/CRABServer/issues/9070#issuecomment-2866481764
