# dmwm/CRABServer issue #7560: Migrate CRAB to PYPI ecosystem

State: closed
Opened: 2023-03-02T17:17:55Z
Closed: 2024-10-31T16:17:46Z
Labels: Priority: High, PyPI
URL: https://github.com/dmwm/CRABServer/issues/7560

## Opening post (novicecpp, 2023-03-02T17:17:55Z)

In short, WMCore already moved to PYPI on production, and we are happy to move too.
But we need to discuss with WMCore developer on how much effort is needed and whether they can give documentation and some support.

-------------

Below are info moved from meeting minutes:
- Wa: Quick update about migrate to PYPI in WMCore (source: Aroosha) It's a good idea to move but we need to figure out how much effort is needed. We need to do it at some point when wmcore does not support building with rpm anymore.
- They already deployed on production.
- https://github.com/dmwm/CMSKubernetes/tree/master/docker/pypi
- It is so simple that I can reuse the base image from [docker/pypi/dmwm-base](https://github.com/dmwm/CMSKubernetes/tree/master/docker/pypi/dmwm-base) to run [notebooks/DatasetsOnDisk.ipynb](https://github.com/belforte/utils/blob/master/notebooks/DatasetsOnDisk.ipynb).
  - Notebook requires dbs and rucio python client which I never manage to install in my own machine.
  - Install jupyterlab in single command! See example [Dockerfile](https://gitlab.cern.ch/tseethon/crab_docker/-/blob/master/crabutils/Dockerfile)
  - I did not try WMCore though
- How do I search for other dependencies we need besides WMCore?
  - CRAB rpm’s spec files
  - Do we need myproxy/gfal2/voms-proxy-* inside the container?
- Well, there is still a lot of work to convert the CRABServer package from RPM to PYPI.
- How to steal from WMCore: 
  - look at this github project https://github.com/dmwm/WMCore/projects/8 
  - and this label: https://github.com/dmwm/WMCore/labels/containerization
- We are happy to move from rpm to PYPI. We must ask WMCore developers whether they can give documentation and some support. For sure we do not want to be the only CMSWEB app. which needs rpm’s . None of us has time to dig into details now, we open a GH issue and come back to this in one month or more. Need to appoint one of the group

## Comment (novicecpp, 2023-12-04T23:41:22Z)

I am ready to open POC PR.

Design choice of the POC in summary:
- Directory
    - crabrest: cicd/crabserver_pypi/
    - taskworker: cicd/crabtaskworker_pypi/
- Each image has it own `requierments.txt`,
    - wmcore deps [requirements.txt](https://github.com/dmwm/WMCore/blob/1459b0fa6d78aec48693cff736c746a658321e7d/requirements.txt#L23C1-L23C58)
    - For crabrest, it is slim down version of WMCore
- Install WMCore with `pip install --no-deps WMCore` and install dependencies manually.
    - Official is including `gfal2-python` but they actually install it separately when [build docker image](https://github.com/dmwm/CMSKubernetes/blob/bff12695b0eadf10177a917af1ed1b46172131cb/docker/pypi/reqmgr2ms-unmerged/Dockerfile#L14-L16).
    - Also, to slim down crab rest image.
- User inside container is crab3 (id 1000)
    - I do not like the way WMCore get services name from user name in the wrapper script [(manage)](https://github.com/dmwm/CMSKubernetes/blob/bff12695b0eadf10177a917af1ed1b46172131cb/docker/pypi/dmwm-base/manage#L19C23-L19C23).
- WMCore version's source of truth is in [cicd/crabserver_pypi/wmcore_requirements.txt](https://github.com/dmwm/CRABServer/blob/ed0faed5534536c68430a16d1db8a73ec88255b8/cicd/crabserver_pypi/wmcore_requirements.txt) where I use the same format as pip.
    - `requirementsParse.py` helper script to print git repo and version separate by space for load as array in bash
- Start the container (make it run forever) with `/data/run.sh`.
    - Start services with `/data/manage` for crabrest and `/data/start.sh` for taskworker.
    - In crabrest, move all cert/secret/config setup to [entrypoint.sh](https://github.com/dmwm/CRABServer/blob/e1694450edb901b18e97259aa7f4087233bcfca4/cicd/crabserver_pypi/entrypoint.sh) and set CMD (args of ENTRYPOINT)  to `/data/run.sh`.
- Need custom script for deploy services
    - crabrest: [custom helm chart](https://github.com/novicecpp/CMSKubernetes/commit/4c21b69287456d0be29e61b8d5bf6a644fe6bcd0)
    - taskworker: [runContainer.py](https://github.com/novicecpp/CRABServer/blob/4004c186a2f9561e8403b36126715507b76a43df/cicd/crabtaskworker_pypi/runContainer.sh.patch)
- `python-ldap` is broken with new wmagent pypi image. See comment in [CMSGroupMapper.py](https://github.com/novicecpp/CRABServer/blob/4004c186a2f9561e8403b36126715507b76a43df/src/python/CMSGroupMapper.py#L27-L29).
- Use [tini](https://github.com/krallin/tini) wrapper as PID 1 mainly to make container stop faster.
    -  https://github.com/krallin/tini/blob/master/README.md#why-tini
- Rebuild should idempotent, you can build as much as you want, but still
    - OS package will update to latest version of packages maintained by OS distribution.
    - Pip dependencies only pin to minor version of requirements.txt, not pin to the hash like Pipfile.lock/Poetry.lock (yet).
- Still lack ability to run from GH.
- Never test Publisher.

## Comment (novicecpp, 2023-12-05T00:25:58Z)

Next tasks:
- [ ] Build crab packages and install with `pip install`.
    - Take advantage of `pip` to clean install new version of crabserver packages, even build it manually in from local/GH dir inside container.
    - Build data files (css/js/html in crabrest, TaskManagerRun.tar.gz in crab).

    I need to do another POC to prove if `pip` can do above, but I still do not know how to do it though.

- [ ] Add ability to run from GH back.
    Sometime I want a quick test in the server but current POC version does not support run from GH.
    I need to revert everything back and deploy RPM images which take a lot of steps and time.

## Comment (novicecpp, 2023-12-18T04:27:09Z)

Lets me explain the poc of PyPI https://github.com/dmwm/CRABServer/pull/8088 here.
First of all, forget the design choice https://github.com/dmwm/CRABServer/issues/7560#issue-1607196899 for now. I will come back to it later.

The goal is **"Remove RPM build"**. 

Because we remove the RPM "building system", we need to come up with our own replacement. What I actually do is convert [crabtaskworker.spec](https://github.com/cms-sw/cmsdist/blob/comp_gcc630/crabtaskworker.spec) to our own building system, which is based on [the PyPI containers from WMCore](https://github.com/dmwm/CMSKubernetes/tree/master/docker/pypi). 
Note that I did not touch the Python packaging, which is worth tracking in a separate issue, but the image building will involve the CI to some extent.

Things I keep in mind while developing this:

1. The less code change in `src/python`, the better.
1. No clone CRABServer, use local file.
    This will simplify how we run on local machine and also in CI.
     If there is a change, the builder will always pick from local files. No need to commit and push.
And for the CI, in the gitlab-ci model, CI jobs always run on the commit. No need to pass repo/branch/commit to the CI. Just push, and then CI will run.
1. If we want some files on the internet, commit the endpoint in this repo.
     For example, the WMCore version I want to install is in [cicd/crabserver_pypi/wmcore_requirements.txt](https://github.com/dmwm/CRABServer/pull/8088/files#diff-5f6c3363105e2c25d0bf95fa7becf90b238f1197ce5e5e823d56e8c5c617a893). Any format is fine as long as you commit it and CI can pick it up.
1. It should be able to run in your local machine.

So here is what I came up with:

1. **Building**
    Simply run single `docker build` command from repo's root directory:
    ```bash
    # go to git root directory
    cd $(git rev-parse --show-toplevel) 
    # build crabserver
    docker build -t registry.cern.ch/cmscrab/crabserver:manual . -f cicd/crabserver_pypi/Dockerfile
    # build taskworker
    docker build -t registry.cern.ch/cmscrab/crabtaskworker:manual . -f cicd/crabtaskworker_pypi/Dockerfile
    ```

2. **Running**
    Because of Dockerfile in both image are a bit long, I will show how I run the container first, hope it will help you understand Dockerfile better.
    
    - **TaskWorker:** `ENTRYPOINT` is `tini` wrapper (please see explanation in the design choice), and `CMD` is executing [crabtaskworker_pypi/run.sh](https://github.com/dmwm/CRABServer/blob/f66997e6f40cc702b4c1bf05980a9ae62249ea17/cicd/crabtaskworker_pypi/run.sh). `run.sh` call [crabtaskworker_pypi/start.sh](https://github.com/dmwm/CRABServer/blob/f66997e6f40cc702b4c1bf05980a9ae62249ea17/cicd/crabtaskworker_pypi/start.sh) which spawn TaskWorker process in background, then run sleep forever.
    - **CRABServer:** CRABServer is a bit complicated because it needs to be integrated with the K8S manifest. There is a setup step created by CMSWEB operators. I adapt it and put it together in [crabserver_pypi/entrypoint.sh](https://github.com/dmwm/CRABServer/blob/f66997e6f40cc702b4c1bf05980a9ae62249ea17/cicd/crabserver_pypi/entrypoint.sh) and make this script as `ENTRYPOINT`. Basically, container start to run `entrypoint.sh` script until [line 53,](https://github.com/dmwm/CRABServer/blob/f66997e6f40cc702b4c1bf05980a9ae62249ea17/cicd/crabserver_pypi/entrypoint.sh#L53) then exec the [crabserver_pypi/run.sh](https://github.com/dmwm/CRABServer/blob/f66997e6f40cc702b4c1bf05980a9ae62249ea17/cicd/crabserver_pypi/run.sh) which will spawn the crabserver process and run cat on the fifo log forever.    

3. **Dockerfile**
    Dockerfile should be a self-explanatory step, a.k.a., how do I build the container. Please see ["Design Choice"](https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1839733761) for the sort of question "Why is it doing this and that?". And please let me know if I did not make it clear enough for you to understand.

## Comment (novicecpp, 2023-12-18T04:46:41Z)

There are some changes on how I install WMCore code, in order to support forked version. I will update the PR later.

## Comment (novicecpp, 2024-01-30T13:43:27Z)

Here is the guide on how do I build and run CRAB REST image.
(Bear with me, it is a bit long. CRAB TaskWorker images will be in another reply).

To build it, simply run:

```
docker build -t registry.cern.ch/cmscrab/crabserver:manual . -f cicd/crabserver_pypi/Dockerfile
```

Where working directory is `path/to/crabserver/repository`.

The [Dockerfile](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile) is straightforward:
- [Line 16](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L16): Install `tini` from `apt`. `tini` will send SIGTERM to all children processes and make container stop faster.
- [Line 19](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L19): Copy `tnsnames.ora` from CMSWEB image.
- [Line 28-30](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L28): install service dependencies and wmcore via pip.
- [Line 32-35](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L32-L35): install CRAB code by copy file from local to `/data/srv/current/lib/python3.8/site-packages` and install html/css/js to `/data/srv/current/data`.
- [Line 42-46](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L42-L46): install mandatory directory that need.
- [Line 49](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L49) copy service starting scripts to `/data/`

Then we execute `wmc-httpd` to start REST service.
Note that I simply copy code from source to `/data/srv/current/lib/python3.8/site-packages` and export `PYTHONPATH` to this directory in [manage](https://github.com/novicecpp/CRABServer/blob/5dd0a31c9545e5e16a395aba0b1b955f1bf37b23/cicd/crabserver_pypi/manage#L41). This will change to PyPI packaging and install via `pip` in the future.

-----------

There is a "deployment convention" for WMCore/REST services that specifies how services read/write files (logs/credential/state/config/etc.).
This will explains why we need this [Dockerfile lines 42-46](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L43-47) and also has an effect on how we deploy in the Kubernetes environment, which I will explain in a later section.


There are 4 directories where the service read or write files.

1. `LOGDIR=/data/srv/logs/crabserver`
This is where services write log to. In version 2022 and earlier, this directory is [mount to CephFS](https://github.com/dmwm/CMSKubernetes/blob/5446006c73d5dfb7123fbee318264134cb611b1c/kubernetes/cmsweb/services/crabserver.yaml#L195-L196).
But after we switch to writing log to stdout we did not use it anymore.

2. `AUTHDIR=/data/srv/current/auth/crabserver`
This is where we store `CRABServerAuth.py`, robotcert/hmac/proxy(?) that setup by CMSWEB.
Services read this file via [exporting PYTHONPATH](https://github.com/dmwm/deployment/blob/94cdfb184264bf11139f417f30565a1881a8e209/crabserver/manage#L37) and [run.sh](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/crabserver/run.sh#L60) script preventing copy `config.py` to this directory.

3. `STATEDIR=/data/srv/state/crabserver`
This is where services write temporary file into (`-d` arg of `wmc-httpd` in [manage#L51](https://github.com/dmwm/deployment/blob/94cdfb184264bf11139f417f30565a1881a8e209/crabserver/manage#L54))
We also store fifo file `crabserver-fifo` to let service write logs to.

4. `CFGDIR=/data/srv/current/config/crabserver`
This is where `config.py` is stored. Service only `config.py` via positional argument of `wmc-httpd`.

**In the new PyPI image, the convention and path are still the same.**
But, replace the old [manage](https://github.com/dmwm/deployment/blob/94cdfb184264bf11139f417f30565a1881a8e209/crabserver/manage) script to new [manage](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/manage) where the new one is based on the new [manage in dmwm-base image](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/pypi/dmwm-base/manage).

------------

The next part is how we deploy this CRAB REST on CMSWEB Kuberenetes cluster.

Currently:
- We store all config/creds/secrets as Kubernetes Secrets and mount it as volumes, see [crabserver.yaml#L262-L283](https://github.com/dmwm/CMSKubernetes/blob/5446006c73d5dfb7123fbee318264134cb611b1c/kubernetes/cmsweb/services/crabserver.yaml#L262-L283).
- We [inject](https://github.com/dmwm/CMSKubernetes/blob/3019f11449c31d7092a4b1351db23bbc3d808a6b/kubernetes/cmsweb/services/crabserver.yaml#L99-L101) the [setup-certs-and-run.sh](https://github.com/dmwm/CMSKubernetes/blob/3019f11449c31d7092a4b1351db23bbc3d808a6b/kubernetes/cmsweb/services/crabserver.yaml#L23C3-L30) then execute [run.sh](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/crabserver/run.sh).
- The upper part of [run.sh](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/crabserver/run.sh#L1-L65) copy files from secrets's mounting path to the "WMCore/REST deployment convention" I explained above.
- Then execute [manage](https://github.com/dmwm/deployment/blob/94cdfb184264bf11139f417f30565a1881a8e209/crabserver/manage#L37) to start service.
- Finally, loop over `cat crabserver-fifo` to read log to container stdout.

**The new PyPI still use same way but replace upper part of old [run.sh](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/crabserver/run.sh#L1-L65) with new [entrypoint.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/entrypoint.sh)**.
Then setup Kubernetes manifest file in container specs section will look like this:
```yaml
containers:
  - image: registry.cern.ch/crab/crabserver:pypi-2ea9d1429ebe56c527b53f17b4adb4503a4f095f
    name: crabserver
    command:
      - /data/entrypoint.sh
    args:
      - /data/run.sh
    ...
```

New process execution flow will be:
- Execute [entrypoint.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/entrypoint.sh) to copy the files from secret mounts.
- Then run the new [run.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/run.sh) (with `tini` wrapper)
    - [run.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/run.sh) start service process by execute new [manage](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/manage).
        - [manage](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/manage) setup necessary environment variables for service process and then execute `wmc-httpd` and exit.
    - Then, run infinit loop `cat crabserver-fifo`, as main process to make container run forever.

--------------

Finally, the dependencies.

I use [wmagent-base](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/pypi/wmagent-base/Dockerfile), which based on [dmwm-base](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/pypi/dmwm-base/Dockerfile), as baseimage of CRAB REST. This image provides:
- Oracle library.
- libcurl
- cmsweb binary (cmsweb-ping/cpy_exporter)

For python dependencies install via pip in [requirements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/requirements.txt), I strip it from [WMCore requirements.txt](https://github.com/dmwm/WMCore/blob/master/requirements.txt), by do trial-and-error adding package to our `requirements.txt` until no more dependency error.

WMCore version is specified in [wmcore_requirements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/wmcore_requirements.txt). It will read by [requirementsParse.py](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/requirementsParse.py) which print space-separate repository and version (tag). The current POC only [get version number and pass it to pip](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile#L28-L29), cannot replace with src in custom repository yet.

--------------

I explicitly not pass any argument to `docker build` but commit it as files (e.g. [wmcore\_requiements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/wmcore_requirements.txt)). This way CI can notify changes and build the new image automatically.
And `./start.sh -g` or equivalent feature is not available at the moment.

## Comment (novicecpp, 2024-02-02T10:22:11Z)

Now it is the time for the guide of CRAB TaskWorker image.

To build it, same as CRAB REST, simply run:

```
docker build -t registry.cern.ch/cmscrab/crabtaskworker:manual . -f cicd/crabtaskworker_pypi/Dockerfile
```
Where working directory is `path/to/crabserver/repository`.

But this time the [Dockerfile](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile) is a bit long and has many dependencies.
Let jump to [line 42](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L42) where main image start. It actually quite straightforward:
- [Line 49-53](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L49-L53): install gfal commandline by copy files from `wmcore-gfal` layer from [line 30-37](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L30-L37). (See *gfal-\** section below)
- [Line 57-59](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L57-L59): install `tini` and `python-ldap` dependenceis, and copy CERN LDAP config from [cern-cc7](https://linux.web.cern.ch/dockerimages/#cerns-dockerhub-page) layer on [Line 80](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L80). (See *python-ldap* section below)
- [Line 67-71](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L67-L71): install dependencies in [requirements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/requirements.txt) and wmcore with pip. (See *Dependencies* section below)
- [Line 75-77](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L75-L77): install CRAB code by copy files from local to `/data/srv/current/lib/python3.8/site-packages`, copy `TaskManagerRun.tar.gz` and other data files from [build-data](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L1-L26) layer to `/data/srv/current/lib/python3.8/site-packages/data`.  There is section dedicate to explain "how do we create `TaskManagerRun.tar.gz`" in *TaskWorker data files* below.
- [Line 83-84](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L83-L84): copy default rucio .cfg to container. This can be bind mount from cvmfs when we run the container.
- [Line 95-103](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L95-L103): create directory and copy running scripts, follow deployment convention of crabtaskworker RPM image.

----------

**gfal-***

In new PyPI image, WMCore build gfal docker on separate [Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/3019f11449c31d7092a4b1351db23bbc3d808a6b/docker/pypi/gfal/Dockerfile) using miniconda. When install in [reqmgr2ms-unmerged](https://github.com/dmwm/CMSKubernetes/blob/3019f11449c31d7092a4b1351db23bbc3d808a6b/docker/pypi/reqmgr2ms-unmerged/Dockerfile#L4-L7), they simply copy whole miniconda directory from gfal image to this image and export PATH/PYTHONPATH to miniconda directory.

In our image we can do the same, however WMCore gfal does not come with [gfal2-util](https://gitlab.cern.ch/dmc/gfal2-util/) which provides cli `gfal-copy`, `gfal-ls`, etc. In [Dockerfile line 29-36](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L29-L36), I simply clone gfal2-util and run `python setup.py install`, then in the main image (at [lines 49-53](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L49-L53)), I copy miniconda directory and symlink to `/usr/bin/` path without export `PYTHONPATH`, and it works out of the box (I do not understand yet why).

There is [gfal2-util](https://anaconda.org/conda-forge/gfal2-util) in conda-forge, I will have a look later.

----------

**python-ldap**

CRAB has feature that users in [cms-crab-HighPrioUsers](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/8662f95b6f41374234b753f7e8349e90fa4bf4a8/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L121) egroup submit the jobs to `highprio` of `accounting_group` which have higher priority than usual `analysis` group. CRAB query the egroup members through CERN LDAP in [CMSGroupMapper](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/python/CMSGroupMapper.py#L20) using [python-ldap](https://github.com/cms-sw/cmsdist/blob/0911f19f5215d68a7aa891952043e43119180ce8/crabtaskworker.spec#L19) python library.

To install `python-ldap` via pip, `libsasl2-dev python3-dev libldap-dev libssl-dev` from debian 11 repository (OS of `wmagent-base`) is required. 
However, libldap 2.4 that come with debian 11 is built with `gnutls` which does not support `cacertdir` option. So code changes in [CMSGroupMapper](https://github.com/dmwm/CRABServer/pull/8088/files#diff-47bafb67a94ef6bcd5168e4b28977f556d12107d24d63422d5a8caebc5fb32fe) is needed. Fortunately, python>3.9 docker images come with Debian 12 and libldap is compiled with openssl that support `caccertdir` (need to be confirmed, but that what I remembered the last time I tried to debug LDAP error).

For LDAP client config, we can fetch directly from [/etc/openldap](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L77) of [cc7-base](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L40) image provided by CERN IT.


Note that I am not sure if this feature is still in-use (our code still support though).

----------

**Dependencies**

I use [wmagent-base](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/pypi/wmagent-base/Dockerfile), which based on [dmwm-base](https://github.com/dmwm/CMSKubernetes/blob/2b0454f9205cb8f97fecb91bf6661b59e4b31424/docker/pypi/dmwm-base/Dockerfile), as baseimage of CRAB REST. This image provides:
- libcurl
- myproxy-* (required by [WMCore.Credential.Proxy](https://github.com/dmwm/WMCore/blob/1e059313b9e465e08c307047d3ad64c2707f548d/src/python/WMCore/Credential/Proxy.py#L634))

(if I understand correctly, we did not need `voms-proxy-*` but it is included in `wmagent-base` anyway)

For python dependencies install via pip in [requirements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/requirements.txt), I am kinda lazy. I clone WMCore [requirements.txt](https://github.com/dmwm/WMCore/blob/2.2.4rc6/requirements.txt), remove `gfal2-python` and add `python-ldap`, install with `pip`, and...it works.

---------

**TaskWorker data files.**

The most complicate part of our TaskWorker deployment is how we build data files. The data files contains `TaskManagerRun.tar.gz`, `CMSRunAnalysis.tar.gz`, and other scripts which use for submit jobs to the condor.

According to [crabtaskworker.spec](https://github.com/cms-sw/cmsdist/blob/0911f19f5215d68a7aa891952043e43119180ce8/crabtaskworker.spec) (and assume `%i` is `./install_dir` directory):
- `cd WMCore` repo directory and run `python setup.py build_system -s crabtaskworker --skip-docs`
- `cd CRABServer` repo directory and run `python setup.py build_system -s TaskWorker --skip-docs=d`
- at `CRABServer` repo directory, run `RPM_RELEASE=1 ./bin/htcondor_make_runtime.sh` ([htcondor_make_runtime.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/bin/htcondor_make_runtime.sh))
    - this step generate `TaskManagerRun.tar.gz` and `CMSRunAnalysis.tar.gz`.
- at `CRABServer`, run `setup.py install_system -s TaskWorker  --prefix=./install_dir` (*install_system instead build_system*)
    - This step will copy some scripts (e.g. `submit_env.sh`) to `./install_dir` directory.


For the new PYPI image, **those steps are still the same** but get simplify by remove RPM-relate line and ignore [updateTMRuntime.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/script/Deployment/TaskWorker/updateTMRuntime.sh) feature (for now), describe in [Dockerfile line 1-26](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L1-L26):
- [wmcore-src](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L2-L9) layer, clone WMCore code needed to build data files.
    - Read repo and version from [cicd/crabserver\_pypi/wmcore\_requirements.txt](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/wmcore_requirements.txt).
- In [build-data](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L12-L27) layer, run [new\_htcondor\_make\_runtime.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/new_htcondor_make_runtime.sh) to generate `CMSRunAnalysis.tar.gz` and `TaskManagerRun.tar.gz`
    - It is simplify version of [htcondor\_make\_runtime.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/bin/htcondor_make_runtime.sh), plus run `python setup.py build_system` inside the new scripts (only this script use content from `build_system`).
- Then run `python setup.py install_system` at [line 24](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L24) to have other scripts and then copy `CMSRunAnalysis.tar.gz/TaskManagerRun.tar.gz` to `/build/install_dir/data`
- At this point, we got all data files we need in `/build/install_dir/data` directory, [ready to copy to main layer](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L77).

This [new\_htcondor\_make\_runtime.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/new_htcondor_make_runtime.sh) still need to rework. For example, define every steps in `setup.py` and run single command `python setup.py install_system` that create `/data` directory ready to use.

Note for inconsistency with [crabserver_pypi/Dockerfile](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabserver_pypi/Dockerfile) which copy data files to `/data/srv/current/data`. According to [setuptools docs](https://setuptools.pypa.io/en/latest/userguide/datafiles.html#data-files-support), they suggested to put data files in package directory, which should be like `/data/srv/current/lib/python3.8/site-packages/CRABServer/data`. I will fix it later.

----------

To start TW process, I have new [start.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/script/Deployment/TaskWorker/start.sh) in-place of old [start.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/script/Deployment/TaskWorker/start.sh). It setup necessary environment variables then execute [MaterWorker.py](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/start.sh#L9)

Process execution flow is simple:
- Starting container with modified [runContainer.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/runContainer.sh.patch) which similar to command `docker run registry.cern.ch/cmscrab/crabtaskworker:manual /data/srv/TaskManager/run.sh`.
- [tini](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/Dockerfile#L120) is the ENTRYPOINT and CMD is [run.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/run.sh), equivalent to `tini /data/srv/TaskManager/run.sh`, basically start run.sh as non-PID1.
    - [run.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/cicd/crabtaskworker_pypi/run.sh) run [start.sh](https://github.com/novicecpp/CRABServer/blob/pypi_poc/cicd/crabtaskworker_pypi/start.sh) and loop sleep forever.
        - In [start.sh](https://github.com/novicecpp/CRABServer/blob/pypi_poc/cicd/crabtaskworker_pypi/start.sh), `CRABTASKWORKER_ROOT` is mandatory variable for [DagmanCreator.py](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/python/TaskWorker/Actions/DagmanCreator.py#L344) to get data files location. In [RPM image](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/script/Deployment/TaskWorker/start.sh#L56-L57) it is defined in Shahzad `env.sh` script.
        
        
------------

The `./start.sh -g` and [env.sh](https://github.com/novicecpp/CRABServer/blob/79a8ab854b221926b3f32bf2e8058fd5f0d1efd7/src/script/Deployment/TaskWorker/env.sh) still not yet available. Also running Publisher process still not support.

## Comment (belforte, 2024-02-02T10:36:36Z)

about LDAP, we still need to support it even if it was/is only used in case of "emergency". I never liked this dependency anyhow. Maybe there is some other way to get the list of members of that e-group ? Maybe we can add that egroup to CRIC, let it do the ldap magic, and fetch the list from CRIC with a simple `curl` ?

## Comment (novicecpp, 2024-02-02T10:50:21Z)

> Maybe we can add that egroup to CRIC, let it do the ldap magic, and fetch the list from CRIC with a simple curl ?

Thanks Stefano. That is interesting, never thought about it.
I am adding it to next to-do list.

## Comment (novicecpp, 2024-02-02T13:41:07Z)

Thanks to Stefano and @Panos512, now we can list users in `cms-crab-HighPrioUsers` through CRIC.
We can easily extend CRIC class from WMCore by add new method similar to [_CRICUserQuery()](https://github.com/dmwm/WMCore/blob/1e059313b9e465e08c307047d3ad64c2707f548d/src/python/WMCore/Services/CRIC/CRIC.py#L73-L81).

## Comment (novicecpp, 2024-02-13T14:56:39Z)

One things I forgot to mention in CRAB REST image is, where WMCore/REST get those data files of CRAB UI?

The answer is this file, [FrontPage.py](https://github.com/novicecpp/CRABServer/blob/46ff962b1d6de17db7cca8cc08425ad602e26cf5/src/python/CRABInterface/Pages/FrontPage.py), the **absolute path of `./data/{html,script,css}`** is defined in this file.
The magic is come from [line 13](https://github.com/novicecpp/CRABServer/blob/46ff962b1d6de17db7cca8cc08425ad602e26cf5/src/python/CRABInterface/Pages/FrontPage.py#L13). For example, 
- The path of this file: `/data/srv/HG2401b-5ac8fb32fb299de758852f123c281791/sw.crab_master/slc7_amd64_gcc630/cms/crabserver/v3.240201-7d39eda58270523b4acf410cd7bca48b/lib/python3.8/site-packages/CRABInterface/Pages/FrontPage.py`
- Output of `rsplit('/',6)[0]` is `/data/srv/HG2401b-5ac8fb32fb299de758852f123c281791/sw.crab_master/slc7_amd64_gcc630/cms/crabserver/v3.240201-7d39eda58270523b4acf410cd7bca48b`
- Then use result above as prefix path of `./data/{html,script,css}` and then feed to `WMCore.REST.Server.RESTFrontPage ` class.

So, as long as you deploy `data` directory 2 level upper of PYTHONPATH (in this case same level as `lib` directory of `lib/python3.8/site-packages`), no matter the path of PYTHONPATH it is, it always works. 

That is why Stefano added [this hack](https://github.com/dmwm/CMSKubernetes/blob/a6612ad45ea6ca79915e71e343cc29a97418973a/docker/crabserver/addGH.sh#L43-L47) to addGH.sh to make web UI works in GH mode. I think new PYPI image will also use this hack and fix it later when we support install CRAB with `pip`.

## Comment (belforte, 2024-02-13T17:59:51Z)

abut the previous comment https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1941698865 it goes w/o saying that any idea about how to simplify is welcome. I can sort of understand the original implementor line of thought that there is a generic application in /data/srv/.../myApp and below that there's lib with the code and data with files including html, but we would surely prefer that location in the server and location in the GH tree are more closely related.

## Comment (novicecpp, 2024-02-14T08:19:25Z)

I want to move it into [data files](https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime) and refer the path from PYTHONPATH. Also, pip will handle update for us when we install updated version.

## Comment (novicecpp, 2024-04-30T00:30:39Z)

For the last part, the Publisher. 

It is simpler than I thought. No extra environment variables is needed. Startup scripts can copy-paste from TaskWorker (`start.sh/stop.sh/manage.sh` in [crabtaskworker_pypi](https://github.com/dmwm/CRABServer/tree/master/cicd/crabtaskworker_pypi)) then tailored to suit the Publisher's needs.

However, there are 2 major changes and 1 discovered bug I want to introduce (compare to the code in the [current master](https://github.com/dmwm/CRABServer/tree/c09182159e0397155da20c56e07d7859ce6d7029/)).

1. Share `run.sh` like RPM image.

I am reinvent the wheel here :sadge:
New `run.sh` is placed in `/data/run.sh` and the decision to execute which `start.sh` is depended on `$SERVICE` (e.g., `/data/srv/${SERVICE}/start.sh`, just like [RPM run.sh](https://github.com/dmwm/CRABServer/blob/c09182159e0397155da20c56e07d7859ce6d7029/Docker/run.sh)).
I tried to separate it once, but the similarity of the code is 80%. 

2. Symlink is done in the `run.sh` step. Not building a container step.

In current master, I have done this in the build step ([Dockerfile#L104-107](https://github.com/dmwm/CRABServer/blob/c09182159e0397155da20c56e07d7859ce6d7029/cicd/crabtaskworker_pypi/Dockerfile#L104-L107)), but then realized that there is an extra directory that needs to be symlinked for Publisher ([PublisherFiles](https://github.com/dmwm/CRABServer/blob/c09182159e0397155da20c56e07d7859ce6d7029/Docker/run.sh#L49)).

3. Bug(?) in the original `Publisher/stop.sh`: cannot start service if the time of the next cycle has passed.

This is what I discovered when I tried to run Publisher PyPI for the first time. The problem is the result of 2 combinations:

- For REST and TW services, the `./manage.sh start` is actually a restart action, for convenience, and it works very well.
- The [Publisher/stop.sh](https://github.com/dmwm/CRABServer/blob/c09182159e0397155da20c56e07d7859ce6d7029/src/script/Deployment/Publisher/stop.sh) does not support stop if the next cycle run is less than now. The result of [line 22](https://github.com/dmwm/CRABServer/blob/c09182159e0397155da20c56e07d7859ce6d7029/src/script/Deployment/Publisher/stop.sh#L22) will be minus and will fail condition `[ $delta -gt 60 ]` next line.

We can fix the condition, and everything will be fine. But I think the function is a bit fragile, and there should be a better way to do this. So, I am not fixing it. I separate `start` and `restart` command so `start` action only runs `start_srv` function instead. 

-------------

PR is coming soon.

## Comment (belforte, 2024-04-30T07:22:56Z)

I guess we never tried until now to stop a Publisher which had never ran !
Fine with the change, but you need to put some protection in the new `start` so that it fails if Publisher is already running or falls back to `restart`

With a bit a of day-after-wisdom, I wander if we have too many symlinks and should rather re-arrange the directory tree. All those directory names are configuration variables, should be easy to rename them.

## Comment (novicecpp, 2024-04-30T20:29:52Z)

> With a bit a of day-after-wisdom, I wander if we have too many symlinks and should rather re-arrange the directory tree. All those directory names are configuration variables, should be easy to rename them.

IMO, the symlink that we still need is the config file, where we can switch to other files on-the-fly without stopping puppet.
Other than that, it can be replaced by configuration+`docker run -v /host:/container` (need to modify `runContainer.sh`).

## Comment (novicecpp, 2024-04-30T22:08:47Z)

With https://github.com/dmwm/CRABServer/pull/8368/commits/c547da07104247eda74761db8e1261f285ed7da5, first line of `DOCKER_VOL` will expand to something like this:
```
+ DOCKER_VOL='-v /data/container/:/data/hostdisk/ -v /data/container/Publisher_schedd/cfg:/data/srv/Publisher/cfg -v /data/container/Publisher_schedd/logs:/data/srv/Publisher/logs -v /data/container/Publisher_schedd/PublisherFiles:/data/srv/Publisher/PublisherFiles -v /data/srv/tmp/:/data/srv/tmp/'
```

Then, switch the `config.General.taskFilesDir` to `/data/srv/Publisher/PublisherFiles` on [Publisher_scheddConfig.py#L35](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/c7d4596afd3cb9a8c03c2659b47224a3b800e081/code/templates/crabtaskworker/publisher/Publisher_scheddConfig.py.erb#L35).

## Comment (belforte, 2024-05-01T10:37:52Z)

thanks @novicecpp , given what you wrote in previous comment, which I fully agree with, I think that we do not need all of those mount either.
Shall we open an ad-hoc thread and review this ?

## Comment (belforte, 2024-05-06T21:26:22Z)

I guess we never tried until now to stop a Publisher which had never ran !
Fine with the change, but you need to put some protection in the new `start` so that it fails if Publisher is already running or falls back to `restart`

With a bit a of day-after-wisdom, I wander if we have too many symlinks and should rather re-arrange the directory tree. All those directory names are configuration variables, should be easy to rename them.

## Comment (novicecpp, 2024-05-29T09:12:44Z)

I encountered this problem today after stop Publisher for too long to make sure TW is up and running.
Let's create the new issue to tackle this.

## Comment (novicecpp, 2024-09-04T19:26:50Z)

I think the last part here is documentation. 

I remembered it is hard for Vijay to figure it out even we already have a new, simpler Dockerfile. 
It is not like we `pip install crabtaskworker` and done. There are specific paths in container that we use and specific way to run containers.

At least give a new guy a map where to look at.

## Comment (novicecpp, 2024-10-31T16:17:12Z)

Sorry. I do not have time to do this.

But at least everything is written down in the Dockerfile, [crabserver](https://github.com/dmwm/CRABServer/blob/19b1bf76091ffe6a275683be5adf716310714ff6/cicd/crabtaskworker_pypi/Dockerfile), [crabtaskworker](https://github.com/dmwm/CRABServer/blob/19b1bf76091ffe6a275683be5adf716310714ff6/cicd/crabtaskworker_pypi/Dockerfile). 

Closing the issue.
