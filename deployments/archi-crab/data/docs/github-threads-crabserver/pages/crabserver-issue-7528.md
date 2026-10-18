# dmwm/CRABServer issue #7528: allow single block taperecall for any Tier

State: closed
Opened: 2023-02-09T22:56:26Z
Closed: 2023-02-17T16:19:12Z
Labels: Type: Enhancement, Priority: High, Area: zDATA RECALL, Status: Available
URL: https://github.com/dmwm/CRABServer/issues/7528

## Opening post (belforte, 2023-02-09T22:56:26Z)

when users request a single block we should allow any data tier.
Optionally allow also multiple blocks but have a cap on total size.

@novicecpp is the natural "volunteer" for this given his recent work on #7525 but others can also do, including  me.

## Comment (novicecpp, 2023-02-10T15:18:03Z)

How about
```
config.TaskWorker.tiersToRecall = ['AOD', 'AODSIM', 'MINIAOD', 'MINIAODSIM', 'NANOAOD', 'NANOAODSIM']
config.TaskWorker.tiersToBlockRecall = ['RAW', 'RECO']
config.TaskWorker.maxTierToBlockRecallSizeGB = 1024
```

and another `elif` check in [DBSDataDiscovery.py#L461
](https://github.com/dmwm/CRABServer/blob/9f6fd04c5061a3dce9a38718d4363be1142dfbc6/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L461)
```diff
diff --git a/src/python/TaskWorker/Actions/DBSDataDiscovery.py b/src/python/TaskWorker/Actions/DBSDataDiscovery.py
index ebfd8acf..722cadf6 100644
--- a/src/python/TaskWorker/Actions/DBSDataDiscovery.py
+++ b/src/python/TaskWorker/Actions/DBSDataDiscovery.py
@@ -470,6 +470,9 @@ class DBSDataDiscovery(DataDiscovery):
                 msg += "\nWill try to request a full disk copy for you. See"
                 msg += "\n https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul"
                 self.requestTapeRecall(blockList=blocksWithLocation, system='Rucio', msgHead=msg)
+            elif inputBlocks and dataTier in getattr(self.config.TaskWorker, 'tiersToBlocksRecall', []): # and total_size_from_dbs(blockwithLocation) < maxAllowRecallSize
+                msg = "recall block"
+                self.requestTapeRecall(blockList=blocksWithLocation, system='Rucio', msgHead=msg)
             else:
                 msg = "Some blocks are on TAPE only and will not be processed."
                 msg += "\nThere is no automatic recall from tape for data tier %s" % dataTier

```

?

## Comment (belforte, 2023-02-10T15:25:02Z)

perfect !!
