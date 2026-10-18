# dmwm/CRABClient issue #5394: undefined 'failingTaskPublish' in `recover`

State: closed
Opened: 2025-06-17T07:20:59Z
Closed: 2025-06-19T14:43:12Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5394

## Opening post (belforte, 2025-06-17T07:20:59Z)

```
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02894/share/cms/crab-dev/v3.250522.00/bin/crab.py", line 142, in __call__
    returnDict = self.cmd()
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02894/share/cms/crab-dev/v3.250522.00/lib/CRABClient/Commands/recover.py", line 107, in __call__
    retval = self.stepBuildLumiRecoveryInfo(report)
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02894/share/cms/crab-dev/v3.250522.00/lib/CRABClient/Commands/recover.py", line 527, in stepBuildLumiRecoveryInfo
    if failingTaskPublish == "T" and self.options.__dict__["strategy"] == "notPublished":
NameError: name 'failingTaskPublish' is not defined
ERROR 2025-06-16 21:35:43.348 UTC: 	 ERROR: NameError: name 'failingTaskPublish' is not defined
```

due to
https://github.com/dmwm/CRABClient/blob/64b0373ce7912719936fdea7c37fdbe7d831b962/src/python/CRABClient/Commands/recover.py#L518-L527

## Comment (belforte, 2025-06-17T07:25:04Z)

`pylint` was flagging it
```console
LapSB:CRABClient$ pylint src/python/CRABClient/Commands/recover.py |grep undef
src/python/CRABClient/Commands/recover.py:527:11: E0602: Undefined variable 'failingTaskPublish' (undefined-variable)
src/python/CRABClient/Commands/recover.py:543:15: E0602: Undefined variable 'failingTaskPublish' (undefined-variable)
```

we have to do better in the "ignore pylint for CRABClient since it has to be py2 compatible"  :-(

FIne to ignore Warning, but at least Errors should be addressed !

## Comment (belforte, 2025-06-17T07:34:29Z)

I am surprised that it was not reported yet. Nor found in our tests.
Bug was introduced in https://github.com/dmwm/CRABClient/commit/8b8da2a40b2ee3bd8a9df03613ff291608262b56 by me :-(

## Comment (belforte, 2025-06-17T07:35:56Z)

Anyhow I'll fix it now because it blocks my tests with ASO-Rucio
