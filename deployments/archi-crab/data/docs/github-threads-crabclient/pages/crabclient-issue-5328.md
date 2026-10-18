# dmwm/CRABClient issue #5328: crab report wrongly reports lumis as both failed and successful for Autom.Split

State: closed
Opened: 2024-07-15T07:57:56Z
Closed: 2025-07-07T12:50:03Z
Labels: bug, Done
URL: https://github.com/dmwm/CRABClient/issues/5328

## Opening post (belforte, 2024-07-15T07:57:56Z)

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

## Comment (belforte, 2024-07-15T08:22:02Z)

@mapellidario  can you tell me how to reproduce the list above ? I can not  find a `failedLumis.json` file what `crab report` writed

## Comment (mapellidario, 2024-07-15T08:25:23Z)

you need to use the `--recovery=failed` option, which will not produce any output unless you apply the PR that I submitted on Friday

## Comment (belforte, 2024-07-15T08:26:36Z)

but I can't find the code which writes that file !

## Comment (belforte, 2024-07-15T08:27:31Z)

anyhow the output is there

## Comment (belforte, 2024-07-15T08:30:00Z)

ok. found

## Comment (belforte, 2024-07-15T08:37:14Z)

this loop should be modified to only look at tail jobs when automatic splitting is used. Even then, when some tail fail, the input will be reprocessed in additional tail subdags, We need to somehow backtrace the job number hierarchy...
https://github.com/dmwm/CRABClient/blob/05e977bb2acea5a465df9ea06f22d8e2fd8cbd26/src/python/CRABClient/Commands/report.py#L189-L198

I start to wonder if we should rather remove `--failed` option !

## Comment (belforte, 2024-07-15T08:38:01Z)

is there any bad side effect from using simply toProcess - Processed ?

## Comment (mapellidario, 2024-07-15T09:34:07Z)

> I start to wonder if we should rather remove --failed option !

After spending a good 15min thinking about how to make this option work for automatic splitting, I came to the very same conclusion. If 2 people out of the 2 who thought about this came to the same conclusion i guess we have enough quorum to proceed! :)

And if we wonder about how impact on our users: well, it was broken, so nobody really could have ever used this feature!

> is there any bad side effect from using simply toProcess - Processed ?

no, there is not. And if I understand correctly, this is exactly what the default crab report option does

https://github.com/dmwm/CRABClient/blob/65a8e7ac63e2328445e1d467c37016a8efab3e08/src/python/CRABClient/Commands/report.py#L171-L172

## Comment (belforte, 2024-07-15T13:04:12Z)

At the very least we need to deprecate `--failed` in case of automatic splitting. In a way, when there's a reliable list of failed jobs, the ability to directly show what lumis were to be processed in those jobs may be good.
POssibly this is also less work.

## Comment (belforte, 2025-07-04T12:55:09Z)

atm `crab report` does not retrieve the info from DB about the splitting algorithm. It is not among what `status` retrieves. Need to add another call to REST

a more "efficient" option would be to add `split_algo` to `report2` output, the `ID_sql` query in there already retrieves, but it is not  propagated to the client.
https://github.com/dmwm/CRABServer/blob/4d340452ef43935a479b6e4c27a38a3e0d1b1a2a/src/python/CRABInterface/HTCondorDataWorkflow.py#L69-L78
