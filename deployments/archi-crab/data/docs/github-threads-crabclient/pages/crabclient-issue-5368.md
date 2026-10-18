# dmwm/CRABClient issue #5368: crab report should get tarballs from S3, not WEB_DIR

State: closed
Opened: 2024-12-18T11:22:10Z
Closed: 2025-07-07T12:48:05Z
Labels: enhancement, Done, CleanUp
URL: https://github.com/dmwm/CRABClient/issues/5368

## Opening post (belforte, 2024-12-18T11:22:10Z)

report uses `run_and_lumis.tar.gz` and `input_files.tar.gz` which are now available inside `InputFiles.tar.gz` in S3.
As done already in `crab preparelocal`
