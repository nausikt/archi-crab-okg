# dmwm/CRABClient issue #5380: crab --version requires cmssw env

State: closed
Opened: 2025-03-19T11:16:45Z
Closed: 2025-04-02T08:17:38Z
Labels: enhancement, HighPrio, In Progress
URL: https://github.com/dmwm/CRABClient/issues/5380

## Opening post (smuzaffar, 2025-03-19T11:16:45Z)

I noticed that even running `crab --version` requires cmssw env and it also tries to create `crab.log`  ( which means one can not run it directly from the release area on cvmfs). Is it possible to not depend of cmssw env and create log for ` crab --version` ?

## Comment (belforte, 2025-03-19T12:54:37Z)

I will look into this.

## Comment (belforte, 2025-04-01T14:43:52Z)

@smuzaffar in my test `crab --version` does not create a log file. Can you help me to reproduce ?

## Comment (smuzaffar, 2025-04-01T14:55:31Z)

@belforte , I can not reproduce the log file creation issue for `crab --version`. I guess might have run `crab version` ( which is not a crab command and in that case crab failed with [a])

[a]
```

Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250318.00/bin/crab.py", line 103, in log_exception
    filehandler = logging.FileHandler(client.logger.logfile)
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-ccc34bac15aa449b4c76ba24d02d2fd7/lib/python3.9/logging/__init__.py", line 1146, in __init__
    StreamHandler.__init__(self, self._open())
  File "/cvmfs/cms.cern.ch/el8_amd64_gcc12/external/python3/3.9.14-ccc34bac15aa449b4c76ba24d02d2fd7/lib/python3.9/logging/__init__.py", line 1175, in _open
    return open(self.baseFilename, self.mode, encoding=self.encoding,
OSError: [Errno 30] Read-only file system: '/cvmfs/cms.cern.ch/el8_amd64_gcc12/cms/cmssw/CMSSW_15_1_0_pre1/crab.log'

```

## Comment (belforte, 2025-04-01T15:01:02Z)

as to work w/o cmsenv... What I can do is to move the check later in the code, right after arg. parsing,  so that as long as there is a decent python available and the argument is `--version` which makes it stop when detected, there will be no complain.  I guess it will still serve the purpose of avoiding that users run it with "who knows what python"' and report errors which we really should not be looking at.

## Comment (belforte, 2025-04-01T16:36:50Z)

@smuzaffar I'd rather not rewrite the [bash wrapper](https://github.com/dmwm/CRABClient/blob/f372163165b2f9313ea6be3fd0934ed6ed9570dc/bin/crab) which uses CMSSW_VERSION to e.g. decide if to use python or python3. Can you accept that if you do not setup cmsenv, you still define that variable ?
Which python do you want to use ? That wrapper uses `python` for older CMSSW's, but there's no `python` on CC8 , only python2 or python3. Shall we change to `python2` in there ? Maybe a good thing anyhow. It will hopefully still work :-)

## Comment (belforte, 2025-04-01T16:52:41Z)

please have a look at proposed changes

## Comment (smuzaffar, 2025-04-02T06:19:36Z)

aw, I did not realize that crab needs CMSSW_VERSION to decide which python to you. I am fine with crab requiring cmssw env for `--version` too. So no need to change bash wrapper. Feel free to close this issue

## Comment (belforte, 2025-04-02T08:17:38Z)

OK. Thanks Shahzad !
