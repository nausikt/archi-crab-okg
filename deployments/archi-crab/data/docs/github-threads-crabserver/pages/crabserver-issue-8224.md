# dmwm/CRABServer issue #8224: Plan for PyPI 

State: closed
Opened: 2024-02-02T14:46:22Z
Closed: 2024-09-04T19:19:53Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8224

## Opening post (novicecpp, 2024-02-02T14:46:22Z)

**Plan for PyPI**

**Goal: move POC to Production**
- [x] POC approval from team
- [x] CI for *automatically* test new pypi image.
    - The goal is, *when new code tagged, ci build and run status tracking against it, and report when test is finish.*
- [x] bring back `./start.sh -g` https://github.com/dmwm/CRABServer/issues/8253
- [x] Build from WMCore private repository.
- [x] Mark deployment version for release that will be on prod.
- [x] Update deployment.
    - [x] Make helm compatible with new pypi image, also move [entrypoint.sh](https://github.com/novicecpp/CRABServer/blob/5dd0a31c9545e5e16a395aba0b1b955f1bf37b23/cicd/crabserver_pypi/entrypoint.sh) from crab rest image to CMSKubernetes 
    - [x] Update runContainer.sh scripts to make it work with jenkins Deploy_TW.
~~- [ ] Replace python-ldap with CRIC~~ Move to https://github.com/dmwm/CRABServer/issues/8439
- ~~[ ] Move gfal miniconda to our Dockerfile and install gfal2-util~~ No need to do it for now.
- [x] Run the Publisher!!
- ~~-Rework TaskWorker data files, move everything to `setup.py`.~~ Next improvement. 
    - ~~[ ] This part will take a lot of time, at least 2 weeks. I still do not know how to do it.~~
    - ~~[ ] Also, deprecating `CRABTASKWORKER_ROOT` and put data files inside package.~~
- ~~[ ] (optional) packaging crab code ready to install via `pip`.~~ Too low priority.
- ~~[ ] (optional) build on alma9~~ Too low priority
----------------

**Plan for CI**

Move to [#8267](https://github.com/dmwm/CRABServer/issues/8267).

~~Sorry, I still cannot provide a clear path for what I will do with CI.~~

~~The high-level goals are to eliminate manual intervention, shorten feedback time, and make it easy to maintain.~~

~~I plan to switch from Jenkins to gitlab-ci which provides a declarative pipeline and makes it easy to write configurations, in exchange for extra maintenance.~~
~~I believe gitlab-ci has better practice and can do fast POC (and I am more familiar with it) compared to Jenkins. Even if the new CI does not get approved, I can apply those practices that "work" back into Jenkins.~~

~~I will start with the new PyPI CI from the *"Plan for Pypi"* above as a prototype.~~

~~After getting more experience, there is a long list of "CI wishlist" in https://github.com/dmwm/CRABServer/issues/7958 that needs to be done.~~

## Comment (belforte, 2024-02-05T07:41:10Z)

about TaskWorker data files, current situation is surely not satisfactory, there are duplications and possibly extra stuff which we should cleanup. I agree to take a bit of time to review and simplify. Maybe we can build the tarballs when the container start ? All in all he current `updateTMRuntime.sh` takes only a couple seconds to run. And surely `htcondor_make_runtime.sh` is heavily dependent on the specifics of the installation via rpm's and should be heavily simplified.

## Comment (novicecpp, 2024-03-15T13:40:16Z)

Today, Alan asked me about what we are relying on current DMWM Jenkins because they need to migrate OS that use by the tools in Jenkins away from CC7.

Main problem for us is RPM build, the [comp_gcc630](https://github.com/cms-sw/cmsdist/tree/comp_gcc630) will not work anymore because it is native to CC7 and need to be migrated.

This mean,
- The CI that build PyPI image
- The Publisher PyPI
- Production testing.

need to be ready before June this year.

Another service/job we rely on is pylint/pycodestyle, but this is just Python process and can be install easily via pip.

## Comment (belforte, 2024-03-15T13:46:02Z)

if disaster happens, we should be able to start a CC7 container in the new Jenkins node and run the build that. But hopefully migration to PyPI can be completed :-)

## Comment (novicecpp, 2024-08-01T15:00:42Z)

New PyPI images are now in production thanks to @aspiringmind-code and @mapellidario. 

Still need to do `Build from WMCore private repository.` before I can close this issue.
But put it on hold until https://github.com/dmwm/CRABServer/issues/8522 done (avoid conflicts in Dockerfile).

## Comment (novicecpp, 2024-09-04T19:19:11Z)

Now, all tasks are done. I can close this issue!!
Thank you very much @belforte @mapellidario

## Comment (belforte, 2024-09-04T19:32:23Z)

thank you @novicecpp  !!!
surely it was more work than it seemed at the time. But you tamed the beast !

![image](https://github.com/user-attachments/assets/bf3e5a4f-fb3d-4ca4-97ec-9fee7aab0a73)
