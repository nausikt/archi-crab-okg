# dmwm/CRABServer issue #8532: adapt Publisher_rucio to have rucio scope:name in tm_dbs_blockname

State: closed
Opened: 2024-06-27T13:43:22Z
Closed: 2024-06-27T16:44:16Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8532

## Opening post (belforte, 2024-06-27T13:43:22Z)

after #8491 and #8525 are in and tested,
need to change Publisher_rucio to adapt to new format of dbs_blockname in filetransfersdb table

tm_dbs_blockname	user.belforte:/GenericTTbar/belforte-ruciotransfers-1719432558-94ba0e06145abd65ccb1d21786dc7e1d/USER#b08c5a53-4031-42d5-815d-f3549cd66d01

## Comment (belforte, 2024-06-27T13:50:01Z)

things are of course broken (in master) until this is fixed

## Comment (belforte, 2024-06-27T16:44:18Z)

fixed via https://github.com/dmwm/CRABServer/pull/8533
