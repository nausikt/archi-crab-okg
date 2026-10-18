# dmwm/CRABClient issue #5182: stop distributing ol python2 DBS Client

State: closed
Opened: 2023-01-11T19:06:20Z
Closed: 2023-07-13T09:01:19Z
Labels: HighPrio, In Progress, Py2/3
URL: https://github.com/dmwm/CRABClient/issues/5182

## Opening post (belforte, 2023-01-11T19:06:20Z)

since it is broken anyhow and CRAB does not use it. Users should be directed to new (py3 only) client
see also https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#use_new_python3_DBSClient

## Comment (belforte, 2023-07-13T09:01:19Z)

Done.
https://github.com/cms-sw/cmsdist/pull/8568 and https://github.com/cms-sw/cmsdist/pull/8580
are now in production
