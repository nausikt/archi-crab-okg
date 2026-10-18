# dmwm/CRABServer issue #8699: sort out confusion/duplicates in tarballs handling from TW to sched to Wrapper

State: closed
Opened: 2024-09-18T13:14:07Z
Closed: 2024-10-10T12:54:39Z
Labels: Status: Done, Priority: High, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8699

## Opening post (belforte, 2024-09-18T13:14:07Z)

currently TW sends one file to scheduler: `InputFiles.tar.gz`
   * expanded by `dag_bootstrap_startup.sh`
   * content in [*]
   * contains the two code tarballs
      *   `CMSRunAnalysis.tar.gz`  (which is shipped to WN)
      *  `TaskManagerRun.tar.gz`
   * also contains the user `sandbox.tar.gz`
 

`CMSRunAnalysis.tar.gz` is  expanded by CMSRunAnalysis.sh [1]. It has
  * `WMCore.zip`
  *  CMSRunAnalysis.py, TweakPSet.py and 3 other py file which are likely not needed [2]

`TaskManagerRun.tar.gz` contains  files used by scripts running on the scheduler [4]
  * expanded by `dagBoostrap.sh` [3]
  * contains files which are duplicates of what's in `CMSRunAnalysis.tar.gz` [4]

[*]

annotated content
Action Needed | file | purpose |
-|-|- 
N | gWMS-CMSRunAnalysis.sh | the JobWrapper. `command` to be passed to HTC in the JDL when submitting to global pool
N | submit_env.sh | used by job wrapper
N | CMSRunAnalysis.sh | by job wrapper to unpack `CMSRunAnalysis.tar.gz`
Y | cmscp.py | used by job wrapper (could be moved inside  `CMSRunAnalysis.tar.gz` )
Y | cmscp.sh | used by job wrapper (could be moved inside  `CMSRunAnalysis.tar.gz`)
Y | RunJobs.dag | the DAG to be run for this task. Also send via `transfer_input_files` ? REMOVE ? 
N | Job.submit | template for the JDL when submitting to grid, will be customized in Job.1.submit etc.
N | dag_bootstrap.sh | used inside DAG to setup the env for PreJobs, PostJob, PreDag steps 
N | AdjustSites.py | called by `dag_bootstrap_startup.sh*`
Y | site.ad | list of available sites for each job in classAd format (obsolete ?) manipulated by AdjustSites but never used ? REMOVE ?
Y | site.ad.json | same in JSON format. Used in `PreJob.py`. Not touched in AdjustSites ! SHOULD CHANGE ?
N | datadiscovery.pkl | for automatic splitting 
N | taskinformation.pkl | for automatic splitting
N | taskworkerconfig.pkl | for automatic splitting
N | run_and_lumis.tar.gz | input runs and lumis for each job
N | input_files.tar.gz | input files for each job
Y | debug/ | subdirectory contains the two files below, uploaded by CRABClient to S3. Can remove ?
Y | debug/crabConfig.py | user config file, useful debugging info
Y | debug/originalPSet.py | user PSet file, useful debugging info
Y | debug/<ScriptFileName> | user ScriptExe file (if present), useful debugging info
N | sandbox.tar.gz | the user files, uploaded by CRABClient to S3
Y | CMSRunAnalysis.tar.gz | to be transferred to running job via HTC file transfer mechanism.
Y | TaskManagerRun.tar.gz | 
N | input_dataset_lumis.json | list of lumis in input dataset, for use by `crab report`
Y | input_dataset_duplicate_lumis.json | retrieved by `crab report`, but .... needed ?
N | debug_files.tar.gz | tarball whose contend has been expanded in `debug/` . DUPLICATION
N | input_args.json | to be fetched by CRABClient and used in `preparelocal` 


[1] https://github.com/dmwm/CRABServer/blob/b3b26dbd3c8aa617e6a0e03b6cfe8f23a5fc3c97/scripts/CMSRunAnalysis.sh#L49

[2]
WMCore.zip
TweakPSet.py
CMSRunAnalysis.py
ServerUtilities.py **Not needed**
CMSGroupMapper.py  **Not needed**
RESTInteractions.py  **Not needed**


[3] https://github.com/dmwm/CRABServer/blob/b3b26dbd3c8aa617e6a0e03b6cfe8f23a5fc3c97/scripts/dag_bootstrap.sh#L69

[4]
 
CRAB3.zip
TweakPSet.py  **Not needed**
CMSRunAnalysis.py **Not needed**
task_process/
task_process/CMSRucio.py
task_process/FTS_Transfers.py
task_process/RUCIO_Transfers.py
task_process/cache_status.py
task_process/task_proc_wrapper.sh
ServerUtilities.py
RucioUtils.py
CMSGroupMapper.py
RESTInteractions.py

## Comment (belforte, 2024-09-24T16:01:49Z)

fall out action items
- [x] remove extra files from TaskManagerRun.tar.gz  - #8718
- [x] remove extra files from CMSRunAnalysis.tar.gz - #8718
    - [x] uff. current `cmscp.py` imports `parseJobAd` from ServerUtilities but can use code from CMSRunAnalysislpy instead [1] ! Also there is no `smv2-lcg` any more, not need to check if `gfal-copy` exists - #8718
- [x] move cmscp.* to CMSRunAnalysis.tar.gz  - postponed, maybe part of bigger restruct as per [comment](https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2374495276) below ?
- [x] verify if RunJobs.dag can be removed from InputFiles.tar.gz
   - [x] NO. It can not.
- [x] clarify situation with debug files and possibly remove `debug/` directory from tarball (keep only debug_files.tar.gz) - moved to #8719
- [x] clarify site.ad vs. site.ad.json and cleanup as proper - #8720
- [x] check if `input_dataset_duplicate_lumis.json` is ever useful.
   * It only used in `crab report` to tell user that there is a non-empty list of duplicates and point to it. Could probably avoid writing when it is empty (content=`{}`) but current way allows to distinguish no-duplicates from error-retrieving-from-WEB_DIR

[1] see also https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/ServerUtilities.py#L427-L434

## Comment (belforte, 2024-09-24T19:41:40Z)

**How files make their way to scheduler's SPOOL_DIR and WN**

thiis is what DagmanCreator has
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L1233-L1235
but also
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L692-L694
i.e.
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L726-L731

So the code to create `InputFiles.tar.gz` was possibly created for `preparelocal`, but eventually
 DagmanSubmitter puts this in the `DAGJob.jdl`
```
transfer_input_files = InputFiles.tar.gz, subdag.jdl
```

The way things work is that DagmanCreator returns https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L1255
which gets passed as input to DagmanSubmitter an in there 
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L261
followed by https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L399
and eventually
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L540

that `jobJDL` object is saved in `DAGJob.jdl` file in TW `/data/srv/tmp/_<taskname>` directory
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanSubmitter.py#L543-L544




 

Later on  `cmscp.sh, cmscp.py` make there way to the grid WN  by being placed in scheduler's SPOOL_DIR and then transferred by HTCondor again to the WN via this in `Job.submit`
```text
transfer_input_files = CMSRunAnalysis.sh, cmscp.py, CMSRunAnalysis.tar.gz, sandbox.tar.gz, run_and_lumis.tar.gz, input_files.tar.gz, submit_env.sh, cmscp.sh
```

**pff...what a mess**

## Comment (belforte, 2024-09-25T15:59:38Z)

a more radical solution to "move cmscp.* inside tarball" would be to add two subdirectories in CRABServer/scripts (1)
```text
scripts/
├── dagman
├── job_wrapper
└── task_process
```
or maybe better (2)
```text
scripts
├── dagman
│   └── task_process
└── job_wrapper
```
so that in https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/cicd/crabtaskworker_pypi/buildTWTarballs.sh#L76-L84

we only copy well named directories around, like done now for `task_process`

and also move expanding of job_wrapper tarball
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/CMSRunAnalysis.sh#L49

to the top wrapper script between these lines
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/gWMS-CMSRunAnalysis.sh#L225-L227

@novicecpp I will very much like your opinion

## Comment (belforte, 2024-09-26T10:29:30Z)

about `debug` directory in tarball.
the reason to expand `debug_files.tar.gz` in DagmanCreator is to make the files available to the CRABServerUI
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L1126
so that in the UI they can be fetched from the scheduler [1]
OTOH this could be done in AdjustSites when WEB_DIR is prepared instead of both copying there  `debug_files.tar.gz` and creating a symlink for `debug/` directory
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/AdjustSites.py#L228-L233

And leave for a future optimization to simply put files in S3, like we do for twlog. w/o creating the `debug_files.tar.gz`. That will require changes to `crab recovery` and `crab getsandbox` too, besides of course `task_info.js` where files will be downloaded from S3, not the scheduler.

Having a tar saves on repeated calls to crabserver (to get preapproved url's) and S3 from the client. The idea was that when CRABClient is executed from sites with a large RTT, the fewer http calls, the better.
Maybe do this in the TW ? DagmanCreator could upload the files to S3 instead of adding to `InputFiles.tar.gz`.

Maybe better to settle on the final solution, and do all changes in one go. Avoid putting code there "for a few months" which is hard to remove.

I will move to ad-hoc issue

[1]
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/script/task_info.js#L231-L245

## Comment (belforte, 2024-09-26T14:59:12Z)

**site.ad vs. site.ad.json**

manipulation of `site.ad` in AdjustSites,py is unchanged since Brian's commit in 2013.
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/AdjustSites.py#L481-L487
But I can't find any other place in the code base which references to CRAB_SiteAdUpdate.
Is that code simply "never executed" ?

PreJob uses `site.ad.json` to create site lists `avalaible` (where we can run) and ``datasites` (where data is).
If it does not find it, falls back to `site.ad` to create list of available sites, only, and at first sight it should crash since `datasites` is unconditionally used in following code

There is also this very interesting commit from Brain 10y ago  https://github.com/dmwm/CRABServer/commit/75b85ca950219a823d92121eb231d1d50c2d4a2a which looks like he introduced the JSON, leaving the old code for temporary compatibility (?) and then.. change stuck.

So I am leaning to `site.ad` can be removed.

AFAICT those two files are created by DagmanCreator
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L1089-L1090
Yet I can't be sure nor figure out how they are populated from reading the code. Need to run it step-by-step.

`site.ad.json` contains `siteinfo` structure
`site.ad` contains `sitead` strucutre
those structures are initialized to "empty" in
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L805-L816
(when DagmanCreator runs in TW, there are no files to read)

so in particular we start with
```python
siteinfo = {'group_sites': {}, 'group_datasites': {}}
```
Then DagmanCreator calls createSubdag() which gets the list of data sites and available sites for each job groups (one job group for each set of locations, IIUC)
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L891
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L896
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L910
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L933
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L943-L944
 and calls  makeDagSpecs() where those are added to `siteinfo` dictionary
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L599-L601
(no comment on the what looks like a horrible dirty trick with L599)

My conclusion from the above is that `site.ad` is old, obsolete, useless and can be simply removed.

## Comment (belforte, 2024-09-27T14:56:22Z)

I will close this when #8718 and #8721 are merged.
Will leave further refectoring as per [comment above](https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2374495276) to new issue #8727 and document "tarball movements" as per https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2372227111 to after I have finalized #7461 and #6544  . Now tracked in #8728

## Comment (belforte, 2024-10-10T12:54:39Z)

conditions for closing met :-)
