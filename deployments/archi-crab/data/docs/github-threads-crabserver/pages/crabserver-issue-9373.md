# dmwm/CRABServer issue #9373: DID not found exception in ReportRecallQuota.py and CheckTapeRecall.py

State: closed
Opened: 2026-07-30T17:19:01Z
Closed: 2026-07-31T12:52:49Z
URL: https://github.com/dmwm/CRABServer/issues/9373

## Opening post (belforte, 2026-07-30T17:19:01Z)

today every monitoring cron is sending mail with following message.
Looks like there is a problematic DID.
We need to deal with that "silently" !
Here's example from CheckTapeRecall.py. The other script ReportRecallQuota.py send the same, just w/o anything before

```text
62 rules exist for activity: Analysis TapeRecall
skip 0 rules created by 'transfer_ops'. 62 are left
state
OK             35
REPLICATING    19
STUCK           3
SUSPENDED       5
dtype: int64
finding tape source for all pending rules (takes some time...)
Fatal exception in 'list_files' : Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 399, in list_files
    raise exc_cls(exc_msg)
rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found
Type of Exception: <class 'rucio.common.exception.DataIdentifierNotFound'>
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 399, in list_files
    raise exc_cls(exc_msg)
rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found
repr(): DataIdentifierNotFound("Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found")
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 399, in list_files
    raise exc_cls(exc_msg)
rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 399, in list_files
    raise exc_cls(exc_msg)
rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found
Traceback (most recent call last):
  File "/data/srv/monit/CheckTapeRecall.py", line 466, in <module>
    main()
  File "/data/srv/monit/CheckTapeRecall.py", line 114, in main
    pendingCompact = createRulesDataframe(pending, rucio, crab, logger)
  File "/data/srv/monit/CheckTapeRecall.py", line 158, in createRulesDataframe
    pending['tape'] = pending.apply(lambda x: findTapesForRule(rucio, x.id), axis=1)
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 9423, in apply
    return op.apply().__finalize__(self, method="apply")
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 678, in apply
    return self.apply_standard()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 798, in apply_standard
    results, res_index = self.apply_series_generator()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 814, in apply_series_generator
    results[i] = self.f(v)
  File "/data/srv/monit/CheckTapeRecall.py", line 158, in <lambda>
    pending['tape'] = pending.apply(lambda x: findTapesForRule(rucio, x.id), axis=1)
  File "/data/srv/monit/CheckTapeRecall.py", line 319, in findTapesForRule
    aFile = next(rucioClient.list_files(scope=rule['scope'], name=rule['name']))
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/didclient.py", line 399, in list_files
    raise exc_cls(exc_msg)
rucio.common.exception.DataIdentifierNotFound: Data identifier not found.
Details: Data identifier 'cms:/%2FZeroBias%2FRun2024H-PromptReco-v1%2FAOD' not found


```

## Comment (belforte, 2026-07-30T17:19:24Z)

FYI @nausikt

## Comment (belforte, 2026-07-30T17:40:58Z)

OTOH the error likely indicates a general problem with Rucio, any DID resutls in :

belforte@lxplus808/TC3> rucio list-content cms:/Muon0/Run2025F-PromptReco-v1/MINIAOD
2026-07-30 19:31:30,767	ERROR	Data identifier not found.
Details: Data identifier 'cms:/%2FMuon0%2FRun2025F-PromptReco-v1%2FMINIAOD' not found
belforte@lxplus808/TC3>

## Comment (belforte, 2026-07-31T12:52:49Z)

Rucio server problem was fixed and problem is gone. I guess that if Rucio is down we can't avoid getting a mail from every crontab.
So I am closing.
