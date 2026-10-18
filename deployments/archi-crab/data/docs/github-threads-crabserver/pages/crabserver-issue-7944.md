# dmwm/CRABServer issue #7944: Publisher monitoring - acquired files by task panel is empty 

State: closed
Opened: 2023-10-13T09:26:10Z
Closed: 2023-10-13T20:57:09Z
Labels: Type: Bug, Status: Done, Area: MONIT, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7944

## Opening post (mapellidario, 2023-10-13T09:26:10Z)

### problem

While investigating the recent alerts from Publisher,
I noticed that something is wrong with publisher monitoring
in "Taskworker Internals" dashboard.
In particular, the panel "acquired files by task" is empty
since 2023-09-14 from about 10am, when Wa deployed v3.230913.

And it makes sense that it is empty, we populate that
panel parsing [3] this logger.debug [4], but the Publisher
loglevel is set to info [5].

Does anybody know how this could work before? Sorry if I have only questions so far :)

### solution

If we rely on a line on our logs for our monitoring, that line should at least be of loglevel `info`. I propose to change [4] to `.info()`

---

[1] https://monit-grafana.cern.ch/goto/pGEgCEMSR?orgId=11

![image](https://github.com/dmwm/CRABServer/assets/16376695/04c4a129-d268-498c-835e-6f4032e3df7e)

[2] https://cms-logbook.cern.ch/elog/Analysis+Operations/3838
[3] [(grok)](https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/script/Monitor/logstash/crabtaskworker.conf#L105)
[4] https://github.com/dmwm/CRABServer/blame/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/python/Publisher/PublisherMaster.py#L448
[5] https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/5b5bc1eb01d01a7858c7980a32d982876505897e/code/templates/crabtaskworker/publisher/Publisher_scheddConfig.py.erb#L38

## Comment (belforte, 2023-10-13T09:29:56Z)

was [5] changed ? Or was it a change in the Publisher code ? last one is surely possible, esp. if logs changes with a CRAB version change !

## Comment (belforte, 2023-10-13T13:17:01Z)

AFAICT `config.General.logLevel ' (from [5]) is never used in the code. But we do set log level to INFO in the  intialization, since ever. I am looking, so far failing to see what made that printout disappear

## Comment (belforte, 2023-10-13T13:19:14Z)

Let's compare v3.230913 with previous one

## Comment (belforte, 2023-10-13T13:49:11Z)

I saved earliest Publisher master log files in `/data/srv/Publisher/logs/processes/SAVED`
```
[crab3@crab-prod-tw01 SAVED]$ ls -l
total 2176
-rw-r--r--. 1 crab3 crab3 757696 Sep 13 23:47 proc.c3id_master.pid_18.txt.2023-09-13
-rw-r--r--. 1 crab3 crab3 643572 Sep 14 23:50 proc.c3id_master.pid_18.txt.2023-09-14
-rw-r--r--. 1 crab3 crab3 823074 Sep 15 23:49 proc.c3id_master.pid_18.txt.2023-09-15
[crab3@crab-prod-tw01 SAVED]$ 
```
and here's the transition to INFO only:
```
2023-09-14 09:45:52,345:INFO:master:Next cycle will start at 10:15:02
2023-09-14 10:13:54,107:INFO:master:PUBSTART: {"version": "v3.230913", "asoworker": "schedd", "instance": "prod", "max_slaves": 6, "DBShost": "cmsweb-prod.cern.ch", "dryRun": false}
2023-09-14 10:13:54,108:INFO:master:version: v3.230913
2023-09-14 10:13:54,108:INFO:master:asoworker: schedd
2023-09-14 10:13:54,108:INFO:master:instance: prod
2023-09-14 10:13:54,108:INFO:master:max_slaves: 6
2023-09-14 10:13:54,109:INFO:master:DBShost: cmsweb-prod.cern.ch
2023-09-14 10:13:54,109:INFO:master:dryRun: False
2023-09-14 10:13:54,225:INFO:master:Will connect to CRAB service: prod
2023-09-14 10:13:54,225:INFO:master:Will connect to CRAB Data Base prod instance via URL: https://cmsweb.cern.ch
2023-09-14 10:13:54,226:INFO:master:Processing publication requests for asoworker: schedd
2023-09-14 10:13:54,379:INFO:master:29 acquired publications retrieved for asoworker schedd
2023-09-14 10:13:54,379:INFO:master:kicking off pool for 11 tasks using up to 6 concurrent slaves
2023-09-14 10:13:54,386:INFO:master:Starting process <Process name='Process-1' pid=44 parent=18 started> 
```
the table of aquired files by tasks should have been between the last and next to last lines above. e.g. a few minutes before
```
2023-09-14 09:45:02,061:DEBUG:master:Retrieving publications from oracleDB
2023-09-14 09:45:02,062:INFO:master:Processing publication requests for asoworker: schedd
2023-09-14 09:45:02,133:DEBUG:master:Retrieving max.100000 acquired publications from oracleDB
2023-09-14 09:45:02,234:INFO:master:41 acquired publications retrieved for asoworker schedd
2023-09-14 09:45:02,234:INFO:master:kicking off pool for 11 tasks using up to 6 concurrent slaves
2023-09-14 09:45:02,235:DEBUG:master:++++++ Using this taskBlackList: ['old']
2023-09-14 09:45:02,236:DEBUG:master: # of acquired files : taskname
2023-09-14 09:45:02,236:DEBUG:master:acquired_files:   OK     1 : 230912_165353:bharikri_crab_2023_Sep_12_step3_RAW2DIGI_MINIAODSIM_Pythia8_QCDPhoton30_TuneCP5
2023-09-14 09:45:02,236:DEBUG:master:acquired_files:   OK     7 : 230914_024434:chouy_crab_job_DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8
2023-09-14 09:45:02,237:DEBUG:master:acquired_files:   OK     1 : 230910_231821:ciperez_crab_RSGravitonToGammaGamma_kMpl001_M_750_TuneCP2_UL
...
```

## Comment (belforte, 2023-10-13T14:02:49Z)

a possibility is that we had always been starting Publsher with -d flag. But the [/data/run.sh](https://github.com/dmwm/CRABServer/blob/master/Docker/run.sh) script only does `start.sh -c` and has not changed since 2 years ago. pff..

## Comment (belforte, 2023-10-13T15:01:09Z)

I can't find any explanation for whey the log level was effectively set to DEBUG until September.
I can accept that when putting in Puclisher_Rucio I messed up something in the effort of consolidating, but nothig seems changed. Also looking at code from v3.230220 the log level is set to INFO.

## Comment (belforte, 2023-10-13T15:02:33Z)

Can we deploy the previous Publisher on a test VM and see what happens ?

## Comment (belforte, 2023-10-13T15:19:22Z)

I am running Publisher_schedd in crab-dev-tw01 and it seems it does print the logger.debug as well. Digging.

## Comment (belforte, 2023-10-13T15:35:48Z)

OK. Found.
As feared it is a bug introduced when I put in a common wrapper to start Publisher_schedd and Publisher_rucio
In this line I take `debug` flag from the option in `start.sh` command
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/python/Publisher/RunPublisher.py#L49
while earlier the Master was instantiated via this line
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/python/Publisher/PublisherMaster.py#L766
and so the `debug` flag has the default value
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/python/Publisher/PublisherMaster.py#L81

## Comment (belforte, 2023-10-13T15:42:30Z)

THis clearly suffers of "confused history" where the `debug` flag was used both to activate a `pdb` breakpoint and to set loglevel.
But I do not feel like refactoring all of that.

So we can restore previous behavior by forcing again `debug=True` or put all messages we care about at loglevel INFO.
All in all I prefer the latter. But the former is safer.

@mapellidario what do you suggest ? A view from the outside can surely help !

## Comment (belforte, 2023-10-13T15:43:25Z)

If OK with you, I will cleanup this issue deleting all those comments which I added to help me tracking my investigation

## Comment (mapellidario, 2023-10-13T16:25:31Z)

Instead of deleting them, you could hide them marking as "outdated". How you investigated this issue may be useful for future operators! 

In any case, I agree that we should set to "info" all the logs we care about, considering as authoritative source of truth the file with list of grok expressions

## Comment (belforte, 2023-10-13T17:16:27Z)

thanks for the advice Dario. It is too late to change tonight though.
Well.. as to "how to debug" I should have not trusted looking at one line of code and simply tested with pdb right away, would have found the flag `debug=True` and onward from there !
