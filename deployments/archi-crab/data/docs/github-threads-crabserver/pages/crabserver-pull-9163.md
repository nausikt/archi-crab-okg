# dmwm/CRABServer pull request #9163: atomic update crabserver image to sidecar repo script, ci-bot for aut…

State: closed
Opened: 2025-08-27T22:40:46Z
Closed: 2025-08-27T22:45:47Z
Merged: 2025-08-27T22:45:47Z
URL: https://github.com/dmwm/CRABServer/pull/9163

## Opening post (nausikt, 2025-08-27T22:40:46Z)

Regarding #9152 

Here is CI for bumping image tag in crab-iac sidecar repo. 

I've wildcard its for only test14 such that i can do e2e testing in our core CI/CD pipeline. also already test the main script locally.

So, please allow me to merge to master, such that i could jumped into testing right away, will let you guys know and patched asap na. (Otherwise i've to forked new branch)

Edited: It's works now i've fixed it in #9164, Thank you for your kind understanding on quick merged testing!

## Comment (cmsdmwmbot, 2025-08-27T22:43:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2586/artifact/artifacts/PullRequestReport.html
