# dmwm/CRABServer pull request #8352: attempt to streamline parent file discovery

State: closed
Opened: 2024-04-24T13:46:16Z
Closed: 2024-04-25T22:28:31Z
Merged: 2024-04-25T22:28:31Z
URL: https://github.com/dmwm/CRABServer/pull/8352

## Opening post (davidlange6, 2024-04-24T13:46:16Z)

After a bit of discussion with @belforte , this is some untested code that shoudl considerably reduce the time spent in checking for overlapping lumis when looking for secondary files.

## Comment (cmsdmwmbot, 2024-04-24T13:47:01Z)

Can one of the admins verify this patch?

## Comment (belforte, 2024-04-24T20:43:01Z)

To get a baseline, I timed the use case which gave origin to this https://cms-talk.web.cern.ch/t/crab-task-queued-on-command-submit-for-a-while/39714  i.e.
primary dataset: `/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_postEE_v1-v2/MINIAODSIM`
secondary dataset: `/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v2/AODSIM`

primary dataset has 6833 files, secondary dataset has 31962 files
code is like
```python
for file in primary:  # loop 1
  for file in secondary:  # loop 2
    find parents by matching lumis
```
I found that each iteration of loop1 takes 15~20 seconds. Of course I killed after a few tens of iterations but all files should be pretty similar.

For a total of the order of 30 hours.
(maybe I should have let that task run :grin:  !

## Comment (belforte, 2024-04-24T21:10:59Z)

With new code (from this PR) time for each iteration went down to 0.15~0.20 seconds. A neat x100 improvement.
Looking forward to a "reasonable" 20 minutes for the whole match.

:bowing_man: 

Onward to validation

## Comment (belforte, 2024-04-25T22:28:12Z)

I tested on 
primary:        /DoubleMuon/Run2018B-02Apr2020-v1/NANOAOD
secondary:   /DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD

and got identical results
