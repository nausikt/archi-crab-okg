# dmwm/CRABServer issue #7583: REST API - Have less and more generic endpoints

State: open
Opened: 2023-04-05T11:24:40Z
Labels: Priority: Medium, Status: Available, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7583

## Opening post (mapellidario, 2023-04-05T11:24:40Z)

As mentioned by Stefano in [1], we should have less endpoints in our REST API, that provide more generic data. It should then be up to the client to aggregate it.

One obvious point where to start from it RESTTask.py, that has a lot of subresource endpoints [2]. 

For example, the following feel a bit redundant:

- https://github.com/dmwm/CRABServer/blob/2f9eb533f8245f3fef4869fb38aa9096c165f655/src/python/CRABInterface/RESTTask.py#L67
- https://github.com/dmwm/CRABServer/blob/2f9eb533f8245f3fef4869fb38aa9096c165f655/src/python/CRABInterface/RESTTask.py#L100
- https://github.com/dmwm/CRABServer/blob/2f9eb533f8245f3fef4869fb38aa9096c165f655/src/python/CRABInterface/RESTTask.py#L174
- https://github.com/dmwm/CRABServer/blob/2f9eb533f8245f3fef4869fb38aa9096c165f655/src/python/CRABInterface/RESTTask.py#L185

---

[1] https://github.com/dmwm/CRABServer/pull/7581#issuecomment-1496200880
[2] https://github.com/dmwm/CRABServer/blob/2f9eb533f8245f3fef4869fb38aa9096c165f655/src/python/CRABInterface/Regexps.py#L89

## Comment (belforte, 2023-04-05T13:43:27Z)

the original line of thought was to have a list of all specific action which one may need to do and have an API for each. That may help prevent mistakes if you expect random developers to try to use your API's and possibly make damage (to themsleves) ? since early developers assumed that users would interact with CRAB Server via its RESTful API. In time it has become clear people outside the CRAB dev tem use CRABClient. So we can take a more flexible attitude.
