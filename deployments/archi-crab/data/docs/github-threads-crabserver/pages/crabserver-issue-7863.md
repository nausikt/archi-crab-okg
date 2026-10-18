# dmwm/CRABServer issue #7863: improve reporting of WebDav failures

State: closed
Opened: 2023-09-05T15:03:11Z
Closed: 2023-11-07T19:53:30Z
Labels: Type: Enhancement, Type: Support, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7863

## Opening post (belforte, 2023-09-05T15:03:11Z)

when destination storage disk quota is full, we now get the very cryptic
```

       1 jobs failed with following error message: (for example, job 33)

            Got recoverable stageout exception:
            Stageout failed with code 1.
            There were 2 failed/killed stageout jobs.
            Failure reasons (per document) follow:
            - ff11f76e2e9c4e4995650140cd007241a928dfaacd12aa723d95b723:
              -----> ASO log start -----
              ['TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull [...CUT...] Full log at https://fts3-cms.cern.ch:8449/fts3/ftsmon/#/job/07771d46-4bd8-11ee-b329-fa163e1db714']
              <----- ASO log finish ----
              The last failure reason is recoverable.
            - c103599795542cbc94307f30d2782506873a71fbdeaa0a5323c5e96f:
              -----> ASO log start -----
              ['3rd push). Last attempt: Transfer failure: Remote side failed with status code 507 [...CUT...] Full log at https://fts3-cms.cern.ch:8449/fts3/ftsmon/#/job/07771d46-4bd8-11ee-b329-fa163e1db714']
              <----- ASO log finish ----
              The last failure reason is recoverable.
```

Note that now FTS query reports both the 3rd pull and 3rp push messages. As Mihai (FTS developer) already pointed out, it would be better if 3rd pull already reported 507 instead of `Copy failed with mode 3rd pull: copy HTTP 400 : Server Error ` (which is in FTSMON log but for some reason not in ASO report).

Now that we use WebDav,  status codes are HTTP ones and [HTTP 507](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/507) is "Insufficient Storage" and so this indicate full disk at destination. We should clearly report this to user with exit code `60323 - User quota exceeded. ` and add a line telling user to check their quota. Such errors are automatically retried, if users act quickly they can make next job submission successful.

## Comment (belforte, 2023-09-05T17:11:50Z)

I was trying to have a first look at where to change and found a bad bug.
All failed transfers in the task https://cmsweb.cern.ch/crabserver/ui/task/230905_015748%3Aciperez_crab_GluGluSpin0ToGammaGamma_W_5p6_M_750_TuneCP2 from where the above example was taken, ended from FTS site with the same reason, correctly fetched by FTS_Transfer.py as clear also in the script log
```
belforte@vocms0144/transfers> grep Failure transfer_inject.log |head -1
2023-09-05 07:29:45,648: Failure reason: TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Remote side failed with status code 507
belforte@vocms0144/transfers> 
```

But looking in transfersdb I see e.g this for the `root` file in one CRAB job
```
tm_transfer_failure_reason | 3rd push). Last attempt: Transfer failure: Remote side failed with status code 507
```
and this for the corresponding `log` file:
```
tm_transfer_failure_reason | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull
```

I think that the problem is that the failure reasons for all files in the same FTS jobid are uploaded to REST in a single call with `subresource='updateTransfers'` as a list. This list is somehow transformed from `['r1','r2',...'rn']` to `r1,r2,...,rn` and then in
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py#L170
it is fed to  WMCore's `makeList` which " Make a python list out of a comma separated list of strings" so  each failure reason ` Failure reason: TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Remote side failed with status code 507` is broken into two parts at the middle `,`

A quick hack could be to remove any `,` from FTS messages.
Better yet to properly manipulate a list of strings all the way from client to Oracle.
Code involved from our side should be
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/ServerUtilities.py#L452
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py#L26
and of course the call to `makeList`

Maybe the error cure is simply to use `validate_strlist` in stead of `validate_string` in e.g.
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py#L46
and do the same in the other cases where this has not hit us yet.. but better be prepared.
Hopefully `validate_strlist` will deal also with a single string.

This deserves an ad hoc issue. But fixing this will surely help to get correct failure reasons to parse in PostJob. WebDav errors are bad enough w/o this extra complexity !

## Comment (belforte, 2023-09-05T17:31:31Z)

:-(
I had added `HTTP 507` already to the list of string-to-look-for-to-assing-stageout-error in
https://github.com/dmwm/WMCore/blame/de110ccf6fc63ef5589b4e871ef4d51d5bce7a25/src/python/WMCore/WMExceptions.py#L325-L327
in https://github.com/dmwm/WMCore/pull/11328

But that does not capture `failed with status code 507` ...  I guess at that time I was looking at output of straight `gfal_copy` from local file to a WebDav server, in `crab checkwrite` context. 3rd party copy messages are ... different.

I'd hate to wait for a new WMCore release for this ! 
Am considering a temporary hack also in
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/ServerUtilities.py#L354-L369

(but the danger is that we never clean this up)

## Comment (belforte, 2023-09-05T17:39:54Z)

given that `STAGEOUT_ERROR` is not used anywhere in WMCore, but only in CRAB, maybe we should simply move 
https://github.com/dmwm/WMCore/blob/de110ccf6fc63ef5589b4e871ef4d51d5bce7a25/src/python/WMCore/WMExceptions.py#L272
and following

into https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/ServerUtilities.py which is the only place where it is used !!!

## Comment (belforte, 2023-11-07T17:29:32Z)

I have moved `STAGEOUT_ERROR` to our repo https://github.com/dmwm/CRABServer/pull/7995 and removed it from WMCore https://github.com/dmwm/WMCore/pull/11787

Next PR will add the missing `failed with status code 507`
