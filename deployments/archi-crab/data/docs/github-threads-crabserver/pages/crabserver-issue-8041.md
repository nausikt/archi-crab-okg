# dmwm/CRABServer issue #8041: Test GH CRABClient using CMSSW_10_1_0 fails to submit

State: closed
Opened: 2023-11-30T11:21:24Z
Closed: 2023-11-30T18:18:25Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8041

## Opening post (cmsdmwmbot, 2023-11-30T11:21:24Z)

**Tests started for following configuration:**


**Configuration:**

 - CRABClient_version: **GH**
- REST_Instance: **preprod**
- CMSSW_release: **CMSSW_10_1_0**
- SCRAM_ARCH: **slc7_amd64_gcc630**
- CRABServer_tag: **HEAD**

**Tests started:**

- [ ] Client_Validation
Started at: 2023-11-30 12:21:23
Link to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/567/)

## Comment (belforte, 2023-11-30T11:35:21Z)

submission failed with the dreaded "can not import past" in python3 even if it was using singularity. I tried interactively and import past works.... pff.. let's simply try again

## Comment (belforte, 2023-11-30T11:38:15Z)

submission log is in https://github.com/dmwm/CRABServer/issues/8042 (there is likely some confusion in our Jenkins and now that I submitted may tests one after the other many comments ended up as new issues in GH)
and pasted here
```
Started by user belforte
Running as SYSTEM
[EnvInject] - Loading node environment variables.
Building remotely on cms-dmwm-cc7-050 (cms-dmwm-cc7 no_label) in workspace /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
[WS-CLEANUP] Deleting project workspace...
[WS-CLEANUP] Deferred wipeout is used...
[WS-CLEANUP] Done
New run name is '#567; CV=true; TS=false; CCV=false; CRABClient=GH; REST=preprod'
[CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins2403995827920366296.sh
[CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins4394745231761308033.sh
+ '[' Xtrue '!=' Xtrue ']'
[CRABServer_ExecuteTests] $ /bin/bash -xe /tmp/jenkins4042921176645304667.sh
+ echo '(DEBUG) client:'
(DEBUG) client:
+ echo '(DEBUG)   \- CRABClient_version: GH'
(DEBUG)   \- CRABClient_version: GH
+ echo '(DEBUG)   \- CRABServer_tag: HEAD'
(DEBUG)   \- CRABServer_tag: HEAD
+ echo '(DEBUG) REST:'
(DEBUG) REST:
+ echo '(DEBUG)   \- REST_Instance: preprod'
(DEBUG)   \- REST_Instance: preprod
+ echo '(DEBUG) CMSSW:'
(DEBUG) CMSSW:
+ echo '(DEBUG)   \- CMSSW_release: CMSSW_10_1_0'
(DEBUG)   \- CMSSW_release: CMSSW_10_1_0
+ echo '(DEBUG) test parameters:'
(DEBUG) test parameters:
+ echo '(DEBUG)   \- Client_Validation_Suite: true'
(DEBUG)   \- Client_Validation_Suite: true
+ echo '(DEBUG)   \- Client_Configuration_Validation: false'
(DEBUG)   \- Client_Configuration_Validation: false
+ echo '(DEBUG)   \- Check_Publication_Status: No'
(DEBUG)   \- Check_Publication_Status: No
+ echo '(DEBUG)   \- Repo_GH_Issue: dmwm/CRABServer'
(DEBUG)   \- Repo_GH_Issue: dmwm/CRABServer
+ echo '(DEBUG)   \- Repo_Testing_Scripts: dmwm/CRABServer'
(DEBUG)   \- Repo_Testing_Scripts: dmwm/CRABServer
+ echo '(DEBUG)   \- Branch_Testing_Scripts: master'
(DEBUG)   \- Branch_Testing_Scripts: master
+ echo '(DEBUG)   \- Test_Docker_Image: registry.cern.ch/cmscrab/crabtesting:231009'
(DEBUG)   \- Test_Docker_Image: registry.cern.ch/cmscrab/crabtesting:231009
+ echo '(DEBUG) end'
(DEBUG) end
+ rm -rf /tmp/crabTestConfig/
+ docker system prune -af
Total reclaimed space: 0B
+ mkdir artifacts
+ touch message_taskSubmitted
+ ls -l /cvmfs/cms-ib.cern.ch/latest/
total 79
drwxr-xr-x. 2 cvmfs cvmfs     6 Nov 26 02:21 bin
-rw-r--r--. 1 cvmfs cvmfs 52781 Jan 19  2022 bootstrap.sh
drwxr-xr-x. 2 cvmfs cvmfs     6 Nov 27 03:56 bootstraptmp
drwxr-xr-x. 2 cvmfs cvmfs   242 Nov 27 04:07 cmsmon
-rwxr-xr-x. 1 cvmfs cvmfs  1558 Nov 26 01:59 cmsset_default.csh
-rwxr-xr-x. 1 cvmfs cvmfs  1530 Nov 26 01:59 cmsset_default.sh
drwxr-xr-x. 2 cvmfs cvmfs    20 Nov 28 11:54 common
lrwxrwxrwx. 1 cvmfs cvmfs     6 Nov 26 01:59 cvmfs -> /cvmfs
drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 26 01:22 el8_amd64_gcc10
drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 29 23:54 el8_amd64_gcc11
drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 30 09:38 el8_amd64_gcc12
drwxr-xr-x. 8 cvmfs cvmfs    17 Aug  3 22:32 el9_amd64_gcc11
drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 29 23:50 el9_amd64_gcc12
drwxr-xr-x. 8 cvmfs cvmfs    21 Nov 26 02:12 etc
-rw-r--r--. 1 cvmfs cvmfs 11358 Nov 26 01:59 LICENSE
drwxr-xr-x. 2 cvmfs cvmfs    55 Nov 27 03:56 logs
drwxr-xr-x. 7 cvmfs cvmfs    17 Nov 26 02:12 share
lrwxrwxrwx. 1 cvmfs cvmfs    30 Nov 30 11:23 SITECONF -> /cvmfs/cms-ib.cern.ch/SITECONF
drwxr-xr-x. 9 cvmfs cvmfs    17 Nov 26 00:37 slc6_amd64_gcc472
drwxr-xr-x. 9 cvmfs cvmfs    88 Nov 26 00:31 slc6_amd64_gcc481
drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:30 slc6_amd64_gcc530
drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:40 slc6_amd64_gcc630
drwxr-xr-x. 8 cvmfs cvmfs    66 Mar 29  2022 slc7_amd64_gcc10
drwxr-xr-x. 8 cvmfs cvmfs    17 Aug  3 22:36 slc7_amd64_gcc11
drwxr-xr-x. 8 cvmfs cvmfs    44 Nov 29 23:54 slc7_amd64_gcc12
drwxr-xr-x. 8 cvmfs cvmfs    77 Nov 26 00:28 slc7_amd64_gcc530
drwxr-xr-x. 8 cvmfs cvmfs    77 Dec 18  2019 slc7_amd64_gcc630
drwxr-xr-x. 8 cvmfs cvmfs    77 Nov  9 16:08 slc7_amd64_gcc700
+ git clone https://github.com/cms-sw/cms-bot
Cloning into 'cms-bot'...
+ voms-proxy-init -rfc -voms cms -valid 192:00
Contacting voms2.cern.ch:15002 [/DC=ch/DC=cern/OU=computers/CN=voms2.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u501.

Your proxy is valid until Fri Dec 08 12:21:21 CET 2023
+ export X509_USER_CERT=/home/cmsbld/.globus/usercert.pem
+ X509_USER_CERT=/home/cmsbld/.globus/usercert.pem
+ export X509_USER_KEY=/home/cmsbld/.globus/userkey.pem
+ X509_USER_KEY=/home/cmsbld/.globus/userkey.pem
++ voms-proxy-info -path
+ export PROXY=/tmp/x509up_u501
+ PROXY=/tmp/x509up_u501
+ voms-proxy-info -all
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=209397420
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC3820 compliant impersonation proxy
strength  : 2048
path      : /tmp/x509up_u501
timeleft  : 191:59:57
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
issuer    : /DC=ch/DC=cern/OU=computers/CN=voms2.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
timeleft  : 191:59:57
uri       : voms2.cern.ch:15002

+ export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
+ PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
+ export ERR=false
+ ERR=false
++ pwd
+ export WORK_DIR=/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
+ WORK_DIR=/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
+ export CMSSW_release=CMSSW_10_1_0
+ CMSSW_release=CMSSW_10_1_0
+ curl -s -O https://raw.githubusercontent.com/dmwm/CRABServer/master/test/testingConfigs
++ grep 'CMSSW_release=CMSSW_10_1_0;' testingConfigs
+ CONFIG_LINE='CMSSW_release=CMSSW_10_1_0;SCRAM_ARCH=slc7_amd64_gcc630;inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM;master=no;'
++ echo 'CMSSW_release=CMSSW_10_1_0;SCRAM_ARCH=slc7_amd64_gcc630;inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM;master=no;'
++ tr ';' '\n'
++ sed 's|SCRAM_ARCH=||'
++ grep SCRAM_ARCH
+ export SCRAM_ARCH=slc7_amd64_gcc630
+ SCRAM_ARCH=slc7_amd64_gcc630
++ echo 'CMSSW_release=CMSSW_10_1_0;SCRAM_ARCH=slc7_amd64_gcc630;inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM;master=no;'
++ tr ';' '\n'
++ grep inputDataset
++ sed 's|inputDataset=||'
+ export inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM
+ inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM
++ echo slc7_amd64_gcc630
++ cut -d_ -f 1
++ tail -c 2
+ export singularity=7
+ singularity=7
+ echo SCRAM_ARCH=slc7_amd64_gcc630
+ echo inputDataset=/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM
+ echo singularity=7
+ echo Repo_GH_Issue=dmwm/CRABServer
+ echo Repo_Testing_Scripts=dmwm/CRABServer
+ echo Branch_Testing_Scripts=master
+ echo Test_Docker_Image=registry.cern.ch/cmscrab/crabtesting:231009
+ echo -e '**Tests started for following configuration:**\n\n'
+ echo -e '**Configuration:**\n\n - CRABClient_version: **GH**\n- REST_Instance: **preprod**\n- CMSSW_release: **CMSSW_10_1_0**\n- SCRAM_ARCH: **slc7_amd64_gcc630**'
+ '[' XGH == XGH ']'
+ echo -e '- CRABServer_tag: **HEAD**'
+ echo -e '\n**Tests started:**\n'
+ '[' Xtrue == Xtrue ']'
+ echo -e '- [ ] Client_Validation'
+ '[' Xfalse == Xtrue ']'
+ '[' Xfalse == Xtrue ']'
++ date '+%Y-%m-%d %H:%M:%S'
+ echo -e 'Started at: 2023-11-30 12:21:23\nLink to the [job](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/567/) '
+ issueTitle='#567: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release'
+ /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#567: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release' -R message_configuration
Authenticating to Github and connecting to repo
Authentication succeeeded
Checking existing Issue curl -s 'https://api.github.com/search/issues?q=%23567%3A%20Test%20GH%20CRABClient%20using%20preprod%20REST%20instance%20and%20CMSSW_10_1_0%20CMSSW%20release+repo:dmwm/CRABServer+in:title+type:issue' | grep '"number"' | head -1 | sed -e 's|.*: ||;s|,.*||'
Existing Issues: 0 
Creating issue request
+ echo 'issueTitle=#567: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release'
+ '[' X7 == X6 ']'
+ '[' X7 == X7 ']'
+ echo 'Starting singularity 7 container.'
Starting singularity 7 container.
+ git clone https://github.com/dmwm/CRABServer
Cloning into 'CRABServer'...
+ cd CRABServer
++ git rev-parse --abbrev-ref HEAD
+ [[ master != master ]]
+ cd test/container/testingScripts
+ scramprefix=cc7
+ '[' X7 == X6 ']'
+ '[' X7 == X7 ']'
+ scramprefix=el7
+ '[' X7 == X8 ']'
+ /cvmfs/cms.cern.ch/common/cmssw-el7 -- ./taskSubmission.sh
WARNING: In non-interactive mode release checks e.g. deprecated releases, production architectures are disabled.
>> Local Products Rules ..... started
>> Local Products Rules ..... done
>> Building CMSSW version CMSSW_10_1_0 ----
>> Subsystem BigProducts built
gmake[1]: Entering directory '/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_10_1_0'
>> Local Products Rules ..... started
>> Local Products Rules ..... done
>> Creating project symlinks
>> Done python_symlink
>> Compiling python modules cfipython/slc7_amd64_gcc630
>> Compiling python modules python
>> All python modules compiled
>> Plugins of all types refreshed.
>> Done generating edm plugin poisoned information
gmake[1]: Leaving directory '/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABServer/test/container/testingScripts/CMSSW_10_1_0'
Your branch is up-to-date with 'origin/master'.
Cloning into 'CRABClient'...
Traceback (most recent call last):
  File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/bin/crab.py", line 17, in <module>
    from ServerUtilities import FEEDBACKMAIL
  File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/ServerUtilities.py", line 31, in <module>
    from past.builtins import basestring
ModuleNotFoundError: No module named 'past'

Starting task submission for Client Validation testing.


Submitting file: ./crabConfiguration.py
Traceback (most recent call last): File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/bin/crab.py", line 17, in <module> from ServerUtilities import FEEDBACKMAIL File "/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/ServerUtilities.py", line 31, in <module> from past.builtins import basestring ModuleNotFoundError: No module named 'past'
+ export ERR=true
+ ERR=true
+ cd /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests
+ mv /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/artifacts/failed_tasks /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/
+ true
+ echo -e 'Something went wrong during task submission. Find submission log [here](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ExecuteTests/567/console). None of the downstream jobs were triggered.'
+ sleep 20
+ /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#567: Test GH CRABClient using preprod REST instance and CMSSW_10_1_0 CMSSW release' -R message_taskSubmitted
Authenticating to Github and connecting to repo
Authentication succeeeded
Checking existing Issue curl -s 'https://api.github.com/search/issues?q=%23567%3A%20Test%20GH%20CRABClient%20using%20preprod%20REST%20instance%20and%20CMSSW_10_1_0%20CMSSW%20release+repo:dmwm/CRABServer+in:title+type:issue' | grep '"number"' | head -1 | sed -e 's|.*: ||;s|,.*||'
Existing Issues: 0 
Creating issue request
+ true
+ exit 1
Build step 'Execute shell' marked build as failure
Archiving artifacts
Finished: FAILURE

```

## Comment (belforte, 2023-11-30T15:38:01Z)

hmm....
I see the dreaded
```bash
export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared 
```
near the top of bash script for execute_tests.

I suspect that this PYTHONPATH is passed inside the singularity container and ends up in messing things. I even remember changing this rather recenlty in "some Jenkins test", but can't find a trace of this in GH closed issues and looking at current scripts in Jenkins ExecuteTests, CheckTestResult, ClientValidation and CrabConfiogurationValidation I always see it near the top.
IIUC thas is only needed for the GH hooks, i.e. at the beginning and end of ExecuteTests and only at the end for the others.
Making some tests ....

## Comment (belforte, 2023-11-30T17:04:21Z)

**RATS**

```
belforte@lxplus736/~> /cvmfs/cms.cern.ch/slc7_amd64_gcc630/external/python3/3.6.4-omkpbe/bin/python3
Python 3.6.8 (default, Nov 14 2023, 16:29:52) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import past
>>> past.__file__
'/afs/cern.ch/user/b/belforte/.local/lib/python3.6/site-packages/past/__init__.py'
>>> 
```

when I test I get past from my pip env :-(
How can I disable that in a reversible way to test things properly ?

## Comment (belforte, 2023-11-30T17:11:31Z)

Yeah... I knew and forgot `mv .local DotLocal` 
With that the problem is easily reproduced.

## Comment (belforte, 2023-11-30T18:07:25Z)

OK. So this is simpler than it looked. For CMSSW_10_1_0 `past` is not part of the CMSSW python build.
Means that we can't support python3 for all CMSSW_10
(for CMSSW_9 and earlier we use python2)

## Comment (belforte, 2023-11-30T18:10:58Z)

`import past` starts to work with CMSSW_10_2_0
Which also matches e.g. what Kevin Pedro wrote in  http://cms-sw.github.io/venv.html about full support for python3 in CMSSW

## Comment (belforte, 2023-11-30T18:18:25Z)

I will  close this and open a new issue about moving use of python3 threshold from CMSSW_10 to CMSSW_10_2
