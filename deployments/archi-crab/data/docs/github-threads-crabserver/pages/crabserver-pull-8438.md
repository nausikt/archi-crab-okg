# dmwm/CRABServer pull request #8438: add voms-clients-java to PyPI container. Fix #8437

State: closed
Opened: 2024-05-29T08:42:58Z
Closed: 2024-05-29T09:36:30Z
Merged: 2024-05-29T09:36:30Z
URL: https://github.com/dmwm/CRABServer/pull/8438

## Opening post (belforte, 2024-05-29T08:42:58Z)

(no text)

## Comment (novicecpp, 2024-05-29T08:45:54Z)

Are you sure `vocms-proxy-init` command is bound/symlink to Java version, not C++?

## Comment (cmsdmwmbot, 2024-05-29T08:47:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2002/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-29T08:53:06Z)

it did so in my test. Sort of "last install wins".  Otherwise we will need to play with `alternatives`.

## Comment (belforte, 2024-05-29T08:53:59Z)

hmm... maybe I can test this locally as an exercise. Do you want me to ?

## Comment (novicecpp, 2024-05-29T09:00:37Z)

"last install wins" is fine as long as it point to Java version.

A while ago when I started experimenting with PyPI, I installed both versions on a new image while reverse engineering the old image and I saw some inconsistencies. Sometimes it is point to C++ another times it is Java. Not 100% sure why or simply memory mixed up.

## Comment (belforte, 2024-05-29T09:04:08Z)

If I could remember the way to use alternatives we can explicitly enforce it there too. Of course easiest is that WMCore people update their image. But it is good that we can test w/o waiting

## Comment (belforte, 2024-05-29T09:36:26Z)

I built `StefanoHTC23-0529` with this and verified that voms client points to v3.
All OK.
