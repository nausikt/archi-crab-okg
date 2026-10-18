# dmwm/CRABServer issue #9302: taskPublish does not properly cut block size

State: closed
Opened: 2026-04-22T14:10:08Z
Closed: 2026-04-25T13:50:10Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9302

## Opening post (belforte, 2026-04-22T14:10:08Z)

We had DBS Migration server crash continuously on attempt to migration blocks from
`/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/MINIAODSIM` for task
https://cmsweb.cern.ch/crabserver/ui/task/260420_190537%3Aekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420

Most likely due to horrendous amount of lumis.  Dataset  has 306 blocks, 10K files. One random file has 9k lumis
```console
belforte@lxplus802/TC3> dasgoclient --query 'lumi file=/store/mc/RunIII2024Summer24MiniAOD/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/MINIAODSIM/Filter_DoubleMuOS43_140X_mcRun3_2024_realistic_v26-v4/2520002/ed04f142-f933-420a-88e8-d6af43ad67e3.root' |wc -l
9364
belforte@lxplus802/TC3> 
```

Dataset was eventually migrated after increasing DBS migration server memory more than x2 by @todor-ivanov 

But when taskPublish.py moved on to try to publish we got the following in
`logs/tasks/ekauffma/260420_190537:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420.log`

```
2026-04-22 08:04:28,048:INFO: inputDataset: /InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-Filter_Do
2026-04-22 08:04:28,064:INFO: Dataset /InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/phys_exotica-ScoutingNano_InclusiveDilept
2026-04-22 08:04:28,100:INFO: Output dataset config: {'dataset': '/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5Plus_13p6TeV_pythia8/phys_exotica-
2026-04-22 08:39:53,639:INFO: Found 5008 files not already present in DBS which will be published.
2026-04-22 08:40:40,484:INFO: Trying to publish 78069404 lumis in 50 blocks
2026-04-22 08:40:40,490:INFO: Reducing to 64 files per block to keep nLumis/block below 1000000.0
2026-04-22 08:45:41,271:ERROR: Error for files: ['/store/group/phys_exotica/axol1tl/MC_ScoutingNano/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5P
2026-04-22 08:45:41,286:ERROR: Error when publishing (/store/temp/user/ekauffma.7da18a16aaa8d09a1ab771470601acdbc970102d/phys_exotica/axol1tl/MC_Scout
  File "/data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py", line 303, in publishInDBS3
    destApi.insertBulkBlock(blockDump)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 647, in insertBulkBlock
    result =  self.__callServer("bulkblocks", data=blockDump, callmethod='POST' )
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 56, in __call__
    curl_object.perform()
pycurl.error: (92, 'HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)')

2026-04-22 08:45:51,774:ERROR: FAILING BLOCK DUE TO (92, 'HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)') SAVED AS /data/srv/Publishe
2026-04-22 08:45:51,990:INFO: PUBSTAT: Nfiles=5008, filestructSize=3436MB, lumis=78069404, iter= 1, blockSize=27MB  , time=310, status=FAIL, task=2604
2026-04-22 08:47:06,008:ERROR: Error for files: ['/store/group/phys_exotica/axol1tl/MC_ScoutingNano/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5P
2026-04-22 08:47:06,015:ERROR: Error when publishing (/store/temp/user/ekauffma.7da18a16aaa8d09a1ab771470601acdbc970102d/phys_exotica/axol1tl/MC_Scout
 Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.dataset_output_configs.Insert Message: Error: ORA-00001: unique c
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/Publisher/TaskPublish.py", line 303, in publishInDBS3
    destApi.insertBulkBlock(blockDump)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 647, in insertBulkBlock
    result =  self.__callServer("bulkblocks", data=blockDump, callmethod='POST' )
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 477, in __callServer
    self.__parseForException(http_error)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 522, in __parseForException
    raise HTTPError(http_error.url, data['exception'], data['message'], http_error.header, http_error.body, serverCode(data))
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblo
 Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.dataset_output_configs.Insert Message: Error: ORA-00001: unique c


2026-04-22 08:47:16,148:ERROR: FAILING BLOCK DUE TO HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.I
 Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.dataset_output_configs.Insert Message: Error: ORA-00001: unique c
 SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1776840426.0195.txt
2026-04-22 08:47:16,595:INFO: PUBSTAT: Nfiles=5008, filestructSize=3436MB, lumis=78069404, iter= 2, blockSize=26MB  , time= 83, status=FAIL, task=2604
```

which appears to suggest that 
`
2026-04-22 08:40:40,490:INFO: Reducing to 64 files per block to keep nLumis/block below 1000000.0
`
did not work, or the threshold (1M lumi per block) is too high, making DBS Writer fail.

It is also possible that 
```
2026-04-22 08:40:40,490:INFO: Reducing to 64 files per block to keep nLumis/block below 1000000.0
2026-04-22 08:45:41,271:ERROR: Error for files: ['/store/group/phys_exotica/axol1tl/MC_ScoutingNano/InclusiveDileptonMinBias_Fil-DoubleMuOS43_TuneCP5P
```
simply meant that operation hit the 5min cmsweb timeout

I blacklisted that task to avoid Publisher getting stuck there, but that deleted that JSON file for the info for publishing so some more effort is needed to reproduce the problem

## Comment (belforte, 2026-04-22T14:25:09Z)

this is also worrying:

HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.InsertBulkBlocksConcurrently Message:46c8f8c2e6b3975b5b946167391f38c182f51e21b4ee5952e1f05a830614ee33 unable to insert dataset output mod configs record, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.dataset_output_configs.Insert Message: Error: ORA-00001: unique constraint (CMS_DBS3_PROD_PHYS03_OWNER.TUC_DC_1) violated

## Comment (belforte, 2026-04-24T20:15:03Z)

I re-created the JSON file for that task via `crab resubmit --publication`, removing from blacklist, hacking PublisherMaster to save also a copy as `Publisher_Files/SB.json` and save it in `logs/migrations/SB.json` so it will not be cleaned up.
Now I can revert hack in PublisherMaster and run TaskPublisher.py on that file with a simple code hack

## Comment (belforte, 2026-04-25T13:14:16Z)

block side reduction works here, but a block with 63 files still is 45MB
```
(Pdb) n
> /data/srv/Publisher/TaskPublish.py(309)publishInDBS3()
-> destApi.insertBulkBlock(blockDump)
(Pdb) len(blockDump)
9
(Pdb) blockSizeKBytes = len(json.dumps(blockDump)) // 1024
(Pdb) blockSize = f"{blockSizeKBytes // 1024}MB"
(Pdb) blockSize
'42MB'
(Pdb) n
```
and `insertBulkBlock` is taking forever....
until
```
(Pdb) n
pycurl.error: (92, 'HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)')
> /data/srv/Publisher/TaskPublish.py(309)publishInDBS3()
-> destApi.insertBulkBlock(blockDump)
(Pdb) 
```
I have no evidence that request has reached DBS Writer. There are 6 pods running but last messages in all are just GET from the probes
```
belforte@vocms0755/dbs-logs> tail  dbs2go-phys03-w-*0425|grep -v GET
==> dbs2go-phys03-w-678b98788f-6bst6.log-20260425 <==

==> dbs2go-phys03-w-678b98788f-9blrz.log-20260425 <==

==> dbs2go-phys03-w-678b98788f-n9qqp.log-20260425 <==

==> dbs2go-phys03-w-bc495d75f-bck2b.log-20260425 <==

==> dbs2go-phys03-w-bc495d75f-kk9t7.log-20260425 <==

==> dbs2go-phys03-w-bc495d75f-pzztz.log-20260425 <==
belforte@vocms0755/dbs-logs> 
```

## Comment (belforte, 2026-04-25T13:21:23Z)

Let's test changing `maxLumisPerBlock` from 1M to 100K, should make blockSize < 5MB (and 6 files)

## Comment (belforte, 2026-04-25T13:32:05Z)

This time no timeout in FE, but after 1 second:
```
FAILING BLOCK DUE TO HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.InsertBulkBlocksConcurrently Message:92c09d68d23f29dfeb2d6265a81d51d21a8cb32532889fd4ed86a80dc472de37 unable to insert files, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1777123587.7026308.txt

PUBSTAT: Nfiles=3540, filestructSize=2528MB, lumis=57447103, iter= 1, blockSize=4MB   , time=  1, status=FAIL, task=260420_190537:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420
```
DBS writer fails. Exception on client side is
```
HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.InsertBulkBlocksConcurrently Message:92c09d68d23f29dfeb2d6265a81d51d21a8cb32532889fd4ed86a80dc472de37 unable to insert files, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency errorTraceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/usr/local/lib/python3.9/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/Publisher/TaskPublish.py", line 307, in publishInDBS3
    t1 = time.time()
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 647, in insertBulkBlock
    result =  self.__callServer("bulkblocks", data=blockDump, callmethod='POST' )
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 477, in __callServer
    self.__parseForException(http_error)
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/usr/local/lib/python3.9/site-packages/dbs/apis/dbsClient.py", line 522, in __parseForException
    raise HTTPError(http_error.url, data['exception'], data['message'], http_error.header, http_error.body, serverCode(data))
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.InsertBulkBlocksConcurrently Message:92c09d68d23f29dfeb2d6265a81d51d21a8cb32532889fd4ed86a80dc472de37 unable to insert files, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error
```

and DBS Writer log is
```
[2026-04-25 13:26:27.64607939 +0000 UTC m=+2467069.190602181] fail to insert files chunks, trec &{IsFileValid:1 DatasetID:3358770 BlockID:30335135 CreationDate:1777123587 CreateBy:/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=373708/CN=Robot: cms crab FilesMap:{mu:{state:0 sema:0} read:{_:[] _:{} v:<nil>} dirty:map[] misses:0} NErrors:1}
[2026-04-25 13:26:27.646669144 +0000 UTC m=+2467069.191191934] 92c09d68d23f29dfeb2d6265a81d51d21a8cb32532889fd4ed86a80dc472de37 unable to insert files, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error
[2026-04-25 13:26:27.654210529 +0000 UTC m=+2467069.198733320] DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.InsertBulkBlocksConcurrently Message:92c09d68d23f29dfeb2d6265a81d51d21a8cb32532889fd4ed86a80dc472de37 unable to insert files, error DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error Error: nested DBSError Code:110 Description:DBS DB insert record error Function:dbs.bulkblocks.insertFilesViaChunks Message: Error: concurrency error Stacktrace: 
goroutine 219500109 [running]:
github.com/dmwm/dbs2go/dbs.Error({0xb2ca20?, 0xc00058f450?}, 0x6e, {0xc0001d01e0, 0xe6}, {0xa5c044, 0x2b})
	/go/src/github.com/vkuznet/dbs2go/dbs/errors.go:185 +0x99
github.com/dmwm/dbs2go/dbs.(*API).InsertBulkBlocksConcurrently(0xc00035c070)
	/go/src/github.com/vkuznet/dbs2go/dbs/bulkblocks2.go:743 +0x24dc
github.com/dmwm/dbs2go/web.DBSPostHandler({0xb2f790, 0xc0000c62e8}, 0xc0005a8240, {0xa3e07d, 0xa})
	/go/src/github.com/vkuznet/dbs2go/web/handlers.go:562 +0x109e
github.com/dmwm/dbs2go/web.BulkBlocksHandler({0xb2f790?, 0xc0000c62e8?}, 0xc0000b21d0?)
	/go/src/github.com/vkuznet/dbs2go/web/handlers.go:978 +0x3b
net/http.HandlerFunc.ServeHTTP(0x0?, {0xb2f790?, 0xc0000c62e8?}, 0x11?)
	/usr/local/go/src/net/http/server.go:2171 +0x29
github.com/dmwm/dbs2go/web.limitMiddleware.func1({0xb2f790?, 0xc0000c62e8?}, 0xc00061a0d0?)
	/go/src/github.com/vkuznet/dbs2go/web/middlewares.go:110 +0x32
net/http.HandlerFunc.ServeHTTP(0xc000e8e150?, {0xb2f790?, 0xc0000c62e8?}, 0xc000341820?)
	/usr/l
[2026-04-25 13:26:27.656524715 +0000 UTC m=+2467069.201047507] HTTP/1.1 400 POST /dbs/prod/phys03/DBSWriter/bulkblocks [data: 4259006 in 884 out] [remoteAddr: 10.100.164.0:52398] [X-Forwarded-For: 188.185.30.204] [X-Forwarded-Host: dbs-prod2.cern.ch] [auth: no-TLS cipher-none "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=373708/CN=Robot: cms crab" cmscrab X509Cert] [ref: "https://cmsweb-prod.cern.ch" "DBSClient/Unknown/"] [req: 210.529938ms proxy-resp: 0]
```

```

## Comment (belforte, 2026-04-25T13:38:24Z)

If this took 1 second to fail, why did a 10x larger block time out ?

## Comment (belforte, 2026-04-25T13:46:15Z)

But when I tried again, it worked ! Maybe DBS just needed "waking up" ?
Now it is runnling along, even if it will take a very long time ! About 1min for each 6 files block, will take 9 hours !

```
Found 3455 files not already present in DBS which will be published.
Trying to publish 56103791 lumis in 34 blocks
Reducing to 6 files per block to keep nLumis/block below 100000.0
PUBSTAT: Nfiles=3455, filestructSize=2469MB, lumis=56103791, iter= 1, blockSize=4MB   , time= 81, status=OK, task=260420_190537:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420
PUBSTAT: Nfiles=3455, filestructSize=2469MB, lumis=56103791, iter= 2, blockSize=4MB   , time= 65, status=OK, task=260420_190537:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420
PUBSTAT: Nfiles=3455, filestructSize=2469MB, lumis=56103791, iter= 3, blockSize=3MB   , time= 23, status=OK, task=260420_190537:ekauffma_crab_ScoutingNano_InclusiveDileptonMinBias_20260420
```
Here's and example entry from DBS Writer log
[2026-04-25 14:21:42.329602866 +0000 UTC m=+2470383.855105607] HTTP/1.1 200 POST /dbs/prod/phys03/DBSWriter/bulkblocks [data: 5045930 in 26 out] [remoteAddr: 10.100.164.0:46366] [X-Forwarded-For: 188.185.81.186] [X-Forwarded-Host: dbs-prod2.cern.ch] [auth: no-TLS cipher-none "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=373708/CN=Robot: cms crab" cmscrab X509Cert] [ref: "https://cmsweb-prod.cern.ch" "DBSClient/Unknown/"] [req: 1m52.898904189s proxy-resp: 0]

`[data: 5045930 in = 5MB`  used `1m52.... seconds`

Clearly that's not data transfer time, 5MB shoudl "fly", it mus the the time on insert 100K lumis

Conclusion:
* there is no bug in CRAB Publisher :-)
- [x] let's change `maxLumisPerBlock` to 100K (or course block will contain at least one file no matter what)

DBS Writer does behave strangely, but I do not think that DBS developers will investigate non-reproducible errors, nor "it is slow".
