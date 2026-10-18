# dmwm/CRABServer issue #8169: Jenkins StatusTracking test fails in getting task status

State: closed
Opened: 2024-01-12T09:47:30Z
Closed: 2024-01-12T09:57:45Z
Labels: Type: Bug, Priority: TOP, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8169

## Opening post (belforte, 2024-01-12T09:47:30Z)

from Jenkins log
<details>
  <summary>Click me</summary>
 <verbatim>
 
23:25:58 ATTENTION return value for 'remake' has been changed to a dictionary
23:25:58  format is {'commandStatus': 'SUCCESS' or 'FAILED',
23:25:58             'workDir': name of the work directory created}
23:25:58 Remaking crab_20240111_230304 folder.
23:25:58 Remaking .requestcache file.
23:25:58 Success: Finished remaking project directory crab_20240111_230304
23:25:58 Traceback (most recent call last):
23:25:58   File "./testingScripts/statusTracking.py", line 138, in <module>
23:25:58     main()
23:25:58   File "./testingScripts/statusTracking.py", line 126, in main
23:25:58     status_command_output = crab_cmd({'cmd': 'status', 'args': status_dict})
23:25:58   File "./testingScripts/statusTracking.py", line 19, in crab_cmd
23:25:58     output = crabCommand(configuration['cmd'], **configuration['args'])
23:25:58   File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.231101.00/lib/CRABAPI/RawCommand.py", line 28, in crabCommand
23:25:58     return execRaw(command, arguments)
23:25:58   File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.231101.00/lib/CRABAPI/RawCommand.py", line 51, in execRaw
23:25:58     cmdobj = getattr(mod, command)(logger, args)
23:25:58   File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.231101.00/lib/CRABClient/Commands/status.py", line 49, in __init__
23:25:58     SubCommand.__init__(self, logger, cmdargs)
23:25:58   File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.231101.00/lib/CRABClient/Commands/SubCommand.py", line 278, in __init__
23:25:58     SubCommand.validateOptions(self)
23:25:58   File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.231101.00/lib/CRABClient/Commands/SubCommand.py", line 660, in validateOptions
23:25:58     if not os.path.isdir(self.options.projdir):
23:25:58   File "/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_26/external/slc7_amd64_gcc700/bin/../../../../../../../slc7_amd64_gcc700/external/python/2.7.14-pafccj/lib/python2.7/genericpath.py", line 49, in isdir
23:25:58     st = os.stat(s)
23:25:58 TypeError: coercing to Unicode: need string or buffer, dict found
 </verbatim>
</details>

there's a `TypeError: coercing to Unicode: need string or buffer, dict found` coming from `status_command_output = crab_cmd({'cmd': 'status', 'args': status_dict})`
this is due to
https://github.com/dmwm/CRABServer/blob/7b0e1b5d54f8bb30b54cc2dd331504eff8e0d7c5/test/container/testingScripts/statusTracking.py#L121-L126
where `remake_dir` is handled as a string, but is instead a  dictionary !
clearly the code was not properly adapted to the new "each command returns a dictionary" standard for CRABClient.

See also these lines earlier in the log
```
23:25:58 ATTENTION return value for 'remake' has been changed to a dictionary
23:25:58  format is {'commandStatus': 'SUCCESS' or 'FAILED',
23:25:58             'workDir': name of the work directory created}
```

This indicates that we did not use StatusTracking test with CRABClient version v3.231010 or later :disappointed:

## Comment (belforte, 2024-01-12T10:27:35Z)

things are more complicated
1. the Jenkins Check_Result test still uses the container, so it is not enough to push a change to master
2. the code in there is not really "scram independent" as I wrote, since now statusTracking.py used python2
https://github.com/dmwm/CRABServer/blob/7b0e1b5d54f8bb30b54cc2dd331504eff8e0d7c5/test/container/testingScripts/statusTracking.py#L1 but we should use python3 from CMSSW like we do with CRABClient. For simplicity and since we do not use any Rucio-related code here, let's stick with
- use python3 for CMSSW_12 or later
- use python2 otherwise

So we need to change this
```bash
#1.2. Run tests
# dario, 2022-11: why dont we need the singluarity container here?
# stefano, 2023-12: we do not use crab submit here, so do not use
#                   any CMSSW code and are "scram independent"
export DOCKER_OPT="-u $(id -u):$(id -g) -v /home:/home -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group" 
export DOCKER_ENV="-e inputDataset -e ghprbPullId -e SCRAM_ARCH -e CRABServer_tag -e Client_Validation_Suite -e Task_Submission_Status_Tracking -e Client_Configuration_Validation -e X509_USER_CERT -e X509_USER_KEY -e CMSSW_release -e REST_Instance -e CRABClient_version -e Check_Publication_Status"
export DOCKER_VOL="-v $WORKSPACE/artifacts/:/data/CRABTesting/artifacts:Z -v /cvmfs/grid.cern.ch/etc/grid-security:/etc/grid-security  -v /cvmfs/grid.cern.ch/etc/grid-security/vomses:/etc/vomses  -v /cvmfs:/cvmfs"
docker run --rm $DOCKER_OPT $DOCKER_VOL $DOCKER_ENV --net=host \
$Test_Docker_Image -c 	\
'source setupCRABClient.sh; ./testingScripts/statusTracking.py' || export ERR=true
```
in https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_CheckTestResults/configure
