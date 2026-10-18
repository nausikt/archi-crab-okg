# dmwm/CRABServer issue #7521: make crabserver UI work also in dbg mode

State: closed
Opened: 2023-02-02T23:41:36Z
Closed: 2023-03-18T14:40:08Z
Labels: Type: Enhancement, Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7521

## Opening post (belforte, 2023-02-02T23:41:36Z)

need these 3 symlinks in the container since there REST runs with root `/data/repos` when running in debug mode

```
ln -s /data/repos/CRABServer/src/html /data/repos/data/html
ln -s /data/repos/CRABServer/src/script /data/repos/data/script
ln -s /data/repos/CRABServer/src/css /data/repos/data/css 
```

## Comment (belforte, 2023-02-02T23:50:44Z)

should do via a change in https://github.com/dmwm/CMSKubernetes/blob/master/docker/crabserver/addGH.sh

## Comment (belforte, 2023-02-03T13:09:07Z)

will be done via https://github.com/dmwm/CMSKubernetes/pull/1311

Let's wait until that's merged and tested before closing

## Comment (belforte, 2023-03-18T14:40:08Z)

working nicely
