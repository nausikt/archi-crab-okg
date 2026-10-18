# dmwm/CRABServer pull request #8740: add checkS3Object and verify S3 upload with it

State: closed
Opened: 2024-10-11T20:17:27Z
Closed: 2024-10-18T00:33:11Z
Merged: 2024-10-18T00:33:11Z
URL: https://github.com/dmwm/CRABServer/pull/8740

## Opening post (belforte, 2024-10-11T20:17:27Z)

(no text)

## Comment (cmsdmwmbot, 2024-10-11T20:33:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 85 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2198/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-10-11T21:27:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 85 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2199/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-10-17T00:16:09Z)

:rocket: :rocket: :rocket:

## Comment (belforte, 2024-10-17T09:51:55Z)

I had only tested from client. But uploading of twlog now fails with 
```
 'x-error-info': 'taskname is missing'
```

```
2024-10-17 11:46:45,900:DEBUG:ServerUtilities:upload to S3 of twlog ./logs/tasks/crabint1/241017_084637:crabint1_crab_20241017_104637.log completed
2024-10-17 11:46:45,900:DEBUG:ServerUtilities:make sure that object is ready for retrieve
2024-10-17 11:46:46,943:ERROR:RESTInteractions:Rejected request when connecting to https://cmsweb-test2.cern.ch:8443/crabserver/dev/cache using subresource=download&objecttype=twlog&clientmethod=head_object. Error details: {'content-type': 'text/html;charset=utf-8', 'date': 'Thu, 17 Oct 2024 09:46:46 GMT', 'response-proto': 'HTTP/1.1', 'response-status': '400 Bad Request', 'response-status-code': '400', 'response-time': '15.413685ms', 'response-time-seconds': '0.015414353', 'server': 'CherryPy/18.8.0', 'x-content-type-options': 'bla', 'x-error-detail': 'Missing required parameter', 'x-error-http': '400', 'x-error-id': '4e6d3d37d4501074f907d5e1956b71e1', 'x-error-info': 'taskname is missing', 'x-rest-status': '301', 'x-rest-time': '9303.570 us', 'content-length': '736'}
```

## Comment (novicecpp, 2024-10-17T13:08:41Z)

Ah yes. It is used for S3 path construction. 
- All sandbox are put together inside `<username>/sandboxes/`  => to share across tasks
- and for twlog it use `<username>/<taskname>/twlog`.                => individual task.

## Comment (belforte, 2024-10-17T13:36:30Z)

thanks Wa. No worry. It was my code, I will figure out. I have doing more than one thing at same time atm. gimme a bit to get to this

## Comment (belforte, 2024-10-17T15:45:32Z)

fixed

## Comment (cmsdmwmbot, 2024-10-17T15:50:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 34 comments to review
 * Pycodestyle check: succeeded
   * 85 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2210/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-17T22:07:55Z)

- [x] validation in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8341908
