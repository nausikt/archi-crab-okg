# dmwm/CRABServer pull request #9330: introduce migrationAccounter. Fix #9329

State: closed
Opened: 2026-06-25T19:49:51Z
Closed: 2026-06-26T10:01:05Z
Merged: 2026-06-26T10:01:05Z
URL: https://github.com/dmwm/CRABServer/pull/9330

## Opening post (belforte, 2026-06-25T19:49:51Z)

Also fix pylint in PublisherDbsUtils

## Comment (cmsdmwmbot, 2026-06-25T19:54:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 15 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2846/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-25T19:56:31Z)

@nausikt I have tested this in my dev test2 with normal publication and one failed migration and it seems to work . But I did not test that it stops trying when a migration failed too much.
 Please review and kindly give me your opinion on whether we could try to use this in production or not.
As mentioned in last meeting I think that current implementation via editing a CSV file is gross to say the least. So it is for you to rewrite the `failedMigrationAccounter` using SQLite.
Do you think that we should wait until that before testing in production ?
I hesitate a bit to do many changes at same time, but it is not easy to test with multiple processes and many migrations outside production.
Advice is more than welcome

## Comment (belforte, 2026-06-26T09:53:16Z)

thanks for ultra-fast review.
10 failures and 2 days is sort of "invented". Note that the limit is per block, not per task. A task may keep happily publishing for a month, but if one block fails to migrate, changes are that most (all) of the parent dataset can't migrate !

That limit 10 fails x 2 days is not very good, we retry failed migrations at every cycle, so ~every hour, and I although there are migrations which work after resubmitting them a bit later (races, server restarts...) I have never seen something recover after a day, other than for DBS Developers intervention.

All in all it may be worth to put those two numbers in the configuration.

I'll make an issue for that, and do it, and one for sqlite which I will assign to you

## Comment (nausikt, 2026-06-26T11:02:28Z)

Thank you for revealed my knowledge gaps so cleanly.🙇

it does resonate with me now, apologize for my superficial review.
