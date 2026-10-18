# dmwm/CRABServer issue #9121: Rucio retries should only retry HTTP errors

State: closed
Opened: 2025-07-07T22:18:26Z
Closed: 2025-07-14T09:30:39Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9121

## Opening post (belforte, 2025-07-07T22:18:26Z)

when here's a network problem or Rucio is down, we want to retry, waiting even tens of minutes, but when the call raises an exception to signal a "normal situation", like the very common "rule already exist" we do not want to retry.

e.g. when processing a dataset a second time:
```
2025-07-08 00:04:57,493:INFO:RucioUtils,88:Rucio server v.37.5.0 contacted
2025-07-08 00:04:57,517:INFO:RucioUtils,90:Rucio client initialized for crab_input in status ACTIVE
2025-07-08 00:04:57,517:INFO:RucioActions,260:Lock /GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM on disk
2025-07-08 00:04:58,891:WARNING:RucioUtils,27:Failed to execute 'add_replication_rule' (attempt 1/3): A duplicate rule fo
r this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
2025-07-08 00:08:00,621:WARNING:RucioUtils,27:Failed to execute 'add_replication_rule' (attempt 2/3): A duplicate rule fo
r this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
2025-07-08 00:11:02,487:WARNING:RucioUtils,27:Failed to execute 'add_replication_rule' (attempt 3/3): A duplicate rule fo
r this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
2025-07-08 00:11:02,487:ERROR:RucioUtils,35:Operation 'add_replication_rule' failed after 3 attempts
2025-07-08 00:11:02,487:DEBUG:RucioActions,90:A duplicate rule for this account, did, rse_expression, copies already exis
ts. Use that
2025-07-08 00:11:02,507:DEBUG:RucioActions,93:List of existing rules for this DID
2025-07-08 00:11:02,508:DEBUG:RucioActions,96:id: %s account: %s activity %s
[...]
2025-07-08 00:11:02,531:DEBUG:RucioActions,96:id: %s account: %s activity %s
2025-07-08 00:11:02,531:DEBUG:RucioActions,96:id: %s account: %s activity %s
2025-07-08 00:11:02,561:INFO:RucioActions,290:Created Rucio rule ID: 6137512fd9334b8b81fd602a1f7d9f41
```

As a secondary note, those messages go to the mail log (twlog.txt) but not to the task-specific log. 
Also there seems to be a formatting problem with `DEBUG:RucioActions,96:id: %s account: %s activity %s`

## Comment (belforte, 2025-07-08T14:59:39Z)

this is making ASO/Rucio spend all its 15minutes in useless sleep loops and eventually timeout, e.g.
```
[2025-07-08 00:24:20,663] [RucioTransfer.Actions.BuildDBSDataset] [INFO] Add replication rule to container "user.belforte:/GenericTTbar/belforte-ruciotransfers-1751925741-94ba0e06145abd65ccb1d21786dc7e1d/USER
[2025-07-08 00:24:20,727] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_replication_rule' (attempt 1/3): A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
[2025-07-08 00:27:20,900] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_replication_rule' (attempt 2/3): A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
[2025-07-08 00:30:21,094] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_replication_rule' (attempt 3/3): A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
[2025-07-08 00:30:21,094] [RucioTransfer.RucioClient] [ERROR] Operation 'add_replication_rule' failed after 3 attempts
[2025-07-08 00:30:21,094] [RucioTransfer.Actions.BuildDBSDataset] [INFO] Rule already exists. Get rule ID from Rucio.
```
also

```
[2025-07-08 10:38:31,109] [RucioTransfer.Actions.BuildDBSDataset] [DEBUG] Creating dataset /GenericTTbar/belforte-ruciotransfers-1751925741-94ba0e06145abd65ccb1d21786dc7e1d_TRANSFER.61980e08/USER#LOGS
[2025-07-08 10:38:31,163] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_dataset' (attempt 1/3): Data Identifier Already Exists.
Details: Data Identifier already exists!
[2025-07-08 10:41:31,265] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_dataset' (attempt 2/3): Data Identifier Already Exists.
Details: Data Identifier already exists!
[2025-07-08 10:44:31,409] [RucioTransfer.RucioClient] [WARNING] Failed to execute 'add_dataset' (attempt 3/3): Data Identifier Already Exists.
Details: Data Identifier already exists!
[2025-07-08 10:44:31,409] [RucioTransfer.RucioClient] [ERROR] Operation 'add_dataset' failed after 3 attempts
```

etc.

## Comment (aspiringmind-code, 2025-07-09T11:30:14Z)

After the fix, add_replication_rule treated as Non-HTTP exception
```
2025-07-09 12:18:12,614:INFO:RucioUtils,58:Initializing native Rucio client
2025-07-09 12:18:12,614:DEBUG:RucioUtils,80:Using cert [/data/certs/robotcert.pem]
 and key [/data/certs/robotkey.pem] for rucio client.
2025-07-09 12:18:12,626:INFO:RucioUtils,95:Rucio server v.37.5.0 contacted
2025-07-09 12:18:12,639:INFO:RucioUtils,97:Rucio client initialized for crab_input in status ACTIVE
2025-07-09 12:18:12,639:INFO:RucioActions,260:Lock /GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM on disk
2025-07-09 12:18:13,769:ERROR:RucioUtils,41:Non-HTTP exception in 'add_replication_rule': A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 25, in wrapper
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 71, in add_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.DuplicateRule: A duplicate rule for this account, did, rse_expression, copies already exists.
```

## Comment (belforte, 2025-07-09T12:26:01Z)

thanks @aspiringmind-code .
Yet I was worried that catching HTTP exceptions may not be enough, I am not sure where the following [*] exactly originates, I thought it was "something went wrong in client/server communiction and we got an empty response" . Should we only immediately re-raise client exceptions of class `RucioException` ?
Or this (alas rather common) error due to a bug on our side ? Or a bug inside Rucio ?
I admit that I have not investigated thought it is certainly off that `rucioClient.list_replica_locks(ruleId)` fails om JSON parsing.

[*]
```text


49 rules exist for activity: Analysis TapeRecall
skip 0 rules created by 'transfer_ops'. 49 are left
state
OK             34
REPLICATING     6
STUCK           8
SUSPENDED       1
dtype: int64
finding tape source for all pending rules (takes some time...)
finding target RSE for all pending rules (takes some time...)
^[[33;1m2025-07-09 14:13:48,744	WARNING	Waiting 0.25s due to reason: server returned 502 ^[[0m
Waiting 0.25s due to reason: server returned 502 
^[[33;1m2025-07-09 14:13:54,393	WARNING	Waiting 0.5s due to reason: server returned 502 ^[[0m
Waiting 0.5s due to reason: server returned 502 
^[[33;1m2025-07-09 14:13:54,900	WARNING	Waiting 1.0s due to reason: server returned 502 ^[[0m
Waiting 1.0s due to reason: server returned 502 
Traceback (most recent call last):
  File "/data/srv/monit/CheckTapeRecall.py", line 466, in <module>
    main()
  File "/data/srv/monit/CheckTapeRecall.py", line 114, in main
    pendingCompact = createRulesDataframe(pending, rucio, crab, logger)
  File "/data/srv/monit/CheckTapeRecall.py", line 162, in createRulesDataframe
    pending['dest'] = pending.apply(lambda x: findDestForRule(rucio, x.id), axis=1)
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 9423, in apply
    return op.apply().__finalize__(self, method="apply")
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 678, in apply
    return self.apply_standard()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 798, in apply_standard
    results, res_index = self.apply_series_generator()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 814, in apply_series_generator
    results[i] = self.f(v)
  File "/data/srv/monit/CheckTapeRecall.py", line 162, in <lambda>
    pending['dest'] = pending.apply(lambda x: findDestForRule(rucio, x.id), axis=1)
  File "/data/srv/monit/CheckTapeRecall.py", line 335, in findDestForRule
    aLock = next(rucioClient.list_replica_locks(ruleId))
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 237, in list_replica_locks
    exc_cls, exc_msg = self._get_exception(r.headers, r.status_code)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/baseclient.py", line 302, in _get_exception
    data = parse_response(data)
  File "/usr/local/lib/python3.8/site-packages/rucio/common/utils.py", line 426, in parse_response
    return json.loads(data, object_hook=datetime_parser)
  File "/usr/local/lib/python3.8/json/__init__.py", line 341, in loads
    raise TypeError(f'the JSON object must be str, bytes or bytearray, '
TypeError: the JSON object must be str, bytes or bytearray, not NoneType

```

## Comment (aspiringmind-code, 2025-07-09T12:35:08Z)

exceptions of just RucioException is a good idea imo.

## Comment (belforte, 2025-07-09T12:35:52Z)

I may have spoken too soon, I edite comment above to report full stdout and now I notice that server reported HTTP 502., client tried 3 times in quick succession (as known) and eventually ... I am not sure, maybe it went ahead and tried to preocess the empty body received together with HTTP 502 and hence the JSON error'.

This means that error is no easy to reproduce/investigate, since it requires server to fail with 502 to begin with :-(

## Comment (aspiringmind-code, 2025-07-09T12:37:27Z)

Should I edit the code to separately catch for 502 to test?

## Comment (belforte, 2025-07-09T12:49:49Z)

Looking at Rucio's BaseClient code we will never get the HTTP exception. 
```python
[...]
     STATUS_CODES_TO_RETRY = [502, 503, 504]
[...]
   for retry in range(self.AUTH_RETRIES + 1):
            try:
              [...]
                self.logger.debug("HTTP Response: %s %s" % (result.status_code, result.reason))
                if result.status_code in STATUS_CODES_TO_RETRY:
                    self._back_off(retry, 'server returned {}'.format(result.status_code))
                    continue
```
so when it get 502, it backs off (sleep) up to 3 times, and then it just skips forward to code outside that `for` loop.

IIUC, of course.

There's still one thing I do not understand, I would thing that in that case, or if HTTP code is not 502,3,4 , we hit this code a bit later
```python
        if result is None:
            raise ServerConnectionException
```
so we may expect a very clear exception. But since this BaseClient is always called by other "clients" like RuleClient  in that case, it all depends on exception handling in those. 
Also I am not sure which version of the code I have in my GH clone

pff...

## Comment (belforte, 2025-07-09T13:01:14Z)

I stand corrected, the only way to get e.g. HTTP 502 is that the GET returns a non empty `result` with the `result.status_code==502`` and so nobody raises anything until the client tries to load the JSON data from `return`.

oh well... 

TLDR: "exceptions of just RucioException is a good idea"

## Comment (aspiringmind-code, 2025-07-09T13:30:16Z)

Thanks @belforte for the investigation. `RucioException` added in latest [commit](https://github.com/dmwm/CRABServer/compare/master...aspiringmind-code:CRABServer:fix9121) Will test with the [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12404149)
