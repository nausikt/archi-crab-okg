# dmwm/CRABServer issue #8244: Automatically handle failed DBS migrations

State: closed
Opened: 2024-02-16T22:08:16Z
Closed: 2024-05-06T22:31:11Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8244

## Opening post (belforte, 2024-02-16T22:08:16Z)

see https://github.com/dmwm/CRABServer/issues/7469#issuecomment-1949403081

I did this [1] in a python shell in the Publisherl, following example in /afs/cern.ch/user/b/belforte/WORK/DBS/migDbg.py [2]
**NOTE** need to change from `cmsweb` to `cmsweb-prod`. migration server does not run on the "for users" cmsweb cluster

[1]
I replayed the migration request that failed in the TaskPublish script, then deleted the exisint migrationId and submitted again, eventually the new migration failed with `status 4` which means "block already at destination", which is just fine. So I manually ran TaskPublish for that task and everything went OK

```txt
>>> migUrl='https://cmsweb-prod.cern.ch/dbs/prod/phys03/DBSMigrate'
>>> globUrl='https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader'
>>> phy3Url = 'https://cmsweb-prod.cern.ch/dbs/prod/phys03/DBSReader'
>>> apiG   = DbsApi(url=globUrl)
>>> apiP3  = DbsApi(url=phy3Url)
>>> apiMig = DbsApi(url=migUrl)
>>> 
>>> data= {'migration_url': globUrl, 'migration_input': b}
>>> data= {'migration_url': globUrl, 'migration_input': b}
>>> data
{'migration_url': 'https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader', 'migration_input': '/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e'}
>>> result = apiMig.submitMigration(data)
DBS Server error: [{'error': {'reason': 'migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e is already exist in DB with id=4392537', 'message': 'Migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e, id=0', 'function': 'dbs.migrate.SubmitMigration', 'code': 125, 'stacktrace': '\ngoroutine 144286 [running]:\ngithub.com/dmwm/dbs2go/dbs.Error({0xae4bc0?, 0xc0005f8060?}, 0x7d, {0xc00053c000, 0xcc}, {0xa0d471, 0x1b})\n\t/go/src/github.com/vkuznet/dbs2go/dbs/errors.go:185 +0x99\ngithub.com/dmwm/dbs2go/dbs.(*API).SubmitMigration(0xc0002f6000)\n\t/go/src/github.com/vkuznet/dbs2go/dbs/migrate.go:679 +0x5e5\ngithub.com/dmwm/dbs2go/web.DBSPostHandler({0xae81b0, 0xc00075c120}, 0xc000118200, {0x9fb1c9, 0x6})\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:561 +0x148a\ngithub.com/dmwm/dbs2go/web.MigrationSubmitHandler({0xae81b0?, 0xc00075c120?}, 0x454134?)\n\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:968 +0x2f\nnet/http.HandlerFunc.ServeHTTP(0xf30000c000476b01?, {0xae81b0?, 0xc00075c120?}, 0x0?)\n\t/usr/local/go/src/net/http/server.go:2109 +0x2f\ngithub.com/dmwm/dbs2go/web.limitMiddleware.func1({0xae81b0?, 0xc00075c120?}, 0x0?)\n\t/go/src/github.com/vkuznet/dbs2go/web/middlewares.go:111 +0x38\nnet/http.HandlerFunc.ServeHTTP(0x94c100?, {0xae81b0?, 0xc00075c120?}, 0x11?)\n\t/usr/local/go/src/net/http/server'}, 'http': {'method': 'POST', 'code': 400, 'timestamp': '2024-02-16 14:50:24.580880652 +0000 UTC m=+117787.938674225', 'path': '/dbs/prod/phys03/DBSMigrate/submit', 'user_agent': 'DBSClient/Unknown/', 'x_forwarded_host': 'dbs-prod.cern.ch', 'x_forwarded_for': '137.138.62.154', 'remote_addr': '10.100.39.0:36384'}, 'exception': 400, 'type': 'HTTPError', 'message': 'DBSError Code:125 Description:DBS Migration error Function:dbs.migrate.SubmitMigration Message:Migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e, id=0 Error: migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e is already exist in DB with id=4392537'}]
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 474, in __callServer
    self.http_response = method_func(self.url, method, params, data, request_headers)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RestApi.py", line 42, in post
    return http_request(self._curl)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-pycurl/3.17.9/lib/python3.8/site-packages/RestClient/RequestHandling/HTTPRequest.py", line 62, in __call__
    raise HTTPError(effective_url, http_code, http_response.msg, http_response.raw_header, http_response.body)
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: Bad Request

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 1834, in submitMigration
    return self.__callServer("submit", data=migrationObj, callmethod='POST')
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 477, in __callServer
    self.__parseForException(http_error)
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 524, in __parseForException
    raise exp
  File "/data/srv/TaskManager/v3.240111-ac252900ca96a6784d9e561ca231c954/slc7_amd64_gcc630/cms/py3-dbs3-client/4.0.12/lib/python3.8/site-packages/dbs/apis/dbsClient.py", line 522, in __parseForException
    raise HTTPError(http_error.url, data['exception'], data['message'], http_error.header, http_error.body, serverCode(data))
RestClient.ErrorHandling.RestClientExceptions.HTTPError: HTTP Error 400: DBSError Code:125 Description:DBS Migration error Function:dbs.migrate.SubmitMigration Message:Migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e, id=0 Error: migration request /Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e is already exist in DB with id=4392537
>>> id=4392537
>>> status = apiMig.statusMigration(migration_rqst_id=id)
>>> status
[{'create_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'creation_date': 1706784889, 'last_modification_date': 1706784889, 'last_modified_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'migration_input': '/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e', 'migration_request_id': 4392537, 'migration_server': 'dbs2go-phys03-migration-58997db5d9-gp6m5', 'migration_status': 9, 'migration_url': 'https://cmsweb-prod.cern.ch:8443/dbs/prod/global/DBSReader', 'retry_count': 4}]
>>> mdic={'migration_rqst_id':id}
>>> apiMig.removeMigration({'migration_rqst_id':mid})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mid' is not defined
>>> apiMig.removeMigration({'migration_rqst_id':id})
[{'status': 'success', 'migration_request_id': 4392537}]
>>> 
>>> result = apiMig.submitMigration(data)
>>> result
[{'migration_details': {'migration_request_id': 4415897, 'migration_url': 'https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader', 'migration_input': '/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e', 'migration_status': 5, 'migration_server': '', 'create_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'creation_date': 1708095162, 'last_modified_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'last_modification_date': 1708095162, 'retry_count': 0}, 'migration_report': 'Migration request is started', 'status': 'QUEUED', 'error': None}]
>>> id=4415897
>>> status = apiMig.statusMigration(migration_rqst_id=id)
>>>
[...]
>>>
>>> apiMig.statusMigration(migration_rqst_id=id)
[{'create_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'creation_date': 1708095162, 'last_modification_date': 1708095162, 'last_modified_by': '/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch', 'migration_input': '/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1/MINIAODSIM#1d24b8c6-ef15-4ffc-8de6-ba80cb3a0d6e', 'migration_request_id': 4415897, 'migration_server': 'dbs2go-phys03-migration-65dbd99c49-dptf6', 'migration_status': 4, 'migration_url': 'https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader', 'retry_count': 1}]
>>> 

```



[2] `cat migDbg.py`
```python

from dbs.apis.dbsClient import DbsApi
migUrl='https://dbs3-test1.cern.ch/dbs/dev/global/DBSMigrate'
phy3Url = 'https://dbs3-test1.cern.ch/dbs/dev/global/DBSReader'
migUrl='https://cmsweb-testbed.cern.ch/dbs/int/phys03/DBSMigrate'
phy3Url = 'https://cmsweb-testbed.cern.ch/dbs/int/phys03/DBSReader'
migUrl='https://cmsweb.cern.ch/dbs/prod/phys03/DBSMigrate'
phy3Url = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
globUrl='https://cmsweb.cern.ch/dbs/prod/global/DBSReader'
apiG   = DbsApi(url=globUrl)
apiP3  = DbsApi(url=phy3Url)
apiMig = DbsApi(url=migUrl)

# pick  a dataset
dataset='/NonPrD0_pT-1p2_y-2p4_pp_13TeV_pythia8/RunIILowPUAutumn18DR-102X_upgrade2018_realistic_v15-v1/AODSIM'

#find blocks
bList=[]
for dic in apiG.listBlocks(dataset=dataset):
    bl1.append(dic['block_name'])

#submit migrations and collect their Id's
migrIds=[]
for b in bList:
    data= {'migration_url': globUrl, 'migration_input': b}
    result = apiMig.submitMigration(data)
    id = result.get("migration_details", {}).get("migration_request_id")
    migrIds.append(id)

#check status, to be repeated until OK (state=2) or terminally failed (state=9)
# https://github.com/dmwm/DBS/blob/625525721c3df9a9b842c84ad0ac29f55180524b/Client/src/python/dbs/apis/dbsClient.py#L1489-L1492
for id in migrIds:
        status = apiMig.statusMigration(migration_rqst_id=id)
        state = status[0].get("migration_status")
        retry_count = status[0].get("retry_count")
        print "migration id, state, retries : %d %d %s" % (id, state, retry_count)


# if there are old, failed migrations, need remove them in order to
# submit them again, the first loop will simly collect their ID's
for mig in migrIds:
    mdic={'migration_rqst_id':mid}
    apiMig.removeMigration({'migration_rqst_id':mid})


```

## Comment (belforte, 2024-02-16T22:50:28Z)

side task
 - [x] fix cmsweb cluster name in   `/afs/cern.ch/user/b/belforte/WORK/DBS/migDbg.py ` and put in GH

## Comment (belforte, 2024-04-26T13:11:08Z)

this happened again https://cms-talk.web.cern.ch/t/crab-job-pubilcation-failed/39892
and again I lost a couple hours on it.

Better fix the code.

## Comment (belforte, 2024-04-29T08:43:17Z)

take this change to
 - [x] make [TaskPublish](https://github.com/dmwm/CRABServer/blob/master/src/python/Publisher/TaskPublish.py) use code shared with [TaskPublishRuco](https://github.com/dmwm/CRABServer/blob/master/src/python/Publisher/TaskPublishRucio.py) from [PublisherDbsUtils](https://github.com/dmwm/CRABServer/blob/master/src/python/Publisher/PublisherDbsUtils.py) and [PublisherUtils](https://github.com/dmwm/CRABServer/blob/master/src/python/Publisher/PublisherUtils.py)

## Comment (belforte, 2024-04-29T20:55:14Z)

dump of most recent error in human format (i.e. pprint)
```text
{'error': {'code': 125,
           'function': 'dbs.migrate.SubmitMigration',
           'message': 'Migration request '
                      '/RelValTTbar_14TeV/CMSSW_14_0_0_pre3-PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/GEN-SIM-DIGI-RAW#c627abb1-b2eb-49a5-9c9f-174fbd82ca24, '
                      'id=0',
           'reason': 'migration request '
                     '/RelValTTbar_14TeV/CMSSW_14_0_0_pre3-PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/GEN-SIM-DIGI-RAW#c627abb1-b2eb-49a5-9c9f-174fbd82ca24 '
                     'is already exist in DB with id=4435739',
           'stacktrace': '\\ngoroutine 1684332 '
                         '[running]:\\ngithub.com/dmwm/dbs2go/dbs.Error({0xae4bc0?, '
                         '0xc00063a9c0?}, 0x7d, {0xc00069a140, 0xa0}, '
                         '{0xa0d471, '
                         '0x1b})\\n\\t/go/src/github.com/vkuznet/dbs2go/dbs/errors.go:185 '
                         '+0x99\\ngithub.com/dmwm/dbs2go/dbs.(*API).SubmitMigration(0xc000196000)\\n\\t/go/src/github.com/vkuznet/dbs2go/dbs/migrate.go:679 '
                         '+0x5e5\\ngithub.com/dmwm/dbs2go/web.DBSPostHandler({0xae81b0, '
                         '0xc000640108}, 0xc000d4aa00, {0x9fb1c9, '
                         '0x6})\\n\\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:561 '
                         '+0x148a\\ngithub.com/dmwm/dbs2go/web.MigrationSubmitHandler({0xae81b0?, '
                         '0xc000640108?}, '
                         '0x454134?)\\n\\t/go/src/github.com/vkuznet/dbs2go/web/handlers.go:968 '
                         '+0x2f\\nnet/http.HandlerFunc.ServeHTTP(0x890000c000c02c01?, '
                         '{0xae81b0?, 0xc000640108?}, '
                         '0x0?)\\n\\t/usr/local/go/src/net/http/server.go:2109 '
                         '+0x2f\\ngithub.com/dmwm/dbs2go/web.limitMiddleware.func1({0xae81b0?, '
                         '0xc000640108?}, '
                         '0x0?)\\n\\t/go/src/github.com/vkuznet/dbs2go/web/middlewares.go:111 '
                         '+0x38\\nnet/http.HandlerFunc.ServeHTTP(0x94c100?, '
                         '{0xae81b0?, 0xc000640108?}, '
                         '0x11?)\\n\\t/usr/local/go/src/net/http/serve'},
 'exception': 400,
 'http': {'code': 400,
          'method': 'POST',
          'path': '/dbs/prod/phys03/DBSMigrate/submit',
          'remote_addr': '10.100.164.0:47826',
          'timestamp': '2024-04-25 08:12:54.165349637 +0000 UTC '
                       'm=+1294416.993904549',
          'user_agent': 'DBSClient/Unknown/',
          'x_forwarded_for': '137.138.157.32',
          'x_forwarded_host': 'dbs-prod2.cern.ch'},
 'message': 'DBSError Code:125 Description:DBS Migration error '
            'Function:dbs.migrate.SubmitMigration Message:Migration request '
            '/RelValTTbar_14TeV/CMSSW_14_0_0_pre3-PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/GEN-SIM-DIGI-RAW#c627abb1-b2eb-49a5-9c9f-174fbd82ca24, '
            'id=0 Error: migration request '
            '/RelValTTbar_14TeV/CMSSW_14_0_0_pre3-PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/GEN-SIM-DIGI-RAW#c627abb1-b2eb-49a5-9c9f-174fbd82ca24 '
            'is already exist in DB with id=4435739',
 'type': 'HTTPError'}

```

## Comment (mapellidario, 2024-04-30T08:36:34Z)

notice that the `document["error","code"] == 125`, which matches the list of error codes from dbs [1]. Maybe this issue is a good place to start with https://github.com/dmwm/CRABServer/issues/7469

[1] https://github.com/dmwm/dbs2go/blob/28e02bde209af797af7d59d4f7e3baba25a98605/dbs/errors.go#L64

## Comment (belforte, 2024-04-30T09:56:43Z)

Thanks Dario,
I am aware. And current code already uses the `error` dictionary above. But there is no use for the DBS error code here since it is the useless "Migration failure" and I have to parse the `reason` string :-(

As much as I hate to parse messages, I'd rather not ask for a change in semantic where the API returns success and reports the existing migrationId, as the old server was doing. I tried to "protect us against changes" via
https://github.com/dmwm/dbs2go/pull/112 . Let's hope DBS maintainer(s) can at least merge that.

## Comment (belforte, 2024-04-30T15:06:29Z)

all of this is now in my branch https://github.com/belforte/CRABServer/tree/deal-with-failed-migrations-8244
and at least Publisher starts (on crab-dev-tw01). I will try some publications. As usual it is not easy to test migrations, and in particular failed migrations !

## Comment (belforte, 2024-05-01T14:56:25Z)

my test task got 50 files correctly published. So at least code is not badly broken by the changes to unify DBS access in the common PublisherDbsUtils.

## Comment (belforte, 2024-05-02T20:46:08Z)

put my branch on preprod and ran a couple Jenkins ST tests.
publication for FTS ASO (TaskPublish.py) appears all OK (of course no migrations).
But I get unexptected problems with Rucio ASO.  That thread is now moved to #8376 

In the meanwhile I am declaring changes to TaskPublish.py (the FTS one) tested enought to make a PR.

I still need to find a way to test migrations. But do not know how to quickly find a dataset which nobody used yet !

## Comment (belforte, 2024-05-06T22:31:12Z)

Closed via #8378 

I could not test failed migrations, but at worst they will be still broken and I will debug when I have an example
