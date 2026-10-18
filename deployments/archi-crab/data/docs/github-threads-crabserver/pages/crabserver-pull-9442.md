# dmwm/CRABServer pull request #9442: fix #9441

State: open
Opened: 2026-10-14T10:45:52Z
URL: https://github.com/dmwm/CRABServer/pull/9442

## Opening post (belforte, 2026-10-14T10:45:52Z)

(no text)

## Comment (belforte, 2026-10-14T10:47:30Z)

@nausikt myself and you are sharing fault here, since you approved the ill fated PR. So I kindly ask you to check again because bash conditionals are tricky for me and I am not confident that I did it right this time.

## Comment (cmsdmwmbot, 2026-10-14T10:49:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2932/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-10-14T17:13:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2933/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-10-14T19:18:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2934/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-10-14T19:40:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2935/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-10-14T20:36:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2936/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-10-14T21:02:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2937/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-10-14T21:03:03Z)

Acknowledged Stefano.

## Comment (cmsdmwmbot, 2026-10-14T21:04:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2938/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-10-14T21:17:07Z)

I have added two committs which are further improvements, but do not directly address #9441 
The second one is tricky since to understand it one needs to dissect how things are passed around with files and e.g. jobReport.json vs. job_fjr.json... took me several iterations to get it right
