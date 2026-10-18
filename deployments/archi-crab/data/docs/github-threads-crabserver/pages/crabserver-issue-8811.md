# dmwm/CRABServer issue #8811: checkS3Object fails on SL7 and breask CRABClient

State: closed
Opened: 2024-11-25T10:38:23Z
Closed: 2024-11-25T21:47:08Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/8811

## Opening post (belforte, 2024-11-25T10:38:23Z)

the change introduced in https://github.com/dmwm/CRABServer/commit/256760aaeda8b8929ab92f56bb6b5b59b6f0c9c7
was not sufficiently tested :-(

It breaks CRABClient for SL7 because `wget` in there does not support the `--method` option
```console
belforte@lxplus940/TC3> cmssw-el7 -- "wget -Sq -O /dev/null --method=HEAD http://a.b.c"
wget: unrecognized option '--method=HEAD'
```
so we need to replace

https://github.com/dmwm/CRABServer/blob/7d13f7d51d9bdd5c65dafa6f7a2a9961c86d001e/src/python/ServerUtilities.py#L750-L751

with a call to `curl`

## Comment (belforte, 2024-11-25T21:42:29Z)

it took very long to test, but eventually one more change is needed for python2 compatibility.

https://github.com/dmwm/CRABServer/blob/362aaee9c7536bace2657d93b53296ad944a2fb6/src/python/ServerUtilities.py#L753-L757

using context manager here results in Exception `AttributeError: '__exit__'` 
Need to stick with old-fashioned 
```
downloadProcess = subprocess.Popen(...)
```
