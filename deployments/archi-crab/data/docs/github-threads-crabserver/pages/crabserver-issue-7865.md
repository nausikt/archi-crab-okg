# dmwm/CRABServer issue #7865: RUCIO_Transfers.py: mark transfer fail when add_replicas raise exception

State: closed
Opened: 2023-09-06T11:03:27Z
Closed: 2023-09-11T11:30:05Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7865

## Opening post (novicecpp, 2023-09-06T11:03:27Z)

Typical `rucio.common.exception.RSEProtocolNotSupported: RSE does not support requested protocol.` error:

```
[2023-09-06 04:18:50,649] [RucioTransfer.Actions.RegisterReplicas] [ERROR] add_replicas(rse, r): rse=T2_UK_London_Brunel_Temp rs=[{'scope': 'user.tseethon', 'pfn': 'davs://dc2-grid-64.brunel.ac.uk:443/dpm/brunel.ac.uk/home/cms/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/prod/230825_100118__rgerosa_crab_20230825_120039/DYJetsToTauTauToMuTauh_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_rucio_transfers_usertask_test12_20230906_040707/230906_020712/0000/tree_12.root', 'name': '/store/user/rucio/tseethon/test-rucio/prod/230825_100118__rgerosa_crab_20230825_120039/DYJetsToTauTauToMuTauh_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_rucio_transfers_usertask_test12_20230906_040707/230906_020712/0000/tree_12.root', 'bytes': 3138302, 'adler32': '2021d89a'}]
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 162, in addFilesToRucio
  File "/cvmfs/cms.cern.ch/rucio/x86_64/slc7/py3/current/lib/python3.6/site-packages/rucio/client/replicaclient.py", line 248, in add_replicas
    raise exc_cls(exc_msg)
rucio.common.exception.RSEProtocolNotSupported: RSE does not support requested protocol.
Details: No protocol for provided settings found : {'availability_delete': True, 'availability_read': True, 'availability_write': True, 'credentials': None, 'deterministic': False, 'domain': ['lan', 'wan'], 'id': 'c0cd40229910481ebbe999d232c7faa6', 'lfn2pfn_algorithm': 'cmstfc', 'protocols': [{'hostname': 'dc2-grid-64.brunel.ac.uk', 'scheme': 'davs', 'port': 443, 'prefix': '/dpm/brunel.ac.uk/home/cms/store/temp/', 'impl': 'rucio.rse.protocols.gfal.Default', 'domains': {'lan': {'read': 0, 'write': 0, 'delete': 0}, 'wan': {'read': 1, 'write': 0, 'delete': 0, 'third_party_copy_read': 1, 'third_party_copy_write': 0}}, 'extended_attributes': None}, {'hostname': 'dc2-grid-64.brunel.ac.uk', 'scheme': 'gsiftp', 'port': 2811, 'prefix': '/dpm/brunel.ac.uk/home/cms/store/temp/', 'impl': 'rucio.rse.protocols.gfal.Default', 'domains': {'lan': {'read': 0, 'write': 0, 'delete': 0}, 'wan': {'read': 2, 'write': 0, 'delete': 0, 'third_party_copy_read': 2, 'third_party_copy_write': 0}}, 'extended_attributes': None}, {'hostname': 'dc2-grid-64.brunel.ac.uk', 'scheme': 'root', 'port': 11001, 'prefix': '/store/temp/', 'impl': 'rucio.rse.protocols.gfal.Default', 'domains': {'lan': {'read': 0, 'write': 0, 'delete': 0}, 'wan': {'read': 3, 'write': 0, 'delete': 0, 'third_party_copy_read': 3, 'third_party_copy_write': 0}}, 'extended_attributes': None}], 'qos_class': None, 'rse': 'T2_UK_London_Brunel_Temp', 'rse_type': 'DISK', 'sign_url': None, 'staging_area': False, 'verify_checksum': True, 'volatile': False, 'read_protocol': 1, 'write_protocol': 1, 'delete_protocol': 1, 'third_party_copy_read_protocol': 1, 'third_party_copy_write_protocol': 1}.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "task_process/RUCIO_Transfers.py", line 10, in <module>
    main()
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 91, in main
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/Main.py", line 89, in main
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/RunTransfer.py", line 53, in algorithm
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 45, in execute
  File "/data/srv/glidecondor/condor_local/spool/7326/0/cluster9377326.proc0.subproc0/CRAB3.zip/ASO/Rucio/Actions/RegisterReplicas.py", line 168, in addFilesToRucio
ASO.Rucio.exception.RucioTransferException: Something wrong with adding new replicas
Command exited with non-zero status 1`
```

When an exception occurs at `add_replicas()`, the code always exits and cannot continue processing other files.

https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L157-L168

This task has an error the first time it runs, making all other transfers stuck forever (and fail eventually).
https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230906_020712:tseethon_crab_rucio_transfers_usertask_test12_20230906_040707/SPOOL_DIR/task_process/transfer_rucio.log

The code needs to handle this error, skip problematic files, and continue processing others. 
Otherwise, it wastes resources; recovery task need to compute every job again.

## Comment (belforte, 2023-09-06T11:25:19Z)

This is a site configuration problem.
We may also terminate the task here and bump the problem to CMS-Rucio/Site admins to fix.
The important thing is to have a very visible alarm.
I presume that by the time this goes into production all temp T'2s, including `rse=T2_UK_London_Brunel` (if I parsed correctly the log) will be in good shape. But we can expect some site to change things and break later on. 
Best would be to have a continuous test of Temp RSE's.

## Comment (novicecpp, 2023-09-06T13:10:55Z)

Yes, this is configuration problem. 
But the part that our service cannot continue to work still bother me, and this issue happen more often than I thought. 
I will keep looking for solutions and keep changes to a minimum.

>  Best would be to have a continuous test of Temp RSE's.

I agree. I would kindly ask DM team to do that.

## Comment (belforte, 2023-09-06T13:15:49Z)

I fear that we will have to use our jobs as testing. DM team people have their hands very full.
