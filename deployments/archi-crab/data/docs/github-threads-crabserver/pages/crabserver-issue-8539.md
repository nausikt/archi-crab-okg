# dmwm/CRABServer issue #8539: avoid exiting container on command error

State: closed
Opened: 2024-07-03T10:43:24Z
Closed: 2024-09-03T11:30:18Z
Labels: Type: Enhancement, Type: Question, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8539

## Opening post (belforte, 2024-07-03T10:43:24Z)

when inside e.g. TW container with `docker exec -ti TaskWorker bash`, after I do
`source env.sh` or `source env.sh -g` to test things locally, the `set -eou pipefile` "persists" so that any command with non zero exit status results in exiting the container.

Would it be possible to add `set +e` at the end of `env.sh` ? Or will it cause problems elsewhere ?

## Comment (novicecpp, 2024-07-03T13:19:18Z)

> Would it be possible to add `set +e` at the end of `env.sh` ? 

Yes. 
You can put a whole `set +eou pipefile` to avoid annoying unbound variable errors and the pipe failing too.

## Comment (belforte, 2024-07-03T14:49:25Z)

I tried various things but while "exit on failed command" is gone at first approximation, if I run `source env.sh -g` again it fails to detect the mode, complains, and exit the bash shell. Maybe the consequence of the `set -auo pipefail` in the container itself. I leave it to you

## Comment (novicecpp, 2024-07-03T14:51:46Z)

Sure, I will have a look tomorrow.

## Comment (belforte, 2024-07-03T14:53:46Z)

not urgent
