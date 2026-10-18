# dmwm/CRABServer issue #8147: validate TaskWorker v3.240111 and CRABClient v3.240110

State: closed
Opened: 2024-01-11T17:34:19Z
Closed: 2024-01-13T12:16:36Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8147

## Opening post (belforte, 2024-01-11T17:34:19Z)

run our standard Jenkins to make sure that also after build and deploy the new versions do not break anything.
Tests will not validate that they fix the problems, but that was checked by hand running from GH
I am running just ClientValidation and ClientConfigurationValidation

- [x] https://github.com/dmwm/CRABServer/issues/8145
- [x] https://github.com/dmwm/CRABServer/issues/8156
- [x] https://github.com/dmwm/CRABServer/issues/8148
- [x] https://github.com/dmwm/CRABServer/issues/8155
- [x] https://github.com/dmwm/CRABServer/issues/8149
- [x] https://github.com/dmwm/CRABServer/issues/8150
- [x] https://github.com/dmwm/CRABServer/issues/8151
- [x] https://github.com/dmwm/CRABServer/issues/8152
- [x] https://github.com/dmwm/CRABServer/issues/8153
- [x] https://github.com/dmwm/CRABServer/issues/8154

## Comment (belforte, 2024-01-11T21:15:32Z)

Run again CV only after modifying test to fail when using wrong python https://github.com/dmwm/CRABServer/commit/7b0e1b5d54f8bb30b54cc2dd331504eff8e0d7c5
(change makes `crab-prod` fail in CMSSW_10_6 as per https://github.com/dmwm/CRABServer/issues/8159 )

All tests for CMSSW_10_1 or earlier are already successful with `crab-prod` because we already used python2 there.
The problem with new client was only with CMSSW_10_2 and later. 
CMSSW_11 has a py3 compatible `LumiList.py` so it is immune to the test introduced in  https://github.com/dmwm/CRABServer/commit/7b0e1b5d54f8bb30b54cc2dd331504eff8e0d7c5
I need a fancier PSet to exercise that. Have asked Matti
I have verified that the `AttributeError: 'unicode' object has no attribute 'cppTag'` error can be reproduced in CMSSW_13_ by adding the "foo lines" from https://cms-talk.web.cern.ch/t/crab-job-failed-with-exit-code-7002/32986/9
but with the corrected client the PSwet.pkl is correctly expanded, but fails and I can't get the satisfactory "job successful"
* task with the "cppTag" error:  https://cmsweb-testbed.cern.ch/crabserver/ui/task/240111_212707%3Abelforte_crab_20240111_222706  (CMSSW_11_3_4 submitted with crab-prod)
* task with the "foo" error https://cmsweb-testbed.cern.ch/crabserver/ui/task/240111_214849%3Abelforte_crab_20240111_224847  (CMSSW_11_3_4 submitted with crab-dev from IB i.e. v3.240111)

* Jenkins CV after the change https://github.com/dmwm/CRABServer/commit/7b0e1b5d54f8bb30b54cc2dd331504eff8e0d7c5
- [ ]  https://github.com/dmwm/CRABServer/issues/8159 **FAILS**
- [x] https://github.com/dmwm/CRABServer/issues/8167 **OK**

## Comment (belforte, 2024-01-11T21:58:23Z)

a last run of full validation of make sure nothing major has been broken in latest TW update.
Also deploy Publishers from new version and check publication too.
One CMSSW release should suffice
- [ ] https://github.com/dmwm/CRABServer/issues/8168
that test was ultimately successful, but with a long history of changes and there are errors in publication with Rucio (never tested before, I presume). tracked in https://github.com/dmwm/CRABServer/issues/8178

Let's try a new one without publication test, hoping for a clean result
- [ ] https://github.com/dmwm/CRABServer/issues/8176
oh damn. dev client fails to submit with Rucio ASO, will look at that separately #8179 

Let's validate new TW with current prod client, at least
- [x] https://github.com/dmwm/CRABServer/issues/8177

try again with dev client after fixing #8179 in #8180
- [x] https://github.com/dmwm/CRABServer/issues/8181

## Comment (belforte, 2024-01-13T09:42:49Z)

All OK. Vaidation concluded
