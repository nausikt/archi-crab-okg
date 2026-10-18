# dmwm/CRABServer pull request #8569: Add monitoring script back to REST's PyPI image

State: closed
Opened: 2024-07-29T15:25:28Z
Closed: 2024-07-29T16:23:27Z
Merged: 2024-07-29T16:23:27Z
URL: https://github.com/dmwm/CRABServer/pull/8569

## Opening post (novicecpp, 2024-07-29T15:25:28Z)

Fix https://github.com/dmwm/CRABServer/issues/8568

## Comment (novicecpp, 2024-07-29T15:36:25Z)

~~Waiting this pipeline to finish: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7842616~~

Tasks could submit is enough.

## Comment (novicecpp, 2024-07-29T15:45:42Z)

Inspect manually in crabserver's pod. 
The `process_exporter` is up and running.
```
crab3@crabserver-7b875c9ffb-tk5h8:/data$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
crab3          1  0.0  0.0   5788  3200 ?        Ss   17:32   0:00 /bin/bash /opt/setup-certs-and-run/setup-certs-and-run.sh
crab3         10  0.0  0.0   2376  1152 ?        S    17:32   0:00 /usr/bin/tini -- /data/run.sh
crab3         47  0.0  0.0   5788  3328 ?        S    17:32   0:00 /bin/bash /data/run.sh
crab3         51  0.0  0.0   4420  1664 ?        S    17:32   0:00 cat /data/srv/state/crabserver/crabserver-fifo
crab3         67  0.0  0.3  36396 26484 ?        S    17:32   0:00 python3 /usr/local/bin/wmc-httpd -r -d /data/srv/state/crabserver -l /data/srv/state/crabserver/crabserver-fifo /data/srv/c
crab3         68  0.0  0.0   4420  1664 ?        S    17:32   0:00 cat /data/srv/state/crabserver/crabserver-fifo
crab3         69  4.4  1.3 824116 101464 ?       Sl   17:32   0:28 python3 /usr/local/bin/wmc-httpd -r -d /data/srv/state/crabserver -l /data/srv/state/crabserver/crabserver-fifo /data/srv/c
crab3         80  0.0  0.0   5788  3328 ?        S    17:33   0:00 /bin/bash /usr/local/bin/process_monitor.sh /data/srv/state/crabserver/crabserver.pid crabserver :18270 15
crab3         96  0.0  0.1 713516 14120 ?        Sl   17:33   0:00 process_exporter -pid 69 -prefix crabserver -address :18270
crab3        653  0.0  0.0   4284  1792 ?        S    17:43   0:00 sleep 15
crab3        655  0.0  0.0   6052  3584 pts/0    Ss   17:43   0:00 bash
crab3        662  0.0  0.0   8648  3072 pts/0    R+   17:43   0:00 ps aux
```

## Comment (cmsdmwmbot, 2024-07-29T15:49:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2073/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-07-29T16:24:36Z)

No. 
We need `process_exporter` from cmsweb baseimage anyway. Therefore, we need to keep the cmsweb baseimage up-to-date.
If you do not like `cmsweb` image because it is now deprecated and it will be gone someday. We can use the upstream [exporters ](https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/exporters/Dockerfile) image. As long as `reqmgr2` use it, it DMWM & Co. will update it for us.

## Comment (belforte, 2024-07-29T16:24:55Z)

sorry @novicecpp I though I was looking at my PR and merged yours instead. Code is fine. But I am a bit worried about loosing track again of what we use, even if new docker is much easier to read !

## Comment (belforte, 2024-07-29T16:28:02Z)

I see. OK. **we need to keep the cmsweb baseimage up-to-date.**
