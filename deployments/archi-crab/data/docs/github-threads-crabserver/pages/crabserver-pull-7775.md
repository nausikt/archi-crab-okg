# dmwm/CRABServer pull request #7775: RUCIO_Transfers.py: read transfer info from file that need to publish and filter out not-to-publish files from publish container

State: closed
Opened: 2023-07-18T17:42:27Z
Closed: 2023-07-20T08:55:19Z
Merged: 2023-07-20T08:55:19Z
URL: https://github.com/dmwm/CRABServer/pull/7775

## Opening post (novicecpp, 2023-07-18T17:42:27Z)

Fix https://github.com/dmwm/CRABServer/issues/7741

## Comment (cmsdmwmbot, 2023-07-18T17:46:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1613/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-07-18T18:03:32Z)

I need to test it before ask Stefano to review.

## Comment (cmsdmwmbot, 2023-07-18T18:04:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1615/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-19T15:53:07Z)

I believe this will work, but hesitate to say "fine" since it looks quite intricated.
Besides what I wrote in comment to the code, I am puzzled that we need another flag.
In Rucio ASO, all files requires transfer, and whether a file should be published or not (i.e. EDM or not) is already part of the file info. Could we simply rely on `outputdatasets.startswith('/FakeDataset` ?

I am trying hard to understand how things work so to get convinced that we can simply set `publish=1` in `transfers.txt. It may requires an "if using Rucio" in the PostJob, but may make things much more readable.

My problem is the usual one, PostJob logic is intricated and I fail to have it clearly in mind while I look at other things.  But this is one reason more to keep `delayed_publicationflag_update` as an internal variable to PostJob.

I know that I approved the original idea of using  `delayed_publicationflag_update` but can not managed to feel good about this.

It is also true that life must go on, so if we do not converge quickly on a better idea, wll have to go for `delayed_publicationflag_update` but should at least add some explanation as comments in the code !

## Comment (novicecpp, 2023-07-20T05:29:04Z)

> I believe this will work, but hesitate to say "fine" since it looks quite intricated. Besides what I wrote in comment to the code, I am puzzled that we need another flag. In Rucio ASO, all files requires transfer, and whether a file should be published or not (i.e. EDM or not) is already part of the file info. Could we simply rely on `outputdatasets.startswith('/FakeDataset` ?

We can set `publish=1` to `transfers.txt`. But, checking it from `outputdatasets.startswith('/FakeDataset` is better.
Nice. Thanks Stefano.

## Comment (cmsdmwmbot, 2023-07-20T06:10:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1625/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-20T08:35:59Z)

> We can set publish=1 to transfers.txt

yes we can, but IIUC only when using Rucio. One day I will have to go through PostJob and document what it does :-(

## Comment (novicecpp, 2023-07-20T08:39:16Z)

We do not use anywhere in FTS_Transfers.py but it is for Publisher to acquire the new files [(ref)](https://github.com/dmwm/CRABServer/blob/2365939e2777e4afa2077f2c6b485b899c1facde/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L32).

## Comment (belforte, 2023-07-20T08:45:21Z)

right. Let's say it correctly:
current PostJob puts in transfers.txt the same `publish` value as it puts in filetransfersdb. We could separate things and use that flag in transfers.txt only to inform RUCIO_Transfers.

Let's keep this as a fall back in case the simple `if FakeDataset` does not work in some case which we have not thought about yet.

## Comment (novicecpp, 2023-07-20T08:55:06Z)

Change PR title to be more accurate with the changes.
