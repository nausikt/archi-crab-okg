# dmwm/CRABServer issue #8437: use voms-clients-java in PyPI container

State: closed
Opened: 2024-05-29T08:35:57Z
Closed: 2024-05-29T09:36:32Z
Labels: Status: Done, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8437

## Opening post (belforte, 2024-05-29T08:35:57Z)

we have determined that voms-client v2 (C++)  present in wma image which we use as base does not work with new IAM server (cms-auth) [1],
while the v3 (Java) is OK

Situation with C++ client is confused, since in the wma image we have `Version: 2.1.0` which works with old VOMS servers but not with new one, while in the host we have `Version: 2.1.1` which works on both.  We also have  `Version: 2.1.1` in the rpm-based container (Debian repo vs. epel repo ?)

Anyhow, since CERN deploys the Java client on lxplus* now, we can do the same.

The debian package name is `voms-clients-java` and change should go in https://github.com/dmwm/CRABServer/blob/886a75271ac769a56ef7eb1bf016d649b3c4ff3a/cicd/crabtaskworker_pypi/Dockerfile#L60



[1]
```
# verify that I am inside the container
#
crab3@crab-dev-tw02:/data/srv/TaskManager$ ps 1
    PID TTY      STAT   TIME COMMAND
      1 pts/0    Ss     0:01 tini -- /data/run.sh
#
# the C++ client
#
crab3@crab-dev-tw02:/data/srv/TaskManager$ voms-proxy-init2 --version
voms-proxy-init
Version: 2.1.0
Compiled: Jul 24 2020 08:53:00
crab3@crab-dev-tw02:/data/srv/TaskManager$ voms-proxy-init2 --cert /data/certs/servicecert.pem --key /data/certs/servicekey.pem -voms cms -out /tmp/dummy 
Your identity: /DC=ch/DC=cern/OU=computers/CN=tw/crab-dev-tw02.cern.ch
Cannot open fileFilename=/home/crab3/.rnd
Function: RAND_load_file
Creating temporary proxy ................................................................................................................................. Done
Contacting  voms-cms-auth.app.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch] "cms" Failed

Error: Server Answer was incorrectly formatted.

None of the contacted servers for cms were capable
of returning a valid AC for the user.
#
# the Java client (after apt-get install executed as root)
#
crab3@crab-dev-tw02:/data/srv/TaskManager$ voms-proxy-init3 --version
voms-proxy-init v. 3.3.2 (voms-api-java/3.3.2 canl/2.6.0 bcprov/1.68.0 bcpkix/1.68.00.0)
crab3@crab-dev-tw02:/data/srv/TaskManager$ voms-proxy-init3 --cert /data/certs/servicecert.pem --key /data/certs/servicekey.pem -voms cms -out /tmp/dummy 
Contacting voms-cms-auth.app.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/dummy.

Your proxy is valid until Wed May 29 20:26:46 UTC 2024
crab3@crab-dev-tw02:/data/srv/TaskManager$ 

```
