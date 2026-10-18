# dmwm/CRABServer issue #9149: CRON commands that relies on crabtwmonit, Failed with No such file or directory, mysteriously missing of monit scripts.

State: closed
Opened: 2025-08-12T12:35:00Z
Closed: 2025-08-12T13:19:31Z
URL: https://github.com/dmwm/CRABServer/issues/9149

## Opening post (nausikt, 2025-08-12T12:35:00Z)

Thanks @aspiringmind-code  for reporting these regarding deluge of cronjob failed emails.

As i try to bring back container `TaskWorker_monit_*` and investigated it, it seems like the underlying problems lies in most of our monit scripts somehow were *missing* from `/data/srv/monit`. Thus cron can't periodically spin up container and run their usual commands. 

We expected monit scripts to be there as we already explicitly copies them from repo to container, as you can see monit Dockerfile [5].
Also `runContainer.sh` might not be the one who mounted volumes and overwrite things, they just try to keep cfg, logs persistent. [6]

[1] ReportRecallQuota
```
export loguuid=$(uuidgen); test -f /home/crab3/runContainer.sh && bash /home/crab3/runContainer.sh -v v3.latest -s TaskWorker_monit_reportrecallquota -u ${loguuid} -c 'python3 /data/srv/monit/ReportRecallQuota.py' >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ] && cat /tmp/monit-${loguuid}.txt
```
[2] GenerateMONIT
```
export loguuid=$(uuidgen); test -f /home/crab3/runContainer.sh && bash /home/crab3/runContainer.sh -v v3.latest -s TaskWorker_monit_generatemonit -u $loguuid -c 'python3 /data/srv/monit/GenerateMONIT.py' >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ] && cat /tmp/monit-${loguuid}.txt
```
[3] aso_metrics_ora
```
export loguuid=$(uuidgen); test -f /home/crab3/runContainer.sh && bash /home/crab3/runContainer.sh -v v3.latest -s TaskWorker_monit_asometrics -u ${loguuid}  -c 'python3 /data/srv/monit/aso_metrics_ora.py' >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ] && cat /tmp/monit-${loguuid}.txt
```
Same OUTPUT(s) from all above commands.
```
[FATAL tini (8)] exec python3 failed: No such file or directory
```
_____

[4] Somehow our monit scripts unexpectedly not lying there in `/data/srv/monit`, thus all commands can't be run.
```
[crab3@crab-dev-tw02 TaskWorker_monit_reportrecallquota]$ docker exec -it TaskWorker_monit_reportrecallquota bash
crab3@crab-dev-tw02:/data/srv/monit$ ls
cfg  hostdisk  logs
crab3@crab-dev-tw02:/data/srv/monit$ python
bash: python: command not found
crab3@crab-dev-tw02:/data/srv/monit$ ls -alh
total 4.2M
drwxr-xr-x. 5 root  root   45 Aug 12 11:37 .
drwxr-xr-x. 4 root  root   30 Aug 12 11:37 ..
drwxr-xr-x. 2 crab3 1399    6 Apr 30  2024 cfg
drwxr-xr-x. 4 crab3 1399   29 Apr 30  2024 hostdisk
drwxr-xr-x. 2 crab3 1399 6.5M Aug 12 10:13 logs
crab3@crab-dev-tw02:/data/srv/monit$ python3 /data/srv/monit/ReportRecallQuota.py
```
[5] Our `cicd/monit_pypi/Dockerfile` looks good, it's confusing me more why `/data/srv/monit` was left empty like in [4]
```Dockerfile
ARG BASE_TAG=latest
FROM registry.cern.ch/cmscrab/crabtaskworker:${BASE_TAG}

RUN pip install --user pandas 

RUN mkdir -p /data/srv/monit/
COPY ./src/python/ServerUtilities.py           \
     ./src/python/RESTInteractions.py          \
     ./src/script/Monitor/GenerateMONIT.py     \
     ./scripts/Utils/CheckTapeRecall.py        \
     ./src/script/Monitor/aso_metrics_ora.py   \
     ./src/script/Monitor/ReportRecallQuota.py \
     /data/srv/monit

ENV PYTHONPATH=/data/srv/current/lib/python/site-packages:${PYTHONPATH:-}

ENV RUCIO_HOME=/cvmfs/cms.cern.ch/rucio/current/
ENV RUCIO_ACCOUNT="crab_server"
# no need to source a rucio environment from cvmfs. rucio client is already installed
# via pip, do not pollute the python env with things you do not need!
# ENV PYTHONPATH=$PYTHONPATH:/cvmfs/cms.cern.ch/rucio/x86_64/el9/py3/current/lib/python3.9/site-packages/
# ENV PYTHONPATH=$PYTHONPATH:/cvmfs/cms.cern.ch/rucio/x86_64/el8/py3/current/lib/python3.6/site-packages/

ENTRYPOINT ["tini", "--"]

CMD bash
# CMD python3 /data/srv/monit/GenerateMONIT.py
# CMD python3.8 /data/srv/monit/CheckTapeRecall.py
    # cp -v RecallRules.html /data/eos/RecallRules-docker.html
    ## we decided to send data to opensearch instead of saving it to eos. no need to copy the file.
```

[6] `runContainer.sh` wish to mount volume only specific stateful paths for writing monitoring states e.g. cfg, logs. 
So it's likely not the culprit who wiped out copied monit scripts.
```bash
#list of directories that should exist on the host machine before container start
dir=("/data/container/${SERVICE}/cfg" "/data/container/${SERVICE}/logs")

case $SERVICE in
  TaskWorker_monit*)
    DIRECTORY='monit'
    ;;
  TaskWorker*)
    DIRECTORY='TaskManager'
    ;;
  Publisher*)
    DIRECTORY='Publisher'
    dir+=("/data/container/${SERVICE}/PublisherFiles")
    ;;
  *)
    echo "$SERVICE is not a valid service to start. Specify whether you want to start one of the 'Publisher' variants or 'TaskWorker'." && helpFunction
esac

volumeMounts=()
for d in "${dir[@]}"; do
  if [ -e "$d" ]; then
      volumeMounts+=("-v ${d}:/data/srv/${DIRECTORY}/$(basename "${d}")")
```

## Comment (nausikt, 2025-08-12T12:42:05Z)

Do you guys have any clues why monit scripts were missing from `crabtwmonit` image?

## Comment (nausikt, 2025-08-12T13:17:01Z)

Stefano found the culprit, there's some corrupted image, leaked to our `v3.latest` 2 weeks ago.
```
REPOSITORY                                TAG                IMAGE ID       CREATED        SIZE
registry.cern.ch/cmscrab/crabtwmonit      v3.250812-stable   5cb24269e6a8   5 hours ago    3.18GB
registry.cern.ch/cmscrab/crabtaskworker   v3.250812-stable   ef200b9b7ff3   5 hours ago    3.02GB
registry.cern.ch/cmscrab/crabtwmonit      <none>             58d0c120aace   20 hours ago   3.18GB
registry.cern.ch/cmscrab/crabtwmonit      <none>             e80305c5bd3e   29 hours ago   3.18GB
registry.cern.ch/cmscrab/crabtwmonit      <none>             29d830130442   6 days ago     3.18GB
registry.cern.ch/cmscrab/crabtwmonit      <none>             5cf76b89c47c   7 days ago     3.18GB
registry.cern.ch/cmscrab/crabtwmonit      v3.latest          e9d720f07837   2 weeks ago    253MB
```

## Comment (nausikt, 2025-08-12T13:19:31Z)

Thanks to Stefano! `docker pull registry.cern.ch/cmscrab/crabtwmonit:v3.latest` solved the issue, we'll leave puppet to overwritten commented out cron for us then.
```
REPOSITORY                                TAG                IMAGE ID       CREATED          SIZE
registry.cern.ch/cmscrab/crabtwmonit      v3.latest          0dd1eb5ecfb9   22 minutes ago   3.18GB
```

## Comment (belforte, 2025-08-12T13:42:09Z)

I do not think that we had a truncated image for 2 weeks. It is more likely that the part of the CI pipeline which updates `crabtwmonit:v3.latest` in `crab-dev-tw02` had a problem and both failed to move the tag to a newer image (there are a5 more recent than two weeks and with a proper size) and somehow truncated the old one. The "truncated" is somehow hard to believe, but unless we go dig into CI logs, and may be not even there.
Yet.. a truncated image should not even start, so we really got a very odd thing !!
I do not see any image with 253 MB of size in Harbor for crabtwmonit going back to early July.
I suggest not to spend more time and remember the "check the v3.latest image" in case of similar problems in the future.

## Comment (nausikt, 2025-08-12T13:44:03Z)

Thank you for insightful conclusion!
