# dmwm/CRABClient issue #5374: make crab recover py2 compatible

State: closed
Opened: 2025-02-17T14:04:08Z
Closed: 2025-06-04T14:43:22Z
URL: https://github.com/dmwm/CRABClient/issues/5374

## Opening post (belforte, 2025-02-17T14:04:08Z)

it fails on e.g. CMSSW_10_6 with


14:54:54 Submitting file: ./crabConfiguration.py
14:54:55 Traceback (most recent call last): File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/bin/crab.py", line 154, in <module> client = CRABClient() File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/bin/crab.py", line 54, in __init__ self.subCommands = getAvailCommands() File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/ClientUtilities.py", line 341, in getAvailCommands subcmdplugins = getPlugins(subcmdpath, subcmdname, ['SubCommand']) File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/ClientUtilities.py", line 270, in getPlugins mod = __import__('%s.%s.%s' % (namespace, plugins, el[1]), globals(), locals(), el[1]) File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/Commands/recover.py", line 713 print(submitConfiguration, file=fd) ^ SyntaxError: invalid syntax

## Comment (aspiringmind-code, 2025-06-03T11:59:04Z)

@belforte I believe this issue is outdated as recover.py script looks py2 compatible.

## Comment (belforte, 2025-06-03T14:29:00Z)

it would be good to see positive proof that it is working.

## Comment (aspiringmind-code, 2025-06-04T13:50:34Z)

Running Client validation on Jenkins doesn't give the error anymore. [Build 960](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/960/)
```
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --dir=crab_20250604_105706  
TEST_RESULT: OK                                                                                 
TEST_MESSAGE:
Collecting information about original task ...
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
Tasks in status COMPLETED can not be recovered
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20250604_105706/crab.log
____________

____________
TEST_COMMAND: crab recover  --proxy=/tmp/x509up_u501  --task=250604_085714:cmsbot_crab_20250604_105706  --instance=prod  
TEST_RESULT: OK                                                                                 
TEST_MESSAGE:
crab recover requires a projdir. Since you passed a taskname, we will run crab remake
Warning: crab_20250604_105706/.requestcache not created, because it already exists.
Collecting information about original task ...
Rucio client intialized for account cmsbot
recover process prematurely exited during checkKill step
Tasks in status COMPLETED can not be recovered
Log file is /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab_20250604_105706/crab.log
```
However, I will also check manually in a case where some failures occur.

## Comment (belforte, 2025-06-04T14:43:22Z)

using git blame, it looks like it was fixed in March
https://github.com/dmwm/CRABClient/commit/efd83431112685d8eb044963da8f13d320b02a65
when the issue was independently re-discovered in https://github.com/dmwm/CRABClient/issues/5378

by which time I had forgotten that I had created this one issue a month before :-(

sorry man !
