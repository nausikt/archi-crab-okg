# dmwm/CRABServer pull request #9151: bump WMCore to 2.4.2

State: closed
Opened: 2025-08-15T11:06:53Z
Closed: 2025-08-15T19:34:32Z
URL: https://github.com/dmwm/CRABServer/pull/9151

## Opening post (nausikt, 2025-08-15T11:06:53Z)

Resolve #9150

## Comment (cmsdmwmbot, 2025-08-15T11:10:05Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2557/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T11:11:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2558/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T11:29:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2559/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T11:50:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2560/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T12:13:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2561/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T12:27:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2562/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T12:53:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2563/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-15T14:37:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2564/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-15T15:32:58Z)

may I suggest that you test things in a private branch and open a PR to master only after you managed to build working images ? Thanks.

Going to python 3.12/13 may be too much pain, but python 3.9, which is the default for alma9, should be easier and still do. I can't say why for WMCore they decided to go for 3.12. 3.9 is sort of end of life, but IIUC alma9 will be supported until 2030 and will have python 3.9

We may even consider using alma9 as base image for taskworker, instead of debian, and so we can get gfal with `yum`.

If we make our code compatible with py 3.9, it should work in python 3.12 as well.

## Comment (nausikt, 2025-08-15T16:11:24Z)

> may I suggest that you test things in a private branch and open a PR to master only after you managed to build working images ? Thanks.

Acknowledge Stefano!

> 
> Going to python 3.12/13 may be too much pain, but python 3.9, which is the default for alma9, should be easier and still do. I can't say why for WMCore they decided to go for 3.12. 3.9 is sort of end of life, but IIUC alma9 will be supported until 2030 and will have python 3.9
>
At First glance, I thought that `rucio-clients`==3X.y.z series required python 3.12++ on ward but as i've checked it works just fine for python 3.9 too, So, me neither don't know why 3.12/13 are in needed, may be some of other WMCore service's deps?

And Yes, I absolutely agree with you to Firstly migrating to 3.9 first, since it hop just 1 minor version, and python 3.8 can't works with rucio-clients 36.5.0, by other means can't works with WMCore 2.4.2.

> We may even consider using alma9 as base image for taskworker, instead of debian, and so we can get gfal with `yum`.
Right now in our image 

I saw some of WMCore practices to provisioning gfal [PR1627](https://github.com/dmwm/CMSKubernetes/pull/1627/files).
they borrow (mini)conda hands for compiling, gfal and let downstream image copying/importing it (which is the same as our current approach [2]).
[1] [docker/pypi/msunmerged/Dockerfile](https://github.com/dmwm/CMSKubernetes/pull/1627/files#diff-dda1f4922c8374213cf804fc3f9ba8dcac390a7317b791f084ef912f16e0a8be)
```Dockerfile
FROM registry.cern.ch/cmsweb/gfal:deb-py312-113-stable as gfal
FROM registry.cern.ch/cmsweb/dmwm-base:pypi-20250611-stable
ENV WDIR=/data
ENV PATH $PATH:$WDIR/miniconda/bin
ENV PYTHONPATH $WDIR/miniconda/lib/python3.8/site-packages/
WORKDIR $WDIR

# Copy Miniconda environment from gfal image
COPY --from=gfal /opt/conda /opt/conda

# Set PATH and LD_LIBRARY_PATH to use gfal2 (Miniconda) environment
ENV PATH=/opt/conda/bin:$PATH \
LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH \
PYTHONPATH=/opt/conda/lib/python3.12/site-packages:$PYTHONPATH \
```
[2]
https://github.com/dmwm/CRABServer/blob/ac6a37af7fa8fdedfbc9fbf0c1f424133bbc8927/cicd/crabtaskworker_pypi/Dockerfile#L25-L33

Would you like me to retreat to `alma9` + maintain OS-deps ourself via `apt-get`, `yum`  OS-deps list, like `cmake`, `build-estential`, `libgfal2-dev`, ... etc. that way?

IMO, Our current approach [2] is a little bit simplistic by was abstracted this way. But let me hear more of your thoughts na Stefano.

> 
> If we make our code compatible with py 3.9, it should work in python 3.12 as well.
🫡

## Comment (belforte, 2025-08-15T16:38:23Z)

there's some "history" here.
We used Debian because we wanted to keep compatibility with WMCore and they decided for Debian because Valentin insisted that the correct way to use python 3.8 was via its upstream image, which is Debian. Starting from python3.8 image sort of keeps thing minimal in size. Valentin feels very strongly about that. Alma9 would be "too much bloated" in his opinion.
Since WMCore started from Debian, they had to use all that `conda` gymnic to import gfal, which Wa copy/pasted into CRAB.
In time we learnt that gfal developers do not support the debian package/conda, but only rpm's for alma9 (so for python 3.9) and moreover they are going to stop development for gfal and there  will never be a release for anything by alma9/python3.9.
Same for Rucio, it may work with newer python, but it is currently built and deployed for alma9 and hence python3.9

Now.. why did WMCore developers picked python 3.12 ? AFAIU, in view of freezing the tool, they wanted to make sure that they did the "last transition to newer python" and went to the current top of line. I would not have done it, personally, but it is not for me to decide.

All that said, Dario already tried to build CRAB on alma9 and it went smoothly. And with some "day after wisdom", looking at what little we gained with debian, if any, I am pretty much in favor of building CRAB on alma9 and be able to use packages from CERN where people use RHEL9.

CRABServer uses cmsweb image as base, which is handy as it comes with oracle, cherrypy, sqlalchemy.... and since the only thing we do is to add some python, we should be able to get along with whatever they do. I think that our code is already compatible at least with python3.9,  and likely py3.12. What we need to adapt is setup.py (which I think Vijay did already) and then replace optparse with argparse (or the other way around, I do not remember now) as per the ad-hoc issue which we have.

Sorry for long writeup. Hope things are a bit more clear now na.  As you can see.. nothing really fundamental, just a bunch of choices among ~equivalent paths where the full implications are not known before the work is done.

P.S. I do not regard [2] above as "simplicistic", I always thought of it as an horrible complication with respect to 
`yum install 'gfal2-all python3-gfal2-util`

## Comment (cmsdmwmbot, 2025-08-15T16:40:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2565/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-15T16:40:49Z)

I suggest that you close this PR and do the work in a branch in your fork. So you can test w/o committing every edit.

## Comment (nausikt, 2025-08-15T16:49:59Z)

> there's some "history" here. We used Debian because we wanted to keep compatibility with WMCore and they decided for Debian because Valentin insisted that the correct way to use python 3.8 was via its upstream image, which is Debian. Starting from python3.8 image sort of keeps thing minimal in size. Valentin feels very strongly about that. Alma9 would be "too much bloated" in his opinion. Since WMCore started from Debian, they had to use all that `conda` gymnic to import gfal, which Wa copy/pasted into CRAB. In time we learnt that gfal developers do not support the debian package/conda, but only rpm's for alma9 (so for python 3.9) and moreover they are going to stop development for gfal and there will never be a release for anything by alma9/python3.9. Same for Rucio, it may work with newer python, but it is currently built and deployed for alma9 and hence python3.9
> 
> Now.. why did WMCore developers picked python 3.12 ? AFAIU, in view of freezing the tool, they wanted to make sure that they did the "last transition to newer python" and went to the current top of line. I would not have done it, personally, but it is not for me to decide.
> 
> All that said, Dario already tried to build CRAB on alma9 and it went smoothly. And with some "day after wisdom", looking at what little we gained with debian, if any, I am pretty much in favor of building CRAB on alma9 and be able to use packages from CERN where people use RHEL9.
> 
> CRABServer uses cmsweb image as base, which is handy as it comes with oracle, cherrypy, sqlalchemy.... and since the only thing we do is to add some python, we should be able to get along with whatever they do. I think that our code is already compatible at least with python3.9, and likely py3.12. What we need to adapt is setup.py (which I think Vijay did already) and then replace optparse with argparse (or the other way around, I do not remember now) as per the ad-hoc issue which we have.
> 
> Sorry for long writeup. Hope things are a bit more clear now na. As you can see.. nothing really fundamental, just a bunch of choices among ~equivalent paths where the full implications are not known before the work is done.
> 
> P.S. I do not regard [2] above as "simplicistic", I always thought of it as an horrible complication with respect to `yum install 'gfal2-all python3-gfal2-util`

Huge Thanks! for high resolution history! this surely save me from wasting time, figuring out this puzzles!

## Comment (belforte, 2025-08-15T19:24:34Z)

so I suggest to delay updating WMcore to when we have moved to python 3.9.
and maybe to alma9 as well.

## Comment (nausikt, 2025-08-15T19:34:32Z)

Okk, I‘ll proceed to other stuffs.
