# dmwm/CRABServer issue #9213: Fix Status Tracking job in gitlab pipeline with CMSSW release versions under 12

State: closed
Opened: 2025-10-13T06:50:18Z
Closed: 2026-04-07T10:48:52Z
URL: https://github.com/dmwm/CRABServer/issues/9213

## Opening post (aspiringmind-code, 2025-10-13T06:50:18Z)

For example see in[ Pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/commit/64effab1c9f11e12b4de84e47100709c27a62501)

## Comment (belforte, 2025-10-13T08:14:50Z)

looks like we are using sl7 scram arch in an sl9 container. When checking task status, any version of CMSSW/client will do, using the proper scram arch should be limited to submission, where we switch to the ad-hoc apptainer.

## Comment (belforte, 2026-02-24T14:19:06Z)

@aspiringmind-code 
That solution does not work, see e.g. https://gitlab.cern.ch/crab3/CRABServer/-/jobs/70352581

We need either to change Client or stick with proven solution of using same, modern CMSSW release to run ST check script, which allows to stay with python3 in there, consistently with all the CRABServer code.
Let me know if you have time for this or prefer that I take it over now that you are busy with new WMS.

And by the way none of the ST checks in the pipeline pointed to in the PR #9268 completed successfully.  Seems that task submission failed. The pipeline is set to ignore failure and completed with a final OK. Which is not good and we need to fix, maybe was put as a temporary  kludge to get along when CMSSW<12 was faiing and stuck around, unfortunately there is no description of the rational in the PR https://github.com/dmwm/CRABServer/pull/9027.
**all** tests have `allow_failure: true` and it looks to me that nobody ever checks the ones which do not suceed.

Please Vijay be more careful in checking, you should have looked for positive confirmation that tests run without error.

We clearly need to revisit the way we declare the pipeline to be OK.

## Comment (belforte, 2026-02-24T15:46:52Z)

I also suspect that there is no way that 9 ST submissions complete within the currently allocated maximum time (200min?) see e.g. https://gitlab.cern.ch/crab3/CRABServer/-/jobs/70352578
I.e. we either run a limited (CCV) test, or there is no way that the full test can be successful.

## Comment (belforte, 2026-03-02T17:51:22Z)

I 'll make this part of a larger and long due improvement to pipeline:
- add more recent CMSSW
- less verbose
- synoptic view of which tests failed/succeded
- remove useless old tests for things which never change
- reduce amount of tests for older CMSSW versions (no need to do full CCV matrix 10 times !)
- properly handle jobs still in running
- fix status tracking by going back to single CMSSW version in all scripts but submissions
- ...

## Comment (belforte, 2026-03-30T07:21:36Z)

addressed in #9287
