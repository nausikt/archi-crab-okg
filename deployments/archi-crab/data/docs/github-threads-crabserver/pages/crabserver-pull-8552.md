# dmwm/CRABServer pull request #8552: Fix TW config section does not exist when hardcode some values in pdb mode

State: closed
Opened: 2024-07-23T10:38:05Z
Closed: 2024-07-23T10:41:21Z
Merged: 2024-07-23T10:41:21Z
URL: https://github.com/dmwm/CRABServer/pull/8552

## Opening post (novicecpp, 2024-07-23T10:38:05Z)

See https://mattermost.web.cern.ch/cms-o-and-c/pl/i3sp1q3hftbyjpu4qz7cp3asec

## Comment (cmsdmwmbot, 2024-07-23T10:40:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 9 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2055/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-23T13:27:23Z)

a bit of an overkill... a configuration file w/o the `TaskWorker` section will likely make things crash in many other places, nor we care to support it :-)
