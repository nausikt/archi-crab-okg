# dmwm/CRABServer pull request #7503: allow tm_rest_(host|uri) values to be missing

State: closed
Opened: 2023-01-23T23:18:10Z
Closed: 2023-01-24T21:56:37Z
URL: https://github.com/dmwm/CRABServer/pull/7503

## Opening post (belforte, 2023-01-23T23:18:10Z)

consolidates in Create.py and updateOracle.sql changes already done in DB

## Comment (belforte, 2023-01-23T23:19:02Z)

@mapellidario this should be very harmless, but please  add your pair of eyes

## Comment (cmsdmwmbot, 2023-01-23T23:20:13Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1400/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-01-24T10:40:26Z)

Did you forget to commit the ~~latest~~ change?

## Comment (belforte, 2023-01-24T10:55:02Z)

thanks Wa. Yes, I did something wrong. Will review

## Comment (belforte, 2023-01-24T21:56:28Z)

everything was put already in master for what concerns "allow tm_rest_(host|uri) values to be missing". This PR is totally uses since only adds an extra blank line by mistakes.
Sorry for the noise. I somehow got confused when checking my local branches.
