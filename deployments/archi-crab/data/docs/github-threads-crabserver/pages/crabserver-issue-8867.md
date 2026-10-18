# dmwm/CRABServer issue #8867: fix Rucio quota reporting in ReportRecallQuota

State: closed
Opened: 2024-12-19T12:28:15Z
Closed: 2024-12-19T12:50:54Z
Labels: Type: Bug, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8867

## Opening post (belforte, 2024-12-19T12:28:15Z)

currently it reports wrong value and crashes in the middle with `connection reset by peer` when talking to Rucio

<details>
  <summary>Detail</summary>
```
http://cms-rucio.cern.ch:80 "GET /dids/cms/%2FSuuToChiChiToWBZTToJets_MSuu-5000_MChi-1000_TuneCP5_13TeV-madgraph-pythia8%2FRunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1%2FMINIAODSIM/files HTTP/1.1" 200 None
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 438, in _error_catcher
    yield
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 767, in read_chunked
    chunk = self._handle_chunk(amt)
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 711, in _handle_chunk
    value = self._fp._safe_read(amt)
  File "/usr/local/lib/python3.8/http/client.py", line 613, in _safe_read
    data = self.fp.read(amt)
  File "/usr/local/lib/python3.8/socket.py", line 669, in readinto
    return self._sock.recv_into(b)
ConnectionResetError: [Errno 104] Connection reset by peer

During handling of the above exception, another exception occurred:

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
urllib3.exceptions.ProtocolError: ("Connection broken: ConnectionResetError(104, 'Connection reset by peer')", ConnectionResetError(104, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "ReportRecallQuota.py", line 110, in <module>
    main(logger)
  File "ReportRecallQuota.py", line 88, in main
    report = createQuotaReport(rucioClient=rucioClient, account=account['name'], activity=activity)
  File "ReportRecallQuota.py", line 35, in createQuotaReport
    totalBytes = getRucioUsage(rucioClient=rucioClient,account=account,activity=activity)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 146, in getRucioUsage
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 146, in <genexpr>
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/baseclient.py", line 329, in _load_json_data
    for line in response.iter_lines():
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 804, in iter_lines
    for chunk in self.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode):
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 763, in generate
    raise ChunkedEncodingError(e)
requests.exceptions.ChunkedEncodingError: ("Connection broken: ConnectionResetError(104, 'Connection reset by peer')", ConnectionResetError(104, 'Connection reset by peer'))
```
</details>

After looking with `pdb` and testing things, I conclude that current code does two wrong things:
 * uses `crab_recall` account name for recall activity, while it should be `None`
 * uses `activity` flag for `crab_input` ending up in  a loop on zilion of files which kills the connection to Rucio server with the error above, instead of simply getting used quota by `crab_input` account in one go.
