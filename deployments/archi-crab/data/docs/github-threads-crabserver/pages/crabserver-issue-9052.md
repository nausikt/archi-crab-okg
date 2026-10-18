# dmwm/CRABServer issue #9052: put retries around Rucio calls

State: closed
Opened: 2025-04-23T20:26:38Z
Closed: 2025-07-04T12:45:53Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/9052

## Opening post (belforte, 2025-04-23T20:26:38Z)

we get too many of these from TW


(most recent call last):\n  File \"/data/srv/current/lib/python/site-packages/TaskWorker/Worker.py\", line 108, in processWorkerLoop\n    workOutput = work(resthost, dbInstance, WORKER_CONFIG, task, procnum, inputargs)\n  File \"/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py\", line 174, in handleNewTask\n    rucioClient = getNativeRucioClient(config=config, logger=handler.logger)\n  File \"/data/srv/current/lib/python/site-packages/RucioUtils.py\", line 49, in getNativeRucioClient\n    ret = nativeClient.ping()\n  File \"/usr/local/lib/python3.8/site-packages/rucio/client/pingclient.py\", line 44, in ping\n    raise exc_cls(exc_msg)\nrucio.common.exception.RucioException: An unknown exception occurred.\nDetails: no error information passed (http status code: 503)\n"]


Maybe it is enough to protect the client intialization ?

The monitoring scripts like recall quota show instead that in a long loop at some point we get
```

Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 697, in _update_chunk_length
    self.chunk_left = int(line, 16)
ValueError: invalid literal for int() with base 16: b''
[....]
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 760, in generate
    for chunk in self.raw.stream(chunk_size, decode_content=True):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 572, in stream
    for line in self.read_chunked(amt, decode_content=decode_content):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 793, in read_chunked
    self._original_response.close()
  File "/usr/local/lib/python3.8/contextlib.py", line 131, in __exit__
    self.gen.throw(type, value, traceback)
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 455, in _error_catcher
    raise ProtocolError("Connection broken: %r" % e, e)
urllib3.exceptions.ProtocolError: ("Connection broken: InvalidChunkLength(got length b'', 0 bytes read)", InvalidChunkLength(got length b'', 0 bytes read))
```

which may also be a bug in the client, should handle `b''` like a `None` w/o crashing.

Anyhow... we have this since months now, Should do something.

## Comment (belforte, 2025-04-24T13:30:02Z)

when possible I will try to leverage existing TW action retry functionality. e.g. for stageout check
```
2025-04-24 14:27:25,666:INFO:StageoutCheck:Will check stageout at T2_CH_CERN
2025-04-24 14:27:25,666:WARNING:RucioUtils:Try Rucio lfn2pn with operation third_party_copy_write
2025-04-24 14:27:27,441:WARNING:RucioUtils:Rucio lfn2pfn resolution for third_party_copy_write failed with:
An unknown exception occurred.
Details: no error information passed (http status code: 503)
Try next one.
2025-04-24 14:27:27,442:INFO:ServerUtilities:Warning: Failed to delete file 250424115624crabint1crabmaxemory_crab3check.tmp
2025-04-24 14:27:27,443:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 96, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/StageoutCheck.py", line 130, in execute
    pfn = getWritePFN(self.rucioClient, siteName=self.task['tm_asyncdest'], lfn=lfn, operations=['third_party_copy_write'], logger=self.logger)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 95, in getWritePFN
    raise TaskWorkerException(msg)
TaskWorker.WorkerExceptions.TaskWorkerException: lfn2pfn resolution with Rucio failed for site: T2_CH_CERN  LFN: /store/user/crabint1/250424115624crabint1crabmaxemory_crab3check.tmp with exception(s) :
operation: third_party_copy_write, exception: An unknown exception occurred.
Details: no error information passed (http status code: 503)
```

## Comment (belforte, 2025-04-24T14:33:00Z)

OTOH things like `getNativeRucioClient` are used also outside TW. ... better add retries in RucioUtils !

## Comment (belforte, 2025-04-24T14:41:57Z)

Rucio client has internal retries, but backoff is a few seconds, OK for network glitches, but our problem are usually lasting minutes, at least !

## Comment (belforte, 2025-04-24T15:27:56Z)

all in all best approach seems to me to use explicit retry-delay loops around Rucio calls.

I wonder if it is possible to somehow embed that in our general wrapper
https://github.com/dmwm/CRABServer/blob/756a3cac1c0db02e7ef82fe744016c8a629458f3/src/python/RucioUtils.py#L9

and somehow simplify (document ?) its call so that it can be used also outside TW, e.g. in https://github.com/dmwm/CRABServer/blob/master/src/script/Monitor/ReportRecallQuota.py

we have a mix of ways of configuring things like Rucio host and auth_host names, which is not so good, IMHO:
- ` /opt/rucio/etc/rucio.cfg` in schedulers (handled via [Puppet](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/rucio.cfg))
-  `TaskWorkerConfig.py` (and similar for Publisher) 
- `export RUCIO_CONFIG=/cvmfs/cms.cern.ch/rucio/x86_64/slc7/py3/current/etc/rucio.cfg`

@aspiringmind-code may I interest you in this ?

## Comment (aspiringmind-code, 2025-04-28T09:00:14Z)

@belforte Yes, I can take this up.

## Comment (belforte, 2025-04-28T11:49:08Z)

thanks Vijay, feel free to reach out with any questions. I will be happy to talk about this.
