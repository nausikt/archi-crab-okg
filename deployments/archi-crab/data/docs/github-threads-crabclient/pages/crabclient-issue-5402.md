# dmwm/CRABClient issue #5402: config.General.instance is not obeyed anymore

State: closed
Opened: 2025-07-01T19:17:58Z
Closed: 2025-07-02T19:05:08Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5402

## Opening post (belforte, 2025-07-01T19:17:58Z)

after latest changes `crab submit`  ignored the instance specification in the config file

```console
belforte@lxplus800/TC3> grep instance crabConfig.py|grep -v '#'
config.General.instance = 'test2'
belforte@lxplus800/TC3> crab submit
Will use CRAB configuration file crabConfig.py
Warning: CRAB configuration parameter General.instance is overwritten by the command option --instance; prod intance will be used.
Importing CMSSW configuration dummyanalyzer.py
Finished importing CMSSW configuration dummyanalyzer.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 250701_191612:belforte_crab_20250701_211608
Project dir: ./crab_20250701_211608
Please use ' crab status -d ./crab_20250701_211608 ' to check how the submission process proceeds.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250701_211608/crab.log
belforte@lxplus800/TC3> 
```

## Comment (belforte, 2025-07-01T19:22:53Z)

overwriting comes from https://github.com/dmwm/CRABClient/blob/64b0373ce7912719936fdea7c37fdbe7d831b962/src/python/CRABClient/Commands/SubCommand.py#L417-L431

## Comment (belforte, 2025-07-01T19:28:37Z)

problem is apparently fixed by removing this line https://github.com/dmwm/CRABClient/blob/73b01f1177eba7cd892562e7ec8e8da14dc46d33/src/python/CRABClient/CRABOptParser.py#L98
which was introduced in  https://github.com/dmwm/CRABClient/commit/0964a4bad23f5271c129ebd622ee5f4fcf41c478

but I am not satisfied with my understanding of things
