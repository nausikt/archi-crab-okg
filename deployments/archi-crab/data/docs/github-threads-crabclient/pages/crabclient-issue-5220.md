# dmwm/CRABClient issue #5220: only initialize Rucio when we have a proxy and if needed

State: closed
Opened: 2023-10-10T19:26:33Z
Closed: 2023-10-12T16:02:42Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5220

## Opening post (belforte, 2023-10-10T19:26:33Z)

current implementation effectively intializes Rucio client immediately
https://github.com/dmwm/CRABClient/blob/fae451b2c8e75614e73eba49aa05dd22cc9f936d/bin/crab.py#L30

Better to delay until we have ensure a valid proxy in SubCommand
https://github.com/dmwm/CRABClient/blob/fae451b2c8e75614e73eba49aa05dd22cc9f936d/src/python/CRABClient/Commands/SubCommand.py#L459-L461

and only if the command will require access to Rucio.

Rather than create yet another field in 
https://github.com/dmwm/CRABClient/blob/fae451b2c8e75614e73eba49aa05dd22cc9f936d/src/python/CRABClient/ClientMapping.py#L133
I will rename `initializeProxy` to `requiresRucio` since as indicated above ALL commands require a proxy !
