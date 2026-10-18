# dmwm/CRABServer issue #7552: Question: how should we handle missing keys in tm_user_config?

State: closed
Opened: 2023-02-24T17:02:45Z
Closed: 2024-08-23T15:28:07Z
Labels: Type: Question, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7552

## Opening post (novicecpp, 2023-02-24T17:02:45Z)

Moved from discussion in https://github.com/dmwm/CRABServer/pull/7547.

The current code (which I wrote myself) handles the keys as we do to column from db, meaning keys are always available for the client (TW/PUB) to use.
We define all possible keys in [RESTUserWorkflow](https://github.com/dmwm/CRABServer/blob/27fe22629968c70171c1a44976a6538cf702f823/src/python/CRABInterface/RESTUserWorkflow.py#L564) when we receive user input.
The problem appears when we deploy both REST and TW. While we stop the old TW before deploying the new REST, some tasks are not processed. When we start a new TW, those tasks will get the error because the new key does not exist.
To prevent this, we patch the unavailable keys in [RESTWorkerWorkflow](https://github.com/dmwm/CRABServer/blob/27fe22629968c70171c1a44976a6538cf702f823/src/python/CRABInterface/RESTWorkerWorkflow.py#L157).

The pain point is that I need to add new keys in 2 files. I add it into `RESTUserWorkflow` but usually forget to add it in `RESTWorkerWorkflow`.
From the latest production deployment, we failed 9 tasks because of this.

Main question here is: how can we improve this? 

Is it possible to define new keys only in `RESTUserWorkflow` and let `RESTWorkerWorkflow` reuse it?
Should we treat the keys as optional and handle the key missing in TW, as Stefano commented in https://github.com/dmwm/CRABServer/pull/7547#issuecomment-1441398505 ?
Or adjust how we deploy? let the old TW run and wait until all old tasks get processed, then deploy the new one.

## Comment (belforte, 2023-02-24T17:34:08Z)

I suspect that there are 2 different issues here.

1) there are two places: where we write (RESTUserWorkflow) and where we read (RESTWorkerWorkflow) [1]. So it make sense that if we ensure that we set a default for all things when we write, it is enough. And indeed your original code works well !
2) whenever we change REST or TW or both we have to worry about backward compatibility with the services data stored by previous versions in the DB and with clients of old service which may need updating. I am not sure that we can find a general solution here. Of course we always struggle to make backward-compatible development, but at times that's not enough. I am open to ideas of course. "Be careful" is easy to say, but it is not a guarantee.

[1] let's not go into naming nor why both do some read and write, but the flow for config. params is that one.

## Comment (belforte, 2023-02-24T23:03:34Z)

put a comment in RESTUserWorkfow to remind us to change RESTWorkerWorkflow as well ?

## Comment (belforte, 2024-08-23T15:28:07Z)

something one can discuss for years. Better address case by case
