# dmwm/CRABServer issue #9014: TaskWorker stops processing tasks

State: closed
Opened: 2025-03-20T15:41:47Z
Closed: 2025-04-01T13:52:52Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9014

## Opening post (belforte, 2025-03-20T15:41:47Z)

since switching to [v3.250310](https://github.com/dmwm/CRABServer/releases/tag/v3.250310) we had two incidents, one with canary TW, the other with production TW, where the MasterWorker was reporting 0 free slaves, and hence injecting no new tasks, while the slaves were alive and doing nothing. Indeed periodic actions which are injected independently from the queue status kept going through.

Links to cms-talk

[March 15](https://cms-talk.web.cern.ch/t/crab-task-on-status-holding/118483/4)
[March 20](https://cms-talk.web.cern.ch/t/tasks-with-status-new-on-command-resubmit-for-a-few-hours/116476/7)

Link to March 20 discussion in MatterMost (with some snapshots from Grafana)
https://mattermost.web.cern.ch/cms-o-and-c/pl/dgc7ntexypb15x4sy511zc1w1c

In both cases problem was solved by TW restart.

From initial look at the code, I believe that something went wrong inside Worker.py.

Action plan:
1. read and understand the code
2. add logging
3. wait for problem to happen again
4. iterate

## Comment (belforte, 2025-03-20T16:11:04Z)

**Note**: when production TW was not processing things, canary was not submitting either, why ?
Becase Master could not move any task from NEW to HOLDING and "move to canary" is applied to HOLDING tasks !
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/MasterWorker.py#L574-L578

## Comment (belforte, 2025-03-20T16:22:35Z)

Now. trying to decode what's happened


below there is an example from `proc.c3id_master.pid_18.txt.2025-03-19`

what happens is that this line returns an empty list
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/MasterWorker.py#L581
because `limit` is 0, from
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/MasterWorker.py#L561
and 
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L310-L318
where ` self.leninqueue` is "hardcoded" to 12 
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L200-L202

In other words somehow it must have happened that `self.queuedTasks()` had not been decreased when working on tasks completed. 
Note from the log that there is no message after `checking if some has finished`, looks like the multiprocess output queue ia empty
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L272-L277

IIUC code after that will always log a message `if out is not None`

```text
2025-03-19 23:37:39,607:INFO:MasterWorker:This is master TW crab-prod-tw01 running.
2025-03-19 23:37:39,608:INFO:MasterWorker:Starting work selection process.
2025-03-19 23:37:39,608:INFO:MasterWorker:Starting external scheduling.
2025-03-19 23:37:47,505:INFO:TaskUtils:Retrieved a total of 1 WAITING tasks
2025-03-19 23:37:47,505:INFO:MasterWorker:
Username | Waiting | Selected
---------|---|--
sciaba   | 1 | 1
2025-03-19 23:37:47,506:INFO:TaskUtils:Will set to NEW task 250319_223716:sciaba_crab_HC-215-T2_UK_London_IC-111311-20250319233700
2025-03-19 23:37:47,536:INFO:MasterWorker:Task 250319_223716:sciaba_crab_HC-215-T2_UK_London_IC-111311-20250319233700 status updated to 'NEW'.
2025-03-19 23:37:47,536:INFO:MasterWorker:Pruning the queue if required...logic tbd
2025-03-19 23:37:47,536:INFO:MasterWorker:Report Queue status... logic tbd
2025-03-19 23:37:47,536:INFO:MasterWorker:Work selected successfully.
2025-03-19 23:37:47,622:DEBUG:Worker:Ready to inject 0 items
2025-03-19 23:37:47,622:DEBUG:Worker:Injection completed.
2025-03-19 23:37:47,623:INFO:MasterWorker:Master Worker status:
2025-03-19 23:37:47,623:INFO:MasterWorker: - free slaves: 0
2025-03-19 23:37:47,623:INFO:MasterWorker: - acquired tasks: 12
2025-03-19 23:37:47,623:INFO:MasterWorker: - tasks pending in queue: 6
2025-03-19 23:38:17,653:INFO:Worker:12 work on going, checking if some has finished
and now another MasterWorker cycle starts immediately, becasue sleep is only inserted when some tasks are set to HOLDING
2025-03-19 23:38:17,654:INFO:MasterWorker:This is master TW crab-prod-tw01 running.
2025-03-19 23:38:17,654:INFO:MasterWorker:Starting work selection process.

```

## Comment (belforte, 2025-03-20T17:24:21Z)

While I do not really understand the code in `Worker.injectWorks`
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L246-L261
I am puzzled and worried by the fact that `workid` was oscillating below 12 inititally, then started to ramp up and now it is !stably at >190
And TW looks "slow" to me, we have  persitent backlog of tasks in NEW which is unusual

![Image](https://github.com/user-attachments/assets/082db1f9-da17-4959-94e4-261ce1f18828)

![Image](https://github.com/user-attachments/assets/45badb53-9471-4b83-b859-d88ff49b5514)

while at the same time, TW actions appears to complete as fast as usual in the last hours

![Image](https://github.com/user-attachments/assets/221b900d-fe15-44bc-aa79-59eb4f401db2)

```text
2025-03-20 10:47:43,146:DEBUG:Worker:Completed work 11 on 250318_053048:ctorresc_crab_ParkingDoubleMuonLowMass7-Run2024H-PromptReco-v1
2025-03-20 10:48:33,298:DEBUG:Worker:Completed work 3 on 250318_052509:ctorresc_crab_ParkingDoubleMuonLowMass0-Run2024E-PromptReco-v1
2025-03-20 10:48:33,299:DEBUG:Worker:Completed work 4 on 250318_052629:ctorresc_crab_ParkingDoubleMuonLowMass2-Run2024C-PromptReco-v1
2025-03-20 10:48:33,299:DEBUG:Worker:Completed work 0 on 250318_050358:ctorresc_crab_ParkingDoubleMuonLowMass2-Run2023C-22Sep2023_v4-v1
2025-03-20 10:48:33,299:DEBUG:Worker:Completed work 2 on 250318_050553:ctorresc_crab_ParkingDoubleMuonLowMass7-Run2023D-22Sep2023_v1-v1
2025-03-20 10:48:33,300:DEBUG:Worker:Completed work 1 on 250318_050423:ctorresc_crab_ParkingDoubleMuonLowMass3-Run2023D-22Sep2023_v1-v1
2025-03-20 10:48:33,300:DEBUG:Worker:Completed work 5 on 250318_052758:ctorresc_crab_ParkingDoubleMuonLowMass3-Run2024I-PromptReco-v2
2025-03-20 10:48:33,301:DEBUG:Worker:Completed work 10 on 250320_070740:hindrich_crab_ETAUL17_3200_CENTRALRW_0
2025-03-20 10:48:33,302:DEBUG:Worker:Completed work 7 on 250318_151709:spolikar_crab_Bfinder_2024_Dpgm_v1_E_0_v2
2025-03-20 10:48:33,302:DEBUG:Worker:Completed work 8 on 250319_114456:slehti_crab_Muon1_Run2024E_PromptReco_v1
2025-03-20 10:48:33,303:DEBUG:Worker:Completed work 6 on 250318_063935:rraturi_crab_CRAB_MINIAODSIM_BsToKKMuMuAPV
2025-03-20 10:49:23,404:DEBUG:Worker:Completed work 9 on 250319_230459:sciaba_crab_HC-203-T2_RU_INR-111310-20250319220300
2025-03-20 10:49:23,405:DEBUG:Worker:Completed work 11 on 250320_080459:gkaratha_crab_data_Run2022E_part3_2025Mar20
2025-03-20 10:49:23,405:DEBUG:Worker:Completed work 17 on 250320_070655:hindrich_crab_ETAUL17_3200_CENTRALB_0
2025-03-20 10:49:23,406:DEBUG:Worker:Completed work 12 on 250319_065856:hboucham_crab_MET_Run2017F
2025-03-20 10:49:23,407:DEBUG:Worker:Completed work 19 on 250320_071326:hindrich_crab_ETAUL17_3200_JERAK4Barrelup_0
2025-03-20 10:49:23,407:DEBUG:Worker:Completed work 16 on 250320_025915:sciaba_crab_HC-231-T2_CH_CSCS-111313-20250320035901
2025-03-20 10:49:23,408:DEBUG:Worker:Completed work 14 on 250320_000540:sciaba_crab_HC-205-T2_US_UCSD-111312-20250320010301
2025-03-20 10:49:23,408:DEBUG:Worker:Completed work 15 on 250320_015400:ccosby_crab_Private_EtaToGammaAp_ApToEE_ApToEE_Ap0p300GeV_EtaPt10_ONESTEP
2025-03-20 10:49:23,409:DEBUG:Worker:Completed work 20 on 250320_071859:hindrich_crab_ETAUL18_3200_TTVAR_0
2025-03-20 10:49:23,409:DEBUG:Worker:Completed work 18 on 250320_070854:sciaba_crab_HC-203-T2_CH_CERN-111310-20250319220300
2025-03-20 10:50:12,993:DEBUG:Worker:Completed work 13 on 250319_220306:fdamas_crab_RawPrime22
2025-03-20 10:50:12,993:DEBUG:Worker:Completed work 21 on 250320_081004:sciaba_crab_HC-205-T2_US_Nebraska-111312-20250320010301
2025-03-20 10:50:12,994:DEBUG:Worker:Completed work 22 on 250319_114420:slehti_crab_Muon0_Run2024E_PromptReco_v1
2025-03-20 10:50:12,995:DEBUG:Worker:Completed work 25 on 250320_053734:sciaba_crab_HC-211-T1_RU_JINR-111309-20250319202500
```
and now
```
2025-03-20 18:10:59,171:DEBUG:Worker:Completed work 198 on 250320_163156:pkatris_crab_20250320_173120
2025-03-20 18:11:48,705:DEBUG:Worker:Completed work 198 on 250319_133221:tafoyava_crab_scenarioA_mpi_2_mA_0p25_ctau_0p1
2025-03-20 18:12:37,462:DEBUG:Worker:Completed work 198 on 250319_133224:tafoyava_crab_scenarioB1_mpi_5_mA_1p00_ctau_10
2025-03-20 18:13:26,528:DEBUG:Worker:Completed work 198 on 250319_225833:wouf_crab_HJ1_2760GeV_tune078_PbPb
2025-03-20 18:14:17,517:DEBUG:Worker:Completed work 198 on 250319_135129:jingyu_crab_EMJ_postEE_M200_1mm_mD10_CP5_13p6TeV_AODSIM_124XFIXED
2025-03-20 18:15:07,657:DEBUG:Worker:Completed work 198 on 250320_162722:hindrich_crab_ETAUL16a_3300_JESFlavorPureBottomup_0
2025-03-20 18:15:57,263:DEBUG:Worker:Completed work 198 on 250320_102515:dmoran_crab_dy6-c5
2025-03-20 18:16:46,832:DEBUG:Worker:Completed work 198 on 250320_122606:hindrich_crab_ETAUL16a_3300_JESFlavorPureQuarkdown_0
2025-03-20 18:17:37,655:DEBUG:Worker:Completed work 198 on 250320_132209:dstaffor_crab_tta_m1250_w10_TuneCP5_13TeV-madgraph-pythia8_miniaodUL17v2_tta_prod
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 
```

what is exacly this `workid` ?

https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L254

## Comment (belforte, 2025-03-20T17:28:05Z)

could it be that work some tasks complete w/o this line to be executed ?
https://github.com/dmwm/CRABServer/blob/70a819bc5215217615ec30aeb43bfcb62af6036f/src/python/TaskWorker/Worker.py#L293

could be due to new code (from me) causing DagmanSubmitter end with an unusual status ?

## Comment (belforte, 2025-03-20T17:31:26Z)

hmm... counting of injected/completed:
```text
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ cat proc.c3id_master.pid_998224.txt|grep -c "INFO:Worker:Injecting work"
1664
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ cat proc.c3id_master.pid_998224.txt|grep -c "DEBUG:Worker:Completed work"
1653
```
difference is 11. Does it mean 11 QUEUED tasks (OK), or 11 "stuck workers" (BAD) ?

In any case it does not explain the 198 keys in the `self.working` dictionary

## Comment (belforte, 2025-03-20T17:40:57Z)

TW is completing about one "work" every minute. 5 min per slave. That's clearly non-sense
```text
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ cat proc.c3id_master.pid_998224.txt|grep  "DEBUG:Worker:Completed work" |tail
2025-03-20 18:31:11,447:DEBUG:Worker:Completed work 198 on 250320_172757:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
2025-03-20 18:32:02,843:DEBUG:Worker:Completed work 198 on 250320_172804:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
2025-03-20 18:32:54,864:DEBUG:Worker:Completed work 198 on 250320_172811:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
2025-03-20 18:33:43,871:DEBUG:Worker:Completed work 198 on 250320_172845:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
2025-03-20 18:34:32,978:DEBUG:Worker:Completed work 198 on 250320_133229:dstaffor_crab_tta_m750_w50_TuneCP5_13TeV-madgraph-pythia8_miniaodUL17v2_tta_prod
2025-03-20 18:35:21,201:DEBUG:Worker:Completed work 198 on 250320_133732:dstaffor_crab_tta_m1750_w10_TuneCP5_13TeV-madgraph-pythia8_miniaodUL16v2_tta_prod
2025-03-20 18:36:10,995:DEBUG:Worker:Completed work 198 on 250320_142359:hindrich_crab_ETAUL16a_3300_JESAbsoluteStatdown_0
2025-03-20 18:37:00,413:DEBUG:Worker:Completed work 198 on 250320_142439:sciaba_crab_HC-211-T1_ES_PIC-111309-20250319202500
2025-03-20 18:37:50,050:DEBUG:Worker:Completed work 198 on 250320_135445:hindrich_crab_ETAUL16a_3300_CENTRAL_0
2025-03-20 18:38:39,143:DEBUG:Worker:Completed work 198 on 250320_140540:dstaffor_crab_tta_m750_w50_TuneCP5_13TeV-madgraph-pythia8_miniaodUL16preVFPv2_tta_prod
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 

```

## Comment (belforte, 2025-03-20T17:50:47Z)

for one worker, here's situation after restart, takes "seconds" for each task and processes them very quickly one after the other
```console
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ cat proc.c3id_3*.txt |grep "completed in"|head -10|awk '{print $2" "$3" "$7" "$8" "$9" "$10}'
10:24:15,165:DEBUG:Worker:Process-3: RESUBMIT completed in 9 seconds:
10:24:23,519:DEBUG:Worker:Process-3: RESUBMIT completed in 8 seconds:
10:24:25,661:DEBUG:Worker:Process-3: RECURRING completed in 2 seconds:
10:25:08,690:DEBUG:Worker:Process-3: RESUBMIT completed in 13 seconds:
10:25:55,469:DEBUG:Worker:Process-3: RESUBMIT completed in 10 seconds:
10:26:07,176:DEBUG:Worker:Process-3: RESUBMIT completed in 11 seconds:
10:26:45,723:DEBUG:Worker:Process-3: RESUBMIT completed in 10 seconds:
10:26:55,389:DEBUG:Worker:Process-3: RESUBMIT completed in 9 seconds:
10:27:35,207:DEBUG:Worker:Process-3: RESUBMIT completed in 10 seconds:
10:27:46,535:DEBUG:Worker:Process-3: RESUBMIT completed in 11 seconds:
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$
```
but now it is a very different story
```console
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ cat proc.c3id_3*.txt |grep "completed in"|tail -10|awk '{print $2" "$3" "$7" "$8" "$9" "$10}'
17:56:51,854:DEBUG:Worker:Process-3: SUBMIT completed in 21 seconds:
18:02:33,090:DEBUG:Worker:Process-3: SUBMIT completed in 21 seconds:
18:07:31,833:DEBUG:Worker:Process-3: SUBMIT completed in 21 seconds:
18:11:29,700:DEBUG:Worker:Process-3: RESUBMIT completed in 11 seconds:
18:16:24,907:DEBUG:Worker:Process-3: KILL completed in 8 seconds:
18:21:38,016:DEBUG:Worker:Process-3: SUBMIT completed in 21 seconds:
18:26:03,017:DEBUG:Worker:Process-3: RECURRING completed in 0 seconds:
18:31:01,141:DEBUG:Worker:Process-3: SUBMIT completed in 19 seconds:
18:35:58,378:DEBUG:Worker:Process-3: SUBMIT completed in 17 seconds:
18:41:26,173:DEBUG:Worker:Process-3: RESUBMIT completed in 9 seconds:
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 
```
it processes a task every 5 minutes !!

it is the same for the other subprocesses

**what is happening in those 5 minutes ?**

## Comment (belforte, 2025-03-20T17:53:51Z)

looks like worker was fully idle !!!
```text
2025-03-20 18:45:31,339:DEBUG:Worker:Process-2: SUBMIT work on 250320_174326:atrianto_crab_freeze_bkg_only completed in 18 seconds: Status: OK
Result = OK

2025-03-20 18:45:31,356:DEBUG:Worker:RSS after finishing 250320_174326:atrianto_crab_freeze_bkg_only: b'147.621' MB
2025-03-20 18:51:03,471:DEBUG:Worker:Process-2: Starting <function handleNewTask at 0x7fe14a9148b0> on 250320_160009:sciaba_crab_HC-206-T3_UK_London_QMUL-111318-20250320165701
2025-03-20 18:51:03,472:INFO:RucioUtils:Initializing native Rucio client
```

## Comment (belforte, 2025-03-20T17:56:11Z)

so workers complete, but TW only notices once every minute that one is free and injects just one unit of work.

## Comment (belforte, 2025-03-21T08:22:03Z)

After a restart, TW is working well, but I still found something odd in the log of new  processes
```console
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ grep "work 21"  proc.c3id_master.pid_1389281.txt*
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:02:29,423:INFO:Worker:Injecting work 21: 250320_174602:rraturi_crab_CRAB_MINIAODSIM_BdToPsipKpiAPV
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 
```
there is no corresponding `Completed work 21` even if log for that task is fine and ends with
```text
2025-03-21 06:02:03,856:DEBUG:Worker:RSS after finishing 250320_174602:rraturi_crab_CRAB_MINIAODSIM_BdToPsipKpiAPV: b'120.738' MB
```

while usually log has
```console
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ grep "work 20"  proc.c3id_master.pid_1389281.txt*
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:01:39,761:INFO:Worker:Injecting work 20: 250320_172722:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:02:09,791:DEBUG:Worker:Completed work 20 on 250320_172722:aziaka_crab_Pythia8CP5Slices_Run3_Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:02:29,423:INFO:Worker:Injecting work 20: 250320_173322:wewei_crab_TTHHTo4b_HEFT_kt-2_TuneCP5_13TeV-madgraph-pythia8_2018_ntuple_0_0
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:03:48,430:DEBUG:Worker:Completed work 20 on 250320_173322:wewei_crab_TTHHTo4b_HEFT_kt-2_TuneCP5_13TeV-madgraph-pythia8_2018_ntuple_0_0
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ grep "work 22"  proc.c3id_master.pid_1389281.txt*
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:03:18,390:INFO:Worker:Injecting work 22: 250318_200227:tafoyava_crab_scenarioA_mpi_4_mA_0p80_ctau_0p1
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:03:48,431:DEBUG:Worker:Completed work 22 on 250318_200227:tafoyava_crab_scenarioA_mpi_4_mA_0p80_ctau_0p1
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:04:08,062:INFO:Worker:Injecting work 22: 250319_133033:tafoyava_crab_scenarioB1_mpi_4_mA_1p33_ctau_100
proc.c3id_master.pid_1389281.txt.2025-03-20:2025-03-20 19:04:38,096:DEBUG:Worker:Completed work 22 on 250319_133033:tafoyava_crab_scenarioB1_mpi_4_mA_1p33_ctau_100
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 
```

## Comment (belforte, 2025-03-21T08:49:38Z)

is this a ("the" ?) problem and things go bad when it cumulates during times of high load ?

## Comment (belforte, 2025-03-21T08:50:58Z)

is TW in trouble again, or am I fully off track ?
Master says "12 acquired, 6 queued" and does not inject, but slaves all completed their work, some as much as 9 minutes ago
```console
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ for l in  proc.c3id_[1-6].pid_*.txt; do tail -1 $l; done
2025-03-21 09:40:38,263:DEBUG:Worker:RSS after finishing 250320_152257:trmishra_crab_ntuplizer_10620_data_MET_Run2016H-UL2016_MiniAODv2-v2: b'166.93' MB
2025-03-21 09:36:44,384:DEBUG:Worker:RSS after finishing 250321_083527:hindrich_crab_ETAUL18_3300_JESAbsoluteScaleup_1: b'139.098' MB
2025-03-21 09:38:51,505:DEBUG:Worker:RSS after finishing TaskWorker.Actions.Recurring.BanDestinationSites: b'132.637' MB
2025-03-21 09:39:10,578:DEBUG:Worker:RSS after finishing 250321_083826:hindrich_crab_ETAUL18_3300_JESFragmentationup_1: b'180.168' MB
2025-03-21 09:48:56,215:DEBUG:Worker:RSS after finishing 250321_084125:hindrich_crab_ETAUL18_3300_JESPileUpDataMCdown_1: b'126.262' MB
2025-03-21 09:39:48,475:DEBUG:Worker:RSS after finishing 250320_152118:trmishra_crab_ntuplizer_10620_data_MET_Run2016G-UL2016_MiniAODv2-v2: b'142.383' MB
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ tail proc.c3id_master.pid_1389281.txt
2025-03-21 09:48:55,537:INFO:MasterWorker:Starting external scheduling.
2025-03-21 09:49:03,429:INFO:TaskUtils:No WAITING task retrieved.
2025-03-21 09:49:03,429:INFO:MasterWorker:No tasks in 'WAITING' status found.
2025-03-21 09:49:03,429:WARNING:MasterWorker:No tasks selected.
2025-03-21 09:49:03,484:DEBUG:Worker:Ready to inject 0 items
2025-03-21 09:49:03,484:DEBUG:Worker:Injection completed.
2025-03-21 09:49:03,485:INFO:MasterWorker:Master Worker status:
2025-03-21 09:49:03,485:INFO:MasterWorker: - free slaves: 0
2025-03-21 09:49:03,485:INFO:MasterWorker: - acquired tasks: 12
2025-03-21 09:49:03,485:INFO:MasterWorker: - tasks pending in queue: 6
crab3@crab-prod-tw01:/data/srv/TaskManager/logs/processes$ 

```

## Comment (belforte, 2025-03-24T13:25:40Z)

there is some evidence that problem is related to Recurring Actions.
I have checked difference in v3.250310 with previously running (and working) v3.250119 and there is no change in recurring action code or (Master)Worker.py part which handles them
https://github.com/dmwm/CRABServer/compare/v3.250109...v3.250310

See also [previous comment](https://github.com/dmwm/CRABServer/issues/9014#issuecomment-2742653772) where there was no "Completed" message for a tak.

## Comment (belforte, 2025-03-27T12:09:21Z)

even if canary is now running at very low fraction (1%),  it has already "leaked one slave" since last restart. Declaring 4 free slaves, but all process logs but "renew proxy" ended with the RSS report.

I have prepared TW version which logs what each slave is supposed to work on and more details from slaves.
 https://github.com/belforte/CRABServer/tree/add-diagnostic-to-Worker
on top of the "buggy" v3.250310. Built as `registry.cern.ch/cmscrab/crabtaskworker:pypi-test2-diagnosetw-1`
and have now deployed it in the Canary TW
<details><summary>detail</summary>
```
[crab3@crab-prod-tw02 ~]$ docker ps --format json |jq
{
  "Command": "\"tini -- /data/run.sh\"",
  "CreatedAt": "2025-03-27 12:57:01 +0100 CET",
  "ID": "34574b972180",
  "Image": "registry.cern.ch/cmscrab/crabtaskworker:pypi-test2-diagnosetw-1",
  "Labels": "",
  "LocalVolumes": "0",
  "Mounts": "/data/srv/tmp,/etc/grid-secu…,/etc/pki/ca-tr…,/cvmfs,/data/certs,/data/container,/etc/pki/ca-tr…,/etc/vomses,/data/containe…,/data/containe…,/data/containe…",
  "Names": "TaskWorker",
  "Networks": "host",
  "Ports": "",
  "RunningFor": "7 minutes ago",
  "Size": "0B",
  "State": "running",
  "Status": "Up 7 minutes"
}
```
</details>

so far, so good
```
2025-03-27 13:04:16,027:INFO:MasterWorker:This is canary TW crab-prod-tw02 running.
2025-03-27 13:04:25,230:DEBUG:Worker:Ready to inject 0 items
2025-03-27 13:04:25,230:DEBUG:Worker:Injection completed.
2025-03-27 13:04:25,231:INFO:MasterWorker:Master Worker status:
2025-03-27 13:04:25,231:INFO:MasterWorker: - free slaves: 5
2025-03-27 13:04:25,231:INFO:MasterWorker: - acquired tasks: 1
2025-03-27 13:04:25,231:INFO:MasterWorker:      RenewRemoteProxies.250327_125719
2025-03-27 13:04:25,231:INFO:MasterWorker: - tasks pending in queue: 0
2025-03-27 13:04:55,234:INFO:Worker:1 work on going, checking if some has finished
2025-03-27 13:04:55,234:INFO:MasterWorker:This is canary TW crab-prod-tw02 running.
```

## Comment (belforte, 2025-03-27T12:52:17Z)

Just deployed a minimally improved `registry.cern.ch/cmscrab/crabtaskworker:pypi-test2-diagnosetw-2`

```text
2025-03-27 13:50:48,154:INFO:MasterWorker:Master Worker status:
2025-03-27 13:50:48,154:INFO:MasterWorker: - free slaves: 2
2025-03-27 13:50:48,154:INFO:MasterWorker: - acquired tasks: 4
2025-03-27 13:50:48,154:INFO:MasterWorker:      wid 0 : RenewRemoteProxies.250327_135048
2025-03-27 13:50:48,154:INFO:MasterWorker:      wid 1 : RemovetmpDir.250327_135048
2025-03-27 13:50:48,154:INFO:MasterWorker:      wid 2 : BanDestinationSites.250327_135048
2025-03-27 13:50:48,154:INFO:MasterWorker:      wid 3 : GetAcceleratorSite.250327_135048
2025-03-27 13:50:48,154:INFO:MasterWorker: - tasks pending in queue: 0
2025-03-27 13:51:18,168:INFO:Worker:4 work on going, checking if some has finished
2025-03-27 13:51:18,169:DEBUG:Worker:Completed work 1 on RemovetmpDir.250327_135048
2025-03-27 13:51:18,170:DEBUG:Worker:Completed work 3 on GetAcceleratorSite.250327_135048
2025-03-27 13:51:18,170:DEBUG:Worker:Completed work 2 on BanDestinationSites.250327_135048
2025-03-27 13:51:18,171:INFO:MasterWorker:This is canary TW crab-prod-tw02 running.
2025-03-27 13:51:26,226:DEBUG:Worker:Ready to inject 0 items
2025-03-27 13:51:26,227:DEBUG:Worker:Injection completed.
2025-03-27 13:51:26,227:INFO:MasterWorker:Master Worker status:
2025-03-27 13:51:26,227:INFO:MasterWorker: - free slaves: 5
2025-03-27 13:51:26,227:INFO:MasterWorker: - acquired tasks: 1
2025-03-27 13:51:26,227:INFO:MasterWorker:      wid 0 : RenewRemoteProxies.250327_135048
2025-03-27 13:51:26,227:INFO:MasterWorker: - tasks pending in queue: 0

```

## Comment (belforte, 2025-03-28T16:57:31Z)

so far so good. No problems

## Comment (belforte, 2025-03-31T12:07:07Z)

found one leaked task
```console
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ grep 250331_100744 proc.c3id_master.pid_18.txt
[{'tm_taskname': '250331_100744:gkole_crab_QCD_Bin-PT-15to7000', 'tm_task_command': 'SUBMIT'}]
2025-03-31 12:08:48,148:INFO:Worker:Injecting work 1: 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
2025-03-31 12:08:48,150:INFO:MasterWorker:      wid 1 : 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
[...]
2025-03-31 13:23:40,494:INFO:MasterWorker:      wid 1 : 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
```
Note the lack of the `Completed work ` message for this task.
 
But the task was submitted successfully
```console
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ tail -2 ../tasks/gkole/250331_100744:gkole_crab_QCD_Bin-PT-15to7000.log

2025-03-31 12:09:09,522:DEBUG:Worker:RSS after finishing 250331_100744:gkole_crab_QCD_Bin-PT-15to7000: b'203.008' MB
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ 
```

It was handled by Worker #3, which proceeded to handle other tasks, from `proc.c3id_3.pid_31.txt`:
```text
2025-03-31 12:08:48,149:DEBUG:Worker:Process-3: Starting <function handleNewTask at 0x7f5b08de7820> on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
[...] (1)
2025-03-31 12:09:09,522:DEBUG:Worker:RSS after finishing 250331_100744:gkole_crab_QCD_Bin-PT-15to7000: b'203.008' MB
2025-03-31 12:09:09,523:DEBUG:Worker:About to put out message in results queue for workid 1
[...] (2)
2025-03-31 12:09:09,524:DEBUG:Worker:Done
2025-03-31 12:13:15,020:DEBUG:Worker:Process-3: Starting <function handleNewTask at 0x7f5b08de7820> on 250331_101157:pvaucell_crab_ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8
```

But there is unusual text in the `[...]` above.

in (1)
```text
2025-03-31 12:09:04,162:DEBUG:Handler:Starting <TaskWorker.Actions.DagmanCreator.DagmanCreator object at 0x7f5af3c3dca0> on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
[...]

2025-03-31 12:09:07,031:INFO:Handler:Finished <TaskWorker.Actions.DagmanCreator.DagmanCreator object at 0x7f5af3c3dca0> on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000 in 2 seconds
2025-03-31 12:09:07,031:DEBUG:Handler:Starting <TaskWorker.Actions.Uploader.Uploader object at 0x7f5af3c3d0a0> on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000
[...]
2025-03-31 12:09:09,496:INFO:Handler:Finished <TaskWorker.Actions.Uploader.Uploader object at 0x7f5af3c3d0a0> on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000 in 2 seconds
2025-03-31 12:09:09,504:DEBUG:Worker:Process-3: SUBMIT work on 250331_100744:gkole_crab_QCD_Bin-PT-15to7000 completed in 21 seconds: Status: OK
```
**i.e. the last step was `Uploader`.  `DagmanSubmitter` was not called.**
Indeed this task was submitted with **dry_run** option
```console
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ grep -i dry ../tasks/gkole/250331_100744:gkole_crab_QCD_Bin-PT-15to7000.log|tr , '\n'|grep -i dry
320:INFO:StageoutCheck:Will not check possibility to write to destination site.User specified dryrun option.
 'tm_dry_run': 'T'
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ 
```

and in (2) the object posted to the Results queue for of the slave pool is 
```
2025-03-31 12:09:09,523:DEBUG:Worker:About to put out message in results queue for workid 1
2025-03-31 12:09:09,523:DEBUG:Worker: out.result: (Submit(                            # i.e. the htcondor.Submit() objecty
My.CRAB_Reqname = "250331_100744:gkole_crab_QCD_Bin-PT-15to7000
My.CRAB_Workflow = "250331_100744:gkole_crab_QCD_Bin-PT-15to7000"
[...] ),
{}, ['InputFiles.tar.gz'],
([<WMCore.DataStructs.JobGroup.JobGroup object at 0x7f5af3c3dee0>, ...) # i.e. the Splitter result
- out.task: {'tm_taskname': ....                                                                                  # i.e. the Task dictionary
, 'jobcount': 800} 
5-03-31 12:09:09,524:DEBUG:Worker:Done
```
which looks OK even if `out.result` and `out.task` should better be put on different lines in
https://github.com/belforte/CRABServer/blob/957c8748d33a5254bf07320fcf8a22ebbdb8f665/src/python/TaskWorker/Worker.py#L149
```python
        logger.debug(" out.result: %s - out.task: %s ", outputs.result, outputs.task)
```

AFAICT the content of `out` message is not used in the Master/Worker/Process handshaking. I only use it to log the taskname https://github.com/belforte/CRABServer/blob/957c8748d33a5254bf07320fcf8a22ebbdb8f665/src/python/TaskWorker/Worker.py#L283-L287
```python
                workid = out['workid']
                result = out['out']
                if result:
                    taskname = result.task['tm_taskname']
                    self.logger.debug('Completed work %d on %s', workid, taskname)
```

Could it be that somehow something breaks when task processing ends at Uploader step ?

## Comment (belforte, 2025-03-31T12:26:04Z)

that one seems the only task with `dry_run` processed by the canary TW
```console
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ grep "'tm_dry_run': 'T'"  proc.c3id_*.txt|tr , '\n'|egrep "dry|taskname"
303:DEBUG:DagmanCreator:{'task': {'tm_taskname': '250331_100744:gkole_crab_QCD_Bin-PT-15to7000'
 'tm_dry_run': 'T'
 <WMCore.DataStructs.Fileset.Fileset object at 0x7f5af2f71250>)) - out.task: {'tm_taskname': '250331_100744:gkole_crab_QCD_Bin-PT-15to7000'
 'tm_dry_run': 'T'
crab3@crab-prod-tw02:/data/srv/TaskManager/logs/processes$ 
```

So I can't compare with "one which works". Primary TW does not have the extra logging.

OTOH [last change](https://github.com/dmwm/CRABServer/commit/97f447747265684589ac1f5be773eed80de02239]) to dry run handling was back  [v3.241107](https://github.com/dmwm/CRABServer/releases/tag/v3.241107)  and that code is part of current primary TW (v3.250109) which is running finely.

I will test dry-run separately and add a bit more loggin.

## Comment (belforte, 2025-03-31T13:24:18Z)

I am testing on crab-dev-tw01 and got
```
2025-03-31 15:04:31,741:INFO:Worker:Uploading failure message to the REST:
Process-1: I just had a failure for cannot pickle 'htcondor2_impl._handle' object
	workid=0
	task=250331_125914:belforte_crab_20250331_145904
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/concurrent/futures/process.py", line 204, in _sendback_result
    result_queue.put(_ResultItem(work_id, result=result,
  File "/usr/local/lib/python3.8/multiprocessing/queues.py", line 362, in put
    obj = _ForkingPickler.dumps(obj)
  File "/usr/local/lib/python3.8/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
TypeError: cannot pickle 'htcondor2_impl._handle' object
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Worker.py", line 106, in processWorkerLoop
    outputs = startChildWorker(WORKER_CONFIG, work, args, logger)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/ChildWorker.py", line 59, in startChildWorker
    raise e
  File "/data/srv/current/lib/python/site-packages/TaskWorker/ChildWorker.py", line 53, in startChildWorker
    outputs = future.result(timeout=procTimeout+1)
  File "/usr/local/lib/python3.8/concurrent/futures/_base.py", line 444, in result
    return self.__get_result()
  File "/usr/local/lib/python3.8/concurrent/futures/_base.py", line 389, in __get_result
    raise self._exception
TypeError: cannot pickle 'htcondor2_impl._handle' object

2025-03-31 15:04:31,805:INFO:Worker:Failure message successfully uploaded to the REST
2025-03-31 15:04:31,806:DEBUG:Worker:Process-1: SUBMIT work on 250331_125914:belforte_crab_20250331_145904 completed in 16 seconds: Status: ERROR
Error = cannot pickle 'htcondor2_impl._handle' object
```

Why no such error on canary crab-tw-prod02 ?

error is "sort of OK" since python doumentation says:

* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) queues serializes all objects that are put into them using [pickle](https://docs.python.org/3/library/pickle.html#module-pickle).

but while my task is in FAILED now, the one above is  happily in UPLOADED, waiting for user to give the go  https://cmsweb.cern.ch/crabserver/ui/task/250331_100744%3Agkole_crab_QCD_Bin-PT-15to7000

## Comment (belforte, 2025-03-31T13:45:30Z)

**OUCH**
my test has "child worker" enable, i.e. every worker is running the Handler in a subprocess which timeout and (crucially) exception checking !
While this is disabled in production and canary.

I set
```python
config.FeatureFlags.childWorker = False
```
for my `crab-dev-tw01` and now my test task ended in `UPLOADED` too: https://cmsweb-test2.cern.ch/crabserver/ui/task/250331_132728%3Abelforte_crab_20250331_152723

## Comment (belforte, 2025-03-31T14:09:46Z)

as a final check I am submitting a task with DryRun to `prod`.
It landed on canary, an it got "stuck".
I was hoping for the exception to be in `nohup.out` since i got it on the console anyhow when running with `pdb` [1]. But it got fully swallowed :-(


**Bottom line: this fails**
https://github.com/dmwm/CRABServer/blob/7606a362f98751b826841718b726f8be811ce7f1/src/python/TaskWorker/Worker.py#L148-L151
**because for DryRun the `outputs` object can not be pickled**


[1]
```text
(Pdb) c

Traceback (most recent call last):
  File "/usr/local/lib/python3.8/multiprocessing/queues.py", line 239, in _feed
    obj = _ForkingPickler.dumps(obj)
  File "/usr/local/lib/python3.8/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
TypeError: cannot pickle 'htcondor2_impl._handle' object
```

## Comment (belforte, 2025-03-31T15:04:21Z)

OK. I was seeing the traceback and getting the error in the TW DB becausse the `childWorker` feature uses `multiprocessing` internally, so the exception is being raised before the final message is put in the `results` queue !
And the task is processed "normally", simply with an error. Note that when there is an exception inside the worker (child or not) the `outputs` object is set to contain only the task dictionary
https://github.com/dmwm/CRABServer/blob/7606a362f98751b826841718b726f8be811ce7f1/src/python/TaskWorker/Worker.py#L122-L123
The problem is when the worker does not raise ! In which case `outputs` is the result of the last action which is a complicated object containing also the input for the next action.
So indeed when not using child worker things are fully silent because there is no try-except around 
https://github.com/dmwm/CRABServer/blob/7606a362f98751b826841718b726f8be811ce7f1/src/python/TaskWorker/Worker.py#L148-L151

## Comment (belforte, 2025-03-31T15:25:39Z)

so the problem was introduced with https://github.com/dmwm/CRABServer/commit/367e5692451b821683af7404cece63eed280d6ce on Jan 30th
where I set
https://github.com/dmwm/CRABServer/blob/7606a362f98751b826841718b726f8be811ce7f1/src/python/TaskWorker/Actions/DagmanCreator.py#L1271
and `JobSubmit` is an `htcondor.Submit()` object which can't be picked !

This is not related to changes to Uploader. Simply the type of the output of DagmanCreator changed :-(

## Comment (belforte, 2025-03-31T16:20:01Z)

hmmm.. putting `try...except` around `results.put` does not catch any exception !
Indeed the exception in https://github.com/dmwm/CRABServer/issues/9014#issuecomment-2766229808 came from the `self.__get_result()` of the `concurrent.futures` class.

But if there would be an exception in `checkFinished` is should appear in Master log.

## Comment (belforte, 2025-03-31T16:34:37Z)

in `checkFinished` 
```python
out = self.results.get_nowait()
```
simply returns `queue.Empty`
and indeed while stepping through things I can see that
```text
(Pdb) Traceback (most recent call last):
  File "/usr/local/lib/python3.8/multiprocessing/queues.py", line 239, in _feed
    obj = _ForkingPickler.dumps(obj)
  File "/usr/local/lib/python3.8/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
TypeError: cannot pickle 'htcondor2_impl._handle' object
```
is printed to console when the Worker arrives at the end, i.e. at `results.put` time.

I am really annoyed that I can't get to see the error in any other way than with `pdb` !!

Anyhow, let's try to fix.

## Comment (belforte, 2025-03-31T20:28:09Z)

I have modified the `processWorkerLoop` so that the object put in the shared queue is always the simple
```python
outputs = Result(task=task, result='OK')
```
similarly to what done in case of exceptions, as per https://github.com/dmwm/CRABServer/issues/9014#issuecomment-2766528992
