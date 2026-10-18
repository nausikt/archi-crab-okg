# dmwm/CRABServer issue #8878: trying to kill a task  should not be an HTTP 500 error

State: closed
Opened: 2025-01-10T19:44:46Z
Closed: 2025-01-29T15:38:51Z
Labels: Type: Enhancement, Type: Support
URL: https://github.com/dmwm/CRABServer/issues/8878

## Opening post (belforte, 2025-01-10T19:44:46Z)

when client tries to kill a task which is not in a "killable" status, server should report e.g. HTTP 400 which will hopefully result in a better handling on client side, instead of making it look like a server error
```
belforte@lxplus807/TC3> crab kill -d crab_20250110_183756/
Fatal error trying to connect to https://cmsweb-test2.cern.ch:8443/crabserver/dev/workflow using workflow=250110_173801%3Abelforte_crab_20250110_183756.
exit code from curl = 0
HTTP code/reason = 500/Internal Server Error .  stdout:
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
    <title>500 Internal Server Error</title>
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
        <h2>500 Internal Server Error</h2>
        <p>Execution error</p>
        <pre id="traceback"></pre>
    <div id="powered_by">
      <span>
        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.8.0</a>
      </span>
    </div>
    </body>
</html>

The server answered with an error.
Server answered with: Execution error
Reason is: You cannot kill a task if it is in the SUBMITFAILED status
Error Id: 1e5842978d65bd5fd7bb6d2d85dd65d3
belforte@lxplus807/TC3> 


```

## Comment (nausikt, 2025-01-29T04:04:30Z)

I've tested on `test12`, and the test results are as follows. 
_____________
===== When user have any **non-killable status**  task like `SUBMITFAILED` =====
```
[kphornsi@lxplus980 CRABClient]$ crab status -d /tmp/crabStatusTracking/crab_20250129_002856
Rucio client intialized for account kphornsi
CRAB project directory:		/tmp/crabStatusTracking/crab_20250129_002856
Task name:			250128_232905:kphornsi_crab_20250129_002856
Grid scheduler - Task Worker:	crab3@vocms9999.cern.ch - crab-dev-tw03
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/250128_232905%3Akphornsi_crab_20250129_002856
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=250128_232905%3Akphornsi_crab_20250129_002856&from=1738103346000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol', 'T2_US_Florida', 'T2_US_MIT']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Failure message from server:	The CRAB server backend was not able to contact the Grid scheduler. Please try again later. If the error persists send an e-mail to cmstalk+computing-tools@dovecotmta.cern.ch. Message from the scheduler: Unable to contact the collector and cached results does not exist for crab3@vocms9999.cern.ch
Log file is /tmp/crabStatusTracking/crab_20250129_002856/crab.log
```
===== The New Response will be 400 BadRequest instead of 500 Internal Server Error =====
```
[kphornsi@lxplus980 CRABClient]$ crab kill -d /tmp/crabStatusTracking/crab_20250129_002856
Fatal error trying to connect to https://cmsweb-test12.cern.ch:8443/crabserver/devthree/workflow using workflow=250128_232905%3Akphornsi_crab_20250129_002856.
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
Error Id: b2639249e7d4f43f463b39d0efb146ae
```

## Comment (nausikt, 2025-01-29T23:08:05Z)

Fix minor issue in #8897 with #8905
