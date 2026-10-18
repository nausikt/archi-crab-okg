# dmwm/CRABClient issue #5268: allow use --task/--instance as alternative to --dir

State: closed
Opened: 2023-12-01T13:02:10Z
Closed: 2023-12-01T13:11:22Z
Labels: Done
URL: https://github.com/dmwm/CRABClient/issues/5268

## Opening post (mapellidario, 2023-12-01T13:02:10Z)

#### status quo

When executing a crab command that requires the requestcache in a local project directory (for example `crab status`), if the user does not have the cache, he/she needs to create it with `crab remake --task`.

#### solution

It would be nice to be able to run crab remake automatically if the user executes `crab status --task=`
