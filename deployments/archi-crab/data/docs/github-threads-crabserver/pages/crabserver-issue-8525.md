# dmwm/CRABServer issue #8525: RUCIO_Transfers should store also scope in filetransfersdb

State: closed
Opened: 2024-06-26T10:33:29Z
Closed: 2024-06-27T11:32:18Z
Labels: Type: Enhancement, Priority: TOP, Publisher
URL: https://github.com/dmwm/CRABServer/issues/8525

## Opening post (belforte, 2024-06-26T10:33:29Z)

change semantycs of `tm_dbs_blockname` colum
https://github.com/dmwm/CRABServer/blob/43a8454abec4059ae5b2804b4efe8e77553d1f38/src/python/Databases/FileTransfersDB/Oracle/Create.py#L62

so that it stores the full Rucio dataset DID `scope:name` to make it easy to correlated with information in Rucio (e.g. for PublisherRucio).
ref: #8491

Ideally we should change the column name as well. But that takes time and is likely multistep: add new column, fill both, switch Publisher to use new one, remove old column, changes are needed in REST too.

## Comment (belforte, 2024-06-26T20:41:10Z)

I have implemented a quick and dirty fix which works in my first test.

Maybe it would have been better to put `scope:name` in the replica dictionary, where we only have `r['name']` (IIUC) so that in `fileDoc['dataset`]` we have a Rucio dataset name `scope:name` not a DBS block name. At least it would make content consistent with name, IMHO.

But such a change would require  quite some time, I would need to become familiar with those data structures and all the places where they are used. Althought ASO/Rucio has way more documentation than other CRAB pieces, those dictionaries are not so clear.

## Comment (belforte, 2024-06-27T11:32:10Z)

fixed via https://github.com/dmwm/CRABServer/pull/8530
