# dmwm/CRABServer pull request #9288: Protect py3 from py2 module leakage in cmsenv during client validation and submission in CI/CD.

State: closed
Opened: 2026-03-30T10:53:44Z
Closed: 2026-03-30T13:02:52Z
URL: https://github.com/dmwm/CRABServer/pull/9288

## Opening post (nausikt, 2026-03-30T10:53:44Z)

Since, we lift the whole codebase into Alma9 and enforce py3 everywhere.

Our [CI/CD pipeline tests failed](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/72381752) because we run py3 inside cmsenv. So py2 module were leaking into py3 runtime.
*Specifically, when submit and try to makeTests ClientValidations test for CMSSW_9.*

## Comment (cmsdmwmbot, 2026-03-30T10:56:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2765/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-30T12:55:15Z)

this is taken care of in #9287 
In any cas. please let's refrain from working in parallel on same code w/o coordination, makes merging difficult.
You should have known that I have been changing ci/cd pipeline.

## Comment (nausikt, 2026-03-30T13:02:52Z)

Roger that Stefano.
