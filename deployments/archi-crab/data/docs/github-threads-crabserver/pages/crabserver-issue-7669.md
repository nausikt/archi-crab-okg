# dmwm/CRABServer issue #7669: urlencode missing in TapeRecallManager

State: closed
Opened: 2023-06-15T16:35:48Z
Closed: 2023-06-15T17:04:48Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7669

## Opening post (belforte, 2023-06-15T16:35:48Z)

in here
https://github.com/dmwm/CRABServer/blob/71fbc9d5c939f21b6aa92a715a3932c62f26d974/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L178-L180

this leads to the very confusing error `"Incorrect 'subresource' parameter`
```
2023-06-15 14:30:51,320:ERROR:TapeRecallManager:Error uploading warning: url=https://cmsweb.cern.ch:8443/crabserver/prod/task, code=400, reason=Bad Request, headers={'Date': 'Thu, 15 Jun 2023 12:30:51 GMT', 'Server': 'Apache', 'Content-Type': 'text/html;charset=utf-8', 'Content-Length': '733', 'X-Rest-Status': '302', 'X-Error-Http': '400', 'X-Error-Id': 'bb29507a2d983ee90b0fe7ddd6e2a0d7', 'X-Error-Detail': 'Invalid input parameter', 'X-Error-Info': "Incorrect 'subresource' parameter <class 'NoneType'> None", 'X-Rest-Time': '2988.815 us', 'CMS-Server-Time': 'D=11093 t=1686832251307996', 'Connection': 'close'},
```
