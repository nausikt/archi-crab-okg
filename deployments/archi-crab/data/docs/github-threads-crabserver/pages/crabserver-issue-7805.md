# dmwm/CRABServer issue #7805: put retries around Rucio data location

State: open
Opened: 2023-08-10T22:45:01Z
Labels: Type: Bug, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7805

## Opening post (belforte, 2023-08-10T22:45:01Z)

e.g.
```
2023-08-10 23:01:03,099:DEBUG:DBSDataDiscovery:Datablock from DBS: ['/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM#3517e1b6-76e3-11e7-a0c8-02163e00d7b3', '/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM#35197562-76e3-11e7-a0c8-02163e00d7b3'] 
2023-08-10 23:01:03,099:INFO:DBSDataDiscovery:Looking up data location with Rucio in cms scope.
2023-08-10 23:01:03,109:WARNING:DBSDataDiscovery:Rucio lookup failed with
Cannot connect to the Rucio server.
2023-08-10 23:01:03,109:WARNING:DBSDataDiscovery:No locations found with Rucio for this dataset
```
