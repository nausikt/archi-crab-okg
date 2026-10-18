# dmwm/CRABServer issue #7676: DBSError 103 caused fail submission of two tasks

State: closed
Opened: 2023-06-19T12:58:35Z
Closed: 2023-06-19T16:05:12Z
Labels: Type: Question
URL: https://github.com/dmwm/CRABServer/issues/7676

## Opening post (mapellidario, 2023-06-19T12:58:35Z)

Dear @belforte and @novicecpp, I have a question for you. 

I noticed that a couple of tasks [1] failed to be submitted with a DBSReader error [2], but I could not replicate the error [3], everything works for me.

Have you noticed anything similar recently? Shall we consider this as a bug or as a transient error?

---

[1] for example `230619_114726:hindrich_crab_TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8`

[2]

<details>

from log file `/data/container/TaskWorker/logs/tasks/hindrich/230619_114726:hindrich_crab_TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8.log` on crab-prod-tw01

```plaintext
2023-06-19 13:48:08,001:ERROR:Handler:Problem handling 230619_114726:hindrich_crab_TTto4Q_Hdamp-158_Tune
CP5_13p6TeV_powheg-pythia8 because of DBSReaderError
Message: Error in DBSReader.getDBSSummaryInfo(None, /TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run
3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_postEE_v1-v3/MINIAODSIM#5da82dcf-8abc-4695-9fa4-0c980ca7
151d)
HTTPError:HTTP Error 400: DBSError Code:103 Description:DBS DB query error, e.g. mailformed SQL statemen
t Function:dbs.filesummaries.FileSummaries Message: Error: nested DBSError Code:102 Description:DBS DB t
ransaction error Function:dbs.executeAll Message: Error: ORA-25408: can not safely replay call


        ClassName : None
        ModuleName : WMCore.Services.DBS.DBSErrors
        MethodName : __init__
        ClassInstance : None
        FileName : /data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cm
s/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/WMCore/Services/
DBS/DBSErrors.py
        LineNumber : 43
        ErrorNr : 1002
 failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskw
orker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/Handler.
py", line 85, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskw
orker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 103, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 362, in executeInternal
    self.checkBlocksSize(blocksWithLocation) # Interested only in blocks with locations, 'blocks' may contain invalid ones and trigger an Exception
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 84, in checkBlocksSize
    blockInfo = self.dbs.getDBSSummaryInfo(block=block)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/WMCore/Services/DBS/DBS3Reader.py", line 419, in getDBSSummaryInfo
    raise DBSReaderError(msg) from None
WMCore.Services.DBS.DBSErrors.DBSReaderError: DBSReaderError
Message: Error in DBSReader.getDBSSummaryInfo(None, /TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_postEE_v1-v3/MINIAODSIM#5da82dcf-8abc-4695-9fa4-0c980ca7151d)
HTTPError:HTTP Error 400: DBSError Code:103 Description:DBS DB query error, e.g. mailformed SQL statement Function:dbs.filesummaries.FileSummaries Message: Error: nested DBSError Code:102 Description:DBS DB transaction error Function:dbs.executeAll Message: Error: ORA-25408: can not safely replay call
```

</details>

[3] opened a shell on crab-preprod-tw01, opened a shell in the TW container, sources `env.sh`, started a python shell, then run `getDBSSummaryInfo` with the same argument that made it fail in [2]. I did the same on crab-prod-tw01. all good.

<details>

```plaintext

> [14:39] crab-preprod-tw01 ~
> docker exec -it TaskWorker bash
[crab3@crab-preprod-tw01 TaskManager]$ source env.sh
Define environment for TASKWORKER in /data/srv/TaskManager
[crab3@crab-preprod-tw01 TaskManager]$ python3
Python 3.8.2 (default, Jan 22 2021, 17:57:37)
[GCC 6.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from WMCore.Services.DBS.DBSReader import DBSReader
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/Utils/TokenManager.py", line 23, in <module>
    import jwt
ModuleNotFoundError: No module named 'jwt'
>>> from ServerUtilities import newX509env
>>> ct = newX509env(X509_USER_CERT="/data/certs/servicecert.pem", X509_USER_KEY="/data/certs/servicekey.pem")
>>> with ct:
...     dbs = DBSReader('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')
...
>>> dbs.getDBSSummaryInfo(block="/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_postEE_v1-v3/MINIAODSIM#5da82dcf-8abc-4695-9fa4-0c980ca7151d")
{'file_size': 10864123853, 'max_ldate': 1676019000, 'median_cdate': 1676019000, 'median_ldate': 1676019000, 'num_block': 1, 'num_event': 129156, 'num_file': 4, 'num_lumi': 188, 'NumberOfFiles': 4, 'NumberOfEvents': 129156, 'NumberOfBlocks': 1, 'NumberOfLumis': 188, 'FileSize': 10864123853, 'path': '', 'block': '/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_postEE_v1-v3/MINIAODSIM#5da82dcf-8abc-4695-9fa4-0c980ca7151d'}
>>>
```

</details>

## Comment (belforte, 2023-06-19T14:01:08Z)

for sure we do not write SQL queries, malformed or not, I guess that something went wrong in communication with DBS server which was not properly caught in vaildation and made for an SQL to be build w/o all the needed pieces. Since this is not reproducible I would not bother to report to Valentin.

## Comment (amaltaro, 2023-06-19T15:32:20Z)

@mapellidario Hi Dario, in case the error happened today, I wanted to mention that we had a CMSR intervention:
https://cern.service-now.com/service-portal?id=outage&n=OTG0077993

Perhaps it matches that intervention?

## Comment (mapellidario, 2023-06-19T16:05:12Z)

Hello Alan!

Yeah, the error happened today, but after that intervention in CMSR finished.

Ok then, we can close this, thanks Stefano and Alan for having a look :)
