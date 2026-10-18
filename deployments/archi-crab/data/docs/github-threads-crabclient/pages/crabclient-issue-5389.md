# dmwm/CRABClient issue #5389: odd error from crab status

State: closed
Opened: 2025-05-07T16:32:44Z
Closed: 2025-05-07T19:53:01Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5389

## Opening post (belforte, 2025-05-07T16:32:44Z)

in the gitlab [pipeline]() I just got this traceback
```text
CRAB project directory:		/home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/workdir/CMSSW_13_0_2/src/crab_20250507_173653
Task name:			250507_153655:crabint1_crab_20250507_173653
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/250507_153655%3Acrabint1_crab_20250507_173653
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=250507_153655%3Acrabint1_crab_20250507_173653&from=1746628615000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol', 'T2_ES_CIEMAT', 'T2_US_MIT', 'T2_UK_London_Brunel']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	SUBMITTED

Jobs status:                    running      		  0.5% (   5/1000)
				transferring 		 99.5% ( 995/1000)

Output dataset:			/GenericTTbar/crabint1-autotest-1746632213-94ba0e06145abd65ccb1d21786dc7e1d/USER

No publication information available yet
Traceback (most recent call last):
  File "/home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/cicd/gitlab/st/statusTracking.py", line 175, in <module>
    main()
  File "/home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/cicd/gitlab/st/statusTracking.py", line 160, in main
    status_command_output = crab_cmd({'cmd': 'status', 'args': status_dict})
  File "/home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/cicd/gitlab/st/statusTracking.py", line 20, in crab_cmd
    output = crabCommand(configuration['cmd'], **configuration['args'])
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02888/share/cms/crab-dev/v3.250505.00/lib/CRABAPI/RawCommand.py", line 28, in crabCommand
    return execRaw(command, arguments)
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02888/share/cms/crab-dev/v3.250505.00/lib/CRABAPI/RawCommand.py", line 52, in execRaw
    res = cmdobj()
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02888/share/cms/crab-dev/v3.250505.00/lib/CRABClient/Commands/status.py", line 243, in __call__
    self.printDetails(statusCacheInfo, automaticSplitt, self.jobids, True, maxMemory, maxJobRuntime, numCores)
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02888/share/cms/crab-dev/v3.250505.00/lib/CRABClient/Commands/status.py", line 576, in printDetails
    ec = str(info['Error',0]) # exit code of this failed job
KeyError: 0
```

running again crab status from same crab-dev in IB reproduces the error

to be investigated

## Comment (belforte, 2025-05-07T16:42:06Z)

do not know why it did not surface in https://github.com/dmwm/CRABServer/issues/9063

## Comment (belforte, 2025-05-07T16:50:15Z)

it happens that in this case the code has
`ec = str(info['Error',0])`
with the integer 0 as key. but the key in the dictionary is a string
```
(Pdb) info['Error'].keys()
dict_keys(['0'])
```
A bug in my latest changes to `cache_status.py` in TW ?

YES !

## Comment (belforte, 2025-05-07T19:53:01Z)

Closing, since it is a Server bug. WIll be followed up in the issue above.
