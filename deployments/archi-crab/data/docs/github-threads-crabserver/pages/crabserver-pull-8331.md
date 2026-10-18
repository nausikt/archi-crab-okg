# dmwm/CRABServer pull request #8331: stop using AuthenticatedSubprocess. Fix #8277

State: closed
Opened: 2024-04-11T16:13:58Z
Closed: 2024-04-12T11:00:42Z
Merged: 2024-04-12T11:00:42Z
URL: https://github.com/dmwm/CRABServer/pull/8331

## Opening post (belforte, 2024-04-11T16:13:58Z)

(no text)

## Comment (belforte, 2024-04-11T16:16:55Z)

@novicecpp this should allow you to test submission with new htcondor bindings #8272 

Up to you if to use my branch or we merge in master. I gave it a round of test (submit/kill/resubmit) on crab-dev-tw01 and it worked.

## Comment (cmsdmwmbot, 2024-04-11T16:18:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 2 warnings
   * 69 comments to review
 * Pycodestyle check: succeeded
   * 141 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1935/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-04-11T16:19:49Z)

Thanks Stefano. Merge to master is better. It is easier for me to rebase/merge to the branch I use to test.
I will review tomorrow. Need to go now.

## Comment (cmsdmwmbot, 2024-04-11T16:26:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 2 warnings
   * 82 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1936/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T16:28:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 2 warnings
   * 82 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1937/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T16:30:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 2 warnings
   * 82 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1938/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T20:53:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 1 warnings
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 147 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1939/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T21:10:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 1 warnings
   * 24 comments to review
 * Pycodestyle check: succeeded
   * 138 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1940/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T21:12:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 1 warnings
   * 24 comments to review
 * Pycodestyle check: succeeded
   * 138 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1941/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T21:24:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 24 comments to review
 * Pycodestyle check: succeeded
   * 138 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1942/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-11T21:46:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 136 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1943/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-04-12T09:38:21Z)

thanks for detailed reading.  I will go through your comments.
FWIW I just tested this again with submit/kill/resubmit and automatic splitting after the rather extensive changes for pylint.

## Comment (belforte, 2024-04-12T09:46:43Z)

I am not sure that is worth for you to read about HTCondor binging now, anyhow documentation is in https://htcondor.readthedocs.io/en/latest/apis/python-bindings/index.html

And I am indeed afraid that I did not test all possible errors, hopefully having try/except around calls to schedd will suffice. But experience always is that such things need to be run for months to be smoothed out. It is always the same problem with changes at the core. Current code works smoothly thanks to many years in operations where everything which could possibly go wrong, did it. And it was taken care of. Yet, sometimes change is needed.

hmm.. now that we saw submission break for migrate scheduler by having wrong ownernship in condor spool, we can try to do that on vocms059 and make sure that it gets reported.
I will do it.

## Comment (belforte, 2024-04-12T10:53:17Z)

@novicecpp please close the comments where you are satisfied with the answer and let me know if something is still not clear. Yeah.. this is very difficult code to read. Took me a while to feel confident about what I was doing, but decided that it was better to take this chance to do also a bit or review and cleanup, not simply replace AuthenticatedSubprocess with another context manager with simply new authentication parameters

## Comment (belforte, 2024-04-12T11:00:36Z)

thanks Wa !!!
