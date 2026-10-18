# dmwm/CRABServer issue #8029: Understand Jenkins submission for SL6 releases (CMSSW_7) 

State: closed
Opened: 2023-11-29T16:25:15Z
Closed: 2023-11-30T23:27:28Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8029

## Opening post (belforte, 2023-11-29T16:25:15Z)

somehow there's evidence that in this case, even selecting "from GH, branch HEAD', task submission for ClientValidation (e.g.) used instead latest current deployed release in CVMFS. This does not make sense at first sight looking at code in https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/configure, https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/setupCRABClient.sh and https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/taskSubmission.sh

- [x] Is this real (reproducible) ?
- [x] Why ?
- [x] Should we change ?

reference: https://github.com/dmwm/CRABServer/issues/8025#issuecomment-1830540956

## Comment (belforte, 2023-11-30T11:07:20Z)

Looking "better" at Jenkins log
```
10:50:13 + /cvmfs/cms.cern.ch/common/cmssw-cc6 -- ./taskSubmission.sh
[...]
10:50:43 gmake[1]: Entering directory `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_7_6_7'
[...]
10:50:48 gmake[1]: Leaving directory `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_7_6_7'
10:50:48 using CMSSW_7 on SL6. Setup/cvmfs/cms.cern.ch/slc6_amd64_gcc900/external/curl/7.59.0
10:50:49 Cloning into 'CRABClient'...
10:50:54 cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54 cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54 cp: cannot stat `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/WMCoreConfiguration.py': No such file or directory
10:50:54 setupCRABClient.sh: line 67: /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/etc/crab-bash-completion.sh: No such file or directory
10:51:02 CRAB client v3.231010
```

translation:
Jenkins script calls [TaskSubmission.sh](https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/taskSubmission.sh), first line there is https://github.com/dmwm/CRABServer/blob/19adcac695227a6cc7918dfe3a25666831c226b5/test/container/testingScripts/taskSubmission.sh#L10

[setupCRABClient.sh](https://github.com/dmwm/CRABServer/blob/master/test/container/testingScripts/setupCRABClient.sh) creates and builds the env. for CMSSW and then clones CRABClient in order to switch to "using client from GH HEAD". But something goes wrong and the clone does not create the directories hence
```
10:50:54 cp: cannot create regular file `CRABClient/src/python/': No such file or directory
```
more errors and the end of the story is that `taskSubmission.sh` uses the default CRABClient which came with cmsenv.

If is odd that `git clone` failed silently, but bottom line is that we need to catch errors and exit with failure, not go on.
I am bit surprised that bash does not do this by default. Anyhow

1. this was clearly a "strange outlier" (full disk ?)
2. I see no evidence that the error was specific of CMSSW_7 or the SL6 container

 FYI @novicecpp since you asked in the meeting "why the py2 lost compatibility error did not affect CMSSW_7"

## Comment (belforte, 2023-11-30T11:08:15Z)

We better fix this while understanding is fresh.
Increase priority.
@mapellidario can you take care ? Your bash skills surely exceeds mine !

## Comment (belforte, 2023-11-30T11:14:06Z)

Should it be useful, here's the full Jenkins log, before it gets deleted by automatic cleanup
```
10:49:22  Started by user belforte
10:49:22  Running as SYSTEM
10:49:22  [EnvInject] - Loading node environment variables.
10:49:22  Building remotely on cms-dmwm-cc7-062 (cms-dmwm-cc7 no_label) in workspace /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
10:49:22  [WS-CLEANUP] Deleting project workspace...
10:49:22  [WS-CLEANUP] Deferred wipeout is used...
10:49:22  [WS-CLEANUP] Done
10:49:22  New run name is '#557; CV=true; TS=false; CCV=false; CRABClient=GH; REST=preprod'
10:49:22  [CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins4434581227535403754.sh
10:49:22  [CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins8323397982101966090.sh
10:49:22  + '[' Xtrue '!=' Xtrue ']'
10:49:22  [CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins5018448462418012809.sh
10:49:22  + echo '(DEBUG) client:'
10:49:22  (DEBUG) client:
10:49:22  + echo '(DEBUG)   \- CRABClient_version: GH'
10:49:22  (DEBUG)   \- CRABClient_version: GH
10:49:22  + echo '(DEBUG)   \- CRABServer_tag: HEAD'
10:49:22  (DEBUG)   \- CRABServer_tag: HEAD
10:49:22  + echo '(DEBUG) REST:'
10:49:22  (DEBUG) REST:
10:49:22  + echo '(DEBUG)   \- REST_Instance: preprod'
10:49:22  (DEBUG)   \- REST_Instance: preprod
10:49:22  + echo '(DEBUG) CMSSW:'
10:49:22  (DEBUG) CMSSW:
10:49:22  + echo '(DEBUG)   \- CMSSW_release: CMSSW_7_6_7'
10:49:22  (DEBUG)   \- CMSSW_release: CMSSW_7_6_7
10:49:22  + echo '(DEBUG) test parameters:'
10:49:22  (DEBUG) test parameters:
10:49:22  + echo '(DEBUG)   \- Client_Validation_Suite: true'
10:49:22  (DEBUG)   \- Client_Validation_Suite: true
10:49:22  + echo '(DEBUG)   \- Client_Configuration_Validation: false'
10:49:22  (DEBUG)   \- Client_Configuration_Validation: false
10:49:22  + echo '(DEBUG)   \- Check_Publication_Status: No'
10:49:22  (DEBUG)   \- Check_Publication_Status: No
10:49:22  + echo '(DEBUG)   \- Repo_GH_Issue: dmwm/CRABServer'
10:49:22  (DEBUG)   \- Repo_GH_Issue: dmwm/CRABServer
10:49:22  + echo '(DEBUG)   \- Repo_Testing_Scripts: dmwm/CRABServer'
10:49:22  (DEBUG)   \- Repo_Testing_Scripts: dmwm/CRABServer
10:49:22  + echo '(DEBUG)   \- Branch_Testing_Scripts: master'
10:49:22  (DEBUG)   \- Branch_Testing_Scripts: master
10:49:22  + echo '(DEBUG)   \- Test_Docker_Image: registry.cern.ch/cmscrab/crabtesting:231009'
10:49:22  (DEBUG)   \- Test_Docker_Image: registry.cern.ch/cmscrab/crabtesting:231009
10:49:22  + echo '(DEBUG) end'
10:49:22  (DEBUG) end
10:49:22  + rm -rf /tmp/crabTestConfig/
10:49:22  + docker system prune -af
10:49:48  Deleted Images:
10:49:48  untagged: registry.cern.ch/cmscrab/crabtesting:231009
10:49:48  untagged: registry.cern.ch/cmscrab/crabtesting@sha256:7f00b3da3b4e5940003f3c25830e88c7d879e19e4bd1aa396220dc8d411ac9af
10:49:48  deleted: sha256:e5639587ab8ef3f4f71484719a53f703f3e9a3900e486aa17c0fc999ed4868c7
10:49:48  deleted: sha256:7b7a9efb0c597eec631dd6c648747a062d5fcffc8227718f129d76486e7f9a4c
10:49:48  deleted: sha256:d6e03e73da0a354d1c460e2e7cae242222f7a79b39d1c2f367005e8d1043ce8b
10:49:48  deleted: sha256:5fc88ef46fdbb054c65985727dfca1bdb98c4266524439587f0483e06fe6bbf0
10:49:48  deleted: sha256:6cec90621f51d38a34cd9f22235ebbb405785cad3e43424caaac24898d264e76
10:49:48  deleted: sha256:aeda601a0adf87bf2e24ada4b21ec6ca8e1b1dbe353dcdbfcb79fac4d5a927dc
10:49:48  deleted: sha256:d2699959effd97945a9075e6771a7e547b29a8a43c4708d9a714478208fa82e1
10:49:48  deleted: sha256:2d7696ee23ce24c5e08ff671d9fc8085de6088eebda62314dc69b47e0b1c4499
10:49:48  deleted: sha256:7165ebffff89396c6eb1191a1f2c8125eca26519e6a361eeca0fe5928c96f5bc
10:49:48  deleted: sha256:3c000c1022ed45a0481eb6d150bf1e30b41b6f71f1b08a8a43e88a592555913f
10:49:48  deleted: sha256:b3b7cba4dc5376670fc9a3ada8b1bd37731844067891088115f2b5e6bbda7d27
10:49:48  deleted: sha256:1c041d86bba768387393a56289c5a6ec6ac756821e1c18761851a9aaa44d9787
10:49:48  deleted: sha256:1d1fdacafe279fbe0c9834f9c540a791640d4df1d2c94356e6dc2f42d3fc3dfa
10:49:48  deleted: sha256:c00ab764af3743f5a87248b1af7e0d20e924be82665206295efd30e6a801ee95
10:49:48  deleted: sha256:6aa02d9456ece2570acb6c3c083fa2054e801011416932645758b7945a7d64ff
10:49:48  deleted: sha256:64d69f85a99ad6fc58f06de4b7485a54cdf0e5c526a16ce36036ddf78afdb59d
10:49:48  deleted: sha256:59bb1281c26b3bd39bd4e6ec492cd5a93e24088c7d30a53cf2a2c06179e06c05
10:49:48  deleted: sha256:28efa39090e9c6bd69fb209a019f7f6c2557f972737187461704603e576443e4
10:49:48  deleted: sha256:b34c329b8d34f473d0231253bb19fc9d31ec444a6fdf83b8c5739876f09220f8
10:49:48  deleted: sha256:5985946d3cb11db0c0218360877105bc192c41f665dbcb32987ae92da4975621
10:49:48  deleted: sha256:38f20f145649c74abe8c5c93100ddef4b8235c51d910553f7144cf8839a9273c
10:49:48  deleted: sha256:3479e31ef7441df62f7f185ca97886d6f7b228fc85d71972a0873673299d5176
10:49:48  deleted: sha256:4e1d6426f2df5d358c8625b8492410d49ddfdf15b812bd47c38ca7e81bf40670
10:49:48  deleted: sha256:5776efeea13a6ae1929e1fb62d152e49700d8e11c7ffbadb76f5330ed2f96e4d
10:49:48  deleted: sha256:42439be83ea864c91595e6869864cb9e3ade28179363cf2de1b92dd5baafce3a
10:49:48  deleted: sha256:598042f19aec7360a5829e90e1dba94a91fa30a69267f44821cc3d9175190327
10:49:48  deleted: sha256:a334aeca7a34a4342961135f8710a617ac2ce9081f1fca6038a1b4ac74823573
10:49:48  deleted: sha256:8ef21b8da5ce4c2615f8b4c3d64375bbf39a2da1d4307e4397a1e9449baefba3
10:49:48  deleted: sha256:1087c00f0c42401caef64d20ec4ea304537984007a0eb4ef23903de8f8daee02
10:49:48  deleted: sha256:0556907966693b7df01fbe9be522bfb3ef514e6c66f3f9f14a2c69c9bb2d8148
10:49:48  deleted: sha256:a9ef99213e33635486bdba1d0d838801f3553b6d930a9777da7f6b9e1f07b73f
10:49:48  deleted: sha256:4de353517478298363bfd408834559a35945458f71f2a1a7aa1d7efa08deb58f
10:49:48  deleted: sha256:905ffbd9eac3594388b72054fe3546a4a4d80fed16dff412130b5c299f2bc695
10:49:48  deleted: sha256:eaf5d8f0342bcba12093b9542c8efb6f918ee0ff49176df9a4eb9217feae6ce4
10:49:48  deleted: sha256:f2d38455c6356dd03d94ce8f4d7af7b438e5c202fd4d49ce6392f9bf2abdc85d
10:49:48  deleted: sha256:fbd8f25453b1eb0773330e54e2fe3cc2a4a4f12c851b2e140b912e66ef1c5fc3
10:49:48  deleted: sha256:abc16edcfd5a57e97882c2b07bd92e8e92ab9728b905245aee0530b871ab99cb
10:49:48  deleted: sha256:a269972824bf0e5c2872a433dab9e22b12362ea2af4c76933286e2d7db4bd8b6
10:49:48  
10:49:48  Total reclaimed space: 3.694GB
10:49:48  + mkdir artifacts
10:49:48  + touch message_taskSubmitted
10:49:48  + ls -l /cvmfs/cms-ib.cern.ch/latest/
10:49:48  total 79
10:49:48  drwxr-xr-x. 2 cvmfs cvmfs     6 Nov 26 02:21 bin
10:49:48  -rw-r--r--. 1 cvmfs cvmfs 52781 Jan 19  2022 bootstrap.sh
10:49:48  drwxr-xr-x. 2 cvmfs cvmfs     6 Nov 27 03:56 bootstraptmp
10:49:48  drwxr-xr-x. 2 cvmfs cvmfs   242 Nov 27 04:07 cmsmon
10:49:48  -rwxr-xr-x. 1 cvmfs cvmfs  1558 Nov 26 01:59 cmsset_default.csh
10:49:48  -rwxr-xr-x. 1 cvmfs cvmfs  1530 Nov 26 01:59 cmsset_default.sh
10:49:48  drwxr-xr-x. 2 cvmfs cvmfs    20 Nov 27 23:56 common
10:49:48  lrwxrwxrwx. 1 cvmfs cvmfs     6 Nov 26 01:59 cvmfs -> /cvmfs
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 26 01:22 el8_amd64_gcc10
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 27 23:53 el8_amd64_gcc11
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 28 00:20 el8_amd64_gcc12
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    17 Aug  3 22:32 el9_amd64_gcc11
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 28 00:31 el9_amd64_gcc12
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    21 Nov 26 02:12 etc
10:49:48  -rw-r--r--. 1 cvmfs cvmfs 11358 Nov 26 01:59 LICENSE
10:49:48  drwxr-xr-x. 2 cvmfs cvmfs    55 Nov 27 03:56 logs
10:49:48  drwxr-xr-x. 7 cvmfs cvmfs    17 Nov 26 02:12 share
10:49:48  lrwxrwxrwx. 1 cvmfs cvmfs    30 Nov 28 09:41 SITECONF -> /cvmfs/cms-ib.cern.ch/SITECONF
10:49:48  drwxr-xr-x. 9 cvmfs cvmfs    17 Nov 26 00:37 slc6_amd64_gcc472
10:49:48  drwxr-xr-x. 9 cvmfs cvmfs    88 Nov 26 00:31 slc6_amd64_gcc481
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:30 slc6_amd64_gcc530
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:40 slc6_amd64_gcc630
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    66 Mar 29  2022 slc7_amd64_gcc10
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    17 Aug  3 22:36 slc7_amd64_gcc11
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 28 00:18 slc7_amd64_gcc12
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:28 slc7_amd64_gcc530
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    77 Dec 18  2019 slc7_amd64_gcc630
10:49:48  drwxr-xr-x. 8 cvmfs cvmfs    77 Nov  9 16:08 slc7_amd64_gcc700
10:49:48  + git clone https://github.com/cms-sw/cms-bot
10:49:48  Cloning into 'cms-bot'...
10:49:55  + voms-proxy-init -rfc -voms cms -valid 192:00
10:50:03  Contacting voms-cms-auth.app.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch] "cms"...
10:50:05  Remote VOMS server contacted succesfully.
10:50:05  
10:50:07  
10:50:07  Created proxy in /tmp/x509up_u501.
10:50:07  
10:50:07  Your proxy is valid until Wed Dec 06 10:50:05 CET 2023
10:50:07  + export X509_USER_CERT=/home/cmsbld/.globus/usercert.pem
10:50:07  + X509_USER_CERT=/home/cmsbld/.globus/usercert.pem
10:50:07  + export X509_USER_KEY=/home/cmsbld/.globus/userkey.pem
10:50:07  + X509_USER_KEY=/home/cmsbld/.globus/userkey.pem
10:50:07  ++ voms-proxy-info -path
10:50:08  + export PROXY=/tmp/x509up_u501
10:50:08  + PROXY=/tmp/x509up_u501
10:50:08  + voms-proxy-info -all
10:50:08  subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=720455755
10:50:08  issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
10:50:08  identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
10:50:08  type      : RFC3820 compliant impersonation proxy
10:50:08  strength  : 2048
10:50:08  path      : /tmp/x509up_u501
10:50:08  timeleft  : 191:59:56
10:50:08  key usage : Digital Signature, Key Encipherment
10:50:08  === VO cms extension information ===
10:50:08  VO        : cms
10:50:08  subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
10:50:08  issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
10:50:08  attribute : /cms/Role=NULL/Capability=NULL
10:50:08  attribute : /cms/country/Role=NULL/Capability=NULL
10:50:08  attribute : /cms/country/ch/Role=NULL/Capability=NULL
10:50:08  attribute : /cms/itcms/Role=NULL/Capability=NULL
10:50:08  timeleft  : 191:59:56
10:50:08  uri       : voms-cms-auth.app.cern.ch:15000
10:50:08  
10:50:08  + export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
10:50:08  + PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
10:50:08  + export ERR=false
10:50:08  + ERR=false
10:50:08  ++ pwd
10:50:08  + export WORK_DIR=/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
10:50:08  + WORK_DIR=/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
10:50:08  + export CMSSW_release=CMSSW_7_6_7
10:50:08  + CMSSW_release=CMSSW_7_6_7
10:50:08  + curl -s -O https://raw.githubusercontent.com/dmwm/CRABServer/master/test/testingConfigs
10:50:08  ++ grep 'CMSSW_release=CMSSW_7_6_7;' testingConfigs
10:50:08  + CONFIG_LINE='CMSSW_release=CMSSW_7_6_7;SCRAM_ARCH=slc6_amd64_gcc493;inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO;master=no;'
10:50:08  ++ echo 'CMSSW_release=CMSSW_7_6_7;SCRAM_ARCH=slc6_amd64_gcc493;inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO;master=no;'
10:50:08  ++ grep SCRAM_ARCH
10:50:08  ++ tr ';' '\n'
10:50:08  ++ sed 's|SCRAM_ARCH=||'
10:50:08  + export SCRAM_ARCH=slc6_amd64_gcc493
10:50:08  + SCRAM_ARCH=slc6_amd64_gcc493
10:50:08  ++ echo 'CMSSW_release=CMSSW_7_6_7;SCRAM_ARCH=slc6_amd64_gcc493;inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO;master=no;'
10:50:08  ++ tr ';' '\n'
10:50:08  ++ sed 's|inputDataset=||'
10:50:08  ++ grep inputDataset
10:50:08  + export inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO
10:50:08  + inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO
10:50:08  ++ echo slc6_amd64_gcc493
10:50:08  ++ tail -c 2
10:50:08  ++ cut -d_ -f 1
10:50:08  + export singularity=6
10:50:08  + singularity=6
10:50:08  + echo SCRAM_ARCH=slc6_amd64_gcc493
10:50:08  + echo inputDataset=/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO
10:50:08  + echo singularity=6
10:50:08  + echo Repo_GH_Issue=dmwm/CRABServer
10:50:08  + echo Repo_Testing_Scripts=dmwm/CRABServer
10:50:08  + echo Branch_Testing_Scripts=master
10:50:08  + echo Test_Docker_Image=registry.cern.ch/cmscrab/crabtesting:231009
10:50:08  + echo -e '**Tests started for following configuration:**\n\n'
10:50:08  + echo -e '**Configuration:**\n\n - CRABClient_version: **GH**\n- REST_Instance: **preprod**\n- CMSSW_release: **CMSSW_7_6_7**\n- SCRAM_ARCH: **slc6_amd64_gcc493**'
10:50:08  + '[' XGH == XGH ']'
10:50:08  + echo -e '- CRABServer_tag: **HEAD**'
10:50:08  + echo -e '\n**Tests started:**\n'
10:50:08  + '[' Xtrue == Xtrue ']'
10:50:08  + echo -e '- [ ] Client_Validation'
10:50:08  + '[' Xfalse == Xtrue ']'
10:50:08  + '[' Xfalse == Xtrue ']'
10:50:08  ++ date '+%Y-%m-%d %H:%M:%S'
10:50:08  + echo -e 'Started at: 2023-11-28 10:50:08\nLink to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/557/) '
10:50:08  + issueTitle='#557: Test GH CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release'
10:50:08  + /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#557: Test GH CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release' -R message_configuration
10:50:10  Authenticating to Github and connecting to repo
10:50:10  Authentication succeeeded
10:50:10  Checking existing Issue curl -s 'https://api.github.com/search/issues?q=%23557%3A%20Test%20GH%20CRABClient%20using%20preprod%20REST%20instance%20and%20CMSSW_7_6_7%20CMSSW%20release+repo:dmwm/CRABServer+in:title+type:issue' | grep '"number"' | head -1 | sed -e 's|.*: ||;s|,.*||'
10:50:10  Existing Issues: 0 
10:50:10  Creating issue request
10:50:10  + echo 'issueTitle=#557: Test GH CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release'
10:50:10  + '[' X6 == X6 ']'
10:50:10  + echo 'Starting singularity 6 container.'
10:50:10  Starting singularity 6 container.
10:50:10  + git clone https://github.com/dmwm/CRABServer
10:50:10  Cloning into 'CRABServer'...
10:50:13  + cd CRABServer
10:50:13  ++ git rev-parse --abbrev-ref HEAD
10:50:13  + [[ master != master ]]
10:50:13  + cd test/container/testingScripts
10:50:13  + scramprefix=cc6
10:50:13  + '[' X6 == X6 ']'
10:50:13  + scramprefix=cc6
10:50:13  + '[' X6 == X8 ']'
10:50:13  + /cvmfs/cms.cern.ch/common/cmssw-cc6 -- ./taskSubmission.sh
10:50:24  WARNING: In non-interactive mode release checks e.g. deprecated releases, production architectures are disabled.
10:50:42  >> Local Products Rules ..... started
10:50:42  >> Local Products Rules ..... done
10:50:42  >> Building CMSSW version CMSSW_7_6_7 ----
10:50:42  >> Subsystem BigProducts built
10:50:43  >> Local Products Rules ..... started
10:50:43  >> Local Products Rules ..... done
10:50:43  gmake[1]: Entering directory `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_7_6_7'
10:50:43  >> Creating project symlinks
10:50:43  >> Done python_symlink
10:50:43  >> Compiling python modules cfipython/slc6_amd64_gcc493
10:50:48  >> Compiling python modules python
10:50:48  >> All python modules compiled
10:50:48  >> Pluging of all type refreshed.
10:50:48  >> Done generating edm plugin poisoned information
10:50:48  gmake[1]: Leaving directory `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_7_6_7'
10:50:48  using CMSSW_7 on SL6. Setup/cvmfs/cms.cern.ch/slc6_amd64_gcc900/external/curl/7.59.0
10:50:49  Cloning into 'CRABClient'...
10:50:54  cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54  cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54  cp: cannot stat `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/WMCoreConfiguration.py': No such file or directory
10:50:54  setupCRABClient.sh: line 67: /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/etc/crab-bash-completion.sh: No such file or directory
10:51:02  CRAB client v3.231010
10:51:02  
10:51:02  Starting task submission for Client Validation testing.
10:51:02  
10:51:02  
10:51:02  Submitting file: ./crabConfiguration.py
10:51:08  Will use CRAB configuration file ./crabConfiguration.py Importing CMSSW configuration pset.py Finished importing CMSSW configuration pset.py Sending the request to the server at cmsweb-testbed.cern.ch Success: Your task has been delivered to the preprod CRAB3 server. Task name: 231128_095108:cmsbot_crab_20231128_105103 Project dir: /tmp/crabClientValidation/crab_20231128_105103 Please use ' crab status -d /tmp/crabClientValidation/crab_20231128_105103 ' to check how the submission process proceeds. Log file is /tmp/crabClientValidation/crab_20231128_105103/crab.log
10:51:08  + cd /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
10:51:08  + mv /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/artifacts/project_directories /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/artifacts/submitted_tasks_CV /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/
10:51:08  + false
10:51:08  + tests=(["Task_Submission_Status_Tracking"]=submitted_tasks_TS ["Client_Validation_Suite"]=submitted_tasks_CV ["Client_Configuration_Validation"]=submitted_tasks_CCV)
10:51:08  + declare -A tests
10:51:08  + for test in '"${!tests[@]}"'
10:51:08  + '[' -s submitted_tasks_TS ']'
10:51:08  + for test in '"${!tests[@]}"'
10:51:08  + '[' -s submitted_tasks_CCV ']'
10:51:08  + for test in '"${!tests[@]}"'
10:51:08  + '[' -s submitted_tasks_CV ']'
10:51:08  ++ cat submitted_tasks_CV
10:51:08  + echo -e 'Task submission for **Client_Validation_Suite** successfully ended.\n```\n231128_095108:cmsbot_crab_20231128_105103\n```\n'
10:51:08  ++ date '+%Y-%m-%d %H:%M:%S'
10:51:08  + echo -e 'Finished at: 2023-11-28 10:51:08\nFind submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/557/console)'
10:51:08  + sleep 20
10:51:28  + /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#557: Test GH CRABClient using preprod REST instance and CMSSW_7_6_7 CMSSW release' -R message_taskSubmitted
10:51:30  Authenticating to Github and connecting to repo
10:51:30  Authentication succeeeded
10:51:30  Checking existing Issue curl -s 'https://api.github.com/search/issues?q=%23557%3A%20Test%20GH%20CRABClient%20using%20preprod%20REST%20instance%20and%20CMSSW_7_6_7%20CMSSW%20release+repo:dmwm/CRABServer+in:title+type:issue' | grep '"number"' | head -1 | sed -e 's|.*: ||;s|,.*||'
10:51:30  Existing Issues: 0 8024
10:51:30  Updating comment
10:51:30  + false
10:51:30  No Files Found! Triggering Skipped.
10:51:30  Triggering projects: CRABServer_CheckTestResults
10:51:30  Triggering projects: CRABServer_ClientValidation
10:51:30  No Files Found! Triggering Skipped.
10:51:30  Triggering projects: CRABServer_ClientConfigurationValidation
10:51:30  Archiving artifacts
10:51:30  Finished: SUCCESS

```

## Comment (belforte, 2023-11-30T15:12:30Z)

I submitted 2 more Jenkins for CMSW_7 and in both cases got the `  cp: cannot create regular file `CRABClient/src/python/': No such file or directory` so something is going on. I need to run a more verbose version of the script.
But will look at #8041 first

## Comment (belforte, 2023-11-30T15:14:37Z)

As far as I know this may have been happening since a very long time, when submission succeeds we do not look at log to check what exactly happened :-(

## Comment (belforte, 2023-11-30T22:27:22Z)

try with debugging added in scripts via https://github.com/dmwm/CRABServer/tree/testJenkins

* https://github.com/dmwm/CRABServer/issues/8056

## Comment (belforte, 2023-11-30T22:29:37Z)

as "feared" cloning of CRABClient failed. From https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/582/consoleText
```
++ git clone https://github.com/dmwm/CRABClient
Cloning into 'CRABClient'...
++ echo '## clone exited with RC= 128'
## clone exited with RC= 128
++ ls -ltr
total 28
drwxr-xr-x.  2 cmsbld cmsbld     6 Nov 30 23:26 artifacts
-rw-r--r--.  1 cmsbld cmsbld     0 Nov 30 23:26 message_taskSubmitted
-rw-r--r--.  1 cmsbld cmsbld  1404 Nov 30 23:26 testingConfigs
-rw-r--r--.  1 cmsbld cmsbld   390 Nov 30 23:26 message_configuration
drwxr-xr-x. 37 cmsbld cmsbld 12288 Nov 30 23:26 cms-bot
-rw-r--r--.  1 cmsbld cmsbld   370 Nov 30 23:26 parameters
drwxr-xr-x. 14 cmsbld cmsbld   237 Nov 30 23:26 CRABServer
++ ls CRABClient
ls: cannot access CRABClient: No such file or directory
```

- [ ] WHY ?

## Comment (belforte, 2023-11-30T22:44:50Z)

note that the cloning of crab server a few lines above worked !!!
https://github.com/dmwm/CRABServer/blob/19adcac695227a6cc7918dfe3a25666831c226b5/test/container/testingScripts/setupCRABClient.sh#L29-L40

could it be ` git@github.com` vs. `https://github.com/` ?

## Comment (belforte, 2023-11-30T22:54:57Z)

there indeed a problem with the `git` from CMSSW_7_6_7

1. enter the `cmssw-el6` container, all OK
```
belforte@lxplus736/~> cmssw-el6
Singularity> cd /tmp/belforte
Singularity> mkdir WD
Singularity> cd WD
Singularity> which git
/usr/bin/git
Singularity> git --version
git version 1.7.1
Singularity> 
Singularity> git clone https://github.com/dmwm/CRABClient 
Initialized empty Git repository in /tmp/belforte/WD/CRABClient/.git/
remote: Enumerating objects: 1178
[...]
Resolving deltas: 100% (6271/6271), done.
Singularity> ls
CRABClient/
```
2. setup `cmsenv`. Get a new `git` and things break
```
Singularity> cd ../CMSSW_7_6_7/
Singularity> cmsenv
Singularity> cd ../WD
Singularity> which git    
/cvmfs/cms.cern.ch/slc6_amd64_gcc493/cms/cmssw/CMSSW_7_6_7/external/slc6_amd64_gcc493/bin/git
Singularity> git --version
git version 1.8.3.1
Singularity> git clone https://github.com/dmwm/CRABClient 
Cloning into 'CRABClient'...
fatal: unable to access 'https://github.com/dmwm/CRABClient/': error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Singularity> 

OK. That's expected, default SSL is not good enough, use CMS' one (like in setupCRABClient.sh)

Singularity>     source /cvmfs/cms.cern.ch/slc6_amd64_gcc700/external/curl/7.59.0/etc/profile.d/init.sh
```
3. this time it silently does nothing !!!
```
Singularity> git clone https://github.com/dmwm/CRABClient 
Cloning into 'CRABClient'...
Singularity> echo $?
128
Singularity> ls
Singularity> 
```
Exactly like in the Jenkins log !

## Comment (belforte, 2023-11-30T23:01:28Z)

I changed the `git clone` , et voila'
It is still silent but works.

```
++ git clone git@github.com:dmwm/CRABClient
Cloning into 'CRABClient'...
Warning: Permanently added the RSA host key for IP address '140.82.121.3' to the list of known hosts.
++ echo '## clone exited with RC= 0'
## clone exited with RC= 0
++ ls -ltr
total 28
drwxr-xr-x.  2 cmsbld cmsbld     6 Nov 30 23:58 artifacts
-rw-r--r--.  1 cmsbld cmsbld     0 Nov 30 23:58 message_taskSubmitted
-rw-r--r--.  1 cmsbld cmsbld  1404 Nov 30 23:58 testingConfigs
-rw-r--r--.  1 cmsbld cmsbld   390 Nov 30 23:58 message_configuration
drwxr-xr-x. 37 cmsbld cmsbld 12288 Nov 30 23:58 cms-bot
-rw-r--r--.  1 cmsbld cmsbld   370 Nov 30 23:58 parameters
drwxr-xr-x. 14 cmsbld cmsbld   237 Nov 30 23:58 CRABServer
drwxr-xr-x.  9 cmsbld cmsbld   140 Nov 30 23:58 CRABClient
++ ls CRABClient
README.md
bin
doc
etc
scripts
setup.py
src
test
++ tree -d CRABClient
setupCRABClient.sh: line 44: tree: command not found
++ cp -v CRABServer/src/python/ServerUtilities.py CRABClient/src/python/
`CRABServer/src/python/ServerUtilities.py' -> `CRABClient/src/python/ServerUtilities.py'
++ cp -v CRABServer/src/python/RESTInteractions.py CRABClient/src/python/
`CRABServer/src/python/RESTInteractions.py' -> `CRABClient/src/python/RESTInteractions.py'
```

## Comment (belforte, 2023-11-30T23:03:08Z)

task submission still work but now it uses the correct CRABCLient.
Will put the change in `setupCRABClient` in master branch
