# dmwm/CRABServer issue #7765: refactor ServerUtilities.py

State: open
Opened: 2023-07-17T08:09:08Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7765

## Opening post (belforte, 2023-07-17T08:09:08Z)

Should have three files
* what is used also in CRABClient, hopefully very little, which needs to stay py2/3 compat
  * create new file name here (e.g. constants !)
* what is used only in server, so can move to py3 only and rely on pylint when changing
* accept also that some code like encodeRequest can be duplicated  or adapted to simpler use case and moved to ClientUtilities

## Comment (novicecpp, 2023-08-07T14:58:12Z)

Just random though from reviewing https://github.com/dmwm/CRABServer/pull/7800
- Keep `ServerUtilities.py` for sharing code for both client and server.
- Move all utils.py files into single directory `src/python/utils` like [wmcore](https://github.com/dmwm/WMCore/tree/master/src/python/Utils) does.
  - This way, we can move `RucioUtils.py` into `utils/rucio/functions.py` and move `RucioActions.py` to `utils/rucio/actions.py`.
  - Also, mark `src/python/utils` directory exclusive for servers (REST/TW/PUB).

## Comment (belforte, 2023-08-07T15:28:02Z)

I like this idea, thanks @novicecpp 
@mapellidario please add your thoughts. I defer further cleanup to after we have finalized this. No hurry.

## Comment (belforte, 2023-08-08T13:36:25Z)

Increased priority since it is good to have a plan. Which we will implement slowly

## Comment (belforte, 2024-05-23T10:52:19Z)

hand to Vijay ?

## Comment (belforte, 2024-07-24T09:05:56Z)

I will introduce `src/python/Utils` now. But I prefer to have few/no subdirectories there at this time, since I expect a limited number of files and there will be several utilities in common between TW and Publisher.

## Comment (belforte, 2024-07-24T10:15:04Z)

pfff..  `CRABServer/src/python/Utils` clashes with `WMCore/src/python/Utils` see https://github.com/dmwm/CRABServer/pull/8557#issuecomment-2247507982
