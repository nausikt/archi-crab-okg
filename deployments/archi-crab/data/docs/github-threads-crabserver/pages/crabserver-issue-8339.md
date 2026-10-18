# dmwm/CRABServer issue #8339: remove HTCondorUtils

State: closed
Opened: 2024-04-16T09:42:25Z
Closed: 2024-07-05T10:39:34Z
Labels: Priority: High, Status: In Progress, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8339

## Opening post (belforte, 2024-04-16T09:42:25Z)

nothing is there is needed anymore after #8332 , #8331 and #8338 

- [x] remove calls/imports
- [x] stop adding it to tarballs
- [x] remove from repository

## Comment (belforte, 2024-06-24T16:07:02Z)

@aspiringmind-code this is about https://github.com/dmwm/CRABServer/blob/master/src/python/HTCondorUtils.py

you should verify that the code is not used anywhere in the current CRABServer master, remove it from the scripts which create tarballs and remove it from the repository. Then test REST, TW and Publisher (of course)
