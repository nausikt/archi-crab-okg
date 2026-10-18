# dmwm/CRABServer issue #7632: RUCIO_Transfer.py: Things need to be done before run test in larger scale.

State: closed
Opened: 2023-05-12T10:31:22Z
Closed: 2023-11-17T15:28:07Z
Labels: Priority: High, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7632

## Opening post (novicecpp, 2023-05-12T10:31:22Z)

The goal of this issue is to track todo lists that need to be done before we can run automated tests at large scale.

Things need to be done are (mostly copy from https://github.com/dmwm/CRABServer/issues/7524#issuecomment-1543590542): 

- [x] Fix `add_replicas` to try again instead of fail them (It should not failed on this step).
- [x] Update correct status to database when files transfer is completed.
- [x] bookkeeping locks monitoring.
  - Need to review it again because it is affected by separating publish and transfer container.
- [x] 1 container for multiple tasks (separate publish and transfer container)
  - However, there is no guarantee it will survive race condition, especially when close the dataset and open new one.
- [x] Fix rucio config broken on `T2_DE_DESY`, and more. https://github.com/dmwm/CRABServer/issues/7740
- [x] Make it run on dev environment.

## Comment (belforte, 2023-05-12T10:56:07Z)

I have not tried to really understand the problem with DESY, but I find it hard to image that a well run site like T2_DE_DESY has a bad configuration, maybe this is us who did not understand how to use the information (so we can fix silently) or, worse, some insufficient specification on how sites should be configured. If the latter it can happen on more sites and we need to get Rucio and SiteFacilities involved.

## Comment (novicecpp, 2023-05-12T10:59:56Z)

About that the site config is not actual problem but it is CMSRucio itself that have weird configuration with temp area.
I have consulted with Rahul and he suggested to open issue in CMSRucio repo and discuss there.

## Comment (belforte, 2023-05-12T11:04:40Z)

yeah, it is a thin and blurred line how much temp_RSE config is a site responsibility vs. a CMS-Rucio vs. a CMS_SiteFacilities responsibility. DIfferent people likely have different ideas where that line lies and all those things change with time, of course

## Comment (novicecpp, 2023-06-21T10:24:12Z)

All list above is now solved (note for broken sites on `T2_DE_DESY` and `T2_UK_SGrid_Bristol` is fixed by hardcode in the scripts.)

3 things that still needs to figure it out before closing this issues.

- [x] Close the dataset when (in OR)
  - It has 100 files
  - 6 hours have passed since last time a block was added to DBS for this task
  - The task has terminated (this was done as a courtesy to user, in case you have a task with 10 jobs, which completed in 1h and do not want to wait 6h to have crab status to say “publication completed”)

If we close it when the above conditions meet, the next iteration will create a new dataset immediately, and it will close in the next 6 hours. So we have many closed datasets without any replicas inside a container. In theory, it may be alright because we use block names in db to publish to DBS, which always has one or more files in it. 

- [x] When `crabConfig.Data.publication=False`, `publishname` is always same (`FakeDataset/fakefile-FakePublish-5b6a581e4ddd41b130711a045d5fecb9/USER`). 

It need to be unique value for each task. Workaround for this is to disable register replica in publish container, but it will defeat the reason of have files manage in Rucio.

- ~~What should we do if replicas stuck form n hours?~~ no need to do anything. Postjob will mark it as failed when time has passed, and we ignore the transfer container after the tasks is end of life.

## Comment (belforte, 2023-06-21T10:32:44Z)

>   If we close it when the above conditions meet, the next iteration will create a new dataset immediately, and it will close in the next 6 hours.

why do we create a new dataset if we have no files to put in it ? Seems something easy to avoid.

I am not sure I fully understand 2nd point. Let's talk about it. In case it should not be too difficult to create a FakeDataset which is unique for each task

## Comment (novicecpp, 2023-06-21T11:08:09Z)

> why do we create a new dataset if we have no files to put in it ? Seems something easy to avoid.

I agree. It should easy to fix but maybe require a lot of code change, same as fake publication.
I will have a look.

## Comment (belforte, 2023-06-21T11:16:29Z)

1. look at transfers.txt
2. no new file ? exit (even as simple as count lines and compare with stored last-line value)
3. use current code

fake publication, I do not know off-hand.

## Comment (novicecpp, 2023-06-29T07:48:58Z)

Closing dataset when time has passed is easier to fix than I though. Now it fixed in my private branch. Closing when the task is completed is another story. There is no easy way to do at the moment.

For FakeDataset I added fix in [PostJob.py#L1627-L1630](https://github.com/novicecpp/CRABServer/blob/47e8804964bc23b760cae497e4e33d3cd24a0942/src/python/TaskWorker/Actions/PostJob.py#L1627-L1630) file. I am not sure if this is proper solution or just workaround. Also, I wonder why we update `tasks.tm_output_dataset` in postjob instead of in REST/TW.

## Comment (belforte, 2023-06-29T12:31:14Z)

> why we update tasks.tm_output_dataset in postjob instead of in REST/TW.

because the PSET hash to put in there needs to be computed by CMSSW using CMSRun output file, which is best (only) done on the WN, and at this point TW is out of the loop and the guy who processes the job output is the PostJob.

## Comment (belforte, 2023-06-29T12:40:30Z)

> I am not sure if this is proper solution or just workaround. 

IIUC we still have a FakeDataset here, simply a different one for each task. Which is what we require in order to have a different container for each task. So I'd call it a fix .

## Comment (novicecpp, 2023-07-20T08:26:26Z)

- [x] https://github.com/dmwm/CRABServer/issues/7741

## Comment (novicecpp, 2023-11-17T15:28:07Z)

All done.
