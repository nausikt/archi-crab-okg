# dmwm/CRABServer issue #9107: TapeRecallManager fails to remove old rule when tasks are killed if  2 or more tasks are using it

State: open
Opened: 2025-06-04T08:21:58Z
Labels: Type: Bug, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/9107

## Opening post (belforte, 2025-06-04T08:21:58Z)

in case there are multiple tasks using same rule for tape recall, current code does not have a way to remove the rule even if they are all killed, since the `handleKill` method in there is a loop on tasks. Even if all tasks are killed, they are processed independently and when checking one there are always other using the rule and rule deletion is skipped.

Rule will eventually be removed 1 month after creation, but in the meanwhile it persists in our dashboard and if partially completed keeps locked data in place affecting quotas.

https://github.com/dmwm/CRABServer/blob/760bad67b5fcdef2ce9641399fbe700c6e980ff7/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L68-L87

## Comment (belforte, 2025-06-04T08:26:22Z)

In the one case I was looking at, there were two killed tasks and rule was in SUSPENDED status. 
Which raises the interesting questions of what to do when TapeRecallManager finds some SUSPENDED rule. Do we report ? Do we delete ? Do we try to fix ?
A way to "try to fix" is to change status from SUSPENDED to STUCK and then boost rule which sets it to REPLICATING so that transfers are attempted again. IIUC Rucio sets rules in SUSPENDED after they have been STUCK (i.e. with some failings) for 15 days and does not try anymore.

## Comment (belforte, 2025-06-11T13:09:53Z)

a possible way to solve this may be by checking the status of those other tasks

## Comment (belforte, 2025-07-10T11:42:18Z)

@sinonkt this is possibly easy to reproduce in production instance, but very hard in a test TW. Let's start do as
1. make sure that you understand the problem, we can about it in case
2. figure out the strategy to address it and let's discuss it
3. implement and we review
4. finally I will helps you with testing

how does it sound ? If you feel that you have things very clear you can do 1, 2 and 3 before coming back to me, but you should still follow that approach

## Comment (nausikt, 2025-07-10T11:58:49Z)

> [@sinonkt](https://github.com/sinonkt) this is possibly easy to reproduce in production instance, but very hard in a test TW. Let's start do as
> 
> 1. make sure that you understand the problem, we can about it in case
> 2. figure out the strategy to address it and let's discuss it
> 3. implement and we review
> 4. finally I will helps you with testing
> 
> how does it sound ? If you feel that you have things very clear you can do 1, 2 and 3 before coming back to me, but you should still follow that approach

It sound great, I believe that i've roughly think through 1,2,3 and have some ideas about it. But, can we've early discuss about [1]? just to make sure i'm on the same page as yours.
