# dmwm/CRABServer issue #7624: map Instance to restHost/dbInstance in a single place

State: open
Opened: 2023-05-03T11:54:26Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7624

## Opening post (belforte, 2023-05-03T11:54:26Z)

we should NOT have multple instance of this code
https://github.com/dmwm/CRABServer/blob/f601c4b61cd2df2a4e8d0bf77f665e8a34c786e5/src/python/TaskWorker/MasterWorker.py#L194-L217
not even as a function called in several places.
Instead the config object should be able to present the correct parameters to the code which uses it.
e.g. by doing this work at the time config. is read from disk
See also discussion in https://github.com/dmwm/CRABServer/pull/7620#issuecomment-1531726093 and nearby comments.

## Comment (belforte, 2024-05-23T10:49:27Z)

Give to Vijay as a way to get familiar with code ?

## Comment (belforte, 2024-06-25T13:44:17Z)

this may be "as simple as" using everywhere
https://github.com/dmwm/CRABServer/blob/43a8454abec4059ae5b2804b4efe8e77553d1f38/src/python/TaskWorker/WorkerUtilities.py#L13

Indeed everything in WorkerUtilities.py is not TW specific, and should be part of the rationalization of the code indicated in https://github.com/dmwm/CRABServer/issues/7765

Together with a rationalization of config files for TW and Publishers so that we cat get from them a REST or Rucio configuration object to pass to the methods which will instantiate the client.

So I have added myself back to this and will start by trying to better describe the problem which I want to solve and my ideas about the new format.
High leverl goal is to avoid code duplication and encapsulate funcionalities to make code base more readable.

Hopefully it will address what @novicecpp and myself talked about.
