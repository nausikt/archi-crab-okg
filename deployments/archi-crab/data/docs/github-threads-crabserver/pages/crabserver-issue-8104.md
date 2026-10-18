# dmwm/CRABServer issue #8104: in CCV replace `sendPythonFolder` test with `sendVenvFolder`

State: closed
Opened: 2023-12-15T22:07:06Z
Closed: 2023-12-18T18:21:23Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8104

## Opening post (belforte, 2023-12-15T22:07:06Z)

(no text)

## Comment (belforte, 2023-12-15T22:54:27Z)

testing in https://github.com/dmwm/CRABServer/issues/8106 after merging in  https://github.com/dmwm/CRABServer/tree/testJenkins   branch #8105

## Comment (belforte, 2023-12-15T23:40:00Z)

test script failed to run, error setting up Rucio client, apparently (required for crab status). Need some time to investigate. [test log](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/791/console)

## Comment (belforte, 2023-12-18T18:05:08Z)

The problem seems the known one that in Jenkins scritp we have
```
export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared 
```
near the top and that messes up the python env.
Moving it to the bottom right before
```
$WORKSPACE/cms-bot/create-gh-issue.py -r $Repo_GH_Issue -t "$issueTitle" -R message_CCVResult
```
solved the problem.
I also took this chance to stop using the container for SL7 here as well. Always use singularity.
