# dmwm/CRABServer issue #9113: Handling Kill in ASO/Rucio

State: open
Opened: 2025-06-19T14:33:54Z
Labels: Priority: Medium, Status: On Hold, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/9113

## Opening post (belforte, 2025-06-19T14:33:54Z)

In #8429 we addressed
 * it should not break
 * it should leave things in a status where `crab recovery` works

A few questions are still open, which are more soft, and require a decision, before a technical implementation

- do we need to cleanly and thoroughly   separete Killed from Failed (i.e. completed with some failed jobs ?)
- [ ] when a task is killed, all jobs in transfer are marked as failed, even if output can eventually be transferred and even published. Should we find a way to make them appear as `finished` in `crab status` ?
- [ ] should we remove the Rucio rule on the tranfer container when task is killed ?

## Comment (belforte, 2025-06-20T16:44:33Z)

idea from @dciangot : detach the file replicas from the killed jobs from the container(s)
https://rucio.cern.ch/documentation/html/client_api/didclient.html#rucio.client.didclient.DIDClient.detach_dids

## Comment (belforte, 2025-06-20T16:46:20Z)

or maybe we can find a way to run PJ for so that jobs become successfull/killed/transferring ?
e.g. https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-interaction.html#suspending-a-running-dag

![Image](https://github.com/user-attachments/assets/78ed466a-e3f1-4f53-b35f-36a6f3c7bf0b)


that way jobs killed while running, idle, unsubmitted, will be marked as FAILED but transferring ones will stay transferring, crab status will show exit code 0. And it may not be so bad that they get really transferred and published.

If we want to kill pending transfers as well, we need indeed a non-trivial cleanup in ASO/Rucio.

## Comment (belforte, 2025-06-20T19:23:11Z)

and here's from Condor experts about how to halt the Dagman
https://www-auth.cs.wisc.edu/lists/htcondor-users/2025-June/msg00054.shtml

The problem here is how to signal the Dagman, via  "create a file in the DAG working directory called **<DAG file>.halt**" from the TW. If we hold/release the Dagman is effectively killed and restarted. I do not know what will happen when if it finds the HALT file when starting.

## Comment (belforte, 2025-06-25T15:21:09Z)

Maybe better to come back to this after we refactor Dagman handling #6270 so that we do much less work in the startup scripts. 
All in all nothing is "broken", simply crab status output is not accurate. We can always address that by making `cache_status.py`check Rucio side as well instead of only using condor logs
