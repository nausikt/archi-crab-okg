# dmwm/CRABClient issue #5414: Improve how we initialize vocmshtcondor

State: closed
Opened: 2025-09-16T10:39:51Z
Closed: 2025-09-16T10:42:38Z
Labels: Low Priority, CleanUp
URL: https://github.com/dmwm/CRABClient/issues/5414

## Opening post (nausikt, 2025-09-16T10:39:51Z)

As we have picked up feedback from SI team today, DMWM workshop meeting.

Florian have kindly suggested us, on how can we improved the way we initialize `vocmshtcondor`.

As we can see here in [ai/it-puppet-hostgroup-vocmsglidein /code/manifests/modules/condor.pp](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/manifests/modules/condor.pp?ref_type=heads). 

Right now, we initialize each module by hand,  so we might not properly initialize all other sub-modules around, 

*Solution*: the better way is CRAB can safely relied on `SI` initialization ([(upstream) ai/it-puppet-module-vocmshtcondor init.pp](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/blob/qa/code/manifests/init.pp?ref_type=heads)) by just `include vocmshtcondor`.

but surely we have to do a lot of tests to check whether this way breaks things. So it's not that urgent but worth well noted. Since this way can keep CRAB and SI aligned better.

## Comment (nausikt, 2025-09-16T10:42:38Z)

My bad i will open it on CRABServer repo.
