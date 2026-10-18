# dmwm/CRABServer issue #7538: add support for indicating a Rucio container as input

State: closed
Opened: 2023-02-16T17:33:17Z
Closed: 2023-03-10T14:08:20Z
Labels: Status: Done, RUCIO, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7538

## Opening post (belforte, 2023-02-16T17:33:17Z)

* allow processing of a set of files described only by a Rucio container, no DBS.
 * only allow `splittingByFile` in this case.
 * do not allow a secondary dataset

User will specify something like:
```
config.Data.InputDataset = 'scope:container'
or
config.Data.RucioContainer = 'scope:container'
```
(which needs a corresponding CRABClient issue). But from CRABServer side we should assume
that somehow the `scope:container` did makes it to TW/DBSDataDiscovery , possibly reusing existing
`tm_dbs_url` and `tm_input_dataset`

FYI @dciangot

## Comment (belforte, 2023-02-17T09:24:21Z)

I am currently leaning toward:
* keep `tm_input_dataset` as is with the dataset(container) name
* use the new functionality to store a `key:value` in `tm_user_config` to store a possible Rucio scope, and check for it very early in DBSDataDiscovery . Then the DID to be used for data discovery will be:
```python
    did =  kwargs['task','tm_user_config','rucioScope'] + ':' +  kwargs['task','tm_input_dataset']
```
- [x] check how this will interact with new blocklist feature ? Is this useful ? Can surely leave for later.

## Comment (belforte, 2023-02-22T17:05:45Z)

I have tried to modify [DBSDataDiscovery](https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/DBSDataDiscovery.py) adding `if` statements here and there.
But that makes it hard to read and to get right w/o breaking things. I gave up after a few days trying.

I am leaning toward adding a new `RucioDataDiscovery` instead to be instantiated in the [Handler](https://github.com/dmwm/CRABServer/blob/518c4760055b4ee232129209ccfaf428a69c28dd/src/python/TaskWorker/Actions/Handler.py#L157-L161) like
```python
    if task['tm_job_type'] == 'Analysis':
        if task.get('tm_user_files'):
            handler.addWork(UserDataDiscovery(config=config, crabserver=crabserver, procnum=procnum))
        elif task.get('tm_user_config') and task['tm_user_config'].get('rucio_scope'):
            handler.addWork(RucioDataDiscovery(config=config, crabserver=crabserver, procnum=procnum, rucioClient=rucioClient))
        else:
            handler.addWork(DBSDataDiscovery(config=config, crabserver=crabserver, procnum=procnum, rucioClient=rucioCl
```
Advantages:
 *  I can't break current functionality

Disadvantages:
 * have to maintain same code in two places

So I may do a first implementation with a lot of replicated code (in progress), but the way to go is to refactor  [DBSDataDiscovery](https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/DBSDataDiscovery.py) to be simple skeleton which may change for `DBSDataDiscovery` vs `RucioDataDiscovery` and a set of common functions to do "all work". 

That step  may indeed be disruptive. I will need @novicecpp help to minimize chances of regression.

I gladly accept input on how to proceed otherwise, of course @mapellidario @dciangot @novicecpp 
we can talk about it tomorrow e.g.

## Comment (belforte, 2023-02-27T22:56:56Z)

this will be done with the above CRABServer PR and with [this](https://github.com/dmwm/CRABClient/pull/5189) PR in CRABClient where the new configuration parameter is introduced:
```python
config.Data.rucioScope = 'scope'
# examples
config.Data.rucioScope = 'cms'
config.Data.rucioScope = 'user.belforte'
```
I am nor sure if there's any value in supporting alternative syntax as well:
```python
config.Data.InputDataset = 'scope:container'
```
it is just more work[1] for ... which gain ?

[1] e.g. one of these:
* change client to parse and send rucioScope anyhow, but so fare client does never do this kind of manipulations
* change inputDataset validation in REST and possibly split it there and fill different DB fields
* change inputDataset validation in REST, pass it along with possibly `scope:` in front and parse it early in the task handling when deciding which DataDiscovery action to instantiate for this task. Makes it more complex what is now very straighforward code.

## Comment (belforte, 2023-03-01T10:54:41Z)

an initial implementation of this is in #7556 
But that is not a good solution yet. Will keep this open even if we merge that.

Things to decide/do:

- [x] Fully implement support for Rucio DIDs in crabConfig even if name does not fit DBS lexicon for inputDataset
- [x] Do we do that via a new DB column, or adding to `tm_user_config` ? 
- [x] Do we report bad configuration in TW or directly in REST ? (e.g. attemption split by lumi  with Rucio)
- [ ] more ?

## Comment (belforte, 2023-03-01T17:16:25Z)

Curent plan, @dciangot please review (expecially last part about what we do not support
- no changes to CRABClient
- user specifies a Rucio did in place of data.inputDataset
- REST is modified (slightly) to allow storing it in `tm_input_dataset` ( a new `RX_RUCIODID` regexp is introduced to validate a Rucio DID)
- Handler.py decides if to put DBSDataDiscover or RucioDataDiscovery in the action list for this task
- RucioDataDiscovery assumes a proper DID in  `tm_input_dataset` : `scope:container` and does the needed
- in RucioDataDiscovery we 
   * fail if splitting is not `FileBased`
   * fail is `secondary dataset` or `use_parents` in user config (no parentage, no lumi info in Rucio)
   * ignore inputblocks (if user wants a smaller container, they create it in Rucio).
   * ignore tape locations
   * do not support tape recall (do not want people to use cms:/a/b/RAW to go around limits iin DBSDataDiscovery)
   * automatically support partialDataset, since there is no tape recall it is straightforward to only use the blocks with a valid replica

That should do at least for the use case of "user creates some data locally ON DISK" and wants to register them in Rucio.

Those "not support" also minimize code overlap with DBSDataDiscovery !

Should those data ever go on tape I think we should assume the policy that "it is up to user to do this, if and when and where user will have access to a tape storage". So it will be user problem to retrieve from tape to disk before using in CRAB input.

Should we ever come to "some official production CMS data are only described as a Rucio container, not in DBS"... well... we will review and recode.

## Comment (belforte, 2023-03-06T16:59:34Z)

Implementation of plan as in https://github.com/dmwm/CRABServer/issues/7538#issuecomment-1450525216 is now complete in https://github.com/dmwm/CRABServer/pull/7556

Some final cleanup and this can be closed.

- [x] update documentation
