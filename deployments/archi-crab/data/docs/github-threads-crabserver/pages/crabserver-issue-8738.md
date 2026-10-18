# dmwm/CRABServer issue #8738: fix Rucio quota checking

State: closed
Opened: 2024-10-11T16:57:34Z
Closed: 2024-10-11T19:02:15Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8738

## Opening post (belforte, 2024-10-11T16:57:34Z)

we have been misled by the (very poor) documentation in https://rucio.cern.ch/documentation/client_api/accountclient#get_local_account_usage

after several tests the actual behavior of that API is
 * **it always returns a generator which will span all RSE's where that account has quota** 
 * **If you indicate a site, it still returns a generator for all RSE's bt the limit are retrieved only for the indicated site**
 
See e.g. this python snippet
```text
>>> for q in rucio.get_local_account_usage(account=account, rse='T2_IT_Legnaro'): print(q)
... 
{'rse_id': '16eef8c8359d47c985c5cc48dd1a1a56', 'rse': 'T1_DE_KIT_Disk', 'bytes': 755868188, 'files': 1196, 'bytes_limit': 0, 'bytes_remaining': -755868188}
{'rse_id': '390097850b0f41ed96164b454df291ce', 'rse': 'T2_IT_Legnaro', 'bytes': 4089582398, 'files': 6468, 'bytes_limit': 2000000000000, 'bytes_remaining': 1995910417602}
>>> 
```
 
Indeed the same can be seen with the CLI comparing e.g. these commands output [1]
```
rucio list-account-usage crab_test_group
rucio list-account-usage --rse T2_IT_Legnaro crab_test_group
rucio list-account-usage --rse T1_DE_KIT_Disk crab_test_group
```

[1]
```console
belforte@lxplus805/TC3> rucio list-account-usage crab_test_group
+----------------+------------+------------+--------------+
| RSE            | USAGE      | LIMIT      | QUOTA LEFT   |
|----------------+------------+------------+--------------|
| T1_DE_KIT_Disk | 755.868 MB | 500.000 GB | 499.244 GB   |
| T2_IT_Legnaro  | 4.090 GB   | 2.000 TB   | 1.996 TB     |
+----------------+------------+------------+--------------+
+------------------+---------+---------+--------------+
| RSE EXPRESSION   | USAGE   | LIMIT   | QUOTA LEFT   |
|------------------+---------+---------+--------------|
+------------------+---------+---------+--------------+
belforte@lxplus805/TC3> rucio list-account-usage --rse T2_IT_Legnaro crab_test_group
+----------------+------------+----------+--------------+
| RSE            | USAGE      | LIMIT    | QUOTA LEFT   |
|----------------+------------+----------+--------------|
| T1_DE_KIT_Disk | 755.868 MB | 0.000 B  | 0.000 B      |
| T2_IT_Legnaro  | 4.090 GB   | 2.000 TB | 1.996 TB     |
+----------------+------------+----------+--------------+
+------------------+---------+---------+--------------+
| RSE EXPRESSION   | USAGE   | LIMIT   | QUOTA LEFT   |
|------------------+---------+---------+--------------|
+------------------+---------+---------+--------------+
belforte@lxplus805/TC3> rucio list-account-usage --rse T1_DE_KIT_Disk crab_test_group
+----------------+------------+------------+--------------+
| RSE            | USAGE      | LIMIT      | QUOTA LEFT   |
|----------------+------------+------------+--------------|
| T1_DE_KIT_Disk | 755.868 MB | 500.000 GB | 499.244 GB   |
| T2_IT_Legnaro  | 4.090 GB   | 0.000 B    | 0.000 B      |
+----------------+------------+------------+--------------+
+------------------+---------+---------+--------------+
| RSE EXPRESSION   | USAGE   | LIMIT   | QUOTA LEFT   |
|------------------+---------+---------+--------------|
+------------------+---------+---------+--------------+
belforte@lxplus805/TC3> 
```
