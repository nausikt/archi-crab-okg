# dmwm/CRABServer issue #7517: Setup monitoring for  "crab_tape_recall" rucio user

State: closed
Opened: 2023-02-02T10:42:17Z
Closed: 2023-08-17T10:22:48Z
Labels: Priority: Medium, Status: In Progress, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7517

## Opening post (novicecpp, 2023-02-02T10:42:17Z)

Quickly copy from minutes: Need to check if Rahul had done anything. Stefano has some useful code from Nick.

## Comment (belforte, 2023-02-02T15:56:05Z)

Here's the pointer to Nick's code which indicates how to plot the amount of storage space used by taperecall 
https://github.com/belforte/utils/blob/master/notebooks/RucioTapeRecallUsage.ipynb
missing part is to extend this to all RSE's
and of course this should be somehow turned into somthing that we can see in Grafana

## Comment (novicecpp, 2023-03-21T16:14:59Z)

Tomorrow at 11.00, I will have brainstorming session with Rahul (@dynamic-entropy) to setup monitoring to `crab_tape_recall` account. 

These are questions from myself:
1. How to check if user abuse inputblocks to recall dataset for all block with seperate crab task? (i.e. submit 100 tasks to get 1 PB of RAW dataset)
1. (from O&C week's live note) Can we monitor the volume of tape recall over time?
1. How many duplicate rule (same dataset but recall from different crab tasks)?
1. Time series for tape recall per users, group by (and/or) number_of_rule/number_of_dataset/total_size(/?).
1. Time series for percentage recall successed vs failed (failed: STUCK and REPLICATION that longer than 14 days).
1. How long does it take for rule to change state from REPLICATION to OK?
1. (How do we get info from expired rules?)

@belforte @mapellidario @KatyEllis  Feel free to add more.

## Comment (belforte, 2023-03-23T14:31:16Z)

List of questions that monitoring should answer:
1. is it used/useful ? (how often is used, by how manym etc,)
2. does it work ? (success vs. fail)
3. how long does it take ?
4. how much data does it move ?
5. how much disk does it keep occupied ?

Then there are annoying details ... does some user abuse, can we use it to spot bugs/inefficiencies in data placement, which sites does it use .. which one can spend a lot of time on but really depend on the big picture first. And things we are curious about like what happens if rules expire before it is satisfied and in case how many rules hit that limit ... and should update rule expiration daily so that it is 14 days after last file on tape ? (now it is 14 days after request, since initial experience was that it takes a few hours and only exceptionally a couple days).

## Comment (novicecpp, 2023-03-23T20:08:48Z)

Thanks Stefano.

From meeting with Rahul today I cannot build any panel yet. Most of data we want are not ready to query in opensearch.
- Simple question like "usage over time" need to query database snapshot. 
- If we want to group by crab user for usage, we need to do extra work to get this info (extract from did).
  - Usage per user need a lot of work (list rule > list content of each rule to get size > sum size group by user) .
- `How long does it take?` No data besides state from database snapshot. 

Well, it is more complicated than I thought.

## Comment (dciangot, 2023-03-24T07:32:12Z)

@novicecpp  I agree, I think there is no way around using db snapshot via spark analitix for this kind of information. I have a baseline from which you can start play with. I did some basic analysis on tape recall some time ago.

## Comment (belforte, 2023-03-24T09:47:29Z)

I am not sure that tracking by user is important. By datatier and primaryDataSet would be enough (to be clear those are the T and P in : datasetname = /P/S/T ), We need to make it easy to find which dataset a taperecall rule refers to. We are free to change how containers we use are named if that helps.

There is also a clear "architectural" question: much of the info can be gathered from CRAB's TW logs as well. Do we go that way ? Or stick with what's available in Rucio ?

Is used quota per account available in OpenSeach ? Could it be added ? If not, could we start with some "automation" around [Nick's two lines](https://github.com/dmwm/CRABServer/issues/7517#issuecomment-1413968908)

## Comment (novicecpp, 2023-03-24T13:09:27Z)

> I have a baseline from which you can start play with. I did some basic analysis on tape recall some time ago.

@dciangot Thanks. could you give me that notebook/code?

> I am not sure that tracking by user is important. By datatier and primaryDataSet would be enough (to be clear those are the T and P in : datasetname = /P/S/T ), We need to make it easy to find which dataset a taperecall rule refers to. We are free to change how containers we use are named if that helps.

It needs to monitor if users abuse the tape recall.

> There is also a clear "architectural" question: much of the info can be gathered from CRAB's TW logs as well. Do we go that way ? Or stick with what's available in Rucio ?

Either way that make our life easier for us. But for now I will stick with what available in Rucio.

> Is used quota per account available in OpenSeach ? Could it be added ? If not, could we start with some "automation" around https://github.com/dmwm/CRABServer/issues/7517#issuecomment-1413968908

Thanks for pointing out(not sure if it available in opensearch though). I will have a look.

## Comment (belforte, 2023-03-24T13:59:47Z)

> Thanks for pointing out(not sure if it available in opensearch though). I will have a look.

Nope. It only queries Rucio DB, where apparently there are tables which track the change in used quota by any given account per RSE. 

I still think that we do not want to care about sorting requests by users. At least not immediately

## Comment (dciangot, 2023-04-05T09:43:37Z)

> @dciangot Thanks. could you give me that notebook/code?

@novicecpp  You can find it here
https://cernbox.cern.ch/s/GakUe3QVNQUtLAW

## Comment (belforte, 2023-08-17T10:22:48Z)

well..... the most pressing issues 
 * how much quota is used overall
 * monitoring of slow/stuck rules
are under control.
More detailed analyitcs... let's file as "monitoring can always be improved"
