# dmwm/CRABClient issue #5203: adapt crab checkwrite to Rucio

State: closed
Opened: 2023-07-13T12:55:15Z
Closed: 2023-10-19T19:31:26Z
Labels: enhancement, Done, RUCIO, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5203

## Opening post (belforte, 2023-07-13T12:55:15Z)

when LFN has the format `/store/group|user/rucio/...` , replace current write check with a quota check.
Also print usage at various RSE's.

Note: Rucio CLI offers [rucio list_account_usage](https://github.com/rucio/rucio/blob/9ab79582cb373198fd272c79f5a2f116a8cff23a/bin/rucio#L1657) which rely on the python client's [get_local_account_usage](https://github.com/rucio/rucio/blob/9ab79582cb373198fd272c79f5a2f116a8cff23a/lib/rucio/client/accountclient.py#L310). The python client also has [get_global_account_usage](https://github.com/rucio/rucio/blob/9ab79582cb373198fd272c79f5a2f116a8cff23a/lib/rucio/client/accountclient.py#L329) I do not know what the latter does

## Comment (belforte, 2023-10-03T19:05:08Z)

on hold waiting for a decision on CRABClient vs. Rucio API in https://github.com/cms-sw/cmsdist/issues/8737

## Comment (belforte, 2023-10-18T17:38:08Z)

Time to go ahead. Can simply use `if self.rucio` in the code to check if Rucio client is available as `self.rucio`

## Comment (belforte, 2023-10-18T17:45:49Z)

example of `get_local_account_usage` 
```
>>> ag=rucio.get_local_account_usage('belforte')
>>> for a in ag: print(a)
... 
{'rse_id': 'e1c33ab333304b33b1e283bea046e112', 'rse': 'T3_IT_Trieste', 'bytes': 0, 'files': 0, 'bytes_limit': 10000000000, 'bytes_remaining': 10000000000}
{'rse_id': '542ab69d82bf401e9218bbe375bb1fce', 'rse': 'T2_CH_CERN', 'bytes': 3306867807, 'files': 1588, 'bytes_limit': 100000000000, 'bytes_remaining': 96693132193}
>>> 
```
while `get_global_account_usage` returns nothing. So choice is simple !
```
>>> agg=rucio.get_global_account_usage('belforte')
>>> for a in agg: print(a)
... 
>>> print(agg)
<generator object BaseClient._load_json_data at 0x7fac67768dd0>
>>> 

```

## Comment (belforte, 2023-10-18T20:31:53Z)

as a start, use directly Rucio client for LFN to PFN resolution when available https://github.com/belforte/CRABClient/commit/c302ac517ae73205f47903ddbdb691990c05bf37
