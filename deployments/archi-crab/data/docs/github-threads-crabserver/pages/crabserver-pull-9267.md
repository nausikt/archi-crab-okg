# dmwm/CRABServer pull request #9267: remove config examples now in puppet.

State: closed
Opened: 2026-01-21T14:18:24Z
Closed: 2026-01-23T13:45:30Z
Merged: 2026-01-23T13:45:30Z
URL: https://github.com/dmwm/CRABServer/pull/9267

## Opening post (belforte, 2026-01-21T14:18:24Z)

Since a few years TW and Pub configuration are built from puppet ERB templates
There is no point in having python examples in here, as they only risk being obsolete.

## Comment (belforte, 2026-01-21T14:20:39Z)

@nausikt also the CRABServer REST configuraions in https://github.com/dmwm/CRABServer/tree/master/src/script/Deployment/REST are obsolete since we now deploy them as secrets. But since you are changing that part I am not sure if we still need them in GitHub in some form or not. So I leave it to you to reorganize.

## Comment (cmsdmwmbot, 2026-01-21T14:21:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2722/artifact/artifacts/PullRequestReport.html
