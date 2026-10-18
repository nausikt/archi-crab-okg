# dmwm/CRABServer issue #8404: make REST accept submit URL's w/o `inputdata` arg

State: closed
Opened: 2024-05-15T14:52:19Z
Closed: 2024-05-15T19:37:45Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8404

## Opening post (belforte, 2024-05-15T14:52:19Z)

make it REALLY optional (see also #8399 )

currently submission for PrivatMC fails because of

https://github.com/dmwm/CRABServer/blob/c69980662cbd4fa76e3801b6f3085856032743d6/src/python/CRABInterface/RESTUserWorkflow.py#L344-L345

which is not capable to accept missing `inputdata`
