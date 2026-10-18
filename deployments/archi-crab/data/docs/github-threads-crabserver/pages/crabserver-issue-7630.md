# dmwm/CRABServer issue #7630: Jenkins integration tests - apptainer/singularity does not work on cmssdt nodes

State: closed
Opened: 2023-05-09T12:12:46Z
Closed: 2023-05-09T12:47:43Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7630

## Opening post (mapellidario, 2023-05-09T12:12:46Z)

Submitting integration tests from the jenkins job [CRABServer_ExecuteTests](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests) is currently broken.

The error is [1] and Andrea managed to reproduce it by simply logging into a `cms-dmwm-cc7` node and starting the singularity image with `/cvmfs/cms.cern.ch/common/cmssw-el8`.

She said that they will have a look, but for the time being every test will need to be submitted "manually" by us.

[1]

```plaintext
11:54:04 + /cvmfs/cms.cern.ch/common/cmssw-el8 -- ./taskSubmission.sh
11:54:04 ERROR  : Failed to create user namespace: user namespace disabled
```

## Comment (mapellidario, 2023-05-09T12:47:43Z)

(github has a glitch and reated the same issue twice)
