# dmwm/CRABServer pull request #7578: set start_time for DAG at the time TW runs. Fix #7498

State: closed
Opened: 2023-04-04T09:35:08Z
Closed: 2023-04-04T15:41:29Z
Merged: 2023-04-04T15:41:29Z
URL: https://github.com/dmwm/CRABServer/pull/7578

## Opening post (belforte, 2023-04-04T09:35:08Z)

(no text)

## Comment (cmsdmwmbot, 2023-04-04T09:42:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 16 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1480/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-04-04T10:40:06Z)

Before submitting a proper review i have a comment. 

I know that we can always retrieve the time a task is added to the DB via its taskname (provided that we never change it), but I would prefer to have a column whose sole purpose is to tell me when the user first added the task to the DB. This can be useful for example when aggregating statistics about which dataset is requested when. 

Let's say we have a plot "total size of input dataset to crab task vs submission day". If you change the `tm_start_time` after a taperecall, then the contribution of a single task to such plot will move from one day to another. The alternative would be to parse the submission day from the taskname, ugly.

The solution that I would prefer would be to use `tm_start_injection` [1] to compute the classads `CRAB_TaskSubmitTime` and `CRAB_TaskEndTime` .

At the moment, this column in the DB is empty, so some effort may be needed to make sure it is properly passed around the dagmansubmitter functions, but it seems it was designed exactly for this usecase. 

[1] https://github.com/dmwm/CRABServer/blob/ec3985683342650500703201e69bd063efe84aa3/src/python/Databases/TaskDB/Oracle/Create.py#L40 

[2] https://github.com/dmwm/CRABServer/blob/19bf7bae634c59ea1dc29f37d11094cb05199984/src/python/TaskWorker/Actions/DagmanSubmitter.py#L495-L497

## Comment (belforte, 2023-04-04T12:50:38Z)

This PR does not change the value in the DB
But I forgot about `tm_injection_time` we can surely think of using that as well, but of course requires more work.

## Comment (mapellidario, 2023-04-04T15:14:28Z)

> This PR does not change the value in the DB

Ah true, now I see, the new task info is not pushed by TW to the DB. okok

## Comment (belforte, 2023-04-04T15:31:41Z)

> > This PR does not change the value in the DB
> 
> Ah true, now I see, the new task info is not pushed by TW to the DB. okok

my difficulty was indeed the lack of an API to do that  ! I do not know if we have one to upated `tm_start_injection` either. If we ever start using it may be good to rename. I do not know why it is there !
