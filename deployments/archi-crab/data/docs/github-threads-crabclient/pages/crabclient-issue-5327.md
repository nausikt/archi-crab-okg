# dmwm/CRABClient issue #5327: crab report wrongly reports lumis as both failed and successful for Autom.Split

State: closed
Opened: 2024-07-15T07:37:54Z
Closed: 2024-07-15T09:36:44Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5327

## Opening post (belforte, 2024-07-15T07:37:54Z)

ref: https://cms-talk.web.cern.ch/t/command-crab-report-not-generate-filed-files/43487

Report from @mapellidario :

User submitted task [240704_211221:matheus_crab_EGammaEXO_Run2018A_20240704_231147](https://cmsweb.cern.ch/crabserver/ui/task/240704_211221%3Amatheus_crab_EGammaEXO_Run2018A_20240704_231147) with Automatic splitting, which means that if a job at step one fails,
the lumisections that it did not process will be processed by a later stage.
This means that it is possible for a lumisection to have been assigned to a job that failed,
and then re-assigned to a job at a later stage that was successful.
In particular, the following lumisections [2] of run 316457 are both in
processedLumis.json and failedLumis.json, while they are not in notFinishedLumis.json.

[2]

{516, 12, 14, 30, 32, 66, 86, 601, 114, 116, 117, 1146, 1147, 129, 1155, 1156, 1159, 136, 1161, 1167, 656, 1169, 661, 662, 663, 664, 1177, 1180, 1181, 1185, 1190, 1192, 1194, 1195, 1196, 1197, 1198, 1199, 1207, 185, 1209, 723, 724, 225, 226, 228, 229, 232, 233, 234, 242, 271, 276, 280, 281, 283, 288, 294, 299, 307, 309, 823, 312, 824, 316, 326, 329, 330, 331, 332, 337, 341, 342, 351, 355, 356, 359, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 380, 394, 395, 396, 397, 398, 400, 402, 403, 407, 409, 410, 412, 416, 425, 429, 440, 448, 489, 492, 497, 499, 503, 504}

## Comment (mapellidario, 2024-07-15T09:36:44Z)

I will close this as duplicate of #5328

## Comment (belforte, 2024-07-15T12:52:36Z)

thanks Dario. I had come browser issue...
