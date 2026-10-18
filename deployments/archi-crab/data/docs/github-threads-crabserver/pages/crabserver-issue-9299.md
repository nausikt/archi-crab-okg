# dmwm/CRABServer issue #9299: O(140k) files stuck in `Acquire` state, which led to an unprecedented terminally failed migration baseline.

State: closed
Opened: 2026-04-17T22:47:33Z
Closed: 2026-04-22T18:09:25Z
Labels: Priority: Critical, Publisher
URL: https://github.com/dmwm/CRABServer/issues/9299

## Opening post (nausikt, 2026-04-17T22:47:33Z)

[Chaos of 100k files stuck](https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&from=1775512800000&to=1776981599000&viewPanel=96) [1] started to developed a little bit before [15-04-2026 incident, when CRAB REST workflowdb/GET and filetransfers/GET](https://monit-grafana.cern.ch/d/VML5DJEnk/crab-crabserver-timber?orgId=11&from=1775512800000&to=1776981599000) [2] suddenly became extremely slow out of nowhere and we never seen this peak of O(100k) baseline this long before especially after when WM have been freeze.

As the time of writing, almost **~328** *tasks/users* were affected/stuck at this `acquire` status while publishing to DBS. 
almost no ones with handful amount of blocks succeed to fully published and we founded that all stuck blocks/datasets falls into the same vicious cycles of checking/status/retry/refused as we can see in [3,4] with error `DBS3 exception: Expecting value: line 1 column 1 (char 0)` for 4 days now.

[1] [CRAB Publication Acquired Files](https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&from=1775512800000&to=1776981599000&viewPanel=96)
<img width="1468" height="721" alt="Image" src="https://github.com/user-attachments/assets/916812e9-aa59-4027-aa55-8b0741d59f56" />

[2] [CRAB crabserver timber](https://monit-grafana.cern.ch/d/VML5DJEnk/crab-crabserver-timber?orgId=11&from=1775512800000&to=1776981599000)
<img width="1479" height="780" alt="Image" src="https://github.com/user-attachments/assets/4f3e78e3-81b9-4cb7-b693-381ede6e9d3c" />

[3] `DBS3 exception: Expecting value: line 1 column 1 (char 0)`
```bash
DBS3 exception: Expecting value: line 1 column 1 (char 0)
2026-04-17 19:40:01,535:ERROR: Migration failed for /InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/MINIAODSIM#c0fd94ca-3144-43c5-91af-73abf3d61234
2026-04-17 19:40:01,538:ERROR: Migration status query for block /InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/MINIAODSIM#fadae1d5-22ce-41f6-b030-3ea2ae03713e failed
```
[4] `Migration request refused ... is already exist in DB` (but the existing things not completed yet)
```bash
2026-04-17 21:27:26,192:ERROR: Migration request refused by server.
2026-04-17 21:27:26,192:ERROR: Migration refusal reason: migration request /InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/MINIAODSIM#577a42ba-7ba6-4ba3-a0cc-595335691058 is already exist in DB with id=6496792
```
[5] Acquired Files by users, note that the real big offender is another user who submitted publications from 54 tasks (~1.4k files each), `260414_185149:garciaja_crab_centralSkim**` end-up with ~75k stuck files baseline.
<img width="1480" height="718" alt="Image" src="https://github.com/user-attachments/assets/c169dd48-5cf8-4b45-afc6-9449702cb6c7" />

## Comment (nausikt, 2026-04-18T08:31:13Z)

Today, we've reached all-time-high O(112k). The last time was in 2025 and It was just few spike lasting about hours time-spans with no developed baseline or terminally failed chaos. [1]

[1] [2 consecutive spike in 2025-03-04](https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&from=1743116108244&to=1744232643276&viewPanel=96)  
<img width="1478" height="732" alt="Image" src="https://github.com/user-attachments/assets/b63a1753-0355-4579-a1c7-121929cf6224" />

[2] Now, in 2026-04-18
<img width="1477" height="726" alt="Image" src="https://github.com/user-attachments/assets/962c2624-c879-4fb1-a5c9-741cf99b6b75" />

## Comment (nausikt, 2026-04-18T12:56:23Z)

Publisher_schedd can no longer be stop gracefully..... [1] i will stop the container abruptly, rm and restart with `v3.260418-stable`.
```
[crab3@crab-prod-tw01 ~]$ docker exec -it Publisher_schedd ./stop.sh
Waiting for MasterPublisher to complete cycle: .
...1m......2m.
.3m......4m
......5m
......6m
......7m......8m...
```

## Comment (nausikt, 2026-04-18T13:05:24Z)

We've restarted Publisher_schedd with hotfix tag `v3.260418-stable`. The publisher multi-processes have started publishing each task’s tiny blocks well. [1]

Right now we hit **O(140k)** [2], I'll monitor whether the baseline drop as we expected, then gradually restart/rescue some terminally failed migrations via resubmitted requests for new migrations.

P.S. It’s starting to plateau / decline. But unluckily, I've some fever now🤒, let me back to the rescue missions ASAP.

[1]
```bash
2026-04-18 14:58:39,882:DEBUG:PublisherMaster,477:Unitarity check: active_:1170 toPublish:1170 toFail:0
2026-04-18 14:58:39,896:INFO:PublisherMaster,510:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260414_190159:garciaja_crab_centralSkim__ScenarioB2_Par_2024_mpi-1_mA-0p60_ctau-100mmvhahm_8p0
2026-04-18 15:15:05,673:DEBUG:PublisherUtils,270:FMDATA: will retrieve data for 6 files
2026-04-18 15:15:05,708:DEBUG:PublisherUtils,283:FMDATA: retrieved data for 6 files
2026-04-18 15:15:05,708:DEBUG:PublisherUtils,284:FMDATA: retrieved: 0 MB in 0 sec for 260417_203309:fdamas_crab_RECOPATwith161pre3_151X_mcRun3_2025_realistic_HI_v5
2026-04-18 15:15:05,708:INFO:PublisherUtils,299:Got filemetadata for 6 LFNs
2026-04-18 15:15:05,709:DEBUG:PublisherMaster,477:Unitarity check: active_:6 toPublish:6 toFail:0
2026-04-18 15:15:05,720:INFO:PublisherMaster,510:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260417_203309:fdamas_crab_RECOPATwith161pre3_151X_mcRun3_2025_realistic_HI_v5
2026-04-18 15:15:09,292:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/srv/Publisher/logs/tasks/fdamas/260417_203309:fdamas_crab_RECOPATwith161pre3_151X_mcRun3_2025_realistic_HI_v5-7.json\n'
2026-04-18 15:15:09,293:INFO:PublisherMaster,532:Taskname 260417_203309:fdamas_crab_RECOPATwith161pre3_151X_mcRun3_2025_realistic_HI_v5 is OK. Published 6 files in 1 blocks.
2026-04-18 15:15:15,554:INFO:PublisherMaster,279:Terminated: <Process name='Process-26' pid=2705 parent=27 stopped exitcode=0> pid=2705
2026-04-18 15:15:15,568:INFO:PublisherMaster,270:Starting process <Process name='Process-27' pid=2723 parent=27 started>  pid=2723
2026-04-18 15:15:15,568:INFO:PublisherMaster,307:Process 260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2 is starting. PID 2723
2026-04-18 15:15:15,568:INFO:PublisherMaster,271:PID 2723 will work on task 260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2
2026-04-18 15:15:15,569:DEBUG:PublisherMaster,313:==== inside SLAVE for 260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2 using blacklist []
2026-04-18 15:15:15,569:INFO:PublisherMaster,322:At least one dataset has less than 100 ready files. Retrieve task status
2026-04-18 15:15:15,635:INFO:PublisherMaster,329:Task status from DAG info: COMPLETED
2026-04-18 15:15:15,635:INFO:PublisherMaster,337:Considering task status as terminal. Will force publication.
2026-04-18 15:15:15,636:DEBUG:PublisherUtils,270:FMDATA: will retrieve data for 1 files
2026-04-18 15:15:15,666:DEBUG:PublisherUtils,283:FMDATA: retrieved data for 1 files
2026-04-18 15:15:15,666:DEBUG:PublisherUtils,284:FMDATA: retrieved: 0 MB in 0 sec for 260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2
2026-04-18 15:15:15,667:INFO:PublisherUtils,299:Got filemetadata for 1 LFNs
2026-04-18 15:15:15,668:DEBUG:PublisherMaster,477:Unitarity check: active_:1 toPublish:1 toFail:0
2026-04-18 15:15:15,692:INFO:PublisherMaster,510:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2
2026-04-18 15:15:28,589:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/srv/Publisher/logs/tasks/abaty/260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2-4.json\n'
2026-04-18 15:15:28,590:INFO:PublisherMaster,532:Taskname 260417_235634:abaty_crab_TauFilter_IonPhysics41_pT18_v2 is OK. Published 1 files in 1 blocks.
2026-04-18 15:15:35,589:INFO:PublisherMaster,279:Terminated: <Process name='Process-27' pid=2723 parent=27 stopped exitcode=0> pid=2723
2026-04-18 15:15:35,597:INFO:PublisherMaster,270:Starting process <Process name='Process-28' pid=2735 parent=27 started>  pid=2735
2026-04-18 15:15:35,598:INFO:PublisherMaster,271:PID 2735 will work on task 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8
2026-04-18 15:15:35,598:INFO:PublisherMaster,307:Process 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8 is starting. PID 2735
2026-04-18 15:15:35,599:DEBUG:PublisherMaster,313:==== inside SLAVE for 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8 using blacklist []
2026-04-18 15:15:35,599:INFO:PublisherMaster,322:At least one dataset has less than 100 ready files. Retrieve task status
2026-04-18 15:15:35,834:INFO:PublisherMaster,329:Task status from DAG info: SUBMITTED
2026-04-18 15:15:35,834:INFO:PublisherMaster,341:Task status is not considered terminal. Will check last publication time.
2026-04-18 15:15:35,858:DEBUG:PublisherMaster,358:Last publication time: None.
2026-04-18 15:15:35,858:INFO:PublisherMaster,364:There was no previous publication. Will force publication.
2026-04-18 15:15:35,858:DEBUG:PublisherUtils,270:FMDATA: will retrieve data for 6 files
2026-04-18 15:15:35,887:DEBUG:PublisherUtils,283:FMDATA: retrieved data for 6 files
2026-04-18 15:15:35,887:DEBUG:PublisherUtils,284:FMDATA: retrieved: 0 MB in 0 sec for 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8
2026-04-18 15:15:35,887:INFO:PublisherUtils,299:Got filemetadata for 6 LFNs
2026-04-18 15:15:35,887:DEBUG:PublisherMaster,477:Unitarity check: active_:6 toPublish:6 toFail:0
2026-04-18 15:15:35,897:INFO:PublisherMaster,510:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8
2026-04-18 15:15:38,511:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/srv/Publisher/logs/tasks/azaza/260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8-442.json\n'
2026-04-18 15:15:38,512:INFO:PublisherMaster,532:Taskname 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8 is OK. Published 6 files in 1 blocks.
```

[2]
<img width="1477" height="730" alt="Image" src="https://github.com/user-attachments/assets/96a38725-45bb-4eb2-92b2-479869ff635e" />

## Comment (nausikt, 2026-04-18T20:20:26Z)

Good news is for the biggest offender task: 
- 260413_155014:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260413

At least, we no longer see [3] DBS3 exception: `Expecting value: line 1 column 1 (char 0)` which often occurs once ~ 1~2 hrs.

```bash
2026-04-18 06:22:35,084:INFO: Submitting 226 block migration requests to DBS3 ...
DBS3 exception: Expecting value: line 1 column 1 (char 0)
...
2026-04-18 08:09:33,369:INFO: Submitting 226 block migration requests to DBS3 ...
DBS3 exception: Expecting value: line 1 column 1 (char 0)
...
2026-04-18 12:28:28,802:INFO: Submitting 226 block migration requests to DBS3 ...
DBS3 exception: Expecting value: line 1 column 1 (char 0)
....
DBS3 exception: Expecting value: line 1 column 1 (char 0)
2026-04-18 14:14:15,201:INFO: Submitting 226 block migration requests to DBS3 ...
DBS3 exception: Expecting value: line 1 column 1 (char 0)
....
DBS3 exception: Expecting value: line 1 column 1 (char 0)
2026-04-18 17:14:33,201:INFO: Submitting 226 block migration requests to DBS3 ...
2026-04-18 21:48:18,077:INFO: Submitting 226 block migration requests to DBS3 ...
```
Now, we left with just [4] `ERROR: Migration request refused migration request ... is already exist in DB`. 
Hopefully things become more robust, and we can address this through request migration renewal.

## Comment (belforte, 2026-04-18T20:51:27Z)

this is not a real error. It is something which may happen, Publisher cose will use the existing
migration ID to track the progress. Due to concurrent nature of things we can not avoid that
multiple processes ask for migration of same block, consistency is enforced inside Oracle
on DBS side.

` ERROR: Migration request refused migration request ... is already exist in DB.`

## Comment (nausikt, 2026-04-18T21:15:50Z)

The biggest offender is **garciaja** that have almost **316** micro-scenario publishing tasks submitted during `2026-04-14` till `2026-04-16`.

As a results we have over 54 tasks, each contributed to *micro* (1.4k files) terminally failed migration baseline, which in total ***O(75k)*** alone from this user.

<img width="1483" height="726" alt="Image" src="https://github.com/user-attachments/assets/892df641-394d-4bfa-be08-79bfa48d17d6" />

## Comment (nausikt, 2026-04-18T21:32:48Z)

Among `garciaja` tasks that stuck all follows this blocks scenario naming [2] 
BUT i've no ideas why they are not listed in `terminally failed migrations` [1]

P.S. Ohh seems like `TerminallyFailedLog.txt` never been updated since 13:32! this is pretty weird!
[1]
```
-rw-r--r--. 1 crab3 crab3  93M Apr 14 13:32 TerminallyFailedLog.txt
```

[1] `garciaja.blocks.list`
```
[crab3@crab-prod-tw01 migrations]$ cat garciaja.block.list
/GluGluHToDarkShowers-ScenarioB2_Par-ctau-0p1-mA-1p10-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM
/GluGluHToDarkShowers-ScenarioC_Par-ctau-0p1-mA-1p60-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM
/GluGluHToDarkShowers-ScenarioB2_Par-ctau-0p1-mA-2p60-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM
....
```

## Comment (nausikt, 2026-04-18T21:59:33Z)

`TerminallyFailedLog.txt` never been updated since `2026-04-13,14:55:50` worries me a bit, lots of failed blocks infos over these 5 days were lost.

BTW, I’ve renewed all terminally failed migrations, as posible by the logs. 
Before proceeding to blacklisting tasks, i will try to find way to queries migration_id of just problematic tasks.

P.S. only way to trackback from given list of tasks, is to scrape from publishers/logs, but does it worth stressed DBS at this moment by resubmitted almost O(100k) back all at once?
P.S. we may come up with recovery script by task, which could be run when baseline developed not this high.

## Comment (nausikt, 2026-04-18T22:54:57Z)

We went with the blacklisting approach for the top 6 offending users, which should reduced the baseline by at least O(100k) files.

## Comment (nausikt, 2026-04-19T11:13:15Z)

it was sharply drop now. [1] I made a few follow-up bans and keep some baseline for point 1.) testing

For record: 
1. the resubmitted new migrations, even after a day, ended up in state 0-Created and did not progress to processing. 
*Unlike in the past, typically, with-in 10 mins we should see the block progress to state-9, thus can confirm terminally failed state.*
2. there is 5 blocks that have been stuck in in-processing since the incident happened and never ended up in state 9-terminally- failed. DBS may be much slower than expected.
3. indicate possibility that DBS process things much slower than usual which may cause by flooding of publishing jobs recently[?]

<img width="1476" height="725" alt="Image" src="https://github.com/user-attachments/assets/79c064ef-43fe-46ee-9234-0ad86e635457" />

## Comment (belforte, 2026-04-19T11:19:29Z)

is there evidence of successful migrations ? Maybe DBS Publication Server is not working.

## Comment (nausikt, 2026-04-19T11:27:07Z)

It is working at least in tiny/small scale[1] e.g. where published a block with 6 files.

In medium/large scale publications, 
Could it be the spikes or mountains like patterns [2] signify that the DBS mechanic are still trying their best? 

[1]
```bash
2026-04-18 15:15:35,897:INFO:PublisherMaster,510:Now execute: python3 /data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py  --configFile=/data/srv/Publisher/current/PublisherConfig.py --taskname=260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8
2026-04-18 15:15:38,511:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/srv/Publisher/logs/tasks/azaza/260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8-442.json\n'
2026-04-18 15:15:38,512:INFO:PublisherMaster,532:Taskname 260326_174603:azaza_crab_WplusHToXX_M-200_TuneCP5_13TeV-powheg-pythia8 is OK. Published 6 files in 1 blocks.
```
[2]
<img width="1478" height="730" alt="Image" src="https://github.com/user-attachments/assets/8916d637-13b5-4afd-b55f-af6815168d46" />

## Comment (belforte, 2026-04-19T15:51:52Z)

Most publications do not need migrations. MIgrations is only needed when the input was never used in CRAB before.

## Comment (belforte, 2026-04-19T15:53:41Z)

One could grep Publisher logs for the proper message when checking migration status, or look at DBS logs

## Comment (nausikt, 2026-04-20T08:23:49Z)

From Publisher logs, so far, i've seen no clear evidences of new failed migrations yet
We saw just left over terminally failed migrations as follows: 
(which mostly have the same dataset/container prefixes as previous batch of terminally failed)
```
/GluGluHToDarkShowers-ScenarioB2_Par-ctau-0p1-mA-0p60-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM#598211ad-0a15-4b9e-94de-097d7289bf07
/JetMET0/Run2026B-PromptReco-v1/AOD#585d60a3-20be-4f08-b4e6-ab204e448f0e
/C1N2_MET-100_HT-200_ctau-20p0_Mc1n2-700_Mlsp-685_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23DRPremix-130X_mcRun3_2023_realistic_v15-v2/AODSIM#9ae39192-24bc-4f37-91b6-8af503130159
### Below: are example of missing failed migrations.
/C1N2_MET-100_HT-200_ctau-200p0_Mc1n2-200_Mlsp-190_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM#2e04f332-d02b-454a-81e5-60de43d70beb 
```
IIUC, No new (failed) migrations comes to us yet?. is this also aligned with no failures have been log in `TerminallyFailedLog.txt`?.

More successful logs: typically new submitted small/medium-size (1k files) tasks published fine. (2026-04-19, 11h06)
```bash
2026-04-20 09:29:12,389:INFO:PublisherMaster,532:Taskname 260419_110611:chnee_crab_Wto3Pi_0J_DIGI-L1-DIGI2RAW-HLT_v3 
is OK. Published 1000 files in 10 blocks. 82 files left for next iteration.
```

I will blacklisted the left over ones.

## Comment (belforte, 2026-04-20T08:35:24Z)

I am not asking about failed migrations. I ask if there is any successful migration ! Not successful publication.

What about migrations stuck in status 0 ? Do we still have them ? AFAIU this can only happen if migration server is not running.

## Comment (nausikt, 2026-04-20T08:40:54Z)

I'm understand the different between all of those (failed/successful/migration/publication)! but how can i give you successful migration one if no new requests was coming!

The status-0 stuck the same as well as status-1, No progress, for new migrations (from resubmitted) happened 1~2 days ago.
```bash
[crab3@crab-prod-tw01 migrations]$ python3 pingDBS.py
2026-04-20 10:37:59 {1: 5, 9: 59, 0: 2, 2: 10}
```

## Comment (belforte, 2026-04-20T08:41:12Z)

careful with blacklisting, there is no striking evidence which tasks are stuck
https://monit-grafana.cern.ch/goto/EwleUshDR?orgId=11

## Comment (nausikt, 2026-04-20T08:48:02Z)

Acknowledged. I will blacklist only the ones that have been terminally failed since April 14.

## Comment (nausikt, 2026-04-20T08:54:23Z)

For clarity, I posted successful publications because, in my PoV, they imply that the migration machinery may be at least partially functioning. (every migration has to publish somethings so at least we can say that publication server is working, separately)

## Comment (nausikt, 2026-04-20T09:02:32Z)

In short: no new migrations succeed, I will reached to DBS team. 
*migration server likely not working as you said, may need some kick/restart*

## Comment (nausikt, 2026-04-20T09:23:06Z)

@belforte Forgive me🙇, for my ignorance, I'm blind they all decoupled micro-services.

all of these issues likely been consequences from the crashed on [Tues, 14 april](https://mattermost.web.cern.ch/cms-o-and-c/pl/rgbriawy87nq7yqksnr1errjie), as Hassan, Aroosha and Todor pointed out.
```
dbs2go-global-migration-5d9d7c56d9-gzwgf   2/2     Running            6 (17d ago)       96d
dbs2go-global-r-77cc95d498-7ss88           1/2     CrashLoopBackOff   214 (3m56s ago)   96d
....
dbs2go-global-w-8d64cf686-62rcd 
```

## Comment (belforte, 2026-04-22T17:33:42Z)

conclusion is that there is no bug on our side. DBS Migration server was continuously crashing due to hitting memory limit. Then there is the usual problem with migrations which keep failing when we retry.

## Comment (belforte, 2026-04-22T17:34:48Z)

#9300 should be reverted, and running Publishers rolled back to previous image.

## Comment (nausikt, 2026-04-22T18:09:25Z)

Thank you for the on-point root cause analysis scattered across many write-ups, meeting minutes and MMs so far. I learned a lot! 🙇

## Comment (belforte, 2026-04-22T20:06:22Z)

Do not feel bad. There's very very few people in CMS who have years of experience with DBS, DBS Migrations, and CRAB i/f with them  :-)
