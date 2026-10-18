# dmwm/CRABServer issue #8428: in TW handle each task in its own subprocess

State: closed
Opened: 2024-05-23T14:01:28Z
Closed: 2024-06-28T11:02:13Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8428

## Opening post (belforte, 2024-05-23T14:01:28Z)

this way we can take care of timeouts #8350 and crashes #8420 

At first sight changes could around Line 99 here
https://github.com/dmwm/CRABServer/blob/40a796ffe3d1c7b1b2cddf6a6e74c3b08e2b5a3a/src/python/TaskWorker/Worker.py#L94-L120

## Comment (novicecpp, 2024-06-11T08:06:13Z)

Use [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) looks promising.
Here is testing snippet:
```python
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool
import time
import requests
import sys
import ctypes
import traceback

def fn(n):
    print(f'return {n}*5')
    return n*5

def fn_timeout(n):
    print('sleeping 6 secs')
    time.sleep(6)
    return n*5

def fn_exception(n):
    time.sleep(1)
    raise TypeError('just raise')
    return n*5

def fn_coredump(n):
    time.sleep(1)
    #https://codegolf.stackexchange.com/a/22383
    ctypes.string_at(1)
    return n*5

print('running..')
with ProcessPoolExecutor(max_workers=1) as executor:
    future = executor.submit(fn, 4)
    outputs = future.result(timeout=5)
print(f'output from future: {outputs}')

print('running timeout')
try:
    with ProcessPoolExecutor(max_workers=1) as executor:
         future = executor.submit(fn_timeout, 5)
         outputs = future.result(timeout=5)
except TimeoutError as e:
    print(''.join(traceback.format_tb(e.__traceback__)))
    print(e)
    print('this is timeout')

print('running exception')
try:
    with ProcessPoolExecutor(max_workers=1) as executor:
         future = executor.submit(fn_exception, 6)
         outputs = future.result(timeout=5)
except Exception as e:
    print(type(e), ''.join(traceback.format_tb(e.__traceback__)))
    print('this is exception')

print('running crash')
try:
    with ProcessPoolExecutor(max_workers=1) as executor:
         future = executor.submit(fn_coredump, 7)
         outputs = future.result(timeout=5)
except BrokenProcessPool as e:
    print(type(e), ''.join(traceback.format_tb(e.__traceback__)))
    print('this is crash')
```

The output:
```
running..
return 4*5
output from future: 20
running timeout
sleeping 6 secs
  File "/home/thanayut/myhome/playground/processpool/main.py", line 39, in <module>
    outputs = future.result(timeout=5)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 458, in result
    raise TimeoutError()


this is timeout
running exception
<class 'TypeError'>   File "/home/thanayut/myhome/playground/processpool/main.py", line 49, in <module>
    outputs = future.result(timeout=5)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception

this is exception
running crash
<class 'concurrent.futures.process.BrokenProcessPool'>   File "/home/thanayut/myhome/playground/processpool/main.py", line 58, in <module>
    outputs = future.result(timeout=5)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception

this is crash
```

## Comment (belforte, 2024-06-11T08:31:27Z)

I am curious why concurrent futures vs. multiprocessing. I tried to educate myself and read that they boil up to same thing, simply concurrent futures has a simpler interface. But since we have a working setup with multiproxess already...

Somehow the point seems to me if we want to keep current design where slaves are persistent and process one task after another, or only last for the duration of a single task.

There is also an example in Publish Master of using multiprocess to execute one process per task and create new slaves as they complete/fail.

Of course I have nothing against using a concurrent futures instead of multiprocessing, esp. it it makes code easier to write and to read, but would like to understand if there's more, since it will still be a non-minor change. E.g. logging will be different.


I have always been reluctant to touch this part, but personally think that the overload of creating a process for each task is low and prefer the "Publisher" approach. Of course I am biased since am the one who did the latter.

## Comment (novicecpp, 2024-06-11T10:31:38Z)

It is [the library that build on top of multprocessing](https://github.com/python/cpython/blob/b8845369aa76a6b2d4f147243d8451ce00abc661/Lib/concurrent/futures/process.py#L51) to make it easier to write concurrent programming for some pattern.
Is it really the same (e.g., logging)? not sure for big service like TW, I do not have experience enough to answer that.

I will have a look at Publisher code.

## Comment (novicecpp, 2024-06-11T15:01:42Z)

@belforte, if I understand correctly,  the `PublisherMaster.py` has "fire and forget" pattern, then do synchronization between iteration in child using DB instead (i.e., mark job in db as fail to publish so next iteration will not pick it up again). 

Can we do the same in TW? maybe no. We need to handle exceptions, including coredump, that occur in `work()` properly. `work()` itself need to return value back to the parent process (maybe not but scope will be on bigger scope than just spawning a new process to run), also update task status to fail in grandchild process after receiving SIGTERM because timeout, well... I imagine that is might be harder than handling it from child process, where child process already have everything in their hand to manage their own grandchild.

## Comment (belforte, 2024-06-11T15:07:43Z)

it is getting difficult to write about this. What about a chat tomorrow morning ?
Today I am particularly dumb, and need to leave shortly, sorry

## Comment (novicecpp, 2024-06-11T15:09:28Z)

Before/After meeting on Thursday is better for me. No hurry. 
I will dump what I find so far so we have material enough for discussion.

## Comment (novicecpp, 2024-06-11T15:53:54Z)

`multiprocessing` is ugly, but straight forward in in term of process handling.
Here is the full snippet using `multiprocessing lib`:
https://gist.github.com/novicecpp/94ba6401e1a4d5298263616f047734f7

Compare with `concurrent.futures` lib, https://gist.github.com/novicecpp/0a78f131f33fbaa56c4fece844b36a90 which much more cleaner especially excecption handling that occur in grandchild.
Note that `concurrent.futures` does not have proper way to terminate the process in case process getting stuck. However, [sigalarm solution works](https://gist.github.com/novicecpp/0a78f131f33fbaa56c4fece844b36a90#file-con_futures-py-L25-L32), i.e., terminate the process by raise exception in sigalarm handler.

## Comment (belforte, 2024-06-11T20:27:59Z)

I do not want to go into code details discussion with you, I have too much to learn. As I said I am happy to change class if it offers cleaner code. At this moment I only care about "architecture". And do not think that Publsher is fire and forget any more than TaskWorker. Bookeeping for publication is ugly, as we was with Rucio, it suffers of still being an adaptation of an old design with a separate CouchDB-based server.
By the way, why did timeout work w/o signal in initial example but you the signal in [sigalarm solution works](https://gist.github.com/novicecpp/0a78f131f33fbaa56c4fece844b36a90#file-con_futures-py-L25-L32) ?
P.S. where is it defined `sig` at line 68 ?

## Comment (novicecpp, 2024-06-12T09:02:24Z)

I will have a deeper look into Publisher later. 
But still, we need the feedback from grandchild we spawn from executing `work()` function and handle the result properly (Is it break? Is it timeout? what kind exception of the child raised?)

> By the way, why did timeout work w/o signal in initial example but you the signal in [sigalarm solution works](https://gist.github.com/novicecpp/0a78f131f33fbaa56c4fece844b36a90#file-con_futures-py-L25-L32) ?

No, previous one does not work. In the end of process, it wait until child process exit and then it exit.

> P.S. where is it defined sig at line 68 ?

Variable from function arg in [line 61](https://gist.github.com/novicecpp/0a78f131f33fbaa56c4fece844b36a90#file-con_futures-py-L61)
