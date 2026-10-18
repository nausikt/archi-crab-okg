# dmwm/CRABServer issue #8667: find a better way to prevent users from recalling PB's

State: open
Opened: 2024-08-28T18:57:31Z
Labels: Type: Enhancement, Type: Support
URL: https://github.com/dmwm/CRABServer/issues/8667

## Opening post (belforte, 2024-08-28T18:57:31Z)

current quota check is "lazy" as creation of several rules can sneak in before user account quota is increased in Rucio to where CRAB limit kicks in.
Lately it resulted in one user being able to ask for recall of O(1.2)PB (out of the dreaded 7PB of HeavyIon AOD) before CRAB refused more submissions.

This is all in all rare, so we do not want to add a lot of code, but it was pointed out that it would be nice to have a way to tell the user something like "hey, are you sure you want to do this ?"

There's no clear good idea yet.

Possibilities include
* lowering the current 500PB quota. 
* doing something special when HI and AOD appear in the dataset name
* when creating a recall rule, wait until quota has been updated, to limit damage of concurrent creation
* force user to "do something extra" for each large recall (e.g. >100TB or 200TB)
* keep track of recall size in our DB so that it is quick and quota check can be effective
* investigate with Rucio experts if something can be done on that side
* ...

## Comment (novicecpp, 2024-08-29T07:53:45Z)

> force user to "do something extra" for each large recall (e.g. >100TB or 200TB)

No, please. 

> when creating a recall rule, wait until quota has been updated, to limit damage of concurrent creation

Dumb idea: 
- random 0-60 seconds before create quota, create. wait quota to update maximum 2 mins.

Another dumb idea: Do tape recall sequentially. 
- Set new stage something like: `TORECALL`
- Recurring action grab `TORECALL` task, then create a recall rule.
- Wait for quota update.
- Then set state to `TAPERECALL`.

## Comment (belforte, 2024-08-29T09:49:14Z)

I love the "do it sequentially" idea. Thank !
:heart: :pray:
