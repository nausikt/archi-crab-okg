# dmwm/CRABServer issue #8005: No 'type' key in transfer dicts for retry job

State: closed
Opened: 2023-11-16T15:24:43Z
Closed: 2023-11-22T15:26:46Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/8005

## Opening post (novicecpp, 2023-11-16T15:24:43Z)

For a retry job, PostJob.py constructs newDoc variable in [line 938](https://github.com/dmwm/CRABServer/blob/1f2a8dcb67740c0d6009514dc6256d9aad6b0955/src/python/TaskWorker/Actions/PostJob.py#L938) which has a slightly different schema compared to the job running first time in [line 896](https://github.com/dmwm/CRABServer/blob/1f2a8dcb67740c0d6009514dc6256d9aad6b0955/src/python/TaskWorker/Actions/PostJob.py#L896).
The `newDoc` will be dumped to `transfers.txt` for ASO to read later.

<details>
<summary>Example of newDoc when job run it first time:</summary>

```json
{
  "checksums": {
    "adler32": "1e40ab67",
    "cksum": "342207876"
  },
  "destination": "T2_CH_CERN",
  "destination_lfn": "/store/user/rucio/tseethon/test-rucio/ruciotransfers-1700067356/GenericTTbar/ruciotransfers-1700067356/231115_165559/0000/output_1.root",
  "filesize": 635045,
  "id": "1c7569ad03899ce6c1e7a1d5ccacef4375eae129c197757100c8c00c",
  "job_id": "1",
  "job_retry_count": 0,
  "outputdataset": "/GenericTTbar/tseethon-ruciotransfers-1700067356-94ba0e06145abd65ccb1d21786dc7e1d/USER",
  "publication_state": "NOT_REQUIRED",
  "publish": 0,
  "publishname": "ruciotransfers-1700067356-00000000000000000000000000000000",
  "source": "T1_ES_PIC_Disk",
  "source_lfn": "/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1700067356/GenericTTbar/ruciotransfers-1700067356/231115_165559/0000/output_1.root",
  "start_time": 1700067883,
  "taskname": "231115_165559:tseethon_crab_rucio_transfers_test_site_20231115_175556_T1_ES_PIC",
  "transfer_state": "NEW",
  "type": "output",
  "username": "tseethon"
}
```

</details>

<details>
<summary>Example of newDoc for retry job:</summary>

```
{
  "checksums": {
    "adler32": "bd953971",
    "cksum": "216833176"
  },
  "destination": "T2_CH_CERN",
  "destination_lfn": "/store/user/rucio/tseethon/test-rucio/ruciotransfers-1700067356/GenericTTbar/ruciotransfers-1700067356/231115_165559/0000/output_5.root",
  "filesize": 633997,
  "id": "8463f7074c338d0ec36dd789135c5b49b6514a27e197f0fce64a2cd1",
  "job_id": "5",
  "job_retry_count": 1,
  "outputdataset": "/GenericTTbar/tseethon-ruciotransfers-1700067356-94ba0e06145abd65ccb1d21786dc7e1d/USER",
  "publication_state": "NOT_REQUIRED",
  "publish": 0,
  "publishname": "ruciotransfers-1700067356-00000000000000000000000000000000",
  "source": "T1_ES_PIC_Disk",
  "source_lfn": "/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1700067356/GenericTTbar/ruciotransfers-1700067356/231115_165559/0000/output_5.root",
  "start_time": 1700069877,
  "subresource": "updateDoc",
  "taskname": "231115_165559:tseethon_crab_rucio_transfers_test_site_20231115_175556_T1_ES_PIC",
  "transfer_retry_count": 0,
  "transfer_state": "NEW",
  "username": "tseethon"
}
```

</details>

The main difference is that there is no `type` key in the retry job, which breaks Rucio ASO where it is used (in [RegisterReplicas#L74](https://github.com/dmwm/CRABServer/blob/1f2a8dcb67740c0d6009514dc6256d9aad6b0955/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L74)) to skip the log transfers.

```
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3519/0/cluster9453519.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 89, in main
  File "/data/srv/glidecondor/condor_local/spool/3519/0/cluster9453519.proc0.subproc0/CRAB3.zip/ASO/Rucio/RunTransfer.py", line 53, in algorithm
  File "/data/srv/glidecondor/condor_local/spool/3519/0/cluster9453519.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 43, in execute
  File "/data/srv/glidecondor/condor_local/spool/3519/0/cluster9453519.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 74, in skipLogTransfers
KeyError: 'type'
```

Reference:
- Task URL: https://cmsweb-test12.cern.ch/crabserver/ui/task/231115_165559%3Atseethon_crab_rucio_transfers_test_site_20231115_175556_T1_ES_PIC
- Transfers.txt: https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231115_165559:tseethon_crab_rucio_transfers_test_site_20231115_175556_T1_ES_PIC/SPOOL_DIR/task_process/transfers.txt
- Full Rucio ASO logs: https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231115_165559:tseethon_crab_rucio_transfers_test_site_20231115_175556_T1_ES_PIC/SPOOL_DIR/task_process/transfer_rucio.log
