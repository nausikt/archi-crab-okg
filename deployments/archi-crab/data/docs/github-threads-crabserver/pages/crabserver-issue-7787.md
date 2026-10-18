# dmwm/CRABServer issue #7787: jenkins PR check - failed with manual trigger

State: closed
Opened: 2023-07-26T15:34:55Z
Closed: 2024-08-23T10:02:30Z
Labels: Priority: Medium, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7787

## Opening post (mapellidario, 2023-07-26T15:34:55Z)

I manually triggered a jenkins check on the PR #7759 and  the jenkins job failed. I will need to

The relevant builds (which I marked such that they are kept forever) are

- ✅ (prerequisite, pylint) https://cmssdt.cern.ch/dmwm-jenkins/job/DMWM-CRABServer-PR-pylintpy3/377/
- ⛔ (pylint output parser) https://cmssdt.cern.ch/dmwm-jenkins/job/DMWM-CRABServer-PR-test/1632/

## Comment (belforte, 2024-08-23T10:02:30Z)

we stop using this
