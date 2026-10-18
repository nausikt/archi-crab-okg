# dmwm/CRABServer issue #8607: use HTC Python bindings to submit sub-DAG's

State: open
Opened: 2024-08-09T21:29:55Z
Labels: Type: Enhancement, Priority: Medium, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8607

## Opening post (belforte, 2024-08-09T21:29:55Z)

instead of forking a CLI command in
https://github.com/dmwm/CRABServer/blob/3616cf5e4ac018be9445d77a1dca28e190edfa0c/src/python/TaskWorker/Actions/PreDAG.py#L335-L339

could use the python API, will make code easier to read and avoid the problem with duplicated `queue` statements #8585 

instead of using `-insert_sub_file FileName` we should read subdag.jdl into a Submit object, create another Submit object using `Submit.from_dag` and combine the two in memory, then submit the final obejct.

See small discussion aroung this comment https://github.com/dmwm/CRABServer/issues/8272#issuecomment-2278765907

Or something like that !

## Comment (belforte, 2024-08-09T21:30:13Z)

not a priority though
