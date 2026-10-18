# dmwm/CRABServer issue #8921: remove port 8443 from cmsweb URL's

State: closed
Opened: 2025-02-14T15:11:02Z
Closed: 2025-05-20T11:08:36Z
Labels: Area: Code Cleanup, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8921

## Opening post (belforte, 2025-02-14T15:11:02Z)

Especially in CRABServeer UI, it often makes page download to fail, until one tries again w/o it.
Ref also to https://mattermost.web.cern.ch/cms-o-and-c/pl/ym4jn56n6iyqifo9pnx5tism6h

This mean some changes to https://github.com/dmwm/CRABServer/blob/master/src/html/index.html and/or jquery files used in there

## Comment (belforte, 2025-02-14T15:34:40Z)

hmmm...
maybe that page is w/o fault. and the 8443 is put in by the RES in building the answer to
https://cmsweb.cern.ch/crabserver/prod/task?subresource=webdirprx&workflow=....

oh well. It is so difficult for me to tell what the UI is doing, sorry.

## Comment (belforte, 2025-03-19T13:57:17Z)

it is amazingly intricated !!
The only solution that comes to mind is to re-work all this webdir vs. webdirproxy thing.
Curretly we store in the DB an URL which points to the scheduler's HTTP server, e.g.
```text
https://cmsweb.cern.ch:8443/scheddmon/0197/aguven/250306_132816:aguven_crab_20250306_142547
```
(from `curl "https://cmsweb.cern.ch/crabserver/prod/task?subresource=webdirprx&workflow=250306_132816:aguven_crab_20250306_142547"`)

which gets transformed in to what this returns `curl "https://cmsweb.cern.ch/crabserver/prod/task?subresource=webdir&workflow=250306_132816:aguven_crab_20250306_142547"` via https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/CRABInterface/RESTTask.py#L237
and following lines, so the "8443" ultimately comes from
https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-shedds-config.json?ref_type=heads

while we can start from removing the port # there, getting rid of all this complexity is certainly better

## Comment (nausikt, 2025-05-19T15:08:47Z)

Thanks you, for ultimate clues! @belforte 

You were right, from **getProxiedWebDir** in `src/python/ServerUtilities.py` to **webdirprx** subresource function in `src/python/CRABInterface/RESTTask.py`. 

they all point to `htcondorSchedds` config in [cmsweb-shedds-config.json](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-shedds-config.json?ref_type=heads), where most of the changes are needed.
https://github.com/dmwm/CRABServer/blob/a9c51b514446df1b2138492a29389b32ca3bf274/src/python/CRABInterface/RESTTask.py#L236-L257 



```json
{
  "crab3@vocms059.cern.ch" : {
    "proxiedurl": "https://cmsweb.cern.ch:8443/scheddmon/059",
    "weightfactor": 0
  },
  "crab3@vocms068.cern.ch" : {
    "proxiedurl": "https://cmsweb.cern.ch:8443/scheddmon/068",
    "weightfactor": 1
  },

```

Additionally, the other location i found was hardcoded that i'm not sure whether it's need changed or not is located in `src/python/TaskWorker/Actions/RetryJob.py`
```python
509:        webDirUrl = f"https://cmsweb.cern.ch:8443/scheddmon/{schedId}/{username}/{taskName}"
510:        stdoutUrl = f"{webDirUrl}/job_out.{jobId}.txt"
511:        postJobUrl = f"{webDirUrl}/postjob.{jobId}.txt"
```

Other than that i think the code cleaning/refactoring about webdir vs webdirProxy, could be open as another issue?

## Comment (nausikt, 2025-05-20T08:32:50Z)

I've removed 8443 port from [cmsweb-shedds-config.json](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/commit/3dccf287177de3e1886c258dfbda49ef613d1193) and also in [Actions/RetryJob.py](https://github.com/dmwm/CRABServer/pull/9083) that was hardcoded.

I will waiting for changes to take effects, new WebDir/JobLog Urls, on production.

## Comment (nausikt, 2025-05-20T11:07:26Z)

Now, whenever user hover/click on Webdir link. It was properly point to non-8443 url one. as we could try on [test task](
https://cmsweb.cern.ch/crabserver/ui/task/250519_123330%3Akphornsi_crab_20250519_143325/dbver/prod).

<img width="826" alt="Image" src="https://github.com/user-attachments/assets/163e0f5f-ae5a-463a-a61e-1e21c779c944" />

## Comment (belforte, 2025-05-20T12:52:53Z)

the change in RetryJob is actually unrelated since it only affects my own tallying of corrupted files. But it is fine to do w/o the port there as well. Thanks
