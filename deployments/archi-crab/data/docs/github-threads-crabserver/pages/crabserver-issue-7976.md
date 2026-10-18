# dmwm/CRABServer issue #7976: Rucio ASO with multiple publish container

State: closed
Opened: 2023-10-25T14:37:17Z
Closed: 2023-11-27T17:26:55Z
Labels: RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7976

## Opening post (novicecpp, 2023-10-25T14:37:17Z)

Continue from output files matrix in https://github.com/dmwm/CRABServer/issues/7940#issuecomment-1761356342

It is hard to clear unwanted files from container, something like when users want to gather diagnostics file from worker node (logs/coredump/whatever) and save to destination site, but later want to clear his space and keep only EDM/T files.
Users needs to manually detach files from Rucio dataset using API/CLI, one by one, which is not trivial.

To make it more manageable, we will put files into different publish container separate by file type, `{EDM,TFile,Misc,Logs}`.
Now it easily to use one-liner `rucio delete rule <rule-id>` to delete rule from unwanted container, to free up the space.

## Comment (novicecpp, 2023-10-25T14:57:01Z)

@belforte I am not sure if there is any other advantage to split container just for categorize and delete files in bulk later.

My alternative idea is, if it's only for deleting files, why don't we create yet-another-crab-command to delete files in the container instead? Behind the scenes, Crab detaches files from the container/dataset, so files do not belong to any rules, and then it does not account for quota.
It might not be as easy as it sounds because I do not know how to handle the case where users manually add files to another container and complain later why their files do not get deleted.

## Comment (belforte, 2023-10-25T15:50:08Z)

I was asking for one container for each output file (like multiple EDM or TFile names) so that we can publish in different datasets in DBS, avoiding to mix different data ).
Now.. it is also true that we always had in the design a separate container for logs, and I think the rational was simply "those should not be put in DBS". 
So we should have one container for each "root output file name", and at least one for "files which will never go in DBS". And as you point out, user may produce files which are not `root` format but still containing output to be saved and reprocessed (NN training data ? ascii files ?) and/or files like additional logs.
We want to be general, w/o being overwhelmed by trying to support use case which never came up so fare (core dump eg).

So I propose to stick with:
 - logs are something we add, and we keep doing as now
 -  then there is a list of file names as output files for the job. Each of them should go in a different container collecting all files with same name, differing only by the jobid `name_jobid.type`
 -  CRAB already has in the list file type as EDM, TFile, other (IIUC). We will only push in EDM becasue they have the needed metadata (there's a tricky magic here, because NANO and DQM are not EDM but have FJR and hence metadata so we publish them. I will need to check the code to give precise directions)
 
I would not try to save on container names by putting in the same basket things which require "if data name starts with" in order to be processed later.

## Comment (novicecpp, 2023-10-26T13:42:51Z)

~~`![multiple-publish-container](https://github.com/dmwm/CRABServer/assets/2346664/60f50a00-501c-47ee-a9fe-994a56e08e30)`~~ (Edited: See update version in https://github.com/dmwm/CRABServer/issues/7976#issuecomment-1781337559)

Like this?

> I would not try to save on container names by putting in the same basket things which require "if data name starts with" in order to be processed later.

Sorry, I do not understand this. Could you give me an example?

## Comment (belforte, 2023-10-26T14:37:02Z)

> Like this?

I do not understand, what are e.g. outedm1/2/3 ? There seem to be too many files names there !

> Sorry, I do not understand this. Could you give me an example?

my cmsRun produces 2 EDM files:  allEvents.root and filteredEvents.root
so we have allEvents_1.root, allEvents_2.root etc. one for each job. Same for filteredEvents_1.root etc.
We should put those in two containers: allAvents and filteredEvents (well, need to add more stuff to name to guaranteed uniqueness.. ).
Should not put in same EDM container, because if we do, when later on I try to process allEvents or only the filteredEvents I want to simply use a  different container (which eventually becomes a DBS dataset) . If you put all EDM files in the same container (IIUC the original proposal, of course !!!)  I would need to check file name whan processing (or moving, or deleting...)

maybe we can have a chat ?

## Comment (novicecpp, 2023-10-26T15:18:32Z)

![multiple-publish-container](https://github.com/dmwm/CRABServer/assets/2346664/7e9582ef-6cdd-484c-ac4b-76f0fce908de)

Sorry, it should be this one.

## Comment (belforte, 2023-10-26T19:37:42Z)

Yes, the `.root` file picture is what I had in mind, thanks.
I think you are too pessimistic here by indicating the possibility of tons of different outputs, which I think is why you have introduced the MISC container. In practice I seriously doubt we will ever have more than a handful files. And I'd rather be prepared for odd file types (xml, json, binary) for AI/MachineLearning (looks like any data analysis now a day needs a "deep" component in order to be take seriously. I am not sure where all that NeuralNet training will happen,
Which is why I still like "do not worry about saving on containers" and have a flat approach where every output file ends in its own container (containing all the file_1.x, file_2.x ... file_n.x from jobs 1, 2..n). I have the prejudice that it makes for simpler code since you do not care about "x". CRAB already tells which file is EDM and which is not, i.e. which container should have block info for DBS.

YOur picture will become much simpler too. We need to mark which conatiner needs to go to DBS and which not, that's all. Transfersdb has this info file-by-file btw. And Publisher will ony look at files for which the `to_publish` flag is True.

## Comment (novicecpp, 2023-10-27T12:51:13Z)

> have a flat approach where every output file ends in its own container (containing all the file_1.x, file_2.x ... file_n.x from jobs 1, 2..n).

Ah, I think I finally understand you now. My first thought is stick with file types we have in db `tm_edm_outfiles/tm_outfiles/tm_tfile_outfiles`, and then give each container for each files for EDM and TFile to match use case you described, and anything else go to misc container as seen in https://github.com/dmwm/CRABServer/issues/7976#issuecomment-1781337559.
But, give each output files a container is indeed simpler.  

> `YOur picture will become much simpler too` 

Sorry, maybe not, hahaha. But it easier to understand. Here the latest version with DBS server in picture:

![multiple-publish-container-with-publisher](https://github.com/dmwm/CRABServer/assets/2346664/4a239572-af43-4a60-b774-7ecc2f6355b9)

## Comment (belforte, 2023-10-27T19:53:24Z)

> Sorry, maybe not, hahaha. 

that's a PlantUml shortcoming !

Maybe you can simply make a list of containers and in each (`file_1.x`, `file_2.x` ...) it sort of goes w/o saying that `file_N.x` comes from job `N`
Then some containers can have an arrow pointing to DBS
 
Let's stick to text !

All files which onl differ by job_id number go into same container. All containers are xferred. For each container ASO look at one file (is enough) to check if publsh flag is set, if so , ASO fills in blockname and blockcomplete in transfersdb.

ASO had no need to know about EDM, Tfile, logs... all files are the same. Decision on what to put in DBS and what not is done elsewhere.  All output files declared to CRAB will be tracked in Rucio containers. Logs become output when user sets `config.General.transferLogs = True`

## Comment (novicecpp, 2023-11-02T13:30:43Z)

ASO code is done and work as expect.
![Screenshot from 2023-11-02 14-22-42](https://github.com/dmwm/CRABServer/assets/2346664/a4c6ed46-e819-4b11-810a-8dbcffa5ba73)

Each Publish Container will have `__<filename>` append to container "name" section. It is human-readable and easy to parse to match file to the container.

On thing I did not know how to do it yet is how do we display all container name and its rules to users. 
For the client part, maybe add `--print-publish-name` opts in `crab status`.?
For the server part, put it in new clob column in taskdb and store kv of container name and the rule id?

## Comment (belforte, 2023-11-02T13:41:30Z)

hmm.. so many years that we support a single dataset that I do not remember the conventions that we were using, which somehow allowed to track multiple datasets with current DB columns.
Let's start by looking at https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling and see if the outputdataset tag is sufficient info. In case I agree that a kv list is the cleanest way.

## Comment (novicecpp, 2023-11-02T16:22:25Z)

Thanks for pointer. Found it in https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Output_dataset_names_in_DBS

In summary, if we have multiple EDM outputs, `module_label` (IIUC, attritbute name of output in PSet.py) will add in front of PSet hash.  See [job_fjr.6.0.json](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231102_121313:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20231102_131304/SPOOL_DIR/job_fjr.6.0.json) from HC-1kj PSet as example.
E.g., `'/GenericTTbar/tseethon-ruciotransfers-1698927184-94ba0e06145abd65ccb1d21786dc7e1d/USER'` with `allevents` and `filteredevents` will become:
- `/GenericTTbar/tseethon-ruciotransfers-1698927184-allevents-94ba0e06145abd65ccb1d21786dc7e1d/USER`
- `/GenericTTbar/tseethon-ruciotransfers-1698927184-filteredevents-94ba0e06145abd65ccb1d21786dc7e1d/USER`

However, `module_label` are only available in EDM files. It pass down to ASO in `outputdataset` form *IF* multiple EDM are allowed.
https://github.com/dmwm/CRABServer/blob/9cb5d51245477e0bfa68fd2fc14931a620f7df15/src/python/TaskWorker/Actions/PostJob.py#L2738-L2762

EDITED: fix output dataset name (epoch string `1698927184` is part of `OutputDatasetTag`)

## Comment (novicecpp, 2023-11-02T16:34:48Z)

I am inclined to avoid using the old format unless we are planning to bring back the multiple output dataset's feature in the future.

The container rule IDs is what I want to store in TaskDB. It is hard differentiate if the rule is created by ASO when we look up from container name.

## Comment (belforte, 2023-11-02T18:57:44Z)

> However, module_label are only available in EDM files. 

But we only publish in DBS EDM files. Well... we also publish NANO and DQM now, but I do not remember how exactly that was handled, if by pretending those are EDM or what.

I think the module label should be available for both EDM and TFile, since those are from cmsRun output processed. Of course files produced via `cout` or by scripts or by direct calls to Root w/o using CMSSW class... we only have the file name.

I am not sure what is wrong with sticking with the format `/GenericTTbar/tseethon-ruciotransfers-filteredevents-1698927184-94ba0e06145abd65ccb1d21786dc7e1d/USER` replacing `filteredevents` with the filename for "misc" files.

All in all container name needs to have the format /a/b/USER . I guess we can have a chat tomorrow ? I suspect I am missing something here !

## Comment (novicecpp, 2023-11-03T12:56:41Z)

> I am not sure what is wrong with sticking with the format /GenericTTbar/tseethon-ruciotransfers-filteredevents-1698927184-94ba0e06145abd65ccb1d21786dc7e1d/USER replacing filteredevents with the filename for "misc" files.

Extra code in ASO (mapping between filename and module_label). 
I am not against it or anything. I just  like my proposal more because it makes it clear which container it belongs to when looking at the filename.

## Comment (belforte, 2023-11-03T13:36:11Z)

I am all for less code and clear names. I think it is better that you go ahead with this and we will see how it works in practice and only discuss changes in front of specific examples.
Thanks

## Comment (novicecpp, 2023-11-06T17:54:44Z)

Thanks to @mapellidario  from pointing out the length of container name.
AFAIK, DBS dataset is restrict to [this regexp](https://github.com/dmwm/WMCore/blob/0ce55b30227164197b081d832fd101c72b209e80/src/python/WMCore/Lexicon.py#L205C1-L205C78), around 350 chars, and (sort of) infinite for Rucio container name.

Maybe good idea to put the validation in the REST side.

## Comment (belforte, 2023-11-06T22:34:52Z)

I thought that we already validate in the REST dataset names which can possibly to to DBS. Was something changed ?
Things like "task container" used for transferring from temp to destination can be named at will.

## Comment (novicecpp, 2023-11-07T17:28:46Z)

Nothing change. I want to prevent the case where users have maximum limit of dataset name and have longggggg file name, and check if it can break our system somehow.

It is not that important, we can fix it later. Just take a note here.

PS. Rahul said there is no check in CMSRucio but database have 500 characters length limit.

## Comment (novicecpp, 2023-11-10T19:04:54Z)

In the [PR here](https://github.com/dmwm/CRABServer/pull/7997), I completely forgot about the Publisher part where it expects the DBS dataset name in `filetransferdb.tm_dbs_blockname` field to be the same as `tasks.tm_output_dataset`.

And we should keep name consistency like Production does, where *Rucio container name is DBS Dataset name*.

@belforte I would like to propose
- If it is EDM file with `tm_publication` is `true`,
  - Rucio container name is `tm_output_dataset`. This relies on 2 assumptions:
    - We do not have a plan to re-enable "publish multiple dataset from single crab task".
    - The `outputdataset` from PostJob always the `tm_output_dataset` for EDM files, not `/FakeDataset`.
- Else, EDM file with `tm_publication` is `false`, TFile, and Misc, Rucio container name will have the format I propose above, e.g., `/a/b_mytfile.root/USER`.

Pros:
- Code in the current PR does not change much, and code to detect EDM files already in [master](https://github.com/dmwm/CRABServer/blob/73db7465fddc22dfd8c05b4593ac6f690200a29d/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L159-L176) (code left from the previous version before we decide to put everything inside single publish container). 
- No magic of mapping Rucio dataset name and DBS block name.

Cons:
- Does not support "Publish multiple dataset from single crab task" at all. That means many code change are needed if want to do.

## Comment (belforte, 2023-11-10T20:13:33Z)

I do not really understand this argument. I guess I need an example task with two output EDM datasets. And to think about it for a couple of days myself too !
According to very old documentation CRAB automatically generate distinct dataset names in case of multiple output files. Maybe that was lost in some PostJob changes ? So that info is not present in the `tranfers.txt` file?

If that's the case, surely I have been sloppy in suggesting that this was easy.
But I do not understand why FakeDataset comes in play for EDM data.

I would say:
- let's make it work in the simple use case
- review the design top-bottom of how names are handled
- take decisions once we fully understand

BTW, latest TW indeed fails to submit because TW does not have the permission to check my Rucio quota :-(

## Comment (novicecpp, 2023-11-14T17:02:49Z)

Let's start with the updated version of the output dataset table (see the original version [here](https://github.com/dmwm/CRABServer/issues/7940#issuecomment-1761356342)) [1]:

| case | output edm | output tfile | output misc | publication | output dataset name | note                                                                             |
|------|------------|--------------|-------------|-------------|---------------------|----------------------------------------------------------------------------------|
| 1    | x          |              |             | T           | /GenericTTBar       |                                                                                  |
| 2    |            | x            | (x)         | T           |                     | fail in crab submit, `tm_publication` is `T` but no file to be publish           |
| 3    | x          |              | x           | T           | /GenericTTBar       | Success, but only publish edm                                                    |
| 4    | \>1        |              |             | T           |                     | fail in crab submit, not support multiple output dataset (deprecated feature)    |
| 5    | x          |              |             | F           | /GenericTTBar        |                                                                                  |
| 6    |            | x            | (x)         | F           | /FakeDataset        |                                                                                  |
| 7    | x          |              | x           | F           | /GenericTTBar       |                                                                                  |
| 8    | \>1        |              |             | F           | /GenericTTBar       | the output dataset will have `module_name` in it but only one output dataset [2] |

[1] This table only applies to `crabConfig` that has `outputDataset` tag.
[2] e.g., `/GenericTTbar/tseethon-ruciotransfer-1699972252-testout-94ba0e06145abd65ccb1d21786dc7e1d/USER`

-----------------------

This section of code determines what the `tm_ouput_dataset` should be:
https://github.com/dmwm/CRABServer/blob/73db7465fddc22dfd8c05b4593ac6f690200a29d/src/python/TaskWorker/Actions/PostJob.py#L2750-L2767

Basically, if your task has EDM file(s) in output, `tm_ouput_dataset` is always the real dataset name, not the `/FakeDataset`.

Complicated stuff is "case 8". When you have more than 1 EDM output, PostJob will append the `module_label` after OutputDatasetTag but before pset hash [2], in `compute_outputdataset_name()`:
https://github.com/dmwm/CRABServer/blob/73db7465fddc22dfd8c05b4593ac6f690200a29d/src/python/TaskWorker/Actions/PostJob.py#L148-L177

Which still works the same way as written in https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Output_dataset_names_in_DBS

The trickiest part of "case 8" is how PostJob save the dataset name in `tm_output_dataset`.
Well, it is actually a single line of code, in [line 2767](https://github.com/dmwm/CRABServer/blob/73db7465fddc22dfd8c05b4593ac6f690200a29d/src/python/TaskWorker/Actions/PostJob.py#L2767).
This means that only **last** `outdataset` from the previous loop gets assigned to `self.output_dataset`, and updated to REST in [line 2037-2046](https://github.com/dmwm/CRABServer/blob/73db7465fddc22dfd8c05b4593ac6f690200a29d/src/python/TaskWorker/Actions/PostJob.py#L2037-L2046)
"**last** `outdataset`" here is the last key of `FJR['steps','cmsRun','output']` (Keys are the filename with striped extension) which gets sorted by `json.load()` in alphabetical order somehow (I counld not find any reference why it gets sorted like that but I have tested in cc7-python3.6 and it is always sorted).

----------------------

About how PostJob.py pass this information to ASO, I will not dive into PostJob.py code. But it can be summarized as follows:


- Each file gets its own `outdataset` as `outputdataset` in `transfers.txt`, where:
    - If the file is EDM, the real dataset name is used (computed by `compute_outputdataset_name()`.
    - Else, `/FakeDataset` is used.
- The order of transfer dict is as explain in *last outdataset* above.

See example of [transfers.txt](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231114_160228:tseethon_crab_rucio_transfers_manyedm_withnonedm_test12_20231114_170227/SPOOL_DIR/task_process/transfers.txt) where the task has 2 edm files and single misc file.
You can compare with [another transfers.txt](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231102_121313:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20231102_131304/SPOOL_DIR/task_process/transfers.txt) where the task has single edm files and single misc file.

those two files are uploaded here as well
[2-edm-transfers.txt](https://github.com/dmwm/CRABServer/files/13413324/2-edm-transfers.txt)
[1-edm-transfers.txt](https://github.com/dmwm/CRABServer/files/13413326/1-edm-transfers.txt)

## Comment (novicecpp, 2023-11-14T17:22:55Z)

Well, I kinda agree with your original suggestion in https://github.com/dmwm/CRABServer/issues/7976#issuecomment-1791369055 .
It will add a bit of code to ASO, but keep consistency between the Rucio container name and Dataset name.

## Comment (belforte, 2023-11-14T17:26:52Z)

I really some time to go through this sorry. I want to get corrupted files out of the way first. And hopefully no distractions from user complains
Is this a cherry on top of the cake (support for multiple datasets) ? Or am I standing in the way of progress in fundamentals ?

## Comment (novicecpp, 2023-11-14T18:08:59Z)

Later. 

"support for multiple Publish Container" is our new fundamental.

The requirement is to make it work with Publisher, which means the Rucio Container name that stores EDM file must be the same as the DBS dataset name [1], for task that have single EDM output.
Rucio Container name for multiple edm task and container name of non-edm files are the cherry on top. It can wait.

[1] I am not 100% sure because I have not read Publisher code yet. It would be great if you could provide a pointer to the code where filetransfersdb.tm_dbs_blockname is used.

## Comment (novicecpp, 2023-11-14T18:14:10Z)

No rush though. 
I still have "Rucio ASO cleanup temp" and pypi in todo list :)

## Comment (novicecpp, 2023-11-20T17:14:26Z)

After a private discussion with @belforte, we came to this conclusion:
- If `publication==False`, `tm_output_dataset` will be`/FakeDataset`, else `/GenericTTbar`.
- container name of non-EDM files and "EDM files with `publication==False`" will be `/FakeDataset/`with append of file name to ProcessedDataset part.

**Example 1**
The inputs:
- output files:
  - output.root (EDM)
  - myfile.txt (misc) 
- output dataset (from `compute_outputdataset_name()`): `/GenericTTbar/tseethon-ruciotransfer-1699972252-testout-94ba0e06145abd65ccb1d21786dc7e1d/USER/`
- `tm_publication==True`

The outputs should be:

- `tm_output_dataset`: `/GenericTTbar/tseethon-ruciotransfer-1699972252-94ba0e06145abd65ccb1d21786dc7e1d/USER/`
- Rucio container name:
  - output.root: `/GenericTTbar/tseethon-ruciotransfer-1699972252-94ba0e06145abd65ccb1d21786dc7e1d/USER/`
  - myfile.txt: `/FakeDataset/fakefile-FakePublish-09b5e9b8cf72d5f9068ec96fa4158a96_myfile.txt/USER`

**Example 2**
The inputs are same as "example 1" except:
- `tm_publication==False`

The outputs should be:
- `tm_output_dataset`: `/FakeDataset/fakefile-FakePublish-09b5e9b8cf72d5f9068ec96fa4158a96/USER`
- Rucio container name:
  - output.root: `/FakeDataset/fakefile-FakePublish-09b5e9b8cf72d5f9068ec96fa4158a96_output.root/USER`
  - myfile.txt: `/FakeDataset/fakefile-FakePublish-09b5e9b8cf72d5f9068ec96fa4158a96_myfile.txt/USER`
