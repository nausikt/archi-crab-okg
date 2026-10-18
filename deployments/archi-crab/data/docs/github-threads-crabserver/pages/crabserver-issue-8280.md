# dmwm/CRABServer issue #8280: add a REST API to allow operators to upload to  a public S3 bucket

State: open
Opened: 2024-03-13T13:39:09Z
Labels: Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/8280

## Opening post (belforte, 2024-03-13T13:39:09Z)

this will make it easier to produce files/table/html's in our containers

Should probably create an ad-hoc bucket in S3. Not clear if automatic objects removal after some time would be useful or harmful

We also need a way to make reading public but write restricted. Maybe S3 allows this. Old [test collection](https://github.com/belforte/utils/blob/master/notebooks/BotoTests.ipynb) does not cover this.

## Comment (belforte, 2024-03-13T14:16:39Z)

we even have an example https://openstack.cern.ch/api/swift/containers/crab_public/object/RecallRules.html which was put here 1 year go. It does not open directly in browser though

I got that URL from https://openstack.cern.ch/project/containers/container/crab_public
maybe there is some other URL which can be used. But in the end S3 is an object store/retrieval service, not an HTML server, so it may be that there's no way. Maybe one of the following works
1. a JavaScript/JQuery/...whatever static page which downloads and show the document
2. a Grafana panel which does the same

Anyhow I know nothing about 1. and too little about 2.

## Comment (belforte, 2024-03-13T14:17:27Z)

@mapellidario let me know if this is needed or not and in case which priority to give. Unless of course you want to do it yourself

## Comment (novicecpp, 2024-03-13T14:20:16Z)

You can access the s3 object directly via `https://s3.cern.ch/<bucket_name>/<object_path>`. 
E.g., https://s3.cern.ch/crab_public/RecallRules.html

## Comment (belforte, 2024-03-13T21:11:56Z)

this works as well
https://crab_public.s3.cern.ch/RecallRules.html
and it is what we documented years ago and I had fully forgotten

https://docs.google.com/document/d/15fKJ-AgMVlN3Y5mlnb8gar7iLm5V9sNlaGNzfWSUqSY/edit#bookmark=id.qcsoy1k1u4fp
linked to from https://github.com/dmwm/CRABServer/wiki/S3-for-CRAB

good that there is consistency !
