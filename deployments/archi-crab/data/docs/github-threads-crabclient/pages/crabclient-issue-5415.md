# dmwm/CRABClient issue #5415: report to users result of automatic splitting probe jobs.

State: closed
Opened: 2025-09-19T12:11:16Z
Closed: 2025-09-26T08:19:42Z
Labels: enhancement, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5415

## Opening post (belforte, 2025-09-19T12:11:16Z)

Users may find it useful to know the metrics which probe jobs reported: ev/sec, ram, output size.
Those should be exposed by `crab status` so user can decide if to let automatic splitting go or kill and adjust or reuse themselves for a fixed splitting task.

Also take this chance to report status and progress of probe jobs. I hate the silent "look at the FAQ".

## Comment (belforte, 2025-09-23T09:40:08Z)

easiest way is to parse PreDag log from WEB_DIR and "promise never to change that log format". A more robust but complicated solution is to write a JSON in PreDag and add code in CacheStatus.py so that a dictionary is added to the status cache file.

## Comment (belforte, 2025-09-25T15:55:25Z)

use this chance to also avoid these warnings in case of automatic splitting, makes no sense to suggest to use what it is being used already !

<img width="891" height="138" alt="Image" src="https://github.com/user-attachments/assets/ad2d0cae-8f49-4a76-a778-6f812b87644a" />

## Comment (belforte, 2025-09-25T16:06:40Z)

example output with new code:
```text
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20250925_170606
Task name:			250925_150615:belforte_crab_20250925_170606
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/250925_150615%3Abelforte_crab_20250925_170606
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=250925_150615%3Abelforte_crab_20250925_170606&from=1758809175000&to=now
Status on the scheduler:	SUBMITTED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch/scheddmon/059/belforte/250925_150615:belforte_crab_20250925_170606/AutomaticSplitting/

Probe Jobs status:              finished     		100.0% (5/5)
Estimated application throughput from probe jobs :
  found 5 completed jobs
  average throughput for 5 jobs: 3716.7478 evt/s
  average eventsize for 5 jobs: 19.8 bytes

Jobs status:                    finished     		 29.4% ( 5/17)
				running      		 70.6% (12/17)
```
