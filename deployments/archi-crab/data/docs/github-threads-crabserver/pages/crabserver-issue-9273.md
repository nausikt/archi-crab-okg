# dmwm/CRABServer issue #9273: improve CMSSW release cut for using tokens

State: closed
Opened: 2026-02-17T17:22:55Z
Closed: 2026-02-27T17:25:35Z
URL: https://github.com/dmwm/CRABServer/issues/9273

## Opening post (belforte, 2026-02-17T17:22:55Z)

see
https://github.com/amaltaro/WMCore/blob/c8dbb1db9e48c5b5ee9f1ed1a991d782d627e8e5/src/python/WMCore/BossAir/Plugins/cmssw_no_token_support.json

it is not CMSSW >= 13 as we have now in https://github.com/dmwm/CRABServer/blob/7aca6b02074c205a4d44f68118d14734d8e8a28c/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L243

shall we simply go for CMSSW>=15 ?

## Comment (belforte, 2026-02-17T17:24:23Z)

cfr. also
https://github.com/dmwm/WMCore/pull/12463

## Comment (belforte, 2026-02-21T16:08:53Z)

Stephan Lammel pinged me about activating tokens on all CRAB AP's. So let's start with being on the safe side and modify cut to CMSSW >= 15. We'll  see about "fine tuning" when it becomes needed.

## Comment (belforte, 2026-02-27T17:25:35Z)

closed via #9275
