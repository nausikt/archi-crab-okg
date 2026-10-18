# dmwm/CRABServer issue #7656: puppet - some things can be improved

State: closed
Opened: 2023-06-07T16:58:55Z
Closed: 2024-06-24T15:33:44Z
Labels: Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7656

## Opening post (mapellidario, 2023-06-07T16:58:55Z)

The puppet repository that we use to configure our VMs can be improved.

- [x] Stop using https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts for our schedds
    - instead, clone to our repo only the scripts that we know we need.
    - for example, `JobCleanup.py` is needed :)
    - JobCleanup.py: use `time.time()` instead of `ServerTime` from the schedd.query python binding (which is broken until condor 10.0.2 or 10.2 at least)  : done by @mapellidario https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/50bd097df10d968003fe258163a3e7d0863a2b67
- [x] review libcurl deployment : not needed in alma9
- [x]  WMArchiveUploader : done by @novicecpp  
- [x] (stefano) make sure all scripts can run in python3 - being done for alma9 #8257

## Comment (belforte, 2023-06-07T17:31:44Z)

we need to do something about WMArchiveUploader too (too big a task for this issue, I guess) which comes with its own very old WMCore version inside :-(

And of course move all scripts to python3 !

## Comment (belforte, 2024-03-04T22:00:30Z)

@mapellidario  I have updated task list at top. I think this can be closed. Pls review and if you agree, close. Thanks

## Comment (belforte, 2024-06-24T10:40:13Z)

@mapellidario can we close ?

## Comment (mapellidario, 2024-06-24T15:33:44Z)

yes, sure we can, sorry for keep you waiting!
