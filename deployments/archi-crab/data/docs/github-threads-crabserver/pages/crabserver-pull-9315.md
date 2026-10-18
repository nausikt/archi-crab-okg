# dmwm/CRABServer pull request #9315: Add DbsApi wrapper to catch and retry ORA-00001, failed block publication.

State: closed
Opened: 2026-05-14T15:10:56Z
Closed: 2026-05-14T16:29:11Z
Merged: 2026-05-14T16:29:11Z
URL: https://github.com/dmwm/CRABServer/pull/9315

## Opening post (nausikt, 2026-05-14T15:10:56Z)

Resolve #9311

## Comment (cmsdmwmbot, 2026-05-14T15:12:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2823/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-05-14T16:21:31Z)

Sure Stefano, Thanks for pointed out the [10s, 3mins] that resonated with me. 

I just realized that my simple 1s x 3 attempts retry strategy would never cover such a large-block cases. it's good to have you here!

## Comment (belforte, 2026-05-14T16:23:37Z)

main problem is that if error is race with a concurrent process, both may fail at same time and retry at same time. That's why in cabled ethernet (yeah... pretty obsolete now) the hardware drive implement retry with random delay when packets collide.

## Comment (nausikt, 2026-05-14T16:30:20Z)

> main problem is that if error is race with a concurrent process, both may fail at same time and retry at same time. That's why in cabled ethernet (yeah... pretty obsolete now) the hardware drive implement retry with random delay when packets collide.

Thanks for emphasizing!

## Comment (cmsdmwmbot, 2026-05-14T16:30:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2824/artifact/artifacts/PullRequestReport.html
