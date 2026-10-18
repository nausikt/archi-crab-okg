# dmwm/CRABServer issue #8372: make REST accept both inputDataset and userInputFiles at same time

State: closed
Opened: 2024-05-02T16:36:43Z
Closed: 2024-05-13T13:06:30Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8372

## Opening post (belforte, 2024-05-02T16:36:43Z)

needed for #8371 and https://github.com/dmwm/CRABClient/issues/5308

currently when bypassing the client check I get a server error
```text
[02/May/2024:18:35:22]      File "/data/srv/HG2401b-28ec7022d805533f1438590b675b0d94/sw.crab_master/slc7_amd64_gcc630/cms/crabserver/v3.240219-3375dda1822c21b51791e8bff69c4393/lib/python3.8/site-packages/CRABInterface/RESTUserWorkflow.py", line 384, in validate - Podname=crabserver-7c98c88bd7-bslgp Type=cherrypylog
[02/May/2024:18:35:22]        if inputDataFromRucio: - Podname=crabserver-7c98c88bd7-bslgp Type=cherrypylog
[02/May/2024:18:35:22]    UnboundLocalError: local variable 'inputDataFromRucio' referenced before assignment - Podname=crabserver-7c98c88bd7-bslgp Type=cherrypylog

```

## Comment (belforte, 2024-05-02T16:40:44Z)

problem is here
https://github.com/dmwm/CRABServer/blob/b959b782d96fd7d0ca4e163475633c0492ce7c05/src/python/CRABInterface/RESTUserWorkflow.py#L364-L365

iin this case `inputDataFromRucio` is not defined

## Comment (belforte, 2024-05-10T17:12:28Z)

Validation of the proper combination, correct LFN's etc. will have to be done in TaskWorker. REST's RX-based validation does nto allow to do better than accept any string for `userInputFiles`

## Comment (belforte, 2024-05-11T16:18:12Z)

now submittion with `userInputFiles` only fails because modified code tries to validate `inputDataset`
```
The server answered with an error.
Server answered with: Invalid input parameter
Reason is: Incorrect 'Data.inputDataset' parameter <class 'str'>
```

## Comment (belforte, 2024-05-12T21:33:19Z)

The reasong is that `optional=True` does not work for `inputdata` in e.g.
https://github.com/dmwm/CRABServer/blob/19b179e7708b84731c11df9948039211852de1a1/src/python/CRABInterface/RESTUserWorkflow.py#L375
because the in cases like this (or fpr privateMC) the client puts in the URL "nothing" `&inputdata=&` but the REST codes sees a empty string `''` as value, not `None` or no keywork, so the `optional` in the validation does not do anything https://github.com/dmwm/WMCore/blob/e4628ce9ab25f5015b71197a42eb09d630286318/src/python/WMCore/REST/Validation.py#L79
```python
def _validate_one(argname, param, safe, checker, optional, *args):
    val = param.kwargs.get(argname, None)
    if optional and val == None:
        safe.kwargs[argname] = None
    else:
        safe.kwargs[argname] = checker(argname, val, *args)
        del param.kwargs[argname]
```

I am fixing the REST now. But I think the Client should simply omit the `inputdata` parame in the URL instead of specifyiin w/o a value. But I suspect that there are palces in the code where that `''` is used :-(  Maybe there was a conscious decision to have an empty string in Oracle instead of `NULL`

## Comment (belforte, 2024-05-12T21:47:10Z)

I could try to replace `''` with `None` in this line https://github.com/dmwm/CRABClient/blob/d4b4151f668ba23cb069569e9613c83776630f6b/src/python/CRABClient/ClientMapping.py#L24
```
                  'inputdata'      : {'default': '',         'config': ['Data.inputDataset'],               'type': 'StringType',  'required': False},
```

## Comment (belforte, 2024-05-13T13:06:30Z)

closed via #8399
