# dmwm/CRABClient issue #5323: avoid comparing cms.uint32 with int

State: closed
Opened: 2024-07-11T13:31:08Z
Closed: 2024-07-11T20:48:22Z
URL: https://github.com/dmwm/CRABClient/issues/5323

## Opening post (belforte, 2024-07-11T13:31:08Z)

see discussion in https://cms-talk.web.cern.ch/t/how-to-run-crab-for-slc7-arch-on-an-el8-machine/42642/6

on pre-CMSSW_9 releases, comparing `cms.uint32` with `int` does not work, resulting in a spurious warning from
https://github.com/dmwm/CRABClient/blob/d17ff66a143d33d99d31c8f767c3cc75fdbceef8/src/python/CRABClient/JobType/CMSSWConfig.py#L298

recommended solution is to use `numPSetCores.value()` wich "eturns the underlying python native type, and is available in all CMSSW releases."
