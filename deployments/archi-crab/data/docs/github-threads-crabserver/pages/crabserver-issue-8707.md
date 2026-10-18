# dmwm/CRABServer issue #8707: add a status.sh to containers

State: closed
Opened: 2024-09-20T14:48:30Z
Closed: 2025-04-16T16:43:19Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8707

## Opening post (belforte, 2024-09-20T14:48:30Z)

e.g. on REST we have
```console
crab3@crabserver-644cb69d77-n7sqw:/data$ ./manage.py status
crabserver is RUNNING, PID 67
crab3@crabserver-644cb69d77-n7sqw:/data$ 
```
which by the way is broken, since in that case at least proc 67 is gone and the correct one is 68

but in TW
```console
crab3@crab-dev-tw01:/data/srv/TaskManager$ ./manage.py status
Error: Not implemented.
crab3@crab-dev-tw01:/data/srv/TaskManager$ 
```

We'd like status to not only indicate if process is running, but also whether it run code from the container `/data/srv/current/lib...` or from the local GithHub repository `/data/repos/....` 

that can be done with this trick from @novicecpp 

```console
crab3@crab-dev-tw01:/data/srv/TaskManager$ cat /proc/18/environ |tr '\0' '\n'|grep PYTHONPATH
PYTHONPATH=/data/srv/current/lib/python/site-packages/:
crab3@crab-dev-tw01:/data/srv/TaskManager$ 
```

`./status.sh` could also print the version number ( tag name)

## Comment (belforte, 2024-10-11T16:50:57Z)

#8737 will fix main requirement here, only thing to add is version number, just a convenience...

## Comment (belforte, 2025-04-16T16:43:19Z)

version number is there too now via #9015
