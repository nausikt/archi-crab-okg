# dmwm/CRABServer issue #9160: jobs at CIEMAT find OSG CVMFS in their PYTHONPATH and fail stageout when using tokens

State: closed
Opened: 2025-08-25T10:52:04Z
Closed: 2025-08-25T16:50:54Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/9160

## Opening post (belforte, 2025-08-25T10:52:04Z)

somehow T2_ES_CIEMAT start jobs with `/cvmfs/oasis.opensciencegrid.org` in the environment. This makes local stageout fail with
```
  File "/usr/bin/gfal-copy", line 30, in <module>
    from gfal2_util.shell import Gfal2Shell
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/23-main/23.250814-1/el9-x86_64/usr/lib/python3.9/site-packages/gfal2_util/shell.py", line 23, in <module>
    from gfal2_util import base
  File "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/23-main/23.250814-1/el9-x86_64/usr/lib/python3.9/site-packages/gfal2_util/base.py", line 35, in <module>
    import gfal2
ImportError: libboost_python39.so.1.75.0: cannot open shared object file: No such file or directory
```

I have verified this adding `env|grep oasis` at the very beginning of gWms-CMSRunAnalysis.sh and indeed

```text
======== gWMS-CMSRunAnalysis.sh STARTING at Mon Aug 25 09:13:02 GMT 2025 on gaew0224.ciemat.es ========
User id:    uid=52301(pilcms01) gid=13998(cmspil) groups=13998(cmspil),65534(nobody)
Local time: Mon Aug 25 11:13:02 CEST 2025
Hostname:   gaew0224.ciemat.es
[...]
PYTHONPATH=/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/23-main/23.250821-1/el9-x86_64/usr/lib/python3.9/site-packages: ....
```

Note that now we pick `gfal-*` from the CMS image. Not from the WN any more.
We never noticed because when using X509 things work
```text
INFO:root:Command to run: #!/bin/bash
env -i X509_USER_PROXY=$X509_USER_PROXY JOBSTARTDIR=$JOBSTARTDIR bash -c '. $JOBSTARTDIR/startup_environment.sh;  date;  gfal-copy -t 2400 -T 2400 -p -v --abort-on-failure -K adler32 -v file:///srv/kk.root davs://srm.ciemat.es:2880/pnfs/ciemat.es/data/cms/prod/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250825_090645/0000/kk_1.root'
[...]
event: [1756113233700] DEST   http_plugin	CHECKSUM:EXIT	
INFO Event triggered: DESTINATION http_plugin CHECKSUM:EXIT 
gfal-copy exit status: 0

stderr: bash: /startup_environment.sh: No such file or directory

INFO:root:
Stage-out succeeded with the current environment.
INFO:root:attempting stageOut
INFO:root:===> Stage Out Successful: {'LFN': '/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250825_090645/0000/kk_1.root', 'PFN': 'davs://srm.ciemat.es:2880/pnfs/ciemat.es/data/cms/prod/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250825_090645/0000/kk_1.root', 'StageOutReport': [], 'PNN': 'T2_ES_CIEMAT', 'StageOutCommand': 'gfal2'}
       <----- Stageout manager log finish
```


I asked in the Facility Service Mattermost, and Stephan said that jobs should start in a clean env
https://mattermost.web.cern.ch/cms-o-and-c/pl/xc9yd5e1ntf15x9h5j55h5dhmr

## Comment (belforte, 2025-08-25T16:50:54Z)

three new things:
1. jobs work now, even with token (i.e. local stagetout to CIEMAT via davs: works)
2. gWms is supposed to clean PYTHONPATH but clearly does not do it, Marco M. says "we updated glideinWMS to 3.10.15 on august 6th"
3. CIEMAT acknowledged that they should not setup OSG wn client and removed it https://helpdesk.ggus.eu/#ticket/zoom/1000400

In conclusion, there is nothing to do on CRAB side. It was a "glitch" in cvmfs at CIEMAT (1.) which made us discover 2. and 3.

Marco M. will follow up on 2. since the design is that gWms cleans up PYTHONPATH.
