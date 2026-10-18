# dmwm/CRABServer issue #7799: input data locking fails in preprod v3.230803

State: closed
Opened: 2023-08-06T22:10:47Z
Closed: 2023-08-07T15:14:53Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7799

## Opening post (belforte, 2023-08-06T22:10:47Z)

```
2023-08-06 23:17:29,714:ERROR:DBSDataDiscovery:Fatal exception in lockData:
name 'config' is not defined
Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py", line 430, in executeInternal
    locker = RucioAction(config=config, crabserver=self.crabserver,
NameError: name 'config' is not defined
2023-08-06 23:17:29,715:INFO:DBSDataDiscovery:Locking of input data failed. Details in TaskWorker log. Submit anyhow
```

## Comment (belforte, 2023-08-07T09:02:38Z)

same bug affects tape recall. I do not know why I did not see this when testing :-(

## Comment (belforte, 2023-08-07T09:20:44Z)

test:
- [x] input dataset lock
- [x] tape recall

## Comment (belforte, 2023-08-07T09:56:37Z)

hmmm.. another bug
```
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py", line 338, in executeInternal
    self.requestTapeRecall(dataToRecall=dataToRecall, sizeToRecall=totalSizeBytes,
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py", line 467, in requestTapeRecall
    recaller.recallData(dataToRecall=dataToRecall, sizeToRecall=sizeToRecall,
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/RucioActions.py", line 229, in recallData
    self.setTaskToTapeRecall(ruleId=ruleId, msg=msg)
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/RucioActions.py", line 165, in setTaskToTapeRecall
    self.uploadWarning(msg, self.userproxy, self.taskName)
AttributeError: 'RucioAction' object has no attribute 'uploadWarning'
```

## Comment (belforte, 2023-08-07T12:21:54Z)

tape recall and input lock now works in preprod using https://github.com/belforte/CRABServer/tree/fix-7799

## Comment (novicecpp, 2023-08-07T14:48:24Z)

I am a bit surprise that `NameError` exception is not catch by `pylint`. For `uploadWarning`, it is understandable because it hidden in `self` which `pylint` does not design to detect that.

I think static type checker tools like `mypy/pyright/pyre` can detect this kind of bug but it is yet-another-3rdparty-software we need to maintain. (I use [pyright](https://github.com/microsoft/pyright) in my editor and it work quite well when I develop Rucio ASO, especially methods and variables hidden in `self` in [ASO/Rucio/Transfer.py](https://github.com/dmwm/CRABServer/blob/8ff0d6f15fb1f15a6996149c6b181d379ce2c191/src/python/ASO/Rucio/Transfer.py)).

## Comment (mapellidario, 2023-08-07T15:17:27Z)

I use vscode with pylance (which includes the functionality from pyright). It does not detect the NameError because it thinks that `config` is defined when running DBSDataDiscovery.py as main at https://github.com/dmwm/CRABServer/blob/272175fa1c946e96a0428fa3e1893ea1f6b0f57a/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L494 . 

So yeah, a tale of how static code analysis can only go so far
