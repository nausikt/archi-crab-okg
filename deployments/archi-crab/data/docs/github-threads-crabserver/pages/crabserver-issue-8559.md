# dmwm/CRABServer issue #8559: incorrect handling of partial dataset

State: open
Opened: 2024-07-25T08:42:56Z
Labels: Type: Bug, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/8559

## Opening post (belforte, 2024-07-25T08:42:56Z)

with ref to https://cmsweb.cern.ch/crabserver/ui/task/240725_080735%3Aekauffma_crab_CICADA_Tau_Run2024F_v1_c_20240725
the messages printed by crab status [1] are clearly inconsistent.
Why were block partially on disk not processed ?




[1]
```text
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ekauffma/crab_CICADA_Tau_Run2024F_v1_c_20240725
Task name:			240725_080735:ekauffma_crab_CICADA_Tau_Run2024F_v1_c_20240725
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/240725_080735%3Aekauffma_crab_CICADA_Tau_Run2024F_v1_c_20240725
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=ekauffma&var-task=240725_080735%3Aekauffma_crab_CICADA_Tau_Run2024F_v1_c_20240725&from=1721891255000&to=now
Warning:			Some blocks are on TAPE only and can not be read.
				You specified to accept a partial dataset, so all blocks
				 on disk will be processed even if only partially replicated
Warning:			82 blocks will be skipped because are not completely replicated on DISK: ['/Tau/Run2024F-v1/RAW#0e3617e6-a320-457a-80b5-b5cfac63018a', '/Tau/Run2024F-v1/RAW#11ab728c-1ace-4080-8d3d-2ac6ec9db460', '/Tau/Run2024F-v1/RAW#11d0e24f-301f-4c69-b3ec-d4de27728f4e', '...']
Failure message from server:	The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset '/Tau/Run2024F-v1/RAW'. (or at least for what passed the lumi-mask and/or run-range selection).
				Use `crab checkdataset` command to find block locations
				and compare with your black/white list
				
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ekauffma/crab_CICADA_Tau_Run2024F_v1_c_20240725/crab.log
```
