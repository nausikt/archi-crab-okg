# dmwm/CRABServer pull request #8905: Fixes 400 exception msg

State: closed
Opened: 2025-01-29T22:56:44Z
Closed: 2025-01-29T23:05:34Z
URL: https://github.com/dmwm/CRABServer/pull/8905

## Opening post (nausikt, 2025-01-29T22:56:44Z)

fix #8897 @belforte I'm sorry, Stefano. My bad, I presumed too much until I misinterpreted your messages.

## Comment (cmsdmwmbot, 2025-01-29T22:58:41Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2358/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-29T23:01:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 308 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2359/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-01-29T23:05:34Z)

The message was preserved now. sorry for the noises though! will make sure i get better at it from time to time.
```
[kphornsi@lxplus932 workspace]$ crab kill -d /tmp/crabStatusTracking/crab_20250129_232618
Fatal error trying to connect to https://cmsweb-test12.cern.ch:8443/crabserver/devthree/workflow using workflow=250129_222624%3Akphornsi_crab_20250129_232618.
exit code from curl = 0
HTTP code/reason = 400/Bad Request .  stdout:
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
    <title>400 Bad Request</title>
    <style type="text/css">
    #powered_by {
        margin-top: 20px;
        border-top: 2px solid black;
        font-style: italic;
    }

    #traceback {
        color: red;
    }
    </style>
</head>
    <body>
        <h2>400 Bad Request</h2>
        <p>You cannot kill a task if it is in the SUBMITFAILED status</p>
        <pre id="traceback"></pre>
    <div id="powered_by">
      <span>
        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.8.0</a>
      </span>
    </div>
    </body>
</html>

The server answered with an error.
Server answered with: You cannot kill a task if it is in the SUBMITFAILED status
Error Id: 215a3e2ad95facb5452ba25326d30dad
```

## Comment (belforte, 2025-01-29T23:47:21Z)

looks better ! Thanks !
