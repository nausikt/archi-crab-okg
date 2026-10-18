# dmwm/CRABServer pull request #8581: bump wmcore to 2.3.3 in pypi images and add deprecate notice to requirements.txt

State: closed
Opened: 2024-08-02T15:28:33Z
Closed: 2024-08-02T15:52:58Z
Merged: 2024-08-02T15:52:58Z
URL: https://github.com/dmwm/CRABServer/pull/8581

## Opening post (novicecpp, 2024-08-02T15:28:33Z)

(no text)

## Comment (cmsdmwmbot, 2024-08-02T15:30:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2080/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-02T15:35:29Z)

why deprecatio msg in  old requirements.txt ? rpm build is broken anyhow.
Anyhow a comment it is surely harmless. Go ahead

## Comment (novicecpp, 2024-08-02T15:42:03Z)

Can I delete it?

## Comment (belforte, 2024-08-02T15:51:28Z)

i'd do that only as part of the cleanup of all rpm-build stuff. Just merge this
