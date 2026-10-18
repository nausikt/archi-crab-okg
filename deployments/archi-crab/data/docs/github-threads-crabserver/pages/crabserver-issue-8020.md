# dmwm/CRABServer issue #8020: Cleanup action should remove Temp_RSE replica from Rucio server

State: open
Opened: 2023-11-27T18:00:37Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/8020

## Opening post (novicecpp, 2023-11-27T18:00:37Z)

[New Cleanup's action](https://github.com/dmwm/CRABServer/blob/4911ebfc557c186316ffd6af6757f515b30e2a5c/src/python/ASO/Rucio/Actions/Cleanup.py) only delete file from Temp_RSE. We still need to remove Temp_RSE entry from replicas.

However, current policy of CMSRucio does not allow users to delete it own replicas. 
We opened the issue https://github.com/dmwm/CMSRucio/issues/297#issuecomment-1697499976, but no progress so far.

Wait until it is solved. 
Not sure about the impact if Temp_RSE replicas stay like this forever.

----------------------

In example: 

```
[tseethon@lxplus804 ~]$ rucio list-file-replicas user.tseethon:/store/user/rucio/tseethon/test-rucio/ruciotransfers-1698936029/GenericTTbar/ruciotransfers-1698936029/231102_144033/0000/miniaodfake_1.root
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SCOPE         | NAME                                                                                                                                         | FILESIZE   | ADLER32   | RSE: REPLICA                                                                                                                                                                                                                                    |
|---------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user.tseethon | /store/user/rucio/tseethon/test-rucio/ruciotransfers-1698936029/GenericTTbar/ruciotransfers-1698936029/231102_144033/0000/miniaodfake_1.root | 104.858 MB | b491db26  | T2_CH_CERN: davs://eoscms.cern.ch:443/eos/cms/store/user/rucio/tseethon/test-rucio/ruciotransfers-1698936029/GenericTTbar/ruciotransfers-1698936029/231102_144033/0000/miniaodfake_1.root                                                       |
| user.tseethon | /store/user/rucio/tseethon/test-rucio/ruciotransfers-1698936029/GenericTTbar/ruciotransfers-1698936029/231102_144033/0000/miniaodfake_1.root | 104.858 MB | b491db26  | T2_CH_CERN_Temp: davs://eoscms.cern.ch:443/eos/cms/store/temp/user/tseethon.d6830fc3715ee01030105e83b81ff3068df7c8e0/tseethon/test-rucio/ruciotransfers-1698936029/GenericTTbar/ruciotransfers-1698936029/231102_144033/0000/miniaodfake_1.root |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

File in `T2_CH_CERN_Temp` is long gone. It should only have `T2_CH_CERN` entry.
