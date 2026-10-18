# dmwm/CRABServer issue #9403: protect against multiple attempts to kill task at same time in PostJob

State: closed
Opened: 2026-08-26T17:30:36Z
Closed: 2026-09-14T12:50:13Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9403

## Opening post (belforte, 2026-08-26T17:30:36Z)

If more postJobs are executing at same time, they may notice "too Many Fatal ASO errors and all try to kill task at same time.
I suspect this is the reason for errors like this in PostJob which makes PJ exit with exit code 9000

```
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob ====== Finished to check for ASO transfers.
Wed, 26 Aug 2026 18:56:59 CEST(+0200):ERROR:PostJob **** Too Many Fatal ASO errors. Abort DAG and kill task ****
Wed, 26 Aug 2026 18:56:59 CEST(+0200):DEBUG:PostJob Killing task 260826_162326:belforte_crab_20260826_182323
Wed, 26 Aug 2026 18:56:59 CEST(+0200):ERROR:RESTInteractions Rejected request when connecting to https://cmsweb-test2.cern.ch:8443/crabserver/dev/workflow using workflow=260826_162326%3Abelforte_crab_20260826_182323&killwarning=Killed+by+CRAB+because+output+can%27t+be+placed+at+destination+site.%0AMake+sure+that+your+destination+site+is+healthy+and%0Athat+you+have+enough+free+disk+space+there+before+submitting+again. Error details: {'content-type': 'text/html;charset=utf-8', 'date': 'Wed, 26 Aug 2026 16:56:59 GMT', 'response-proto': 'HTTP/1.1', 'response-status': '400 Bad Request', 'response-status-code': '400', 'response-time': '68.965005ms', 'response-time-seconds': '0.068965645', 'server': 'CherryPy/18.10.0', 'x-content-type-options': 'bla', 'x-error-detail': 'This request are invalid.', 'x-error-http': '400', 'x-error-id': '6990493c56179cefc91acc6ddcb8e5de', 'x-rest-status': '40001', 'x-rest-time': '67613.125 us', 'content-length': '736'}
Wed, 26 Aug 2026 18:56:59 CEST(+0200):ERROR:PostJob Failure during post-job execution.
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2187, in execute_internal
    ret_code = self.perform_transfers()  # inject to ASO or check ASO status
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2425, in perform_transfers
    raise PermanentStageoutError(msg)
TaskWorker.Actions.PostJob.PermanentStageoutError: Stageout failed with code 1.
There were 1 failed/killed stageout jobs. 1 of those jobs had a permanent failure.
Failure reasons (per document) follow:
- 3ebec05feba4edcd34bcec1eaa429fc2e5065a0d7e804d3786b40fa5:
  -----> ASO log start -----
  ['DESTINATION [1] HTTP 403 : Permission refused [...CUT...] Full log at https://fts3-cms.cern.ch:8449/fts3/ftsmon/#/job/87a3f49e-a16b-11f1-b168-fa163eaa97bf']
  <----- ASO log finish ----
  The last failure reason is permanent.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 1727, in execute
    retval, retmsg, ASOExitCode = self.execute_internal()
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 2226, in execute_internal
    self.killThisTask(killMsg)
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/TaskWorker/Actions/PostJob.py", line 3220, in killThisTask
    self.crabserver.delete(api='workflow', data=encodeRequest(data))
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/RESTInteractions.py", line 260, in delete
    return self.server.delete(uri, data)
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/RESTInteractions.py", line 136, in delete
    return self.makeRequest(uri=uri, data=data, verb='DELETE')
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/CRAB3.zip/RESTInteractions.py", line 168, in makeRequest
    response, datares = self['conn'].request(url, data, encode=True, headers=headers, verb=verb, doseq=True,
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/WMCore.zip/Utils/PortForward.py", line 66, in portMangle
    return callFunc(callObj, newUrl, *args, **kwargs)
  File "/data/srv/glidecondor/condor_local/spool/3387/0/cluster10603387.proc0.subproc0/WMCore.zip/WMCore/Services/pycurl_manager.py", line 353, in request
    raise exc
http.client.HTTPException: url=https://cmsweb-test2.cern.ch:8443/crabserver/dev/workflow, code=400, reason=, headers={'content-type': 'text/html;charset=utf-8', 'date': 'Wed, 26 Aug 2026 16:56:59 GMT', 'response-proto': 'HTTP/1.1', 'response-status': '400 Bad Request', 'response-status-code': '400', 'response-time': '68.965005ms', 'response-time-seconds': '0.068965645', 'server': 'CherryPy/18.10.0', 'x-content-type-options': 'bla', 'x-error-detail': 'This request are invalid.', 'x-error-http': '400', 'x-error-id': '6990493c56179cefc91acc6ddcb8e5de', 'x-rest-status': '40001', 'x-rest-time': '67613.125 us', 'content-length': '736'}, result=b'<!DOCTYPE html PUBLIC\n"-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n<head>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>\n    <title>400 Bad Request</title>\n    <style type="text/css">\n    #powered_by {\n        margin-top: 20px;\n        border-top: 2px solid black;\n        font-style: italic;\n    }\n\n    #traceback {\n        color: red;\n    }\n    </style>\n</head>\n    <body>\n        <h2>400 Bad Request</h2>\n        <p>This request are invalid.</p>\n        <pre id="traceback"></pre>\n    <div id="powered_by">\n      <span>\n        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.10.0</a>\n      </span>\n    </div>\n    </body>\n</html>\n'
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob ====== Starting to prepare error report.
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob Updating error summary for jobid 2 retry 0 with following information:
'exit code' = 90000 ('Post-processing failed')
'exit message' = Failure during post-job execution.
Wed, 26 Aug 2026 18:56:59 CEST(+0200):DEBUG:PostJob Writing error summary file
```

which happend while another PostJob was logging
```
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob ====== Finished to check for ASO transfers.
Wed, 26 Aug 2026 18:56:59 CEST(+0200):ERROR:PostJob **** Too Many Fatal ASO errors. Abort DAG and kill task ****
Wed, 26 Aug 2026 18:56:59 CEST(+0200):DEBUG:PostJob Killing task 260826_162326:belforte_crab_20260826_182323
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob Tag Jobs as ForcefullyTerminated
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob Mail sent to operators about task killing
Wed, 26 Aug 2026 18:56:59 CEST(+0200):INFO:PostJob ====== Starting to prepare error report.
```

## Comment (belforte, 2026-08-28T16:08:34Z)

should add a `kill sent` fiels to `aso_summary.json` and use lock on it
