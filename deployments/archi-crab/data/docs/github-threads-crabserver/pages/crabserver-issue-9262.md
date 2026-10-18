# dmwm/CRABServer issue #9262: CMSSW_8_0_36 ships with old Git 1.8.3.1 bin and an obsolete ca-bundle, thus break our CI/CD release pipeline.

State: closed
Opened: 2026-01-19T09:04:28Z
Closed: 2026-01-19T11:25:13Z
Labels: Type: Bug, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/9262

## Opening post (nausikt, 2026-01-19T09:04:28Z)

I encountered [error](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/67867444) [1] in CI/CD release pipeline only with **CMSSW_8_36** 

Specifically while the pipeline is doing *git clone CRABClient*, during the submission testsuite stage

Its turn out that `cmsenv` enforce us to use old git by exports two problematic env variables that override the system-wide Git.
```bash
+++ export GIT_SSL_CAINFO=/cvmfs/cms.cern.ch/slc7_amd64_gcc530/external/git/1.8.3.1-giojec/share/ssl/certs/ca-bundle.crt
+++ export GIT_EXEC_PATH="/cvmfs/cms.cern.ch/slc7_amd64_gcc530/external/git/1.8.3.1-giojec/libexec/git-core";
```
 
[1] `SSL certificate problem: unable to get local issuer certificate`
```bash
++ git clone [https://github.com/dmwm/CRABClient](https://github.com/dmwm/CRABClient) /home/gitlab-runner/shell/builds/t3\_ZsMk1N/0/crab3/CRABServer/workdir/CMSSW\_8\_0\_36/src/CRABClient -b master
Cloning into '/home/gitlab-runner/shell/builds/t3\_ZsMk1N/0/crab3/CRABServer/workdir/CMSSW\_8\_0\_36/src/CRABClient'...
fatal: unable to access '[https://github.com/dmwm/CRABClient/](https://github.com/dmwm/CRABClient/)': SSL certificate problem: unable to get local issuer certificate
~/shell/builds/t3\_ZsMk1N/0/crab3/CRABServer
```

## Comment (belforte, 2026-01-19T10:19:24Z)

Hi @smuzaffar it looks like there is an old ca-bundle in older CMSSW releases. I have found same problem with CMSSW_7_6_7 which points to `/cvmfs/cms.cern.ch/slc7_amd64_gcc493/external/git/1.8.3.1/share/ssl/certs/ca-bundle.crt`
More older releases may suffer same problem , most likely the root CA used by github.com has expired and was renewed. 
Could a general solution be found ?

## Comment (smuzaffar, 2026-01-19T11:00:35Z)

@belforte , yes this is a know issue ( see https://github.com/cms-sw/cmssw/issues/49762 ). I can deploy the fix i.e. globally unset GIT_SSL_CAINFO for slc6/slc7

## Comment (belforte, 2026-01-19T11:15:13Z)

Thanks @smuzaffar, and sorry for multiple reporting. We are now OK since   Krittin has changed our build script to use system git for git clone. For us it does not matter whether you distribute git or not or whatever solution you pick for the users at large.
