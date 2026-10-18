# dmwm/CRABServer issue #7614: TW containers must take pki bundle from host

State: closed
Opened: 2023-04-24T14:40:10Z
Closed: 2023-04-24T14:46:28Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7614

## Opening post (belforte, 2023-04-24T14:40:10Z)

CERN updated their root CA and all things stopped to work.
It came out that we take `/etc/grid-security/certificates` from the host, but that is not relevant, since SSL stuff picks first the content from `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`

We managed to updated that bundle on the VM hosts via
```
yum install -y CERN-CA-certs
update-ca-trust
```
(note that in this case `yum update` was not working ! )

But in order to make the containers use the new bundle in place of the one which was current when the base image (`cmsweb`) was created, we need to munt the bundle from the host.

More info in:
https://mattermost.web.cern.ch/cms-o-and-c/pl/gzsneygpu3b4jki1umk9x5aweh
