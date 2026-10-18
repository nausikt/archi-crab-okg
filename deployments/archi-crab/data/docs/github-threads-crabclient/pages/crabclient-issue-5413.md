# dmwm/CRABClient issue #5413: crab report fails for automatic splitting

State: closed
Opened: 2025-09-16T10:17:43Z
Closed: 2025-10-01T08:13:59Z
Labels: bug, In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5413

## Opening post (belforte, 2025-09-16T10:17:43Z)

A bug was introduced in https://github.com/dmwm/CRABClient/issues/5409

See: https://cms-talk.web.cern.ch/t/failure-on-crab-report-command/131905

Client now fetches runs, lumis, files list from S3, but for automatic splitting those files only contain the ProbeJobs at submit time. The tarballs on the AP are later updated by the various PreDag as processing and tails steps run. But remain local.

There are two possible solutions:

   1) for automatic splitting re-vive old code which wgets tarballs from WEB_DIR
   2) in AP, upload new tarball to S3 whenever a PreDag runs

Solution 2) is sort or "more elegant" but combersome, 1) is ugly but simple
Solution 1)  is a bit slower since for large tasks pulling files from AP is not as efficient as from S3

## Comment (belforte, 2025-09-16T10:18:28Z)

@sinonkt do you want to tackle this as learning step in taking care of CRAB ?

## Comment (nausikt, 2025-09-16T10:19:01Z)

Sure, Stefano

## Comment (nausikt, 2025-09-16T10:19:15Z)

Do we need to rollback first or something?

## Comment (belforte, 2025-09-16T10:21:22Z)

I told the user to do `crab-pre report` which works in this case.

`crab-pre` is there exactly as a "ready rollback". It is not possible to change `crab-prod` "immediately", as you have seen

## Comment (belforte, 2025-09-25T11:36:42Z)

should be fixed by the TW change in https://github.com/dmwm/CRABServer/pull/9190
