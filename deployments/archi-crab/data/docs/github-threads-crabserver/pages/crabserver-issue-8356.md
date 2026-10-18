# dmwm/CRABServer issue #8356: use a list or reliable sites for tape recall

State: closed
Opened: 2024-04-24T22:15:39Z
Closed: 2024-05-08T11:07:52Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8356

## Opening post (belforte, 2024-04-24T22:15:39Z)

(no text)

## Comment (belforte, 2024-04-24T22:16:07Z)

do it now, before I forget

## Comment (belforte, 2024-04-24T22:23:05Z)

current list for Europe is:
```
Will use rseExpression = T1_DE_KIT_Disk|T1_ES_PIC_Disk|T1_FR_CCIN2P3_Disk|T1_IT_CNAF_Disk|T1_UK_RAL_Disk|T2_BE_IIHE|T2_BE_UCL|T2_CH_CERN|T2_CH_CSCS|T2_DE_DESY|T2_DE_RWTH|T2_EE_Estonia|T2_ES_CIEMAT|T2_FI_HIP|T2_FR_GRIF|T2_FR_GRIF_IRFU|T2_FR_GRIF_LLR|T2_FR_IPHC|T2_HU_Budapest|T2_IN_TIFR|T2_IT_Bari|T2_IT_Legnaro|T2_IT_Pisa|T2_IT_Rome|T2_KR_KISTI|T2_PL_Swierk|T2_UK_London_IC|T2_UK_SGrid_RALPP
```
not too bad (current code picks sites with > 1PB disk, which cuts away most edge cases) but e.g. should remove TIFR and Swierk unitl they get good

and for FNAL we have all US sites plus Brazil, which should go away
