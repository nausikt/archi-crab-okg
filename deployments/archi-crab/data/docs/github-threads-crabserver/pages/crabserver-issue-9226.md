# dmwm/CRABServer issue #9226: PostJob crashes during automatic splitting

State: closed
Opened: 2025-11-03T11:37:58Z
Closed: 2025-12-05T03:17:07Z
Labels: Type: Bug, Priority: Critical, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9226

## Opening post (belforte, 2025-11-03T11:37:58Z)

see
https://cms-talk.web.cern.ch/t/automatic-file-splitting-issue/136483/3

## Comment (belforte, 2025-11-03T12:04:05Z)

@nausikt I have tentatively assigned to you fixing of this interesting race condition. It is a tricky thing since I do not think that we can systematically reproduce it and it is more a matter of "making code good by design" which hopefully suits a "perfectionist". Of course I will help, but would also try not to bias you and a fresh perspective may actually be good.
Let me know what you think now that argocd is hopefully out of the way.

## Comment (nausikt, 2025-11-03T12:10:07Z)

Thank you Stefano. Acknowledged, that suits me!

## Comment (belforte, 2025-11-05T15:13:52Z)

thanks. My first hypothesis is that PJ tries to open the tar while shutil.copy() is overwriting it. Which sounds difficult to believe. But maybe possible.

## Comment (belforte, 2025-11-05T20:51:34Z)

full traceback from PostJob crash
```text

Sat, 04 Oct 2025 12:18:29 CEST(+0200):ERROR:PostJob Failure during post-job execution.
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/2851/0/cluster132272851.proc0.subproc0/TaskWorker/Actions/PostJob.py", line 1695, in execute
    retval, retmsg = self.execute_internal()
  File "/data/srv/glidecondor/condor_local/spool/2851/0/cluster132272851.proc0.subproc0/TaskWorker/Actions/PostJob.py", line 2033, in execute_internal
    self.saveAutomaticSplittingData()
  File "/data/srv/glidecondor/condor_local/spool/2851/0/cluster132272851.proc0.subproc0/TaskWorker/Actions/PostJob.py", line 1873, in saveAutomaticSplittingData
    f.extract(fn, path=tmpdir)
  File "/usr/lib64/python3.9/tarfile.py", line 2400, in extract
    tarinfo, unfiltered = self._get_extract_tarinfo(
  File "/usr/lib64/python3.9/tarfile.py", line 2414, in _get_extract_tarinfo
    unfiltered = self.getmember(member)
  File "/usr/lib64/python3.9/tarfile.py", line 2025, in getmember
    tarinfo = self._getmember(name.rstrip('/'))
  File "/usr/lib64/python3.9/tarfile.py", line 2804, in _getmember
    members = self.getmembers()
  File "/usr/lib64/python3.9/tarfile.py", line 2036, in getmembers
    self._load()        # all members, we first have to
  File "/usr/lib64/python3.9/tarfile.py", line 2844, in _load
    tarinfo = self.next()
  File "/usr/lib64/python3.9/tarfile.py", line 2749, in next
    self.fileobj.seek(self.offset - 1)
  File "/usr/lib64/python3.9/gzip.py", line 392, in seek
    return self._buffer.seek(offset, whence)
  File "/usr/lib64/python3.9/_compression.py", line 143, in seek
    data = self.read(min(io.DEFAULT_BUFFER_SIZE, offset))
  File "/usr/lib64/python3.9/gzip.py", line 506, in read
    raise EOFError("Compressed file ended before the "
EOFError: Compressed file ended before the end-of-stream marker was reached
Ended TaskManagerBootstrap with code 1
```

so the `EOFError: Compressed file ended before the end-of-stream marker was reached` comes when executing
https://github.com/dmwm/CRABServer/blob/ad2bf834e2614af5e367e9ec5f6d2a79a8852dda/src/python/TaskWorker/Actions/PostJob.py#L1872-L1873

## Comment (belforte, 2025-11-05T21:06:25Z)

@nausikt following up on what we said in the meeting today, you can have a look at the use of the `getLock` context manager in e.g. PostJob and RetryJob

https://github.com/dmwm/CRABServer/blob/ad2bf834e2614af5e367e9ec5f6d2a79a8852dda/src/python/TaskWorker/Actions/PostJob.py#L116
https://github.com/dmwm/CRABServer/blob/ad2bf834e2614af5e367e9ec5f6d2a79a8852dda/src/python/TaskWorker/Actions/PostJob.py#L423
https://github.com/dmwm/CRABServer/blob/ad2bf834e2614af5e367e9ec5f6d2a79a8852dda/src/python/TaskWorker/Actions/RetryJob.py#L498

https://github.com/dmwm/CRABServer/blob/ad2bf834e2614af5e367e9ec5f6d2a79a8852dda/src/python/ServerUtilities.py#L429-L436

## Comment (belforte, 2026-01-21T08:39:25Z)

Eventually we did not do what was initially suggested here but went for a more radical (and simpler) solution which also takes care of potential races between our scripts and HTCondor file transfer. See full discussion in the [PR](https://github.com/dmwm/CRABServer/pull/9233)
