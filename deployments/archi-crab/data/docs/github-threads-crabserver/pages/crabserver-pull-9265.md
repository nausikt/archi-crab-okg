# dmwm/CRABServer pull request #9265: Migration to Alma9 with py3.9 on CRABServer & TW

State: closed
Opened: 2026-01-21T08:18:04Z
Closed: 2026-03-03T15:45:29Z
Merged: 2026-03-03T15:45:29Z
Labels: Priority: Medium, PR: do not merge, alma9
URL: https://github.com/dmwm/CRABServer/pull/9265

## Opening post (nausikt, 2026-01-21T08:18:04Z)

Regarding #9252, https://github.com/dmwm/CRABServer/issues/8956#issuecomment-3760038590

This is a `DO NOT MERGE` PR that lift to Alma9 env on **test14** for further testing and referencing.
*P.S. I did some quick test for [normal task](https://cmsweb-test14.cern.ch/crabserver/ui/task/260120_162232%3Akphornsi_crab_test_CMSSW_15_2026_test14_wmaget_alma9_base_2) and some [regression test with pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13821508) on test14, and they all went well. I will make few more refinements before testing it thoroughly.*

## Comment (cmsdmwmbot, 2026-01-21T08:21:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2720/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-01-27T14:21:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2727/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-01-27T14:32:57Z)

while it is good to have py3.12 compatible code, do you really want to go through the extra complexity of installing a different python version than what the OS brings, given that we do not **need** any py3.12 feature ?

## Comment (nausikt, 2026-01-27T14:35:27Z)

No man, there is a lot need to be improve here actually still more to come, but got stuck with latest `cmsweb/cmsweb:wmfreeze` a bit.

## Comment (nausikt, 2026-01-27T14:43:06Z)

also have a problem with `tnsnames.ora` that we used to pick-up from `cmsweb/cmsweb` image.

I wonder why we don't have it explicitly in `crabtaskworker`.

do we actually need (to call) oracle from TaskWorker or we just completely use http call to crabserver to interact with oracle on behalf of TW.

## Comment (belforte, 2026-01-27T14:58:36Z)

Only CRABServer interacts with Oracle. We do not need tnsnames.ora in TW.
For CRABServer it ibetter to use dnf from CERN repository directly, which is guaranteed to be up to date, rather than copy from cmsweb which must in turn be rebuilt with new file in order to work. Again.. when images were build on Debian, people had to copy files around, but CERN Oracle Support maintains the names needed for CERN Oracle servers in CERN rpm repo.

## Comment (belforte, 2026-01-27T14:59:30Z)

CRABServer's main function is to be a REST interface in front of Oracle which supports X509 authentication :-)

## Comment (nausikt, 2026-01-27T15:05:29Z)

> Only CRABServer interacts with Oracle. We do not need tnsnames.ora in TW. For CRABServer it ibetter to use dnf from CERN repository directly, which is guaranteed to be up to date, rather than copy from cmsweb which must in turn be rebuilt with new file in order to work. Again.. when images were build on Debian, people had to copy files around, but CERN Oracle Support maintains the names needed for CERN Oracle servers in CERN rpm repo.

Okkk got it, forgive me the internal links (for tnsnames repo) might works with the right gpg key i should have try the links.

## Comment (nausikt, 2026-01-27T15:13:55Z)

Okk, do you see us migrating to Alma9 for CRABServer as well? @belforte 

Otherwise i will simply drop `Oracle` from TW, cleaning up.

## Comment (belforte, 2026-01-27T15:16:36Z)

Yes. Well.. that's the only "challenging" one. I think that TW should work on Alma9 with only the python dependencies (which should be easier if we stick with the python which comes with the OS).

You can certainly drop Oracle from TW image !!!

## Comment (belforte, 2026-01-27T15:20:54Z)

the CERN KB page has the repository URL's but not the much more handy files to be placed in the repo list. Maybe you can copy from `/etc/yum-puppet.repos.d/Oracle-InstantClient-OL9.x.repo` on lxplus9

so that you use `dnf install Oracle-InstantClient-OL9.x` etc

## Comment (belforte, 2026-01-27T15:25:53Z)

or lookup the `cernoracle::clients` class in puppet. I do not know from the top of my head how to find those in CERN repositories, but I think Ediz should be familiar with CERN puppet

## Comment (belforte, 2026-01-27T15:30:13Z)

N.B. https://linuxsoft.cern.ch is only accessible from inside CERN. If you at home, you need to use tunnel

## Comment (nausikt, 2026-01-27T15:30:14Z)

No worries man, i've find the way to embedded CERN repos installation in Dockerfile for ease of change. let's me cleans things up before getting to that. i guessed if we came from CERN puppet, we might have to find the way to mounted those repo file into the container.

## Comment (cmsdmwmbot, 2026-01-27T15:34:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2728/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-01-27T15:35:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2729/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-01-27T15:56:07Z)

[cmsweb/Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/2f52b8ef238cdace2555f15ae8ab74da277e56e3/docker/cmsweb/Dockerfile#L11-L17) way to install cern repo, i guessed they have some specific vm for building where all local repo ready there either via manually fetching, cvmfs or puppet.

## Comment (cmsdmwmbot, 2026-01-27T16:10:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2730/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-01-27T16:50:33Z)

cool. Maybe Docker ADD commands understand the `https://` and uses wget ? Those URL's appear to point to the needed repo files for yum.

## Comment (belforte, 2026-01-27T16:51:18Z)

of course you may need to be on CERN LAN for that to work

## Comment (cmsdmwmbot, 2026-01-27T16:52:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2731/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-01-27T17:31:03Z)

OK, right now we *no longer* relied on `wmagent-base` and `dmwm-base` layers for both **CRABServer** and **TaskWorker**. 
*(both now operating in Alma9 with py3.9)*

And this way we also ***Agnostic*** to the building machine. 
\*\**I built it on my laptop, with my lxtunnel down. i guessed CERN oracle repo are mirrored repo? still considered to be public unlike repo for **tnsnames.ora**.*\*\*

And Yes, we still have a *little* problem with *only* *sensitive* artifact left (***tnsnames.ora***) which actually best to be mounted at run-time or building time.

But Valentine's way of abstracting problem for everyone by layering are paid-off here. [cmsweb:cmsweb/Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/2f52b8ef238cdace2555f15ae8ab74da277e56e3/docker/cmsweb/Dockerfile#L11-L170)

So any image that derived from `cmsweb/cmsweb` for just picking some sensitive artifacts (things required gpgkey,authens,internal) will be available here. and if the image (also ours) was forced --no-cache rebuilding it will be refreshed, propagating to downstream images well.

_______
Therefore i highly recommended, keep the following this way, should be least confusing to the new operator.
```Dockerfile
FROM registry.cern.ch/cmsweb/cmsweb:wm-freeze AS cmsweb
COPY --from=cmsweb /etc/tnsnames.ora /etc/tnsnames.ora
```
Another remaining derivation is just *cmsweb* utilities commands for debugging inside the container. that we better keep it that way too.
```Dockerfile
FROM registry.cern.ch/cmsweb/exporters:20250519-stable AS exporters
COPY --from=exporters /data/cmsweb-ping /usr/bin/cmsweb-ping
COPY --from=exporters /data/process_exporter /usr/bin/process_exporter
COPY --from=exporters /data/cpy_exporter /usr/bin/cpy_exporter
COPY --from=exporters /data/process_monitor.sh /usr/bin/process_monitor.sh
```

That's all derivations left, coupling with `cmsweb` base images. Hopefully it allow us to gain full control during freezing time.

## Comment (cmsdmwmbot, 2026-01-27T17:51:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2732/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-01-27T20:58:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2733/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-16T12:11:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 30 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2735/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-16T12:24:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2736/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-02-16T12:37:02Z)

- [x] now, gfal was installed via mirror CERN epel 9 repo.
- [x] and Thanks to ldap dep were removed by @belforte! (https://github.com/dmwm/CRABServer/issues/9224), and was completely drop from TW build in [#9269](https://github.com/dmwm/CRABServer/pull/9269/changes). So, i've done the same here in Dockerfile for Alma9 build.
- [x] there is a little issue, when pip install try to do some isolation-env building for rucio-clients and somehow it can't retrieving setuputils and pkg_resources modules in any pypi index, So i did force them to not build in isolation env, and using system-wide env instead where setup-tools and wheel available thus solved the issue.
______
will proceeding to test it more extensively, 
- should/shall we have a release? to be well tested in preprod. 
*also other stuffs like `acceleratorParams` that i have added in twiki docs but not released yet.*

## Comment (nausikt, 2026-02-19T11:04:23Z)

This task [260216_121229:crabint1_crab_collector](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/70044030) in pipeline test suite, who try to test againt `cmsgwms-collector-itb.cern.ch` collector, seems stuck at JobStatus=1 (idle) forever somehow [1] 

Eventhough, there is a slot willing to run our test jobs but it turned out unusually busy? 
(*its been idling for at least 3 days now*).
 or may be it just because my priority got low? I will try again after sometime. 

[1] `condor_q 3056366 -better-analyze`
```bash
[crabint1@vocms068 260216_121229:crabint1_crab_collector]$ condor_q 3056366 -better-analyze
-- Schedd: crab3@vocms068.cern.ch : <137.138.62.197:4080?...
The Requirements expression for job 3056366.000 is

    (stringListMember(TARGET.Arch,REQUIRED_ARCH)) && (TARGET.OpSys == "LINUX") &&
    (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) &&
    (TARGET.HasFileTransfer)

    [0]    : stringListMember(TARGET.Arch,REQUIRED_ARCH)
    [1]    : TARGET.OpSys == "LINUX"
    [2]    : [0] && [1]
    [3]    : TARGET.Disk >= RequestDisk
    [4]    : [2] && [3]
    [5]    : TARGET.Memory >= RequestMemory
    [6]    : [4] && [5]
    [7]    : TARGET.HasFileTransfer
    [8]    : [6] && [7]

Job 3056366.000 defines the following attributes:

    RequestDisk = 100000 (kb)
    RequestMemory = 2000 (mb)
    REQUIRED_ARCH = "X86_64"

The Requirements expression for job 3056366.000 reduces to these conditions:

        Slots
Step   Matched  Condition
----- --------- ---------
[0]           2  stringListMember(TARGET.Arch,REQUIRED_ARCH)
[1]           2  TARGET.OpSys == "LINUX"
[3]           2  TARGET.Disk >= RequestDisk
[5]           2  TARGET.Memory >= RequestMemory
[7]           2  TARGET.HasFileTransfer


3056366.000:  Run analysis summary ignoring user priority.  Of 2 slots on 1 machines,
      0 slots are rejected by your job's requirements
      1 slots reject your job because of their own requirements
      1 slots match and are willing to run your job
```

## Comment (belforte, 2026-02-19T14:01:32Z)

maybe as simple as a problem with ITB ? If only this job is idle, I surely would not worry.

## Comment (belforte, 2026-02-19T14:03:09Z)

it is **extremly** difficult to use `condor_q analyze` in a glideInWms world.

## Comment (nausikt, 2026-02-19T14:08:44Z)

Okk, will proceed to test other areas like AS.🫡

## Comment (belforte, 2026-02-19T14:45:13Z)

looks like there is no pilot running in ITB

belforte@vocms068/~> condor_status
belforte@vocms068/~> 

you can of course get Florian involved, but we surely do not need this test to validate the build !

## Comment (nausikt, 2026-02-23T13:54:41Z)

Guys, I've tested via [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/14053136) and [AutomaticSplitting task](https://cmsweb-test14.cern.ch/crabserver/ui/task/260223_131618%3Akphornsi_crab_test14-automatic-splitting-CMSSW-16-py312-compatible) on test 14! and they went well.

A few things left to test that i can think of are
- RenewRemoteProxies.py
- Other monit scripts that has to be run inside tw_monit image (which derived from this TW built).
- anything else?  

I think it’s ready to merge. We can trigger a release build and deploy to preprod to verify the monitoring image and test the remaining items.

## Comment (belforte, 2026-02-23T14:06:49Z)

let's not be paranoid. It is a rebuild, not a re-code. "it runs" is test enough imho.
I think the most important is to make sure that we are covered for dependencies which the TW standard tests do not exercise. Like pandas. SO please check the monitoring scripts.

## Comment (nausikt, 2026-02-24T21:19:47Z)

I've manually rebuild Alma9 `crabtwmonit` image with tag:`pypi-test14-1771243616` [1], and tested monit scripts [2] & RenewRemoteProxies [3]. everything look fine, anything else you guys think should be test?

[1] rebuild/derive from Alma9 tw image.
```
IMAGE_TAG=pypi-test14-1771243616
docker build --build-arg BASE_TAG=$IMAGE_TAG -t registry.cern.ch/cmscrab/crabtwmonit:$IMAGE_TAG -f cicd/monit_pypi/Dockerfile .
docker push registry.cern.ch/cmscrab/crabtwmonit:$IMAGE_TAG
```
[2] All monitoring script look fine, they exit with 0.
```
[crab3@crab-dev-tw05 ~]$ bash /home/crab3/runContainer.sh -v pypi-test14-1771243616 -s TaskWorker_monit_generatemonit -c 'python3 /data/srv/monit/GenerateMONIT.py'

bash /home/crab3/runContainer.sh -v pypi-test14-1771243616 -s TaskWorker_monit_checktaperecall -c 'python3 /data/srv/monit/CheckTapeRecall.py'

bash /home/crab3/runContainer.sh -v pypi-test14-1771243616 -s TaskWorker_monit_asometrics -c 'python3 /data/srv/monit/aso_metrics_ora.py'

bash /home/crab3/runContainer.sh -v pypi-test14-1771243616 -s TaskWorker_monit_reportrecallquota -c 'python3 /data/srv/monit/ReportRecallQuota.py'
0
1
TaskWorker_monit_generatemonit
Unable to find image 'registry.cern.ch/cmscrab/crabtwmonit:pypi-test14-1771243616' locally
pypi-test14-1771243616: Pulling from cmscrab/crabtwmonit
....
Digest: sha256:eee7d0c0954590c2fc4400843e0e914fb0a1f37791b9b24ffd4c91962b3393c6
Status: Downloaded newer image for registry.cern.ch/cmscrab/crabtwmonit:pypi-test14-1771243616
TaskWorker_monit_* detected, waiting for it to finish...
Sleeping for 3 seconds.
0
0
TaskWorker_monit_* detected, waiting for it to finish...
Sleeping for 3 seconds.
0
0
TaskWorker_monit_* detected, waiting for it to finish...
Sleeping for 3 seconds.
0
0
TaskWorker_monit_* detected, waiting for it to finish...
Sleeping for 3 seconds.
```
[3] RenewRemoteProxies went well but it still stick with old `classad, htcondor` somehow so i  did test with `classad2 as classad` and `htcondor2 as htcondor` since in new image env it seems to have/enforce only v2 interface may be because we bumped it to aligned with wmfreeze? or did i missed something here?
```
python ./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Skipping refresh of proxy for task 260224_081241:crabint1_crab_transferOutputs because it still has a lifetime of {int(lifetime/3600)} hours.
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Skipping refresh of proxy for task 260224_082032:crabint1_crab_disableAutomaticOutputCollection because it still has a lifetime of {int(lifetime/3600)} hours.
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Skipping refresh of proxy for task 260126_185821:crabint1_crab_20260126_195818 because it still has a lifetime of {int(lifetime/3600)} hours.
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Skipping refresh of proxy for task 260223_161401:crabint1_crab_extraJDL because it still has a lifetime of {int(lifetime/3600)} hours.
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Done updating proxies for schedd crab3@vocms059.cern.ch
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Updating tasks in schedd crab3@vocms068.cern.ch
Tue, 24 Feb 2026 22:14:29 CET(+0100):DEBUG:RenewRemoteProxies Trying to locate schedd.
Tue, 24 Feb 2026 22:14:29 CET(+0100):ERROR:RenewRemoteProxies Unable to update all proxies for schedd crab3@vocms068.cern.ch
Traceback (most recent call last):
  File "/data/repos/CRABServer/./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 209, in execute
    self.execute_schedd(schedd_name, collector)
  File "/data/repos/CRABServer/./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 146, in execute_schedd
    self.logger.debug("Schedd found at %s", schedd_ad['MyAddress'])
TypeError: 'NoneType' object is not subscriptable
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Updating tasks in schedd crab3@vocms069.cern.ch
Tue, 24 Feb 2026 22:14:29 CET(+0100):DEBUG:RenewRemoteProxies Trying to locate schedd.
Tue, 24 Feb 2026 22:14:29 CET(+0100):ERROR:RenewRemoteProxies Unable to update all proxies for schedd crab3@vocms069.cern.ch
Traceback (most recent call last):
  File "/data/repos/CRABServer/./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 209, in execute
    self.execute_schedd(schedd_name, collector)
  File "/data/repos/CRABServer/./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 146, in execute_schedd
    self.logger.debug("Schedd found at %s", schedd_ad['MyAddress'])
TypeError: 'NoneType' object is not subscriptable
Tue, 24 Feb 2026 22:14:29 CET(+0100):INFO:RenewRemoteProxies Updating tasks in schedd crab3@vocms0106.cern.ch
Tue, 24 Feb 2026 22:14:29 CET(+0100):DEBUG:RenewRemoteProxies Trying to locate schedd.
Tue, 24 Feb 2026 22:14:29 CET(+0100):DEBUG:RenewRemoteProxies Schedd found at <188.184.80.88:4080?addrs=[2001-1458-201-e3--100-52]-4080+188.184.80.88-4080&alias=vocms0106.cern.ch&noUDP&sock=schedd_5602_15a3>
```

## Comment (belforte, 2026-02-25T08:25:33Z)

thanks Krittin. About [3], is that log before of after the change to `htcondor2` ? It was "stuck" with old condor v1 API because at the time I did the transition the remote proxy renewal was not available in v2 API. That should have been fixed in more recent condor versions.
Otherwise this looks all fine to me.

## Comment (nausikt, 2026-02-25T08:28:21Z)

thanks Stefano, it's after the change to `htcondor2`.

## Comment (belforte, 2026-02-25T09:13:41Z)

rats. So we need to find out about
  File "/data/repos/CRABServer/./src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 146, in execute_schedd
    self.logger.debug("Schedd found at %s", schedd_ad['MyAddress'])
TypeError: 'NoneType' object is not subscriptable

is this in a TW where I can login and investigate ?

## Comment (belforte, 2026-02-25T10:00:12Z)

I think the error is because we list 068/069 (ITB AP's) together with global pool's AP's in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/data/hostgroup/vocmsglidein/crabtaskworker.yaml?ref_type=heads

We should improve the message to be "AP such and such not found in collector such and such"

Indeed currently in production we have the message
```
2026-02-24 23:41:26,696:INFO:RenewRemoteProxies:Updating tasks in schedd crab3@vocms068.cern.ch
2026-02-24 23:41:26,696:DEBUG:RenewRemoteProxies:Trying to locate schedd.
2026-02-24 23:41:27,003:ERROR:RenewRemoteProxies:Unable to update all proxies for schedd crab3@vocms068.cern.ch
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 209, in execute
    self.execute_schedd(schedd_name, collector)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Recurring/RenewRemoteProxies.py", line 145, in execute_schedd
    schedd_ad = collector.locate(htcondor.DaemonTypes.Schedd, schedd_name)
  File "/usr/local/lib/python3.8/site-packages/htcondor/_lock.py", line 70, in wrapper
    rv = func(*args, **kwargs)
htcondor.HTCondorLocateError: Unable to find daemon.
```

I am not sure atm how best to deal with a single list of AP's which are in two HTC pools, i.e. is there would be any drawback in listing in the YAML file only production AP's, not ITB ones. All in all we already indicate the pool there.

## Comment (nausikt, 2026-02-26T12:01:41Z)

Thanks for your comments Stefano! Will find convergence.

## Comment (cmsdmwmbot, 2026-02-27T14:46:34Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2741/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-27T14:55:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2742/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-27T15:04:34Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2743/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-27T15:16:35Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2744/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-27T16:58:33Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2745/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-02-27T18:56:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 52 warnings and errors that must be fixed
   * 7 warnings
   * 414 comments to review
 * Pycodestyle check: succeeded
   * 695 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2747/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-02T11:22:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 52 warnings and errors that must be fixed
   * 7 warnings
   * 414 comments to review
 * Pycodestyle check: succeeded
   * 695 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2748/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-03-02T17:13:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 52 warnings and errors that must be fixed
   * 7 warnings
   * 414 comments to review
 * Pycodestyle check: succeeded
   * 695 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2749/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-03-03T15:43:21Z)

I missed your last comment around wmc-httpd, converged!

## Comment (nausikt, 2026-03-03T15:45:16Z)

Thanks for your thoughtful reviews & comments, will merged it now.

## Comment (cmsdmwmbot, 2026-03-03T15:47:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 52 warnings and errors that must be fixed
   * 7 warnings
   * 414 comments to review
 * Pycodestyle check: succeeded
   * 695 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2750/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-30T07:59:11Z)

@nausikt this PR still has "DRAFT" in the title. Was it fully tested ? Shall we create a new tag, make sure that it works and deploy new alma9 containers everywhere ?

## Comment (nausikt, 2026-03-30T08:05:53Z)

> @nausikt this PR still has "DRAFT" in the title. Was it fully tested ? Shall we create a new tag, make sure that it works and deploy new alma9 containers everywhere ?

Sure, Stefano, let me do further regression tests on the new release.
