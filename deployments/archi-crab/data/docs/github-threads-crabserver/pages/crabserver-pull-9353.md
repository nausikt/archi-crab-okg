# dmwm/CRABServer pull request #9353: Some pep8 whitespace fixes to be consistent with nearby lines, and br…

State: closed
Opened: 2026-07-17T12:20:15Z
Closed: 2026-07-17T13:00:26Z
Merged: 2026-07-17T13:00:26Z
URL: https://github.com/dmwm/CRABServer/pull/9353

## Opening post (oljemark, 2026-07-17T12:20:15Z)

…eak up a long message in two.

Hi, @belforte . I saw there were quite a lot of harmless code style suggestions, so I fixed a few of them (and probably added one or two where most of the lines where lined up along "=" with extra spaces). 

Pylint was already tamped down quite a lot for this older code, so do you want to keep the code strictly as-is, or are these changes ok?

## Comment (cmsdmwmbot, 2026-07-17T12:23:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 comments to review
 * Pycodestyle check: succeeded
   * 386 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2859/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-17T12:55:13Z)

thanks for your attention Frederick, but indeed cleaning up down to this level old code is definitely out of scope.
At least for me, risk of breaking something with a typo hugely wins over the pain of knowing that a list of PEP-8 comments is there. Of course major typos will be detected immediately, but if something slips in a rarely executed part of the code, we do not have a way to catch it until it becomes a problem in operations.

My guideline is to limit fixes to what makes for **bold** lines in pylint report. And indeed for old code which worked for years and I do not fully understand, I prefer to silence pylint unless the fix is trivial.

## Comment (belforte, 2026-07-17T12:59:44Z)

OTOH you also found and fixed wrong spaces in recent code changes which indeed should have been done better :-(
Thanks for catching those !
