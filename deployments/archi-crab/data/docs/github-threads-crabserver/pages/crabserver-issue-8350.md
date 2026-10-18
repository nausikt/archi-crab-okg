# dmwm/CRABServer issue #8350: add timeout for TW actions

State: closed
Opened: 2024-04-24T09:40:28Z
Closed: 2024-09-19T10:08:38Z
Labels: Type: Enhancement, Type: Support, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8350

## Opening post (belforte, 2024-04-24T09:40:28Z)

with reference to
https://cms-talk.web.cern.ch/t/crab-task-queued-on-command-submit-for-a-while/39714
we have no protection against the situation where TW slaves get stuck for many hours.

So far this has been rare, but we can't risk users to keep submitting stalled tasks and make system grind to halt.

Can start with e.g. 1hour timeout and monitor

## Comment (belforte, 2024-04-24T09:54:25Z)

@novicecpp do you agree to take this once CI/CD is done ? Should not be too much work, but I do not have a specific implementation plan in mind.

## Comment (belforte, 2024-04-24T10:23:52Z)

related to #7720

## Comment (novicecpp, 2024-04-24T12:37:24Z)

Yes. I can but not immediately after CI.
I need to go back to PyPI to make Publisher work with PyPI image.

## Comment (belforte, 2024-04-24T20:43:44Z)

PR https://github.com/dmwm/CRABServer/pull/8352 is related to this

## Comment (novicecpp, 2024-05-16T08:27:20Z)

@belforte do you have any implementation idea in mind? 

My idea is to kill worker process entirely if it reach timeout threshold.

There is 2 ways to achieve this:
- Use [concurrent.futures.Executor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor) to spawn child thread of worker process (with `max_workers=1`) and use result timeout (similar to `join()` in `multiprocessing`) as a signal to terminate the child. Simple enough, in exchange for the extra overhead of spawning threads (also, later we can refactor multiprocessing part by replacing it with concurrent.futures at MasterWorker)
- Save the timestamp of the start/end of each iteration of the worker process on MasterWorker, then calculate the timeout from the timestamp and [terminate](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate) the worker process if it reaches the threshold. This requires a separate queue for each process to prevent [data corrupt from process terminated](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues), which will add complexity on how we distributing the tasks to each process's queue. The advantage of this way is there is no extra overhead from thread spawning.

Acknowledge: Thanks Dario for the brainstorming!

## Comment (belforte, 2024-05-16T08:46:22Z)

I had no ideas !
firsrt way seems better than the second. But I was hoping that we could act inside the Handler. And keep it simpler.

Something like this maybe https://python.pages.doc.ic.ac.uk/2021/lessons/decorator/03-application/02-timeout.html ?
The good thing is that relies on standard python [signal.alarm(time)](https://docs.python.org/3/library/signal.html#signal.alarm)
See also https://pypi.org/project/timeout-decorator/
(I just googled things up now).

Anyhow, both of you surely know more than me !

Unrelated, using `concurrent.futures` is appealing, but I a bit worried about the amount of work. Yet if it allows to fork a process for each new task instead of slaves which persists for days it may be worth.

## Comment (novicecpp, 2024-05-16T09:04:22Z)

I did not consider signal option because it is not work well with `multiprocessing`,  most of solution I found on the google required some hackish approach ([for example](https://stackoverflow.com/questions/40672264/python-dynamic-multiprocessing-and-signalling-issues)).

## Comment (novicecpp, 2024-09-13T10:43:38Z)

To-do:
- [ ] Enable on production.

## Comment (belforte, 2024-09-19T10:08:38Z)

let's move enable and test to a different issue
