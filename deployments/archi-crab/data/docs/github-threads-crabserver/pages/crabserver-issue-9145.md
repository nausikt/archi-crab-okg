# dmwm/CRABServer issue #9145: do we need CRABServer/setup.py ?

State: open
Opened: 2025-08-06T13:38:16Z
URL: https://github.com/dmwm/CRABServer/issues/9145

## Opening post (belforte, 2025-08-06T13:38:16Z)

That script is hard to understand for current maintainers, and hence a fragile point.
But.. give that we do not build rpm's any more and have no place to use pip, but can run everything by pointing PYTHONPATH to `CRABSERVER/src/python`  (or a zip file with its content).... why do we keep it around ?

We have only two "builds":
1. CRABServer (REST(
2. TaskWorker

publishers and twmonit run in the TaskWorker container, simply using a different start script.

It seems to me that our setup is only called in
https://github.com/dmwm/CRABServer/blob/82a2c5e5bffae25e2c5ce238baba5ee5970de24f/cicd/crabtaskworker_pypi/buildTWTarballs.sh#L50-L53

But what cops files from the repo clone to `/data/srv/current/lib/python/site-packages/` in the container seems to be Docker
https://github.com/dmwm/CRABServer/blob/82a2c5e5bffae25e2c5ce238baba5ee5970de24f/cicd/crabtaskworker_pypi/Dockerfile#L83-L86

Maybe `setup.py` prepares a `CRABServer/build` directory with "the files specified in setup.py" which then Docker copies. But it seems to me that it would be very easy to copy files from the GH clone w/o going through setup.py

I have not looked at CRABServer, but I suspect the only extra thing is the `/data` subdir which needs to contain the stuff for httpd (i.e. the UI).

## Comment (belforte, 2025-08-18T15:32:22Z)

@sinonkt @aspiringmind-code  without hurry, I'd like to have your opinion on this possible simplification. Feel free to add your comment in the issue
