# dmwm/CRABServer issue #7740: RUCIO_Transfers.py: Sites misconfiguration

State: closed
Opened: 2023-07-11T08:18:48Z
Closed: 2023-11-17T15:27:22Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7740

## Opening post (novicecpp, 2023-07-11T08:18:48Z)

During test RUCIO_Transfers.py, I encounter 3 sites that have problems with misconfiguration:

#### `T2_DE_DESY`
- [x] `T2_DE_DESY`

For this site, I think it misconfiguration in Rucio.
Rucio rejects PFN return from `rucioClient.lfns2pfns()` [3] and raises this exception:

```
RSEFileNameNotSupported: RSE does not support provided filename.
Details: Invalid prefix: provided '/pnfs/desy.de/cms/tier2/temp', expected '/pnfs/desy.de/cms/tier2/store/temp'
```

See the reproducible snippet in [4].

I have checked with gfal command. It can access both paths properly (not sure if it is a temp solution from the site admin or else).

Well, this can [hardcode fix](https://github.com/novicecpp/CRABServer/blob/88d0e7a833405235e511351bbaa189f489a98060/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L279) for now. Not so urgent.

[3] `davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230707_101712/0000/output_95.root`

<details>
  <summary>[4]</summary>

  ```python
  # omit rucioClient initializing
  rse = 'T2_DE_DESY'
  rse_temp = f'{rse}_Temp'
  src_lfn = '/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230707_101712/0000/output_95.root'
  dst_lfn = '/store/user/rucio/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230707_101712/0000/output_95.root'
  src_did = f'user.tseethon:{src_lfn}'
  pfn = rucio.lfns2pfns(rse, [src_did], operation="third_party_copy_read", scheme='davs')[src_did]
  fr = [{'scope': 'user.tseethon', 'name': dst_lfn, 'pfn': pfn, 'bytes': 630787, 'adler32': '8da5ff37'}]
  rucioClient.add_replicas(rse_temp, fr)
  ```
</details>

#### `T2_UK_SGrid_Bristol`
- [x] `T2_UK_SGrid_Bristol`

This site has a broken configuration in Rucio.

In [getSourcePFN()](https://github.com/dmwm/CRABServer/blob/d3ddc20155be74a992b051076f5117501fcb0831/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L205), we use normal RSE to get PFN and imply that temp\_RSE has the same PFN URI.

But `T2_UK_SGrid_Bristol_Temp` only announced `root` scheme. I tried `davs` with gfal, and it works fine.

I tried to hardcode `root` scheme but still got `RSEProtocolNotSupported` exception when executing `rucioClient.add_replicas()`. See the reproducible snippet in [2].

I need to open a ticket to CMS DM.


<details>
  <summary>[1]</summary>

  ```
  >>> rucio.get_protocols('T2_UK_SGrid_Bristol_Temp')
  [{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 0,
    'read': 3,
    'third_party_copy_read': 3,
    'third_party_copy_write': 0,
    'write': 0}},
  'extended_attributes': None,
  'hostname': 'xrootd.phy.bris.ac.uk',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 1094,
  'prefix': '//xrootd/cms/store/temp/',
  'scheme': 'root'}]
  >>>
  >>>
  >>> rucio.get_protocols('T2_UK_SGrid_Bristol')
  [{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 1,
    'read': 1,
    'third_party_copy_read': 1,
    'third_party_copy_write': 1,
    'write': 1}},
  'extended_attributes': None,
  'hostname': 'xrootd.phy.bris.ac.uk',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 1094,
  'prefix': '/xrootd/cms/',
  'scheme': 'davs'},
 {'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
   'wan': {'delete': 3,
    'read': 3,
    'third_party_copy_read': 3,
    'third_party_copy_write': 3,
    'write': 3}},
  'extended_attributes': None,
  'hostname': 'xrootd.phy.bris.ac.uk',
  'impl': 'rucio.rse.protocols.gfal.Default',
  'port': 1094,
  'prefix': '//xrootd/cms/',
  'scheme': 'root'}]
  ```
</details>

<details>
  <summary>[2]</summary>

  ```python
  # omit rucioClient initializing
  rse = 'T2_UK_SGrid_Bristol'
  rse_temp = f'{rse}_Temp'
  src_lfn = '/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230707_101712/0000/output_951111.root'
  dst_lfn = '/store/user/rucio/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230707_101712/0000/output_95.root'
  src_did = f'user.tseethon:{src_lfn}'
  pfn = rucio.lfns2pfns(rse, [src_did], operation="third_party_copy_read", scheme='root')[src_did]
  fr = [{'scope': 'user.tseethon', 'name': dst_lfn, 'pfn': pfn, 'bytes': 630787, 'adler32': '8da5ff37'}]
  rucioClient.add_replicas(rse_temp, fr)
  ```
  Exception:
  ```
  RSEProtocolNotSupported: RSE does not support requested protocol.
  Details: No protocol for provided settings found : {'availability_delete': True, 'availability_read': True, 'availability_write': True, 'credentials': None, 'deterministic': False, 'domain': ['lan', 'wan'], 'id': 'a904cefbdc5c4d09a3032e0f8e3eb8bc', 'lfn2pfn_algorithm': 'cmstfc', 'protocols': [{'hostname': 'xrootd.phy.bris.ac.uk', 'scheme': 'root', 'port': 1094, 'prefix': '//xrootd/cms/store/temp/', 'impl': 'rucio.rse.protocols.gfal.Default', 'domains': {'lan': {'read': 0, 'write': 0, 'delete': 0}, 'wan': {'read': 3, 'write': 0, 'delete': 0, 'third_party_copy_read': 3, 'third_party_copy_write': 0}}, 'extended_attributes': None}], 'qos_class': None, 'rse': 'T2_UK_SGrid_Bristol_Temp', 'rse_type': 'DISK', 'sign_url': None, 'staging_area': False, 'verify_checksum': True, 'volatile': False, 'read_protocol': 1, 'write_protocol': 1, 'delete_protocol': 1, 'third_party_copy_read_protocol': 1, 'third_party_copy_write_protocol': 1}.
  ```
</details>

#### `T2_FR_IPHC`
- [x] `T2_FR_IPHC`

This is the site misconfiguration.

Many jobs run in this site cannot do local stage-out to local site and got fallback to `T2_FR_GRIF_LLC`. But, when I try to check the file with gfal using URI return by [getSourcePFN()](https://github.com/dmwm/CRABServer/blob/d3ddc20155be74a992b051076f5117501fcb0831/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L205), the file is not found.
I asked @guyzsarun (CatA site support) to investigate, and he found that `T2_FR_IPHC` still uses the old fallback config.

In summary, for this [job_out.87.0.txt](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230710_104725:tseethon_crab_rucio_transfers_frsites_test12_20230710_124723/job_out.87.0.txt),

- `getSourcePFN()` return: `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230710_104725/0000/output_87.root`
- The correct path that can access by gfal is: `davs://polgrid4.in2p3.fr//dpm/in2p3.fr/home/cms/trivcat/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1/GenericTTbar/ruciotransfers-1/230710_104725/0000/output_87.root`

@guyzsarun promises me he will fix it soon :) .

## Comment (belforte, 2023-07-11T08:38:10Z)

so the problem is with T2_UK_SGrid_Bristol_Temp, not T2_UK_SGrid_Bristol, right ? @KatyEllis

## Comment (belforte, 2023-07-11T08:41:26Z)

for T2_DE_DESY can you say which commad/call produces the reported error ? Then it should be passed to CMS Rucio Ops (aka @dynamic-entropy  :-) )

## Comment (novicecpp, 2023-07-11T08:48:42Z)

> so the problem is with T2_UK_SGrid_Bristol_Temp, not T2_UK_SGrid_Bristol, right ?

Yes. The temp one. 

> for T2_DE_DESY can you say which commad/call produces the reported error ?

The usual `rucioClient.add_replicas()`.

## Comment (belforte, 2023-07-11T08:51:03Z)

I guess the argument matters. For sure there are times where get LFN2PFN for DESY and it works !

## Comment (novicecpp, 2023-07-11T08:59:10Z)

Because both paths are accessible, that is why FTS_Transfers.py always works.

## Comment (guyzsarun, 2023-07-11T11:58:10Z)

IPHC fallback stageout updated, can you try submitting jobs again @novicecpp ?

## Comment (novicecpp, 2023-07-11T12:39:32Z)

Thanks. 
Here Grafana link for workflow I submitted (metrics not yet available):
https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=tseethon&var-task=230711_123441%3Atseethon_crab_rucio_transfers_iphc_test12_20230711_143438&from=1689075281000&to=now

## Comment (novicecpp, 2023-07-12T06:18:29Z)

The task above is stuck to transfers due to a bug in RUCIO\_Transfers.py.
I fixed it this morning and found that (from job logs [job\_out.1.0.txt](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230711_123441:tseethon_crab_rucio_transfers_iphc_test12_20230711_143438/job_out.1.0.txt)):
- The fallback stageout went to [1].
- It is PFN of `T2_FR_GRIF_LLC` according to Rucio `get_protocols` [3].  But WMCore `StageOutMgr` reported fallback stageout site to `T2_FR_GRIF`.
- When `RUCIO_Transfers.py` resolve `T2_FR_GRIF` with `lfns2pfns()`, it returns a different PFN [2] from where the file is, making stageout fail (file not found).

@guyzsarun Are you sure the fallback of `T2_FR_IPHC` should go to `/eos/grif/cms/llr/` instead of `/eos/grif/cms/grif/`?

[1] `davs://eos.grif.fr:11000/eos/grif/cms/llr/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfer-1689078878/GenericTTbar/ruciotransfer-1689078878/230711_123441/0000/output_1.root`
[2] `davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfer-1689078878/GenericTTbar/ruciotransfer-1689078878/230711_123441/0000/output_1.root`

<details>
  <summary>[3]</summary>

  ```
  >>> rucioClient.get_protocols('T2_FR_GRIF_LLR_Temp')
  [{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
     'wan': {'delete': 1,
      'read': 1,
      'third_party_copy_read': 1,
      'third_party_copy_write': 1,
      'write': 1}},
    'extended_attributes': None,
    'hostname': 'eos.grif.fr',
    'impl': 'rucio.rse.protocols.gfal.Default',
    'port': 11000,
    'prefix': '/eos/grif/cms/llr/store/temp/',
    'scheme': 'davs'}]
  >>>
  >>>
  >>> rucioClient.get_protocols('T2_FR_GRIF_Temp')
  [{'domains': {'lan': {'delete': 0, 'read': 0, 'write': 0},
     'wan': {'delete': 1,
      'read': 1,
      'third_party_copy_read': 1,
      'third_party_copy_write': 1,
      'write': 1}},
    'extended_attributes': None,
    'hostname': 'eos.grif.fr',
    'impl': 'rucio.rse.protocols.gfal.Default',
    'port': 11000,
    'prefix': '/eos/grif/cms/grif/store/temp/',
    'scheme': 'davs'}]
  ```
</details>

## Comment (novicecpp, 2023-07-12T07:13:56Z)

@belforte Sorry for confused in T2_DE_DESY case. I have updated the correct LFN/PFN path and added a snippet in [4].

## Comment (belforte, 2023-07-12T08:51:37Z)

Thanks.  I guess that the reason is that the Protocols section for `T2_DESY_Temp` is "too much different" from the one for `T2_DE_DESY` so the rules about which LFN to accept and how to map to a PFN are different.
cfr:
```
rucio-admin rse info T2_DE_DESY
vs
rucio-admin rse info T2_DE_DESY_Temp
```
in particular
```
DESY:
  davs
    domains: '{"lan": {"read": 0, "write": 0, "delete": 0}, "wan": {"read": 1, "write": 1, "delete": 1, "third_party_copy_read": 1, "third_party_copy_write": 1}}'
    extended_attributes: {'tfc_proto': 'webdav', 'tfc': [{'proto': 'pnfs', 'path': '/+store/unmerged/(.*)', 'out': '/pnfs/desy.de/cms/tier2/unmerged/$1'}, {'proto': 'pnfs', 'path': '/+store/temp/(.*)', 'out': '/pnfs/desy.de/cms/tier2/temp/$1'}, {'proto': 'pnfs', 'path': '/+(.*)', 'out': '/pnfs/desy.de/cms/tier2/$1'}, {'proto': 'webdav', 'path': '/+(.*)', 'out': 'davs://dcache-cms-webdav-wan.desy.de:2880/$1', 'chain': 'pnfs'}]}
    hostname: dcache-cms-webdav-wan.desy.de
    impl: rucio.rse.protocols.gfal.Default
    port: 2880
    prefix: /
    scheme: davs

DESY_Temp
  davs
    domains: '{"lan": {"read": 0, "write": 0, "delete": 0}, "wan": {"read": 1, "write": 1, "delete": 1, "third_party_copy_read": 1, "third_party_copy_write": 1}}'
    extended_attributes: None
    hostname: dcache-cms-webdav-wan.desy.de
    impl: rucio.rse.protocols.gfal.Default
    port: 2880
    prefix: /pnfs/desy.de/cms/tier2/store/temp
    scheme: davs
```

For a couple of other sites which I checked, those are identical. Maybe as simple as "copy extended_attributes from DESY to DESY_Temp.
But since I do not fully understand those things, I defer to @dynamic-entropy 

I do not like that info has to be imported by hand from one config. to the other, consistency will always be lost.

## Comment (belforte, 2023-07-12T09:24:40Z)

> @guyzsarun Are you sure the fallback of T2_FR_IPHC should go to /eos/grif/cms/llr/ instead of /eos/grif/cms/grif/?

I suspect that `/eos/grif/cms/llr`/ in `/cvmfs/cms.cern.ch/SITECONF/T2_FR_IPHC/JobConfig/site-local-config.xml` is a left-over from before GRIF storage was consolidated in a single EOS instance.

Of course it is not good that writing to `T2_FR_IPHC:/store/temp/user` failed to begin with. The first file was written, then all others failed. But that's a different story. I think we had seen already this "gfal does not properly handle that destination directory already exists, tries to create it again and fails", but my memory fails me about how it ended (a new gfal version ?)  Maybe Stephan Lammel remembers, bu I do not have/find his GH handle . @guyzsarun

## Comment (dynamic-entropy, 2023-07-12T09:27:04Z)

Hello, 
I remember having some conversations around this with wa. However, I failed to understand why DESY is an outlier.
Unfortunately, I am not well versed with tfc (tbh, I do not know what tfc is other than a algorithm to map from lfn to pfn and why it is used in cms), so I would suggest opening an issue in CMSRucio and asking Eric about it.

## Comment (novicecpp, 2023-07-12T09:42:02Z)

@dynamic-entropy I will.

@belforte I had a private discussion with Guy this morning. He said there is ongoing storage migration in T2_FR_IPHC so it may be the cause of the fallback stageout, and he will fix the site config for us later today.

## Comment (guyzsarun, 2023-07-12T09:50:57Z)

@novicecpp Sorry my bad, storage migration is at FI_HIP :)

From my understanding before GRIF merged, IPHC fallback uses `polgrid4.in2p3.fr` under GRIF_LLR and not GRIF eos.  
should we move it to GRIF (`/eos/grif/cms/grif`)  or continue with the same GRIF_LLR under `/eos/grif/cms/llr`?

## Comment (belforte, 2023-07-12T10:04:24Z)

that's for IPHC and GRIF admins to decide. In consultation with SiteSupport of course ! 

I thought that `llr` and `irfu` directories were going to eventually disappear ad data be consolidated under `/eos/grif/cms/store`, but.. what do I know ?

## Comment (belforte, 2023-07-12T10:12:40Z)

@dynamic-entropy > what tfc is other than a algorithm to map from lfn to pfn and why it is used in cms

You must not be in the dark here !
It is exactly that ! It is used becasue the original design allowed for freedom to map some LNF's here, some LFN's there. Eventually site admins managed to get all disk in a single storage server and decided to keep things as simple as possible, so we are almost fully  in the Rucio standard situation where LFN to PFN is just a matter of adding a prefix. RSE configs mention indeed "prefix" in most cases.

The FTC is also needed for data access via xrootd, where we pass a LFN to the redirectors, so it can figure out how files with different path are indeed identical replicas.

I do not know if there are still sites where a prefix is not enough, which, why etc... And I have  been out of the loop in RSE configuration work, and am happy to stay like that !

## Comment (novicecpp, 2023-07-25T07:31:20Z)

Issue opened in CMSRucio: https://github.com/dmwm/CMSRucio/issues/577

For `T2_FR_IPHC`, Guy fixed the site config and now it work perfectly.

## Comment (novicecpp, 2023-11-17T15:27:23Z)

This issue original intention is to figure it out the proper way to reconcile the protocol (`rucio.get_protocols()`) of site's normal RSE and temp RSE.
 
Conclusion from discussed with Eric https://github.com/dmwm/CMSRucio/issues/577#issuecomment-1759751252:
- PFN of most site can copy prefix from normal RSE to Temp RSE
- We need to hardcode it for some site (e.g. `T2_DE_DESY`, likely the site that still use TLC from Phedex era)

So, I will leave the [RegisterReplicas.py#L298-L300](https://github.com/dmwm/CRABServer/blob/33170eb14256f6d689225426e3d038d0a8a9e10c/src/python/ASO/Rucio/Actions/RegisterReplicas.py#L298-L300) as is and do the refactor later if there are more sites need to hardcode. 

`T2_FR_IPHC` is fixed, `T2_UK_SGrid_Bristol` was fix by itself (it was working a month ago but now it on the crab global blacklist). 

Suggest to open the ticket to CMSRucio/Data Transfer if we found more site misconfigurations (e.g., no davs protocol in Temp RSE, get RSEProtocolNotSupported in Rucio ASO logs, or no davs protocol from temp RSE)

Closing this issue as complete.
