# dmwm/CRABServer issue #9309: Publisher's PublisherFiles directory is not correctly used

State: closed
Opened: 2026-05-08T16:46:32Z
Closed: 2026-05-12T15:22:24Z
Labels: Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/9309

## Opening post (belforte, 2026-05-08T16:46:32Z)

runContainer.sh mounts `PublisherFiles` in the container
https://github.com/dmwm/CRABServer/blob/97c04445b571e98ed92e572559db1be2693a750e/src/script/Container/runContainer.sh#L52-L54
https://github.com/dmwm/CRABServer/blob/97c04445b571e98ed92e572559db1be2693a750e/src/script/Container/runContainer.sh#L61-L63
so that is available inside the container as `/data/srv/Publisher/PublisherFiles/`
but the code uses a local directory instead

```console
[crab3@crab-prod-tw01 Publisher]$ grep taskFiles current/PublisherConfig.py 
config.General.taskFilesDir = '/data/srv/Publisher_files/'
[crab3@crab-prod-tw01 Publisher]$ 
```

leaving the directory from host VM "idle"
```console
[crab3@crab-prod-tw01 Publisher]$ ls -ld /data/hostdisk/Publisher/PublisherFiles/
drwxr-xr-x. 3 crab3 1399 4096 Dec 30  2021 /data/hostdisk/Publisher/PublisherFiles/
[crab3@crab-prod-tw01 Publisher]$ 
```

while this is certainly not fatal, it means
* temporary files in `config.General.taskFilesDir` are only cleaned when container restarts so we may risk running out of space in the local container file system
* list of blacklisted tasks in https://github.com/dmwm/CRABServer/blob/97c04445b571e98ed92e572559db1be2693a750e/src/python/Publisher/PublisherMaster.py#L65 is lost every time we restart the container

Simplest solution seems to me to change the PublisherConfig.py erb template in puppet leaving everything else the same.

- [x] change locally in my dev and test  
- [x] change in qa
- [x] test in preprod 
- [x] check if changes are needed to Publisher utils script
- [x] change in master and deploy to prod
- [x] change documentation as needed
- [x] ensure that old files are cleaned: done in  [cleanTW](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/files/crabtaskworker/cleanTW.sh?ref_type=heads) crontab

## Comment (belforte, 2026-05-11T20:53:55Z)

All done, but can move `qa` to `master` in puppet because it brings new JobRouter with it. 
One possibility is to roll back JObRouter change from `qa` leaving it in `dev` only. Put back AP's in `prod` and change "by hand" vocms0198 and vocms0106, changes to JR will be lost if condor is restarted, but it is unlikely to happen. What do you think @nausikt ?

## Comment (belforte, 2026-05-12T15:22:24Z)

Lacking guidance from my devOps, I went for cherrypicking the change from qa into master. This may require a bit of work next time we merge qa into master, let's hope we do it sooner rather than later.
I then ran puppet agent on cran-prod-tw01, copied files from old to new place and restarted Publisher_schedd container. Everything is fine. Now all json work file, failed blocks dump and blacklist are persistent.
