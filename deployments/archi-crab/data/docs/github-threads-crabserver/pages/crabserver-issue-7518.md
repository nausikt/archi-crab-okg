# dmwm/CRABServer issue #7518: take care of secondary dataset location

State: open
Opened: 2023-02-02T15:18:46Z
Labels: Type: Enhancement, Priority: Medium, Status: Available
URL: https://github.com/dmwm/CRABServer/issues/7518

## Opening post (belforte, 2023-02-02T15:18:46Z)

CRAB should be aware of secondary input data location, make sure it is accessible and run jobs where either primary or secondary data are as appropriate (using remote reading for the lighter data)
A possible action list is
- [ ] find out how to identify the secondary data set (config. may only indicate "userParent")
- [ ] add code in DBSDataDiscovery (the place where we talk to DBS) to find the needed parents and check location with Rucio
- [ ] if data are not on disk, decide if to ask a recall or give up and bump recall work to user
- [ ] if all data is on disk, decide if to use as DesiredSites the location(s) of primary or secondary. If Tier is different (RAW/SIM/RECO/AOD..) decide based on that. If same tier (sim + pileup e.g.) check for "pileup" string in db name. Or simply check dataset size and run where the dataset with most bytes is located
