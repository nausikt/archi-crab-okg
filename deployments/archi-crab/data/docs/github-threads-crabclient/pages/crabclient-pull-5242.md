# dmwm/CRABClient pull request #5242: avoid rucio setup getting confused by existing CMSSW stuff

State: closed
Opened: 2023-10-25T21:28:57Z
Closed: 2023-10-26T09:26:57Z
Merged: 2023-10-26T09:26:57Z
URL: https://github.com/dmwm/CRABClient/pull/5242

## Opening post (belforte, 2023-10-25T21:28:57Z)

if one has CMSSW setup for a different arch than the current machine (e.g. do cmsrel on SL7 and than run on SL8, which works) the `/cvmfs/cms.cern.ch/rucio/setup-py3.sh` will get confused and fail to resolve dependencies.
This PR makes sure that Rucio is setup in the pre-cmsenv environment.

## Comment (cmsdmwmbot, 2023-10-25T21:33:33Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/971/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-26T09:26:50Z)

well. this can surely only help and it is harmless. Let's merge so it will be tested by Jenkins
