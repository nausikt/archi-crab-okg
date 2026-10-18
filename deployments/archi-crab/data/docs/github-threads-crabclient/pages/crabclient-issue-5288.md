# dmwm/CRABClient issue #5288: complete transitioning preparelocal to args via JSON

State: closed
Opened: 2024-01-30T21:09:18Z
Closed: 2025-02-27T09:17:00Z
Labels: enhancement, Done, HighPrio, CleanUp
URL: https://github.com/dmwm/CRABClient/issues/5288

## Opening post (belforte, 2024-01-30T21:09:18Z)

bulding up on #5276 and #5287 two things are needed in order to fully deprecated old code and remove it

- [x] make this use the JSON file. or deprecate it !! https://github.com/dmwm/CRABClient/blob/28add710e8594491093bc35b433294014302ac47/src/python/CRABClient/Commands/preparelocal.py#L89 
- [x] put all JSON files in a single tarball in and expand it e.g. in CMSRunAnalysis.sh so to preserve the possibility to submit jobs locally as per https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABPrepareLocal#HTCondor_submission (those instructions will need to be updates) 
   * alternatives
      * **have a single JSON file and pass the jobId to CMSRunAnalysis.py.** **It is the one I picked** I had played with this idea already for #5287 but I wanted to preserve an easy way to look a the arguments with `cat` when working interactively in the local directory.
      * Maybe make a tarball with the individual JSON and expand it in `run_job.sh` as done now for   `CMSRunAnalysis.tar.gz` ?

## Comment (belforte, 2024-11-07T12:07:23Z)

better do this now that I am fresh of "tarballs and preparelocal refactoring"
as per https://github.com/dmwm/CRABServer/issues/6544#issuecomment-2380693510

## Comment (belforte, 2025-01-08T10:37:28Z)

the single JSON file with all arguments is now prepared by DagmanCreator https://github.com/dmwm/CRABServer/blob/97e7e253fe35a2b0c2c02e88babd188737a39ece/src/python/TaskWorker/Actions/DagmanCreator.py#L704-L712
and is part of the `InputFiles.tar.gz` tarball which is prepared for every task and put in S3.

So the first step will be to use that file in CMSRunAnalysis.py passing to the script simple the jobId as argument instead of the current
`
Arguments = "-a $(CRAB_Archive) --sourceURL=$(CRAB_ISB) --jobNumber=$(CRAB_Id) --cmsswVersion=$(CRAB_JobSW) --scramArch=$(CRAB_JobArch) '--inputFile=$(inputFiles)' '--runAndLumis=$(runAndLumiMask)' --lheInputFiles=$(lheInputFiles) --firstEvent=$(firstEvent) --firstLumi=$(firstLumi) --lastEvent=$(lastEvent) --firstRun=$(firstRun) --seeding=$(seeding) --scriptExe=$(scriptExe) --eventsPerLumi=$(eventsPerLumi) --maxRuntime=$(maxRuntime) '--scriptArgs=$(scriptArgs)' -o $(CRAB_AdditionalOutputFiles)"
`
https://github.com/dmwm/CRABServer/issues/8869

## Comment (belforte, 2025-01-10T16:40:34Z)

a new version of `preparelocal` is now in my branch https://github.com/belforte/CRABClient/tree/use-json-file-for-job-args-5288 and works. But it requires the modified CMSRunAnalysis.py.
I do not see any easy way to make this backward compatible, would need to somehow detect the version of CMSRunAnalyis.py inside `preparelocal.py`, doable but very ugly and possibly fragile.

So this change can only be pushed to Client once TW has been changed in production and all old tasks completed. 
It is instead very easy to keep supporting `--json` argument to CMSRunAnalyisis.py, i.e. have the new TW backward compatible with current client.

## Comment (belforte, 2025-02-17T09:03:18Z)

the required TW changes have been deployed on Jan 10th with v3.250109 [ref](https://cms-talk.web.cern.ch/t/canary-tw-updated-to-v3-250109/94000/2?u=belforte)

Time to merge and push to crab-dev

## Comment (belforte, 2025-02-27T09:16:01Z)

the only thing left to do is to deploy CRABClient v3.250217 in production. All running tasks are compatible with the new code.
Then... cleanup !
