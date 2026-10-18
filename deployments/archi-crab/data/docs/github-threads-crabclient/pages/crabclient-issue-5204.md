# dmwm/CRABClient issue #5204: import DBS3SetDatasetStatus and DBS3SetFileStatus into CRAB

State: closed
Opened: 2023-07-13T13:05:27Z
Closed: 2023-10-27T19:54:20Z
Labels: enhancement, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5204

## Opening post (belforte, 2023-07-13T13:05:27Z)

- [x] copy  files from https://github.com/dmwm/DBS/tree/master/Client/utils/DataOpsScripts to our repo
- [x] make them py2/3 compatible
- [x] make them work as `crab` commands. We should replace calls to new DBS3 python client with direct `curl` to server (as per Valentin's instructions) so that code will work with both py2 and py3

- [ ] Also update instructions in https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
- [ ] Add to Jenkins ClientValidation test

## Comment (belforte, 2023-07-13T13:07:14Z)

@novicecpp @mapellidario while I am the default volunteer/victim here, this is something that you should be able to do as well. Feel free to pick it up in case (change the assignee) and then feel free to ask me questions !

## Comment (belforte, 2023-10-23T23:27:38Z)

`crab setdataset` is done. I will look at `setfiles` before worrying about the `--recursive` option which I am not sure is that useful for USER datasets.

```

belforte@lxplus805/TC3> crab setdataset --dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER --status DELETED            
looking up Dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER in DBS prod/phys03
Dataset status in DBS is VALID
Will set it to DELETED
Dataset status changed successfully
Dataset status in DBS now is DELETED
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> 

belforte@lxplus805/TC3> crab setdataset --dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER --status VALID   
looking up Dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER in DBS prod/phys03
Dataset status in DBS is DELETED
Will set it to VALID
Dataset status changed successfully
Dataset status in DBS now is VALID
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> 

```

## Comment (belforte, 2023-10-24T21:39:38Z)

initial version of `crab setfiles` is also ready. I only takes a single LFN to act upon. Next I will extend to a list or file with a list or all files in a dataset. The latter is bit fuzzy since it looks like old DBS code by Yuyi allows to pass a block https://github.com/dmwm/DBS/blob/14df8bbe8ee8f874fe423399b18afef911fe78c7/Client/utils/DataOpsScripts/DBS3SetFileStatus.py#L151 while new server only takes LFN(s) or dataset https://github.com/dmwm/DBSClient/blob/df14cab23662f8d8b5f072857d937b4fadd2885b/src/python/dbs/apis/dbsClient.py#L1975

Examples from my branch https://github.com/belforte/CRABClient/tree/add-change-DBS-dataset-file-status-fix-5204

```
belforte@lxplus805/TC3> dasgoclient --query 'file file=/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root instance=prod/phys03 |grep file.is_file_valid'
1  
belforte@lxplus805/TC3> crab setfiles --lfn /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root --status INVALID
looking up LFN /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root in DBS prod/phys03
File status in DBS is VALID
Will set it to INVALID
Dataset status changed successfully
LFN status in DBS now is INVALID
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> dasgoclient --query 'file file=/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root instance=prod/phys03 |grep file.is_file_valid'
0  
belforte@lxplus805/TC3> crab setfiles --lfn /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root --status VALID  
looking up LFN /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root in DBS prod/phys03
File status in DBS is INVALID
Will set it to VALID
Dataset status changed successfully
LFN status in DBS now is VALID
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> dasgoclient --query 'file file=/store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root instance=prod/phys03 |grep file.is_file_valid'
1  
belforte@lxplus805/TC3> crab setfiles --lfn /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root --status VALID
looking up LFN /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_1.root in DBS prod/phys03
File status in DBS is VALID
Will set it to VALID
Dataset status changed successfully
LFN status in DBS now is VALID
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> 

```

## Comment (belforte, 2023-10-24T23:13:56Z)

I got parameter manipulation under control to replicate the `--files` option from https://github.com/dmwm/DBS/blob/master/Client/utils/DataOpsScripts/DBS3SetFileStatus.py
But exploration with passing a list of files to the DBS REST server ran into odd issues. I have asked DBS experts (Valentin) https://github.com/dmwm/dbs2go/issues/102
Valenting confirmed a bug on server side. But he is not maintaining dbs2go code anymore. Let's see.

## Comment (belforte, 2023-10-25T10:27:12Z)

should change command names to:
 - crab setdatasetstatus
 - crab setfilestatus
 consistently with "old" names in https://github.com/dmwm/DBS/tree/master/Client/utils/DataOpsScripts

## Comment (belforte, 2023-10-25T20:54:02Z)

From my side code changes are completed, pending review of https://github.com/dmwm/CRABClient/pull/5241 and full validation for "nothing broke"

Now `crab setfilestatus` prints summary of status before/after the change is applied.
When indicating a full dataset:
```
belforte@lxplus805/TC3> crab setfilestatus --status VALID --dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER
Dataset file count total/valid/invalid = 40/1/39
File(s) status changed successfully
Dataset file count total/valid/invalid = 40/40/0
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> 
```
or when indicating a single file (I use same code/format):
```
belforte@lxplus805/TC3> crab setfilestatus --file /store/user/rucio/belforte/testRucioPub/GenericTTbar/Stefano-TestRucioP-230817/230817_203741/0000/kk_15.root --status INVALID
LFN to be changed belongs to dataset /GenericTTbar/belforte-Stefano-TestRucioP-230817-94ba0e06145abd65ccb1d21786dc7e1d/USER
Dataset file count total/valid/invalid = 40/40/0
File(s) status changed successfully
Dataset file count total/valid/invalid = 40/39/1
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus805/TC3> 
```

## Comment (belforte, 2023-10-26T12:08:44Z)

I merged [my branch](https://github.com/belforte/CRABClient/tree/add-change-DBS-dataset-file-status-fix-5204) with master dmwm repo  in [test-setdatasetfilesstatus branch](https://github.com/dmwm/CRABClient/tree/test-setdatasetfilesstatus) tagged as [testSetDsetFilesStatus.1](https://github.com/dmwm/CRABClient/releases/tag/testSetDsetFilesStatus.1) and ran Jenkins CV to check for regression
* https://github.com/dmwm/CRABServer/issues/7977
* https://github.com/dmwm/CRABServer/issues/7978
* https://github.com/dmwm/CRABServer/issues/7979
* https://github.com/dmwm/CRABServer/issues/7980
* https://github.com/dmwm/CRABServer/issues/7981

All OK !

## Comment (belforte, 2023-10-26T12:45:31Z)

actions from Wa's review in https://github.com/dmwm/CRABClient/pull/5241#pullrequestreview-1699272409

- [x] Move HTTPRequests to utils and move DBSREST to new file same level as CrabRestInterface.py
   -  ClientUtils is already too long. I am creating a new file RestInterfaces.py to contain HTTPRequest, CRABRest and  DBSRest
- [x] look a the feasibility to rename `uri` argument in HTTPRequests to `api`
   * this requires some work. There's too much history in HTTPRequests class, the best way is to create a new class like CRABRest with its own get/put/post... methods which take `api` as arg and subclass it as DBSRestReader and DBSRestWriter. Not sure it is worth. And of course leave it to another time good cleanup of HTTPRequests solving the schizophrenic use of `hostname` and the horrible way to use `self` as a dictionary - Moved to https://github.com/dmwm/CRABServer/issues/7986
- [x] getDbsREST should find the current client version, not ask for it as argument
- [x] fix usage of `Content-type` in HTTPRequests
   * maybe I do not need the `Content-type=json`, now that all my problems were clarified as a dbs2go bug ?
   * Yes. Everything works w/o it. Looking again at [DBS2GO documentation](https://github.com/dmwm/dbs2go/blob/master/docs/apis.md#put-dbs-apis) and [curl documentation](https://everything.curl.dev/http/post/content-type) (thanks Wa!) I conclude that DBS2GO simply assumes that data is JSON (which explains some of the errors I was having) and that indicating it explictly in the `curl` is sort of "being nice and very clear". So all in all I will keep this. As:
     *  if user of HTTPRequests is not happy with `curl`'s default, they can pass a `contentType`
