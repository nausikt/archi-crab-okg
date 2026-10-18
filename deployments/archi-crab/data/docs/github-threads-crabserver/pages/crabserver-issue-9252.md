# dmwm/CRABServer issue #9252: Migrate TW image to Alma9, maintain OS and Python version homogeneity with Schedd (AP's), support Py3.9 → Py3.12

State: closed
Opened: 2025-12-19T11:53:57Z
Closed: 2026-03-03T15:47:50Z
Labels: Type: Enhancement, Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9252

## Opening post (nausikt, 2025-12-19T11:53:57Z)

As Stefano pointed out in https://github.com/dmwm/CRABServer/issues/8956#issuecomment-3197455329,
> Given that
> * WMCore and CRAB code are "feature frozen" now
> * alma9 will have security fixes (and hence be usable as container base) until [2032](https://wiki.almalinux.org/release-notes/)
> * python 3.9 is and will always be the python version in Alma9 and Schedulers (AP's) already used them.
>
> move TW image to use Alma9 container as base, instead of python3.8 Debian one
>

Currently, our TW image basically derived from `wmagent-base` which in time of `wmfreeze` has **Debian 13 (Trixie)** underneath as First class base OS-support by WMCore team. 
https://github.com/dmwm/CRABServer/blob/620a01ce9db324f0815e5661b0b55693fd620bae/cicd/crabtaskworker_pypi/Dockerfile#L38-L40
*\*\*there is no alma9 build support by WMCore team yet in this `wmagent-base` layer, as we can see in [harbor/wmagent-base](https://registry.cern.ch/harbor/projects/1771/repositories/wmagent-base/artifacts-tab)\*\**
*N.B. Debian Trixie shipped py3.13 as default, on the other hand Alma9, as a rebuild old RHEL, will officially support py3.9 up-to py3.12 in its default package repositories, further py3.13++ having to be installed from source manually. BUT py3.9 is just fine for our context now.*

_____
AFAICS, we have **3** options to adopt Alma9 in TW could be **Either** 
- [1] Ask WMCore team for `wmagent-base`:`alma9-py3.9--YYMMDDDD` build. 

**OR** try to derive from lower layer image ourself. **i.e.**
- [2] [dmwm-base](https://github.com/dmwm/CMSKubernetes/tree/master/docker/pypi/dmwm-base) (where `wmagent-base` derived from, See also [wmagent-base/Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/2f52b8ef238cdace2555f15ae8ab74da277e56e3/docker/pypi/wmagent-base/Dockerfile#L1-L27))
5 months ago, Alma9 has been support in this layer via [alma9-based Dockerfile](https://github.com/dmwm/CMSKubernetes/tree/master/docker/pypi/dmwm-alma9-base). 
we can see that [harbor/dmwm-base](https://registry.cern.ch/harbor/projects/1771/repositories/dmwm-base/artifacts-tab) have `alma9-py3.12-20250728-stable` and `alma9-py3.9-20250703-stable` available for us. 

**So**, if we work on top of this layer we can switch OS and `py3.9` -> `py3.12` (if AP's was promoted to py3.12 later in the future, we can aligned TW again here) fairly easily via just changing the tag, meanwhile we can have some dmwm's conventions + grounded work out of the box.

*Note: Be aware that we still need to install ***oracle client***, set paths, linking libs a little bit ourself , which used to be handled by `wmagent-base`, where oracle client was provided by Valentin's [cmsweb/oracle](https://github.com/dmwm/CMSKubernetes/blob/master/docker/oracle/Dockerfile)  which been built in debian based env, 
So, here i have **no confident** whether can we copying oracle artifacts across OS-env, and things will magically work out here or not.*
- [3] [cmsweb-alma9-base](https://github.com/dmwm/CMSKubernetes/blob/master/docker/cmsweb-alma9-base) (See also [harbor/cmsweb-alma9-base](https://registry.cern.ch/harbor/projects/1771/repositories/cmsweb-alma9-base/artifacts-tab), [Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/master/docker/cmsweb-alma9-base)] 
where some CMSWEB required certs & packages was addressed. BUT this image have **NO** grounded work from `dmwm` team, so we have to re-established some civilisation ourself from almost scratch. 
____
**My First Glance call**
In January, i see ourself going with [2], not bother WMCore team, instead we open PR to help them support `wmagent-alma9-base` for whole dmwm since someone in dmwm have to get [2] done anyhow? OR other way around is to simply use `wmfreeze` and sitck with `Debian (Trixie)` giving up Alma9.
*P.S. Ofcourse, The other way around is to simply use **wmfreeze** and stick with **Debian (Trixie)** instead, giving up Alma9.*

## Comment (nausikt, 2026-01-21T09:24:30Z)

I tried option [2], and there are a few things to note. *See also* #9265 

1. `dmwm-base`:alma9-**py3.9-20250703**-stable is *not working* now.
     As the time it was built, the image was not derived from **cern/alma9-base** yet, so the CERN rhel9 local repos and also WLCG packages repos were missing inside the container. (*Thus, making the installation of myproxy, voms\* non-trivial*)
2. `dmwm-base`:alma9-**py3.12-20250728**-stable (*the one we are deriving from*)
     now was properly dervied from **cern/alma9-base**, and it works well with only a few minor detail left to be patched.
     e.g. `ln -sf /usr/bin/pip3.12 /usr/bin/pip` to ensure global pip aligned with the right global python that dmwm team have set.
3. when we thoroughly tested *Alma9 equivalent* [2] of the [*Debian* image](https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/wmagent-base/Dockerfile) and it works well. (at least from CRAB side) 
This means we can propose a new **wmagent-alma9-base** Dockerfile [4], for building the new tags e.g. `wmagent-base`:**alma9-py{3.9|3.12}-wmfreeze**, providing alma9 support to the community in this layer.

[4] **wmagent-alma9-base** Dockerfile is expected to be placed at [dmwm/CMSKubernetes:docker/pypi](https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/)/***wmagent-alma9-base***.
*This would be the Alma9 equivalent of the Debian-based in [wmagent-base/Dockerfile](https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/wmagent-base/Dockerfile)*
```Dockerfile
FROM registry.cern.ch/cmsweb/oracle:23_9-go1.25-oci8-deb13-aio-stable AS oracle
FROM registry.cern.ch/cmsweb/dmwm-base:alma9-py3.12-20250728-stable

RUN dnf install -y epel-release # required by rlwrap package.
RUN dnf -y update && \
    dnf -y install \
      # basic OS packages
      cronie cronie-anacron \
      mariadb-server mariadb-connector-c-devel \
      myproxy voms-clients \
      rlwrap libaio \
      # build-essential
      gcc gcc-c++ make glibc-devel \
      # required for yui
      wget unzip \
      # debugging
      hostname net-tools iputils procps-ng jq \
      # Install recursive ps utility tool (pstree, a replacement of pslist)
      psmisc \
      s-nail && \
    dnf -y clean all && \
    rm -rf /var/cache/dnf

# copy oracle client:
COPY --from=oracle /usr/lib/oracle /usr/lib/oracle
# Renaming are not necessary in alma9, Since libaio live well in /usr/lib64/libaio.so.1
# RUN ln -s /usr/lib/x86_64-linux-gnu/libaio.so.1t64.0.2 /usr/lib/x86_64-linux-gnu/libaio.so.1
ENV LD_LIBRARY_PATH=/usr/lib/oracle
ENV PATH=$PATH:/usr/lib/oracle
ENV PKG_CONFIG_PATH=/usr/lib/oracle
```

## Comment (nausikt, 2026-03-03T15:47:50Z)

Done.
