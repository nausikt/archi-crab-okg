# dmwm/CRABServer issue #8880: keep uptodate dependencies on WMCore

State: closed
Opened: 2025-01-15T13:56:07Z
Closed: 2025-01-27T13:47:23Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8880

## Opening post (belforte, 2025-01-15T13:56:07Z)

we have not updated the wmcore version which we use since long time.
Should test recent tags and possibly think of a way to do it routinely.
Note that WMCore comes in differently in CRABServer (via WMA image) and TW/Publisher (via GH)

## Comment (belforte, 2025-01-15T16:27:59Z)

note also https://github.com/dmwm/WMCore/issues/12181#issuecomment-2591082512

## Comment (nausikt, 2025-01-23T14:53:33Z)

I've added the bumping script to ease our routine. Please have a look at the script [here](https://github.com/dmwm/CRABServer/pull/8891). #8891 
###  How-to-Use 
- for bumping to latest version (now=2.3.7.1) > `./scripts/bumpWMCoreVersion.sh`
- for bumping to specific version > `./scripts/bumpWMCoreVersion.sh 2.3.7.6`
_____________________

This script will update tag version in the comment of **_3 requirements.txt_** on both **CRABServer** and **TaskWorker**

1. [cicd/crabserver_pypi/requirements.txt](https://github.com/dmwm/CRABServer/blob/master/cicd/crabserver_pypi/requirements.txt) 

```
-# https://github.com/dmwm/WMCore/blob/9c6e83d1d23983c0296eee318c9e6255ff80d01b/requirements.txt
+# https://github.com/dmwm/WMCore/blob/2.3.7.1/requirements.txt
```
2. [cicd/crabtaskworker_pypi/requirements.txt](https://github.com/dmwm/CRABServer/blob/master/cicd/crabtaskworker_pypi/requirements.txt).
```
-# https://github.com/dmwm/WMCore/blob/2.2.4rc6/requirements.txt
+# https://github.com/dmwm/WMCore/blob/2.3.7.1/requirements.txt
```
3. [cicd/crabserver_pypi/wmcore_requirements.txt](https://github.com/dmwm/CRABServer/blob/master/cicd/crabserver_pypi/wmcore_requirements.txt).
```
-https://github.com/dmwm/WMCore 2.3.6rc2
+https://github.com/dmwm/WMCore 2.3.7.1
```

All of the updated version tag in these comments will be retrieve later and WMCore will be either installed via `cicd/crabserver/installWMCore.sh` or `cicd/crabtaskworker_pypi/Dockerfile` during CI, docker image building time. As you can see in the following.
``` Dockerfile
RUN wmcore_repo="$(grep -v '^\s*#' wmcore_requirements.txt | cut -d' ' -f1)" \
    && wmcore_version="$(grep -v '^\s*#' wmcore_requirements.txt | cut -d' ' -f2)" \
    && git clone  --depth 1 ${wmcore_repo} -b "${wmcore_version}" /build/WMCore \
    && ( cd /build/WMCore; git status )
```
______________________________
### My Questions:
Should we also include bumping version of *cmsweb* derived image to `cmsweb/cmsweb:20240501-stable` in CRABServer's Dockefile in this procedure as well? Thank you!
``` Dockerfile
FROM registry.cern.ch/cmsweb/cmsweb:20230427-stable AS cmsweb
```

## Comment (belforte, 2025-01-23T15:25:38Z)

are those commented out lines like
`# https://github.com/dmwm/WMCore/blob/2.3.7.1/requirements.txt`
really used ? If so we should better have some hint about this in the out `requirements.txt` files.

did you test this ? And the images built in this way ?

updating cmsweb image name is easy also w/o a script, questions are more : how to know when a new one is build, how to validate...

## Comment (belforte, 2025-01-23T15:44:04Z)

I like the idea of having a script which makes sure we change consistently in all places and helps us remember what to change.

## Comment (nausikt, 2025-01-23T15:52:23Z)

> are those commented out lines like `# https://github.com/dmwm/WMCore/blob/2.3.7.1/requirements.txt` really used ? If so we should better have some hint about this in the out `requirements.txt` files.
> 
> did you test this ? And the images built in this way ?
> 
> updating cmsweb image name is easy also w/o a script, questions are more : how to know when a new one is build, how to validate...

You were right that commented out lines were not used in both CRABServer and TaskWorker cases. the `wmcore_requirements.txt` are the only file that matter.

For testing via image building, somehow i got stuck on local (illegal instruction something might related to my M3 architecuture). let me fixes this and put more efforts on testing aspects.
```
Preparing to unpack .../bash-completion_1%3a2.11-2_all.deb ...
Illegal instruction
dpkg: error processing archive /var/cache/apt/archives/bash-completion_1%3a2.11-2_all.deb (--unpack):
 new bash-completion package pre-installation script subprocess returned error exit status 132
Errors were encountered while processing:
 /tmp/apt-dpkg-install-RWrMJf/01-bash-completion_1%3a2.11-2_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
The command '/bin/bash -c apt-get update     && apt-get install -y tini voms-clients-java libsasl2-dev python3-dev libldap-dev libssl-dev zip git fd-find ripgrep bash-completion     && apt-get clean all' returned a non-zero code: 100
```

## Comment (nausikt, 2025-01-23T19:05:11Z)

It has gone through our test suites on `test12`, but got stuck at `check_testsuite` with exit code 4 as following.
```
~/shell/builds/sedxNxqzs/0/crab3/CRABServer
+ [[ FULL-STATUS-UNKNOWN == \F\U\L\L\-\S\T\A\T\U\S\-\U\N\K\N\O\W\N ]]
+ exit 4
Command fail with exit code 4 (3/10 attempted)
Sleep for 900 seconds. Until  20:01 CET
```
but not sure if this is sufficient to confirm that we are safe to proceed with the bump. please let me know is there any other validation needed.

Beside that, Let me try propose something and learn from your feedbacks.
________________________________
#### Regarding your questions, wishes to reduce our routine workloads.
Weekly/Bi-Weekly/Monthly polling-based Jenkins bot to automatically update dependencies for us.
1. The Jenkins bot polls **WMCore** and **CMSWeb** to check for any changes via github api for their latest stable `tag_name`.
2. Then it creates an `automatic-update-deps-{weekly?}-{year}` branch.
3. It bumps the `tag_name` to the latest stable release.
4. Validation is done by using the git tag to trigger the CI, **build-deploy-test** pipeline.
5. If _testsuite_, _testsuite_CV_, _testsuite_CCV_ and _check_testsuite_ go well: 
6. The Jenkins bot commits, pushes, and opens a pull request for us.
7. Finally, Leaving us with one-click of merge PR every Bi-Weekly to decide whether to keep things up-to-date if there exists new releases.

These could also applied to other aspects of `libs`, `deps` versions beyond `WMCore` and `CMSWeb` too.
**3,4,5** utilized our core pipeline, it's already done and well maintained by our CRAB's folks. **1,2,6,7**  could be adopt/extended functionality from our **Jenkins pylint bot**. 

**Why don't we use push-based hooks for these events?**
-> From our history we rarely updates these deps version. therefore, periodically might keep things simple, than unpredictable push events.
**Weekly/Bi-Weekly/Monthly?**
-> it depends on how frequently we want to keep up with evolving dependencies, security patches, and vulnerability updates.

## Comment (belforte, 2025-01-24T10:14:20Z)

I can't help with building on Mac. But I think at some point I was managing to build on my Ubuntu laptop. But I do never do because it takes too long to pull/push from CERN registry to Italy. But if your popeline reached the check step, it clearly means that build was OK and you an inspect deployed containers to check what WMCore version they have.

As to the `Command fail with exit code 4 (3/10 attempted)` that's likely due to ongoing problem with the pipeline which Vijay is working on. It never runs satisfactorily since a while. But you can use Grafana to check if jobs worked. Maybe Vijay is at CERN and can show you ? Otherwise I will.

## Comment (belforte, 2025-01-24T10:25:32Z)

I like a lot your ideas on how to make this almost fully automatic. Checking once a month will be plenty.
Let's talk about it in next meeting and converge.

## Comment (nausikt, 2025-01-27T13:47:23Z)

Resolve #8891
