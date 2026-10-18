# dmwm/CRABServer issue #8411:  AdjustSites.py race condition

State: closed
Opened: 2024-05-16T06:13:02Z
Closed: 2024-05-16T16:32:02Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8411

## Opening post (novicecpp, 2024-05-16T06:13:02Z)

There is race condition where [AdjustSites.py#L393](https://github.com/dmwm/CRABServer/blob/d4b13331e9d5d5ab4656d0ff58beb67f787e64a7/scripts/AdjustSites.py#L393) is executed before TW could set task status to `SUBMITTED` 

For example, with this task [240514_130645:crabint1_crab_rucio_transfers_20240514_150644](https://cmsweb-test12.cern.ch/crabserver/ui/task/240514_130645%3Acrabint1_crab_rucio_transfers_20240514_150644). The task status msg reported boostrap failure:

```
The task failed to bootstrap on the Grid scheduler. Crab resubmit will not work. Please send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch.
Hold reason: 'This dagman does not match task information in TASKS DB'
```

When look at the `adjust_out.txt` at `vocms059:/data/srv/glidecondor/condor_local/spool/4987/0/cluster9594987.proc0.subproc0/adjust_out.txt`, the logs reported: 

```
2024-05-14 13:06:59.196789: Task status on DB: QUEUED, clusterID on DB: None, schedd name on DB: crab3@vocms059.cern.ch; 
clusterID on condor ads: 9594987, schedd name on condor ads: crab3@vocms059.cern.ch 
2024-05-14 13:06:59.196845: Exiting AdjustSites because this dagman does not match task information in TASKS DB
```

The task log from TW (`crab-dev-tw03:/data/container/TaskWorker/logs/tasks/crabint1/240514_130645:crabint1_crab_rucio_transfers_20240514_150644.log`):

```
2024-05-14 13:06:56,473:DEBUG:DagmanSubmitter:Trying to submit task 240514_130645:crabint1_crab_rucio_transfers_20240514_150644 to schedd crab3@vocms059.cern.ch for the 0 time.
2024-05-14 13:06:56,473:DEBUG:DagmanSubmitter:Getting schedd object
2024-05-14 13:06:56,479:DEBUG:DagmanSubmitter:Got schedd object
2024-05-14 13:06:56,511:INFO:DagmanSubmitter:User crabint1 mapped to local groups {'/cms', '/cms/production'}.
2024-05-14 13:06:56,511:DEBUG:DagmanSubmitter:Finally submitting to the schedd
2024-05-14 13:06:57,266:DEBUG:DagmanSubmitter:Condor cluster ID returned from submit is: 9594987
2024-05-14 13:06:57,267:DEBUG:DagmanSubmitter:Submission finished
2024-05-14 13:06:57,267:DEBUG:DagmanSubmitter:Pushing information centrally {'workflow': '240514_130645:crabint1_crab_rucio_transfers_20240514_150644', 'status': 'SUBMITTED', 'subresource': 'success', 'clusterid': 9594987}
2024-05-14 13:07:00,002:INFO:DagmanSubmitter:Summary of schedd failures/successes for slave process 1 (PID 22):
        crab3@vocms059.cern.ch:
                Number of successes: 1
                Number of failures:  0
Last successful submission: ClusterId 9594987 submitted to schedd crab3@vocms059.cern.ch
```

Looking at timestamp, there are 3 seconds gap between dag submitted and update task status to rest, and AdjustSites.py error's timestamp is between this gap.

It never occurred to me when submitting with Jenkins or manual, but it happened occasionally when running the Gitlab-CI pipeline. It was very frustrating. 

Should we add retry in AdjustSites or simply delay boostrap for 1 min?

## Comment (belforte, 2024-05-16T09:30:38Z)

Puzzling. It should be extremely rare that AdjustSites.py runs within a few seconds from submission. I have seen this in user reports rarely and usually in situation where uploading to REST fails and needs to be retried. A small delay like you suggest would not fix that.

## Comment (belforte, 2024-05-16T14:57:07Z)

Let me review the original motivation for this in #6151 and #6145 

At first sight the only really safe way is (as usual) the one Brian suggested in #6151, but it complicates TW a lot.

OTOH, we have discussed to introduce new task statuses already: WAITING between NEW and HOLDING (which means "grabbed by TW") and COMPLETED/FAILED to signal that DAGMAN stopped #8394 

So maybe adding ACTIVE (or call it RUNNING) is not too bad.

I propose to add a 30sec/1min sleep to avoid the "next condor schedd cycle happens instantly as soon as dag is submitted" and re-evaluate the above proposal as a better alternative to current check in AdjustSites
