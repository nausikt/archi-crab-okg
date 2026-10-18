# dmwm/CRABServer issue #9332: move to PublisherConfig the parameters for "doomed migration"

State: closed
Opened: 2026-06-26T10:05:53Z
Closed: 2026-07-01T07:57:10Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9332

## Opening post (belforte, 2026-06-26T10:05:53Z)

we currently use this in the FailedMigrationAccounter
https://github.com/dmwm/CRABServer/blob/e371f33876cf7a9fef1939a4763817a085507559/src/python/Publisher/PublisherUtils.py#L365-L367

but since the number of failed and number of days are quite arbitrary, better to have those in the configuration so we can change easily as we gain experience

FYI @nausikt

## Comment (belforte, 2026-06-26T14:49:04Z)

also tested behavior when a migration is "doomed":

2026-06-26 16:47:46,196:INFO: Have to migrate 1 blocks from https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader to https://cmsweb-prod.cern.ch:8443/dbs/prod/phys03/DBSReader.
2026-06-26 16:47:46,203:INFO: Cannot migrate. Some blocks have persistently failed migration:
['/MonoHToGG_ZpBaryonic_MZp500_MChi100_TuneCP5_13TeV_madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM#c9b98cd0-769a-4f40-a64f-85e358c0ee48']. Mark all files as failed

## Comment (belforte, 2026-06-26T14:52:12Z)

waiting for #9334 to be merged since I need to modify TaskPublisherRucio.py as well
