# dmwm/CRABServer issue #9216: CRAB tape recall uses wrong list of destination sites

State: closed
Opened: 2025-10-15T13:48:03Z
Closed: 2026-03-31T15:19:47Z
Labels: Type: Bug, Status: On Hold, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9216

## Opening post (belforte, 2025-10-15T13:48:03Z)

from https://its.cern.ch/jira/browse/CMSTRANSF-1241
it appears that CRAB still uses full list of T2's for tape recall, e.g. in
https://cms-rucio-webui.cern.ch/rule?rule_id=ecdc8b5d4cf641c6950ce5ca39569eb0
while it should be using only reliable ones.

## Comment (belforte, 2025-10-15T13:49:12Z)

the change to use only reliable sites was done back in May via https://github.com/dmwm/CRABServer/issues/8356

No that was in 2024 and was a "tentative approximation by me".  There is list by Hasan now.. I still have to find the correct issue .

## Comment (belforte, 2025-10-15T14:00:18Z)

I can't find an issue about this. So have asked Hasan in the JIRA mentioned at the top which RSE Expression to use.

## Comment (belforte, 2025-10-15T14:43:37Z)

OK. I was mixing memories :-(
Here's Hasan's reply

> Hi [Stefano Belforte](https://its.cern.ch/jira/secure/ViewProfile.jspa?name=belforte) the RSE expression we requested CRAB to use for only MINIAOD and MINIAODSIM is "keep_miniaod=True" and you implemented this. Details: https://its.cern.ch/jira/browse/CMSTRANSF-1199 This is only for MINIAOD* and I don't recall any other RSE expression that we suggested CRAB to use.

## Comment (belforte, 2025-10-15T14:57:20Z)

so it is clear that we want to do better than this, but do not know how

RSE Expression:             T1_DE_KIT_Disk|T1_ES_PIC_Disk|T1_FR_CCIN2P3_Disk|T1_IT_CNAF_Disk|T1_PL_NCBJ_Disk|T1_UK_RAL_Disk|T2_BE_IIHE|T2_BE_UCL|T2_CH_CERN|T2_CH_CSCS|T2_DE_DESY|T2_DE_RWTH|T2_EE_Estonia|T2_ES_CIEMAT|T2_FI_HIP|T2_FR_GRIF|T2_FR_GRIF_IRFU|T2_FR_GRIF_LLR|T2_FR_IPHC|T2_HU_Budapest|T2_IT_Bari|T2_IT_Legnaro|T2_IT_Pisa|T2_IT_Rome|T2_KR_KISTI|T2_UK_London_IC|T2_UK_SGrid_RALPP

## Comment (belforte, 2025-10-15T15:01:57Z)

On HOLD waiting for suggestion from DM or new ideas

## Comment (belforte, 2026-03-31T15:19:43Z)

there is no point in keeping this open. All in all things are working. If at some point DM gives us a list of sites to use, it will be easy to implement it.
