# dmwm/CRABServer issue #8308: Publisher fails with `413 Request Entity Too Large` from DBS

State: open
Opened: 2024-04-02T21:37:07Z
Labels: Type: Bug, Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8308

## Opening post (belforte, 2024-04-02T21:37:07Z)

reference:  https://cms-talk.web.cern.ch/t/publication-failed/38246

looks like in spite of past efforts to break down large blocks, we still have a problem
https://cmsweb.cern.ch/crabserver/ui/task/240402_010755%3Atsheng_crab_2024d0ppdigi_v1#task-info

blocks in this case has only 93 files [1] but it is 22MB
```text
[crab3@crab-prod-tw01 tsheng]$ ls -lh /data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt
-rw-r--r--. 1 crab3 crab3 22M Apr  2 04:01 /data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt
[crab3@crab-prod-tw01 tsheng]$ 
```
those 93 files have 44833 parents !
```text
[crab3@crab-prod-tw01 tsheng]$ cat /data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt|grep -c parent_logical_file_name
44833
```
even if the number of lumis is not so absurd
```text
[crab3@crab-prod-tw01 tsheng]$ cat /data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt|grep -c lumi
4650
```


I think this is a new "use case" .  Likely would have failed with old DBS too. New server is kind enough to return http error instead of timing out.


[1]
```text

Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 413: Request Entity Too Large

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/crabtaskworker/v3.240111-ac252900ca96a6784d9e561ca231c954/lib/python3.8/site-packages/Publisher/TaskPublish.py", line 933, in publishInDBS3
    destApi.insertBulkBlock(blockDump)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 647, in insertBulkBlock
    result =  self.__callServer("bulkblocks", data=blockDump, callmethod='POST' )
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 486, in __callServer
    self.__parseForException(data)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 512, in __parseForException
    raise http_error
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 413: 
URL=https://cmsweb-prod.cern.ch:8443/dbs/prod/phys03/DBSWriter/bulkblocks
Code=413
Message=Request Entity Too Large
Header=HTTP/1.1 100 Continue

HTTP/1.1 413 Request Entity Too Large
Date: Tue, 02 Apr 2024 02:01:46 GMT
Server: Apache
Content-Type: text/html
Content-Length: 176
CMS-Server-Time: D=138887 t=1712023306398334
Connection: close


Body=<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>



2024-04-02 04:01:49,471:ERROR: FAILING BLOCK DUE TO HTTP Error 413: 
URL=https://cmsweb-prod.cern.ch:8443/dbs/prod/phys03/DBSWriter/bulkblocks
Code=413
Message=Request Entity Too Large
Header=HTTP/1.1 100 Continue

HTTP/1.1 413 Request Entity Too Large
Date: Tue, 02 Apr 2024 02:01:46 GMT
Server: Apache
Content-Type: text/html
Content-Length: 176
CMS-Server-Time: D=138887 t=1712023306398334
Connection: close


Body=<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>

 SAVED AS /data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt
2024-04-02 04:01:49,471:INFO: PUBSTAT: Nfiles=  93, filestructSize=  11MB, lumis=   4650, iter= 1, blockSize=  19MB, time=  3s, status=FAIL, task=240402_010755:tsheng_crab_2024d0ppdigi_v1
2024-04-02 04:01:49,471:INFO: End of publication status: failed 93, published 0, publish_in_next_iteration 0, results {'existingFiles': 0, 'files': 0, 'blocks': 0}
2024-04-02 04:01:49,471:INFO: Marking 93 file(s) as failed
2024-04-02 04:01:49,860:INFO: marked 10 files
2024-04-02 04:01:50,265:INFO: marked 20 files
2024-04-02 04:01:50,753:INFO: marked 30 files
2024-04-02 04:01:51,175:INFO: marked 40 files
2024-04-02 04:01:51,561:INFO: marked 50 files
2024-04-02 04:01:52,021:INFO: marked 60 files
2024-04-02 04:01:52,444:INFO: marked 70 files
2024-04-02 04:01:52,833:INFO: marked 80 files
2024-04-02 04:01:53,264:INFO: marked 90 files
[crab3@crab-prod-tw01 tsheng]$ 

```

## Comment (belforte, 2024-04-02T22:00:18Z)

side note: there are 92 failed blocks for last month in `/data/srv/Publisher_files/FailedBlocks/`
We should revamp effort to track them down. Problem seem "just sine March" !
![image](https://github.com/dmwm/CRABServer/assets/1837785/85a05b03-b683-4ec0-a70d-0e940aa85daf)

I managed to look as users behind the failure (brute force hack with grep of those files to extract one lfn and get user name inside it) but there's no clear dominance. The user with today's problem (`tsheng`) only has two failed blocks and both refer to same task as discussed here
```text
[crab3@crab-prod-tw01 tsheng]$ grep -m 1 tsheng /data/srv/Publisher_files/FailedBlocks/*txt
/data/srv/Publisher_files/FailedBlocks/failed-block-at-1712021537.1638997.txt:                     'lfn': '/store/group/phys_heavyions/tsheng/run23/Pythia8_DzeroToKPi_prompt_Pthat5_TuneCP5_5360GeV/MC_20240401_DIGI_v1/240402_010755/0000/signal_RAW_44.root',
/data/srv/Publisher_files/FailedBlocks/failed-block-at-1712023306.5412498.txt:                     'lfn': '/store/group/phys_heavyions/tsheng/run23/Pythia8_DzeroToKPi_prompt_Pthat5_TuneCP5_5360GeV/MC_20240401_DIGI_v1/240402_010755/0000/signal_RAW_76.root',
[crab3@crab-prod-tw01 tsheng]$ 
```
Maybe many failures were simply "DBS restart" during cmsweb migrations and succeeded after retry ?

## Comment (todor-ivanov, 2024-04-03T05:53:55Z)

Hi @belforte from your messages above, I see the origins could be two here:
* large blocks from CRAB side 
* DBS infrastructure issues during the last days on March. 

If the former, should we also start  looking into ways to increase the limitations on the block size records from the DBS server side, or do you think it won't be needed?

## Comment (belforte, 2024-04-03T08:38:22Z)

thanks for helping out @todor-ivanov . Let's do the simple thing and retry the publication in case it was the second.
I will do and post result here.

If it is the first indeed a starting point could be to compare with what WMA does, as it may suffer of same problem (classical pileup brings in many many files as parents in its effort to randomize events across a large minbias dataset). Or maybe it is a user misconfiguration that we better solve making it impossible to create such a mess :-)

Forcing DBS to accept outlandish inputs should be last resort. Such things may create problems down the line as well.

## Comment (todor-ivanov, 2024-04-03T08:56:39Z)

Thanks @belforte . I'll stay put, while watching the outcome from this particulate use case.
