# dmwm/CRABClient pull request #5205: Print rule id instead of container name in "crab status" command

State: closed
Opened: 2023-08-08T13:37:36Z
Closed: 2023-08-09T13:42:55Z
Merged: 2023-08-09T13:42:55Z
URL: https://github.com/dmwm/CRABClient/pull/5205

## Opening post (novicecpp, 2023-08-08T13:37:36Z)

Sub task of https://github.com/dmwm/CRABServer/issues/7797

(See the line after `Job status:`) Changing from 

![Screenshot from 2023-08-08 13-18-09](https://github.com/dmwm/CRABClient/assets/2346664/676cca0c-aef5-4474-88e8-635cdc34b19b)

```
Rucio Container:  user.tseethon:/GenericTTbar/tseethon-ruciotransfers-1-94ba0e06145abd65ccb1d21786dc7e1d/USER
Tips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 
```

To 

![Screenshot from 2023-08-08 15-16-15](https://github.com/dmwm/CRABClient/assets/2346664/25e62d85-b9ef-414f-8153-0a59479dc601)

```
Transfer container's rule: https://cms-rucio-webui.cern.ch/rule?rule_id=5dd94c3731994a8f8251571a7f5aab9c
Tips on how to check on Rucio StageOut at https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Stageout_with_Rucio 
```

## Comment (cmsdmwmbot, 2023-08-08T13:39:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 3 warnings
   * 207 comments to review
 * Pycodestyle check: succeeded
   * 99 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/934/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-08T15:00:18Z)

I am a bit unhappy with retrieving full transfersdb info for all files, only to get one value. We can put this is for our convenience, but if and when people start using it extensively we may run into problems. Why don't we add one column to TaskDB table ?

## Comment (belforte, 2023-08-08T15:23:56Z)

Maybe add to cache_status file as a transient  solution ? Not sure it is less work, surely less clean than an ad hoc column. BTW, in task DB we have outdataset which will be the name of the "staying" container where additional tasks can add files. We also have a task-dedicated container which we use for tracking the task transfers, shall we add that to the DB as well ?

## Comment (novicecpp, 2023-08-09T06:11:30Z)

If you are okay with adding 2 new columns in Tasks table, I will go this way.

What about `tm_transfer_container_name` and `tm_transfer_container_ruleid` for the new column's names?

## Comment (belforte, 2023-08-09T12:23:43Z)

can you remind me if we now have a rule for each transfer container or one for each output dataset ?
Anyhow I propose slightly shorter names `tm_transfer_container` and `tm_transfer_rule`

You can certainly merge this PR and leave the new columns for a later time (e.g.after your vacations)

## Comment (novicecpp, 2023-08-09T13:42:33Z)

Thanks. 

I plan to put a separate rule for publish container too. But let's discuss it later.
And thanks for the shorter name. It is indeed much better.
