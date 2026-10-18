# dmwm/CRABServer pull request #9432: Notify the user via CRAB_UserEmail on too many fatal ASO errors

State: closed
Opened: 2026-09-26T12:46:33Z
Closed: 2026-10-01T16:05:36Z
Merged: 2026-10-01T16:05:36Z
URL: https://github.com/dmwm/CRABServer/pull/9432

## Opening post (nausikt, 2026-09-26T12:46:33Z)

PR on top of #9431 

## Short Summary
This PR refactored the existing ASO logic into proper `handleTooManyFatalAsoErrors` handler fn and added `sendMaxFatalAsoMailToUser` as a separate path from operator mailing, which may be used to provide additional debugging information for prod env in the future. Also added safety locks for UserMail firing.

### Context
Since #9383/#9416, PostJob kills a task (or, with `maxFatalAsoDryRun`, pretends to)
once fatal stageout errors cross the `maxFatalAsoNumber` / `RelativeFraction` /
`AbsoluteFraction` thresholds, and mails the operators about it. That path is
running in production and is **not changed here**. This PR adds the end-user half
of #9419: the same event is reported to the task owner, addressed to the
`CRAB_UserEmail` classAd.

### What changes
- **`config.TaskWorker.maxFatalAsoSendUserMail`** (new, default `False`) is a
  safety lock for the user notification:
  - `False`: the mail is only written to the PostJob log as
    `Firing email: <address>` followed by subject and body. Nothing reaches the Mail Transfer Agent (MTA).
  - `True`: it is handed to `/usr/bin/mail`, same transport as the operators mail.
  It can be flipped back at any time should users turn out to be flooded.
- **`sendMaxFatalAsoMailToUser(killed)`**: builds a user-worded message
  (different text when the task was really killed vs. left running in dry run),
  including the same ASO summary as the operators mail and the `FEEDBACKMAIL`
  address for help.
- **`getUserEmailFromAd()`**: tolerates both
- counting ASO `userMailSent` separately from Operator's `mailSent`. 

Refs #9419 (mail-sending mechanism), builds on #9422 (`CRAB_UserEmail` classAd from CRIC).

## Comment (cmsdmwmbot, 2026-09-26T12:49:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 290 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2926/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-09-26T19:42:16Z)

I’ve been trying to trigger the numErrors > 100, maxFatalASORelative: 0.5, and maxFatalASOAbsolute: 0.1 conditions in an E2E test manner submit 1000-jobs task, but still no luck.

The following were ideas that i've tried. otherwise i may need to do manual intervening during ASO through DB query or try quickly mockingly modify `aso_summary.json` at the moment it crossed to ASO transferring phase[?]

1. try to enforce quicker than usual ASOTimeout.
```bash
config.Debug.extraJDL = [
    '+CRAB_RetryOnASOFailures=0',
    '+CRAB_ASOTimeout=900'
]
```

2. Write on RSE that i have no permission but can't find way to bypass `SUBMITREFUSED`.
```
config.Site.storageSite = 'T2_IT_Rome_User'
``` 

3. Submit task to extremely Flaky Site like Vanderbilt, but mostly got 8901: Unexpected Job Terminated executable failures instead.
```
Rucio client intialized for account kphornsi
CRAB project directory:         /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-ASOTimeout-4-T2_US_Vanderbilt
Task name:                      260926_161418:kphornsi_crab_test-force-maxASO-1000-jobs-failures-by-ASOTimeout-4-T2_US_Vanderbilt
Grid scheduler - Task Worker:   crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:      SUBMITTED
Task URL to use for HELP:       https://cmsweb-test14.cern.ch/crabserver/ui/task/260926_161418%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-ASOTimeout-4-T2_US_Vanderbilt
Dashboard monitoring URL:       https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=260926_161418%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-ASOTimeout-4-T2_US_Vanderbilt&from=1790435658000&to=now
Status on the scheduler:        RUNNING

Jobs status:                    failed                    1.2% (  12/1000)
                                running                   1.6% (  16/1000)
                                transferring             97.2% ( 972/1000)

No publication information (publication has been disabled in the CRAB configuration file)

Error Summary: (use crab status --verboseErrors for details about the errors)

  12 jobs failed with exit code 8901
 ````

4. Fill my own space quota in T3_CH_CERNBOX up-to almost 1 TB, before submit, then quickly filled the destination site space in EOS to force massive ASO Failures `507 Insufficient Storage` or `Permissions Defined (Quota)`. (this way is the most promising one but i missed and already filled up so need to wait for quota to be reclaimed.`
```bash
e-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6
Dashboard monitoring URL:       https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=260926_192609%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6&from=1790447169000&to=now
Log file is /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6/crab.log
<b_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6
Rucio client intialized for account kphornsi
CRAB project directory:         /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6
Task name:                      260926_192609:kphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6
Grid scheduler - Task Worker:   crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:      SUBMITREFUSED
Task URL to use for HELP:       https://cmsweb-test14.cern.ch/crabserver/ui/task/260926_192609%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6
Dashboard monitoring URL:       https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=260926_192609%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6&from=1790447169000&to=now
Warning:                        Not enough Rucio quota at T3_CH_CERNBOX:/store/user/rucio/kphornsi. Remain quota: 0 GB.
Log file is /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-6/crab.log
```

I will comeback and try again tomorrow.

## Comment (nausikt, 2026-09-26T19:46:52Z)

Any known tips/ideas on how to do ASO failures triggering or by passing `SUBMITREFUSED` would be much appreciate!

## Comment (nausikt, 2026-09-27T08:29:46Z)

Rucio quota at `T3_CH_CERNBOX` didn't recovered yet even a day has passed.
```
[kphornsi@lxplus9114 maxFatalASOtesting]$ du -sh /eos/user/k/kphornsi/
922G    /eos/user/k/kphornsi/

<b_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9
Rucio client intialized for account kphornsi
CRAB project directory:         /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9
Task name:                      260927_081406:kphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9
Grid scheduler - Task Worker:   crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:      SUBMITREFUSED
Task URL to use for HELP:       https://cmsweb-test14.cern.ch/crabserver/ui/task/260927_081406%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9
Dashboard monitoring URL:       https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=260927_081406%3Akphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9&from=1790493246000&to=now
Warning:                        Not enough Rucio quota at 

T3_CH_CERNBOX:/store/user/rucio/kphornsi. Remain quota: 0 GB.
Log file is /tmp/crabStatusTracking/crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-9/crab.log
```

I have to try it the other way around.

## Comment (belforte, 2026-09-27T09:47:03Z)

looking for this ?
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/479/diffs?commit_id=afd8299650aefd9d1d297326ad4b0ad82662d775

Then you can make ASO succeed/fail by simply changing destination site

## Comment (nausikt, 2026-09-27T09:48:06Z)

Arhhhh, Thank you!

## Comment (belforte, 2026-09-27T09:48:37Z)

besides: **nobody has Rucio quota on CERNBOX** !!!
If you want to write to CERNBOX you must use normal ASO.

In any case ASO-Rucio is not really used now, please test with what it is used.

## Comment (nausikt, 2026-09-27T09:51:00Z)

My bad i forgot to commented out `config.Data.outLFNDirBase = '/store/user/rucio/kphornsi'` when try to test with `config.Site.storageSite = 'T2_IT_Rome_User'` back then.

## Comment (nausikt, 2026-09-27T11:27:47Z)

Tested when `config.TaskWorker.maxFatalAsoSendUserMail = False`, No noise to the users. [1,2,3]

[1] Just one PostJob log (253), fired a single email well, with no duplicates or race.
```bash
[kphornsi@vocms059 SPOOL_DIR]$ rg Firing
rg: _condor_stderr: Permission denied (os error 13)
postjob.253.0.txt
108:Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob Firing email: [krittin.phornsiricharoenphant@cern.ch](mailto:krittin.phornsiricharoenphant@cern.ch)
rg: 79a291b03989fb066c157fd21774457c4e2360fa: Permission denied (os error 13)
rg: _condor_stdout: Permission denied (os error 13)
```
[2] Full Example email to the user, all ASO failures criterias... numErrors > 100, relative > 50%, absolute > 10% were met well at the moment tripped. 
```bash
Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob Mail sent to operators about task killing
Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob Firing email: [krittin.phornsiricharoenphant@cern.ch](mailto:krittin.phornsiricharoenphant@cern.ch)
Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob   subject: CRAB task 260927_102804:kphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-12-disabled-check-stageout: too many stageout failures
Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob   body:
Dear kphornsi,

your CRAB task
  260927_102804:kphornsi_crab_test-force-maxASO-1000-jobs-failures-by-fill-krittin-personal-CERNBOX-eos-12-disabled-check-stageout
has too many output files which could not be transferred to T2_DE_DESY.
CRAB would normally kill the task in this situation, but it was left running.

Please make sure that your destination site is healthy and that you have
enough free disk space there before submitting again.

For reference, the failure was detected in PostJob for crabId 253.0.
Jobs in task : 1000
ASO summary:
 Relative
   OK    0/102 = 0%
   FAIL  102/102 = 100%
 Absolute
   OK    0/1000 = 0%
   FAIL  102/1000 = 10%

If you need help, please send an e-mail to [cmstalk+computing-tools@dovecotmta.cern.ch.](mailto:cmstalk+computing-tools@dovecotmta.cern.ch.)
Sun, 27 Sep 2026 13:01:20 CEST(+0200):INFO:PostJob maxFatalAsoSendUserMail is False: user mail NOT sent, only logged
```
[3] CRAB task massively failed as expected.
<img width="984" height="811" alt="Screenshot 2026-09-27 at 13 08 54" src="https://github.com/user-attachments/assets/51459788-b9d9-41eb-904f-394fe2c07916" />

## Comment (nausikt, 2026-09-27T12:01:20Z)

Tested when `config.TaskWorker.maxFatalAsoSendUserMail = True`, email was sent well to the user (me)!

[1] We got dry-run user-specific email to the ASO-failures task fine.
<img width="853" height="420" alt="Screenshot 2026-09-27 at 13 59 24" src="https://github.com/user-attachments/assets/489686c5-2c1b-4836-a9ef-4d7b296e984f" />

## Comment (belforte, 2026-09-29T15:09:48Z)

Thanks. I am curious, did you write the nice summary at the top, or was it AI-generated ? I think I should do the same with my PR'a !

## Comment (nausikt, 2026-09-29T15:17:49Z)

Forgive me, it definitely is AI-generated but i did checks na.

## Comment (belforte, 2026-09-29T15:35:30Z)

There's nothing to forgive. Well done. Can you teach me how do it ? (not via comments here, of course).

## Comment (nausikt, 2026-09-29T15:50:28Z)

Sure Stefano! let's revise/equip you with some AI agentic workflow for your next decade career. LoL (if you still have fun and not too tired of Analysis, newWMS stuffs) 

P.S. possibly be November or Dec.

## Comment (cmsdmwmbot, 2026-09-30T11:16:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 287 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2928/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-09-30T11:23:37Z)

I had no objections with all thoughtful review by Stefano since yesterday.

Now, we're testing in another branch on test14, will re-request review once this refactoring has no issues.

## Comment (belforte, 2026-10-01T15:58:30Z)

looks good now. Let's merge

## Comment (belforte, 2026-10-01T15:58:49Z)

I am eager to try it !

## Comment (nausikt, 2026-10-01T16:05:56Z)

LoL, here you go!
