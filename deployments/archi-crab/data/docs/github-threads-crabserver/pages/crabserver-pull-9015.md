# dmwm/CRABServer pull request #9015: Add status.sh

State: closed
Opened: 2025-03-24T16:50:54Z
Closed: 2025-03-27T11:16:59Z
Merged: 2025-03-27T11:16:59Z
URL: https://github.com/dmwm/CRABServer/pull/9015

## Opening post (belforte, 2025-03-24T16:50:54Z)

Wa added `status` to possible commands long ago.
This is long due addition of a script to execute them, sort of to remind us that they exists !
I took this chance to also add printing of the running version.

## Comment (cmsdmwmbot, 2025-03-24T16:53:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2404/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-26T15:27:35Z)

thanks Vijay.  Agreed

## Comment (belforte, 2025-03-26T15:32:55Z)

yeah... I was a bit lazy

## Comment (belforte, 2025-03-26T15:35:36Z)

I took this chance to add this also for Publisher.

## Comment (cmsdmwmbot, 2025-03-26T15:37:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2405/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-26T15:52:49Z)

anyhow, let's build and test, to make sure I did not slip a bash syntax error in which breaks everthing. I will and report here.

## Comment (belforte, 2025-03-26T20:11:53Z)

it looks like I broke something
```
[crab3@crab-dev-tw01 belforte]$ docker logs Publisher_schedd
/data/srv/Publisher /data/srv/Publisher
/data/run.sh: line 52: ./manage.py: No such file or directory
[crab3@crab-dev-tw01 belforte]$ 
```

## Comment (cmsdmwmbot, 2025-03-27T10:04:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2406/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-03-27T10:04:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2407/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-03-27T10:51:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2408/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-27T10:54:40Z)

@aspiringmind-code  fixed, squashed, tested. Ready for final review
