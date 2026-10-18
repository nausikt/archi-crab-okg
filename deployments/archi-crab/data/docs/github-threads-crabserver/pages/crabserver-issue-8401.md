# dmwm/CRABServer issue #8401: PyPI release image/pipeline

State: closed
Opened: 2024-05-14T08:10:24Z
Closed: 2024-06-24T10:50:56Z
Labels: Area: CI/CD, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8401

## Opening post (novicecpp, 2024-05-14T08:10:24Z)

This is the part of [the new PyPI image](https://github.com/dmwm/CRABServer/issues/7560) and [the new automated pipeline](https://github.com/dmwm/CRABServer/issues/8267).

The release image is the image that we use in prod. The only different between dev image and release image is the version string that service can use for report to monitoring system.

We are not commit the version string into source code but alter it in RPM build process instead:
- For REST, `version` variable is inside [src/python/CRABInterface/\_\_init\_\_.py](https://github.com/dmwm/CRABServer/blob/c69980662cbd4fa76e3801b6f3085856032743d6/src/python/CRABInterface/__init__.py) ([crabserver.spec](https://github.com/cms-sw/cmsdist/blob/a5a0b8640d227a432388285b8c0a11dfd5c0706d/crabserver.spec#L35))
- For TW, `version` variable is inside [src/python/TaskWorker/\_\_init\_\_.py](https://github.com/dmwm/CRABServer/blob/c69980662cbd4fa76e3801b6f3085856032743d6/src/python/TaskWorker/__init__.py) ([crabtaskworker.spec](https://github.com/cms-sw/cmsdist/blob/a5a0b8640d227a432388285b8c0a11dfd5c0706d/crabtaskworker.spec#L38))

If we build and deploy PyPI image from current master branch in production, we will get version report from our monitor as `development`, not proper version string like `v3.240305`.
So pre-release step is needed before building images.

One more thing is the image tag. It is better to differentiate between RPM and the new PyPI image. Also, CMSWEB requires the tag to have a `-stable` suffix to set the cleanup rules for non-stable tags and retain the latest stable tag forever.

## Comment (novicecpp, 2024-05-14T08:17:39Z)

@mapellidario @belforte, I would like to ask for consensus on the image tag.

I propose to suffix the image tag with `.pypi-stable`. For example, the image tag of [v3.240510](https://github.com/dmwm/CRABServer/releases/tag/v3.240510) would be `v3.240510.pypi-stable`.

Do you guys agree?

## Comment (mapellidario, 2024-05-14T08:21:15Z)

if we plan about dropping the "pypi" portion sooner or later, then yes I agree :)

## Comment (belforte, 2024-05-14T09:36:55Z)

why do we need `pypi` at all ?

## Comment (novicecpp, 2024-05-14T09:41:17Z)

To prevent confusion during migration from RPM to PyPI in production.

I plan to still build RPM image until PyPI image is running in prod for at least 2 weeks.

## Comment (belforte, 2024-05-14T09:44:00Z)

but do we have `-stable` for RPM built images ? Maybe change tag name for those which will disappear ?

## Comment (novicecpp, 2024-05-14T10:07:48Z)

> but do we have -stable for RPM built images ?

No. We never do it. It is not enforced by the system or anything. Now we have an automated pipeline, so we can do it automatically (to be fair, we can add more lines of code to Jenkins to automate this too).

> Maybe change tag name for those which will disappear ?

Sorry, no. This require more work to do so.

## Comment (belforte, 2024-05-14T11:19:13Z)

So no need to add pipy. -stable already tells that image comes from new pipeline

On May 14, 2024 12:08 PM, Thanayut Seethongchuen ***@***.***> wrote:

but do we have -stable for RPM built images ?

No. We never do it. It is not enforced by the system or anything. Now we have an automated pipeline, so we can do it automatically (to be fair, we can add more lines of code to Jenkins to automate this too).

Maybe change tag name for those which will disappear ?

Sorry, no. This require more work to do so.

—
Reply to this email directly, view it on GitHub<https://github.com/dmwm/CRABServer/issues/8401#issuecomment-2109802868>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AAOAVWOESE5LZAII6DPHJJTZCHPATAVCNFSM6AAAAABHVVAKWGVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDCMBZHAYDEOBWHA>.
You are receiving this because you were mentioned.Message ID: ***@***.***>

## Comment (novicecpp, 2024-05-14T12:03:23Z)

Thanks for comments, Stefano, Dario.
From now on, the image tag of the new PyPI image will be `v3.YYMMDD-stable`.

## Comment (novicecpp, 2024-05-14T12:12:35Z)

For the pipeline part, 

- 2 new stages
    - `pre_release`: Between `prepare_env` and `build_docker` to alter the `__init__.py` like we do with RPM build. Use CI cache to store change between stage.
    -  `release`: After the `check_testsuite` stage to retag the image.
- New tool call [crane](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md) are used for register the release tag to docker registry. It pull image from that built in previous stage, re-tag, and then push the new tag. Compare to Kaniko that need to rebuild the whole image everytime (see [GoogleContainerTools/kaniko#676](https://www.github.com/GoogleContainerTools/kaniko/issues/676#issuecomment-597504724))
    - It is small binary file that can copy/paste to [buildtools](https://github.com/dmwm/CRABServer/tree/master/cicd/buildtools) and works out off the box.
- ~~`FORCE_RELEASE` variable will be used to skip  `deploy`, `run_testsuite` and `check_testsuite`.~~ Trigger CI with `SKIP_DEPLOY` and use release tag (this is simpler in CI config compare to add more variables).

## Comment (belforte, 2024-05-14T14:14:06Z)

I am curious, how is `crane` here  different from a tiny script with three docker commands ? We should avoid binaries in GH as much as possible. Not all nice tools are still working 3 years in the future.

## Comment (novicecpp, 2024-05-14T15:05:19Z)

`crane` can run in userspace like kaniko, i.e., it can run inside any container. 
I already thought about your concern and have the same solution as you said: simply switch back to the docker command.

But, it is OK to use docker command because we own the runner and have root access to use docker command. I switch to that.

## Comment (belforte, 2024-05-14T15:10:47Z)

> crane can run in userspace like kaniko, i.e., it can run inside any container.

:open_mouth:   I am talking about things which I do not understand, sorry. How does the runner get access to kaniko, I vaguely remember that you are not using the CERN-deployed one yet.

## Comment (novicecpp, 2024-05-14T15:35:44Z)

kaniko is a binary inside a container that can build images without calling the Docker daemon. Remember that calling the `docker` command means you ask the Docker daemon to do something; this requires privilege equivalent to root.

We run kaniko like we run CRAB REST in Kubernetes, no direct access to node resources, no root power.

## Comment (belforte, 2024-05-14T16:02:49Z)

yes, all stuff that I do not understand enough to have an educated opinion. Forget all I said on this topic. For running docker in the VM's we use unix group which does not give root-like privileges. We can still put binaries in a public container in S3, if crane can't be downloaded on the fly like in https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md#using-with-gitlab (IIUC)

## Comment (novicecpp, 2024-06-24T10:50:56Z)

Docs are done. Please take a look.

Explanation: https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/pipelines/release.html
Tutorial: https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/tutorial.html#running-the-release-pipeline
