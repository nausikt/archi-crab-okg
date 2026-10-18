# dmwm/CRABServer issue #7621: deletewarnings API should not raise fatal error if thers' no warning

State: closed
Opened: 2023-04-28T12:43:55Z
Closed: 2023-04-28T17:10:50Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/7621

## Opening post (belforte, 2023-04-28T12:43:55Z)

I got this:

Fri, 28 Apr 2023 14:31:46 CEST(+0200):DEBUG:RESTInteractions Sleeping 30 seconds after HTTP error. Error details:  {'Content-Length': '745', 'Content-Type': 'text/html;charset=utf-8', 'Date': 'Fri, 28 Apr 2023 12:31:46 GMT', 'Response-Proto': 'HTTP/1.1', 'Response-Status': '500 Internal Server Error', 'Response-Status-Code': '500', 'Response-Time': '9.008272ms', 'Response-Time-Seconds': '0.009009315', 'Server': 'CherryPy/18.8.0', 'X-Content-Type-Options': 'bla', 'X-Error-Detail': 'Execution error', 'X-Error-Http': '500', 'X-Error-Id': '4a02e641a9ec1018c05cfeeae56cbae2', 'X-Error-Info': 'No warnings to remove.', 'X-Rest-Status': '403', 'X-Rest-Time': '6962.538 us'}

Note:
* HTTP `500  Internal Server Error`  - means fatal error
* `Error-Info': 'No warnings to remove.` -  this is not an error !

OTOH:
` X-Rest-Status': '403`
 does this mean that CRAB REST returned 403 (good) and something changed it to 500 ?

## Comment (belforte, 2023-04-28T12:45:43Z)

anyhow, I got it while testing, in real life we will neve call `deletewarning` if there's not warning, and in any case it is eventually harmless, simply annoying messages and a few sleep-retry.

## Comment (belforte, 2023-04-28T15:48:40Z)

Actually the  `X-Rest-Status': '403` was not an attempt to return an "invalid call" HTTP error in the 4xx range,
just something defined in WMCore in
https://github.com/dmwm/WMCore/blob/31d65166dc62c7251edd52890bc4ac2f0b79d7fe/src/python/WMCore/REST/Error.py#L218-L228
it was really a "bad idea from original implementor", there is no reason to raise an error here !
https://github.com/dmwm/CRABServer/blob/3d7cb32e23e1b3c0da6fd2f93c7f646f093509a5/src/python/CRABInterface/RESTTask.py#L271-L274

There is nothing in https://github.com/dmwm/WMCore/blob/31d65166dc62c7251edd52890bc4ac2f0b79d7fe/src/python/WMCore/REST/Error.py for "Nothing to do", and surely makes no sense to add this. I do not see any error here,
just do nothing and return success.

## Comment (belforte, 2023-04-28T16:20:03Z)

Since it is trivial, I fix it now that  I have things at my fingertips.
