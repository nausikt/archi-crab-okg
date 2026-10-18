# dmwm/CRABServer issue #8719: change how user "debug" files in `debug_files.tar.gz` are handled 

State: closed
Opened: 2024-09-26T11:00:06Z
Closed: 2025-03-03T17:15:10Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8719

## Opening post (belforte, 2024-09-26T11:00:06Z)

currently we put in S3 cache `debug_files.tar.gz` which contains user's config and script exe to help operators debug problems and to create a new task to submit in `crab recovery`

But in order to make those files visible in the UI, we need an URL which points to the text version. We currently do this by placing files in WEB_DIR/debug and fetching via scheduler.

Also for historical reasons the TW sends to the scheduler both the tarball and the explicit files, which is a duplication of content.

Can we do something better, simpler and easier to document and understand ?

Since those files are small, the duplication in sending from TW to scheduler is not a big worry, but confusion and lack of documentation is bad.

## Comment (belforte, 2024-09-26T11:01:34Z)

move my thoughts here from https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2376562701

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


[1]
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/script/task_info.js#L231-L245

## Comment (belforte, 2025-03-03T17:10:49Z)

The above has been (silently ?) done already as part of Dagman* and sandbox handling restructuring.
Situation is:

* CRABClient prepares `debug_files.tar.gz` and uploads it to S3
   * https://github.com/dmwm/CRABClient/blob/bf347bd46487754cc4388af7a8c77a835496df44/src/python/CRABClient/JobType/Analysis.py#L188-L194
* AdjustSites donwloads it from S3 and expands into `WEB_DIR/debug_files`
   *  https://github.com/dmwm/CRABServer/blob/5918264f44561765ae22010ed06945c213e5e2b2/scripts/AdjustSites.py#L433

## Comment (belforte, 2025-03-03T17:15:10Z)

So all was done, and there is nothing more to do
