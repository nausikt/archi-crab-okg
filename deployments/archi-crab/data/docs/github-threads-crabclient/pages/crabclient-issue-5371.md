# dmwm/CRABClient issue #5371: fix list of valid task statuses for preparelocal

State: closed
Opened: 2025-02-17T11:20:09Z
Closed: 2025-02-17T13:52:32Z
URL: https://github.com/dmwm/CRABClient/issues/5371

## Opening post (belforte, 2025-02-17T11:20:09Z)

from Jenkins test log
```text
Some CRABClient commands failed. Find failed commands below:
11:27:17 
11:27:17 TEST_COMMAND: crab preparelocal  --proxy=/tmp/x509up_u501  --dir=crab_20250217_104215  
11:27:17 TEST_RESULT: FAILED                                                                                 
11:27:17 TEST_MESSAGE:
11:27:17 Getting input files into tmp dir /tmp/tmplcw4y6pg
11:27:17 Can only execute jobs from tasks in status SUBMITTED or UPLOADED. Current status is KILLED
```

Could add KILLED to
https://github.com/dmwm/CRABClient/blob/c9bcc3d4e5af87a2a4a74221e29545a982fdf1c8/src/python/CRABClient/Commands/preparelocal.py#L77-L78

but in view of list of status possibly changing (e.g. with https://github.com/dmwm/CRABServer/issues/8394 ) it may be safer to simply exclude transient ones from beginning of pipeline: WAITING, NEW, HOLDING, QUEUED

## Comment (belforte, 2025-02-17T11:31:57Z)

the list of good or bad states is too long for my taste[1]. No alternative now. But best solution IMHO is to add a column in DB where we set a bit to indicate that all needed files are availabe in S3. I.e. that task went through UPLOADED status even if it progressed to new ones afterwords.

@aspiringmind-code @sinonkt what do you thing ? any volunteer to do that change ?

Another possibility is to try to download the tarballs, catch the failures, and complain then, leaving the user with no clue !

[1]
states to avoid 'WAITING', 'NEW', 'HOLDING', 'QUEUED', 'SUBMITFAILED', 'REFUSED', 'TAPERECALL' . More ?
states oK : UPLOADED, SUBMITTED, KILLED, KILLFAILED, COMPLETE, FAILED. More ?

## Comment (aspiringmind-code, 2025-02-17T12:22:47Z)

I'd like to volunteer.  Let's exclude the transient task states and add a column in DB. I don't prefer the tarballs method.

## Comment (belforte, 2025-02-17T13:41:37Z)

thanks Vijay ! Let's put this patch now to make test suite happy and revisit client once a new TW is in production with the new column properly filled.
