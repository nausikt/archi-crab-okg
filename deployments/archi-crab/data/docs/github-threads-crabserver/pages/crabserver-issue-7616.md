# dmwm/CRABServer issue #7616: switch to cmsweb image 24022023

State: closed
Opened: 2023-04-24T21:16:58Z
Closed: 2024-04-24T12:35:20Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7616

## Opening post (belforte, 2023-04-24T21:16:58Z)

we should change
https://github.com/dmwm/CRABServer/blob/f785d252ec2153bd207127b765f8f756ffeea1cc/Docker/Dockerfile#L1
to use new image from Aroosha with new pki bundle
aside from that, it is always good to have a recent base image with latest OS

I am not sure if we have way to test other than changing and building image via Jenkins.
It would be also a good time to update documentation which still refers to
uploading to docker hub (and possibly other things have changed)
https://github.com/dmwm/CRABServer/blob/master/README.MD

I also noted that we do not have anywhere instructions on how to log on
registry.cern.ch to view list of images. When I tried I got odd errors.

## Comment (novicecpp, 2023-04-26T05:08:53Z)

Test against jenkins is good enough. I found bug on new wmcore version from those tests.

## Comment (belforte, 2023-04-26T09:04:10Z)

I agree Jenkins is enough. I was curious if we have a way to make a test build before committing a new docker build file to master.

## Comment (belforte, 2024-04-24T10:30:01Z)

has this became obsolete with the switch to new build based on python3.8 debian image ?

## Comment (novicecpp, 2024-04-24T12:35:20Z)

Yes. Also, supersedes by https://github.com/dmwm/CRABServer/pull/8278.
