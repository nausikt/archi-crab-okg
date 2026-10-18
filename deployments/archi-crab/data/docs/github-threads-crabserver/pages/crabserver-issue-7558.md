# dmwm/CRABServer issue #7558: Error when running GPU custom plugin with crab (libcrypt.so.2: cannot open shared object file)

State: closed
Opened: 2023-03-02T16:23:17Z
Closed: 2023-03-08T16:31:29Z
Labels: Type: Question
URL: https://github.com/dmwm/CRABServer/issues/7558

## Opening post (novicecpp, 2023-03-02T16:23:17Z)

I got this error when I tried to run custom gpu plugin task from @AdrianoDee 
https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230302_132243:tseethon_crab_adriano_gpu_customplugin_prod_20230302_142207/job_out.4.0.txt
```
== CMSSW: unable to load /srv/CMSSW_13_1_0_pre1/lib/el8_amd64_gcc11/pluginMyGPUAnalyzerPluginsPortableCudaAsync.so because libcrypt.so.2: cannot open shared object file: No such file or directory
```
It also happen when run in `crab preparelocal` in lxplus8-gpu. But, run directly via `cmsRun runAnalyzer.py` is works fine.

**Step to reproduce**

Custom plugin code: https://github.com/AdrianoDee/DiMuonSoAAnalyzer
cmsenv: `CMSSW_13_1_0_pre1` 
SCRAM\_ARCH: `el8_amd64_gcc11`
Client: crab-dev `v3.230227`
OS: `lxplus8-gpu`

- Run this command to prepare environment
    ```
    cmsrel CMSSW_13_1_0_pre1
    cd CMSSW_13_1_0_pre1/src/
    cmsenv
    git clone https://github.com/AdrianoDee/DiMuonSoAAnalyzer
    scram b -j 8
    ```
- To submit to crab, use crabConfig and customized pset from https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230302_132243:tseethon_crab_adriano_gpu_customplugin_prod_20230302_142207/debug/
- To run directly with original pset
    ```
    cd DiMuonSoAAnalyzer/DiMuonSoAAnalyzer/python/
    cmsRun runAnalyzer.py
    ```

## Comment (belforte, 2023-03-02T17:03:36Z)

Is this "as simple as" crab job wrapper does not set el8 arch? sent from Stefano's mobile

## Comment (novicecpp, 2023-03-02T17:26:23Z)

I am not familiar with jobwrapper but CMSSW logs said that it ran with `Architecture: el8_amd64_gcc11`.

## Comment (belforte, 2023-03-03T09:18:58Z)

OK, I tried. Nothing trivial then. I will have to reproduce this myself then may be able to dig for clues.

## Comment (novicecpp, 2023-03-06T15:54:10Z)

After private chat with Stefano, we discovered that `scram b` was run in my local machine without setup properly build environment. Thus, `scram b` link the custom plugins to latest libcrypt `libcrypt.so.2` which only have in my local machine.

To solve this, setup build environment by execute `cmssw-el8`. It will start el8 singularity container and attach shell to it. Then, run usual `scram b`.

## Comment (novicecpp, 2023-03-08T16:31:29Z)

After `scram b` error is solved, [my job](https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/230306_151832:tseethon_crab_adriano_gpu_customplugin_prod_20230306_161801/job_out.2.2.txt) got FileReadError but I do not know why. I specify runRange from Adriano config as workaround and finally jobs are finished without error.
