# dmwm/CRABServer issue #8426: make sure /etc/vomses is up to date on all VM's

State: closed
Opened: 2024-05-23T13:18:16Z
Closed: 2024-05-23T14:23:21Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8426

## Opening post (belforte, 2024-05-23T13:18:16Z)

e.g. on crab-dev-tw01

in the host, everything is fine
```
[root@crab-dev-tw01 belforte]# cd /etc/vomses/
[root@crab-dev-tw01 vomses]# ls
cms-voms-cms-auth.app.cern.ch
[root@crab-dev-tw01 vomses]# 
```

but inside the container
```
[crab3@crab-dev-tw01 TaskManager]$ ps 1
    PID TTY      STAT   TIME COMMAND
      1 pts/0    Ss+    0:01 /bin/sh -c sh /data/run.sh && sh /data/monitor.sh && while true; do sleep 60;done
[crab3@crab-dev-tw01 TaskManager]$ ls /etc/vomses
cms-lcg-voms2.cern.ch  cms-voms2.cern.ch
[crab3@crab-dev-tw01 TaskManager]$ 
```

same (of course) for crab-prod-tw01
```
belforte@crab-prod-tw01/~> ls /etc/vomses
cms-voms-cms-auth.app.cern.ch
belforte@crab-prod-tw01/~> TW
[crab3@crab-prod-tw01 TaskManager]$ ls /etc/vomses
cms-lcg-voms2.cern.ch  cms-voms2.cern.ch
[crab3@crab-prod-tw01 TaskManager]$ 
```

## Comment (novicecpp, 2024-05-23T13:21:42Z)

Shall we mount it from host like /etc/grid-security?

## Comment (belforte, 2024-05-23T13:23:01Z)

Yes, I just tested it on crab-dev-tw01 and it worked like a charm.

## Comment (belforte, 2024-05-23T13:35:59Z)

we will need to restart all TW containers, of course. Good time to bet back the two workers on prod which died beacuse of problem described in #8420

## Comment (amaltaro, 2024-05-23T17:02:12Z)

@belforte this ticket caught my attention :)
Is this something that you/CRAB did alone, or together with the VoC (or whoever is currently helping with VoC activities)?

## Comment (belforte, 2024-05-23T17:19:46Z)

HA !! You ignored the mail from Lammel, even if your DN in in the list attached to it. Shame on you !

For some historical reason we, not the VOC, manage our VM's and launch our containers. So we are fixing ourselves (just add one line to the script which start containers to add one bind to docker run, even I can manage that !). Puppet on the VM was OK, but the container was built with its own hardcoded vomses, well.. it did not change for 20 years.. I thought it was safe to keep hardcoded !

As to "us vs. VOC", there are of course pro's (full control) and con's (more work), maybe we can revisit once the new VOC is here and well in control. On the good side Dario is now well trained in puppet things and will be able to help you.

## Comment (amaltaro, 2024-05-23T20:02:41Z)

LoL!
I did not, I just didn't manage to react yet to that email. I will refer to the change you made and the suggestion made by Stephan and resolve it for WM nodes as well. Thanks Stefano!

## Comment (belforte, 2024-05-23T20:24:13Z)

:+1: 
summary: insert this between `docker run` and  the command to run :
`-v /etc/vomses/:/etc/vomses/`

## Comment (belforte, 2024-05-29T07:29:20Z)

@amaltaro @todor-ivanov did you get a chance to test this ? Somehow the voms-proxy-init which we find in WMA image does not work with new vomses. Which may very well be a problem on our side. We are still investigating. It is a pretty odd situation and our voms expert (Stefano) is very puzzled.

## Comment (belforte, 2024-05-29T09:06:24Z)

Alan, Todor, FYI we ended up overriding the voms-client which comes with wma image with the java version #8437 
You may need the same before end of June

## Comment (amaltaro, 2024-05-29T10:46:56Z)

Hi Stefano, thank you for letting us know.
The `dmwm-base` image is actually importing the voms package/setup from the `cmsweb-base` image, which is still built against CC7, see: https://github.com/dmwm/CMSKubernetes/blob/master/docker/cmsweb-base/Dockerfile#L11

We haven't discussed it in the WMCore team yet, but I think we will have to create a new (cmsweb-)base image based on Alma9 and with up-to-date packages, to be then used by `dmwm-base` image. You might want to subscribe to this ticket:
https://github.com/dmwm/WMCore/issues/11997
as I predict changes happening very very soon.

## Comment (belforte, 2024-05-29T12:50:17Z)

I thought you were using an image built from `python:3.8` i.e. Debian ! i.e. https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/wmagent-base/Dockerfile. Indeed that issue refers to the Debian based image, not Alma9. And we were using voms client from there (line 6 in the above). Anyhow... I presume you will hit same error as we did and we can talk again.
