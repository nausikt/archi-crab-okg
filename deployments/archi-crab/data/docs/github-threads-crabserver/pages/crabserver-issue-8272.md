# dmwm/CRABServer issue #8272: test new HTCondor python bindings

State: closed
Opened: 2024-03-06T23:02:29Z
Closed: 2024-12-18T17:06:18Z
Labels: Status: Done, Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8272

## Opening post (belforte, 2024-03-06T23:02:29Z)

following up on mail thread with Todd Miller @ Madison
They are preparing a new version of HTCondor python bindings which is almost but not
fully backward compatible and would like us to get a feedback from us before finalizing.

We need to setup once TW and one scheduler where we replace htcondor python
with the new version as per
https://github.com/htcondor/htcondor/blob/main/INSTALL.md
Details to be figured out. We never did this before !

```text

-------- Forwarded Message --------
Subject: Re: testing CRAB server
Date: Wed, 6 Mar 2024 12:46:14 -0600 (CST)
From: Todd L Miller <tlmiller@cs.wisc.edu>
To: Stefano Belforte <stefano.belforte@cern.ch>
CC: Thanayut Seethongchuen <thanayut.seethongchuen@cern.ch>, Todd Tannenbaum <tannenba@cs.wisc.edu>, Dario Mapelli <dario.mapelli@cern.ch>

> Todd, send us the instructions and we'll give it a try.

https://github.com/htcondor/htcondor/blob/main/INSTALL.md

	For now, just build the 'main' branch; the new modules should show up in the python3 package.

> I really appreciate your willingness to do the work for us,
> but having us do it is overall the most efficient way.

	Thanks for your help. :)

> Chances are that anything we find can be reproduced outside
> the CRAB server.

	Probably.

> I guess it is mostly a matter of which exact calls we make with which 
> arguments.

	Exactly.  Almost all of the functions are still there, with
almost all of the same arguments.

> If we come to the point that you need to login, we will dig instructions 
> to resurrect your account. I presume that Center for High Throughput 
> Computing - University of Wisconsin which is now a CMS member 
> institution will need to add you as member. Members currently are Todd 
> Tannenbaum (as the boss) and James Frey.

	I didn't know CHTC was a CMS member institution.  That'll probably make things a lot easier. :)

-- ToddM
```

## Comment (belforte, 2024-03-06T23:14:28Z)

@todd-l-miller FYI (just a check that I got your correct GH handle)

## Comment (Todd-L-Miller, 2024-03-07T21:01:24Z)

Yup, that's me.  (Checking ability to comment...)

## Comment (novicecpp, 2024-03-08T22:25:54Z)

Just to report what I found today.

I tried to build and run CRAB with the new htcondor binding (`htcondor2`) for fun.
To build htcondor:
- I need to build htcondor from source inside `htcondor/nmi-build:x86_64_Debian11-23000100` because we use the official python:3.8 image as our baseimage, which uses Debian 11 as its baseimage.
- Because of python3.8, I need to compile and install python3.8 manually in the htcondor build image,
plus manually build libboost-python that need by htcondor build system. Otherwise, I will get htcondor2 static lib for python3.9.
- I failed to set up the build environment inside my own TaskWorker image (built on the `python:3.8` baseimage)

But, eventually, I could build it without errors. Please see the [Dockerfile](https://github.com/novicecpp/CRABServer/blob/ci_gitlab_htcondor2/cicd/htcondor2/Dockerfile_debian11) for the details.
 The steps in the Dockerfile are guess-plus-trial-and-errors until it works. I have zero knowledge of cmake, boost, and how dynamic links work.

------------------------

Next, I added the whole `release_dir` to my TaskWorker image and just exported PYTHONPATH to `$(realpath release_dir)/lib/python3`.
And, it magically works (I could do `import htcondor2 as htcondor` with python3.8 inside my image).

Still, I cannot submit jobs to Schedd yet because of API mismatch:

1.  Not accepting `bytes`

In [HTCondorLocator.py#L184](https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/HTCondorLocator.py#L184)

```python
     htcondor.param['COLLECTOR_HOST'] = self.getCollector().encode('ascii', 'ignore')
```
It raise type error but remove `.encode('ascii', 'ignore')` fix the issue.

Another place is `classad.quote` in [HTCondorLocator.py#L186](https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/HTCondorLocator.py#L186) ([line 18 in HTCondorUtils.py](https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/HTCondorUtils.py#L18) make `HTCondorUtils.quote = classad.quote`).

```python
schedds = coll.query(htcondor.AdTypes.Schedd, 'Name=?=%s' % HTCondorUtils.quote(schedd.encode('ascii', 'ignore')),
                     ["AddressV1", "CondorPlatform", "CondorVersion", "Machine", "MyAddress", "Name", "MyType",
                      "ScheddIpAddr", "RemoteCondorSetup"])
```
Also, remove `.encode('ascii', 'ignore')` fix the issue.


2.  `xquery()` method of Schedd object.

At [DagmanSubmitter.py#L330](https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/TaskWorker/Actions/DagmanSubmitter.py#L330), we use `xquery()` to get..I do not know, sorry.
But it looks like replacing it with `query()` work; I cross-checked with another server, both of them returned an empty list.
The object from htcondor2 is `<htcondor2._schedd.Schedd object at 0x7f64760d5e20>`.

3. No `htcondor.SecMan()` or similar name in `htcondor2`.

Here at [HTCondorUtils.py#L62](https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/HTCondorUtils.py#L62). I am stuck at this point. I do not know what `htcondor.SecMan()` does or which API can replace it.

That is all for today.

## Comment (Todd-L-Miller, 2024-03-09T01:54:47Z)

> I tried to build and run CRAB with the new htcondor binding 
> (`htcondor2`) for fun.

 	Thanks!  This is great.

[snip: building]

 	I'm glad you were able to get this figured out; the build 
containers are public for sadly good reason.  The version 2 bindings
don't require Boost, but we haven't made that optional for the build
system yet.

> Next, I added the whole `release_dir` to my TaskWorker image and just 
> exported PYTHONPATH to `$(realpath release_dir)/lib/python3`.
>
> And, it magically works (I could do `import htcondor2 as htcondor` with 
> python3.8 inside my image).

 	Yay!

> It raise type error but remove `.encode('ascii', 'ignore')` fix the issue.

 	Interesting.  HTCondor will generally accept UTF-8 encoding 
anywhere (so the conversion to ASCII shouldn't be necessary), but the 
version 2 bindings are generally stricter about type-checking (which is
a little un-Pythonic, but makes the C++ side of the bindings way easier
to write).

> Also, remove `.encode('ascii', 'ignore')` fix the issue.

 	Do you know if this encode() calls were added to fix problems, or 
just to be careful?

> 2.  `xquery()` method of Schedd object.

 	We had to retire xquery(); this will be called out in a transition 
guide.  The original intent of xquery() was to stream results back from
the schedd, but given that the code converts the result into a list before 
looking at it, there's clearly no concern about using too much memory 
here, which I'm glad to hear.

> 3. No `htcondor.SecMan()` or similar name in `htcondor2`.
>
> I am stuck at this point. I do not know what `htcondor.SecMan()` does 
> or which API can replace it.

 	SecMan is currently missing from the htcondor2 library.  That 
call appears to be the only place that it's being used in CRAB; I'm not
sure why the authenticated subprocess needs to reauthenticate from 
scratch, but that particular function probably shouldn't take too long to 
implement.

> That is all for today.

 	Thank you for the excellent reporting.

 	I don't know if CRAB will work properly if you just comment-out 
the call to SecMan, but even getting things to the point where it fails 
because of that missing call rather than because of any other problem with
the new bindings would be tremendous.  Thanks again for your help.

- ToddM

## Comment (belforte, 2024-03-11T10:35:56Z)

Amazing work Wa, thanks !

I can't comment/advice on building. I hope that we will not have to worry about things like python 3.8 vs. python 3.9, atm we use python3.8 in TW , python 3.6 in schedulers, same HTC major version (10) and everything is OK.

Todd let me try make 3 comments:

1. `encode{'ascii'`
Let's keep in mind that our source code is very old here. And it reflects the very first version of python bindings from Brian B. Plus was originally written in python2. So I have no idea why `encode('ascii', ignore) was used. I suspect that we could take it away also in current code and it will work. 

2. `xquery` vs. `query` 
again, from BB firs implementation, IIRC the point at the time was to be more kind on collector, by doing the equivalent of `condor_q -af p1 p2 ...` instead of `condor_q -l | egrep  .... `. We never had a worry about memory on our side. IIUC we can change  with `query` already. Happy to do so !

3. `SecMan` and `authenticated subprocess`
the extra complexity is a legacy of GSI authentication. First implementation of CRAB used a service proxy to talk with other central services and to perform "global queries to HTCondor" while inside the subprocesses which submit user jobs to schedd's (which run on different VM's) we had to switch to the specific user proxy every time. But now all interactions with HTCondor are done with a single, common token. We kept changes at minimum at the time, but I am optimistic that all of this code can be simply removed and we should make calls to condor bindings directly in TW code w/o going through a (authenticated) subprocess. 
Yet I am puzzled that `SecMan` is listed in latest bindings [doc](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html) as the only cure in case a daemon restarts and `all future commands will fail with strange connection errors.` Maybe we simply need to be sure that all collector and schedd objects which we create are in the temporary scope of some object and do not try to persist in memory for days ?

Bottom line: we can surely  profit anyhow from aligning current code to current bindings and clean up GSI legacy stuff. Then chances are that htcondor2 and classad2 work smoothly. In the end we do not to do anything more then what is the examples in the documentation ! The only non trivial
thing is that the schedd we submit to runs on a different VM. But I presume that that is part of standard tests for the bindings.
Wa did not get to test `classAd2` here, but the use we make of it should be very basic.

I am not sure about next step(s) though. We can remove 1. 2. 3. above and try again but for a full test it would be way more convenient to have a build from HTCondor to use since we need to deploy both in the container we use for TW (what Wa did) and in the scheduler hosts where we currently get condor via `yum`.
In the schedulers we have a bunch of classAd read/write (hopefully transparent) and a couple more exotic use case with JEL's and `htcondor.lock()`. I am just a tiny bit worried by the latter since I do not find it in the [documentation](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html) even if it is working in HTC 23. BTW I just discovered that
```
/usr/lib64/python3.6/site-packages/htcondor/_deprecation.py:41: FutureWarning: lock() is deprecated since v8.9.8 and will be removed in a future release.
```
To see that warning one needs to call it in an interactive shell. It is not in our logs.

Working w/o locking condor log files is a different story though. And it may simply mean that eventually we really need to do the work outlined in #6270

## Comment (Todd-L-Miller, 2024-03-12T17:11:42Z)

> I hope that we will not have to worry about things like python 3.8 vs. 
> python 3.9, atm we use python3.8 in TW , python 3.6 in schedulers, same 
> HTC major version (10) and everything is OK.

 	The htcondor and classad packages are (and must be) built for 
specific Python minor versions, but have the same compatibility guarantees 
as HTCondor proper.  At some point, hopefully in the near future, we'll
start building the htcondor2 and classad2 packages in the 
minor-version-independent way that they support.

> 3. `SecMan` and `authenticated subprocess`
>
> but I am optimistic that all of this code can be simply removed and we 
> should make calls to condor bindings directly in TW code w/o going 
> through a (authenticated) subprocess.

 	That would be good news for me, and I think simplify and speed up 
your code, so this sounds like a good idea to me. :)

> Yet I am puzzled that `SecMan` is listed in latest bindings 
> as the only cure in case a daemon restarts and `all future commands 
> will fail with strange connection errors.`

 	I'll have to do some digging to determine if this is a general 
Python bindings problem, a v1-specific problem, or just a design decision 
on our part, because it's clearly a situation our daemons can deal with.

> Maybe we simply need to be sure that all collector and schedd objects 
> which we create are in the temporary scope of some object and do not try 
> to persist in memory for days ?

 	That seems like a reasonable approach, but I think the C++ 
library's session cache isn't tied to the lifetime of any particular 
daemon object.  That doesn't necessarily mean the Python bindings have to 
expose that fact, but I have some investigating to do.

> Bottom line: we can surely profit anyhow from aligning current code to 
> current bindings and clean up GSI legacy stuff. Then chances are that 
> htcondor2 and classad2 work smoothly.

 	That would be awesome.

> In the end we do not to do anything more then what is the examples in 
> the documentation ! The only non trivial thing is that the schedd we 
> submit to runs on a different VM. But I presume that that is part of 
> standard tests for the bindings.

 	Our test suite is not that sophisticated, sadly. :(

> Wa did not get to test `classAd2` here, but the use we make of it should 
> be very basic.

 	Good news.  I have a fair amount of confidence in `classad2`, but 
we also deliberately removed a few things from the API there.

> I am not sure about next step(s) though. We can remove 1. 2. 3. above 
> and try again but for a full test it would be way more convenient to 
> have a build from HTCondor to use since we need to deploy both in the 
> container we use for TW (what Wa did) and in the scheduler hosts where 
> we currently get condor via `yum`.

 	I believe the RPMs for 23.x in our repositories have (some version 
of) the `classad2` and `htcondor2` modules in them already; I recommended 
building them from source so that you could test any updates I made as a 
result of your testing more easily.

 	I appreciate your willingness to update your code and help us test 
ours!

> In the schedulers we have a bunch of classAd read/write (hopefully 
> transparent) and a couple more exotic use case with JEL's

 	I believe the JobEventLog class is already 100% supported in the 
htcondor2 module.

>  and `htcondor.lock()`.
>
> I am just a tiny bit worried by the latter since I do not find it in the 
> documentation even if it is working in HTC 23.

 	`htcondor.lock()` doesn't appear in the 10.0 documentation, 
either, that I can tell.

> To see that warning one needs to call it in an interactive shell. It is 
> not in our logs.

 	To my -- limited -- understanding, this was a design decision by 
the Python people.  See

https://docs.python.org/3/library/warnings.html#default-warning-filter

; you can turn on deprecation warnings explicitly.

> Working w/o locking condor log files is a different story though.
>
> And it may simply mean that eventually we really need to do the work 
> outlined in #6270

 	That looks like a much cleaner solution.

- ToddM

## Comment (belforte, 2024-05-30T21:39:04Z)

Hi @Todd-L-Miller 
I wanted to reassure you that this is not forgotten, but we had to give priority to Alma9 transition and @novicecpp (aka Wa) is busy with a new CI/CD setup for CRAB, so in spite of some progress in modernizing our usage of python bindings I can't test with `htcondor2` yet. I need his magic build/

BTW I tried to use htcondor2 in HTC 23, but it fails to be imported due to lack of classad2
Here's in a schedd whith htcondor 23.0
```
belforte@crab-sched-903/~> condor_version
$CondorVersion: 23.0.4 2024-02-08 BuildID: 712251 PackageID: 23.0.4-1 $
$CondorPlatform: x86_64_AlmaLinux9 $
belforte@crab-sched-903/~> python3
Python 3.9.18 (main, Jan 24 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> htcondor.version()
'$CondorVersion: 23.7.2 2024-05-16 BuildID: UW_Python_Wheel_Build $'
>>> import htcondor2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2/__init__.py", line 30, in <module>
    from ._common_imports import classad
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2/_common_imports.py", line 7, in <module>
    import classad2 as classad
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/classad2/__init__.py", line 26, in <module>
    from .classad2_impl import _version as version
ModuleNotFoundError: No module named 'classad2.classad2_impl'
>>> 
```
same error from `import classad2` (of course). While `import classad` works finely (of course).

Could this be a shortcoming of our installation ?
In that case it is out of our turf and we need to ask Marco Mascheroni and his team to follow up.

In the submission machine we simply `pip install htcondor 23` 
```
root@crab-dev-tw01:/data/srv/TaskManager# pip install htcondor
Requirement already satisfied: htcondor in /usr/local/lib/python3.8/site-packages (23.7.2)
```
and have same problem with `classad2`

## Comment (Todd-L-Miller, 2024-05-30T22:43:48Z)

> Could this be a shortcoming of our installation ?

 	The Python wheels don't have htcondor2 or classad2 yet; you should 
only be getting those from the .rpm / .deb / .tar.gz installation(s).  It 
looks like  (based on the .local in the path) that maybe both of your 
tests were against a verion of the bindings installed from a wheel?

 	(I'm curious about the contents of

/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/classad2
and
/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2

in this test -- IIRC, htcondor2 tries to load classad2 before it tries to 
load its own extension module, so it's possible that both of them are 
missing the .so's, as expected).

-- ToddM

## Comment (belforte, 2024-05-31T00:01:48Z)

indeed, here's the container where we pip-installed condor
```
root@crab-dev-tw01:/data/srv/TaskManager# ls /usr/local/lib/python3.8/site-packages/htcondor/
__init__.py  _deprecation.py  _lock.py	_wrap.py     dags     htcondor.so
__pycache__  _job_status.py   _utils	compat_enum  htchirp  personal.py
root@crab-dev-tw01:/data/srv/TaskManager# 
```

But in the scheduler host we install from rpm (via puppet) from htcondor-stable-23.0
```
[root@crab-sched-903 ~]# yum list|grep condor
condor.x86_64                                                                            23.0.4-1.el9                                   @htcondor-stable-23.0    
condor-stash-plugin.x86_64                                                               6.12.1-1                                       @htcondor-stable-23.0    
python3-condor.x86_64                                                                    23.0.4-1.el9                                   @htcondor-stable-23.0    
globus-gram-job-manager-condor.noarch                                                    3.0-10.el9                                     epel                     
[root@crab-sched-903 ~]# 
```
in this case I have these binaries
```
[root@crab-sched-903 ~]# ls /usr/lib64/python3.9/site-packages/htcondor*/*.so
/usr/lib64/python3.9/site-packages/htcondor/htcondor.cpython-39-x86_64-linux-gnu.so
[root@crab-sched-903 ~]# ls /usr/lib64/python3.9/site-packages/classad*/*.so
/usr/lib64/python3.9/site-packages/classad/classad.cpython-39-x86_64-linux-gnu.so
[root@crab-sched-903 ~]# 
```

thanks for having pointed out that somehow I have managed to get  `$HOME/.local/lib/python3.9/site-packages/htcondor2` which I am not sure how it got there !
In my .local  I also have `classad2` and `classad3`. All of them w/o `.so` files.
Anyhow, my .local confusion aside  (it is a sort of scratch area/playground at the end of the day)
I am puzzled that we do not have the binaries in the rpm install.

Maybe as simple as install the rpm for the HTC 23 feature branch (23.7 e.g.) non the stable 23.0 ?

## Comment (belforte, 2024-05-31T09:18:25Z)

I switched the scheduler host to 23.7.2 and now import of htcondor2 and classad2 work !

The submitter process runs in a debian-based docker container where we currently pip-install.
I will try to use apt-get instead

## Comment (belforte, 2024-05-31T20:22:20Z)

HI @Todd-L-Miller 
I played a bit with HTC installs, and things are difficult to do cleanly since we want to test htcondor2 in our container based on python3.8.. longish story short, do you think it is OK if I simply grab
```
/usr/lib/python3/dist-packages/htcondor2/htcondor2_impl.cpython-39-x86_64-linux-gnu.so
/usr/lib/python3/dist-packages/classad2/classad2_impl.cpython-39-x86_64-linux-gnu.so
``
from a debian install and put them in our `/usr/local/lib/python3.8/....` where we pip-installed the bindings w/o the wheels ?
Yeah.. also  change `cpython-39` to `cpython-3.8` in the name.

I tried and at least `import htcondor2` works. But maybe once called they will look for other packages and this is never going to work, at least not well enough that it there's a problem we can't tell if it is on your or our side w/o spending too much time.

## Comment (belforte, 2024-05-31T20:26:41Z)

for me and @novicecpp : the changes I did to get a TW container with HTC 23.7 and htcondor2 binaries are in https://github.com/belforte/CRABServer/tree/htc23.x and the container image is `registry.cern.ch/cmscrab/crabtaskworker:belforte-HTC23x `

## Comment (Todd-L-Miller, 2024-06-03T15:56:11Z)

Good news: as of last Friday, the version 2 bindings are 
included (in a minor-version independent way) in the version 1 wheels. 
For our own internal purposes, those wheels are available as version 
'23.9.0a2', which you should hopefully just be able to pip-install:

https://pypi.org/project/htcondor/23.9.0a2/

This particular release is of course unsupported, but it was made so that 
we could release version 2's documentation, which you can preview at:

https://htcondor.readthedocs.io/en/main/apis/python-bindings/api/version2/index.html

-- ToddM

## Comment (belforte, 2024-06-03T16:04:54Z)

I can pip-install and import. WIll build a new container so we can run our code with this.

## Comment (Todd-L-Miller, 2024-06-03T16:09:03Z)

> I can pip-install and import. WIll build a new container so we can run 
> our code with this.

 	Good.  Thanks again for working with all this before its official 
release.

-- ToddM

## Comment (belforte, 2024-06-03T22:02:39Z)

docker image `registry.cern.ch/cmscrab/crabtaskworker:belforte-HTC23_0603` has now `HTC 23.9.0a2`
<strike>
and crab TW from master

now running in `crab-dev-tw01`
first validation:
 - [ ] https://github.com/dmwm/CRABServer/issues/8468
</strike>

oops, latest fixes in master were left out. Try again. Anyhow "it runs"

## Comment (belforte, 2024-06-03T22:51:57Z)

try again with `belforte-HTC23_0604`
 - [x] https://github.com/dmwm/CRABServer/issues/8470

## Comment (belforte, 2024-06-12T13:27:46Z)

Hi @Todd-L-Miller 
 Now that I have a code version which does not use deprecated methods, I can try v2 bindings.
First discovery is that v1 works even w/o a config file, simply prints a warning as it reverts to
` using a null condor_config`
v2 instead fails with the rather obscure
`ERROR "Unwilling or unable to try IPv4 or IPv6.  Check the settings ENABLE_IPV4, ENABLE_IPV6, and NETWORK_INTERFACE." at line 1202 in file /var/lib/condor/execute/slot1/dir_2361636/htcondor_source/src/condor_io/sock.cpp`
So the condor_config file is mandatory, even if pointing $CONDOR_CONFIG to an empty file seems to work.

Is this a feature ? or an oversight ?

## Comment (belforte, 2024-06-12T14:14:47Z)

first real problem.
How do I put an integer as value in the Submit object ?
This works in v1
```
bash-5.1$ python3
Python 3.9.18 (main, Jan 24 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> jdl=htcondor.Submit()
>>> jdl['somead']=1
>>> print(jdl)
somead = 1
```
but 
```
bash-5.1$ python3
Python 3.9.18 (main, Jan 24 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor2 as htcondor
>>> jdl=htcondor.Submit()
>>> jdl['somead']=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_submit.py", line 123, in __setitem__
    raise TypeError("value must be a string")
TypeError: value must be a string
>>> 
```
of course something like `jdl['priority'] = "10"` is accepted. Will it work ? With v1 too ? I had to change from a string to an int that one the other day since submission was complaining.

## Comment (belforte, 2024-06-12T14:50:18Z)

also `htcondor.HTCondorException` is gone. What should I use instead to notice that a call failed ?
e.g. our favorite "submission failed becaue scheduler is busy, unreacheable, unhappy, overloaded..." ?
fall back to
```
try:
 result=schedd.Submit(jdl, 1, True)
except Exception:
  log("something went wrong")
```
?

## Comment (belforte, 2024-06-12T15:50:39Z)

and finally scheduler.spool() method is changed, for the good of course, and it takes as argument a submitterResult object, does not need the workaround in https://lists.cs.wisc.edu/archive/htcondor-users/2024-May/msg00047.shtml

So I doubt we can have a single code version which works with both bindings.
Will need some kind of switch flag.

I still have to "test everything" and already see that something has changed in JEL area.
But I managed to to the remote submission of a CRAB DAG and it got executed.
:tada:

## Comment (belforte, 2024-06-12T16:04:54Z)

@Todd-L-Miller 
is this  bug on your side, by any chance ? or the way to use JEL's is quite different. I haven't looked up new documentation yet.

```
 File "/data/srv/glidecondor/condor_local/spool/9550/0/cluster9550.proc0.subproc0/task_process/cache_status.py", line 348, in storeNodesInfoInFile
    pickle.dump(jel, f)
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_job_event_log.py", line 101, in __getstate__
    offset = _job_event_log_get_offset(self, self._handle)
NameError: name '_job_event_log_get_offset' is not defined
```

## Comment (Todd-L-Miller, 2024-06-12T16:08:33Z)

> v2 instead fails with the rather obscure
>
> `ERROR "Unwilling or unable to try IPv4 or IPv6.  Check the settings 
> ENABLE_IPV4, ENABLE_IPV6, and NETWORK_INTERFACE." at line 1202 in file 
> /var/lib/condor/execute/slot1/dir_2361636/htcondor_source/src/condor_io/sock.cpp`
>
> So the condor_config file is mandatory, even if pointing $CONDOR_CONFIG 
> to an empty file seems to work.
>
> Is this a feature ? or an oversight ?

 	Oversight.  I'll try to figure out what changed from v1.  Thanks 
for the heads-up; the environment I test in of course, always has a valid 
CONDOR_CONFIG.

- ToddM

## Comment (Todd-L-Miller, 2024-06-12T16:15:45Z)

> How do I put an integer as value in the Submit object ?

 	The semantics of the Python interface have changed to reflect the 
underlying reality: the HTCondor submit language only understands strings. 
Those strings sometimes/frequently convert into ClassAd values, but

> of course something like `jdl['priority'] = "10"` is accepted. Will it work ?

 	Yes, in exactly the same way it work if you wrote

priority = 10

in the submit file.  That's kind of the point of this change, that the 
previous interface let people believe they were passing through integers 
-- or worse, more complicated data structures -- through, when in fact we 
were mostly just str()ingify them and hoping.

 	I've made a note of this for the migration guide, and if enough 
people complain strongly enough, we might back off some of the changes. 
(For instance, the semantics and syntax of converting ints to string and 
back are known to work exactly as you might expect, so handling them 
explicitly is probably OK, if people decide a little bit of confusion is 
worth the convenience.)

-- ToddM

## Comment (Todd-L-Miller, 2024-06-12T16:18:13Z)

> also `htcondor.HTCondorException` is gone. What should I use instead to 
> notice that a call failed ?

 	At the moment, htcondor2 is just using the generic exceptions 
corresponding to the custom ones from v1.  (htcondor.HTCondorException 
should never be being raised -- it's supposed to just be a parent class.)

 	This should probably be changed before release, but I haven't had 
a chance to make it happen yet.

-- ToddM

## Comment (Todd-L-Miller, 2024-06-12T16:23:12Z)

> and finally scheduler.spool() method is changed, for the good of course, 
> and it takes as argument a submitterResult object, does not need the 
> workaround in 
> https://lists.cs.wisc.edu/archive/htcondor-users/2024-May/msg00047.shtml

 	Super-convenient, right? :)

> So I doubt we can have a single code version which works with both bindings.
> Will need some kind of switch flag.

 	The following glorious hack may be of interest:

schedd = htcondor.Schedd()
if 'classad2' in str(type(schedd)):
 	schedd.spool(submit)
else:
 	# previous hackery

> I still have to "test everything" and already see that something has 
> changed in JEL area.

 	I'm 99% sure I copied the JEL code over unmodified, so that's a 
little worrying.

> But I managed to to the remote submission of a CRAB DAG and it got 
> executed. :tada:

 	Awesome!  Could you guess at how long it took from when the code 
had been modernized to when you got it working with version 2?

- ToddM

## Comment (Todd-L-Miller, 2024-06-12T16:27:39Z)

> is this bug on your side, by any chance ? or the way to use JEL's is 
> quite different. I haven't looked up new documentation yet.

 	The way to use JELs _should_ be identical.  The function
_job_event_log_get_offset() is in the native library (htcondor2_impl.so),

...

OK, I could have sworn I tested this.  If you open htcondor2/_job_event_log.py,
you should see the following:

from .htcondor2_impl import (
     _job_event_log_init,
     _job_event_log_next,
     _job_event_log_close,
)

If you change that list to

from .htcondor2_impl import (
     _job_event_log_init,
     _job_event_log_next,
     _job_event_log_close,
     _job_event_log_get_offset,
     _job_event_log_set_offset,
)

does it start working?  Sorry for the trouble.

 	And thanks.  This has been really helpful and will benefit a lot 
of other people.

-- ToddM

## Comment (belforte, 2024-06-12T17:11:46Z)

Super helpful Todd. Thanks. I'll give more details after dinner, or after sleep 😁

## Comment (Todd-L-Miller, 2024-06-12T17:24:27Z)

> Super helpful Todd. Thanks. I'll give more details after dinner, or 
> after sleep 😁

 	Thanks again; looking forward to it.

-- ToddM
--1770009992-571966204-1718213023=:12350--

## Comment (belforte, 2024-06-12T19:38:36Z)

* JEL: I tried to add the imports but
```
  File "/home/grid/crabtw/.local/lib/python3.9/site-packages/htcondor2/_job_event_log.py", line 104, in __getstate__
    return (self.__dict__, self._deadline, offset_)
NameError: name 'offset_' is not defined
```
  maybe I did something wrong, will check again tomorrow
  
* CONDOR_CONFIG: I see no problem in making it required, but then better to exit immediately and provide an example of a simple config in the documentation. That an empty files does it, is a bit odd. And I am sure there are other use cases beside mine where one wants to use the binding on a machine where I can't copy from /etc/condor_config or similar places as the documentation suggests. I am not even sure that copying the config from e.g. a scheduler (sorry AP), would be good. Indeed we had a dummy one originally, at some point I was disgusted by an empty file and decided to clean up. As usual, nobody does as much harm as those who aim to do good !

* I am fine with exceptions the way they are (and thanks for pointing out my mistake in trying to catch something which is never raised)

* I am happy with `jdl['priority']=str(10)`, and agree that "everything is a string" is easier.

* hard to say "how long it took", I did all of this in one afternoon, but I had already mastered the pip install and got a lot of benefit from the work on changing the submission semantyc (thanks again for that).  It took some perserverance and imagination, but the only tough one was `Unwilling or unable to try IPv4 or IPv6.`. I only found a solution because I knew there must have been one since @novicecpp made it further down already ! 

* odds and ends: I discovered that while not documented, if I put `+RequestedCores=N` in the JDL, I end up with `RequestCores=N ` in the requirements. Drove me crazy for a bit, then I decided to stop messing around and prefixed `+CRAB_` on all  custom ads which solves all problems.

## Comment (belforte, 2024-06-12T19:39:00Z)

and **tanks for glorious hack** I will put it in

## Comment (Todd-L-Miller, 2024-06-12T20:01:43Z)

> * JEL: I tried to add the imports but

 	This is on my plate to look at now -- I was just hoping there was 
a simple fix / oversight, but it looks like it's going to be complicated.
My apologies -- we obviously don't have a test for this and need one.

> CONDOR_CONFIG: I see no problem in making it required

 	I also made changing this a ticket.  Whatever we're doing in 
version 1 to avoid this problem we can almost certainly do in version 2,
and I don't think requiring one benefits anybody.

> * I am fine with exceptions the way they are (and thanks for pointing 
> out my mistake in trying to catch something which is never raised)

 	It might actually work to catch any exception deliberately raised 
by the bindings -- as opposed to an exception that the bindings are just 
passing up from elsewhere -- so it's still useful, I just wanted to make 
sure that you were doing that on purpose. :)

> * I am happy with `jdl['priority']=str(10)`, and agree that "everything 
> is a string" is easier.

 	Thanks.

> * hard to say "how long it took", I did all of this in one afternoon, 
> but I had already mastered the pip install and got a lot of benefit from 
> the work on changing the submission semantyc (thanks again for that). 
> It took some perserverance and imagination, but the only tough one was 
> `Unwilling or unable to try IPv4 or IPv6.`. I only found a solution 
> because I knew there must have been one since @novicecpp made it further 
> down already !

 	"One afternoon" is a wonderfully consise and sufficiently precise 
measurement. :)

> * odds and ends: I discovered that while not documented, if I put 
> `+RequestedCores=N` in the JDL, I end up with `RequestCores=N ` in the 
> requirements. Drove me crazy for a bit, then I decided to stop messing 
> around and prefixed `+CRAB_` on all custom ads which solves all 
> problems.

 	I don't _think_ that's specific to the version 2 bindings, but I 
guess let me know if it is, and I'll try to figure out what's going on. 
(You may need to specify "MY.RequestedCores" instead, but I think you're 
tripping on magic code to allow "request_<resource> = 7" to work for any 
custom resource (named <resource>).)

-- ToddM

## Comment (belforte, 2024-06-13T15:00:10Z)

> you're tripping on magic code to allow "request_<resource> = 7" to work for any
custom resource (named <resource>).)

Exactlty ! In similar case (`cpus`instead of `cores`) changing `+` to `MY.` had no effect, which is correct IMHO.
I do not think it is v2 either, simply the change from submit(ads) to submit(submit). At some point the trick you gave to put requirements="TARGET.cpus=1" was not working anymore, I tried a few things. Eventually "always use +CRAB for custom things" did it.

## Comment (Todd-L-Miller, 2024-06-17T20:42:54Z)

> v2 instead fails with the rather obscure
> `ERROR "Unwilling or unable to try IPv4 or IPv6.  Check the settings ENABLE_IPV4, ENABLE_IPV6, and NETWORK_INTERFACE." at line 1202 in file /var/lib/condor/execute/slot1/dir_2361636/htcondor_source/src/condor_io/sock.cpp`
> So the condor_config file is mandatory, even if pointing $CONDOR_CONFIG to an empty file seems to work.

 	I haven't been able to duplicate this particular problem, although 
the fix I'm looking at may well avoid it.  In the same environment, 
and where /etc/condor/condor_config doesn't exist and CONDOR_CONFIG is 
unset, what do the following two config queries return?

CONDOR_CONFIG=/dev/null condor_config_val -v IPV4_ADDRESS
CONDOR_CONFIG=/dev/null condor_config_val -v IPV6_ADDRESS

Thanks.

-- ToddM

## Comment (belforte, 2024-06-18T08:51:59Z)

well, I need a full condor install to get condor_config_val command.
In my case I simply pip-install the bindings in a Debian container.

The error happens when I try to talk to the remove collector, which the
first action in order get a proper Scheduler object.
In the meanwhile I am adding an empty /etc/condor/condor_config file
to may container.

FWIW here's a reproducer on my laptop (Ubuntu 22.04)
```text
LapSB:~$ python3
Python 3.8.19 (default, May 24 2024, 17:43:40) 
[GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor2

Neither the environment variable CONDOR_CONFIG,
/etc/condor/, /usr/local/etc/, nor ~condor/ contain a condor_config source.
Either set CONDOR_CONFIG to point to a valid config source,
or put a "condor_config" file in /etc/condor/ /usr/local/etc/ or ~condor/
>>> htcondor2.version()
'$CondorVersion: 23.9.0 2024-05-31 BuildID: UW_Python_Wheel_Build PRE-RELEASE-UWCS $'
>>> coll=htcondor2.Collector('cmsgwms-collector-global.cern.ch')
>>> coll.query(htcondor2.AdTypes.Schedd)
06/18/24 10:40:25 ERROR "Unwilling or unable to try IPv4 or IPv6.  Check the settings ENABLE_IPV4, ENABLE_IPV6, and NETWORK_INTERFACE." at line 1202 in file /var/lib/condor/execute/slot1/dir_36618/htcondor_source/src/condor_io/sock.cpp
LapSB:~$ 
```

Same happens on an Alma9 VM.
Using `import htcondor` I get the list of schedulers in that pool instead.

## Comment (Todd-L-Miller, 2024-06-21T15:39:26Z)

>> * JEL: I tried to add the imports but
>
> 	This is on my plate to look at now -- I was just hoping there was a 
> simple fix / oversight, but it looks like it's going to be complicated.
> My apologies -- we obviously don't have a test for this and need one.

 	Fix merged (and test added) this morning, so it will go out with 
the next release.

-- ToddM

## Comment (Todd-L-Miller, 2024-06-21T15:50:12Z)

> Using `import htcondor` I get the list of schedulers in that pool instead.

 	Thanks for the reproducer.  I confirm that it causes the problem 
for me, and that the patch that was merged yesterday fixes (or, rather, 
avoids) the problem.

-- ToddM

## Comment (belforte, 2024-06-21T15:50:38Z)

thanks Todd

## Comment (belforte, 2024-07-05T15:33:41Z)

new binding is out [23.9.0a3](https://pypi.org/project/htcondor/23.9.0a3/)

 - [x] update pypi TW containers to use it
    * https://github.com/dmwm/CRABServer/pull/8547
    * building  `pypi-test2-050724` with it in this [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7704336) 
 - [x] deploy on vocms059 and crab-preprod-scd03
     * pip-installed on `crabtw` user local

## Comment (belforte, 2024-07-29T16:38:31Z)

to make more tests and progress I need a simple way to switch from v1 to v2 bindings when running to use for the next months, can't stick to the old release where I based my tests on. Our pypi TW image already has htcondor 23.9.a3, but we need to make that available on schedulers as well.
 - [x] #8571 
 - [ ] #8572

## Comment (belforte, 2024-07-31T08:06:15Z)

as a first step I have aligned the v2 version with current master in https://github.com/belforte/CRABServer/tree/allow-v2-bindings-8571 and tested with Jenkins standard test.

## Comment (belforte, 2024-07-31T15:54:04Z)

Besides TaskWorker submitting/running/killing tasks, there are other places where HTC bindings are used:
* GenerateMONIT  
* recurring action: GetAcceleratorSite
* recurring action: RenewRemoteProxies

RenewRemoteProxies neess to stay with V1 until `schedd.refreshGSIProxy` is made available in v2
For the other two, we can simply switch once the more challenging Task-Handling flow is declared OK.

## Comment (belforte, 2024-08-02T17:48:36Z)

hi @Todd-L-Miller 
I discovered that when creating a JDL file from an htcondor.Submit object (e.g. via `print()`)
the v2 bindings automatically add a `queue` line at the bottom which was not there with v1.

I presume that there are good reasons for the change, so will not question it, but this breaks our code now (I end up with a dagman submission file with two `queue` statements in it ). I guess that I will find a fix, but I suggest that you point out this change in the documentation.

Thanks

## Comment (belforte, 2024-08-02T18:00:35Z)

there is a also an error when looking at an empty Submit object. Nothing fatal of course, but a bit annoying
```text
>>> import htcondor
>>> import htcondor2
>>> s=htcondor.Submit()
>>> s
''
>>> s=htcondor2.Submit()
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2/_submit.py", line 179, in __repr__
    return f'Submit({self})'
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2/_submit.py", line 167, in __str__
    for key, value in self.items():
  File "/usr/lib64/python3.9/_collections_abc.py", line 850, in __iter__
    for key in self._mapping:
  File "/afs/cern.ch/user/b/belforte/.local/lib/python3.9/site-packages/htcondor2/_submit.py", line 156, in __iter__
    keys = _submit_keys(self, self._handle)
SystemError: Negative size passed to PyUnicode_FromStringAndSize
>>> 
```

## Comment (belforte, 2024-08-02T18:03:38Z)

and this is a trivial reproducer for the "extra queue"
```text
>>> s1=htcondor.Submit()
>>> s2=htcondor2.Submit()
>>> s1['MY.var'] = "hey"
>>> s2['MY.var'] = "hey"
>>> print(s1)
MY.var = hey

>>> print(s2)
MY.var = hey
queue

>>> 
```

## Comment (belforte, 2024-08-08T21:42:58Z)

I found that PostJob.py script is using the deprecated `schedd.transaction` : https://github.com/dmwm/CRABServer/issues/8597

there is also a problem with running PosJobs, they run too slowly, or some got stuck, or something else https://github.com/dmwm/CRABServer/issues/8598

## Comment (Todd-L-Miller, 2024-08-09T20:06:11Z)

> RenewRemoteProxies needs to stay with V1 until `schedd.refreshGSIProxy` is made available in v2 

Now https://opensciencegrid.atlassian.net/browse/HTCONDOR-2577.

## Comment (Todd-L-Miller, 2024-08-09T20:12:51Z)

> I presume that there are good reasons for the change,

The v2 Submit object now handles complete submit files correctly, so its string converter now generates complete submit files.  If removing the queue statement proves troublesome, let me know and we can think about additional APIs or about API tweaks.

> so will not question it, but this breaks our code now (I end up with a dagman submission file with two `queue` statements in it ). I guess that I will find a fix, but I suggest that you point out this change in the documentation.

I'll hold off on updating the documentation until you let me know how painful the change/fix you had to make was.

## Comment (Todd-L-Miller, 2024-08-09T20:23:18Z)

> there is a also an error when looking at an empty Submit object. Nothing fatal of course, but a bit annoying

Nonetheless, it's not OK; thanks for the heads up.  Fixed, but it make take a bit for that fix to be released.

## Comment (belforte, 2024-08-09T20:39:45Z)

about the addition of the `Queue` statement in the streaming to string of the Submit object, it was easy to fix
```python
subdag = str(subdagJDL)  # print subdagJDL into a string
subdag = subdag.rstrip('queue\n')  # strip "queue" from last line
```
but in a way that's a bit fragile as it relies on that being the last line. I guess I can be more general there, though.

Another option is that [condor_dagman_submit](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit_dag.html) gets smarter and when passed the `-insert_sub_file` option "properly handles a proper Submit file which may include a queue statement"

That would elegantly move the ball out of mine and your field !

## Comment (belforte, 2024-08-09T20:40:02Z)

thanks @Todd-L-Miller

## Comment (Todd-L-Miller, 2024-08-09T20:48:54Z)

> Another option is that [condor_dagman_submit](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit_dag.html) gets smarter and when passed the -insert_sub_file option "properly handles a proper Submit file which may include a queue statement"

That certainly _sounds_ like a bug; I'll ask the DAGMan guy about it.  Are you actually shelling out `condor_dagman_submit`?  If so, that may imply something missing in the Python API, too..

## Comment (belforte, 2024-08-09T20:57:15Z)

yes I "shell" it
https://github.com/dmwm/CRABServer/blob/3616cf5e4ac018be9445d77a1dca28e190edfa0c/src/python/TaskWorker/Actions/PreDAG.py#L335-L339

## Comment (belforte, 2024-08-09T21:03:02Z)

if there's now a python API I can certainly look into switching

## Comment (Todd-L-Miller, 2024-08-09T21:03:07Z)

I talked to the DAG guy.  Two main points: first, every condor_submit_dag command-line flag has, in version 2, a corresponding API bit.  Second, if you call `Submit.from_dag()`, you get a `Submit` object back... which you could then manipulate in exactly the same way you manipulate `subdagJDL` before you turn around and submit it, which would avoid this problem (and a `fork()`) entirely.

## Comment (Todd-L-Miller, 2024-08-09T21:05:13Z)

The docstring for `Submit.from_dag()` in v2 is wrong; the `Submit` object is generated _from_ the DAG description on disk.

## Comment (belforte, 2024-08-09T21:14:35Z)

i hesitate to go that way w/o an example. [v1 doc](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#htcondor.Submit.from_dag) is not fully clear to me, and it does not mention `insert_sub_file`. I guess it can be replaces by joining two Submit objects. Yeah.. time to outgrow what Brian wrote 7 years ago, I know. But... CLI should also work, right ? Those fork are executed at << 1/hour rate. I do not care for performance here.

## Comment (Todd-L-Miller, 2024-08-09T21:14:51Z)

So something like
```
s = Submit.from_dag( "subdag", {
    "DoRecov": true,
    "AutoRescue": 0,
    "MaxIdle": maxidle,
   # etc
}
s["subdag_jdl_property_one"] = str(value_one)
```

## Comment (Todd-L-Miller, 2024-08-09T21:16:17Z)

>  But... CLI should also work, right ? Those fork are executed at << 1/hour rate. I do not care for performance here.

If it's not easier for you, don't worry about switching.  You've got a solid work-around already.

## Comment (belforte, 2024-08-09T21:17:26Z)

> So something like

And then `result=schedd.submit(s)` ?

## Comment (Todd-L-Miller, 2024-08-09T21:18:07Z)

> > So something like
> 
> And then `result=schedd.submit(s)` ?

Yeah, exactly.

## Comment (belforte, 2024-08-09T21:19:06Z)

in the long term using python API will make this easier to understand for those who come after me. But I need to pick my battles. Thanks

## Comment (Todd-L-Miller, 2024-08-09T21:31:49Z)

No problem.  And thank you for finding these problems.

## Comment (belforte, 2024-08-09T21:35:07Z)

well.. IMHO the `condor_submit_dag` CLI could stll benefit from a fix here. Even if I am protected now.

## Comment (Todd-L-Miller, 2024-08-09T21:42:36Z)

Oh, agreed, and that ball has successfully been moved into another field.

## Comment (belforte, 2024-08-12T13:59:58Z)

Hi @Todd-L-Miller 
I have a problem with `schedd.edit` in V2 when trying to set a classAd to a list of values.
Looks like something at your end #8604 

Maybe you can also reproduce it locally by using a different clusterId :-)

## Comment (belforte, 2024-08-28T21:18:35Z)

on HOLD waiting for #8572 which is waiting on #8660

## Comment (belforte, 2024-09-01T17:13:23Z)

#8660 solved, waiting for [deployment of HTC 23.9](https://github.com/dmwm/CRABServer/issues/8572)

## Comment (belforte, 2024-10-01T16:33:37Z)

all schedulers have HTC 23.9 I will enable crab-preprod-tw01 to use v2 bindings, so that all our validation jobs will use it.

## Comment (belforte, 2024-12-18T17:05:15Z)

currently 50% of all user tasks run with HTC v2 API
https://cms-talk.web.cern.ch/t/start-testing-htcv2-api-in-production/76456/3

no reported issue
Will leave like that  and go to 100% in January

## Comment (belforte, 2024-12-18T17:06:18Z)

Testing phase is over !

## Comment (Todd-L-Miller, 2024-12-18T18:51:18Z)

> Testing phase is over !

w00t!
