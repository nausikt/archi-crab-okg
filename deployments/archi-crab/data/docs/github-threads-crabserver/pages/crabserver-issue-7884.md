# dmwm/CRABServer issue #7884: list also SUSPENDED rules in html table

State: closed
Opened: 2023-09-18T15:08:10Z
Closed: 2023-09-18T15:14:26Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7884

## Opening post (belforte, 2023-09-18T15:08:10Z)

this table
![image](https://github.com/dmwm/CRABServer/assets/1837785/d9fe2728-889b-44d3-b57f-60b1bfd556e7)

should also list SUSPENDED rules, e.g. from TapeRecallManager log:
```
belforte@crab-prod-tw01/recurring> cat TapeRecallManager_230918-1429.log
2023-09-18 14:29:24,914:INFO:MasterWorker:Will connect to CRAB service: prod
2023-09-18 14:29:24,915:INFO:RucioUtils:Initializing native Rucio client
2023-09-18 14:29:24,915:DEBUG:RucioUtils:Using cert [/data/certs/servicecert.pem]
 and key [/data/certs/servicekey.pem] for rucio client.
2023-09-18 14:29:24,930:INFO:RucioUtils:Rucio server v.1.31.6 contacted
2023-09-18 14:29:24,945:INFO:RucioUtils:Rucio client initialized for crab_server in status ACTIVE
2023-09-18 14:29:24,946:INFO:RucioUtils:Initializing native Rucio client
2023-09-18 14:29:24,946:DEBUG:RucioUtils:Using cert [/data/certs/servicecert.pem]
 and key [/data/certs/servicekey.pem] for rucio client.
2023-09-18 14:29:24,959:INFO:RucioUtils:Rucio server v.1.31.6 contacted
2023-09-18 14:29:24,976:INFO:RucioUtils:Rucio client initialized for crab_tape_recall in status ACTIVE
2023-09-18 14:29:31,616:INFO:TapeRecallManager:Retrieved a total of 3 TAPERECALL tasks
2023-09-18 14:29:31,616:INFO:TapeRecallManager:Working on task 230905_105453:mowolf_crab__QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL16RECO-1
2023-09-18 14:29:31,617:INFO:TapeRecallManager:Task points to Rucio RuleId:  2eb183f35ea94f3d9c1c815d43b004a7
2023-09-18 14:29:31,628:INFO:TapeRecallManager:Rule 2eb183f35ea94f3d9c1c815d43b004a7 is SUSPENDED
2023-09-18 14:29:31,715:INFO:TapeRecallManager:Done on this task

```
