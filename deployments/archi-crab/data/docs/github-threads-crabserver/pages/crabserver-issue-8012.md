# dmwm/CRABServer issue #8012: TW load wrong Rucio client certificate

State: closed
Opened: 2023-11-17T14:13:20Z
Closed: 2023-11-18T15:08:37Z
URL: https://github.com/dmwm/CRABServer/issues/8012

## Opening post (novicecpp, 2023-11-17T14:13:20Z)

Yesterday, after Eric switched the Rucio auth server to a new version, we had an authentication problem report by users in [cms-talk](https://cms-talk.web.cern.ch/t/cannot-authenticate-to-account-crab-server-with-given-credentials/31744).

I found that changed from https://github.com/dmwm/CRABServer/pull/7897 make TaskWorker always used cert from `config.TaskWorker.cmscert`, but not `config.TaskWorker.Rucio_cert`. 
If we look at the logs, it clearly say it use `/data/certs/servicecerts.pem`:
```
2023-11-16 16:29:56,640:DEBUG:Worker:Process-3: Starting <function handleNewTask at 0x7f5daa938310> on 231116_152942:muahmad_crab_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1-UL-HLT-ZgammaJetsToBB
2023-11-16 16:29:56,641:INFO:RucioUtils:Initializing native Rucio client
2023-11-16 16:29:56,642:DEBUG:RucioUtils:Using cert [/data/certs/servicecert.pem]
 and key [/data/certs/servicekey.pem] for rucio client.
2023-11-16 16:29:56,657:INFO:RucioUtils:Rucio server v.32.3.1 contacted
2023-11-16 16:29:56,754:INFO:Worker:Uploading failure message to the REST:
Process-3: I just had a failure for Cannot authenticate.
Details: Cannot authenticate to account crab_server with given credentials

```
Because in the [TaskWorkerConfig.py](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/baf4cf6b8e28b685b866e3f21eff68f007054332/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L16), we set `Rucio_cert` to `Services` attribute of `ConfigurationEx`, not `TaskWorker`.
I was misunderstanding the `ConfigurationEx` scope that I thought somehow we have the same copy of `config.TaskWorker` and `config.Services` it can be used interchangeably.

## Comment (novicecpp, 2023-11-18T15:08:37Z)

Done via https://github.com/dmwm/CRABServer/pull/8006
