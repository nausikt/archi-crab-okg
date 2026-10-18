# dmwm/CRABClient issue #5375: clean up client HTTP 500 error message in general and also when task not found in database.

State: open
Opened: 2025-02-28T11:00:04Z
URL: https://github.com/dmwm/CRABClient/issues/5375

## Opening post (nausikt, 2025-02-28T11:00:04Z)

handling this frequent HTTP 500 ,when task not found, to HTTP 40X with more constructively, informatively messages. clean up flooded raw HTTP responses.

```
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
