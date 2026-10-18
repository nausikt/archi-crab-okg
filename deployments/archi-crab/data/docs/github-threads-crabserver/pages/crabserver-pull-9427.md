# dmwm/CRABServer pull request #9427: keep job in queue for 30min after PJ ends

State: closed
Opened: 2026-09-23T15:39:18Z
Closed: 2026-09-24T07:13:46Z
Merged: 2026-09-24T07:13:46Z
URL: https://github.com/dmwm/CRABServer/pull/9427

## Opening post (belforte, 2026-09-23T15:39:18Z)

Fix #9426

## Comment (cmsdmwmbot, 2026-09-23T15:43:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 292 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2922/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-09-23T21:43:46Z)

actually I did not test with tasks. I simply checked that the `schedd.edit` sets the classAd to the desired value.
`time()` is filled at run time by the schedd with the current time. So this should be `True` as long as the current time is less than the time set in the PostJob as "time of PJ execution ( time.time() ) + 30 min"

Or did I do stupid things like confusing `<` with `>` ?

## Comment (belforte, 2026-09-23T21:58:28Z)

@nausikt please have a second look in light of what I wrote and let me know if it looks OK
