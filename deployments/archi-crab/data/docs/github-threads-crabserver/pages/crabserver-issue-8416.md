# dmwm/CRABServer issue #8416: Rucio ASO stuck due to files disappeared in /store/temp

State: closed
Opened: 2024-05-16T17:18:47Z
Closed: 2024-05-23T14:16:46Z
URL: https://github.com/dmwm/CRABServer/issues/8416

## Opening post (belforte, 2024-05-16T17:18:47Z)

as discussed in today's meeting. I saw for the first time a situation where files disappeared from /store/temp before Rucio could copy them. This happened running Jenkins StatusTracking on `test2` instance

| Task | Rule | Grafana |
| - | - | -|
| [240515_152305:cmsbot_crab_rucio_transfers_20240515_172303](https://cmsweb-test2.cern.ch/crabserver/ui/task/240515_152305%3Acmsbot_crab_rucio_transfers_20240515_172303) | [904469b342f24ee593164ba6b390f7f2](https://cms-rucio-webui.cern.ch/rule?rule_id=904469b342f24ee593164ba6b390f7f2#locks) | [jobs](https://monit-grafana.cern.ch/goto/XIll3ZESR?orgId=11) |
| [240515_152307:cmsbot_crab_rucio_transfers_group_20240515_172306](https://cmsweb-test2.cern.ch/crabserver/ui/task/240515_152307%3Acmsbot_crab_rucio_transfers_group_20240515_172306) | [a83780c4d6ae4de5bfab45d89869c75b](https://cms-rucio-webui.cern.ch/rule?rule_id=a83780c4d6ae4de5bfab45d89869c75b) | [jobs](https://monit-grafana.cern.ch/goto/ySGmeWPSg?orgId=11) |
| [240515_152310:cmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308](https://cmsweb-test2.cern.ch/crabserver/ui/task/240515_152310%3Acmsbot_crab_rucio_transfers_manyedm_nopublication_20240515_172308) | [0b84179ad9664456b908509a0a1e2638](https://cms-rucio-webui.cern.ch/rule?rule_id=0b84179ad9664456b908509a0a1e2638) | [jobs](https://monit-grafana.cern.ch/goto/cw3K6ZPIR?orgId=11) |

## Comment (belforte, 2024-05-16T17:45:53Z)

things are not straightforward

**task 3** miss 4 files, 2 from each job 22 and 28. Yet they appear to be at GRIF allright
```
belforte@lxplus811/~> gfal-ls -l  davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/user/cmsbot.a89d85b5d3b5e016ca3701eebcb42631cde823ba/cmsbot/ruciotransfers-1715786588/GenericTTbar/ruciotransfers-1715786588/240515_152310/0000
-rwxrwxrwx   0 0     0        633473 May 15 17:36 output_22.root	
-rwxrwxrwx   0 0     0        631698 May 15 17:36 output_28.root	
-rwxrwxrwx   0 0     0        633492 May 15 17:36 secondoutput_22.root	
-rwxrwxrwx   0 0     0        631723 May 15 17:36 secondoutput_28.root	
belforte@lxplus811/~> 
```
maybe a matter of waiting ?

**task1** misses 6 files, from jobs 9,21,23,33,37,38 
and those are there as well !! Even if I can swear that they were missing yesterday. Maybe some disk at T2_FR_GRIF went off/on line :-(  . Maybe they have not mastered EOS operations yet.
```
belforte@lxplus811/~> gfal-ls -l davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/user/cmsbot.a89d85b5d3b5e016ca3701eebcb42631cde823ba/cmsbot/ruciotransfers-1715786583/GenericTTbar/ruciotransfers-1715786583/240515_152305/0000
-rwxrwxrwx   0 0     0        631713 May 15 17:35 output_21.root	
-rwxrwxrwx   0 0     0        631666 May 15 17:36 output_23.root	
-rwxrwxrwx   0 0     0        631808 May 15 17:36 output_33.root	
-rwxrwxrwx   0 0     0        633229 May 15 17:36 output_37.root	
-rwxrwxrwx   0 0     0        631446 May 15 17:35 output_38.root	
-rwxrwxrwx   0 0     0        628728 May 15 17:36 output_9.root	
belforte@lxplus811/~> 
```

**task2** is more tricky since it misses files from both T2_FR_GRIF and T2_IT_Legnaro
and sure enough, 18 files are missing and 18 files are there waiting to be copied at those sites
```
	
belforte@lxplus811/~> gfal-ls -l  davs://t2-xrdcms.lnl.infn.it:2880/pnfs/lnl.infn.it/data/cms/store/temp/user/cmsbot.a89d85b5d3b5e016ca3701eebcb42631cde823ba/rucio/crab_test/ruciotransfers-1715786586/GenericTTbar/ruciotransfers-1715786586/240515_152307/0000/              
-rwxrwxrwx   0 0     0        631962 May 15 17:34 output_10.root	
-rwxrwxrwx   0 0     0        629664 May 15 17:34 output_13.root	
-rwxrwxrwx   0 0     0        631091 May 15 17:34 output_15.root	
-rwxrwxrwx   0 0     0        631183 May 15 17:35 output_26.root	
-rwxrwxrwx   0 0     0        632556 May 15 17:36 output_31.root	
-rwxrwxrwx   0 0     0        634056 May 15 17:34 output_35.root	
-rwxrwxrwx   0 0     0        631446 May 15 17:34 output_38.root	
-rwxrwxrwx   0 0     0        633409 May 15 17:36 output_6.root	
belforte@lxplus811/~> gfal-ls -l davs://eos.grif.fr:11000/eos/grif/cms/grif/store/temp/user/cmsbot.a89d85b5d3b5e016ca3701eebcb42631cde823ba/rucio/crab_test/ruciotransfers-1715786586/GenericTTbar/ruciotransfers-1715786586/240515_152307/0000
-rwxrwxrwx   0 0     0        631057 May 15 17:34 output_12.root	
-rwxrwxrwx   0 0     0        637049 May 15 17:34 output_14.root	
-rwxrwxrwx   0 0     0        632327 May 15 17:34 output_18.root	
-rwxrwxrwx   0 0     0        634760 May 15 17:34 output_2.root	
-rwxrwxrwx   0 0     0        631713 May 15 17:35 output_21.root	
-rwxrwxrwx   0 0     0        630670 May 15 17:35 output_27.root	
-rwxrwxrwx   0 0     0        635035 May 15 17:34 output_29.root	
-rwxrwxrwx   0 0     0        633229 May 15 17:35 output_37.root	
-rwxrwxrwx   0 0     0        630332 May 15 17:34 output_4.root	
-rwxrwxrwx   0 0     0        628728 May 15 17:34 output_9.root	
belforte@lxplus811/~> 
```

maybe Rucio will try again later on and fix them all ?
The error reported for task2 is a more ominous `RequestErrMsg.TRANSFER_FAILED:TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: copy HTTP 500 : Unexpected server error: 500 ` but it could simply mean that the storage server had a temporary issue. Rucio does not tell which file it refers to, nor the FTS job-id :-(

## Comment (belforte, 2024-05-16T17:47:34Z)

@novicecpp I assign to you since this morning you asked for the task names, but I do not thing there's anything to be done. Maybe we can try to bump the rucio rules into "try now", but it may require admin privilege.

## Comment (novicecpp, 2024-05-17T06:44:24Z)

1 and 3 are now done. 
2 still stuck with a 500 error. For example:
```
davs://t2-xrdcms.lnl.infn.it:2880/pnfs/lnl.infn.it/data/cms/store/temp/user/cmsbot.a89d85b5d3b5e016ca3701eebcb42631cde823ba/rucio/crab_test/ruciotransfers-1715786586/GenericTTbar/ruciotransfers-1715786586/240515_152307/0000/output_38.root
```
File is accessible with corrected checksum. But, I do not know how/where to get the FTS error logs.

## Comment (belforte, 2024-05-17T08:37:17Z)

thanks for checking. I know how, but it is a pain, one needs to get it ouf of OpenSearch. Rucio should provide this :-( They have been talking about a new UI for years, I was waiting to see what it looks like before asking for a new feature :-(
DataOps is not interested-in/capable-of tracking single failures so I am not sure investing on some tool which digs in OpenSearch/HDFS automatically is worth :-(
Yet some general way of making an OS query from local python instead of spending 10min in the WebUI could be nice and maybe they set it up already. If you or Dario are interested, you can ping Nikodemas

## Comment (belforte, 2024-05-20T18:05:45Z)

here's FTS log for one of the files which are still failing
https://fts-cms-007.cern.ch:8449/var/log/fts3/transfers/2024-05-20/eos.grif.fr__t2-xrdcms.lnl.infn.it/2024-05-20-1439__eos.grif.fr__t2-xrdcms.lnl.infn.it__4231741179__d08b8312-16b6-11ef-9057-fa163e7dd35e

shows same error as #8417 
```

INFO    Mon, 20 May 2024 16:39:54 +0200; Davix: Negative result for operation: HTTP 404 : File not found . After 1 retry
INFO    Mon, 20 May 2024 16:39:54 +0200; [1716215994457] DEST http_plugin	CLEANUP	0
INFO    Mon, 20 May 2024 16:39:54 +0200; Gfal2: Event triggered: DESTINATION http_plugin CLEANUP 0
INFO    Mon, 20 May 2024 16:39:54 +0200; [1716215994457] BOTH http_plugin	TRANSFER:EXIT	ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
INFO    Mon, 20 May 2024 16:39:54 +0200; Gfal2: Event triggered: BOTH http_plugin TRANSFER:EXIT ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
ERR     Mon, 20 May 2024 16:39:54 +0200; Recoverable error: [5] TRANSFER ERROR: Copy failed (3rd pull, 3rd push). Last attempt: Transfer failure: Peer certificate cannot be authenticated with given CA certificates
```

## Comment (belforte, 2024-05-20T18:11:05Z)

problems also show up in FTS dashboard
https://monit-grafana.cern.ch/d/mtQFDScGk/cms-fts-metrics?orgId=11&refresh=5m&var-vo=cms&var-group_by=activity&var-src_rse=T2_IT_Legnaro&var-src_rse=T2_IT_Legnaro_Temp&var-src_rse=T2_FR_GRIF&var-dst_rse=T2_IT_Legnaro&var-fts_server=All&var-activity=All&var-protocol=All&var-auth_method=All&var-bin=1h

but nobody wlll follow up

## Comment (belforte, 2024-05-22T13:28:03Z)

since we need transfer to T2_IT_Legnaro to work for our tests, I have created a [GGUS ticket](https://ggus.eu/?mode=ticket_info&ticket_id=166833)

## Comment (belforte, 2024-05-23T09:02:41Z)

T2_IT_Legnaro fixed a misconfiguration and those transfers are now done.
In conclusion:
 * "disappeared* files in /store/temp at GRIF: solved by waiting a couple days
 * stuck transfers from T2_IT_Legnaro_temp to T2_IT_Legnaro: required local admin action
 
 I think that we can stick with "wait a week and then kill".  Maybe give user a way to extend the 7dasy in case there's ongoing work with site admins ? Maybe extend the timeout and if user is fed up with waiting they can kill ? 
 Need to make sure that crab kill stops everything !

## Comment (belforte, 2024-05-23T10:09:38Z)

after brief discussion in crab meeting:
 * stick with fixed timeout
 * modify stageout so that when jobs are failed by PJ after N days proper cleanup is done, e.g. make sure that currently open block are closed so that done jobs are published
 * make sure that things are properly closed also in case of crab kill

WIll more to ad hoc issue : #8429

## Comment (belforte, 2024-05-24T13:47:32Z)

action items listed above are tracked in #8429 

closing
