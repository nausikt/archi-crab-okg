# dmwm/CRABServer issue #7573: allow processing of incomplete blocks

State: closed
Opened: 2023-03-27T15:28:08Z
Closed: 2023-04-02T18:50:03Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7573

## Opening post (belforte, 2023-03-27T15:28:08Z)

when user specifies `partialDataset=True` in task submission configuration:

 * current behavior is to process whatever blocks are on disk w/o triggering a tape recalls
 * we should extend to process whatever files are on disk, including inomplete block replicas.

See some discussion e.g. in [CMS-talk](https://cms-talk.web.cern.ch/t/cannot-find-any-valid-file-inside-the-dataset/20761/27)

Note that [our documentation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile) already says:
```
Allow to process input dataset that is only partially on disk.
Normally, when CRAB finds out that some files of the input dataset are not fully replicated on disk,
CRAB will issue tape recall to Rucio and wait for all files to be on disk before running the task.
If partialdataset is True, CRAB will submit task to condor immediately without request tape recall
and process the files currently on disk
```

 - [x] change code
 - [x] update documentation

## Comment (belforte, 2023-03-28T14:49:17Z)

An initial quick implementation would be to change this
https://github.com/dmwm/CRABServer/blob/e2e09dde7ebedf1450df67450e3c77bda03c113f/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L356
to be
```python
    if item['state'].upper() == 'AVAILABLE' or usePartialDataset:
```

## Comment (belforte, 2023-03-28T14:51:44Z)

the only shortcoming that we see is in the case that the parially available blocks are at multiple sites, that will cause jobs to run at ANY of those sites, regardless if they host full replica or only one file. Those use cases are hopefully rare and we rely on:
* if users said: `usePartialDataset` . They must be happy with whatever they get and ignore file read errors (8028)

## Comment (belforte, 2023-03-29T23:18:29Z)

I have coded so that:
- if a block has full replicas, use those RSE's
- otherwise use all RSE's which have (part of) the block
and of course keep skipping blocks which are only on tape
