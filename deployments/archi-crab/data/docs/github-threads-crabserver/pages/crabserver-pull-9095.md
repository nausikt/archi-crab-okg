# dmwm/CRABServer pull request #9095: use docker dns

State: closed
Opened: 2025-05-27T08:28:39Z
Closed: 2025-05-27T11:39:19Z
Merged: 2025-05-27T11:39:19Z
URL: https://github.com/dmwm/CRABServer/pull/9095

## Opening post (aspiringmind-code, 2025-05-27T08:28:39Z)

Fix #9074 
Tested on crab-dev-tw03
```
[vchakrav@crab-dev-tw03 ~]$ ./runContainer.sh -v v3.250509-stable -s TaskWorker
Sleeping for 3 seconds.
Running containers:
CONTAINER ID   IMAGE                                                        COMMAND                  CREATED         STATUS         PORTS     NAMES
cfa2a172b870   registry.cern.ch/cmscrab/crabtaskworker:v3.250509-stable     "tini -- /data/run.sh"   3 seconds ago   Up 3 seconds             TaskWorker
```

## Comment (cmsdmwmbot, 2025-05-27T08:31:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2484/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-27T09:59:38Z)

glad that container run. Can you verify that DNS resolving works as expected ? Which of course requires to start the container to begin with :-)

## Comment (aspiringmind-code, 2025-05-27T13:01:54Z)

```
[vchakrav@crab-dev-tw03 etc]$ cat resolv.conf
# This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.
nameserver 127.0.0.53
options edns0 trust-ad
search cern.ch
[vchakrav@crab-dev-tw03 etc]$ docker exec -it TaskWorker bash
crab3@crab-dev-tw03:/data/srv/TaskManager$ cd /etc
crab3@crab-dev-tw03:/etc$ cat resolv.conf
# This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.
nameserver 127.0.0.53
options edns0 trust-ad
search cern.ch
```

## Comment (belforte, 2025-05-27T13:22:58Z)

I am afraid that I do not know enough about those things to feel reassured by a dump of /etc/resolv.cong

I know that the container does not have `tcpdump` but maybe it is worth to add so we can check ?
