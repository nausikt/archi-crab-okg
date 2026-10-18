# dmwm/CRABServer pull request #9283: add debug xrootd logging

State: open
Opened: 2026-03-24T09:56:52Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/pull/9283

## Opening post (aspiringmind-code, 2026-03-24T09:56:52Z)

Fix #9282

## Comment (cmsdmwmbot, 2026-03-24T09:58:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 7 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2758/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-24T10:44:52Z)

LGTM - Thanks. Did you test ?

## Comment (aspiringmind-code, 2026-03-24T12:02:45Z)

Yes
```
[vchakrav@lxplus915 results]$ grep xroot job_out.1.0.txt 
XRD_LOGLEVEL set to Debug for xrootd verbose logging
== CMSSW: [2026-03-24 12:42:29.306382 +0100,Debug  ,Utility           ] Initializing xrootd client version: unknown
== CMSSW: [2026-03-24 12:42:29.307091 +0100,Debug  ,PlugInMgr         ] Processing plug-in definitions in /etc/xrootd/client.plugins.d...
== CMSSW: [2026-03-24 12:42:29.307580 +0100,Debug  ,PlugInMgr         ] Processing plug-in definitions in /srv/.xrootd/client.plugins.d...
== CMSSW: [2026-03-24 12:42:29.307587 +0100,Debug  ,PlugInMgr         ] Unable to process directory /srv/.xrootd/client.plugins.d: [ERROR] OS Error: no such file or directory
```
