# dmwm/CRABServer issue #7864: FTS failure reasons are broken into pieces in transfersdb

State: closed
Opened: 2023-09-05T17:12:39Z
Closed: 2023-11-08T13:18:19Z
Labels: Type: Bug, Type: Question, Type: Support, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7864

## Opening post (belforte, 2023-09-05T17:12:39Z)

as described in https://github.com/dmwm/CRABServer/issues/7863#issuecomment-1706999574

## Comment (belforte, 2023-09-05T17:14:20Z)

@mapellidario @novicecpp I would be grateful if one of you could volunteer to pick up this. Proper handling of strings in python is a a land where I  am not comfortable.

## Comment (belforte, 2023-09-05T17:14:52Z)

yeah... we should move detailed description from https://github.com/dmwm/CRABServer/issues/7863#issuecomment-1706999574 to here and leave there only a summary

## Comment (belforte, 2023-11-02T15:34:00Z)

this is now needed so that I can progress with #7863 . CHanging priority to TOP and assign to me.

## Comment (belforte, 2023-11-02T15:35:58Z)

detailed description:

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
https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py#L174
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

## Comment (belforte, 2023-11-07T10:56:13Z)

hmm... not reallty. I tested code with pdb and
`params.kwargs['list_of_failure_reason']="['r1, R1', 'r2, R2', 'r3, R3']"` is turned by `validate_str` to 
```
(Pdb) mys.kwargs
{'subresource': 'updateTransfers', 'list_of_failure_reason': "['r1, R1', 'r2, R2', 'r3, R3']"}
```
while `validate_strlist` yields
```
(Pdb) mys2.kwargs
{'subresource': 'updateTransfers', 'list_of_failure_reason': ["['r1, R1', 'r2, R2', 'r3, R3']"]}
```
Which is even worse to hanlde !
Now the problem is to turn  the string 
```
"['r1, R1', 'r2, R2', 'r3, R3']"
```
into the python list `['r1, R1', 'r2, R2', 'r3, R3']` while `makelist` output is

```
(Pdb) mys.kwargs
{'subresource': 'updateTransfers', 'list_of_failure_reason': "['r1, R1', 'r2, R2', 'r3, R3']"}
(Pdb) reasons = makeList(mys.kwargs['list_of_failure_reason'])
(Pdb) reasons
['r1', 'R1', 'r2', 'R2', 'r3', 'R3']
(Pdb) 
``` 

Could this be a bug in `makelist` ?

## Comment (belforte, 2023-11-07T11:15:49Z)

The problem seems to be that when `makelist` splits its argument at each `,` it handles quotes as string characters, does not read `'r1,r2'` as a substring to be kept separated, indeed it strips away all `'` and `"` chars.

The fact is that due to the way our API's are constructed (?) we are simply dealing with the  "stream to string" representation of a python list and a crude `eval` would do !
```
# reasons w/o commas
(Pdb) safe.kwargs['list_of_failure_reason']
"['r1 R1', 'r2 R2', 'r3 R3']"
(Pdb) eval(safe.kwargs['list_of_failure_reason'])
['r1 R1', 'r2 R2', 'r3 R3']

# reasons with commas
(Pdb) mys.kwargs['list_of_failure_reason']
"['r1, R1', 'r2, R2', 'r3, R3']"
(Pdb) eval(mys.kwargs['list_of_failure_reason'])
['r1, R1', 'r2, R2', 'r3, R3']
(Pdb) 
```

Maybe a side effect of not using a well defined format for passing args, like e.g. JSON. We handle everything as a single string and this has "limits".

## Comment (belforte, 2023-11-07T11:18:12Z)

The problem seems to be that when `makelist` splits its argument at each `,` it handles quotes as string characters, does not read `'r1,r2'` as a substring to be kept separated, indeed it strips away all `'` and `"` chars.

The fact is that due to the way our API's are constructed (?) we are simply dealing with the  "stream to string" representation of a python list and a crude `eval` would do !
```
# reasons w/o commas
(Pdb) safe.kwargs['list_of_failure_reason']
"['r1 R1', 'r2 R2', 'r3 R3']"
(Pdb) eval(safe.kwargs['list_of_failure_reason'])
['r1 R1', 'r2 R2', 'r3 R3']

# reasons with commas
(Pdb) mys.kwargs['list_of_failure_reason']
"['r1, R1', 'r2, R2', 'r3, R3']"
(Pdb) eval(mys.kwargs['list_of_failure_reason'])
['r1, R1', 'r2, R2', 'r3, R3']
(Pdb) 
```

Maybe a side effect of not using a well defined format for passing args, like e.g. JSON. We handle everything as a single string and this has "limits".

## Comment (belforte, 2023-11-07T11:31:35Z)

in a way the problem is that the REST code was really meant to deal with lists of the form "a,b,c,d" but e.g. in FTS_Transfers.py we send real python lists, even if urlencoded.

## Comment (belforte, 2023-11-07T11:34:30Z)

At this point I am reluctant to change https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py introducing calls to `eval`, in a way it should be done everywhere, not just for `list_of_failure_reason`.

I am afraid that the safest fix is to replace possible commas `,` in FTS message with e.g. a dot ` .`

## Comment (novicecpp, 2023-11-07T15:20:41Z)

Hi @belforte, sorry for joining late.

Are we supposed to use `encodeRequest(data, listParams=['list_of_ids', 'list_of_failure_reason', 'list_of_...'])` on client side and `validate_strlist()` on server side?
Is there any reason why we stick with the current code and do `makeList()` on server side later?

-------------

I have tested with my custom code, and it deserializes on the server correctly.
Server side, change [line 46](https://github.com/dmwm/CRABServer/blob/e7c14e3115c53c5542bb0884d618a45397f5886c/src/python/CRABInterface/RESTFileTransfers.py#L46) to 
```python
validate_strlist("list_of_failure_reason", param, safe, RX_ANYTHING)
```
On client side, I just mock data from Rucio ASO ([example](https://codimd.web.cern.ch/s/0ogNGMzM9#)) and sent to server with 
```python
encodeRequest(data, listParams=['list_of_failure_reason'])
```
Here is pdb output from REST:
```
(Pdb) pp kwargs['list_of_failure_reason']
['TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: '
 'Transfer failure: Remote side failed with status code 507',
 'TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: '
 'Transfer failure: Remote side failed with status code 507',
 'TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: '
 'Transfer failure: Remote side failed with status code 507',
 ...
```

## Comment (belforte, 2023-11-07T16:13:08Z)

thanks @novicecpp . Whilt it will take me a bit to digest, it looks like you are correct.
There's a lot of confusion and inconsistency in how thow calls have been coded and used around. In a way, if we go down the path which you indicate, we should get rid of that `makeList`  everywhere in RESTFileTrasnfers.py and use `encodeRequest(data, listParams=)` instead in  FTS_Transfers.py . Doing this only for one argument will make it too much confusing. IIAMC there's only another place where `makeList` is used in the code base, but look sOK to me (from SQL output to python list).

In the end the answer to "Is there any reason why" is two-fold:
1. fear
2. lazyness

:-)

## Comment (belforte, 2023-11-07T16:22:50Z)

shall we open a GH issue of CleanUp category about this ? fully testing a modified FTS_Transfer is a bit of a pain.
@novicecpp do you agree ? If so I will close this and open the new one at low priority

## Comment (belforte, 2023-11-08T11:23:34Z)

we agree on that. Let's do.
