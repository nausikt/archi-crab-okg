# dmwm/CRABServer issue #8442: Publisher stop.sh fails if the Publisher process stops for longer than the next cycle

State: closed
Opened: 2024-05-29T09:27:24Z
Closed: 2024-10-31T16:21:52Z
Labels: OPERATION, PyPI, Publisher
URL: https://github.com/dmwm/CRABServer/issues/8442

## Opening post (novicecpp, 2024-05-29T09:27:24Z)

The stop.sh script (or manage.sh stop in new PyPI image) will wait forever if it run after exceed "Next cycle" time and no Publisher process is running.

The script parse timestamp from last log line from `logs/log.txt`:
```
2024-05-29 11:13:12,912:INFO:PublisherMaster,296:Next cycle will start at 11:39:01
```
https://github.com/dmwm/CRABServer/blob/97bf5913bd1900c229d87ab77c803e39a15743e1/src/script/Deployment/Publisher/stop.sh#L19-L23

The `delta` is gradually decreasing while the time (epoch) is increasing. No process is running mean no one will update the log line and script will stuck forever.

Workaround is exec to the container and kill `/bin/bash ./stop.sh` to allow Deploy_TW to continue.

## Comment (novicecpp, 2024-05-29T09:28:47Z)

Simply check Publisher process if it is still running before checking with time, maybe resolve the issue.

## Comment (belforte, 2024-05-29T12:42:08Z)

that's surely good ! But maybe we can also introduce a timeout. Originally the idea was that at time a single Publisher iteration could take hours and we did not want to have a timeout + hard kill. Publisher was not designed with the idea of being stateless and idempotent, and I opted for "safety". But we were only using stop as issued by operator. As we try to have something automatic, and  have enough experience, we can probably try a timeout at 2h.

## Comment (novicecpp, 2024-09-13T11:06:17Z)

After https://github.com/dmwm/CRABServer/issues/8561, it rarely happens on prod/preprod but happens quite a lot on test env and is super annoying.

My new idea is we do flock using `getLock()` like PostJob.py 
https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/src/python/TaskWorker/Actions/PostJob.py#L426-L428
Wrap over
https://github.com/dmwm/CRABServer/blob/ce559a11ef02c447f909ee166b7d48f218eb021d/src/python/Publisher/Main.py#L69
On the process controller script, just check if flock file exist.

Is this too over-engineering @belforte ?

## Comment (belforte, 2024-09-13T19:31:22Z)

#856 does not exist. Which issue did you want to point to ?
Maybe we can simply use file to record the PID of the running Publisher, like it happens for the REST ?
IIUC the problem is that we end up  waiting forever while there is nothing running.

PostJob has locks to prevent multiple PJs running at same time from trying to update same file a at same time. But here we should not need such locks.

Or maybe I am confused :-), as usual.

## Comment (belforte, 2024-09-15T11:05:46Z)

modify isPublisherBusy to do a "ps" ?

## Comment (novicecpp, 2024-09-17T18:07:59Z)

Ok, I remember why I need `getLock()`.
Parsing `logs.txt` to find the time to execute next round is unreliable. But I forgot which case that make `stop.sh` stall.

But...The real problem is that `stop.sh` stall forever in CI. 
When it happens, it feels like "everything is fine" because you did not get a fail message within 15mins, but actually the Publisher deployment has been in progress for hours.

The real(?) solution would be to set a timeout, as you said in https://github.com/dmwm/CRABServer/issues/8442#issuecomment-2137321230 . 
2 hr is too much, 5 mins should be enough for every env.

## Comment (belforte, 2024-09-17T20:00:30Z)

but stlll.. wouldn't your original idea https://github.com/dmwm/CRABServer/issues/8442#issuecomment-2136962442 be enough ?

## Comment (belforte, 2024-09-17T20:07:43Z)

if you mean to kill Publsher 5min after "next iteration will start at ..." time, I am kind of lost.

## Comment (novicecpp, 2024-09-17T20:43:10Z)

> but stlll.. wouldn't your original idea https://github.com/dmwm/CRABServer/issues/8442#issuecomment-2136962442 be enough ?

Yes, and it already implemented in https://github.com/dmwm/CRABServer/pull/8562 .
But....there is a case when publisher process is running (publishing/sleeping/whatever) but stop.sh never manage to terminate it and stuck forever. Sorry, I am not sure "how" until I see it again. 

> if you mean to kill Publsher 5min after "next iteration will start at ..." time, I am kind of lost.

No. Change stop.sh from "waiting forever" to "exit with error if waiting longer than 5mins".
Then, CI will shout an error, which means manual intervention is required. Not just keep silencing...

## Comment (belforte, 2024-09-18T00:18:23Z)

:astonished: 
**wow** odd things are going on. Yup let's try to catch em, or at least live with them

## Comment (novicecpp, 2024-10-31T16:21:52Z)

This is done in https://github.com/dmwm/CRABServer/pull/8737
