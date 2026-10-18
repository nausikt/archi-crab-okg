# dmwm/CRABServer issue #8678: Canary (QA) deployment for TW and Publishers

State: closed
Opened: 2024-08-30T14:43:19Z
Closed: 2025-02-27T10:47:15Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8678

## Opening post (belforte, 2024-08-30T14:43:19Z)

with reference to #8650 
Overall strategy is described in https://github.com/dmwm/CRABServer/wiki/TaskWorker-Canary-Deployment

Pending question:
 **How do we monitor ?**

 high level TW plots in overview (tasks in new/queued/failed...) are hard to separate by TW.
Maybe better to leverage the filebeat->logstash path and create "telling" plots for the QA instance via the timber data ?
Those already have the hostname. 
e.g.

{
  "_index": "monit_private_crab_logs_crabtaskworker-2024-08-30",
  "_id": "6264f8d0-8a69-a1bf-6e13-79a160b523ea",
  "_score": 1,
  "_source": {
    "data": {
      "cmsweb_cluster": "prod",
      "producer_time": 1725029552607,
      "message": "2024-08-30 16:52:29,843:DEBUG:Worker,137:Process-3: RESUBMIT work on 240813_100805:mseidel_crab_UL18_qcdel50_electron_all completed in 6 seconds: Status: OK",
      "completionTime": 6,
      "rec_timestamp_str": "2024-08-30T14:52:29.843Z",
      "log_type": "work_on_task_completed",
      **"filebeat_name": "crab-prod-tw01.cern.ch",**
      "slaveID": "3",
      "filebeat_id": "4c3371b2-460d-4f05-93d4-dc9223d4da87",
      "log_file": "/data/hostdisk/TaskWorker/logs/twlog.txt",
      "cmsweb_env": "prod",
      "workType": "RESUBMIT",
      "taskName": "240813_100805:mseidel_crab_UL18_qcdel50_electron_all",
      "filebeat_version": "8.14.3",
      "record_time": 1725029549843
    },
    "metadata": {
      **"hostname": "crab-prod-tw01.cern.ch",**
      "partition": "3",
      "offset": "78540447",
      "type_prefix": "logs",
      "kafka_timestamp": 1725029558377,
      "json": "true",
      "producer": "crab",
      "topic": "monit-crab_logs",
      "_id": "6264f8d0-8a69-a1bf-6e13-79a160b523ea",
      "type": "crabtaskworker",
      "timestamp": 1725029549843
    }

from https://monit-timberprivate.cern.ch/dashboards/app/discover#/doc/9fee84b0-cd1c-11ec-9cca-9f64af2c2bfb/monit_private_crab_logs_crabtaskworker-2024-08-30?id=6264f8d0-8a69-a1bf-6e13-79a160b523ea
(N.B. use `cmsweb` tenant for that OpenSearch instance)

## Comment (aspiringmind-code, 2025-02-27T10:47:15Z)

See [1](https://monit-grafana.cern.ch/goto/z5IDH4tNg?orgId=11)  , [2](https://monit-grafana.cern.ch/goto/_MsFHVpNg?orgId=11)
