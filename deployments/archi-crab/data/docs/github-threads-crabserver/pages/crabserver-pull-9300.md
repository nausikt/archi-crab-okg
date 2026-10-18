# dmwm/CRABServer pull request #9300: Mitigate terminally failed migration baseline by adding jitter delays between our Publisher DBS API calls.

State: closed
Opened: 2026-04-17T23:45:06Z
Closed: 2026-04-18T08:55:33Z
Merged: 2026-04-18T08:55:33Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/pull/9300

## Opening post (nausikt, 2026-04-17T23:45:06Z)

Resolve #9299 

## Summary
When processing many tasks with 100-200+ blocks simultaneously, the Publisher fires rapid back-to-back
DBS API calls (submitMigration, statusMigration, listBlocks, insertBulkBlock) with
no delay between requests (Like a mini-While-True loop). 

This overwhelms/break the DBS server or cms-auth-proxy or may trigger CERN firewall appliances, causing rate-limiting or intermittent/abrupt connection drops, resulting in empty responses or errors, which make files stuck in the acquire-status checking loop and eventually misclassified as terminal migration failures, leaving them permanently stuck in the Acquire state.

## So this PR will resolved/mitigated the issues by:
Added randomized jitter delays (random.uniform) between DBS API calls in:
- `findParentBlocks` — after each parent file lookup round (0.1-0.3s)
- `migrateByBlockDBS3` — between migration submissions (0.2-0.5s)
- `migrateByBlockDBS3` — between migration status checks (0.2-0.5s)
- `TaskPublish.publishInDBS3` — between block insertions (0.2-0.5s)
- `TaskPublishRucio.publishInDBS3` — between block insertions (0.2-0.5s)

## Why **Jitter** (randomized sleep)? 
it is used instead of fixed sleep to prevent multiple concurrent Publisher processes from synchronizing, self-organized criticality of hitting DBS simultaneously with same IP.

## Expectations
- [ ] Publisher logs show expected delays between DBS calls.
- [ ] Terminally failed migration, which not running out of their retry_count=10 yet, can make a progress, completed their migrations, or been able to resubmitted request new migrations.
- [ ] Acquired file backlog should decreases over time, since we have less and less terminally failures. 
*(Of course, with some kick, manually resubmit, but may never have to **blacklist** tasks?)*

______
*My suggestion is that we should release this PR ASAP to prevent new submissions from getting stuck and to rescue some migrations that are still recoverable or retryable.*
P.S. we've reached all-time-high O(112k) now.

## Comment (cmsdmwmbot, 2026-04-17T23:49:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 8 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2799/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-04-18T00:26:17Z)

Here’s our bug reproduced result `Expecting value: line 1 column 1 (char 0)` inside `crab-prod-tw01`.

When we ran DBSApi calls almost sequentially for just 77 blocks in a while True loop, we unable to maintain pinging for longer than a minute; [1] it failed with the same empty responses. 

But when we added a little bit of jitter delay (10 ms) inside the loop, we could keep pinging almost indefinitely fine w/o such an error.

[1]
```bash
[crab3@crab-prod-tw01 migrations]$ python3 pingDBS.py
2026-04-17 23:32:01 {1: 5, 9: 62, 2: 10}
2026-04-17 23:32:01 {1: 5, 9: 62, 2: 10}
2026-04-17 23:32:02 {1: 5, 9: 62, 2: 10}
2026-04-17 23:32:03 {1: 5, 9: 62, 2: 10}
2026-04-17 23:32:04 {1: 5, 9: 62, 2: 10}
....
2026-04-17 23:32:46 {1: 5, 9: 62, 2: 10}
Migration status query for block {'block_name': '/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/MINIAODSIM#1cbae68d-6631-48dd-ac20-ad644d726f15'} failed
DBS3 exception: Expecting value: line 1 column 1 (char 0)
Traceback (most recent call last):
  File "/data/srv/Publisher/logs/migrations/pingDBS.py", line 28, in <module>
    raise ex
  File "/data/srv/Publisher/logs/migrations/pingDBS.py", line 22, in <module>
    status = migrateApi.statusMigration(block_name=block['block_name'])
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 1855, in statusMigration
    return self.__callServer("status", params=kwargs)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 486, in __callServer
    self.__parseForException(data)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 514, in __parseForException
    data = json.loads(data)
  File "/usr/lib64/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python3.9/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Comment (nausikt, 2026-04-18T08:51:52Z)

Since this patch can't do no harm and quite trivial but hold potential to resolves the issues.

I’ll merge and release to prod now, with subsequent gradual resubmissions of migrations as I see fit.

## Comment (nausikt, 2026-04-22T19:47:04Z)

This was off the point, so i've reverted #9304 as Stefano pointed out https://github.com/dmwm/CRABServer/issues/9303#issuecomment-4298184190
