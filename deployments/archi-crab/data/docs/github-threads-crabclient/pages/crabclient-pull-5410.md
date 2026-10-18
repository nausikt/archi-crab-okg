# dmwm/CRABClient pull request #5410: Make compatible with new tarballs 5409

State: closed
Opened: 2025-08-11T20:30:33Z
Closed: 2025-08-20T10:02:21Z
Merged: 2025-08-20T10:02:21Z
URL: https://github.com/dmwm/CRABClient/pull/5410

## Opening post (belforte, 2025-08-11T20:30:33Z)

(no text)

## Comment (cmsdmwmbot, 2025-08-11T20:34:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1137/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-11T20:43:13Z)

@aspiringmind-code I know that this is a tough one to review since context is not clear. All I ask is that you agree that current behavior is preserved. I tested on a task submitted with current TW .. but a second look is always better. If you find that it takes too much of your precious time, do not do it. We will have to go through the whole "new tarballs" thing at some point

## Comment (aspiringmind-code, 2025-08-13T08:24:26Z)

Thanks @belforte I will review it by today.

## Comment (belforte, 2025-08-13T08:55:57Z)

no urgency. I am still way off from having a TW which needs this

## Comment (belforte, 2025-08-20T09:56:48Z)

Thanks for you review VIjay
about the `sh`... pretty stupid thing. Somehow the file does not have the `+x` permission anymore. I did not have the stomach to look for where it got lost, and since already `gWMS-CMSRunAnalysis.sh` calls this as `sh ./CMSRunAnalysis.sh "$@"` I thought better to simply use the same when running it locally, to be safe.

## Comment (belforte, 2025-08-20T09:58:51Z)

let me know if you think I should change

## Comment (aspiringmind-code, 2025-08-20T10:00:47Z)

No need to change. Thanks!
