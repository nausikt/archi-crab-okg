# dmwm/CRABServer issue #8957: find better way to handling HTTP 500 when task is not in the DB

State: open
Opened: 2025-02-28T10:27:06Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8957

## Opening post (nausikt, 2025-02-28T10:27:06Z)

find better way to handling HTTP 500 when task is not in the DB and make client print a more useful message. At least should not have this flooded HTTP headers.
  
```
> GET /crabserver/preprod/task?subresource=search&workflow=250227_151017%3Acrabint1_crab_rucio_transfers_withnoneedm_20250227_161013 HTTP/1.1
> Host: cmsweb-testbed.cern.ch:8443
> User-Agent: CRABClient/v3.250217
> Accept: */*
> Content-Length: 101
> Content-Type: application/x-www-form-urlencoded
> 
} [101 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [6710 bytes data]
* Mark bundle as not supporting multiuse
< HTTP/1.1 500 Internal Server Error
< Content-Length: 745
< Content-Type: text/html;charset=utf-8
< Date: Thu, 27 Feb 2025 23:12:32 GMT
< Response-Proto: HTTP/1.1
< Response-Status: 500 Internal Server Error
< Response-Status-Code: 500
< Response-Time: 370.697406ms
< Response-Time-Seconds: 0.370703686
< X-Content-Type-Options: bla
< X-Error-Detail: Execution error
< X-Error-Http: 500
< X-Error-Id: 6d0a9941793d45956f38c0a160fabecc
< X-Error-Info: Impossible to find task 250227_151017:crabint1_crab_rucio_transfers_withnoneedm_20250227_161013 in the database.
< X-Rest-Status: 403
< X-Rest-Time: 365563.393 us
< 
{ [586 bytes data]
100   846  100   745  100   101   1915    259 --:--:-- --:--:-- --:--:--  2174
* Connection #0 to host cmsweb-testbed.cern.ch left intact
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
status_command_output is None for [2502](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/52065402#L2502)27_151017:crabint1_crab_rucio_transfers_withnoneedm_20250227_161013
```

## Comment (belforte, 2025-02-28T10:41:20Z)

you will need another issue in CRABClient repo
Note about crab client:
the above full-blast thing is when using the CRAB python API
Client is less noisy, but will too much noise for my taste:

```console
belforte@lxplus813/ste> crab status -d crab_20250226_192242/
Rucio client intialized for account belforte
Fatal error trying to connect to https://cmsweb-testbed.cern.ch:8443/crabserver/preprod/task?subresource=search&workflow=250226_182249%3Abelforte_crab_20250226_192242 using subresource=search&workflow=250226_182249%3Abelforte_crab_20250226_192242.
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
Reason is: Impossible to find task 250226_182249:belforte_crab_20250226_192242 in the database.
Error Id: 600683b4473ff85ea35000ea91786d7e
belforte@lxplus813/ste> 
```

## Comment (belforte, 2025-02-28T10:43:21Z)

important note
**Error Id: 600683b4473ff85ea35000ea91786d7e**
is a very useful line. We can talk about it. But make sure that you preserve it

## Comment (nausikt, 2025-02-28T10:44:39Z)

I see. Acknowledge @belforte
