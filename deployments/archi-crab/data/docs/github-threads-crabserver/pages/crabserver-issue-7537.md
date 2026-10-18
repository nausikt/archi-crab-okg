# dmwm/CRABServer issue #7537: Use CRAB task to import existing dataset into RUCIO

State: closed
Opened: 2023-02-16T11:21:22Z
Closed: 2023-11-07T22:03:59Z
Labels: Priority: Medium, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7537

## Opening post (dciangot, 2023-02-16T11:21:22Z)

Minimal use case::
- I'm a user with a dataset published on phys03 DBS and I want to import this into RUCIO namespace/control

We can already work on provide an example task that will read data from data on `/store/user/<username>` and register a copy as a RUCIO owned file in `/store/rucio/user/`

Improvements/open items:

- [ ] crab data discovery of user scoped data in rucio
- [ ] RUCIO dataset dbs publication

## Comment (belforte, 2023-03-10T15:10:20Z)

after discussion, we are not sure how much needed this is now that @dynamic-entropy has a script which does the same. Pending further discussion with Rahul and @dciangot , let's lower priority/.

## Comment (belforte, 2023-11-07T22:03:59Z)

addressed in https://github.com/dmwm/CRABServer/issues/7755
