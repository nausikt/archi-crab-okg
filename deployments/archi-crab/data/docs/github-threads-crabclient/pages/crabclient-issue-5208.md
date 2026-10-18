# dmwm/CRABClient issue #5208: Usage of flags with dashes in pyCfgParams

State: closed
Opened: 2023-09-19T13:15:14Z
Closed: 2023-09-22T08:30:33Z
Labels: bug, On Hold, In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5208

## Opening post (kpedro88, 2023-09-19T13:15:14Z)

https://github.com/cms-sw/cmssw/pull/42650 introduces general support for dash-prefixed flags in cmsRun Python config files. However, the entry for `pyCfgParams` in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters states "double dashes break things". I would like to clarify if:
A. this warning is just there because previously, double dashes could break things in cmsRun itself, so it warns users in advance to avoid many spurious issue reports, or
B. there is actually some problem in the CRAB client that prevents it from accepting flags with double dashes.

If the latter, this will need to be fixed.

## Comment (belforte, 2023-09-19T15:55:56Z)

I need to review this old topic, but IIUC it used to be the latter. Some problem with passing strings around.

## Comment (kpedro88, 2023-09-20T14:35:50Z)

Okay, once https://github.com/dmwm/CRABServer/pull/7888 is deployed, we can try some test cases.

## Comment (belforte, 2023-09-20T16:51:59Z)

I had a look and I believe all work is done in the client.
IIUC the PSet.py is loaded with the pyCfgParams arguments and the result
is saved as a pickle. Those params are not passed to the grid job.
So it should be easy to test.
If you have a PSet at hand which tasks args, I can give it a try. I tried passing args to a plain PSet, but they are happily ignored AFAICT.

Or do you @kpedro88 maybe mean that future versions of `cmsRun` will accept additional params with `-option` and/or `--option` ? CRAB is not prepared to pass user provided arguments to `cmsRun`.
If that's the need, I will look into how best to support it.

## Comment (kpedro88, 2023-09-20T17:03:50Z)

the new functionality that is supported with https://github.com/cms-sw/cmssw/pull/42650 is a command like this:
```
cmsRun config.py --arg 1 --another-arg
```
where `--arg 1 --another-arg` are passed directly to `config.py` as `sys.argv` when it's evaluated in Python.
(to be clear, this technically works already, but requires various kludges, whereas in the future it will be supported natively.)

To me, what's in here already looks like it will work as intended: https://github.com/dmwm/CRABClient/blob/549c4e3b6158e8344315437d1d128f2288551d47/src/python/CRABClient/JobType/CMSSWConfig.py#L47-L62

https://github.com/cms-sw/cmssw/pull/42650 introduces a few test configs like [test_argparse.py](https://github.com/cms-sw/cmssw/pull/42650/files#diff-7d2267b2acb976530035ac7bf5fab8dfc6b6fc39b533801e0268f0216c4fedaa). I can try to make a test submission with something like this in the next few days.

## Comment (belforte, 2023-09-20T17:21:17Z)

I guess my problem is that I do not understand how `sys.argv` ends up in 
https://github.com/dmwm/CRABClient/blob/549c4e3b6158e8344315437d1d128f2288551d47/src/python/CRABClient/JobType/CMSSWConfig.py#L87 so am not able to say what will or will nor work and why. But I can certainly make tests.

I will follow up.

## Comment (kpedro88, 2023-09-20T17:28:00Z)

I took a similar approach to make `edmConfigDump` work with command-line arguments in https://github.com/cms-sw/cmssw/pull/42650/files#diff-1909f065fd31286cb427528c31b4d73328a06edc51a0cf606941efe6cdb80f84, so it seems like it can work. (though it uses the newer importlib rather than the deprecated imp; the latter will be removed in python 3.12, so a migration is warranted irrespective of this specific issue.)

## Comment (belforte, 2023-09-20T17:32:53Z)

that's not my code and surely I do not like `imp`, but we need to keep compatibly with older python versions as well since we use the one from the CMSSW release of the day.
I will figure out.

## Comment (kpedro88, 2023-09-20T19:51:22Z)

I think most `importlib` functionality should also be available in Python2.

## Comment (belforte, 2023-09-20T22:46:30Z)

oh well..
I tested [test_argparse.py](https://github.com/cms-sw/cmssw/pull/42650/files#diff-7d2267b2acb976530035ac7bf5fab8dfc6b6fc39b533801e0268f0216c4fedaa) with `pyCfgParams=["--maxEvents=8"]` on both CMSSW_13 (py3) and CMSSW_11 (py2.7) and it worked. 
So it seems like that warning in the twiki applied to some "old" things at the time (> 5 years ago). I clearly remember that some users hit this double-slash problem and was solved as indicated, but details have not been preserved. I also do not know what to make of [this twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile#argparse), in particular the thing about the `unamed '--' argument `

My test  fails when using CMSSW_6 inside cmssw_el6 container with
```
Importing CMSSW configuration tpar.py
ERROR: AttributeError: 'Process' object has no attribute 'maxEvents'
```
which looks like `tpar.py` worked but the config is not consistent with that CMSSW version.
IIUC, we do not care about what happens with older CMSSW when trying to use this new functionality.


**OTOH**, I found that `pyCfgParams=["--maxEvents 8"]` fails, you need `--maxEvents=8`  or the "non-obvious" `pyCfgParams=["--maxEvents", "8"]`, I think this can't be helped as far as arg passing goes, it we want to be friendly we should insert the missing `=` or split multistring args in the CRABClient.

One annoying "feature" is that if the argument is incorrect and makes the PSet exit, `crab submit` just stops and exits w/o printing any more messages. I will try to fix this.


@kpedro88  I will wait for more testing from you, if all goes well we close this and fix the documentation.
Let's leave for another time to replace `imp` with `importlib` (`importlib.machinery` is not there in py2)

## Comment (kpedro88, 2023-09-21T07:54:31Z)

That twiki shows one of the kludges/workarounds that is currently required to use argparse with `cmsRun`. (CRAB isn't directly `cmsRun`-ing the config, but first importing it with `sys.argv` set, so this isn't strictly necessary in the CRAB case.) https://github.com/cms-sw/cmssw/pull/42650 makes this unnecessary. Indeed, old versions of CMSSW will likely not support this out of the box, and that's fine.

`pyCfgParams = ["--maxEvents","8"]` is the "correct" way to do it, though the version with `=` is also okay.

I'll report once I've had time to run tests.

## Comment (belforte, 2023-09-21T08:29:38Z)

thanks
> pyCfgParams = ["--maxEvents","8"] is the "correct" way to do it, though the version with = is also okay.

I made this more clear in the documentation twiki

## Comment (belforte, 2023-09-21T12:39:13Z)

moved to  TOP of list, now that I am on it I'd like to get it out of the way quickly

## Comment (kpedro88, 2023-09-21T14:03:03Z)

Can you let me know when https://github.com/dmwm/CRABServer/pull/7888 is deployed in crab-dev? The full test needs this.

## Comment (belforte, 2023-09-21T14:05:38Z)

I had not realized the need, sorry. WIll do

## Comment (kpedro88, 2023-09-21T19:06:43Z)

My test was successful, so I think we can conclude that flags with dashes work fine.

However, to test with https://github.com/cms-sw/cmssw/pull/42650 compiled on top of CMSSW_13_3_0_pre3, I had to make several unexpected adjustments to the CRAB config. Namely:
```
config.JobType.inputFiles = [os.getenv('CMSSW_BASE')+'/bin',os.getenv('CMSSW_BASE')+'/python']
```

I was quite surprised to find that those directories are not included in the sandbox by default. (https://github.com/cms-sw/cmssw/pull/42650 puts important contents in both of them: modified `cmsRun` and `edmConfigDump` in `/bin`, and a new python component used by the latter in `/python`.) Personally, I would expect that excluding these would lead to a lot of confusion.

## Comment (belforte, 2023-09-21T21:07:23Z)

we have
`sendPythonFolder` for the latter.  I am open to making it default,  so far need was limited and sandbox size always an issue. That's why it is not default. That's an decision taken by other years ago, as usual. Possibly things have changed and I notice that python directory is usually empty, so .. if user puts code there seems safe to assume that it is needed. Yet it could be simply some work in progress. Anyhow on such matters we go with what CMSSW folks say, of course !
Should we follow same line for `venv` folder as well and always include ?

The less config. parameters we have in CRAB, the happier I am !

I am suprised that `bin` is needed, never heard of it before. So far $CMSSW_BASE/bin is happily empty. Why does someone need a different version of cmsRun and edmConfigDump from what is in the release, testing new code aside ?
Anyhow.. .as before, if we need, we will add. But if a generic "you" is testing locally and have 3 or four versions of those binaries and submit a crab task meant to do other things, and hit sandbox limit, I fear you will come complaining.

I'd be happy to have a CMSSW tool which packages the sandbox for us, delivering CRAB from any responsibility there.

## Comment (kpedro88, 2023-09-22T07:45:51Z)

The `$CMSSW_BASE/python` directory gets populated if there are any folders `$CMSSW_BASE/src/Subsystem/Package/python`; it's how the files in those folders become importable by python (in the system path). Since CRAB imports and concretizes the config file on the client side, it isn't strictly needed for `cmsRun` jobs. However, for "scriptExe" jobs, there are many cases where it would be needed. (In particular, it seems inconsistent to me that CRAB always includes `$CMSSW_BASE/src/Subsystem/Package/python` folders in the sandbox, but not the `$CMSSW_BASE/python` that actually makes them work...)

Any compiled executable goes in `$CMSSW_BASE/bin` - only the latest version of the compiled executable, not multiple versions. Again, this is mostly important for "scriptExe" jobs. But for this particular feature, since it most likely won't be backported (because of the need to fix dozens of unit tests), a user might want to install a modified `cmsRun` manually if using an older release.

Perhaps the Core SW group can make a global recommendation for sandboxing. Personally, I keep everything except for `$CMSSW_BASE/test` and `$CMSSW_BASE/tmp` when making my own sandboxes outside of CRAB (but at least `$CMSSW_BASE/logs` can probably also be omitted).

## Comment (kpedro88, 2023-09-22T07:50:23Z)

As a reference, in my working area for https://github.com/cms-sw/cmssw/pull/42823 (which includes many packages, and also the other related PRs), `$CMSSW_BASE/bin` is 4.8MB and `$CMSSW_BASE/python` is 1.7MB. `lib` and `include` are the ones that get big (>100MB) when compiling a lot of packages.

In the full release CMSSW_13_3_0_pre3 on cvmfs, `$CMSSW_RELEASE_BASE/bin` is 48MB and `$CMSSW_RELEASE_BASE/python` is 3.6MB. A user could of course do something unusual that would put a huge executable in `$CMSSW_BASE/bin`, but I can't think of any legitimate way for `$CMSSW_BASE/python` to get much larger than that.

## Comment (belforte, 2023-09-22T08:30:33Z)

> Personally, I keep everything except for $CMSSW_BASE/test and $CMSSW_BASE/tmp when making my own sandboxes

you will be suprised (but maybe not !) at the kind and amount of junk people have in $CMSSW_BASE,
from root files to CRAB work directories :-(

Anyhow, short answer is that with all likelyhood when Marco and others added the `sendPythonFolder` they did not have a good understanding of how it works.
I am happy to always include ` $CMSSW_BASE/python`

We can "try" adding `CMSSW_BASE/bin` as well since it is very likely to be empty unless when people know about it and know what they are doing. At the end of the day, if sandbox is too big we print a size-sorted list of content and hopefully user will figure out.

I wish we could easily allow for bigger sandboxes (current limit is 120MB), but it really depends on size x number of jobs starting at more or less similar time. HTCondor is already reporting long queues and failures in that area every now and then.

So I will close this as "nothing required"  and open a new issue about changes to what we put in sandbox.
Thanks

## Comment (kpedro88, 2023-09-22T08:48:31Z)

One more note for posterity: if a user wants to write their arguments exactly as they would on the command line, rather than splitting them up into a Python list by hand, they can do the following:
```python
import shlex
args = '--arg 1 --another-arg "my name"'
config.JobType.pyCfgParams = shlex.split(args)
```

The output of `shlex.split(args)` for this case is:
```python
['--arg', '1', '--another-arg', 'my name']
```
i.e. it correctly preserves quoted spaces etc.

## Comment (belforte, 2023-09-22T09:06:07Z)

will add to twiki
