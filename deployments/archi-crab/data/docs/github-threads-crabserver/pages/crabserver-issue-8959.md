# dmwm/CRABServer issue #8959: fix inoperable test14

State: closed
Opened: 2025-02-28T11:47:35Z
Closed: 2025-06-02T16:49:25Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8959

## Opening post (nausikt, 2025-02-28T11:47:35Z)

test14 going down again, seems like obsolete crab-secret are not only reasons behind this.

The problematic error in pipeline could be seen here: https://gitlab.cern.ch/crab3/CRABServer/-/jobs/52043185

## Comment (belforte, 2025-02-28T13:02:27Z)

[28/Feb/2025:14:01:54]      File "/usr/local/lib/python3.8/site-packages/WMCore/Services/pycurl_manager.py", line 338, in request - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog
[28/Feb/2025:14:01:54]        curl.perform() - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog
[28/Feb/2025:14:01:54]    pycurl.error: (58, 'could not load PEM client certificate, OpenSSL error error:0909006C:PEM routines:get_name:no start line, (no key found, wrong pass phrase, or wrong file format?)') - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog

## Comment (nausikt, 2025-02-28T13:03:59Z)

> [28/Feb/2025:14:01:54] File "/usr/local/lib/python3.8/site-packages/WMCore/Services/pycurl_manager.py", line 338, in request - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog [28/Feb/2025:14:01:54] curl.perform() - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog [28/Feb/2025:14:01:54] pycurl.error: (58, 'could not load PEM client certificate, OpenSSL error error:0909006C:PEM routines:get_name:no start line, (no key found, wrong pass phrase, or wrong file format?)') - Podname=crabserver-7d94f6f6d4-77756 Type=cherrypylog

Thanks for hint!

## Comment (belforte, 2025-02-28T20:37:53Z)

hhmmm....

the location of the certificate is in the `crabserver/config,py` file.
data.serverhostcert = "%s/auth/crabserver/dmwm-service-cert.pem" % __file__.rsplit('/', 3)[0]

On cmsweb-test2:
```console
crab3@crabserver-6fb55ff99-27bsr:/data$ openssl x509  -subject -dates -noout  -in /data/srv/current/auth/crabserver/dmwm-service-cert.pem 
subject=DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = crabcms, CN = 852819, CN = Robot: CRAB CMS Web Service Account
notBefore=Apr 30 06:08:05 2024 GMT
notAfter=Jun  4 06:08:05 2025 GMT
crab3@crabserver-6fb55ff99-27bsr:/data$ 
```

on test14 there is a **very** old thing . I leave it to you to check there an in other clusters.

I am lead to fear that our instructions for deploying secrets are not complete/correct :-(

Please take this chance to review them.

## Comment (nausikt, 2025-05-20T12:19:43Z)

Thanks for clues & hints Stefano @belforte 
```
crab3@crabserver-757b9f9895-lpzd6:/data$ openssl x509  -subject -dates -noout  -in /data/srv/current/auth/crabserver/dmwm-service-cert.pem
subject=DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = cmswebmg, CN = 852819, CN = Robot: Service account for CMSWeb migration
notBefore=Oct 30 11:05:32 2023 GMT
notAfter=Dec  3 11:05:32 2024 GMT
```
Many things are outdated in frontend APS part as well which actually could be fixed by deploy.sh script but i will go with re-created to keep everything in-sync copied from test2, a working example, for simplicity.
P.S. grid host certs/key/pems/frontend configs of test14 cluster are out of sync in shared repos (e.g. k8s_admin_config, private frontend certificates)

## Comment (nausikt, 2025-06-02T16:49:25Z)

Finally, I made it. the re-created of test14 are working now. Thanks to Aroosha's instructions.
```
[kphornsi@lxplus925 workspace]$ crab submit -c HC_10j_test14.py
Will use CRAB configuration file HC_10j_test14.py
Enter GRID pass phrase for this identity:
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb-test14.cern.ch
Success: Your task has been delivered to the devfour CRAB3 server.
Task name: 250602_163156:kphornsi_crab_20250602_183145
Project dir: /tmp/crabStatusTracking/crab_20250602_183145
Please use ' crab status -d /tmp/crabStatusTracking/crab_20250602_183145 ' to check how the submission process proceeds.
Log file is /tmp/crabStatusTracking/crab_20250602_183145/crab.log
[kphornsi@lxplus925 workspace]$ crab status -d /tmp/crabStatusTracking/crab_20250602_183145
Rucio client intialized for account kphornsi
CRAB project directory:		/tmp/crabStatusTracking/crab_20250602_183145
Task name:			250602_163156:kphornsi_crab_20250602_183145
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - NotKnownYet
Status on the CRAB server:	WAITING on command SUBMIT
Task URL to use for HELP:	https://cmsweb-test14.cern.ch/crabserver/ui/task/250602_163156%3Akphornsi_crab_20250602_183145
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=250602_163156%3Akphornsi_crab_20250602_183145&from=1748878317000&to=now
Log file is /tmp/crabStatusTracking/crab_20250602_183145/crab.log
```
___________
### Things worth mentioned
[1] cern-authz daemonset in kube-system when they crashed all CA(s) will not properly provisioned from host node to k8s.
As you can see inside auth-proxy-server daemonset pods, `etc/grid-security/certificates/` was empty led to lot of certs issue.
```
/ # ls /proc/1/root/etc/grid-security/certificates/
/ # ls /proc/1/root/etc/grid-security
certificates
cmsweb-test14-nlkqguzvrfv2-node-0.cern.ch.grid.crt
cmsweb-test14-nlkqguzvrfv2-node-0.cern.ch.grid.key
cmsweb-test14-nlkqguzvrfv2-node-0.cern.ch.grid.pem
hostcert.pem
hostkey.pem
```
P.S. One way to fixed this issue is, For now, we have to manually bumping cern-grid-certificates image by the following patch cmd. (Thanks to CERN IT)
```
kubectl -n kube-system patch ds cern-authz --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "registry.cern.ch/kubernetes/cern-grid-certificates:0.6.7"}]'  
kubectl rollout restart -n kube-system ds cern-authz
```
[2] When we re-creating the cluster, make sure that all tls-{cert/key}.pem was properly wiped out in all nested directory of services_configs. such that deploy.sh could correctly provisioning/refreshing certs for both APS/XPS.
[3] rollout restart daemonset, help you refreshed newly provisioned key/certs in APS/XPS sometimes.
[4] APS take care of 443, XPS take care of 8443.

## Comment (belforte, 2025-06-03T09:20:09Z)

thanks @sinonkt . Since deploying cern-authz daemonset and ensuring TLS cert/keys is in CMSWEB responsibility, not CRAB, please make sure that those hints are in some place where CMSWEB people find them !

## Comment (nausikt, 2025-06-03T09:21:46Z)

> thanks [@sinonkt](https://github.com/sinonkt) . Since deploying cern-authz daemonset and ensuring TLS cert/keys is in CMSWEB responsibility, not CRAB, please make sure that those hints are in some place where CMSWEB people find them !

Acknowledge, Stefano.
