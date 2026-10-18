# dmwm/CRABClient issue #5409: make client compatible with new tarball format

State: closed
Opened: 2025-08-11T10:11:54Z
Closed: 2025-08-20T10:02:22Z
Labels: Done
URL: https://github.com/dmwm/CRABClient/issues/5409

## Opening post (belforte, 2025-08-11T10:11:54Z)

with ref to https://github.com/dmwm/CRABServer/issues/8727#issuecomment-3161188761

We are moving to having in `InputFiles.tar.gz` (which is in S3) only two tarballs the JobWrapper one `CMSRunAnalysis.tar.gz` and the TW one `TaskManagerRun.tar.gz`

They need to be expanded appropriately in order to get files like `input_files.tar.gz` and `run_and_lumis.tar.gz` for `crab report` and all the job wrapper top level files for `crab preparelocal`

Will try to do this in a way which is backward compatible and will not require code change once new TW is in place.
