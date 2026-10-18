# dmwm/CRABServer issue #8892: restructure DagmanCreator and DagmanSubmitter

State: closed
Opened: 2025-01-23T16:28:38Z
Closed: 2025-01-30T16:24:31Z
Labels: Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8892

## Opening post (belforte, 2025-01-23T16:28:38Z)

after the changes for `input_args.json` in #8883 there is a a large amount of confusion and now-obsolete code in DagmanCreator

Take this chance to restructure and cleanup.
Main goals

- [x] stop using `info` dictionary everywhere to mean different things
- [x] instead of `JOB_SUBMIT` string and format where one needs to look in 3 or fours places to find out what goes in 'Job.submit' file, use an `htcondor.Submit()` object and `classad.quote()` and avoid as much as possible ad-hoc, unexplained, string manipulations
- [x] simplify and clarify what information is really needed to submit the DAG bootstrap job and rework the informaiton transfer from DagmanCreator to DagmanSubmitter. Ideally pass an `htcondor.Submit()` object with the classAds common to boths submissions, which DagmanSubmitter will extend as needed
- [x] address small "historical" differences and oddities in other parts of the code which rely/require specific ads with non-standard syntax/values

## Comment (belforte, 2025-01-23T16:30:39Z)

evolving code in my branch https://github.com/belforte/CRABServer/tree/CleanupAfterSwitchTo-input_args

so far I have a new DagmanSubmitter which reproduces current Job.submit file in a simple test task.
Next step is to work on communication with DagmanSubmitter

The try all tasks

## Comment (belforte, 2025-01-27T20:23:06Z)

That branch is now able to submit a simple task.
Still need to worry about DagmanResubmitter.

first taks which succeeded: https://cmsweb-test2.cern.ch/crabserver/ui/task/250127_195607%3Abelforte_crab_20250127_205602
