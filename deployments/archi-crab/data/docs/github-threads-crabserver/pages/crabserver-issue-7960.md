# dmwm/CRABServer issue #7960: Make ASO entries in CMS FTS Dashboard report RSE

State: closed
Opened: 2023-10-18T15:37:45Z
Closed: 2024-05-23T23:09:32Z
Labels: Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7960

## Opening post (belforte, 2023-10-18T15:37:45Z)

ASO entries in https://monit-grafana.cern.ch/d/mtQFDScGk/cms-fts-metrics do not have RSE info

Looking at FTS raw info in ES  it seems to me that Rucio transfers use FTS metadata to convey this information e.g. in 
[this doc](https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/80773820-d0bb-11ea-a34a-f59641c8979f/monit_prod_fts_raw_start-2023-10-18?id=ecc11622-40aa-9520-3172-4d05bd8189c9)
we find `data.file_metadata.src_rse` and `data.file_metadata.dst_rse T2_AT_Vienna`

while the `.file_metadata.*_rse` fields are not preset in [ASO case](https://monit-opensearch.cern.ch/dashboards/app/discover#/doc/80773820-d0bb-11ea-a34a-f59641c8979f/monit_prod_fts_raw_state-2023-10-18?id=e82867cc-208e-c331-3abb-a0213c966e9c)
where we have fields inserted by ASO as `job_metadata` e.g. ` data.job_metadata.userDN` and the only file metadata is `data.file_metadata.oracleId` which does not look like "CRAB"
 
I suspect we looked a this already and come to some conclusion that reporting file_meatdata was not possible, but it is worth revisit again and possibly talk again with FTS developers, maybe something has changed !

## Comment (belforte, 2023-10-19T14:44:20Z)

high prio, since either I do "this year" or I never do

## Comment (belforte, 2024-05-23T14:53:28Z)

I was wrong, the `data.file_metadata.oracleId`  comes from
https://github.com/dmwm/CRABServer/blob/0e09fe691c354b0fca9ac9a078fcd7678434f658/scripts/task_process/FTS_Transfers.py#L268-L274
