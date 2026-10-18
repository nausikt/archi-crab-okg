# dmwm/CRABServer issue #9185: Improve how we initialize vocmshtcondor

State: open
Opened: 2025-09-16T10:44:00Z
Labels: Priority: Low, Area: HTCondor, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9185

## Opening post (nausikt, 2025-09-16T10:44:00Z)

As we have picked up feedback from SI team today, DMWM workshop meeting.

Florian have kindly suggested us, on how can we improved the way we initialize `vocmshtcondor`.

As we can see here in [ai/it-puppet-hostgroup-vocmsglidein /code/manifests/modules/condor.pp](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/manifests/modules/condor.pp?ref_type=heads). 

Right now, we initialize each module by hand,  so we might not properly initialize all other sub-modules around, 

*Solution*: the better way is CRAB can safely relied on `SI` initialization ([(upstream) ai/it-puppet-module-vocmshtcondor init.pp](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/blob/qa/code/manifests/init.pp?ref_type=heads)) by just `include vocmshtcondor`.

but surely we have to do a lot of tests to check whether this way breaks things. So it's not that urgent but worth well noted. Since this way can keep CRAB and SI aligned better.

## Comment (belforte, 2025-09-16T12:04:04Z)

I guess you want to create a test foreman environment first and put e.b. crab-sched-903 in there, just to work out the puppet syntax etc, them move to qa

## Comment (nausikt, 2025-09-16T12:14:05Z)

Q (from SI team): is there any specific reasons back then, that made crab machines set up this way?

## Comment (belforte, 2025-09-16T12:28:25Z)

No specific reason. Maybe at the time `vocmshtcondor` was structured differently. Maybe Prajhesh first and Wa next simply tried to cleanup something much more messy which was the original setup before SI splitted off in their own repository (Diego Davila times, I think), and they did it w/o consultation with SI, or the SI person at the time was not as good with puppet as Florian...
