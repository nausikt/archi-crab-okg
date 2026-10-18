# dmwm/CRABClient issue #5427: crab report undercounts files/events when UserFiles input LFNs are replaced by DummyLFN

State: closed
Opened: 2026-06-27T21:57:27Z
Closed: 2026-06-30T09:33:51Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5427

## Opening post (Kiarendil, 2026-06-27T21:57:27Z)

Hi,

I found a `crab report` accounting issue for a private MC task using `config.Data.userInputFiles` with `FileBased` splitting, 3 input files per job. The CRAB Task in question is https://cmsweb.cern.ch/crabserver/ui/task/260603_121045%3Akivanov_crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025 .
The jobs ran successfully and CMSSW processed all input files, but `crab report` reported wrong accounting:

```text
Number of files processed: 1
Number of events read: 960641
```

while an independent count over `processedFiles.json` gives:

```text
1193 files
2881134 events
```

I used e.g. job 1 for debugging. The [FJR](https://cmsweb.cern.ch/scheddmon/0137/kivanov/260603_121045:kivanov_crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/job_fjr.1.0.json) is correct:

```text
mini_pix_1.root    events = 2500
mini_pix_10.root   events = 2452
mini_pix_100.root  events = 2385
ProcessingSummary.NumberEvents = 7337
```

But the [PostJob log](https://cmsweb.cern.ch/scheddmon/0137/kivanov/260603_121045:kivanov_crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/postjob.1.0.txt) shows that all three input files were uploaded with the same POOLIN LFN:

```text
/store/user/dummy/DummyLFN_1, events = 2500
/store/user/dummy/DummyLFN_1, events = 2452
/store/user/dummy/DummyLFN_1, events = 2385
```

The original input LFNs contained a double slash, e.g.

```text
/store/group/phys_bphys/kivanov/Bfinder/PrivateMC/MIT//pix_2025/...
```

so I suspect they failed LFN validation and were replaced by `/store/user/dummy/DummyLFN`.

This causes two visible problems:

1. **Event count is wrong** because multiple input files in the same job are uploaded with the same POOLIN `outlfn`, so their metadata records collide.

2. **File count becomes 1** because `crab report` later strips the final `_jobid` suffix, so `DummyLFN_1`, `DummyLFN_2`, etc. all collapse to `DummyLFN`.

I find this behaviour quite confusing, when in general everything is fine with the task, but `report` misbehaves due to LFN problems for private MC, and does it silently, so I spent some time investigating. I would suggest either to make the dummy POOLIN LFN unique per input file, or warn/fail when invalid UserFiles LFNs would make `crab report` accounting unreliable, etc. 

Best regards, 
Kirill 

[job_fjr.1.0.json](https://github.com/user-attachments/files/29422438/job_fjr.1.0.json)
[postjob.1.0.txt](https://github.com/user-attachments/files/29422419/postjob.1.0.txt)

## Comment (belforte, 2026-06-28T11:11:54Z)

Thanks @Kiarendil for reporting this. It looks like a bug that I should be able to fix.
Hopefully fixing PostJob to upload the correct metdata will do.

## Comment (belforte, 2026-06-28T11:30:38Z)

hmmm... fixing the PostJob should take care of **1.** above. But **2.** is sitll puzzling. I would expect to have filemetadata for just one input file per job, not 3, due to PJ bug, but then there should be 398 processed input files, not 1.

## Comment (belforte, 2026-06-28T11:58:59Z)

OK., when PJ creates `Dummy_file_<jobid>` it is effectively saying that all jobs processed the single `dummy_file` input, it add the jobid to deal with the situation where multiple jobs processed different parts (sets of lumis) of the input file.
To avoid this problem a different dummy_file should be created for each job... but this seems all due to some logical confusion. If the input file is in DBS, there is no problem because it will pass LFN validation, if the input file is not in DBS, there should be no need to put anything in inputfilemetadata.

While handling the `//` is easy, I need to worry about the situation when UserInputFiles is a list of PFN's which will never pass LFN validation.

Need some time to reconstruct the full logical chain from PJ to crab report and to Publisher.

## Comment (Kiarendil, 2026-06-28T12:04:21Z)

Maybe it is easier to just forbid user to submit CRAB task, when UserFiles do not pass LFN validation? Or there could be cases when it can be useful?

## Comment (belforte, 2026-06-28T13:50:45Z)

The idea was that user can also provide PFN's like `root://.....` or `dcap:...` or any file locally mounted at the site where jobs run, regardless of being in `/cms` directory tree.
Of course as long as all data are accessible via `xrootd` and are places inside CMS name space, LFN will suffice. But having this feature may still be good.

Besides, even if CRAB is end-of-life now, I prefer to take this chance to  bring clarity of design where "what should happen" is clearly spelled in English and code is consistent with that.
I nothing else, it will be "use case description for next WMS tool"

## Comment (belforte, 2026-06-28T15:12:22Z)

Trying to find out how dummy file names make their way into `crab report`:

First:
```python
dictresult, status, _ = server.get(api=self.defaultApi, data={'workflow': self.cachedinfo['RequestName'], 'subresource': 'report2'})
```
which gives things like:
```
(Pdb) pprint(dictresult['result',0,'runsAndLumis','1'])
[{'events': 0,
  'lfn': '/store/user/kivanov/Bfinder/MC/BuJpsiK_pix_2025/2024/CRAB_UserFiles/CRAB3_Bfinder/260603_121045/0000/BFinder_pix_1.root',
  'parents': '[]',
  'runlumi': '{}',
  'type': 'TFILE'},
 {'events': 2500,
  'lfn': '/store/user/dummy/DummyLFN_1',
  'parents': '[]',
  'runlumi': "{'1': {'1': 'None'}}",
  'type': 'POOLIN'}]
(Pdb) 
```
which lists both output (as TFILE) and input (as POOLIN).... 

this is then copied into `reportData['processedRunsAndLumis',jobId]` (jobId as a string)

Then input file list is retrieved from S3, the tarball contains one file per job like
```console
belforte@lxplus813/IF> cat job_input_file_list_1.txt |jq
[
  "/store/group/phys_bphys/kivanov/Bfinder/PrivateMC/MIT//pix_2025/BuJpsiK_pix_2025/crab_BuJpsiK_pix_2025/260602_155211/0000/mini_pix_1.root",
  "/store/group/phys_bphys/kivanov/Bfinder/PrivateMC/MIT//pix_2025/BuJpsiK_pix_2025/crab_BuJpsiK_pix_2025/260602_155211/0000/mini_pix_10.root",
  "/store/group/phys_bphys/kivanov/Bfinder/PrivateMC/MIT//pix_2025/BuJpsiK_pix_2025/crab_BuJpsiK_pix_2025/260602_155211/0000/mini_pix_100.root"
]
belforte@lxplus813/IF> 
```
Those becomes a list of dictionaries in `reportData['filesToProcess']`

The number of processed input files is then computed based on the `POOLIN` files
```python
        numFilesProcessed = _getNumFiles(reportData['processedRunsAndLumis'], 'POOLIN')
```
but `_getNumFiles` has
```python
 # the split is done to remove the jobnumber at the end of the input file lfn
      files.add('_'.join(rep['lfn'].split('_')[:-1]))
```

So `crab report` should be fixed by fixing PostJob. I will anyhow tests this.

## Comment (belforte, 2026-06-28T15:18:51Z)

@Kiarendil I'd like to test re-running PostJob on your task to make sure I understand the code flow and test a fix. Am I free to mess with your task ? I do not expect anything to change, but it could be that a new `crab report` will give different (and yet not correct) results.
Do you still have a use for the json files in `crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/results` ?

## Comment (Kiarendil, 2026-06-28T15:22:17Z)

Sure, please mess whatever you need :)

## Comment (belforte, 2026-06-28T16:31:19Z)

Note: I do not like that the numbers printed by `crab report` to stdout are not consistent with the content of `results/processedFiles.json`. Ideally things should come from same source, whether they are right or wrong.
Maybe the input file metadata should be ignored here.

But it seems that input file metadata is the only place where we record the number of processed events.

The ideal solution would be that the statistics for `crab report` are compute by parsing the FJR's of successful jobs, i.e. in the AP, then added to the status_cache.json file which is read by the client. We have some schizophrenic approach where something comes form DB, but still crab report need a working crab status ... so if AP's WEB_DIR becomes unavailable we are stuck in any case.

I am making the dummy file name in the metadata a valid LFN format yet unique for every unique input file name. That should solve this, but leaves the schizophrenia.

## Comment (belforte, 2026-06-29T09:20:45Z)

The PostJob change in https://github.com/dmwm/CRABServer/pull/9337 will fix this (see https://github.com/dmwm/CRABServer/issues/9336#issuecomment-4830837779)

I will look into cross-checking number file files processed with the content of `filesToProcess.json` and print some telling information in case we can not reliably count things from FJR.

## Comment (Kiarendil, 2026-06-29T09:25:44Z)

Great! 
Thanks :)

## Comment (belforte, 2026-06-29T10:37:20Z)

for your task new crab client would have printed this
```text
belforte@lxplus813/kiril> crab report crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/
Running crab status to fetch necessary information.
Rucio client intialized for account belforte
Warning:: Inconsistent/unusable information from cmsRun FJR's.
 Fall back to counting processed files from imput list. Counting of processed events is not possible
Will put report files in directory /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/kiril/crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/results
Summary from successful jobs (i.e. in status 'finished'):
  Number of files processed: 1193
  Number of events read: n/a
  Number of events written in EDM files: n/a
  Number of events written in TFileService files: n/a
  Number of events written in other type of files: n/a
  Processed lumis written to processedLumis.json
  Files to process written to filesToProcess.json
  Files processed by successful jobs written to processedFiles.json
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/kiril/crab_Bfinder_2024_BuJpsiK_pix_2025_BuJpsiK_pix_2025/crab.log
belforte@lxplus813/kiril> 

```

While if same task is submitted with new TaskWorker, it will be just fine.

New TaskWorker should be in production in O(1 week), while CRABClient updates only happen when a new CMSSW_17 gets built
