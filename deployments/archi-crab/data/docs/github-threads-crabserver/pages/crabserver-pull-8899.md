# dmwm/CRABServer pull request #8899: CCV and TS testsuites fix

State: closed
Opened: 2025-01-29T14:56:57Z
Closed: 2025-01-30T10:31:54Z
Merged: 2025-01-30T10:31:54Z
URL: https://github.com/dmwm/CRABServer/pull/8899

## Opening post (aspiringmind-code, 2025-01-29T14:56:57Z)

Major changes include:
- Handling of return status 2 instead of exit in CCV
- Separating TS testing from CV and CCV
- Usage of return values from checkStatus function

## Comment (cmsdmwmbot, 2025-01-29T14:58:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 1 warnings
   * 162 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2355/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-29T20:40:15Z)

I am sorry Vijay, but I can't possibly go through all code differences and asses if changes to something that I did not fully understand before anyhow are correct. Let's put this in and try it out !
