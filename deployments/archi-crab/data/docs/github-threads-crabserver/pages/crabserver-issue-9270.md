# dmwm/CRABServer issue #9270: add in-memory caching for high-prio users list

State: closed
Opened: 2026-01-30T11:18:20Z
Closed: 2026-02-20T17:33:08Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/9270

## Opening post (belforte, 2026-01-30T11:18:20Z)

With reference to https://github.com/dmwm/CRABServer/issues/9224#issuecomment-3823171653 and new `TaskWorker/WorkerUtilities.getHighPrioUsersFromCRIC` possibly combine with https://github.com/dmwm/CRABServer/blob/bad7564a9705d2da18d31e21353f6a1482bd417c/src/python/CMSGroupMapper.py#L116 
so that we have a single "user to group" map as a  persistent TW object, instead of using globals.
That way  we also bring CMSGroupMapper inside TW code tree with proper user of logging etc.

## Comment (belforte, 2026-01-30T11:25:19Z)

I am waiting for #9269 to be merged first. In case there's a need for changes which may affect this

## Comment (belforte, 2026-02-02T11:27:48Z)

I tried at length to use `global` variables for the in-memory cache along the lines of https://github.com/dmwm/CRABServer/blob/102cb1a496385b5b84f4b47ec6001eb768db933c/src/python/CMSGroupMapper.py#L7-L23
But could not make it to work across TW Action instantiations.
Indeed after adding print statement, I found that it does not work for the original either [1]

There is something which I fail to understand which makes it work if I run the sequential worker (with `pdb`), i.e. everything in a single process, but when I let slave run as a separate process, expire time for the cache is always reset to 0 for a new task.

[1]
```
crab3@crab-dev-tw01:/data/srv/TaskManager$ cat logs/nohup.out |grep ===
=====================================================
 ==== in map_user_to_group expire time is 0
 ==== Refresh cache ! 
 ==== users cached at 2026-02-02 11:35:14.313393
 ==== new expire time 11:50:14
=====================================================
=====================================================
 ==== in map_user_to_group expire time is 0
 ==== Refresh cache ! 
 ==== users cached at 2026-02-02 11:48:18.190691
 ==== new expire time 12:03:18
=====================================================
=====================================================
 ==== in map_user_to_group expire time is 0
 ==== Refresh cache ! 
 ==== users cached at 2026-02-02 11:49:18.406824
 ==== new expire time 12:04:18
=====================================================
crab3@crab-dev-tw01:/data/srv/TaskManager$ 
```

Maybe it has something to do with the fact that every TW action is now executed in a child process ?

https://github.com/dmwm/CRABServer/blob/102cb1a496385b5b84f4b47ec6001eb768db933c/src/python/TaskWorker/Worker.py#L101-L108

That makes me doubtful that a simple solution can be found. Maybe a "caching class" object could be added to WORKER_CONFIG object and passed around that way ?

Seems pretty ugly though, only to avoid making a light HTTP query to CRIC for every submit. Which will never be kHz !

I will ask for advice from my collaborators !

## Comment (belforte, 2026-02-20T17:33:08Z)

we have decided to write files with the info in the host via a crontab, so no caching inside container is needed. Info will be read from disk file at every `submit`
