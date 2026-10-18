# dmwm/CRABServer issue #9184: Publisher should not try to migrate blocks which are already at destination

State: closed
Opened: 2025-09-11T14:01:52Z
Closed: 2025-09-11T14:54:47Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9184

## Opening post (belforte, 2025-09-11T14:01:52Z)

While debugging obscure [failed migrations in DBS](https://github.com/dmwm/dbs2go/issues/146) I noticed that [TaskPublish/[y](https://github.com/dmwm/CRABServer/blob/master/src/python/Publisher/TaskPublish.py) tries to migrate all parent blocks, even if they are already at destination.

Usually this is "stupid by harmless" since DBS returnas HTTP 400 and points to the migration which originally put the block in phys03, so TaskPublish checks status of that, finds OK., and goes on happily.

In the case of that issue, the original migration was marked as terminlly failed, and things never recover.

Yet is would be lighter on DBS and more elegant that we check which blocks are at destination and only migrate the missing ones.

## Comment (belforte, 2025-09-11T14:10:59Z)

hmm... we already have such code ! Only look for parent blocks for files which are not in PHYS03
https://github.com/dmwm/CRABServer/blob/4090bc52d466408f02a972270987cc3165762e7b/src/python/Publisher/PublisherDbsUtils.py#L129-L136

Is it possible that we have some files which are not in PHYS03, yet the block was (incompletely) migrated ? Current code does not check for this and will insert a new migration request.

## Comment (belforte, 2025-09-11T14:54:47Z)

Indeed that's exactly what happened
```console
belforte@lxplus813/~> dasgoclient --query 'file block=/BToPhi_MPhi-0p7_ctau-10mm_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM#95a97811-3258-44aa-a400-1fd406bf5d7b instance=prod/global'
/store/mc/Run3Summer22DRPremix/BToPhi_MPhi-0p7_ctau-10mm_TuneCP5_13p6TeV_pythia8/AODSIM/124X_mcRun3_2022_realistic_v12-v2/70000/aa1bb70c-6b2e-4202-97b1-c84eb77ebb97.root
belforte@lxplus813/~> dasgoclient --query 'file block=/BToPhi_MPhi-0p7_ctau-10mm_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM#95a97811-3258-44aa-a400-1fd406bf5d7b instance=prod/phys03'
belforte@lxplus813/~> 
```

The problem is that inserting a block is expected to be an atomic operation iN DBS. IIUC DBS has no way to add files to an existing block.
So the partially migrated block will fail forever.

There is nothing that I can do from CRAB side.
