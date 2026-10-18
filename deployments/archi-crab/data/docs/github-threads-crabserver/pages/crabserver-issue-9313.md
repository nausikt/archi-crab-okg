# dmwm/CRABServer issue #9313: use gzip option when communicating with DBS

State: closed
Opened: 2026-05-12T14:23:35Z
Closed: 2026-06-22T09:36:08Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9313

## Opening post (belforte, 2026-05-12T14:23:35Z)

On 12/05/2026 13:47, Valentin Y Kuznetsov wrote:
> Stefano,
> thanks for follow up with this as I think we didn't propagate proper message
> across all relevant parties. Please make necessary adjustments to CRAB calls
> to reduce network traffic. And, according to DBS3Reader wrapper in WMCore
> [1] we do not useGzip option.
> Best,
> Valentin.
>
> [1] https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/Services/DBS/DBS3Reader.py#L92
>
> On  0, Stefano Belforte <stefano.belforte@cern.ch> wrote:
>> Hi,
>>
>> I was looking at DBSClient code (sorry for being nosy) and noticed the
>> useGzip option which I was not aware of (sorry, it is new I guess and nobody
>> told me...)
>>
>> https://github.com/dmwm/DBSClient/blob/1e6acbd55c55497cf747a2a0cf4539936138a04a/src/python/dbs/apis/dbsClient.py#L401
>>
>> should I set this to "lighten" CRAB calls ? Both when retrieving lumi lists
>> and mostly when inserting blocks ?
>>
>> CRAB's Publisher calls DBSClient directly, so it will be easy to change,
>> but CRAB's data discovery goes via WMCore's DBSReader wrapper,
>> does the DBSReader enforce gzip already, or is there an additional argument
>> to do so ?
>>
>>
>> Thanks
>>
>> Stefano
>>
>

## Comment (belforte, 2026-05-12T14:24:34Z)

this is particularly important for Publisher when it sends (large) blocks to DBS as JSON

## Comment (belforte, 2026-06-18T17:31:28Z)

This is done for Publisher in #9314 
But when I tried to do it in data discovery step [1], to speed up retrieval of blocks/files/lumis lists, I got a fatal sever error [2]. I stepped in with `pdb` and verified that the data is passed in zipped format by the client in the POST query. Maybe that's wrong ? But this is code inside `WMCore/DBS3Reader/ getFileListByDataset` when it calls DBS's API `listFileArray`.   How can this work in WMA ?
Note that gzipping of the POST data field happens inside DBSClient
https://github.com/dmwm/DBSClient/blob/1e6acbd55c55497cf747a2a0cf4539936138a04a/src/python/dbs/apis/dbsClient.py#L466-L470
Yet the server complains about "unable to decode HTTP post payload" [2]


[1] changed
https://github.com/dmwm/CRABServer/blob/1858c33b7adc155b77a67877b6f7a42baa1c2cd3/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L190
to
```python
 self.dbs = DBSReader(dbsurl, useGzip=True)
```


[2]
```text
HTTP Error 500: DBSError Code:115 Description:DBS decode record failure, e.g. mailformed JSON Function:web.parsePayload Message:unable to decode HTTP post payload Error: EOF
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 500: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py", line 191, in executeInternal
    self.dbs = DBSReader(dbsurl, useGzip=True)
  File "/data/repos/WMCore/src/python/WMCore/Services/DBS/DBS3Reader.py", line 312, in listDatasetFileDetails
    fileDetails = self.getFileListByDataset(dataset=datasetPath, validFileOnly=validFileOnly, detail=True)
  File "/data/repos/WMCore/src/python/WMCore/Services/DBS/DBS3Reader.py", line 780, in getFileListByDataset
    fileList = self.dbs.listFileArray(dataset=dataset, validFileOnly=validFileOnly, detail=detail)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 1607, in listFileArray
    return self.__callServer("fileArray", data=kwargs, callmethod="POST")
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 477, in __callServer
    self.__parseForException(http_error)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 522, in __parseForException
    raise HTTPError(http_error.url, data['exception'], data['message'], http_error.header, http_error.body, serverCode(data))
```

## Comment (belforte, 2026-06-18T17:34:49Z)

I am not sure whether it is worth pursuing this with the DBS developers, or simply leaving TaskWorker as it is.

## Comment (belforte, 2026-06-20T15:51:52Z)

here's the error with `debug=True` option for DBSApi, so it show what exact query it is making
```text
-> filedetails = self.dbs.listDatasetFileDetails(inputDataset, getParents=True, getLumis=needLumiInfo, validFileOnly=0)
(Pdb) n
HTTP=POST URL=https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader method=fileArray params={} data=b'\x1f\x8b\x08\x00V\xb66j\x02\xff\xabVJI,I,N-Q\xb2RP\xd2wO\xcdK-\xcaL\x0e\tIJ,\xd2\xf7p\xd6u\xf6\r\x0e\x0e\x8f\xb7\x8c7\x8a7\x8b\xb74\x8c\x88\xcfM\x0e*\xcd3\x8c/JM\xcc\xc9,.\xc9L\x8e/3\xd2-3\xd2w\xf4w\t\xf6\xf4U\xd2QP*\x03J\xa4\xb8e\xe6\xa4\xfa\xe7\xe5T\x02\x8d4\x00\x8a\xa5\xa4\x96$f\xe6\x009%E\xa5\xa9\xb5\x00#)\x963q\x00\x00\x00' headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'UserID': 'crab3@crab-dev-tw01.cern.ch', 'User-Agent': 'DBSClient/Unknown/', 'Content-Encoding': 'gzip'}
DBS Server error: [{'error': {'reason': 'EOF', 'message': 'unable to decode HTTP post payload', 'function': 'web.parsePayload', 'code': 115, 'stacktrace': '\ngoroutine 145335317389 [running]:\ngithub.com/dmwm/dbs2go/dbs.Error({0xb2bc20?, 0xe792b0?}, 0x73, {0xa543c1, 0x22}, {0xa428b3, 0x10})\n\t/go/src/github.com/vkuznet/dbs2go/dbs/errors.go:185 +0x99\ngithub.com/dmwm/dbs2go/web.parsePayload(0x9f4380?)\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:372 +0x29a\ngithub.com/dmwm/dbs2go/web.DBSPostHandler({0xb2f790, 0xc000012c78}, 0xc00083b320, {0xa3d3e5, 0x9})\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:532 +0xad3\ngithub.com/dmwm/dbs2go/web.FileArrayHandler({0xb2f790?, 0xc000012c78?}, 0xc000837290?)\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:959 +0x29\nnet/http.HandlerFunc.ServeHTTP(0x0?, {0xb2f790?, 0xc000012c78?}, 0x11?)\n\t/usr/local/go/src/net/http/server.go:2171 +0x29\ngithub.com/dmwm/dbs2go/web.limitMiddleware.func1({0xb2f790?, 0xc000012c78?}, 0xc0004dd570?)\n\t/go/src/github.com/vkuznet/dbs2go/web/middlewares.go:110 +0x32\nnet/http.HandlerFunc.ServeHTTP(0xc0008441b0?, {0xb2f790?, 0xc000012c78?}, 0xc000b29220?)\n\t/usr/local/go/src/net/http/server.go:2171 +'}, 'http': {'method': 'POST', 'code': 500, 'timestamp': '2026-06-20 15:48:38.970256357 +0000 UTC m=+3490491.416838383', 'path': '/dbs/prod/global/DBSReader/fileArray', 'user_agent': 'DBSClient/Unknown/', 'x_forwarded_host': 'dbs-prod2.cern.ch', 'x_forwarded_for': '188.185.14.65', 'remote_addr': '10.100.164.0:55294'}, 'exception': 500, 'type': 'HTTPError', 'message': 'DBSError Code:115 Description:DBS decode record failure, e.g. mailformed JSON Function:web.parsePayload Message:unable to decode HTTP post payload Error: EOF'}]
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 500: DBSError Code:115 Description:DBS decode record failure, e.g. mailformed JSON Function:web.parsePayload Message:unable to decode HTTP post payload Error: EOF
> /data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py(424)executeInternal()
-> filedetails = self.dbs.listDatasetFileDetails(inputDataset, getParents=True, getLumis=needLumiInfo, validFileOnly=0)
(Pdb) 
```

same w/o formatting, somehow easier to read

-> filedetails = self.dbs.listDatasetFileDetails(inputDataset, getParents=True, getLumis=needLumiInfo, validFileOnly=0)
(Pdb) n
HTTP=POST URL=https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader method=fileArray params={} data=b'\x1f\x8b\x08\x00V\xb66j\x02\xff\xabVJI,I,N-Q\xb2RP\xd2wO\xcdK-\xcaL\x0e\tIJ,\xd2\xf7p\xd6u\xf6\r\x0e\x0e\x8f\xb7\x8c7\x8a7\x8b\xb74\x8c\x88\xcfM\x0e*\xcd3\x8c/JM\xcc\xc9,.\xc9L\x8e/3\xd2-3\xd2w\xf4w\t\xf6\xf4U\xd2QP*\x03J\xa4\xb8e\xe6\xa4\xfa\xe7\xe5T\x02\x8d4\x00\x8a\xa5\xa4\x96$f\xe6\x009%E\xa5\xa9\xb5\x00#)\x963q\x00\x00\x00' headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'UserID': 'crab3@crab-dev-tw01.cern.ch', 'User-Agent': 'DBSClient/Unknown/', 'Content-Encoding': 'gzip'}
DBS Server error: [{'error': {'reason': 'EOF', 'message': 'unable to decode HTTP post payload', 'function': 'web.parsePayload', 'code': 115, 'stacktrace': '\ngoroutine 145335317389 [running]:\ngithub.com/dmwm/dbs2go/dbs.Error({0xb2bc20?, 0xe792b0?}, 0x73, {0xa543c1, 0x22}, {0xa428b3, 0x10})\n\t/go/src/github.com/vkuznet/dbs2go/dbs/errors.go:185 +0x99\ngithub.com/dmwm/dbs2go/web.parsePayload(0x9f4380?)\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:372 +0x29a\ngithub.com/dmwm/dbs2go/web.DBSPostHandler({0xb2f790, 0xc000012c78}, 0xc00083b320, {0xa3d3e5, 0x9})\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:532 +0xad3\ngithub.com/dmwm/dbs2go/web.FileArrayHandler({0xb2f790?, 0xc000012c78?}, 0xc000837290?)\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:959 +0x29\nnet/http.HandlerFunc.ServeHTTP(0x0?, {0xb2f790?, 0xc000012c78?}, 0x11?)\n\t/usr/local/go/src/net/http/server.go:2171 +0x29\ngithub.com/dmwm/dbs2go/web.limitMiddleware.func1({0xb2f790?, 0xc000012c78?}, 0xc0004dd570?)\n\t/go/src/github.com/vkuznet/dbs2go/web/middlewares.go:110 +0x32\nnet/http.HandlerFunc.ServeHTTP(0xc0008441b0?, {0xb2f790?, 0xc000012c78?}, 0xc000b29220?)\n\t/usr/local/go/src/net/http/server.go:2171 +'}, 'http': {'method': 'POST', 'code': 500, 'timestamp': '2026-06-20 15:48:38.970256357 +0000 UTC m=+3490491.416838383', 'path': '/dbs/prod/global/DBSReader/fileArray', 'user_agent': 'DBSClient/Unknown/', 'x_forwarded_host': 'dbs-prod2.cern.ch', 'x_forwarded_for': '188.185.14.65', 'remote_addr': '10.100.164.0:55294'}, 'exception': 500, 'type': 'HTTPError', 'message': 'DBSError Code:115 Description:DBS decode record failure, e.g. mailformed JSON Function:web.parsePayload Message:unable to decode HTTP post payload Error: EOF'}]
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 500: DBSError Code:115 Description:DBS decode record failure, e.g. mailformed JSON Function:web.parsePayload Message:unable to decode HTTP post payload Error: EOF
> /data/repos/CRABServer/src/python/TaskWorker/Actions/DBSDataDiscovery.py(424)executeInternal()
-> filedetails = self.dbs.listDatasetFileDetails(inputDataset, getParents=True, getLumis=needLumiInfo, validFileOnly=0)
(Pdb)

## Comment (belforte, 2026-06-20T15:59:37Z)

I tried to reproduce the problem with DBS using a direct `curl`, but I could not make it work with gzip ad reported it https://github.com/dmwm/dbs2go/issues/155

I do not know what else to do

## Comment (vkuznet, 2026-06-20T18:15:38Z)

@stefano, when you asking to gzip do you meant to use it for passed payload or for returning results? That said, here is correct way to ask curl to provide gzip encoded output from DBS API:
```
scurl -v --compressed -X POST -H "Content-Type: application/json" -H "Accept: application/json" --data '{"dataset": "/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM", "validFileOnly": 0, "detail": false}'   "https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader/fileArray"
```
You need to provide `--compressed` option which will instruct server to put its output in gzip encoding and curl will decompress it. To verify that you can see its verbose output:
```
* [HTTP/2] [1] OPENED stream for https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader/fileArray
* [HTTP/2] [1] [:method: POST]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: cmsweb-prod.cern.ch:8443]
* [HTTP/2] [1] [:path: /dbs/prod/global/DBSReader/fileArray]
* [HTTP/2] [1] [user-agent: curl/8.20.0]
* [HTTP/2] [1] [accept-encoding: deflate, gzip, br, zstd]
* [HTTP/2] [1] [content-type: application/json]
* [HTTP/2] [1] [accept: application/json]
* [HTTP/2] [1] [content-length: 114]
> POST /dbs/prod/global/DBSReader/fileArray HTTP/2
> Host: cmsweb-prod.cern.ch:8443
> User-Agent: curl/8.20.0
> Accept-Encoding: deflate, gzip, br, zstd
> Content-Type: application/json
> Accept: application/json
> Content-Length: 114
>
* upload completely sent off: 114 bytes
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 200
< content-encoding: gzip
< content-type: application/json
< date: Sat, 20 Jun 2026 18:10:26 GMT
< response-proto: HTTP/1.1
< response-status: 200 OK
```
Pay attention to `accept-encoding` and to `content-encoding` printouts. Therefore for your python client you'll need to provide `Accept-encoding: gzip` and once you receive the gzipped payload you need to decompress it properly.

## Comment (belforte, 2026-06-21T15:55:31Z)

thanks @vkuznet , by "using `gzip` I mean to instantiate WMCore DBSReader object via
 `self.dbs = DBSReader(dbsurl, useGzip=True)`
which results in WMCore calling up DBSClient as
 ` DbsApi(url=url, useGzip=True)`
I have followed this in the python code and ends in using for communication with DBS this object
```
{'url': 'https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader', 'proxy': None, 'key': None, 'cert': None, 'userAgent': '', 'accept': 'application/json', 'aggregate': True, 'debug': True, 'http_response': <RestClient.RequestHandling.HTTPResponse.HTTPResponse object at 0x7fbcc7902730>, 'gzip': True, 'rest_api': <RestClient.RestApi.RestApi object at 0x7fbcc796bfa0>}
```
So I am trying to reproduce that with `curl` to give you an example which does not depend on python DBSClient.

Since `self.gzip` is `True` and this is a POST, the data for the post is gzipped in memory and adds `'Content-Encoding':'gzip'` to the Headers  as per
https://github.com/dmwm/DBSClient/blob/1e6acbd55c55497cf747a2a0cf4539936138a04a/src/python/dbs/apis/dbsClient.py#L466-L470
Final call is made with :
` headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'UserID': 'crab3@crab-dev-tw01.cern.ch', 'User-Agent': 'DBSClient/Unknown/', 'Content-Encoding': 'gzip'}`

I do not see a way to separate gzip usage for data in the POST ad returned value.
I use the same  ` DbsApi(url=url, useGzip=True)` when creating the API used to POST new blocks and it works fine. 

It seems to me that `fileArray` and `insertBulkBlock` are doing some different handling/validation of data, maybe because `insertBulkBlock` does not return any data. I.e. `gzip` only works when talking to DBSWriter, not Reader.

Looking in DBSClient I see that the lines I point to above are the only place where `self.gzip` is used and that the `decompress()` methos is never called, which makes me suspect that the DBSClient is not capable to accept gzipped data ! When doing a GET 

Now, you will surely say that DBSClient in python should not be used and I should change code to fork plain `curl` or use `Requests` etc. etc., but I was simply looking or a small improvement on current situation when CRAB pulls lists of files and lumis for job splitting, sort of a low-hanging-fruit. Major changes in CRAB code are out of scope. I can surely leave things as they are. Changes to DBSClient are surely not in my scope !

FWIW I have tried to add `'Accept-Encoding': 'gzip'` to he headers inside DBS call to server and this time HTTP  returns code 500  with
`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte`

That was only curiosity/education, I surely do not want to have my own version of dmwm/DBSClient and dmwm/PycurlClient.

I do not see a way to make progress. And if you agree, I will close this here.
