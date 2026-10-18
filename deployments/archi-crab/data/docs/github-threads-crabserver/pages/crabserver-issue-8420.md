# dmwm/CRABServer issue #8420: TW fails to catch and report crashes during submission to HTCondor

State: closed
Opened: 2024-05-20T20:59:00Z
Closed: 2024-05-23T13:45:56Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8420

## Opening post (belforte, 2024-05-20T20:59:00Z)

see e.g.
https://s3.cern.ch/crabcache_prod/piperov/240517_215114%3Apiperov_crab_SONIC_MiniAOD_CRAB_testPurdue807_1x4900-1000j/twlog?AWSAccessKeyId=e57ff634b5334df9819ae3f956de5ca6&Signature=xK9VdrPWqew0wCVP2IQ3l5wPkGM%3D&Expires=1718830467

which ends with
```
2024-05-17 23:55:00,612:INFO:DagmanSubmitter:User piperov mapped to local groups {'T3_US_FNALLPC', 'T2_US_Purdue', '/cms'}.
2024-05-17 23:55:00,612:DEBUG:DagmanSubmitter:Finally submitting to the schedd
```

the slave died at that time
```
[crab3@crab-prod-tw01 processes]$ ls -l proc.c3id_5.pid_54.txt
-rw-r--r--. 1 crab3 crab3 9874340 May 17 23:55 proc.c3id_5.pid_54.txt
[crab3@crab-prod-tw01 processes]$ tail -2  proc.c3id_5.pid_54.txt
2024-05-17 23:55:00,612:INFO:DagmanSubmitter:User piperov mapped to local groups {'T3_US_FNALLPC', 'T2_US_Purdue', '/cms'}.
2024-05-17 23:55:00,612:DEBUG:DagmanSubmitter:Finally submitting to the schedd
[crab3@crab-prod-tw01 processes]$ 
```
and the task was left in QUEUED forever
https://cmsweb.cern.ch/crabserver/ui/task/240517_215114%3Apiperov_crab_SONIC_MiniAOD_CRAB_testPurdue807_1x4900-1000j

Task stuck in QUEUED is bad, and crashed slave is worse !

The submission failure was due to a bad extraJDL argument on user side

in the Task Info tab of the UI
```
tm_extrajdl	['Requirements = regexp("bell",Machine)==False']
```
in the user config (as privately reported by @kpedro88 ) :
```python
config.Debug.extraJDL = ['Requirements = regexp("bell",Machine)==False']
```

## Comment (mapellidario, 2024-05-21T13:15:17Z)

I manually set the task status of [1] to "submitfailed" in the DB

[1]

- `240517_215114:piperov_crab_SONIC_MiniAOD_CRAB_testPurdue807_1x4900-1000j`
- `240517_214911:piperov_crab_SONIC_MiniAOD_CRAB_testPurdue806_1x4900-100j`

## Comment (belforte, 2024-05-21T14:46:57Z)

I am testing adding this to my task
```
config.Debug.extraJDL = ['Requirements = regexp("bell",Machine)==False']
```
interestingly, in DagmanSubmitter, just before calling ` schedd.submit(dagAd,... ` the `dagAd` object contain both these
```
(Pdb) dagAd['Requirements']
true || false
(Pdb) dagAd['Requirements ']
' regexp("bell",Machine)==False'
(Pdb) 
```
The former comes from https://github.com/dmwm/CRABServer/blob/fa964382216c9ecac345927afc8ff6b02eee0cb2/src/python/TaskWorker/Actions/DagmanSubmitter.py#L490
and I have no idea what it is supposed to mean, but since Brian B. put it there in the original version, it must be needed or at least not harm. Maybe a way to say "no requirements from here", since anyhow schedd will add requirements based on site, memory, cores...

The latter appears to contain an extra space and extra single quotes.
Indeed if I do `print(dagAd)`  I get:
```
[...]
        CRAB_UserHN = "belforte"; 
        'Requirements ' = " regexp(\"bell\",Machine)==False"; 
        CRAB_UserRole = undefined; 
[...]
        CRAB_AsyncDest = "T2_CH_CERN"; 
        Requirements = true || false; 
        CRAB_UserDN = "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=belforte/CN=373708/CN=Stefano Belforte"; 
[...]
```

```

## Comment (belforte, 2024-05-21T14:53:35Z)

and when I execute the submit line I get
```
-> clusterId = schedd.submit(dagAd, 1, True, resultAds)
(Pdb) n
terminate called after throwing an instance of 'boost::python::error_already_set'
./start.sh: line 65: 24746 Aborted                 (core dumped) python3 -m pdb ${COMMAND_DIR}/SequentialWorker.py ${CONFIG} --logDebug
```

which IMHO suggests that setting `Requirements` twice triggers the `error_already_set` in the C++ side of the HTCondor API which ends in abort and core dump, not a python exception.

I do not know if there's a way to catch that.

## Comment (belforte, 2024-05-21T15:11:17Z)

hmm.. not really. HTCondor doc clearly states that if multiple `Requirementa` classAd's are present in the submission, only the last one is used. So the `boost::python::error_already_set` must be something else

I am also quite puzzled that single quotes made it to the classAd value, the code which handles the extraJDL is in here
https://github.com/dmwm/CRABServer/blob/fa964382216c9ecac345927afc8ff6b02eee0cb2/src/python/TaskWorker/Actions/DagmanSubmitter.py#L89-L105

## Comment (belforte, 2024-05-21T16:45:50Z)

If I remove the extra spaces around the `=` in the `extraJDL` things "work" in the sense that CRAB overrides the user attempt to redefine Requirements with "our" ones, as by design, and there is no error.
This can be achieved stripping start/end spaces in `adName` and `adVal` :
https://github.com/dmwm/CRABServer/blob/fa964382216c9ecac345927afc8ff6b02eee0cb2/src/python/TaskWorker/Actions/DagmanSubmitter.py#L100
which makes the code a bit more robust.

Still I do not know how to possibly catch the boost error :-(

Do we need to resurrect "calling schedd.submit in a forked subprocess" ?

## Comment (belforte, 2024-05-21T16:47:12Z)

I have no problem with the user's attempt to set Requirements to be ignored, documentation clearly states that `extraJDL` is for experts only. In this case people who tried to use it did not know how glideinWms works.

## Comment (belforte, 2024-05-22T08:31:35Z)

Indeed even the simple `config.Debug.extraJDL = ['This = that']` results in `boost::python::error_already_set`.
Same for `config.Debug.extraJDL = ['This = "that"']`.

**Conclusion**: spaces around the `=` sign are what kills us and need to be sanitized regardless of the very special use case which gave start to this

## Comment (belforte, 2024-05-22T09:00:14Z)

As to catching the fact that slave aborts and task is left in QUEUED, the only info we have atm are these lines in `nohup.out` i.e. the `stdout/stderr` or the master worker:
```
[crab3@crab-prod-tw01 TaskManager]$ cat nohup.out 
[...usual messages about jwt and OpenSSL..]
terminate called after throwing an instance of 'boost::python::error_already_set'
terminate called after throwing an instance of 'boost::python::error_already_set'
[crab3@crab-prod-tw01 TaskManager]$ 
```
We can possibly monitor-for or otherwise discover dead workers, but a restart will not fix (the QUEUED tasks will be processed again) and checking logs to find which task was being processed and what went wrong will take a lot of human time.

One way I can think f now it to change MasterWorker to fork a separate process for each task, up to a maximun number of concurrent ones. Like we do in PublisherMaster. Instead of the current fixed pool of slaves which get work from a shared queue.
That's quite a change, but may help in other ways too. 

Another way is to check if slave is alive  inside the master loop and record somewhere the current task of a slave.
I do not know how to do it atm, but could be possible. TW slaves are instances of `multiprocessing.Process` like the MasterPublisher ones for which we already use the `is_alive`method

Checking on heatch of TW slave is something we "need to do" since ever, urgency comes and go as problems which make them die come and go.

@novicecpp I will welcome your suggestions
@mapellidario  I will welcome your suggestions

!!! Sorry Marco Mambelli if you were spammed.

## Comment (mapellidario, 2024-05-22T13:16:02Z)

I had experience with `subprocess.Popen`, I never really used multiproessing, so it took me a while to come up with a proper suggestion.

Long story short: I think that in `Worker.py` we need to regularly loop over every process in `self.pool` and:

- `p.join(0.1)`: join with a timeout, see [1]. if does not block forever, it blocks at maximum for `0.1` seconds, if the process is still running nothing will happen, if the process finished, then `p.is_alive()` and `p.exitcode` are updated
- `p.is_alive()`: this returns a consistent result only after a join!
- if it is not alive, check the exitcode. if it is not zero, remove this process from the pool and add a new one. 

<details><summary> Example, that provides a longer explaination </summary>

```python
import multiprocessing
import time
import os
import signal

def worker(x, qout, pids):
    print(f"pid={os.getpid()}; input={x}")
    pids.put(os.getpid())
    time.sleep(10)
    qout.put(x*x)

def main():
    inputs = list(range(1,6))
    qin = multiprocessing.Queue()
    for i in inputs:
        qin.put(i)
    qout = multiprocessing.Queue()
    pids = multiprocessing.Queue()
    pool = []
    for _ in range(qin.qsize()):
        x = qin.get()
        p = multiprocessing.Process(target=worker, args = (x, qout, pids))
        p.start()
        pool.append(p)
    print("started the processes")
    pkill = pids.get()
    print("about to kill: ", pkill)
    os.kill(pkill, signal.SIGKILL)
    print("check if a process died")
    for p in pool:
        print(f" died(0)? pid={p.pid}; alive={p.is_alive()}; exitcode={p.exitcode}")
        p.join(timeout=0.1)
        print(f" died(1)? pid={p.pid}; alive={p.is_alive()}; exitcode={p.exitcode}")
    print("wait until all processes finish")
    for p in pool:
        p.join()
        print(f" finished? pid={p.pid}; alive={p.is_alive()}; exitcode={p.exitcode}")
    print("processes finished. results:")
    for _ in range(qout.qsize()):
        print(" ", qout.get())

if __name__ == "__main__":
    main()
```

output

```plaintext
> python main.py
pid=564448; input=1
pid=564449; input=2
pid=564451; input=3
started the processes
pid=564453; input=4
about to kill:  564448
check if a process died
 died(0)? pid=564448; alive=True; exitcode=None
pid=564455; input=5
 died(1)? pid=564448; alive=False; exitcode=-9
 died(0)? pid=564449; alive=True; exitcode=None
 died(1)? pid=564449; alive=True; exitcode=None
 died(0)? pid=564451; alive=True; exitcode=None
 died(1)? pid=564451; alive=True; exitcode=None
 died(0)? pid=564453; alive=True; exitcode=None
 died(1)? pid=564453; alive=True; exitcode=None
 died(0)? pid=564455; alive=True; exitcode=None
 died(1)? pid=564455; alive=True; exitcode=None
wait until all processes finish
 finished? pid=564448; alive=False; exitcode=-9
 finished? pid=564449; alive=False; exitcode=0
 finished? pid=564451; alive=False; exitcode=0
 finished? pid=564453; alive=False; exitcode=0
 finished? pid=564455; alive=False; exitcode=0
processes finished. results:
  4
  9
  16
  25
```

notice the lines:

```plaintext
 died(0)? pid=564448; alive=True; exitcode=None
 died(1)? pid=564448; alive=False; exitcode=-9
```

this means the before the join the value of `is_alive()` can not really be trusted, it can be outdated!

</details>

[1] https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join

## Comment (belforte, 2024-05-22T13:47:44Z)

I think that `is_alive` can be trusted but you need to put some delay between these lines to give the process time to die 
```
 os.kill(pkill, signal.SIGKILL)
    print("check if a process died")
    for p in pool:
        print(f" died(0)? pid={p.pid}; alive={p.is_alive()}; exitcode={p.exitcode}")
```
I added 1 sec sleep and it is OK, if I am not mistaken.

all in all, I use `is_alive` in Publisher and works even w/o `join`

Sorry if I was not clear, I want feedback on a plan. Not converge on all implementation details right away. I know how to start processes, I am not sure how exactly to change the Worker.py code which we did not touch "since ever" w/o too much risk. And I do not know a good way to tell which task was being worked on when process. crashed

## Comment (mapellidario, 2024-05-22T14:00:11Z)

If the plan is "let's invest time to make sure that we detect dead workers", then I am all in.

if you need help with a plan for " a good way to tell which task was being worked on when process. crashed" or "I am not sure how exactly to change the Worker.py code which we did not touch "since ever" w/o too much risk", then sorry i am not sure how to do it without giving feedback that will be rejected as "implementation details"

## Comment (belforte, 2024-05-22T14:05:26Z)

in other words: it will be a bit of work and require a lot of testing. If we decide to do it, let's open a new issue and discuss details there.

Adding detection of dead workers e.g. in https://github.com/dmwm/CRABServer/blob/40a796ffe3d1c7b1b2cddf6a6e74c3b08e2b5a3a/src/python/TaskWorker/Worker.py#L246
by adding an `is_alive` check should be easy and as long as we simply record a message, safe !

## Comment (novicecpp, 2024-05-23T05:01:59Z)

What's about handling the task that causes the child's process to crash?

## Comment (novicecpp, 2024-05-23T05:20:45Z)

> One way I can think f now it to change MasterWorker to fork a separate process for each task, up to a maximun number of concurrent ones. Like we do in PublisherMaster. Instead of the current fixed pool of slaves which get work from a shared queue.

I support this idea, also solve https://github.com/dmwm/CRABServer/issues/8350.

We can divide into 2 steps, first is wrap the [work()](https://github.com/dmwm/CRABServer/blob/40a796ffe3d1c7b1b2cddf6a6e74c3b08e2b5a3a/src/python/TaskWorker/Worker.py#L99) in `Worker.py` to execute in grandchild process. If this work well, refactor the code at MasterWorker to spawn child each task

One concern is about performance. It will fork grandchild for every task, which costs a lot of CPU overhead.

## Comment (mapellidario, 2024-05-23T09:16:17Z)

It's also true that TW actions take at least a few seconds, spawning a new process for every task may not be a that much more cpu usage in the grand scheme of things

[1] https://monit-grafana.cern.ch/goto/cbpwWLPIR?orgId=11

## Comment (belforte, 2024-05-23T13:44:33Z)

we discussed in the meeting and agreed on Wa's suggestion and can go straight for forking one child to handle each task and take care of timeout at same time. Will open ad-hoc issue

## Comment (belforte, 2024-05-23T13:45:56Z)

I am closing this on:
* if HTCondor raises an exception, it is handled properly already
* if HTCondor causes an abort (like in this case) it is the same as "worked died for out of memory or any accident" and we deal with it in new issue
