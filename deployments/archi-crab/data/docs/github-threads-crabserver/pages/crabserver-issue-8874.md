# dmwm/CRABServer issue #8874: TW crashes when killing a task in TAPERECALL

State: closed
Opened: 2025-01-09T13:32:51Z
Closed: 2025-01-13T12:25:40Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8874

## Opening post (belforte, 2025-01-09T13:32:51Z)

more in general, if KILL command is sent before a task is submitted to HTCondor, the schedd name in the DB table is empty (`None`) and
```
> /data/srv/current/lib/python/site-packages/HTCondorLocator.py(190)getScheddObjNew()
-> schedds = coll.query(htcondor.AdTypes.Schedd, f"Name=?={classad.quote(schedd)}",
(Pdb) print(schedd)
None
(Pdb) n
terminate called after throwing an instance of 'std::logic_error'
  what():  basic_string: construction from null is not valid
/data/srv/TaskManager/manage.sh: line 23: 1337248 Aborted                 (core dumped) crab-taskworker --config "${CONFIG}" --logDebug --pdb
```

It is possible that this was not "that fatal" with HTC v1 API, or we would have noticed before. But it is surely better not to try to talk to HTCondor if no submission had been done.

## Comment (belforte, 2025-01-09T14:02:37Z)

it is indeed a problem due to v2 API. in v1 there was an exception, not a crash.
OTOH the crash happens with HTC 23.9.6 wich we use in TW now [1]. In current LTS 24.3 that simply returns an empty string ! [2] and this makes line 190 in HTCondorLocator to return an empty list of schedds [3]. 

I.e. the problem will be gone by using latest HTC.

[1]
```text
crab3@crab-prod-tw02:/data/srv/TaskManager$ python3
Python 3.8.16 (default, May 23 2023, 14:26:40) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import classad
>>> import classad2
>>> classad.version()
'23.9.6'
>>> classad2.version()
'23.9.6'
>>> schedd=None
>>> classad.quote(schedd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Boost.Python.ArgumentError: Python argument types in
    classad.classad.quote(NoneType)
did not match C++ signature:
    quote(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > input)
>>> classad2.quote(schedd)
terminate called after throwing an instance of 'std::logic_error'
  what():  basic_string: construction from null is not valid
Aborted (core dumped)
crab3@crab-prod-tw02:/data/srv/TaskManager$ 
```

[2]
```text
(HTC) LapSB:~$ python3
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import classad
>>> import classad2
>>> classad.version()
'24.3.0'
>>> classad2.version()
'24.3.0'
>>> schedd=None
>>> classad.quote(schedd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Boost.Python.ArgumentError: Python argument types in
    classad.classad.quote(NoneType)
did not match C++ signature:
    quote(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > input)
>>> classad2.quote(schedd)
'""'
>>> 
```

[3]
```
>>> schedd
'""'
>>> schedds = coll.query(htcondor.AdTypes.Schedd, f"Name=?={schedd}", ["Name"])
>>> schedds
[]
>>> 
```

## Comment (belforte, 2025-01-09T14:24:43Z)

For mind sanity I will do both. Rebuild TW with HTC 24.3.0 (immediately) and change code to avoid talking with HTC if there is not schedd name
