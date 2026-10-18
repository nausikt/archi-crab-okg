# dmwm/CRABServer pull request #9218: make function names compatile with our standard

State: closed
Opened: 2025-10-15T16:10:31Z
Closed: 2025-10-15T16:32:53Z
Merged: 2025-10-15T16:32:53Z
URL: https://github.com/dmwm/CRABServer/pull/9218

## Opening post (belforte, 2025-10-15T16:10:31Z)

also a couple other minor pylint fixes

## Comment (belforte, 2025-10-15T16:13:09Z)

Hi @nausikt  I wanted to reuse your very handy `safe_get` so decided to name it according to current camelCase standard as used in our pylint, to keep my chance "clean". Took this chance to do a few more pylint corrections.

Please make sure I did not screw up and that my added descriptions are not wrong .Thanks !

## Comment (cmsdmwmbot, 2025-10-15T16:25:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 4 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2661/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-10-15T16:28:52Z)

OMG, I didn't aware that we use camelCase for functions, apologize i assume we use PEP-8.

It's LGTM now. sorry for noises.

## Comment (belforte, 2025-10-15T16:32:49Z)

I didn't write those rule, but it is good be consistent across the CRAB code base, when we can. Thanks for reading so quickly

## Comment (belforte, 2025-10-15T16:37:51Z)

now we should use `sageGet` everywhere we have all those `if hasattr... then getattr...` ! but not now

## Comment (nausikt, 2025-10-15T16:39:18Z)

Thanks! for renaming man.
