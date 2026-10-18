# dmwm/CRABServer issue #8973: add new colums to Task table in DB

State: closed
Opened: 2025-03-10T17:05:49Z
Closed: 2025-03-24T12:18:49Z
URL: https://github.com/dmwm/CRABServer/issues/8973

## Opening post (belforte, 2025-03-10T17:05:49Z)

1. `uploaded` (True/False) for #8928 
2. `DAGstatus` (String) for #8394 
3. `NumJobs` (Integer) for #7766 


Action list

- [x] add in create.py
- [x] add in [etc/updateOracle.sql](https://github.com/dmwm/CRABServer/blob/master/etc/updateOracle.sql)
- [x] apply updateOracle.sql to all DB's
   - [x] dev
   - [x] devtwo
   - [x] devthree
   - [x] devfour
   - [x] preprod
   - [x] prod 
- [x] add/modify REST API's as needed to set/read.
- [x] hmm... Take this chance to add an 'edit one param' API ? Make it request operator authz  but let it free to touch anything (maybe a list of params as well ?). Could be useful in a lot of other places ! For reading we may stick with "read all info for this task".

## Comment (belforte, 2025-03-11T23:14:28Z)

so I went for adding an `edit` subresource to `task` API which allows to set a value for any column, e.g.

```python
        data={'subresource': 'edit', 'workflow': '250308_212448:belforte_crab_20250308_222239',
           'column': 'tm_num_jobs', 'value': 33}
        result = crabserver.post(api='task', data=urlencode(data))
```
**CARE IS NEEDED FROM USERS, since checking of column and value is very limited**

## Comment (belforte, 2025-03-19T09:37:03Z)

code is ready in https://github.com/dmwm/CRABServer/tree/addInfoToTasks-03-25
But  before we deploy we need to update all databases with new columns !

## Comment (aspiringmind-code, 2025-03-24T12:18:49Z)

@belforte  All Oracle DBs have been updated.
