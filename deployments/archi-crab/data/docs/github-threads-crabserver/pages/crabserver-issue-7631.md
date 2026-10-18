# dmwm/CRABServer issue #7631: Jenkins integration tests - apptainer/singularity does not work on cmssdt nodes

State: closed
Opened: 2023-05-09T12:13:52Z
Closed: 2023-05-16T10:48:40Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7631

## Opening post (mapellidario, 2023-05-09T12:13:52Z)

Submitting integration tests from the jenkins job [CRABServer_ExecuteTests](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests) is currently broken.

The error is [1] and Andrea managed to reproduce it by simply logging into a `cms-dmwm-cc7` node and starting the singularity image with `/cvmfs/cms.cern.ch/common/cmssw-el8`.

She said that they will have a look, but for the time being every test will need to be submitted "manually" by us.

[1]

```plaintext
11:54:04 + /cvmfs/cms.cern.ch/common/cmssw-el8 -- ./taskSubmission.sh
11:54:04 ERROR  : Failed to create user namespace: user namespace disabled
```

## Comment (belforte, 2023-05-12T15:46:15Z)

@mapellidario maybe you can close this now ?

## Comment (belforte, 2023-05-12T15:46:53Z)

we do not need to write here how Shahzad fixed namespace things

## Comment (mapellidario, 2023-05-16T10:48:40Z)

this is ok indeed. thanks stefano
