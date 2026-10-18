# dmwm/CRABServer issue #7530: improve tape recall policies

State: closed
Opened: 2023-02-10T11:34:43Z
Closed: 2023-04-20T10:43:24Z
Labels: Type: Question, RUCIO, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7530

## Opening post (belforte, 2023-02-10T11:34:43Z)

after discussing with DM experts in Rucio/cms-ops channeI in slack, and in light of the fact that lately many CRAB taper recalls end up with several disk-disk transfers,  believe there's some easy improvement that we can do our side
- [x] better detect existing rules by avoiding adding "which RSE" in the target list
   * this requires a different name for the container, common to multiple tasks: #7603 
https://github.com/dmwm/CRABServer/blob/c484c2377476c3eeca32207fc4d2117bfdf714e2/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L194-L205
   * anyhow is not really a policy. So mark here as done and will follow up in the above issue
- [x] tell apart "fully on tape" from "partily on disk" datasets and avoid using grouping=all for the latter. Hopefully then Rucio will not move files already on disk.
   * **NOTE added Apr 14**: all in all the fragmented datasets was a transient thing, eventually it will be gone or very much reduced. So I will do nothing here. And possibly think again in light of new/better evidence later on.
- [x] avoid tape recalls across Atlantic : #7589

## Comment (belforte, 2023-02-10T11:42:35Z)

@KatyEllis  please have a look and tell me if this makes sense. Also advice on priority. I am inclined to set aside "publishing in DBS when using Rucio for ASO" for a couple days and do this instead. What do you think ?
@dciangot I do not know if you have time for such things, but your opinion will also be welcome

In particular I think that existing check `rucioClient.list_did_rules(myScope, containerName)` is useless since we name containers with the task name which changes at each `crab submit`. Should we put there the DBS-dataset name instead ? Or simply look for rules rucio-dataset by rucio-dataset ? Questions for Martin ?

## Comment (belforte, 2023-03-10T16:16:27Z)

I do not find a simple way to check for existing rules nor am sure which action would be best.
All in all, even if some dataset/block has a rule duplicated a few times.. what's the harm ?

I am inclined to say that there is nothing to do here.
@KatyEllis @dciangot

## Comment (belforte, 2023-03-10T21:15:18Z)

I found that if multiple tasks are submitted for same dataset on tape, Rucio may easily end up in making multiple disk copies at various sites. But I also do not see any simple way to fix.

## Comment (belforte, 2023-03-10T21:19:54Z)

hmm.. I am not so sure of above comment. There are odd things around, but can't really tell why

## Comment (belforte, 2023-04-20T10:43:24Z)

We have no other high level policy change in our list at this moment
