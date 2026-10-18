# dmwm/CRABClient issue #5416: changed for http2 in #5412 do not work on SL6

State: closed
Opened: 2025-09-25T12:21:05Z
Closed: 2025-09-26T14:08:36Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5416

## Opening post (belforte, 2025-09-25T12:21:05Z)

When using SL6 based (yet still supported) CMSSW releases like CMSSW_10_1 and earlier, CRABClient fails to import `http`
```
  File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02908/share/cms/crab-dev/v3.250908.00/lib/CRABClient/RestInterfaces.py", line 21, in <module>
    import http
ImportError: No module named http
```

@Lorenzov1999   Please provide a backward-compatible implementation

Until then we need to roll back your #5412  since our intergration tests are failing

## Comment (belforte, 2025-09-25T12:30:31Z)

@nausikt feel free to fix this yourself if you know how and get to it sooner than @Lorenzov1999 , otherwise please roll it back and make a new tag for crab-dev w/o it

## Comment (Lorenzov1999, 2025-10-02T09:47:14Z)

Thanks! Sorry for not taking care of this, I have been away for a while.
