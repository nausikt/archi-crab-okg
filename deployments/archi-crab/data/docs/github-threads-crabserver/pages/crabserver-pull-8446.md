# dmwm/CRABServer pull request #8446: Fix successful_publication log line

State: closed
Opened: 2024-05-30T16:36:16Z
Closed: 2024-05-30T19:45:02Z
Merged: 2024-05-30T19:45:02Z
URL: https://github.com/dmwm/CRABServer/pull/8446

## Opening post (novicecpp, 2024-05-30T16:36:16Z)

Fixing https://github.com/dmwm/CRABServer/issues/8445

Current version:
```
2024-05-30 18:10:05,752:INFO:PublisherMaster,531:Taskname 240528_102302:lrygaard_crab_TTZToLLNuNu_LLPnanoAODv1 is OK. Published 2 in 1 blocks.
```

Expected: 
```
2024-05-28 00:20:04,315:INFO:PublisherMaster,731:Taskname 240524_022359:shiyi_crab_SPS_RESONANECE_FEEDDOWN_GEN_v2_n5 is OK. Published 42 files in 1 blocks.
```

The "files" after `summary['publishedFiles']` is missing.

## Comment (cmsdmwmbot, 2024-05-30T16:44:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2003/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-05-30T19:44:45Z)

Tested in `crab-dev-tw03` (From `crab-dev-tw03:/data/container/Publisher_schedd/logs/log.txt`)
```
2024-05-30 19:14:18,739:INFO:PublisherMaster,531:Taskname 240530_182528:crabint1_crab_20240530_202527 is OK. Published 100 files in 1 blocks.
```

## Comment (belforte, 2024-05-30T20:40:51Z)

thanks Wa !

## Comment (belforte, 2024-05-30T20:41:38Z)

I guess it was a mistake on my side converting messages to f-string :-(
 Sorry
