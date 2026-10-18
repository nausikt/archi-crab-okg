# dmwm/CRABServer issue #7842: refactor Publisher_rucio

State: closed
Opened: 2023-08-18T18:59:48Z
Closed: 2023-08-24T21:03:16Z
Labels: Area: Code Cleanup, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7842

## Opening post (belforte, 2023-08-18T18:59:48Z)

there is a lot of code duplicated in  TaskPublish vs. TaskPublishRucio and PublishMaster vs. PublisherMasterRucio

Move common funcions to a separate PublisherUtils.py and reuse.
This also makes code more readable since TaskPublish* is too long

## Comment (belforte, 2023-08-22T08:52:53Z)

good progress in https://github.com/belforte/CRABServer/tree/refactor-TaskPublishRucio

## Comment (belforte, 2023-08-22T13:28:26Z)

current problem is that somehow log says that it marked all files as good, but only 20 files are moved from acquired to done at each iteration... 
I am trying to reproduce that

that was likely due to the bug in `findParentBlocks` which I just fixed. All looks good now.

## Comment (belforte, 2023-08-22T14:32:47Z)

I need to put some order with block names:
 - [x] key in dictionary: `block_name` (same as DBS requires) as already in TaskPublish.py
 - [x] variable to indicate a block in code `blockName`

## Comment (belforte, 2023-08-23T12:35:26Z)

progress so far capitalized in https://github.com/dmwm/CRABServer/pull/7849

## Comment (belforte, 2023-08-24T13:31:45Z)

for all values which end in DBS I try to keep dictionary keys named like in DBS (`global_tag`, `release_version` etc.) and the name of the variable containing the value to follow usual LazyCamel (`globalTag`, `releaseVersion` etc.). Hopefully this will help not to get lost with so many similarly named things.

## Comment (belforte, 2023-08-24T15:12:08Z)

the above, more cleanup, and a switch to publish in `int/phys03` so to force input migration is now in https://github.com/belforte/CRABServer/tree/more-refactoring
