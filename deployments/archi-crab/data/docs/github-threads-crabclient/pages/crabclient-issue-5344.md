# dmwm/CRABClient issue #5344: bad logic in recover

State: closed
Opened: 2024-11-01T14:24:58Z
Closed: 2024-11-01T15:05:55Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5344

## Opening post (belforte, 2024-11-01T14:24:58Z)

following log from CV test indicates that ` all lumis have been published in the output dataset. crab recover will exit` did not make code exit loop with success, as it should be expected.
 
```text
Will save lumi files into output directory /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results
Summary from jobs in status '\''finished'\'':
  Number of files processed: 1
  Number of events read: 600
  Number of events written in EDM files: 600
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
Summary from output datasets in DBS:
  Number of events:
    /GenericTTbar/cmsbot-CRAB3_analysis-2411-94ba0e06145abd65ccb1d21786dc7e1d/USER: 6600
  Output datasets lumis written to outputDatasetsLumis.json
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
stepReport() - all lumis have been published in the output dataset. crab recover will exit
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
recover process prematurely exited during report step
File /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/results/notPublishedLumis.json does not exist. crab report could not produce it, the task can not be recovered
Command recover failed
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20241101_133630/crab.log
```

## Comment (belforte, 2024-11-01T14:25:32Z)

let's fix while I am fresh of work on `crab recover`
