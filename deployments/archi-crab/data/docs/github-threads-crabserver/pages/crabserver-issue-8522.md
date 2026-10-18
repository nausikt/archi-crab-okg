# dmwm/CRABServer issue #8522: Improve PyPI images building process

State: closed
Opened: 2024-06-20T18:38:01Z
Closed: 2024-09-02T16:23:45Z
Labels: Area: CI/CD, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8522

## Opening post (novicecpp, 2024-06-20T18:38:01Z)

Currently, the `crabtaskworker` image is...too big (3.88 GB uncompressed), mainly because the Dockerfile is not optimized.
Also, newer image could not use the layers from older image even the contents are the same because it get rebuild everytime, make it consume so much space (both dev machine and registry), and time.

We can improve this by
- [x] Improving the Dockerfile
    - This [single line](https://github.com/dmwm/CRABServer/blob/f88a9b98f80f9a38e3180ed0a5b2b193a75ee5c0/cicd/crabtaskworker_pypi/Dockerfile#L138) cause files duplication in `/data` path.
    - Use [dive](https://github.com/wagoodman/dive) to inspect the layer. It work fine when dump the output to json file.
- [ ] Caching PyPI deps to make pip install layers more idempotent.
- [x] Consider `docker build` instead of `kaniko` to take advantage of image caching and parallelism ([buildx](https://github.com/docker/buildx))
- [x] Split image into multiple image, a.k.a, "base image". We have expert sit in our office (Andrea, CatA Core Software) to consult.
- Else?

## Comment (belforte, 2024-06-20T19:25:53Z)

is this a good topic for the summer student ? Investigate, try, evaluate.... ?

## Comment (novicecpp, 2024-07-09T17:02:52Z)

First, we can improve the size by simply fix [single line]() that cause files duplication. 

To confirm, using [dive]() to inspect the image by dump the output to json using this command:
```bash
dive -j crab-taskworker-v3-240618-stable.json registry.cern.ch/cmscrab/crabtaskworker:v3.240618-stable
```

Here the json output: [crab-taskworker-v3-240618-stable.json](https://github.com/user-attachments/files/16158722/crab-taskworker-v3-240618-stable.json)
(Note that I cannot open dive in interactive mode, it freeze.) 

If I interpret output correctly, the `.image.fileReference` field show number of time and the file path that have more than one copy in different layer.

For example from json output: 
```json
{
  "image": {
    "sizeBytes": 3880994829,
    "inefficientBytes": 1740276490,
    "efficiencyScore": 0.7727956479413789,
    "fileReference": [
      {
        "count": 2,
        "sizeBytes": 141771252,
        "file": "/data/repos/WMCore/.git/objects/pack/pack-04239b6b0afb94c64c197d9272850b397d18256e.pack"
      },
      {
        "count": 2,
        "sizeBytes": 74617776,
        "file": "/data/miniconda/lib/libopenblasp-r0.3.21.so"
      },
      ....
```

The file `/data/miniconda/lib/libopenblasp-r0.3.21.so` is duplicate, but it may store in different layer.

When I do image flattening (`crane flatten`), the final image is reduce from 3.8GB to 2.98 GB (please ignore the naming here)
```
REPOSITORY                                        TAG                                                                    IMAGE ID       CREATED         SIZE
localhost:44332/test1                             testflatten                                                            9d223d8eba5a   3 hours ago     2.92GB
localhost:44332/test1                             test                                                                   a506bf737f7d   3 hours ago     3.8GB
```

That mean, if we did not make file duplication when build the image, you can reduce final image size up to 900MB.


Now, let take a look at that [single line]() that cause files duplication. 
```
RUN chown -R 1000:1000 ${WDIR}
```
This line, We change the owner of all files in `/data/` path, where we install all of necessary script/binary/library for our services.
What docker does is **copy all files in this path** to new layer, then change permission.

Why? (I did not have ref here, but I think this is what happens ) Because of how container image works; each layer is immutable. You need to copy to the new layer in order to modify it. 
The 2 major advantages of of immutable layer are integrity and caching. You have hash of each layer and can share togather with other images, save disk/transfer/time.

To fix this, we need to make sure **at the time we create the files inside container, it has a proper permission.** For example

- [line 51](https://github.com/dmwm/CRABServer/blob/9728a8552f7e500b9c20445b3773a545246c14ee/cicd/crabtaskworker_pypi/Dockerfile#L51), for `COPY` statement, you need to supply [--chown](https://docs.docker.com/reference/dockerfile/#copy---chown---chmod) option.
- [line 109-111](https://github.com/dmwm/CRABServer/blob/9728a8552f7e500b9c20445b3773a545246c14ee/cicd/crabtaskworker_pypi/Dockerfile#L109-L111), `RUN` statement that create the new directoy. You need to do `chown` at the end of statement or switch to `install` command instead.

## Comment (novicecpp, 2024-09-02T15:25:47Z)

To summarize the solution for above comment, 

Janna removed [the trouble line](https://github.com/dmwm/CRABServer/blob/f88a9b98f80f9a38e3180ed0a5b2b193a75ee5c0/cicd/crabtaskworker_pypi/Dockerfile#L138) and set proper owner when do `COPY` and `RUN` statement. It quite tedious to fix it all for long Dockerfile files. 

But after fix, it surprised me that we actually gain 900MB back!
```
REPOSITORY                                TAG                      IMAGE ID       CREATED       SIZE
registry.cern.ch/cmscrab/crabtaskworker   pypi-test12-1724940928   01e0817c31a5   4 days ago    2.97GB  
registry.cern.ch/cmscrab/crabtaskworker   v3.240809-stable         8332f57c2394   3 weeks ago   3.8GB
```
`v3.240809-stable` is the image version before Janna PR merged.

`dive` still report some files duplication. However, it is a small fraction so no need to bother.

## Comment (novicecpp, 2024-09-02T16:13:08Z)

Janna's PR also contains change of image builder from Kaniko to BuildKit, plus the simpler way to caching images across CI build jobs using [external storage backend](https://docs.docker.com/build/cache/backends/) (we use `registry` backend which is already supported by registry.cern.ch). So, Instead of extra maintenance of creating baseimage, we just push all cache to registry. It cost extra space in registry but it reduce building.

I do not have exact data on how much time it reduce from using BuildKit and registry caching, but in gereral:
- The maximum build time now is not more than 5 mins (build everything from scratch)
- Average build time is 2 minutes if you change some files in `src` directory.
- The minimum build time is 1 minute if you just change the process controller scripts.
- The lowest build time I saw is 26 seconds. I am not sure what does it do though.

But the most satisfying thing for me is when you build in CI and try to pull/run on your local machine, sometimes it takes only 5 seconds to complete. It might be because of BuildKit, cache, refactoring the Dockerfile, or all of them. 

I love this so much because I only have mobile internet in my apartment and it takes ages to pull image again and again.

## Comment (novicecpp, 2024-09-02T16:23:45Z)

I think we do not need the "Caching PyPI deps to make pip install layers more idempotent." anymore because caching already work.

There is still some room for improvement to squeeze more building efficiency, which can start from https://docs.docker.com/build/cache/optimize/

But for this issue, this is enough and we (I am pretty sure that not just me) are happy about the result.

## Comment (belforte, 2024-09-02T17:06:45Z)

VERY HAPPY
