# dmwm/CRABServer issue #7569: Take aways from spring O&C week

State: closed
Opened: 2023-03-17T13:22:52Z
Closed: 2024-08-23T10:34:37Z
Labels: Status: On Hold, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7569

## Opening post (belforte, 2023-03-17T13:22:52Z)

takeaways from  [talk by Dima](https://indico.cern.ch/event/1256427/contributions/5302294/attachments/2613543/4516299/2023-03-17%20Disk%20Space%20Management%20Options.pdf)  (see also [live notes](https://docs.google.com/document/d/1qeo2YZ9zgQFDBpF0cRT8yDXTYURznRdqx5Foq68bBzA/edit#heading=h.nj0gfrlutmaw) page 34) were discussed by us in [googleDoc](https://docs.google.com/document/d/1Du9VNTlbYZ15WQ2MflY9_l2F4RR3cXiZyi0vyXS4H0w/edit) and distilled into following action items for us
 - [x] crab tape recall should not recall across atlantic #7589 
 - [x] help users deal with tails #7595
 - [x] allow processing of blocks which miss some files #7573 
 - [x] Lock data on disk when submitting a task #7592 
 - [x] report progress of tape recall (and expiration) in crab status #7593
 - [x] setup monitoring of tape recalls #7517 
 - [x] implement `crab recall --dataset=.... --sites=... --days=...` #7594
 - [x] help users find whether a dataset is fully on disk
   - [x] improve reporting from TW #7596
   - [x] implement  `crab checkdataset ....` https://github.com/dmwm/CRABClient/issues/5191

## Comment (belforte, 2023-04-13T22:28:32Z)

I set as TOP priority because we need to make plans for this. As soon as every thing has an ad hoc issue assigned, set on HOLD. Then close when all actions are done

## Comment (novicecpp, 2023-04-14T12:14:13Z)

From live note:
> Consider efficiency of recalling from tape, easier to recall large blocks of files than lots of little groups. There need to be operational procedures in place to minimize the pain

Do we need to take any action about this?

## Comment (belforte, 2023-04-14T12:23:43Z)

No, this is for Rucio to worry about. And IMHO not even Rucio should care. There are other SW layers between Rucio and the tape drives : FTS and the local site storage managers, usually sites run tape management software which builds a queue of requests and reorders them to minimize tape mount/dismount/seek (i.e. tape wear). 

We could worry about "if user asked for one block today, maybe they will ask for next block next week, so it would be better to recall two or more blocks now" or "if this is a small dataset, even if they asked for a block, recall it all".
But it is difficult to say how much it would help.

There is one action that we should do anyhow, to make our side cleaner, and that will also help here:
* if user asks for a non-AOD (i.e. no autorecall) tier, but overall size is <10TB, recall it anyhow w/o bothering to ask for a list of blocks.
I was about to open an issue for this !

## Comment (novicecpp, 2023-04-14T13:03:36Z)

That is clear. Thanks Stefano.

> if user asked for one block today, maybe they will ask for next block next week, so it would be better to recall two or more blocks now

Hmm, interesting. I will try to look at monitoring later if it can detect this behavior.

## Comment (belforte, 2023-04-14T16:14:36Z)

I doubt you will find anything in monitoring. It just sending thoughts to explore small corners of phase-space.
The more "realistic" scenario I can imagine is:
I somehow decided a need to process dataset  /A/B/RERECO which is 1 PB.
I find that CRAB only let me get 10TB at a time.
So I submit 10 tasks to get 100TB.
As soon as they complete, I submit more.

This did not happen yet, and it may never, but once we tall people "only 10TB at a time" sooner or later someone will do.

From site POV, better recall 1 PB "now" and get done with it. From our POV, maybe this will only happen  rarely, maybe user will get tired after 200TB, maybe we will be able to detetc and stop, maybe we will discover that we can safely allow 100TB instead of 10TB so that "a piece a day for 100 days" will not happen.

Maybe time to worry about what information to send to ES in order to monitor things. Parsing a free format comment field in the rule (the only way we have now) is not good.

## Comment (belforte, 2023-04-20T10:39:20Z)

On HOLD now. CLose when all boxes are checked

## Comment (belforte, 2024-08-23T10:34:37Z)

no need for `crab recall`
