# dmwm/CRABServer issue #9336: PostJob messes up input file accounting when input LFN contains '//'

State: closed
Opened: 2026-06-28T11:15:09Z
Closed: 2026-06-30T09:32:39Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9336

## Opening post (belforte, 2026-06-28T11:15:09Z)

See https://github.com/dmwm/CRABClient/issues/5427

More in general, apparently when  input file validation fails PJ creates a dummy name unique for all jobs. This makes no sense and must be avoided.

## Comment (belforte, 2026-06-28T15:24:42Z)

relevant lines
https://github.com/dmwm/CRABServer/blob/b5ea08b82ec0e58ed656a5650673ef2ef951251e/src/python/TaskWorker/Actions/PostJob.py#L2427-L2430

as  Kiril pointed out, at the very least the LFN should be unique (i.e. have job # in the suffix) so that counting is correct.
Same two lines above in case there is no input file.

## Comment (belforte, 2026-06-29T06:21:57Z)

I am not sure what to do in case of no input file in the FJR. How can we count read files and events in this case ?

## Comment (belforte, 2026-06-29T09:04:30Z)

looking in code history, the use of DummyLFN in case an input LFN is missing in the FJR was introduced with https://github.com/dmwm/CRABServer/issues/5171
So it was not really thought over in detail. The most likely use case leading to this that I can think of is users running some non-CMSSW script and providing their owm FJR, in which case we can't make any assumption on what's in the FJR,
e.g. it may be used simply to pass an exit code to the job.
If there's no input information in FJR we can not count number of input events anyhow, nor can tell how many files were processed by the job. So I am sticking with a common `DummyLFN`, when users see
```text
  Number of files processed: 1
  Number of events read: 0
```
they will realize that those lines must be ignored. I will look into improving crab client to print `n/a` or similar.

## Comment (belforte, 2026-06-29T09:16:32Z)

I tested with a config. similar to what  Kiril reported in https://github.com/dmwm/CRABClient/issues/5427, i.e. process a list of files with an extra `/` so cmsRun works but input LFN is rejected by Lexicon. 2 jobs, 2 files per job.

With the change in the commit, crab report changes from
```text
Summary from successful jobs (i.e. in status 'finished'):
  Number of files processed: 1
  Number of events read: 39600
  Number of events written in EDM files: 87600
```
to

```text
Summary from successful jobs (i.e. in status 'finished'):
  Number of files processed: 4
  Number of events read: 85200
  Number of events written in EDM files: 85200
```
note how not only the number of files is corrected, but also number of events read/written is consistent (and consistent with what can be derived by looking at FJR's)
