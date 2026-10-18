# dmwm/CRABServer issue #8382: bug in fix for failed migrations

State: closed
Opened: 2024-05-08T11:01:48Z
Closed: 2024-05-08T17:07:07Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8382

## Opening post (belforte, 2024-05-08T11:01:48Z)

the fix for #8378 does not work
```
2024-05-08 12:55:21,942:INFO: Submiting migration request for block /ZeroBias/Run2023D-22Sep2023_v1-v1/MINIAOD#af3a80c5-7980-46f1-b8da-56e9dfaa1ccd ...
2024-05-08 12:55:22,374:ERROR: Exception raised inside migrateByBlockDBS3
'messsage'
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: Bad Request

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/Publisher/PublisherDbsUtils.py", line 414, in requestBlockMigration
    result = migrateApi.submitMigration(data)
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 1834, in submitMigration
    return self.__callServer("submit", data=migrationObj, callmethod='POST')
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 477, in __callServer
    self.__parseForException(http_error)
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/data/srv/TaskManager/v3.240423-5d4408d23c05f23b6dadb69059696d8c/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 522, in __parseForException
    raise HTTPError(http_error.url, data['exception'], data['message'], http_error.header, http_error.body, serverCode(data))
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: DBSError Code:125 Description:DBS Migration error Function:dbs.migrate.SubmitMigration Message:Migration request /ZeroBias/Run2023D-22Sep2023_v1-v1/MINIAOD#af3a80c5-7980-46f1-b8da-56e9dfaa1ccd, id=0 Error: migration request /ZeroBias/Run2023D-22Sep2023_v1-v1/MINIAOD#af3a80c5-7980-46f1-b8da-56e9dfaa1ccd is already exist in DB with id=4417308

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/Publisher/TaskPublish.py", line 197, in publishInDBS3
    statusCode, failureMsg = migrateByBlockDBS3(taskname, migrateApi, destReadApi, sourceApi,
  File "/data/repos/CRABServer/src/python/Publisher/PublisherDbsUtils.py", line 310, in migrateByBlockDBS3
    ok = requestBlockMigration(taskname, migrateApi, sourceApi, block)
  File "/data/repos/CRABServer/src/python/Publisher/PublisherDbsUtils.py", line 429, in requestBlockMigration
    message = body[0,'error','messsage']
KeyError: 'messsage'
2024-05-08 12:55:22,376:INFO: Exception raised inside migrateByBlockDBS3 Not publishing any files.
[crab3@crab-preprod-tw01 Publisher]$ 
```
