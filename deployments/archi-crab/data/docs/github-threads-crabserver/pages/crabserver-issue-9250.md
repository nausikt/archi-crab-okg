# dmwm/CRABServer issue #9250: Protect CheckTapeRecall.py from rules being deleted

State: open
Opened: 2025-12-17T11:31:23Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9250

## Opening post (belforte, 2025-12-17T11:31:23Z)

this is an interesting case of a rule being deleted while the script is running,
CheckTapeRecall starts by getting a list of rules from Rucio and later
one of them is not found.
FYI @nausikt wrt to one mail we got today from crab-dev-tw02

<br>-------- Forwarded Message --------
Subject: | Cron  <crab3@crab-dev-tw02> export loguuid=$(uuidgen);                 test -f /home/crab3/runContainer.sh &&                bash  /home/crab3/runContainer.sh -v v3.latest                -s  TaskWorker_monit_checktaperecall -u ${loguuid}                -c  'python3 /data/srv/monit/CheckTapeRecall.py'                 >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ] &&                 cat /tmp/monit-${loguuid}.txt
-- | --
Wed, 17 Dec 2025 00:15:35 +0100
(Cron Daemon) <crab3_crab-dev-tw02@cern.ch>
cms-service-crab-operators@cern.ch





```
127 rules exist for activity: Analysis TapeRecall
skip 0 rules created by 'transfer_ops'. 127 are left
state
OK             33
REPLICATING    88
STUCK           6
dtype: int64
finding tape source for all pending rules (takes some time...)
finding target RSE for all pending rules (takes some time...)
Add (DBS) dataset name ...
Fatal exception in 'get_replication_rule' : No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RuleNotFound: No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found
Type of Exception: <class 'rucio.common.exception.RuleNotFound'>
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RuleNotFound: No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found
repr(): RuleNotFound('No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found')
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RuleNotFound: No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RuleNotFound: No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found
Traceback (most recent call last):
  File "/data/srv/monit/CheckTapeRecall.py", line 466, in <module>
    main()
  File "/data/srv/monit/CheckTapeRecall.py", line 114, in main
    pendingCompact = createRulesDataframe(pending, rucio, crab, logger)
  File "/data/srv/monit/CheckTapeRecall.py", line 165, in createRulesDataframe
    pending['dataset'] = pending.apply(lambda x: findDatasetForRule(rucio, x.id), axis=1)
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 9423, in apply
    return op.apply().__finalize__(self, method="apply")
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 678, in apply
    return self.apply_standard()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 798, in apply_standard
    results, res_index = self.apply_series_generator()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 814, in apply_series_generator
    results[i] = self.f(v)
  File "/data/srv/monit/CheckTapeRecall.py", line 165, in <lambda>
    pending['dataset'] = pending.apply(lambda x: findDatasetForRule(rucio, x.id), axis=1)
  File "/data/srv/monit/CheckTapeRecall.py", line 349, in findDatasetForRule
    rule = rucioClient.get_replication_rule(ruleId)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 73, in call
    return attr(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 108, in get_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RuleNotFound: No replication rule found.
Details: No rule with the id 2a0ec244c2ee48499f930112fcb0f924 found

```
