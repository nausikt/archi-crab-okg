# dmwm/CRABServer issue #7932: report to Monit list of root branches read by users

State: closed
Opened: 2023-10-11T16:05:59Z
Closed: 2024-02-03T18:21:39Z
Labels: Type: Enhancement, Priority: High, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/7932

## Opening post (belforte, 2023-10-11T16:05:59Z)

@nsmith- expressed interest in looking at which AOD branches are read by users of AOD in CRAB.
Generally speaking adding this information to CRAB seems a good idea.
So @mapellidario and myself looked at how to implement.

**Current status**

Currently CRAB gets  back from the worker node a shortened version of `FrameworkJobReport.xml` in json format `fjr.json` which is produced by [WMCore's FwkJobReport/Report/parse](https://github.com/dmwm/WMCore/blob/56143c9011322f65159c9d904256a30cdaeed68b/src/python/WMCore/FwkJobReport/Report.py#L136)

There is no branch information in that file.

The original  `FrameworkJobReport.xml` instead has lines like
```
<ReadBranches>
<Branch Name="recoTracks_globalMuons__RECO." ReadCount="600"/>
</ReadBranches>
```

**Proposal**
changing WMCore would take long time and we will be left anyhow with extracting info from `fjr.json` in the PostJob and sending it to Monit somehow.
We rather would like to
1. we modity CRAB JobWrapper so that it
 * parses `fjr.xml` e.g. via python3 built-in parser
 * extract a "string" with the list of branches as comma-separated (blank separated ?) words
 * chirps this to HTCondor as a classAd
   * `CRAB_ReadBranches="B1,B2,B3....,Bn" 
2. @nikodemas should then modify https://github.com/dmwm/cms-htcondor-es/blob/master/src/htcondor_es/convert_to_json.py to catch this Ad for completed jobs and add it to what is sent to MONIT so that it is available in ES and HDFS.
   * IIUC info will stay in ES for 30days and HDFS for 1y. If  we need it for longer some kind of aggregation has to be devised.

@nsmith- Will this do ? Is it OK to ignore ReadCount ? Can you parse that multi-word string ?

## Comment (nikodemas, 2023-10-12T07:32:27Z)

Hi @belforte,

I think we save completed jobs only in OpenSearch (in [es-cms.cern.ch](https://es-cms.cern.ch/dashboards/app/discover?security_tenant=global#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(_source),filters:!(),index:'0f3117a0-d2e6-11ed-bdae-e3cf8c07f2fc',interval:auto,query:(language:lucene,query:''),sort:!()))) and to include a new field in there no change of code is needed. We also save all jobs in [monit-opensearch.cern.ch](https://monit-opensearch.cern.ch/dashboards/app/discover?security_tenant=global#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(_source),filters:!(),index:dd1ba850-d169-11ea-966a-e1c0a7950cea,interval:auto,query:(language:lucene,query:''),sort:!())) for 40 days and HDFS for 3 years (might be reduced to 18 months in the near future) and for this we would need to modify the script you referenced (https://github.com/dmwm/cms-htcondor-es/blob/master/src/htcondor_es/convert_to_json.py#L441-L540).

## Comment (belforte, 2023-10-12T07:41:51Z)

thanks @nikodemas . I find it a bit odd that we keep completed jobs info only for 30 days and running (not complete yet) info for 3 years. That means job info dump every 15min.. should not be  a big effort to keep one extra entry per job when job terminates ! Anyhow we need to hear from @nsmith- about the proposed format before we finalize implementation. I am not familiar with HDFS searches.

## Comment (nikodemas, 2023-10-12T07:51:54Z)

Oh I forgot to mention that completed jobs are kept for 18 months in [es-cms.cern.ch](https://es-cms.cern.ch/dashboards/app/discover?security_tenant=global#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(_source),filters:!(),index:'0f3117a0-d2e6-11ed-bdae-e3cf8c07f2fc',interval:auto,query:(language:lucene,query:''),sort:!())).

## Comment (belforte, 2023-10-12T08:05:06Z)

nice, thanks. I still fail to see the rational for an incomplete picture in HDFS, but hopefully it was a conscious decision with strong arguments behind. I am also curious if there's anything which looks at classAd history overy time for a a job which ran 1 year ago !

## Comment (nsmith-, 2023-10-12T22:13:56Z)

String parsing by splitting according to a special character in PySpark [is possible](https://spark.apache.org/docs/3.1.2/api/python/reference/api/pyspark.sql.functions.split.html). I would find a list of strings a bit easier to use, though I suppose that requires more work to implement. Comma should be a safe character, but ROOT does seem to allow branch names with a comma. I do not know if CMSSW does. I'm asking Matti now.

As for read count, in principle even if one entry is accessed we would expect to need the whole branch available, so I think it is safe to ignore ReadCount, other than whether or not it is greater than 0 of course.

## Comment (belforte, 2023-10-13T08:13:19Z)

List of strings should be fine.
Looking e.g. at https://es-cms.cern.ch/dashboards/app/discover?security_tenant=global#/doc/0f3117a0-d2e6-11ed-bdae-e3cf8c07f2fc/cms-2023-10-13?id=crab3@vocms0144.cern.ch%2398651751.0%231697182894%231697183344
we have this field in the JSON. If this format is ok we can surely format the list of branches in the same way.

 "CRAB_SiteWhitelist": "['T2_CH_CERN_P5', 'T2_UK_London_Brunel', 'T2_US_Florida', 'T2_ES_IFCA', 'T2_US_Nebraska', 'T2_US_Vanderbilt', 'T2_US_Wisconsin', 'T2_US_Purdue', 'T2_CH_CSCS', 'T2_ES_CIEMAT', 'T2_IT_Pisa', 'T2_CH_CERN_HLT', 'T2_CH_CERN', 'T2_DE_DESY', 'T2_IT_Legnaro', 'T2_US_Caltech', 'T2_US_UCSD', 'T2_UK_London_IC', 'T2_UK_SGrid_RALPP', 'T2_IT_Bari', 'T2_IT_Rome', 'T2_UK_SGrid_Bristol', 'T2_DE_RWTH']"

I hope it is same format in pyspark (i.e. spark sees the full JSON doc).

So we skip branches with ReadCount=0, if any, correct ?
I guess we should run a test and if it all looks ok, push to production.
Nick, I think we can report for all tasks, you can always use CMSPrimaryDataTier to fillter AODs

## Comment (nsmith-, 2023-10-17T22:34:08Z)

Yes, I can easily read lists of strings in spark, just confirmed!

## Comment (belforte, 2023-10-18T07:12:06Z)

thanks, onward we go.

## Comment (belforte, 2023-11-09T20:54:35Z)

time to takle this. @nsmith- do you have by any chance a PSet (and AOD dataset) at hand that I can use to produce a FJR.XML with the desired info and use it as test setup for dev and test ? The PSets which we use for CRAB validation all drop everything to be quick and simple.

## Comment (belforte, 2023-11-10T16:50:45Z)

I am testing using DemoAnalyzer. It claims it reads all branches. Hopefully users' code will not be so dumb.
So far so good, having some issues with `condor_chirp`, contacting expert(s).

## Comment (belforte, 2023-11-12T13:54:14Z)

@nikodemas @nsmith- 
longish story short. I have tested the plan as in the top comment,
but it [turns out](https://lists.cs.wisc.edu/archive/htcondor-users/2023-November/msg00053.shtml) that `condor_chirp` only accepts 1024 chars attributes.

Pretty useless given the huge list of branches.
I can easily bring a file with the list back to the scheduler, or add to existing `fjr.json` which will eventually be sent to WMArchive. WMArchive info is eventually on HDFS, I think (@nikodemas )
1. I do not know if WMArchive needs a given format, ignores extra fields
2. Any other way be which I can make those `fjr.json` available ?
3. @nsmith- the list of branches in my simple test has 517 branches and is 30K long (!). Do you want that ? Or could it be somehow shorteneed e.g. listing only the first string before `_` in the list (135 elements, 3K) or the first 2 (to disambiguate things like `double` or `fload`) (359 entries, 18K)

Nick, how should we look at this ? It is just a "once" things to get a sense of things so we go for a quick hack ? Or should it become something which we do for good, so become part of the stable infrastructure and needs a "proejct" ? Maybe a small one, but still somehitng were multiple groups are involved, agreements has to be obtained, implemented with all proper documentation etc. Not a big deal.. but not a one afternoon thing either. Who will look at that information ? Do we need to worry avoid visualization as well ? WMArchive so far is mainly used by P&R to follow workflows progress, and I do not know how they access it.

## Comment (nsmith-, 2023-11-12T22:45:33Z)

Honestly, I think the extent to which it has long-term value depends on what we see the first time we look. If it turns out everyone reads every branch, then there is not much point. But if the hit rate (number of branches accessed vs. total number in file) is low universally, and different datasets have different hit rates, then we have something actionable and worth keeping long-term stats for.
In terms of splitting by `_`, generally all 4 fields are important, so I'm reluctant to try some data reduction scheme.
Perhaps it's worth a short meeting to discuss options?

## Comment (nikodemas, 2023-11-13T09:35:43Z)

> WMArchive info is eventually on HDFS, I think

Yes, it is under `/project/monitoring/archive/wmarchive/raw/metric/`

## Comment (belforte, 2023-11-13T10:11:08Z)

Thanks @nikodemas .If I wanted to test, since I am not good with HDFS, is there an OpenSearch index which I can use ?
@nsmith- let's explore the WMArchive path then. I am not sure if a meeting would help, whom should be present  ? I suspect that the easiest is to try, and in case, ask Valentin, who will say that he's no allowed to work on it anymore, but may still answer.

## Comment (nikodemas, 2023-11-13T10:14:23Z)

Yes, it is on [monit-opensearch.cern.ch ](https://monit-opensearch.cern.ch/) under the name `monit_prod_wmarchive_*`.

## Comment (belforte, 2023-11-13T17:01:16Z)

nope.
the WMA document looks extremely "terse" when compard to FJR https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/60770470-8326-11ea-88fc-cfaa9841e350/monit_prod_wmarchive_raw_metric-2023-11-13?id=1c80c2dc54e545d7bec3fbf649deaf7e

and when I select WMA from a CRAB task I do not even have ways to select on input data or username (which would be needed for testing) https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/60770470-8326-11ea-88fc-cfaa9841e350/monit_prod_wmarchive_raw_metric-2023-11-13?id=19f12f4bfb794264a63ff05ac306aa5d

Looks like only a very small subset of the info is stored in WMArchive. I guess we should check with WMCore people,  I really do not know anything about this, and am a bit surprised that this info can be used for practical purposes.

I have added the ReadBranches list to the WMAFrameworkReport.json which is uploaded and got no error. But since I can't find my one entry in the ziliions of entries....But I very much doubt that the info was stored :-(

We could setup some independent CRAB-to-HDFS channel, but that's quite some work. Maybe piggy back on what was done last summer by Dario, Wa and Ek-ong ? I do not know details @nikodemas what do you think ?

Ideally this information should be available together with other job related info in `monit_condor_prod_raw_metric_*` index, where we tried to put it initially by disguising it an HTCondor classAd. So one can correlated with input data, used time, number of jobs etc.
But atm the only viable solution seems to me that we put it somewhere (EOS ?) where the spider can fetch it and push it to the MONIT pipeline, which looks very ugly to say the least.

I am our of ideas, maybe a use case to bump up to CERN MONIT team ? Can they aggregate data streams ?

## Comment (nikodemas, 2023-11-14T13:09:32Z)

During the summer's work CMS Monitoring only helped CRAB to get the full Oracle table dumps into the HDFS, so I am not sure if that helps here. The data injection to OpenSearch was done by your team.

I can discuss this with @leggerf and @brij01 (also adding them to the discussion in case they have some immediate suggestions) and maybe ask MONIT for their advice if that is needed.

## Comment (belforte, 2023-11-14T13:55:13Z)

thanks @nikodemas, yes the Summar work was about getting info from an Oracle table into MONIT, so I agree it does not apply. The problem here is that "a largish list from every job" is a lot of data in the end, and even to get a sense of things as @nsmith- indicated, we need something like a month of data to figure out patterns. This is a never-looked-at-before topic AFAIK so we have no previous wisdom to guide us.
How to get that non-trivial amount of data in HDFS is something I really do not know how to do, simple as that !

Thanks for followin up

## Comment (nsmith-, 2023-11-14T16:57:52Z)

One thing worth mentioning is that, although the list of branch names is long (up to 500 for AOD) and each name is long (ending up with 30kB figure as @belforte mentioned above), the number of unique branch names across all jobs is very small, not much more than the number per job. So it will compress extremely well, FWIW.
As a hacky solution to start understanding the problem, if we can find a way to send this list from the CRAB production server to a message queue, I can deal with reading messages and storing the results somewhere. Of course, if we can get it into HDFS without much pain, all the better.

## Comment (leggerf, 2023-11-14T17:26:50Z)

sorry this is a long thread so I might be missing details. A few comments:
- we can for sure setup another flow to write this data to HDFS which can be used later in spark jobs to aggregate with condor data, but why can't this info be condensed in a Condor ClassAd? There is no way to do it? This would be the best solution
- we cannot "enrich" the data in the spider, because the spider needs to run in 12 minutes and we cannot add the overhead of reading from EOS
- OTOH MONIT does run some "enrichment" jobs for other data flows, for example FTS data. We can ask what their requirements are for that

## Comment (belforte, 2023-11-14T17:38:22Z)

Thanks @leggerf ,  I think you got it !
* the list of ReadBranches is too long to fit in a ClassAd
* I understand the difficulty of adding another data source to the spider !
* if we can aggregate on HDFS side, useful keys would be "taskName" and "jobId" (yeah I will look up exact name and format in `condor_raw_data` and replicate). I would limit this to successful jobs so we do not worry about retry count
* answering to @nsmith- I believe that sending of data to HDFS is usually done via AMQ, so if I send data there, we can hopefully get it into HDFS, I just miss credentials, code... etc.  But it is stuff that exists and I expect can be copy/pasted.

Just hope I am not got myself into too big a job here. But understanding what users do really is useful !

## Comment (belforte, 2023-11-17T10:04:20Z)

as we talked about this in CRAB devop meeting, @mapellidario suggested that if the list of branches is known and somehow fixed, we can simply report a T/F bit mask as a 30-something hex string. It surely is very fragile in the long term, but maybe we can get a list of branch names for the initial evaluation of "what's going on" ?
I got one list from a `/SingleElectron/Run2017B-09Aug2019_UL2017-v1/AOD` I have no idea how general it is.
I do not see any good alternative to having that list hardcoded in the job wrapper and replicated on @nsmith-  's pyspark side.

maybe @Panos512 ,  who the other day setup a rucio-to-ES pipeline in a few minutes, can also help with ideas ?

Anyhow, @leggerf you are going to follow up with CERN MONIT, right ? If we can have a proper solution via HDFS and avoid the above, things will be much more clear.

## Comment (nikodemas, 2023-12-06T16:35:34Z)

Hi, just to have the progress documented - there is a SNOW ticket `RQF2479427` for CERN MONIT regarding this.

## Comment (belforte, 2023-12-06T16:48:47Z)

thanks @nikodemas , please note that the SNOW ticket is now in status "waiting for user", they asked you to fill-in some info. Since you were at the meeting (and we were not) I would not know how to jump in and do it for you.

@nsmith- what do you think about getting a list of branches so that  we can fill a bit-mask with Y/N ? Is that list "existing" ? Or do we have to read one file from every possible dataset to find out ? For a first test we do not need a complete list, but something like "in half of the jobs half of the read branches are in the list", then we report "number of read branches not in our list". Those 2 things can be put in existing reporting via condor classAds and we go on from there. But needs to be some sensible approx. of reality.

## Comment (nikodemas, 2023-12-11T10:32:31Z)

sorry for the late reply @belforte, but I talked to @mapellidario in person and he said that he will answer the question in the ticket since you guys know better what kind of files would be placed in EOS (and that is the only direct question to be answered there).

## Comment (belforte, 2023-12-13T11:20:38Z)

We discussed a bit and agree that involving CERN MONIT to a non trivial level is not useful. We have other priorities for them and we do not know fir sure yet if this info is going to be useful.

OK. Let's start with reporting the number of branches which each user job reads. If we see large variations, we know we will be interested in the list. If it is a narrow peak... wrap up.

If not, we'll look again at the bitmask approach.

## Comment (belforte, 2023-12-19T11:32:47Z)

I decided to start simple and only count the number of read branches. Once we see how much variation (if any) there is, we will know if it is important to look in more detail

## Comment (nsmith-, 2023-12-19T15:57:59Z)

Is there a way we could send the actual branches to some data reduction process implemented somewhere in MONIT? We generally would only care about the branches read per task at the finest granularity, certainly not per job. As I mentioned, the number of unique branch names is very limited, we might be able to scan a few (Mini-)AOD datasets and enumerate most all of them. But the plan you outline so far seems to be a good direction for now.

## Comment (belforte, 2023-12-19T16:19:39Z)

thanks @nsmith- for your feedback. It is good to see that I am not alone here.
Are branch names same in MiniAOD and AOD  ? Or are those two different sets ?
The MONIT path requires use to install STOMP on the schedulers and so add more code and dependencies.  But your point about reporting per-task is a very good one. We can certainly do that and dramatically reduce the amount of data. But again some changes are neede
. Reporting number of branches is very easy. I am also entertaining the idea of comparing with a list fetched via http, report a couple new one and increment that list ~daily. Anyhow will not be able to get to this before the holidays

## Comment (nsmith-, 2023-12-19T17:48:59Z)

The list of branch names is not the same for MiniAOD and AOD.

## Comment (belforte, 2023-12-21T22:58:17Z)

small progress I managed to add code to JobWrapper in my test TW so that
https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/dd1ba850-d169-11ea-966a-e1c0a7950cea/monit_prod_condor_raw_metric-2023-12-21?id=crab3%40vocms059.cern.ch%239476560.0%231703197153%231703197340
now reports
```
data.Chirp_CRAB3_BranchNumber  103
```
more tests and cleanup (extra quotes e.g.) after the Holiday before pushing to production and see what we get on user jobs. also
- [x] only do when exit code is 0 and it is jobId=1 (i.e. once per task)

## Comment (belforte, 2024-01-22T14:02:26Z)

The new wrapper 
* adds the list of read branches to `job_fjr.1.0.json` which is returned to the scheduler as `fjr['steps','cmsRun','ReadBranches']`
* reports the number of read branches as classAd `Chirp_CRAB3_BranchNumber`
* compares the list or read branches with a reference kept in https://belforte.web.cern.ch/belforte/Branches
* reports at most 5 new branches a classAd `Chirp_CRAB3_5NewBranches` so that reference can be updated

Example dashboard: https://monit-opensearch.cern.ch/dashboards/goto/e185ddd4baeee62eac482768eb221744?security_tenant=global

## Comment (belforte, 2024-01-24T15:56:44Z)

the reporting is now in production and initial values from real users are there
https://monit-opensearch.cern.ch/dashboards/goto/5d8e9e30ab0309935f321c322f60b348?security_tenant=global
![image](https://github.com/dmwm/CRABServer/assets/1837785/1944dff1-c02b-4d24-acb6-a49b35a54370)

I have not found a satisfactory way to visualize them in OpenSearch though.

## Comment (nsmith-, 2024-01-24T16:39:58Z)

Maybe something like this for now: https://monit-opensearch.cern.ch/dashboards/goto/65a8be38dc1329426cb435050f5ab0a2?security_tenant=global
<img width="1289" alt="Screenshot 2024-01-24 at 10 40 31 AM" src="https://github.com/dmwm/CRABServer/assets/6587412/ca8228b1-2876-4a29-a845-0cc1ecc3ec08">


This is already interesting data!

## Comment (belforte, 2024-01-24T18:55:24Z)

thanks @nsmith- I had tried that with split by row and looks horrendous, likely because ordering by Term a number gives funny order, split by columns did the trick !
The100+ are from my tests where I read all branches.
 
Indeed preliminary indication is that we do nee to report those short branch lists. @mapellidario and myself talked about it and it is possible that we  can send the full list directly to ES w/o the overhead of installing Stomp client on HTCondor schedulers.

## Comment (belforte, 2024-01-25T12:18:29Z)

new (better?) dashboard in OS, somehow storing these URLs seems the only way to "save" them https://monit-opensearch.cern.ch/dashboards/goto/ad1717c1f8ef2f8bb2b6e0dc10f7989f

and this for the "discovery" view https://monit-opensearch.cern.ch/dashboards/goto/688903b94b0e1a9fa2966ebe0dac91ec

## Comment (belforte, 2024-01-29T10:42:58Z)

At this point we have good evidence that most user tasks access only a small number of branches.
So we need to report the list.
![image](https://github.com/dmwm/CRABServer/assets/1837785/a7312a51-3259-4e2e-9b21-e8bfe4bcaadc)

## Comment (belforte, 2024-01-29T11:00:24Z)

@mapellidario can you test writing to ES via same method (`requests.post`) as in GenerateMONIT ? As an example input you can create a JSON list of the length that you prefer from the lists of branches which I collected so fare in `/afs/cern.ch/user/b/belforte/BOX/www/Branches/*txt`
I have verified that it is possible to `import requests` into the Postjob. So we can easily test sending the info from some example tasks from the list in https://monit-opensearch.cern.ch/dashboards/goto/a392fe20c03f18e367d645ea3f2b284f

## Comment (nsmith-, 2024-01-29T14:11:25Z)

I found a way to histogram the results: https://monit-opensearch.cern.ch/dashboards/goto/a2a375f3ee1b556e579ca115a57c818c?security_tenant=global
<img width="1250" alt="Screenshot 2024-01-29 at 8 10 32 AM" src="https://github.com/dmwm/CRABServer/assets/6587412/6668ae34-7200-4e9d-9c82-57eec36ed8c8">

## Comment (belforte, 2024-01-29T14:20:18Z)

we are working on providing the list. Can you access data in here ?  https://monit-opensearch.cern.ch/dashboards/goto/a8e5474ea4daa93df5908bb595316639
I want to finish something else first. Then will add also things like datatier, inputdataset, crab task name, username... Then of course we need to make sure there's no bug !

## Comment (belforte, 2024-01-29T21:44:31Z)

how to send data to OpenSeach, from @mapellidario 

```python
"""

run: 

> export CRABTEST_OPENSEARCH_SECRET='XXXXX'
> python3 send-branches.py

result:

- single document: https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/3829fac0-bc68-11ee-b776-cb346cc4cf26/monit_prod_crab-test_raw_branches-2024-01?id=db01c4ab-f1c3-79b6-74e4-b98232bf0aa1
- multiple documents: https://monit-opensearch.cern.ch/dashboards/goto/a8e5474ea4daa93df5908bb595316639
"""

import requests
from requests.auth import HTTPBasicAuth
import os
import json

USER = "crab-test"
PWD = os.getenv("CRABTEST_OPENSEARCH_SECRET", "empty pwd")

def send_opensearch(document):
    r = requests.post(f'https://monit-metrics.cern.ch:10014/{USER}', 
                        auth=HTTPBasicAuth(USER, PWD),
                         data=json.dumps(document),
                         headers={"Content-Type": "application/json; charset=UTF-8"},
                         verify=False
                         )
    print(r.status_code, r.text)

def create_document(branches):
    doc = { "producer": USER,
            "type": "branches",
            "branches": branches,  # a list of strings
            }
    return doc


def main():
    doc = create_document(read_branches())
    send_opensearch(doc)

if __name__ == "__main__":
    main()
 
```

## Comment (belforte, 2024-02-01T22:35:43Z)

Branch list is now reported by CRAB e.g. in https://monit-opensearch.cern.ch/dashboards/goto/e45ff690b4c1517c7ef38ff00e75f61d

So far only my test TaskWorker has the new code and only our test scheduler vocms059 has the secrets needed to post to monit.

I am running validation to make sure nothing is broken, then will deploy in production. @mapellidario and @novicecpp are lookiing at distributing secrets via puppet to all HTCondor schedulers.

## Comment (belforte, 2024-02-01T22:37:55Z)

on hold since no more development looks needed, but let's wait before closing, maybe @nsmith- wants other info, maybe secretes should be placed in different file(s), maybe we want to move from the `crab-test` index in monit to `crab`

## Comment (nsmith-, 2024-02-01T22:49:38Z)

I looked at the branch list info and it seems to cover whatever I could need. As I understand, this all ends up in hdfs, so I can always do a join in spark on the `taskname` if I need more information.

## Comment (belforte, 2024-02-23T11:26:37Z)

@nsmith- the reporting is running in production since 2 days and data are now in the "long term" OpenSearch, retention time 1 year. https://monit-opensearch-lt.cern.ch/dashboards/goto/b0bfab9883d93a0e40395dc72a715356

As to access via hdfs, if you need help to find the data... I do not know. Maybe @mapellidario or @novicecpp know, otherwise @nikodemas or of course MONIT people via SNOW.

## Comment (belforte, 2024-03-19T15:07:26Z)

here's OpenSearch plots of number of read branches distribution for (MINI)AOD with Nick's cute format https://monit-opensearch-lt.cern.ch/dashboards/goto/c63f4b18b2ce572a522ab9c38db6985b

the link in previous comment is still good and provides a look into the list of branch names.

@nsmith- are you stll planning to find some way to dig into the actual branch names and possibly obtain some evidence for changing some of the things which we do ? Or guide us to a better future ?

## Comment (nsmith-, 2024-03-19T15:14:53Z)

Very much so, I was waiting for some decent amount of data to be collected before diving in.

## Comment (belforte, 2024-03-19T15:19:05Z)

we have almost 30 days now. Of course what people are doing now may very well be quite different from what (different people) will be doing next fall !
