# dmwm/CRABClient issue #5210: always include `$CMSSW_BASE/python`and `bin` in sandbox

State: closed
Opened: 2023-09-22T09:22:47Z
Closed: 2023-10-09T19:17:03Z
Labels: enhancement, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5210

## Opening post (belforte, 2023-09-22T09:22:47Z)

see https://github.com/dmwm/CRABClient/issues/5208#issuecomment-1730960183

- [x] code
- [ ] documentation [Twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile)

## Comment (belforte, 2023-10-09T14:45:19Z)

@kpedro88 what about `cfipython` directory which current code always includes when user say `sendPythonFolder` (which will become obseolete) ? Shall we always include that one as well ?
https://github.com/dmwm/CRABClient/blob/3e3582d4738a400b29d291b9bc11897b943d029a/src/python/CRABClient/JobType/UserTarball.py#L129-L131

## Comment (kpedro88, 2023-10-09T14:48:09Z)

Yes, that folder is a total of ~4MB in a full CMSSW release, so it will be quite small for user releases, but necessary for CMSSW to work as intended when a package with plugins that use `fillDescriptions` is installed.
