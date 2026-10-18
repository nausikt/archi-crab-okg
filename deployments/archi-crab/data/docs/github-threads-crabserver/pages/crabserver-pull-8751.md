# dmwm/CRABServer pull request #8751: Spelling and missing 'not' in exception message

State: closed
Opened: 2024-10-29T01:50:51Z
Closed: 2024-10-29T08:18:07Z
Merged: 2024-10-29T08:18:07Z
URL: https://github.com/dmwm/CRABServer/pull/8751

## Opening post (oljemark, 2024-10-29T01:50:51Z)

Exception message accidentally positive

## Comment (cmsdmwmbot, 2024-10-29T01:52:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 37 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2223/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-29T08:17:33Z)

thanks @oljemark for spotting and fixing. I am a bit surprised that you have stumbled on the "could not expand tarball with debug files". It should "never" happen and it may point to a problem somewhere. If you have information on why it happened, or any hint that something may be wrong in the code, please feel free to share.

## Comment (oljemark, 2024-10-29T08:19:57Z)

Hi @belforte . No, I was just looking through the code changes of the last few months, I didn't see the exception triggered.

## Comment (belforte, 2024-10-29T08:35:37Z)

I see. WOW !! Thanks again for excellent review !!!!!!!!!!
