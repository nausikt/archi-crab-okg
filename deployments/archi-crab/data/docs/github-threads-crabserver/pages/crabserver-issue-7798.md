# dmwm/CRABServer issue #7798: Integrating summer students's works into our monitoring pipeline.

State: closed
Opened: 2023-08-04T12:39:39Z
Closed: 2024-10-11T15:33:26Z
URL: https://github.com/dmwm/CRABServer/issues/7798

## Opening post (novicecpp, 2023-08-04T12:39:39Z)

The main goal is integrate Ek-ong and Tan's works to crab as part of monitoring system and keep maintain it forever.

Resources:
- Ek-ong code: https://github.com/ekongat/crab-datapipeline/
- The dashboard: https://monit-grafana.cern.ch/d/w8jWTsC4k/crab-ss-ekong?orgId=11&from=now-30d&to=now
- Docs: TBD
- Ek-ong's final goal: https://codimd.web.cern.ch/n0zKtr4KTZq2gquFpoQJdA?both#
- Ticket dicussion with CMS MONIT: [CMSMONIT-555](https://its.cern.ch/jira/browse/CMSMONIT-555)

The plan:
- [ ] Move pipeline's cronjobs to our environment.
  - Move Ek-ong script to gitlab's crab3.
  - Run CMS MONIT docker container in TW machine.
  - Setup cronjobs entries via Puppet.
- [ ] Validate all panel created by Ek-ong in Grafana before move it in to production dashboard.
- [ ] Create monitoring.
  - to notify pipeline fail and  measure running time.
- [ ] Docs

## Comment (mapellidario, 2023-08-17T16:26:02Z)

We continued our work on this topic, mainly some cleanup.

What we did:

- [x] create a doc page in mkdocs: https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-spark.html
- [x] open a PR to dmwm/CRABServer
- [x] change the workdir in crab-dev-tw04 so that we now use Ek-Ong's branch of dmwm/CRABServer, not his original repo.
- [x] puppet: create a crontab https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/crabdev_taskworker/code/manifests/crabtaskworker/crabspark.pp 

What we still have to do.

- [x] (bug) set proper permissions of `cron_daily.sh` and `run_spark.sh`, the scripts need to be executable
- [x] (ops / tutorial for dario) create the new indexes in opensearch
    - dario created a couple of new indexes with better names, but still need to finish it
- [ ] (doc) add link to source of osearch.py by ceyhun
- [x] (ops) ask cms monit team for the service account cmscrab to have permissions to write to cms hdfs
    - otherwise we can not use cmscrab keytab to process the condor raw metrics
- [x] (ops) add to puppet the cronjob for the daily script
    - dario started working on this, but he still has to finalize it
- [x] (org) move the code from `ekongat/crab-datapipeline` to `dmwm/CRABServer/src/script/Monitor/crab-spark`. Ek-Ong will need to open a PR to dmwm/CRABServer
- [x] (ops) run the cronjob from a crab-prod-tw01 / tw02
- [x] (improve) the cronjob should send notification only if we have a failure!
    - logs are available at `/var/log/crab/crabspark.log`
- [x] use crabspark keytab
    - I see that we do not have new data in some panels, i think this fails to write to hdfs the intermediate data...

Comments are welcome! Feel free to edit this comment as we progress with our work :)

## Comment (mapellidario, 2023-09-22T13:50:58Z)

We identified an issue with the data source that we use for raw condor metrics:

```plaintext
!hdfs dfs -ls /project/monitoring/archive/condor/raw/metric/2023/09/

drwxr-xr-x+  - monitops hdfs          0 2023-09-10 07:45 /project/monitoring/archive/condor/raw/metric/2023/09/01
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:44 /project/monitoring/archive/condor/raw/metric/2023/09/02
drwxr-xr-x+  - monitops hdfs          0 2023-09-11 03:52 /project/monitoring/archive/condor/raw/metric/2023/09/03
drwxr-xr-x+  - monitops hdfs          0 2023-09-12 05:00 /project/monitoring/archive/condor/raw/metric/2023/09/04
drwxr-xr-x+  - monitops hdfs          0 2023-09-13 04:57 /project/monitoring/archive/condor/raw/metric/2023/09/05
drwxr-xr-x+  - monitops hdfs          0 2023-09-15 08:48 /project/monitoring/archive/condor/raw/metric/2023/09/06
drwxr-xr-x+  - monitops hdfs          0 2023-09-15 10:03 /project/monitoring/archive/condor/raw/metric/2023/09/07
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 07:52 /project/monitoring/archive/condor/raw/metric/2023/09/08
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:46 /project/monitoring/archive/condor/raw/metric/2023/09/09
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:42 /project/monitoring/archive/condor/raw/metric/2023/09/10
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:51 /project/monitoring/archive/condor/raw/metric/2023/09/11
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:52 /project/monitoring/archive/condor/raw/metric/2023/09/12
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:44 /project/monitoring/archive/condor/raw/metric/2023/09/13
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:53 /project/monitoring/archive/condor/raw/metric/2023/09/14
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:47 /project/monitoring/archive/condor/raw/metric/2023/09/15
drwxr-xr-x+  - monitops hdfs          0 2023-09-17 08:56 /project/monitoring/archive/condor/raw/metric/2023/09/16
drwxrwxr-x+  - monitops hdfs          0 2023-09-18 00:48 /project/monitoring/archive/condor/raw/metric/2023/09/17.tmp
drwxrwxr-x+  - monitops hdfs          0 2023-09-19 00:01 /project/monitoring/archive/condor/raw/metric/2023/09/18.tmp
drwxrwxr-x+  - monitops hdfs          0 2023-09-20 00:53 /project/monitoring/archive/condor/raw/metric/2023/09/19.tmp
drwxrwxr-x+  - monitops hdfs          0 2023-09-21 00:36 /project/monitoring/archive/condor/raw/metric/2023/09/20.tmp
drwxrwxr-x+  - monitops hdfs          0 2023-09-22 00:00 /project/monitoring/archive/condor/raw/metric/2023/09/21.tmp
drwxrwxr-x+  - monitops hdfs          0 2023-09-22 15:00 /project/monitoring/archive/condor/raw/metric/2023/09/22.tmp
```

We informed Nikodemas from CMS Monit team and we will follow up.

## Comment (mapellidario, 2023-09-22T13:58:40Z)

Moreover, we noticed that the data about rucio taperecall from cmsspark [1] does not match with rucio monitoring [2]

we will investigate

[1]

![image](https://github.com/dmwm/CRABServer/assets/16376695/0dcef1ce-94a3-42ae-9c1a-691b19ff9f2f)


[2]

![image](https://github.com/dmwm/CRABServer/assets/16376695/4560ff42-5b24-4e47-be2d-9696f70d95fd)

## Comment (mapellidario, 2024-01-31T13:22:23Z)

Request from Stefano, on mattermost private channel:

- [ ] "breakdown by datatier of data locked by CRAB for tape recall and data input "

## Comment (novicecpp, 2024-03-11T13:10:45Z)

![image](https://github.com/dmwm/CRABServer/assets/2346664/9d4aeb40-c123-4d24-89d3-9f888151ecbb)

@nikodemas kindly ping me today that our pipeline has been broken for a long time.
I proposed to him to have a chat in the first week of April (including usage of `cms1` instance), after Easter.
Is it ok for you @mapellidario ?

## Comment (belforte, 2024-08-30T11:58:36Z)

moving the "leftovers" to @novicecpp

## Comment (novicecpp, 2024-09-10T16:42:05Z)

Today I have tried to debug spark for the question: [How long does it take to recall dataset?](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=14)
What I found so far:
- Formatting bug https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/src/script/Monitor/crab-spark/cronjobs/crab_tape_recall_rules_history_daily.py#L72
- Need to switch filter from `crab_tape_recall` account to `activity="Analysis TapeRecall"`

Also, what we do right now is we check on the rules that expire "TODAY" to ensure that rules reach the final stage and not change anymore. Then we send data to Opensearch with timestamp "TODAY". 
This is hard to spot if there is really no rules expire TODAY, or query is broken. Backfill also pain because you need to purge index and rerun for all days each day.

Because the table we query already contains all rules from the beginning of time, it would be better to compute it again and again every day, and let Grafana get the info from the latest entries only. But I do not know how to do so.

## Comment (belforte, 2024-09-10T19:25:35Z)

makes me wonder if Spark is the right tool here. We already feed recall information to OpenSearch for the "recall in progress" table, would not be hard to send a record when we detect that a rule turned OK. Rule has creation date.  Querying all rules since the beginning of time seems on overkill.

## Comment (belforte, 2024-09-10T19:26:15Z)

maybe there are other questions which can only be answered by querying Rucio DB dumps ?

## Comment (novicecpp, 2024-09-13T09:53:18Z)

> would not be hard to send a record when we detect that a rule turned OK. Rule has creation date.

Sorry, I need your help. Could you give me a light on how to do this?

What I am imaging is that you save the current result as `previous`, then next time fetch `current` again and compare with `previous` to get the rules that change the state from REPLICATING to OK. 
IMO, it is not an elegant way to do, and could potentially make CheckTapeRecall.py more complicated.

## Comment (novicecpp, 2024-09-13T10:30:59Z)

Allow me to create goals and to-do list for closing this issue:
Goal:
- [x] Fix [How long does it take to recall dataset?](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=14)
- [x] Remove [CRAB Tape Recall : No. of Expired Files](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=4). I do not remember why we need this. Stefano: I do not remember either. "expired files" makes no sense. Maybe it was supposed to mean tape recall request which get canceled after 2 (3?) week by TapeRecallManager w/o having ever completed ?
- [x] ~~Fix [crab taperecall rules quota - group by dest RSE (broken?)](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=33). Better to use CMSMONIT/Data Management data if they already have it.~~ Use [Rucio Activity Account Monitoring](https://monit-grafana.cern.ch/d/a9fac9a3-6fd9-4c16-a5ac-6c81a06305aa/rucio-activity-account-monitoring?orgId=11) from DMOps instead.

To-do:
- [x] Rework on development environment. Right now I feel like I need to do everything from scratch (Now, I am regret that I did not do it while Dario was here).
    - [x] Ask Nikodemas for test user on os-cms.cern.ch, with permission delete/create indexes and schema under index prefix  `crab-test-*`
    - [x] Ask Nikodemas for a new datasource to `crab-test-*` index in grafana.
- [x] Ask Nikodemas to allow crab team to [edit our spark dashboard](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11)
- [x] Ask Nikodemas/Panos(?) if we can use filter `Activity='Analysis TapeRecall'` on [Rucio datasets daily stats \[DBS\]](https://monit-grafana.cern.ch/d/CuGmwA8nz/rucio-datasets-daily-stats-dbs?orgId=11) dashboard.  The datasource for that dashboard is not listed in [datasources.json](https://github.com/dmwm/CMSMonitoring/blob/3fcf6053050f9f14310fe48b728f992333ea3e8e/static/datasources.json)
- [ ] Document each script what are the questions it try to answer. Potentially refactor script fucntion into modules.
- [ ] Document the monitoring that [Dario set it up](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=49).
- [x] (Optional) Run scripts directly from notebook.

## Comment (belforte, 2024-09-13T19:21:57Z)

I need to review TapeRecallManager and CheckTapeRecall to answer. Thanks for the question. I will. I agree that we want simplicity and if what you indicated become necessary, it is not the right way.

## Comment (novicecpp, 2024-10-02T17:51:41Z)

I give up fixing [crab taperecall rules quota - group by dest RSE (broken?)](https://monit-grafana.cern.ch/d/cb38ecf4-c5f8-4948-877c-88c3472eb20b/crab-usage-spark?orgId=11&viewPanel=33) and use [Rucio Activity Account Monitoring](https://monit-grafana.cern.ch/d/a9fac9a3-6fd9-4c16-a5ac-6c81a06305aa/rucio-activity-account-monitoring?orgId=11) as a replacement (thanks to Stefano and Vijay for discover all info for us). 

Here is the info of "Rucio Activity Account Monitoring" dashboard:
-  Spark script [rucio_activity_account_usage.py](https://gitlab.cern.ch/cmsdmops/cmsdmops/-/blob/8da699db49097d7a58440e6058f022c3f93992e2/monitoring/kubernetes/src/rucio_activity_account_usage.py)
- Opensearch 
    - instance: <https://monit-opensearch-lt.cern.ch>
    - index: `monit_prod_cms_dmops_raw_activity_account_usage-*`
- [Example doc](https://monit-opensearch-lt.cern.ch/dashboards/app/discover#/doc/f1bf4f00-24b2-11ef-8b59-1b7923216166/monit_prod_cms_dmops_raw_activity_account_usage-2024-10?id=c4459f3d-76a8-7be2-5112-f71e27fff6e1)
    ![Screenshot from 2024-10-02 19-38-59](https://github.com/user-attachments/assets/d2bdf23b-57bf-45b9-8ff0-6871b3d02c07)

Note that that dashboard is lacking "group by data tier" compare to our dashboard.  
Adding the new field like data tier we can possibly to do it by ourselves, but we need to discuss if it worth or not, for us and for them, and what does it cost.
I have a recipe in here [crab_rucio_rules_poc.ipynb](https://github.com/novicecpp/CRABServer/blob/ff73f96779bdac9ef0e8312743658456f36db259/src/script/Monitor/crab-spark/notebooks/crab_rucio_rules_poc.ipynb), the total docs are increase from 1500 to 6500 for today (2024-10-02) data, which is not bad. I leave the decision to you guys.

## Comment (belforte, 2024-10-02T20:42:20Z)

I am lost. Please meet with Vijay and make sure that he understand. I am not sure how much time I can put on this next week. Maybe the two of you can have a chat with Rahul or whoever else is working on populating that index ?

## Comment (novicecpp, 2024-10-31T16:08:09Z)

All know-how about spark are in https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-spark/introduction.html
