# dmwm/CRABServer pull request #9415: Split fatal Application segfaults out of 50115 as 50117.

State: closed
Opened: 2026-09-09T15:14:45Z
Closed: 2026-09-28T17:02:30Z
Merged: 2026-09-28T17:02:29Z
URL: https://github.com/dmwm/CRABServer/pull/9415

## Opening post (nausikt, 2026-09-09T15:14:45Z)

(partially) resolves #9357

## Background

50115 currently means "cmsRun did not produce a valid job report" and is retried three times with a 1.3× memory bump. A survey of 1000 tasks that hit 50115 between 2026-08-04 and 2026-08-30 shows the code covers two populations:
 | tasks | behaviour
-- | -- | --
never succeeded after retries | 262 (26.2%) | retries are pure waste
≥80% of failures were 50115, all eventually succeeded | 565 (56.5%) | retries work as intended

TWiki JobExitCode also already confirm/admits the ambiguity that 50115 "often means cmsRun segfaulted". 

## This PR includes
It resolves the subset we can identify with confidence: 

A segmentation violation that happened **after the event loop started** which may due to user code error or misconfigurations. 
> These are relabelled as 50117 fail-fast and not retried. Everything else remains the current 50115 behaviour.

Users get a faster feedback loop on their own crashes, and the grid stops running three copies of a job that cannot succeed.

## Twiki JobExitCodes

50115 — cmsRun did not produce a valid job report at runtime (cause undetermined; retried)
**50117 — cmsRun terminated with a segmentation violation after processing began (not retried)**

## Why CPU seconds, not wall clock
*Claude opus raised, well recommended us to use Cpu time*
A job stalled on sick CVMFS or a hung xrootd read accumulates wall time while burning almost no CPU — a wall-clock gate would misclassify exactly the transient population this PR is trying to protect. Since 50115 means there is no FJR, the classad (RemoteUserCpu + RemoteSysCpu) is the only available source.

The **SEGFAULT_CPU_THRESHOLD** should be safe threshold and derived from the **survey data of 262 workflows**

## Things will follow up on another PR

New codes for the 565-task transient population. Their behaviour is already correct; new codes there buy monitoring granularity only, and every published code is a permanent commitment in user-facing docs. Revisit once the log patterns are proven.

## Comment (cmsdmwmbot, 2026-09-09T15:17:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2917/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-09-09T15:18:13Z)

This is a draft PR and not tested yet. Let me back to you when completely sure na.

## Comment (belforte, 2026-09-09T20:51:55Z)

I slightly changed the message https://github.com/dmwm/CRABServer/pull/9415/commits/ac99496f2da2cc36ced3904a8636e76af6408be9

## Comment (cmsdmwmbot, 2026-09-09T20:53:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2919/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-09-27T12:34:05Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 20 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2927/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-09-28T16:34:17Z)

LGTM. Thanks
