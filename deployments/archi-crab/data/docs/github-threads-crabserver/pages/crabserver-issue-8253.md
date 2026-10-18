# dmwm/CRABServer issue #8253: PyPI: Bring back ./start.sh -g -d

State: closed
Opened: 2024-02-19T16:48:08Z
Closed: 2024-03-11T12:47:52Z
Labels: Priority: High, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8253

## Opening post (novicecpp, 2024-02-19T16:48:08Z)

I have dropped `./start.sh -g -d` feature to rewrote the startup scripts. Now, it is time to bring them back.

The goals are:
- `./start.sh -g` should run code from Github in `/data/repos/{WMCore,CRABServer}`.
- Plus, for Taskworker, run update runtime **everytime** when executing `./start.sh -g` to rebuild the data files (TaskManagerRun.tar.gz) from GH repos.
- `/start.sh -g -d` should work.

I will open the PR and explain the idea here.

## Comment (novicecpp, 2024-02-20T09:37:06Z)

In the [#8254](https://github.com/dmwm/CRABServer/pull/8254), there are 2 things, "How we run the app?" and "How we build the image?"

Let talk about on "How we run the app?" first.

---------------------

**How we run the app?**

From the first bullet in the goals above, user (us) is already in docker at `WORKDIR` path (`/data` from crabrest image and `/data/srv/TaskManager` for crabtaskworker image). The user wants to run code from the feature branch in CRABServer's private repo. What he/she does is:
- Checkout feature branch in `/data/repos/CRABServer`
    - `pushd /data/repos/CRABServer`
    - `git fetch <remote name>`, hardcoded in [CMSKubernetes/addGH.sh](https://github.com/dmwm/CMSKubernetes/blob/a6612ad45ea6ca79915e71e343cc29a97418973a/docker/crabserver/addGH.sh).
    - `git checkout -t <remote name> feature_branch`
    - `popd`
- Run `./start.sh -g -d` (fromGH mode, interactive).

My proposal is, make startup scripts into 2 files, `./start.sh` and `./manage`. 

`./start.sh` resposible for:
- Entrypoint for user to execute command. 
- Dealing with args (`-g`,`-d`).
- Setting 2 variables, `$DEBUG` mode and `$APP_PATH` point to python code. Both will passing to `./manage` later.
- (TaskWorker image) trigger buiding and deploy the data files.

`./manage` resposible for:
- Setup debug environment if `$DEBUG` is `true`.
- Export `PYTHONPATH` from `${APP_PATH}`
- Start+Stop CRAB process.

Each docker images has it own script but follow similar convention described above.

-------------------------

**How we build the image?**

Everything is nearly the same, except build data files in TaskWorker. There are 3 files changes:

*1. [build\_data\_files.sh](https://github.com/dmwm/CRABServer/blob/38bf04c1b709c5d9bd13b7f5a62e1e3e5f1273e2/cicd/crabtaskworker_pypi/build_data_files.sh)*

This is a new file where I encapsulate the bulding step from [crabtaskworker/Dockerfile#L23-L27](https://github.com/dmwm/CRABServer/blob/3af9d658271a101db02194f48c5cecaf5fab7725/cicd/crabtaskworker_pypi/Dockerfile#L23-L27) and add extra instructions to make the script able to test locally.
- Script get the path of CRABServer and WMCore repos from `$CRABSERVERDIR` and `$WMCOREDIR`.
    - We develop code in our local machine, we already have code from both repos somewhere, just point to it. No need to push/pull/clone again.
    - In CI, CI need to prepare both repos before execute the script.
- Specify `$INSTALL_DIR` and `$RUNTIME_DIR` to put all generated files single place, prevent it mess with local repo and easy to clean it up later.
    - However, WMCore does not support `--prefix` option in `setup.py`, so the files generate from setup.py always go to `$GIT_ROOT_DIR/build` directory. Fortunately when we run setup.py again it will clean up for us.
    - `$INSTALL_DIR` is "working directory" for this script.
    - `$RUNTIME_DIR` is the same but for `new_htcondor_make_runtime.sh`.


Script will run [new\_ht\_condor\_make\_runtime.sh](https://github.com/dmwm/CRABServer/blob/38bf04c1b709c5d9bd13b7f5a62e1e3e5f1273e2/cicd/crabtaskworker_pypi/new_htcondor_make_runtime.sh) to generate `TaskManagerRun.tar.gz` and `CMSRunAnalysis.tar.gz` (will explain later), follow by `setup.py install_system`. All needed files will be in `${INSTALL_DIR}/data`, ready to deploy.

Note that, default value for `$CRABSERVERDIR`, `$WMCOREDIR`, `$INSTALL_DIR`, and `$RUNTIME_DIR` is opinionated:
- `$INSTALL_DIR` and `$RUNTIME_DIR` is subdirectory of current directory (=working directory, =$GIT\_ROOT\_DIR).
- `$CRABSERVERDIR` and `$WMCOREDIR` is in the same directory.
    -  Unlike in CI, `$CRABSERVERDIR` is current directory, and `$WMCOREDIR` is subdirectory `./WMCore`. This is why I need to explicitly pass environment variable as seen in [Dockerfile](https://github.com/dmwm/CRABServer/blob/38bf04c1b709c5d9bd13b7f5a62e1e3e5f1273e2/cicd/crabtaskworker_pypi/Dockerfile#L25) 


*2. [new\_htcondor\_make\_runtime.sh](https://github.com/dmwm/CRABServer/blob/38bf04c1b709c5d9bd13b7f5a62e1e3e5f1273e2/cicd/crabtaskworker_pypi/new_htcondor_make_runtime.sh)*

Mostly modify to support to build files in `$RUNTIME_DIR`. The logic still the same, replace some path with absolute path and `popd/pushd` to correct directory.
Please see the changes in PR.


*3. [new\_updateTMRuntime.sh](https://github.com/dmwm/CRABServer/blob/38bf04c1b709c5d9bd13b7f5a62e1e3e5f1273e2/cicd/crabtaskworker_pypi/new_updateTMRuntime.sh)*

This script is rewrote entirely from scratch, but do the same thing as original [updateTMRuntime.sh](https://github.com/dmwm/CRABServer/blob/3af9d658271a101db02194f48c5cecaf5fab7725/src/script/Deployment/TaskWorker/updateTMRuntime.sh) do: 
- Build data files `./data` directory from GH to build directory. By running `./build_data_files.sh` to generate new data files to `/data/build/install_dir/data`.
- Do the backup by `/data/srv/current/lib/python/site-packages/data/` to `/data/srv/current/lib/Original_data_files.tar.gz`. 
- Copy `/data/build/install_dir/data` to `/data/srv/current/lib/python/site-packages/data/`, do clean up before delete.

All path is hardcoded in the script to follow the deployment convention of TW container.

One main idea I want to point out here is, to make the scripts able to run locally as much as possible. Even though the new scripts are simplified versions of the RPM image, they are still too complicate and time-consuming. Also, this will reduce feedback time from the build/copy-paste/deploy/test loop when running on a remote machine.

--------------------------

That is all. Let me know if you have any questions.

## Comment (belforte, 2024-02-20T10:11:56Z)

thanks for very clear description. I **really** like this.
We can dwell on details later, only one suggestion now: I do not like `new-htciondor...` name, let's call it `build_TW_tarballs.sh` or something like that.
