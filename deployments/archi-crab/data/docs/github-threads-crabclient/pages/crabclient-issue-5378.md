# dmwm/CRABClient issue #5378: latest client v3.250217 is broken for `submit` on CMSSW < 12

State: closed
Opened: 2025-03-13T16:34:21Z
Closed: 2025-03-18T12:01:17Z
Labels: bug, critical, In Progress
URL: https://github.com/dmwm/CRABClient/issues/5378

## Opening post (belforte, 2025-03-13T16:34:21Z)

e.g. on CMSSW_10
```text
Singularity> crab submit
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250217.00/bin/crab.py", line 154, in <module>
    client = CRABClient()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250217.00/bin/crab.py", line 54, in __init__
    self.subCommands = getAvailCommands()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250217.00/lib/CRABClient/ClientUtilities.py", line 341, in getAvailCommands
    subcmdplugins = getPlugins(subcmdpath, subcmdname, ['SubCommand'])
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250217.00/lib/CRABClient/ClientUtilities.py", line 270, in getPlugins
    mod = __import__('%s.%s.%s' % (namespace, plugins, el[1]), globals(), locals(), el[1])
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250217.00/lib/CRABClient/Commands/recover.py", line 713
    print(submitConfiguration, file=fd)
                                   ^
SyntaxError: invalid syntax
Singularity> 
```

The problem is that for `submit` we are stuck with python2 until CMSSW_12 and all code is imported anyhow in the client, even if not executed, so that line triggers a syntax error even if `crab recover` will be executed in `python3` for that release.

Looks like we never tested the client with earlier CMSSW :-( sigh...

## Comment (belforte, 2025-03-13T16:55:27Z)

indeed failure is imeediate in Jenkins as well
https://github.com/dmwm/CRABServer/issues/8985#issuecomment-2721964449

too bad that we stopped running it
