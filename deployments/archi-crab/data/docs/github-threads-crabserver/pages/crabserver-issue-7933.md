# dmwm/CRABServer issue #7933: crab checkwrite test in Jenkins fails (silently)

State: closed
Opened: 2023-10-11T16:27:17Z
Closed: 2023-10-14T08:52:14Z
Labels: Status: In Progress, Priority: TOP, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7933

## Opening post (belforte, 2023-10-11T16:27:17Z)

see below for details. There are two things here
- [x] make `crab checkwrite` in Jenkins work (now fails on Jenkins side)
- [x] make the test report failure when it does not (in case problem is in CRABClient) - moved to https://github.com/dmwm/CRABClient/issues/5223

@mapellidario and myself found that in Jenkins ClientValidation was only executing the minimal `submit` and `status` tests when running on CC8. That was meant to be only for SL6. So we modified [CRABServer_ClientValidation](https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ClientValidation/) to execute full test suite on CC8 as well.

But when submitted I found that `chekwrite` test fails with a problem in contacting Rucio [1] and, worst, the test is still declared successful.
I need working client tests in order to validate changes that I am doing to CRABClient to import Rucio client API. So need to fix this a first priority.

Fixing the test to report error may be "as simple as modify CRABClient to exit with an exception in this case".
Fixing the problem looks hard because:
 - if I run this in `cmssw-cc8` singularity container myself, it works
 - the robot certificate is known to Rucio, since this test works for SL7
 - it is the same error which I got inside Jenkins with even simpler tests when trying to test new client which has `from rucio.Client import client; rucio=Client()`
 - in current (even dev) CRABClient the call to Rucio is executed in a subprocess after a `scram unsetenv`

[1]
```

17:10:54 TEST_COMMAND: crab checkwrite  --site=T2_CH_CERN  --proxy=/tmp/x509up_u501  
17:10:59 TEST_RESULT: OK                                                                                 
17:10:59 TEST_MESSAGE:
17:10:59 BEWARE: this is the development version of CRAB Client.
17:10:59 Be sure to have a good reason for using it
17:10:59 
17:10:59 Will check write permission in the default location /store/user/<username>
17:10:59 Validating LFN /store/user/cmsbot...
17:10:59 LFN /store/user/cmsbot is valid.
17:10:59 Will use `gfal-copy`, `gfal-rm` commands for checking write permissions
17:10:59 Will check write permission in /store/user/cmsbot on site T2_CH_CERN
17:10:59 PFN lookup failed
17:10:59   Stderr:
17:10:59     ^[[31;1m2023-10-11 17:10:59,382	ERROR	ConnectionError: [Errno 21] Is a directory^[[0m
17:10:59     ^[[31;1m2023-10-11 17:10:59,390	ERROR	ConnectionError: [Errno 21] Is a directory^[[0m
17:10:59     ^[[31;1m2023-10-11 17:10:59,397	ERROR	ConnectionError: [Errno 21] Is a directory^[[0m
17:10:59     Traceback (most recent call last):
17:10:59       File "/tmp/crab_lfn2pfn-lkqdyxfl.py", line 3, in <module>
17:10:59         client = Client()
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/client.py", line 77, in __init__
17:10:59         super(Client, self).__init__(**args)
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/baseclient.py", line 282, in __init__
17:10:59         self.__authenticate()
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/baseclient.py", line 929, in __authenticate
17:10:59         self.__get_token()
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/baseclient.py", line 822, in __get_token
17:10:59         if not self.__get_token_x509():
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/baseclient.py", line 681, in __get_token_x509
17:10:59         result = self._send_request(url, get_token=True, cert=cert)
17:10:59       File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel8/py3/current/lib/python3.6/site-packages/rucio/client/baseclient.py", line 436, in _send_request
17:10:59         raise ServerConnectionException
17:10:59     rucio.common.exception.ServerConnectionException: Cannot connect to the Rucio server.
17:10:59     
17:10:59 ____________
17:10:59 
```

## Comment (belforte, 2023-10-11T21:18:29Z)

I wrote a very simple Rucio testing script [1]  , and it runs happily on both cmssw-cc7 and cmssw-el8 singularity containers. But I had to make sure `RUCIO_ACCOUNT=cmsbot` while the test runs as user `cmsbld`. This should be a problem in CRABClient though, since e.g. checkwrite picks RUCIO_ACCOUNT from the username obtained from the proxy.
Also in that case the error is the clear
```
2023-10-11 23:17:53,078	ERROR	Cannot authenticate.
Details: Cannot authenticate to account cmsbot with given credentials
2023-10-11 23:17:53,078	ERROR	Please verify that your proxy is still valid and renew it if needed.
```
not the `Cannot connect to the Rucio server.` above

I am  still puzzled.

[1]
```bash
#!/bin/bash
voms-proxy-info
echo "++ Who am I ?"
whoami
id
echo "++ source /cvmfs/cms.cern.ch/rucio/setup-py3.sh"
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh

echo "++ force RUCIO_ACCOUNT to cmsbot"
export RUCIO_ACCOUNT=`whoami`
export RUCIO_ACCOUNT=cmsbot
echo "++ RUCIO_ACCOUNT= $RUCION_ACCOUNT"

echo "++ test rucio whoami"
rucio whoami && echo SUCCESS
echo ""
```

## Comment (belforte, 2023-10-11T22:02:37Z)

I found that things work after removing this line from the [Jenkins script in ClientValidation](https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ClientValidation/configure)
```bash
export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared 
```

purpose of that line is indeed mysterious and Daina is not around anymore to ask.
But I am not so surprised that mixing those python modules in may have confused Rucio client !

Will try some cleaning and of course validation

this is also worrysome
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/test/container/testingScripts/setupCRABClient.sh#L10
But maybe the idea there was simply to always test client in IB. I need to understand and document. Since it conflicts with comment a few line above
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/test/container/testingScripts/setupCRABClient.sh#L6

## Comment (belforte, 2023-10-11T22:05:54Z)

testing above hypothesis in https://github.com/dmwm/CRABServer/issues/7934

## Comment (belforte, 2023-10-12T07:34:52Z)

with this removed
```bash
export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared 
```
`crab checkwrite` is now successful  [1]

Bu test fails to update GH issue with
```
00:27:35 + /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#506: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release' -R message_CVResult
00:27:35 Traceback (most recent call last):
00:27:35   File "/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/cms-bot/create-gh-issue.py", line 3, in <module>
00:27:35     from github import Github
00:27:35 ImportError: No module named github
00:27:35 Build step 'Execute shell' marked build as failure
```

so we know why that line was needed.
Let's simply move it at the end and try again

[1]
```
00:26:19 ____________
00:26:19 TEST_COMMAND: crab checkusername  --proxy=/tmp/x509up_u501  
00:26:21 TEST_RESULT: OK                                                                                 
00:26:21 TEST_MESSAGE:
00:26:21 Username is: cmsbot
00:26:21 ____________
00:26:21 
00:26:21 ____________
00:26:21 TEST_COMMAND: crab checkwrite  --site=T2_CH_CERN  --proxy=/tmp/x509up_u501  
00:26:27 TEST_RESULT: OK                                                                                 
00:26:27 TEST_MESSAGE:
00:26:27 Will check write permission in the default location /store/user/<username>
00:26:27 Validating LFN /store/user/cmsbot...
00:26:27 LFN /store/user/cmsbot is valid.
00:26:27 Will use `gfal-copy`, `gfal-rm` commands for checking write permissions
00:26:27 Will check write permission in /store/user/cmsbot on site T2_CH_CERN
00:26:27 Will use PFN: davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/crab3checkwrite_20231012_002622.tmp
00:26:27 
00:26:27 Attempting to create (dummy) directory crab3checkwrite_20231012_002622 and copy (dummy) file crab3checkwrite_20231012_002622.tmp to /store/user/cmsbot
00:26:27 
00:26:27 Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -p -v -t 180 file:///build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/crab3checkwrite_20231012_002622.tmp 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/crab3checkwrite_20231012_002622.tmp'
00:26:27 Please wait...
00:26:27 
00:26:27 Successfully created directory crab3checkwrite_20231012_002622 and copied file crab3checkwrite_20231012_002622.tmp to /store/user/cmsbot
00:26:27 
00:26:27 Attempting to delete file davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/crab3checkwrite_20231012_002622.tmp
00:26:27 
00:26:27 Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-rm -v -t 180 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/crab3checkwrite_20231012_002622.tmp'
00:26:27 Please wait...
00:26:27 
00:26:27 Successfully deleted file davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/crab3checkwrite_20231012_002622.tmp
00:26:27 
00:26:27 Attempting to delete directory davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/
00:26:27 
00:26:27 Executing command: which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-rm -r -v -t 180 'davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/'
00:26:27 Please wait...
00:26:27 
00:26:27 Successfully deleted directory davs://eoscms.cern.ch:443/eos/cms/store/user/cmsbot/crab3checkwrite_20231012_002622/
00:26:27 
00:26:27 Checkwrite Result:
00:26:27 Success: Able to write in /store/user/cmsbot on site T2_CH_CERN
00:26:27 ____________
00:26:27 
```

## Comment (belforte, 2023-10-12T08:06:10Z)

new test in https://github.com/dmwm/CRABServer/issues/7935

## Comment (belforte, 2023-10-12T08:09:02Z)

everythin fine at last !
Reminder: this is CMSSW_13_0_2 on el8

```
10:03:54 + echo -e '**Test:** Client validation\n**Result:** SUCCEEDED\n**Finished at:** 2023-10-12 10:03:54\n**Test log:** [https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/390/console\n**All](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/390/console/n**All) executed commands:** [https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/390//artifact/client-validation.log/*view*/\n**Message:**](https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientValidation/390//artifact/client-validation.log/*view*//n**Message:**) All commands were executed successfully.\n'
10:03:54 + export PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
10:03:54 + PYTHONPATH=/cvmfs/cms-ib.cern.ch/jenkins-env/python/shared
10:03:54 + /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/cms-bot/create-gh-issue.py -r dmwm/CRABServer -t '#507: Test prod CRABClient using preprod REST instance and CMSSW_13_0_2 CMSSW release' -R message_CVResult
10:03:57 Authenticating to Github and connecting to repo
10:03:57 Authentication succeeeded
10:03:57 Checking existing Issue curl -s 'https://api.github.com/search/issues?q=%23507%3A%20Test%20prod%20CRABClient%20using%20preprod%20REST%20instance%20and%20CMSSW_13_0_2%20CMSSW%20release+repo:dmwm/CRABServer+in:title+type:issue' | grep '"number"' | head -1 | sed -e 's|.*: ||;s|,.*||'
10:03:57 Existing Issues: 0 7935
10:03:57 Updating comment
10:03:57 + false
10:03:57 New run name is '#390 CRABServer_ClientValidation CRABClient=prod; REST=preprod'
10:03:57 Archiving artifacts
10:03:58 [WS-CLEANUP] Deleting project workspace...
10:03:58 [WS-CLEANUP] Deferred wipeout is used...
10:03:58 [WS-CLEANUP] done
10:03:58 Finished: SUCCESS
```

## Comment (belforte, 2023-10-12T08:24:40Z)

now, make sure SL7 still works as well:  https://github.com/dmwm/CRABServer/issues/7936

## Comment (belforte, 2023-10-12T09:03:50Z)

OK. Nothing broken.
Next step is to make sure that when `chckwrite` fails, it is reported as such
