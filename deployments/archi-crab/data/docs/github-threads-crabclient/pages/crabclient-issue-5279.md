# dmwm/CRABClient issue #5279: client v3.231101 creates bad PSet.pkl

State: closed
Opened: 2024-01-05T09:11:41Z
Closed: 2024-01-10T09:37:37Z
Labels: bug, critical
URL: https://github.com/dmwm/CRABClient/issues/5279

## Opening post (belforte, 2024-01-05T09:11:41Z)

as discussed in https://cms-talk.web.cern.ch/t/crab-job-failed-with-exit-code-7002/32986
changes introduced in v2.231101 make CRABClient use python3 for creating the pickle,
while when cmsRun reads it it uses python2. And fails.

## Comment (belforte, 2024-01-05T10:13:44Z)

Given that the error is not a pickle forma incompatibility, but rather about missing objects, I fear that we can't fix this by e.g. adding `protocol=0` to the pickle, but it is really due to different dependencies in CMSSW when using py2 or py3.
I.e. there is no alternative to "pickle using same python as cmsRun will use to unpickle".

options that come to mind

1.  expand the pickle in the job wrapper using python3 before passing it to cmsRun (or even do this client side and send a PSet.py ?)
2.  use JSON instead of pickle
3. go back to running CRABClient in same python as default for cmsRun (give up on using Rucio for CMSSW < 12)
4. move CMSSW config manipulation in https://github.com/dmwm/CRABClient/blob/218c2253cf5f3b4af7f3a9b00475f10cd8eee2c6/src/python/CRABClient/JobType/Analysis.py#L79 to a separate script which runs in current CMSSW default python
5. automatically switch to python2 for `crab submit` when using CMSSW < 12 like planned for #5239

## Comment (belforte, 2024-01-05T11:26:33Z)

@makortel   what is the way to tell if current CMSSW version will use python2 or python3 when it processes the PSet ?

I am leaning for option 5. It looks the safest and it is quite simple to implement with a couple lines in https://github.com/dmwm/CRABClient/blob/master/bin/crab

## Comment (belforte, 2024-01-05T13:24:55Z)

so adding this in https://github.com/dmwm/CRABClient/blob/master/bin/crab makes it work for config used by Federico Vazzoler in the cms-talk thread
```bash
[ $CMSSW_Major -le 12 ] &&  [ X$1 == Xsubmit ] && python_cmd="python"
```

I guess we only need to be sure at which CMSSW release to make the switch from python2 to python3 in preparing the PSet.pkl

## Comment (makortel, 2024-01-05T14:07:53Z)

> what is the way to tell if current CMSSW version will use python2 or python3 when it processes the PSet ?

I think the simplest is "CMSSW <= 12_0_0_pre3 uses python2, CMSSW >= 12_0_0_pre4 uses python3". So if one ignores the pre-releases (which is probably safe assumption by now), the "use python2 for CMSSW < 12" would indeed be the way to go.

## Comment (belforte, 2024-01-07T16:48:28Z)

Fixing this will also solve the problem reported in https://cms-talk.web.cern.ch/t/issue-with-crab-submit/33039 which again stems from using `python3` for `crab submit` on a CMSSW release which is not python3 ready

## Comment (belforte, 2024-01-08T18:17:44Z)

my apologiels @makortel, I do not know how/why I failed to note this comment of yours 3 days ago. Sorry for the extra noise in cms-talk 


> > what is the way to tell if current CMSSW version will use python2 or python3 when it processes the PSet ?
> 
> I think the simplest is "CMSSW <= 12_0_0_pre3 uses python2, CMSSW >= 12_0_0_pre4 uses python3". So if one ignores the pre-releases (which is probably safe assumption by now), the "use python2 for CMSSW < 12" would indeed be the way to go.
