# dmwm/CRABServer issue #9058: gaps in Publisher work

State: closed
Opened: 2025-04-26T19:04:07Z
Closed: 2025-05-06T08:19:34Z
Labels: Type: Bug, Priority: High, Status: In Progress, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/9058

## Opening post (belforte, 2025-04-26T19:04:07Z)

Publisher was apparently doinb nothing for almost 3 hours

![Image](https://github.com/user-attachments/assets/5bd58c09-ab7c-4308-91d1-652b535cecc5)

log confirms

```text
2025-04-26 14:23:31,804:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/s
rv/Publisher/logs/tasks/afelizia/250426_113550:afelizia_crab_crab_afelizia_2025-04-26_UTC13-35-34-1.json\n'
2025-04-26 14:23:31,805:INFO:PublisherMaster,532:Taskname 250426_113550:afelizia_crab_crab_afelizia_2025-04-
26_UTC13-35-34 is OK. Published 3500 files in 35 blocks. 52 files left for next iteration.
2025-04-26 14:23:38,308:INFO:PublisherMaster,289:Terminated: <Process name='Process-4732' pid=554652 parent=
5117 stopped exitcode=0> pid=554652
2025-04-26 17:08:17,242:INFO:PublisherMaster,515:TaskPublishScript done : b'Completed with result in /data/s
rv/Publisher/logs/tasks/chensh/250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM-3.json\n'
2025-04-26 17:08:17,242:INFO:PublisherMaster,532:Taskname 250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM is
 OK. Published 5100 files in 51 blocks. 90 files left for next iteration.
2025-04-26 17:08:27,183:INFO:PublisherMaster,289:Terminated: <Process name='Process-4683' pid=543570 parent=
5117 stopped exitcode=0> pid=543570
2025-04-26 17:08:27,184:INFO:PublisherMaster,292:Algorithm iteration completed
2025-04-26 17:08:27,184:INFO:PublisherMaster,293:Wait 0 sec for next cycle
2025-04-26 17:08:27,184:INFO:PublisherMaster,297:Next cycle will start at 17:08:27
2025-04-26 17:08:27,272:DEBUG:PublisherMaster,96:Retrieving publications from oracleDB
```

OTOH just one process completed 5pm, `250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM` which published 5K files in 51 blocks. Could it be that this took 3 hours ??

## Comment (belforte, 2025-04-26T19:11:18Z)

hmmm... here's from log for that task
```text
2025-04-26 14:18:18,580:INFO: Found 5190 files not already present in DBS which will be published.
2025-04-26 14:21:51,735:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 1, blockSize=4MB   , time=209, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:25:18,190:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 2, blockSize=4MB   , time=206, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:28:46,601:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 3, blockSize=4MB   , time=208, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:32:10,944:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 4, blockSize=4MB   , time=204, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:35:33,351:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 5, blockSize=4MB   , time=202, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:38:53,178:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 6, blockSize=4MB   , time=199, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:42:10,194:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 7, blockSize=4MB   , time=196, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:45:23,598:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 8, blockSize=4MB   , time=193, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:48:43,559:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter= 9, blockSize=4MB   , time=199, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:52:05,853:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=10, blockSize=4MB   , time=202, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:55:21,276:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=11, blockSize=4MB   , time=195, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 14:58:52,187:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=12, blockSize=4MB   , time=210, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:02:15,520:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=13, blockSize=4MB   , time=203, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:05:45,176:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=14, blockSize=4MB   , time=209, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:09:17,148:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=15, blockSize=4MB   , time=211, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:12:45,444:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=16, blockSize=4MB   , time=208, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:16:11,076:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=17, blockSize=4MB   , time=205, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:19:47,402:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=18, blockSize=4MB   , time=216, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:23:12,329:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=19, blockSize=4MB   , time=204, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:26:36,911:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=20, blockSize=4MB   , time=204, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:30:01,721:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=21, blockSize=4MB   , time=204, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:33:40,013:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=22, blockSize=4MB   , time=218, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:36:54,100:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=23, blockSize=4MB   , time=194, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:40:13,322:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=24, blockSize=4MB   , time=199, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:43:33,479:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=25, blockSize=4MB   , time=200, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:47:03,285:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=26, blockSize=4MB   , time=209, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:50:23,523:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=27, blockSize=4MB   , time=200, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:53:47,580:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=28, blockSize=4MB   , time=203, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 15:57:12,211:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=29, blockSize=4MB   , time=204, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:00:37,930:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=30, blockSize=4MB   , time=205, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:04:13,839:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=31, blockSize=4MB   , time=215, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:07:43,293:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=32, blockSize=4MB   , time=209, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:11:11,106:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=33, blockSize=4MB   , time=207, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:14:45,153:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=34, blockSize=4MB   , time=213, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:18:23,825:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=35, blockSize=4MB   , time=218, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:21:55,108:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=36, blockSize=4MB   , time=211, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:25:25,681:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=37, blockSize=4MB   , time=210, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:28:54,962:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=38, blockSize=4MB   , time=209, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:32:27,708:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=39, blockSize=4MB   , time=212, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:35:44,987:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=40, blockSize=4MB   , time=197, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:38:40,139:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=41, blockSize=4MB   , time=175, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:41:25,419:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=42, blockSize=4MB   , time=165, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:44:15,562:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=43, blockSize=4MB   , time=170, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:47:07,920:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=44, blockSize=4MB   , time=172, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:49:45,955:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=45, blockSize=4MB   , time=157, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:52:27,183:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=46, blockSize=4MB   , time=161, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:55:13,853:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=47, blockSize=4MB   , time=166, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 16:57:59,747:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=48, blockSize=4MB   , time=165, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 17:00:52,641:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=49, blockSize=4MB   , time=172, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 17:03:27,613:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=50, blockSize=4MB   , time=154, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 17:06:17,289:INFO: PUBSTAT: Nfiles=5190, filestructSize=225MB , lumis=5190000, iter=51, blockSize=4MB   , time=169, status=OK, task=250426_100620:chensh_crab_DPStoPsi2SJ_2018_SKIM
2025-04-26 17:06:17,316:INFO: End of publication status: failed 0, published 5100, publish_in_next_iteration 90, results {'existingFiles': 2500, 'files': 5100, 'blocks': 51}
2025-04-26 17:06:17,316:INFO: Marking 5100 file(s) as published.
```

## Comment (belforte, 2025-04-28T10:39:47Z)

So the TaskPublisher process for this task was indeed running for those 3 hours, preventing the Publisher from starting another loop and effectively blocking everything.
Publisher cuts blocks at 100 files, so 51 iterations to publish 5100 files are OK.
What is not OK is that it took 2~3 minutes every time.
Sort of "DBS" was overloaded.

While things could be done to make Publisher work in a more continuous way, there is little to gain if we are stuck in writing to DBS.

Was this a special use case ? 5190000 lumis / 5190 files = 1K lumis per file.
Which of course and as usual makes no sense. This [task](https://cmsweb.cern.ch/crabserver/ui/task/250426_100620%3Achensh_crab_DPStoPsi2SJ_2018_SKIM) was processing a user-generated MC: [/Pythia8_DPStoPsi2SJ_filter3p5/chensh-MC2018_RECO_chensh_v7-a5d501e738bc46974ac8d371aaff19e9/USER](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod/phys03&input=/Pythia8_DPStoPsi2SJ_filter3p5/chensh-MC2018_RECO_chensh_v7-a5d501e738bc46974ac8d371aaff19e9/USER) with 1 file per job.

Also all 5190 jobs completing in a short amount of time is very unusual.

Or 5190 jobs all starting in a short time, job duration from `crab status`:   `0:01:03 min, 0:11:22 max, 0:02:54 ave`  :-(

I still have the feeling that even with 1K lumis, one 100-file block should not take 2~3 minutes to publish, but that's a DBS thing.

All considered, I do not see any simple way to resolve this. 
This task was totally crazy, the input datsaset has ` Number of events: 4797 Number of files: 9945` , files mostly have 0 or 1 events and yet user ran a SKIM step with 1 file per job as input, no wonder running time is 1min).

I will think if we can put some protection against this.
To be compared with the effort of rewriting the main Publisher loop so that it does not wait for all subprocesses to be completed before checking for new work.

## Comment (belforte, 2025-04-28T13:34:48Z)

Job completion for that user

![Image](https://github.com/user-attachments/assets/eff52da9-2a51-4845-b7be-a2d2e8bf53a9)
is indeed packed in a short time interval but not extraordinary as rate goes when compared with all users in same interval

![Image](https://github.com/user-attachments/assets/ca7d4b6e-f019-4e69-ba77-c536bc41d048)

Comparing with e.g. tasks for user `afelizia` I got convinced that the thing which slows DBS is the old number of lumis evil, with 1K lumis in each input file. I can't find the details of the task which created that dataset with 1K lumis and 1 event per file. I suspect that 1K lumis is some kind of "user default for GEN" and number of events is simply due to heavy filtering.

## Comment (belforte, 2025-04-28T14:48:03Z)

The original dataset was a GEN from https://cmsweb.cern.ch/crabserver/ui/task/250422_150118%3Achensh_crab_DPStoPsi2SJ_2018_GEN
with 10^9 events, 10K jobs, 100K events per job, so given our default of `'tm_events_per_lumi = 100``, indeed 1K lumi per job.
Which gave a dataset with 10K files and 1K lumi per file which was then processed through DIGI, HTL and RECO to obtain the input to this final SKIM.

Clearly 1k lumis per file made no sense here, 1 lumi should be good enough.

I do not remember now why we picked 100 events per lumi as the default, maybe at the time we were seeing 1M event tasks for generation, not 1 billion. I guess that setting as input `lumis_per_files` would be too many code changes ? I'd rather not changes the splitting code based on `events_per_lumi` but we could change the client to set it based on lumis per file with a default of 1.

Most user do not use `events_per_lumi` anyhow.
But I see that some still do, even currently and with more or less sensible values like this task [250428_024650:mmadhu_crab_Pythia3MuMassBBCCTest_cfi_RedecayAprilRoundC1Type9](https://cmsweb.cern.ch/crabserver/ui/task/250428_024650%3Ammadhu_crab_Pythia3MuMassBBCCTest_cfi_RedecayAprilRoundC1Type9) with `10K jobs, 50M events (so 5K events per job) and 30K events_per_lumi` which eventually lead to 1 lumi per file

## Comment (belforte, 2025-04-28T15:35:35Z)

one possibility is to change code in the client so that if user does not specify `events_per_lumi` it gets computed from Njobs and Nevents to be 1 lumi per job.
And give to users with special needs the possibility to indicate a different value of `lumis_per_file` with a BIG warning (maybe implement and do not tell until someone comes up with a use case ? or simply keep in mind but not implement).

I.e. keep current client/server interface based on `events_per_lumi` but stop accepting as input to the client.

## Comment (belforte, 2025-04-28T22:31:10Z)

I have a tentative implementation of `lumis_per_files` in https://github.com/belforte/CRABClient/tree/add-lumis-per-file which overrides `events_per_lumi`.
Will be very easy to make this default to `1` when `events_per_lumi` is not indicated.
I will try to poll users before implementing.
This should then be moved to a CRABClient issue.

Reworking Publisher is too much effort IMHO. All in all those pathological tasks are bad anyhow, better to prevent them than to accomodate them.
If there are genuine use cases with 1K lumis per file, those should be from real data and not come in 10K jobs each. All in all 1K lumi per file x 10K files is 10M lumis. x 23.3 sec this is 7 years of integrated running time !!

## Comment (belforte, 2025-04-29T09:18:06Z)

users polled: https://cms-talk.web.cern.ch/t/changes-to-craclient/124290

## Comment (belforte, 2025-04-29T09:23:52Z)

CRABClient issue: https://github.com/dmwm/CRABClient/issues/5385

## Comment (belforte, 2025-05-06T08:19:35Z)

this should not happen any more with new client [v3.250505](https://github.com/dmwm/CRABClient/releases/tag/v3.250505)
