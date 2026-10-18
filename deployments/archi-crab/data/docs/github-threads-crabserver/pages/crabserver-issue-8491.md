# dmwm/CRABServer issue #8491: Publisher_rucio must check to have all files in a block

State: closed
Opened: 2024-06-12T14:56:44Z
Closed: 2025-06-12T10:36:07Z
Labels: Type: Bug, RUCIO, Priority: TOP, Publisher
URL: https://github.com/dmwm/CRABServer/issues/8491

## Opening post (belforte, 2024-06-12T14:56:44Z)

as described in #8376  the publication flag for individual files is set in PostJob up to 30min after the file replica has been added to the Rucio-dataset/DBS-block by RucioTransfer. So when RucioTransfer adds the last file, declares the block closed and correspondently mark all entries in filetransfersdb, some files in the block may still not have the publish flag set.
If Publisher_Rucio runs "too soon" it will miss some files and since publshed blocks are closed, it will never be able to add them.

Solution is that Publisher checks the block/dataset content in Rucio and waits untill all needed files are ACQUIRED

Subtasks (tested in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7641939 )
- [x] make sure that changes for this do not break TaskWorker
- [x] also that configuration is properly constructed inside PreDag to be used when running on scheduler

## Comment (belforte, 2024-06-26T09:57:16Z)

I realized that I need the Rucio scope name, in addition to the DBS block name. This is trivial for users, but for groups it would required parsing the LNF, or maybe that's no sufficient. In any case awkward and fragile. I propose to change the `tm_dbs_blockname` column to store the Rucio dataset name `scope:dbs_blockname`. @novicecpp what do you think ?

## Comment (novicecpp, 2024-06-26T10:03:16Z)

Agreed.

## Comment (belforte, 2025-05-23T17:00:55Z)

While testing, I realized that I had not thoroughly reviewed the use case.
The situation where task is killed is not properly handled in the ASO/Publisher communication

https://github.com/dmwm/CRABServer/issues/9094

## Comment (belforte, 2025-06-12T10:36:07Z)

the "synchronization with Publisher" is likely solved by #9094

I have found a different problem #9111 which will be addressed separetely
