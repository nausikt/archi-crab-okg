# dmwm/CRABServer pull request #9339: Make runner more robust

State: closed
Opened: 2026-07-02T14:09:24Z
Closed: 2026-07-03T19:15:14Z
Merged: 2026-07-03T19:15:14Z
URL: https://github.com/dmwm/CRABServer/pull/9339

## Opening post (belforte, 2026-07-02T14:09:24Z)

sometimes our pipeline test fails early in setup client with error like
```
gmake[1]: *** [config/SCRAM/GMake/Makefile.rules:1887: CompilePython] Error 1
gmake: *** [config/SCRAM/GMake/Makefile.rules:1753: src] Error 2
clientValidation.sh ended with exit code: 2
```
triggering a re-run by clicking in the pipeline gitlab UI usually fixes it.
I do not know what could cause it.

So let's try to re-run in the script and see if error goes away, also do w/o redirecting stdout to /dev/null in hope of hints, in case

## Comment (belforte, 2026-07-02T14:09:45Z)

oopsss... I need to rebase

## Comment (cmsdmwmbot, 2026-07-02T14:13:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2851/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-03T16:50:48Z)

rebased.

## Comment (cmsdmwmbot, 2026-07-03T16:54:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2852/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-07-03T19:15:08Z)

thanks Krittin for such a fast review

## Comment (belforte, 2026-07-03T19:16:01Z)

Note: this is effective immediately since pipeline takes scripts from `master`

## Comment (nausikt, 2026-07-03T20:04:27Z)

Acknowledged!
