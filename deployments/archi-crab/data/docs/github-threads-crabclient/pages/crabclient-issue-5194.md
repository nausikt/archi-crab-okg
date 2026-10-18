# dmwm/CRABClient issue #5194: protect against badly specified nThreads in PSet

State: closed
Opened: 2023-04-17T09:03:32Z
Closed: 2023-04-17T09:26:15Z
URL: https://github.com/dmwm/CRABClient/issues/5194

## Opening post (belforte, 2023-04-17T09:03:32Z)

EM framework requires that number of threads in the PSet is indicated as `uint32` but users may mistakenly use `int32` and the resulting pset will still be valid, but only use 1 thread.
See discussion in [MatterMost CPU Efficiency channel](https://mattermost.web.cern.ch/cms-o-and-c/pl/4hckcnwz3pgo7r5a9a9arua11h)

CRABClient need to check that number of threads is correctly indicated before allowing to submit a request for e.g. 8 cores where only 1 will be used.

## Comment (belforte, 2023-04-17T09:04:54Z)

@mmascher  as agreed please make a PR with the check. I can take care of tuning action and message.
