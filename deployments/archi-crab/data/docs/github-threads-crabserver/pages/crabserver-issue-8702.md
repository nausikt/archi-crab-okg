# dmwm/CRABServer issue #8702: Cronjobs for monitoring fails silently

State: closed
Opened: 2024-09-19T21:49:58Z
Closed: 2025-02-27T10:50:33Z
Labels: Type: Bug, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/8702

## Opening post (novicecpp, 2024-09-19T21:49:58Z)

Because image not found (cause by https://github.com/dmwm/CRABServer/issues/8701).

There is no log to look at unless run it manually.

```
[crab3@crab-prod-tw02 ~]$ export loguuid=watest1log; bash /home/crab3/runContainer.sh -v v3.240904-stable -s TaskWorker_monit_checktaperecall -u ${loguuid} -c 'python3 /data/srv/monit/CheckTapeRecall.py'
0
0
Unable to find image 'registry.cern.ch/cmscrab/crabtwmonit:v3.240904-stable' locally
docker: Error response from daemon: unknown: artifact cmscrab/crabtwmonit:v3.240904-stable not found.
See 'docker run --help'.
```

Log file is there in /tmp dir but no content (No log file mean everything is fine).

## Comment (aspiringmind-code, 2025-02-27T10:50:33Z)

I believe this issue has been rendered moot after resolution of #8701
