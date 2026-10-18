# dmwm/CRABServer issue #9172: bug in ProcessBadFileList ?

State: closed
Opened: 2025-09-04T15:12:21Z
Closed: 2025-09-04T19:56:35Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9172

## Opening post (belforte, 2025-09-04T15:12:21Z)

crontab reported
`Cron job output from lxplus808.cern.ch:belforte at Thu Sep 4 02:34:44 2025`

```text

Failed to parse /eos/cms/store/temp/user/BadInputFiles/corrupted/new/250810_121607:jordanm_crab_XToEMu_GSF_2018_ALL_20250810_141438_ParkingBPH5_D_20250810_141603/suspicious
Traceback (most recent call last):
  File "ProcessBadFilesList.py", line 328, in <module>
    main()
  File "ProcessBadFilesList.py", line 72, in main
    shutil.move(filePath, doneTaskDir)
  File "/usr/lib64/python3.6/shutil.py", line 548, in move
    raise Error("Destination path '%s' already exists" % real_dst)
shutil.Error: Destination path '/eos/cms/store/temp/user/BadInputFiles/corrupted/done/250810_121607:jordanm_crab_XToEMu_GSF_2018_ALL_20250810_141438_ParkingBPH5_D_20250810_141603/suspicious' already exists
```
there is a very odd path `/eos/cms/store/temp/user/BadInputFiles/corrupted/new/<taskname>/suspicious`

suspicious files should be in a separate tree
```console
belforte@lxplus808/BadInputFiles> tree -d -L 2
.
|-- corrupted
|   |-- done
|   `-- new
|-- summaries
|-- suspicious
|   |-- done
|   `-- new
`-- truncated
    |-- done
    `-- new
```

or was something very wrong done in writing to EOS from RetryJob ?

odd directory `/eos/cms/store/temp/user/BadInputFiles/corrupted/new/<taskname>/suspicious` was created at 02:31, the time cronjob runs
So it looks a wrong "move" in the cronjob

## Comment (belforte, 2025-09-04T18:08:51Z)

I could not find anything wrong nor suspicious in https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/ProcessBadFilesList.py not in https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/RetryJob.py

Things are very strange, e.g. the postjob log for one file that "odd" directory says that report already exists. But file name has jobId + retry number, should be fully unique. Could PostJob have run twice "for the first time" ?

```
Thu, 28 Aug 2025 21:43:28 CEST(+0200):ERROR:RetryJob gfal-copy failed with out: b'' err: b'gfal-copy error: 17 (File exists) - Destination davs://eoscms.cern.ch:443/eos/cms/store/temp/user/BadInputFiles/suspicious/new/250810_121607:jordanm_crab_XToEMu_GSF_2018_ALL_20250810_141438_ParkingBPH5_D_20250810_141603/Badfile.job.5513.15.json exists and overwrite is not set\n'
```

I will try to simply fix the BadInputFiles directory by hand and run the script again.

## Comment (belforte, 2025-09-04T19:56:35Z)

I have "strenghtned" a bit [ProcessBadInputFilesList.py](https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/ProcessBadFilesList.py) via #9173 and #9174 which caused `falsePositives` directories to popup again. Let's see how it goes.
Script now runs fine.
