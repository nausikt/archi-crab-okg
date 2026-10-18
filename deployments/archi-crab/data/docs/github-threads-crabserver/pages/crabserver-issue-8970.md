# dmwm/CRABServer issue #8970: switching to new CMSWeb testbed cluster regarding the old testbed decommissioning

State: closed
Opened: 2025-03-07T12:00:47Z
Closed: 2025-04-01T23:04:40Z
Labels: Priority: High, Area: Code Cleanup, Area: zK8s, Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8970

## Opening post (nausikt, 2025-03-07T12:00:47Z)

Since 19th Feb, testbed Decommisioning intervention.

I've to make sure that
- [x] our CI/CD pipelines all point to new testbed with new kubeconfig.
- [x] we have write-up, short instruction guide, for CRAB folks for the switching.
- [x] cmscrab doc was updated regarding the new preprod/testbed.

## Comment (nausikt, 2025-04-01T23:04:40Z)

I'm sorry you guy for extremely late on this one. Should be done since 19th Feb my bad indeed on poor read and prioritization. Now, our pipeline works along side with new testbed as expected as you can see below.
```
[kphornsi@lxplus916 ~]$ curl --cert $X509_USER_PROXY --key $X509_USER_PROXY "https://cmsweb-testbed.cern.ch/crabserver/preprod/info"
{"desc": {"columns": ["null"]}, "result": [
 {"crabserver": "Welcome", "version": "pypi-preprod-1743545289"}
]}
```

I will write-up about how to did these in k8s on our cmscrab doc. In my case, it's very trivial since Aroosha & Wa already did most of the work for us in new testbed & gitlab, all i have to do is set the right token in gitlab. Thanks to them!
