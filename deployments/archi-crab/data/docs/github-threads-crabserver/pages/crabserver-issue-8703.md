# dmwm/CRABServer issue #8703: GH repos inside TW container must be owned by crab3 user

State: closed
Opened: 2024-09-20T09:33:47Z
Closed: 2024-09-20T15:40:49Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8703

## Opening post (belforte, 2024-09-20T09:33:47Z)

looks like this
https://github.com/dmwm/CRABServer/blob/3c8607f723248dff957d6146a25162d8f8128fbb/cicd/crabtaskworker_pypi/Dockerfile#L101-L104

should be changed to be like
https://github.com/dmwm/CRABServer/blob/3c8607f723248dff957d6146a25162d8f8128fbb/cicd/crabserver_pypi/Dockerfile#L58-L63

## Comment (belforte, 2024-09-20T15:01:26Z)

@novicecpp I have tried this in my test pipeline, but it seems to have no effect.
Any idea ?

## Comment (belforte, 2024-09-20T15:07:22Z)

I guess I have to wonder if my local cicd/crabtaskworker-pypi/Docker file is really used. Maybe I must commit first ?

## Comment (novicecpp, 2024-09-20T15:09:04Z)

yes, if you use ci to build.

## Comment (belforte, 2024-09-20T15:12:18Z)

thanks for confirming. Forgive me for such a stupid mistake.
