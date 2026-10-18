# dmwm/CRABClient issue #5303: adapt to list of authorized retrievers having a `:`

State: closed
Opened: 2024-04-16T16:51:44Z
Closed: 2024-04-16T20:24:30Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5303

## Opening post (belforte, 2024-04-16T16:51:44Z)

this line
https://github.com/dmwm/CRABClient/blob/0a267d70365e02621f2187bf09ccad791ac2e60d/src/python/CRABClient/ProxyInteractions.py#L170
fails when the list of authorized retrievers has a `:` char in it, like needed for a Robot certificate.
Ineed currently we'd like to have

  trusted retrieval policy: /DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=817881/CN=Robot: cms crab|/DC=ch/DC=cern/OU=computers/CN=stefanov(m|m2).cern.ch|/DC=ch/DC=cern/OU=computers/CN=dciangot-tw.cern.ch

and that will result in
```
trustedRetrievers = '/DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=817881/CN=Robot'
```

but that will make Client always find that what was delegated is different from the reference from CRAB REST and force a new myproxy-init.

## Comment (belforte, 2024-04-16T16:56:01Z)

this should do, see https://docs.python.org/3.8/library/stdtypes.html?highlight=split#str.split
```python
trustedRetrievalPolicy.split(sep=':', maxsplit=1)[1]
```
