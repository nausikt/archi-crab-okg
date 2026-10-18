# dmwm/CRABServer issue #9356: Ensure that input files can be opened before starting user application

State: open
Opened: 2026-07-20T14:39:37Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/9356

## Opening post (belforte, 2026-07-20T14:39:37Z)

Need to use cmsRun in order to have proper handling of LFN to PFN, redirector fallback etc.

## Comment (belforte, 2026-07-27T10:34:50Z)

looks like this should do
`cmsRun dummyPSet.py`
where `dummyPSet.py` is
```python

import FWCore.ParameterSet.Config as cms

process = cms.Process('Dummy')

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
'/store/[...].root'
                                                                           )                           )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

```

## Comment (belforte, 2026-08-24T16:16:34Z)

OTOH, so far it looks that this happens in significant number only when user select IgnoreLocality !
https://cms-talk.web.cern.ch/t/wasted-cpu-time-corehours-in-crab/147739/10?u=belforte

At least as far as "if happens in the middle of the run and wastes a lot of CPU".

So let's put it aside until we know more/better.
