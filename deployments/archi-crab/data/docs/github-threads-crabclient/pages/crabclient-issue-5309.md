# dmwm/CRABClient issue #5309: optional string configuration param should default to None, not `''`

State: closed
Opened: 2024-05-13T17:35:49Z
Closed: 2024-05-20T16:12:03Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5309

## Opening post (belforte, 2024-05-13T17:35:49Z)

this will allow "sane" validation in the REST, see e.g. https://github.com/dmwm/CRABServer/issues/8372#issuecomment-2106380644

I suspect that current code is a legacy of (very old) thing of trying to validate parameter type in the client, and some mis-conception/mis-comunication about  what `required=False` should mean.

Of course need to test that nothing breaks with this change

## Comment (belforte, 2024-05-13T20:18:41Z)

all standard tests worked https://github.com/dmwm/CRABServer/issues/8400
But I do not feel fully confident yet.

## Comment (belforte, 2024-05-13T21:28:21Z)

I verified that with this change when `config.Data.inputDataset ` is not present in `crabConfig.py` the URL used for submission does not have `&inputdata=&` but simply `inputdata` argument is not there.
Which is the desired behavior.

## Comment (belforte, 2024-05-13T21:28:34Z)

Trying to think of what else to test.

## Comment (belforte, 2024-05-15T10:21:38Z)

testing StatusTracking as well: https://github.com/dmwm/CRABServer/issues/8403

hmm.. submission of privateMC to preprod with this client failed, but it worked on my (modified) test2. Investigating.
OK. in my earlier test I used un-modified client.
Problems is clear in https://github.com/dmwm/CRABServer/blob/c69980662cbd4fa76e3801b6f3085856032743d6/src/python/CRABInterface/RESTUserWorkflow.py#L345
```python
                if param.kwargs['inputdata'] or 'inputblocks' in param.kwargs:
```

## Comment (belforte, 2024-05-15T12:27:28Z)

so this will be a 3-step process:
1.  change REST to accept new URL
2. change Client not to send `&inputata=&` in the URL
3. change REST to use the new format to do a proper and cleaner validation of inputdata

## Comment (belforte, 2024-05-20T16:12:03Z)

closing again. Will remember to update REST before tagging and deploying.
