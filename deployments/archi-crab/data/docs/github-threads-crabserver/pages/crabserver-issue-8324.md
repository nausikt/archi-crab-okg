# dmwm/CRABServer issue #8324: T2_DE_DESY_temp Rucio config changed, break Rucio ASO

State: closed
Opened: 2024-04-09T14:49:41Z
Closed: 2024-04-12T10:21:10Z
URL: https://github.com/dmwm/CRABServer/issues/8324

## Opening post (novicecpp, 2024-04-09T14:49:41Z)

There are 2 issues:
1. T2_DE_DESY_Temp's Ruico protocol has changed. 

This break the hardcode I put in `RegisterReplicas.py`.

https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L303-L304

Good things is now DESY normal RSE and Temp RSE protocol consistent (FYI: We get `pfn` path from `rucio.lfns2pfns()` by passing normal RSE to function and assumed `Temp` area has same protocol).

**CURRENT** result from: `rucio.get_protocols('T2_DE_DESY_Temp')` (only davs):
```python
{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 1,
    'read': 1,
    'third_party_copy_read': 1,
    'third_party_copy_write': 1,
    'write': 1}},
  'extended_attributes': None,
  'hostname': 'dcache-cms-webdav-wan.desy.de',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 2880,
  'prefix': '/pnfs/desy.de/cms/tier2/temp/',
  'scheme': 'davs'}
```


**LAST YEAR** result from: `rucio.get_protocols('T2_DE_DESY_Temp')` (only davs):
```python
{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 1,
    'read': 1,
    'third_party_copy_read': 1,
    'third_party_copy_write': 1,
    'write': 1}},
  'extended_attributes': None,
  'hostname': 'dcache-cms-webdav-wan.desy.de',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 2880,
  'prefix': '/pnfs/desy.de/cms/tier2/store/temp',
  'scheme': 'davs'}
```

**T2_DE_DESY** does not change (paste it here for comparison)
```python
{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 1,
    'read': 1,
    'third_party_copy_read': 1,
    'third_party_copy_write': 1,
    'write': 1}},
  'extended_attributes': {'tfc': [{'out': '/pnfs/desy.de/cms/tier2/unmerged/$1',
     'path': '/+store/unmerged/(.*)',
     'proto': 'pnfs'},
    {'out': '/pnfs/desy.de/cms/tier2/temp/$1',
     'path': '/+store/temp/(.*)',
     'proto': 'pnfs'},
    {'out': '/pnfs/desy.de/cms/tier2/$1', 'path': '/+(.*)', 'proto': 'pnfs'},
    {'chain': 'pnfs',
     'out': 'davs://dcache-cms-webdav-wan.desy.de:2880/$1',
     'path': '/+(.*)',
     'proto': 'webdav'}],
   'tfc_proto': 'webdav'},
  'hostname': 'dcache-cms-webdav-wan.desy.de',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 2880,
  'prefix': '/',
  'scheme': 'davs'}
  ```

Remove the hardcode should fix.

2. Rucio ASO break because issue above.

I expected Rucio ASO to survive exception cause by 1, mark job as fail, then let retry mechanism do the rest.
However, it not, and block indefinitely. This is due different exception is raised, `RSEFileNameNotSupported`, as shown in [rucio_transfer.log](http://vocms059.cern.ch/mon/tseethon/240408_114824:tseethon_crab_rucio_transfers_20240408_134822/SPOOL_DIR/task_process/transfer_rucio.log)

```
2024-04-08 19:47:17,240] [RucioTransfer.Actions.RegisterReplicas] [DEBUG] Registering replicas from T2_DE_DESY_Temp
[2024-04-08 19:47:17,240] [RucioTransfer.Actions.RegisterReplicas] [DEBUG] Replicas: {'e6410a90da68703fe3f2e70ba9c3eca00feaf74aa67b68d2299737f3': {'scope': 'user.tseethon', 'pfn': 'davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/ruciotransfers-1712576902/GenericTTbar/ruciotransfers-1712576902/240408_114824/0000/output_6.root', 'name': '/store/user/rucio/tseethon/ruciotransfers-1712576902/GenericTTbar/ruciotransfers-1712576902/240408_114824/0000/output_6.root', 'bytes': 633409, 'adler32': '5aa85c44'}}
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 107, in main
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/CRAB3.zip/ASO/Rucio/RunTransfer.py", line 54, in algorithm
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 50, in execute
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 170, in addFilesToRucio
  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/current/lib/python3.9/site-packages/rucio/client/replicaclient.py", line 279, in add_replicas
    raise exc_cls(exc_msg)
rucio.common.exception.RSEFileNameNotSupported: RSE does not support provided filename.
Details: Invalid prefix: provided '/pnfs/desy.de/cms/tier2/store', expected '/pnfs/desy.de/cms/tier2/temp/'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/task_process/RUCIO_Transfers.py", line 10, in <module>
    main()
  File "/data/srv/glidecondor/condor_local/spool/6243/0/cluster9556243.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 111, in main
Exception: Unexpected error during main
Command exited with non-zero status 1
```

The line that catch exception: 

https://github.com/dmwm/CRABServer/blob/5f3ab24a9f3544995d920610b84405d2d2b4dc3a/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L180

It is safe to use just generic RucioException here, and improve the monitoring later to cache this type of error.

## Comment (belforte, 2024-04-09T15:16:14Z)

very good !! thanks.

Worth checking with Rahul that thing with Rucio@DESY are now stable

## Comment (novicecpp, 2024-04-11T13:07:59Z)

Rahul told me it got fix from this change https://github.com/dmwm/CMSRucio/pull/766/files
I still do not understand. Maybe @dynamic-entropy can elaborate more?

## Comment (dynamic-entropy, 2024-04-11T13:34:51Z)

The rucio script that parsed the tfc rules did not add a trailing slash in prefeix `/store/temp/rucio` and `store/test/rucio` for `_Temp` and `_Test` rses respectively. 
This change ensures that. 
This was an issue with configuring RSEs for tokens because of this, and Guy identified this issue.

## Comment (novicecpp, 2024-04-11T13:35:54Z)

Thanks man!
