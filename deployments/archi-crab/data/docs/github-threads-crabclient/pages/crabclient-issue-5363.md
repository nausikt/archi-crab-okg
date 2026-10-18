# dmwm/CRABClient issue #5363: crab report should make it clear that list of read event/files are from successful jobs

State: closed
Opened: 2024-12-09T09:57:33Z
Closed: 2024-12-09T10:07:32Z
Labels: Support
URL: https://github.com/dmwm/CRABClient/issues/5363

## Opening post (belforte, 2024-12-09T09:57:33Z)

ref https://cms-talk.web.cern.ch/t/crab-can-not-access-some-files-with-exit-code-8028/74421/11

e.g.
```console
belforte@lxplus825/ste> crab report --task 241203_033126:mlouka_crab_Analysis_qqZZ
crab report requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_Analysis_qqZZ folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_Analysis_qqZZ
Running crab status first to fetch necessary information.
Rucio client intialized for account belforte
Will save lumi files into output directory /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_Analysis_qqZZ/results
Summary from jobs in status 'finished':
  Number of files processed: 1799
  Number of events read: 99148000
  Number of events written in EDM files: 0
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
  Warning: 'notFinished' lumis written to notFinishedLumis.json
           The 'notFinished' lumis were calculated as: the lumis to process minus the processed lumis.
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_Analysis_qqZZ/crab.log
belforte@lxplus825/ste> 

```

## Comment (belforte, 2024-12-09T10:03:40Z)

I guess `Summary from jobs in status 'finished':`  is not clear enough.
