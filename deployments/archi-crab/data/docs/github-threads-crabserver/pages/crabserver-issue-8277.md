# dmwm/CRABServer issue #8277: remove use of  HTCondorUtils.AuthenticatedSubproces

State: closed
Opened: 2024-03-12T22:22:48Z
Closed: 2024-04-12T11:00:43Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8277

## Opening post (belforte, 2024-03-12T22:22:48Z)

it was needed when TaskWorker was using multiple X509 proxies at same time and needed to submit to schedulers with the user's proxy.

Now that we submit using a single service token, w/o GSI, there's no need anymore

This is needed in order to progress on #8272

## Comment (belforte, 2024-03-19T14:06:06Z)

So far done in DagmanSubmitter and it works.

## Comment (belforte, 2024-04-03T14:22:05Z)

modified code for DagmanSubmitter is in my branch https://github.com/belforte/CRABServer/tree/stop-using-authenticated-subprocess-8277
I am not sure if possible errors are properly handled in this version, in particular I am trying to avoid returning a clusterId incase `schedd.submit` works but `schedd.spool` fails.
