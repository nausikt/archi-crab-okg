# dmwm/CRABServer issue #8329: HTTP error 413 Request Entity Too Large when inserting blocks in DBS

State: closed
Opened: 2024-04-11T12:08:41Z
Closed: 2024-04-15T07:57:57Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8329

## Opening post (belforte, 2024-04-11T12:08:41Z)

we have again cases of blocks too big to be published,
DBS server returns `HTTP error 413 Request Entity Too Large`

<details><summary>Detail:</summary>

Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.240325-e142b415228994babce71846cc653b98/slc7_amd64_gcc630/cms/crabtaskworker/v3.240325-e142b415228994babce71
846cc653b98/lib/python3.8/site-packages/Publisher/TaskPublish.py", line 935, in publishInDBS3
    destApi.insertBulkBlock(blockDump)
  File "/data/srv/TaskManager/v3.240325-e142b415228994babce71846cc653b98/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-pack
ages/dbs/apis/dbsClient.py", line 647, in insertBulkBlock
    result =  self.__callServer("bulkblocks", data=blockDump, callmethod='POST' )
  File "/data/srv/TaskManager/v3.240325-e142b415228994babce71846cc653b98/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-pack
ages/dbs/apis/dbsClient.py", line 486, in __callServer
    self.__parseForException(data)
  File "/data/srv/TaskManager/v3.240325-e142b415228994babce71846cc653b98/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-pack
ages/dbs/apis/dbsClient.py", line 512, in __parseForException
    raise http_error
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 413: 
URL=https://cmsweb-prod.cern.ch:8443/dbs/prod/phys03/DBSWriter/bulkblocks
Code=413
Message=Request Entity Too Large
Header=HTTP/1.1 100 Continue

HTTP/1.1 413 Request Entity Too Large
Date: Wed, 10 Apr 2024 04:51:02 GMT
Server: Apache
Content-Type: text/html
Content-Length: 176
CMS-Server-Time: D=14222 t=1712724662049200
Connection: close

```text
Body=<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>
```
</details>

in a couple of seconds while earlier tests with old python-based server where timing out at 5minuts in CMSWEB FE.

In the [most recent case](https://cms-talk.web.cern.ch/t/publication-failed/38246/7)
DBS is failing that way on blocks with 31K lumis and 1MB size.
Current publisher cuts blocks at 1M lumis !! and that was working https://github.com/dmwm/CRABServer/issues/6670.

Is the new DBS server setting this very strict limit now ? @todor-ivanov 
Or is this CMSWEB setting a 1MB limit on payloads ? @arooshap 
It seems same error as in https://github.com/dmwm/WMCore/issues/11960 wich led to [this](https://mattermost.web.cern.ch/cms-o-and-c/pl/8kbxjzzqf3gimbjh81fnsqrriy) short MatterMost thread.  I am not sure the units in the `1m` and `3m` there, but the last error report is from Apr 10 (yesterday)

I looked at recorded statistics from CRAB Publisher.
Up to CRAB tasks submitted on March 26 blocks of up to 30MB were published successfully in DBS. But after that nothing 1MB or larger makes it through.
Did something change with the beginning of April ?
In DBS ? In CMSWEB ?

I can look into making smaller blocks, but current issue is from a user who can't publish a block with 60 files. I'd rather not go to 10 files per block !!

## Comment (belforte, 2024-04-11T12:23:17Z)

failed publications per hour in last 30 days clearly indicates how April is different from March. Of course user jobs are different, yet...
![image](https://github.com/dmwm/CRABServer/assets/1837785/1500f4d1-7db3-499e-bea5-60aa6a8701c1)
from https://monit-grafana.cern.ch/goto/M3Gzdv-SR?orgId=11

## Comment (belforte, 2024-04-14T14:18:38Z)

Problems persist, all blocks >1MB are failing
![image](https://github.com/dmwm/CRABServer/assets/1837785/27d11ed6-8b23-4f54-8ecd-01bce99e434d)

This is not part of DBS/CMSWEB specification and I do not have a way to cut things in samller pieces.
@arooshap @todor-ivanov

## Comment (arooshap, 2024-04-15T07:36:15Z)

Hi @belforte, I just removed the limit contraints from the ingress in both production clusters.

## Comment (belforte, 2024-04-15T07:57:57Z)

thanks a lot @arooshap !

## Comment (todor-ivanov, 2024-04-15T09:43:40Z)

hi @belforte,

> Did something change with the beginning of April ?
> In DBS ? In CMSWEB ?

I can tell for sure, nothing has changed on April related  to DBS. No extra limitations  has been enforced. 
BTW, Did @arooshap's  intervention fix the problem. I was advocating in the past (even for the WMCore issue) that the problem should be resolved by increasing the Frontend limits, but people are afraid of hitting further limitations down the chain (e.g DBS).

## Comment (arooshap, 2024-04-15T09:56:10Z)

@todor-ivanov yes, it is related to the ingress limits. Just to correct something, we are not imposing any limits on our frontends. It was the nginx that we are using in the backend. The service is maintained by the CERN IT. So, by default, it was imposing the size constraints(which have now been removed).

## Comment (todor-ivanov, 2024-04-15T10:14:42Z)

hi @arooshap 
> which have now been removed 

That's actually great 
Thanks!
