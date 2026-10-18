# dmwm/CRABServer pull request #9137: add gpg+sops to crab/buildtools image.

State: closed
Opened: 2025-07-22T21:10:27Z
Closed: 2025-07-29T20:20:24Z
Merged: 2025-07-29T20:20:24Z
URL: https://github.com/dmwm/CRABServer/pull/9137

## Opening post (nausikt, 2025-07-22T21:10:27Z)

Keep crab/buildtools Dockerfile in sync.

## Comment (cmsdmwmbot, 2025-07-22T21:12:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2541/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2025-08-15T14:29:20Z)

sorry to chime in, did you test this? does it really work without explcitly installing [pinentry](https://packages.fedoraproject.org/pkgs/pinentry/pinentry/)? :)

## Comment (nausikt, 2025-08-15T15:13:27Z)

Thank you for chime in Dario! I've test in my [MR](https://gitlab.cern.ch/crab3/crab-secrets/-/merge_requests/4/diffs#587d266bb27a4dc3022bbed44dfa19849df3044c), it could be decrypt na.

May be i'm lucky in this case where i work with only non-passphrase gpg key. it seems mandatory for passphrase prompts in general as you mentioned.

Back then I've tried it with passphrase [here](https://gitlab.cern.ch/crab3/crab-secrets/-/merge_requests/4/diffs?commit_id=be75730b8ce365c42eb685d221d235be52868fa3) but i can't make it works, i do not find the way to importing key & passphrase simultaneously, also can't start agent with --batch and pinentry-mode loopback at the beginning of container life cycle (such that we can feed passphrase file directly to prompt in automated fashion) unless we kill agent once and start in new mode, but restarting it still can't make it work and there might be something i've missed😢. have you been through these before? please show me the way na.

## Comment (belforte, 2025-08-15T15:35:38Z)

HI Krittin, what does "na" means ? Sorry for my ignorance

## Comment (nausikt, 2025-08-15T15:38:01Z)

Sorry, it's Thai suffixes to soften things and sound gentler.

## Comment (belforte, 2025-08-15T16:04:52Z)

what about adding a comment in Dockerfile with something like "Note: this only works for gpg keys w/o passphrase" ?

## Comment (nausikt, 2025-08-15T16:17:16Z)

How about install `pinentry` to make our image more generic for the future as Dario's hint?

## Comment (belforte, 2025-08-15T16:19:54Z)

if it works, sure.
