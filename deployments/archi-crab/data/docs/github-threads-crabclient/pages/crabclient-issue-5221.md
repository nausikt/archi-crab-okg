# dmwm/CRABClient issue #5221: define and implement inferface of CRABClient and Rucio python client. 

State: closed
Opened: 2023-10-12T08:52:08Z
Closed: 2023-10-23T08:38:55Z
Labels: question, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5221

## Opening post (belforte, 2023-10-12T08:52:08Z)

Scope creep from “run jobs on the grid” to “and also manage my data”, which points to incorporating Rucio python client into CRAB Client ,
After discussion with Eric and Shahzad in [cmsdist](https://github.com/cms-sw/cmsdist/issues/8737)  and initial integration in [crab and crab.py](https://github.com/dmwm/CRABClient/issues/5213) The plan is 
 * do it for CMSSW_12_6 or later  integrating Rucio python client
 * later look into extending down to CMSSW_11 and hopefully CMSSW_10_6 (used for UL)
 * no support for earlier releases beside the current couple of cases where we fork a pyhon script (e.g. checkwrite)

## Comment (belforte, 2023-10-13T12:53:21Z)

about CMSSW versions:

* full compatibility with python3 starts with CMSSW_11 and Rucio python client can at least be intialized there. #5222 
* CMSSW_10_6 has python3 but we use [FWCore.PythonUtilities.LumiList](https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_1/FWCore/PythonUtilities/python/LumiList.py) which imports urllib2 which is not available in python3
* python2 client for Rucio exist, but not supported and quite old. I prefer to avoid it

Therefore we will use Rucio python client for CMSSW_11 and onward. We wiill keep dirty trick of forking a python script in a subshell for earlier releases where absolutely needed (I.e. code which is there already) and new functionalities will be there for CMSSW_11 and later.
Rucio calls can we done line this:
```python
if self.rucio:
    myself = self.rucio.whoami()
```

@mapellidario @novicecpp  feel free to comment and advice.
In theory we can pick `FWCore.PythonUtilities.LumiList.py` from e.g. CMSSW_11 and freeze it in our repo and it is likely to work with CMSSW_10 as well, like we did with `WMCore config` but I do not like to detach from the main repo in this way. Maybe we could switch to the frozen one only for CMSSW_10... where everything is frozen anyhow.  Maybe as simple as
```python
try:
    import FWCore.PythonUtilities.LumiList
except ModuleNotFoundError:
    import CRABClient.LumiList
```
?

## Comment (belforte, 2023-10-16T09:21:40Z)

In a way, this is done. Am waiting to close it is used in a few commands so we are sure there's no change needed.

## Comment (belforte, 2023-10-19T13:33:37Z)

In CRAB meeting this morning we agreed to pursue "our own, python3 compatible, LumiList in our repo and fall back to is when import from FWCore fails, so extendo Rucio Python client integration to CMSSW_10

## Comment (belforte, 2023-10-19T21:37:43Z)

using python3 for CMSSW_10 brings also
```
ImportError: pycurl: libcurl link-time version (7.59.0) is older than compile-time version (7.61.1)
```
We need to complete removing all instances of pycurl and stick to plain curl. Half made work at the time :-(

## Comment (belforte, 2023-10-19T22:07:01Z)

I made switched  to python3 for CMSSW_10, fixed LumiList as indicated and removed at least pycurl checks in crab.py (will see later where exactly it is still used) in 6ddac07c16a5dd5011dc6b751ae1e2dae385258b

Now crab submit fails on an odd
```
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/Analysis.py", line 95, in run
    valid, msg = self.cmsswCfg.validateConfig()
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py", line 298, in validateConfig
    elif numPSetCores > 1:
TypeError: '>' not supported between instances of 'NoneType' and 'int'
ERROR 2023-10-19 21:49:57.262 UTC: 	 ERROR: TypeError: '>' not supported between instances of 'NoneType' and 'int'

```
which at first sight should ALWAYS be a problem !
will investigate

I also notice that here comment and code disagree !
https://github.com/dmwm/CRABClient/blob/2ceaca1351b0cc158efc6cb84ae26d174b465330/src/python/CRABClient/JobType/CMSSWConfig.py#L273-L275

Looks like the default changed in CMSSW from 10 to 11.
CMSSW_10
```
-> numPSetCores = getattr(getattr(self.fullConfig.process, 'options', object), 'numberOfThreads', None)
(Pdb) n
> /afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py(277)validateConfig()
-> if numPSetCores and not isinstance(numPSetCores, uint32):
(Pdb) numPSetCores
(Pdb) 
```
CMSSW_11
```
-> numPSetCores = getattr(getattr(self.fullConfig.process, 'options', object), 'numberOfThreads', None)
(Pdb) n
> /afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/CRABClient/JobType/CMSSWConfig.py(277)validateConfig()
-> if numPSetCores and not isinstance(numPSetCores, uint32):
(Pdb) numPSetCores
cms.untracked.uint32(1)
(Pdb) 

```

## Comment (belforte, 2023-10-19T22:31:44Z)

this test is also wrong
https://github.com/dmwm/CRABClient/blame/2ceaca1351b0cc158efc6cb84ae26d174b465330/src/python/CRABClient/JobType/CMSSWConfig.py#L280-L288
if one of the two vars is `None` the initial `if` is false and the check on "You did not specify" is useless....pff...

## Comment (belforte, 2023-10-19T22:33:30Z)

anyhow `crab submit` works after changing
https://github.com/dmwm/CRABClient/blob/2ceaca1351b0cc158efc6cb84ae26d174b465330/src/python/CRABClient/JobType/CMSSWConfig.py#L274-275
to
```python
cfgNumCores = getattr(self.config.JobType, 'numCores', 1)
numPSetCores = getattr(getattr(self.fullConfig.process, 'options', object), 'numberOfThreads', uint32(1))
```

## Comment (belforte, 2023-10-19T22:45:49Z)

calls to `pycurl` to be removed are in report.py and copycat.py. The latter can be ignored since Dario and Wa will replace it.
But now that crab submit and crab status work. Let's validate all other commands and Rucio part before fixing crab report.

## Comment (belforte, 2023-10-19T22:48:54Z)

Well.. the `pycurl` in report is actually old code not used anywhere and left around "in case one day we figure out what it was here and what it was used for". Time to cleanup !

## Comment (belforte, 2023-10-19T22:52:05Z)

Ready for full validation.
New  code is in a new branch in CRABClient repo: https://github.com/dmwm/CRABClient/tree/test-cmssw_10-with-py3

## Comment (belforte, 2023-10-20T08:34:25Z)

I ran Jenkins ClientValidation on that for
* CMSSW_13: https://github.com/dmwm/CRABServer/issues/7970
* CMSSW_11: https://github.com/dmwm/CRABServer/issues/7972
* CMSSW_10 : https://github.com/dmwm/CRABServer/issues/7971

The test on CMSSW_11 ran before jobs completed, but the result so far indicates that the client with python3 on CMSSW_10 works, which is the important point. Og course Jenkins test is not complete and I do not think it exercises LumiList, but  it looks like only ad hoc testing can validate those corners.

@mapellidario maybe we can merge this and than you can test your new code also on CMSSW_10, for sure you have lumi maniulation there. Even if of course it is very difficult to imagine that LumiList from CMSSW_11 is broken.

I am not sure what is next step on this,other than merging into master !

## Comment (belforte, 2023-10-20T08:38:55Z)

hmm... I only tested CMSSW_10_6_26 put am currently swithing to python3 for all CMSSW_10_X.
Better try some earlier versions as well !

## Comment (belforte, 2023-10-20T13:39:05Z)

running Jenkins ClientValidation on CMSSW_10_1_0 now
*   https://github.com/dmwm/CRABServer/issues/7975

## Comment (belforte, 2023-10-20T14:07:37Z)

Everything looks good. I could alos run crab remake and crab status for that task from my `belforte` account and do `crab checkwrite --lfn /store/user/rucio/belforte`

## Comment (belforte, 2023-10-20T14:09:04Z)

Last concern:

* since we force python3 instead of python2 for CMSSW_10 and 11, which we never did before. Do we risk having problems with less trivial CMSSW PSets than the ones used in our test ?

## Comment (belforte, 2023-10-20T14:29:10Z)

I have (privately) asked Shahzad/David/Matti

## Comment (mapellidario, 2023-10-20T17:08:21Z)

> @mapellidario maybe we can merge this and than you can test your new code also on CMSSW_10, for sure you have lumi maniulation there. Even if of course it is very difficult to imagine that LumiList from CMSSW_11 is broken.

Ooook I will :)

## Comment (belforte, 2023-10-20T19:36:34Z)

I think I see the light a the end of the tunnel.
From what David Lange replied to my mail, I understand that there is almost no chance that using python3 will break the little pieces of CMSSW that we use in [CMSSWConfig.py](https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/JobType/CMSSWConfig.py)

The only real danger in forcing python3 for releases (CMSSW_10 and 11) where we used python2 so far is that some user may have python2-only syntax in their PSet.py or crabConfiguration.py

But I have a plan ! I just sent it in mail to David/Matti/Shahzad and here's it is for you @mapellidario and @novicecpp , please find holes and/or fill gaps !!

**The plan**
oh well.. users should get rid of that py2-only syntax
In the end:
- if most users need py2, we will stick with py2 with CMSSW.. you tell me
  up to 11 ? 12 ? is there a watershed ? Whe does CMSSW switch to
  using py3 for its own things ?
- if it is a few, and they can change their code, so much the better
- if it is only a few cases where it is desperately needed, we can
  find a way to give them a choice (at worst a crab2 command)
All in all we are only talking about these 2 lines from [1] !
```bash
python_cmd="python"
[ $CMSSW_Major -ge 10 ] && python_cmd="python3"
```

Maybe there is a way to pass an argument to this and strip it
from what is passed to  crab.py in the last line ? Something like
 `crab py2 <usual stuff>`
for those condemned to live in the past ?

I am afraid I do not fully understand the last line in [1]
hmm.... https://stackoverflow.com/questions/31418236/what-does-1-mean-in-a-unix-shell-script ??

So maybe `crab py2 submit...` is not so hard, all in all !

[1]
https://github.com/dmwm/CRABClient/blob/33cc58d2b73a40fc97bde58271ac8163663f7f3c/bin/crab

## Comment (belforte, 2023-10-20T20:13:55Z)

maybe we move that to different issue, like "allow users to force using python2 to run crab" ?
So can close this one and the CRAB vs. Rucio topic !

## Comment (makortel, 2023-10-21T04:36:06Z)

> * if most users need py2, we will stick with py2 with CMSSW.. you tell me
>   up to 11 ? 12 ? is there a watershed ? Whe does CMSSW switch to
>   using py3 for its own things ?

CMSSW became python3-only in 12_0_0_pre5. Framework itself became python3-compatible way earlier (can't really tell without deep investigation when), as did the configuration fragments used in production. User configuration is, of course, very different matter.

## Comment (belforte, 2023-10-23T08:38:55Z)

OK. And I note that non-py3 compliant statements in crabConfig or PSet only matter for `crab submit1.
Final recap:
1. CMSSW_12+ : python3 only
2. CMSSW up to 9 : python2 only
3. CMSSW_10,11 : python3 and we offer a `crab submit-with-python2` (will find a better name) #5239
