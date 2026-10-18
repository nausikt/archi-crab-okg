# dmwm/CRABServer issue #7741: RUCIO_Transfers.py: RUCIO ASO does not have publish infomation to proper create publish container

State: closed
Opened: 2023-07-11T10:26:12Z
Closed: 2023-09-12T07:56:01Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7741

## Opening post (novicecpp, 2023-07-11T10:26:12Z)

In case the task has both edm and non-edm files, non-edm files always have `/FakeDataset` from PostJob.py.
RUCIO_Transfers.py grab the first item of `transfers.txt` and uses it as the container name.

For transfers container, any name should be fine as long as Rucio accepts and can link back to the task that was created.

But for publish container, this will be a problem if the first item is non-edm:

- It uses `/FakeDataset` as an incorrect container name. It should use the same name we put in db (`tasks.tm_output_dataset`).
- We publish non-edm files along edm files to DBS, which will raise the exception in publisher later.

To fix this, I will pass `delayed_publicationflag_update` flag to `transfers.txt` to let RUCIO_Transfers.py pick only files with `delayed_publicationflag_update=True` and add them to publish container.

## Comment (belforte, 2023-07-21T16:33:56Z)

@novicecpp I think we need to establish an agreement here.
I was expecting to find `dbs_blockname` filled in `transfersdb` only for files which need to be published in DBS.
But in recent task `230720_064558:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20230720_084555`  I find `dbs_blockname` set to `/FakeDataset/fakefile-FakePublish-657b30b60b5efd8eaf8dc7a61e5a49bb/USER#0ee53a28-bbe3-4e30-bdf9-5300a2570a80`
![image](https://github.com/dmwm/CRABServer/assets/1837785/b098796d-df3f-4cdb-a74b-ab9afb7f5f83)

I can adapt, or you can change, or this was some test and I should ignore.

Let me know. I am not attempting to publish yet, still working on the part which collects info from transfersdb and filemetadata and prepares json files to feed to Publisher/TaskPublish.py, so there is no special hurry.

## Comment (novicecpp, 2023-07-26T09:26:16Z)

This test task has buggy RUCIO_Transfers.py, please ignore (Bug fix: https://github.com/dmwm/CRABServer/pull/7786/files).

You can use these task instead:
- https://cmsweb-test12.cern.ch/crabserver/ui/task/230725_085336:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20230725_105333
- https://cmsweb-test12.cern.ch/crabserver/ui/task/230726_092447%3Atseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20230726_112445

## Comment (belforte, 2023-09-11T20:38:15Z)

I though this was done, no ?
> To fix this, I will pass delayed_publicationflag_update flag to transfers.txt to let RUCIO_Transfers.py pick only files with delayed_publicationflag_update=True and add them to publish container.

## Comment (novicecpp, 2023-09-12T07:56:01Z)

Yes. This was already done. We can close it now.
