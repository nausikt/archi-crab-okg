# dmwm/CRABServer issue #8357: crab getoutput fails in Jenkins

State: closed
Opened: 2024-04-24T23:01:36Z
Closed: 2024-05-16T17:51:30Z
Labels: Type: Bug, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8357

## Opening post (belforte, 2024-04-24T23:01:36Z)

we have an odd and persistent error. From e.g. https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_ClientConfigurationValidation/1042/consoleText after https://github.com/dmwm/CRABServer/commit/77f421ed926cf6ac044a9258d5d59ed8ba0317ed
```

CRABClient version: v3.240416
Instance is preprod
Server base url is cmsweb-testbed.cern.ch
Command api workflow
Will use `gfal-copy` command for file transfers
Starting ChildProcess with 10 ChildProcess
Placing file 'output_1.root' in retrieval queue 
Retrieving output_1.root 
Placing file 'My_output_1.txt' in retrieval queue 
Please wait
stopchildproc() method has been called
Retrieving My_output_1.txt 
Warning: Failed retrieving My_output_1.txt
	 
Warning: Failed retrieving output_1.root
	 
The output of the transfer subprocesses follows:
	INFO 2024-04-25 00:41:09,774: 	 Retrieving output_1.root 
	DEBUG 2024-04-25 00:41:09,775: 	 Executing which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -v -K ADLER32  -T 1800  -t 60  root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240424_215409/0000/output_1.root file:///build/cmsbld/jenkins/workspace/CRABServer_ClientConfigurationValidation/crab_outputFiles/results/output_1.root
	INFO 2024-04-25 00:41:09,785: 	 Retrieving My_output_1.txt 
	DEBUG 2024-04-25 00:41:09,785: 	 Executing which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -v -K ADLER32  -T 1800  -t 60  root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240424_215409/0000/My_output_1.txt file:///build/cmsbld/jenkins/workspace/CRABServer_ClientConfigurationValidation/crab_outputFiles/results/My_output_1.txt
	DEBUG 2024-04-25 00:41:11,269: 	 Finish executing for file My_output_1.txt
	INFO 2024-04-25 00:41:11,269: 	 Warning: Failed retrieving My_output_1.txt
	INFO 2024-04-25 00:41:11,269: 	 	 
	DEBUG 2024-04-25 00:41:11,271: 	 Full stderr follows:
	TLS: Unable to create TLS context; invalid private key.
	TLS: 47882433451776:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
	
	
	DEBUG 2024-04-25 00:41:11,353: 	 Finish executing for file output_1.root
	INFO 2024-04-25 00:41:11,354: 	 Warning: Failed retrieving output_1.root
	INFO 2024-04-25 00:41:11,354: 	 	 
	DEBUG 2024-04-25 00:41:11,355: 	 Full stderr follows:
	TLS: Unable to create TLS context; invalid private key.
	TLS: 47191492134656:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
```

## Comment (belforte, 2024-04-24T23:04:10Z)

The odd thing that started since a week or so. Can not be a simple bug in X509_USER_PROXY handling in our test.

## Comment (belforte, 2024-04-25T20:00:01Z)

I tried to also set X509_USER_PROXY, still same error.
I tried to log on lxplus7 first, then start `cmssw-el8` and gfal-copy works.

Could this be soemthing wrong in the `cms-dmwm-cc7-060 ` node where this runs ?

Can we run on an EL8 node instead ?

## Comment (belforte, 2024-04-25T20:00:18Z)

I ran the test on El9, still same problem https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ClientConfigurationValidation/1045/consoleText

## Comment (belforte, 2024-04-25T20:00:36Z)

hm...  I ran a simple test and i seems that `gfal-copy` works in spite of the nasty-looking TLS error !
https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRAB_Stefano-1/24/console

```
21:33:32 + cat myTest.sh
21:33:32 set -x
21:33:32 echo /tmp/x509up_u501
21:33:32 which gfal-copy
21:33:32 gfal-copy root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240425_133946/0000/output_1.root ./out.root
21:33:32 ls -l out.root
21:33:32 rm out.root
21:33:32 + echo ==EXECUTE+++
21:33:32 ==EXECUTE+++
21:33:32 + /cvmfs/cms.cern.ch/common/cmssw-el8 -- ./myTest.sh
21:33:32 +++ echo /tmp/x509up_u501
21:33:32 /tmp/x509up_u501
21:33:32 +++ which gfal-copy
21:33:32 /usr/bin/gfal-copy
21:33:32 +++ gfal-copy root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240425_133946/0000/output_1.root ./out.root
21:33:32 TLS: Unable to create TLS context; invalid private key.
21:33:32 TLS: 22860391716608:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
21:33:32 
21:33:32 Copying 635045 bytes root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240425_133946/0000/output_1.root => file:///build/cmsbld/jenkins/workspace/CRAB_Stefano-1/out.root
21:33:32 +++ ls -l out.root
21:33:32 -rw-r--r--. 1 cmsbld cmsbld 635045 Apr 25 21:33 out.root
21:33:32 +++ rm out.root
```
I also verified that gfal-copy exit code is 0.

Question then is why CRABClient printed
```
Warning: Failed retrieving My_output_1.txt
	 
Warning: Failed retrieving output_1.root
```

## Comment (belforte, 2024-04-25T22:14:09Z)

I have added in the test dump of crab.log https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ClientConfigurationValidation/1049/consoleText
The task name is  `240425_202013:cmsbot_crab_outputFiles`
Still not enough details to tell what's going on
```

DEBUG 2024-04-25 22:02:43.705 UTC: 	 Instance is preprod
DEBUG 2024-04-25 22:02:43.705 UTC: 	 Server base url is cmsweb-testbed.cern.ch
DEBUG 2024-04-25 22:02:43.705 UTC: 	 Command api workflow
INFO 2024-04-25 22:02:43.711 UTC: 	 Will use `gfal-copy` command for file transfers
DEBUG 2024-04-25 22:02:43.749 UTC: 	 Starting ChildProcess with 10 ChildProcess
INFO 2024-04-25 22:02:43.793 UTC: 	 Placing file 'output_1.root' in retrieval queue 
INFO 2024-04-25 22:02:43.817 UTC: 	 Placing file 'My_output_1.txt' in retrieval queue 
INFO 2024-04-25 22:02:43.817 UTC: 	 Please wait
DEBUG 2024-04-25 22:02:43.817 UTC: 	 stopchildproc() method has been called
DEBUG 2024-04-25 22:03:45.245 UTC: 	 The output of the transfer subprocesses follows:
DEBUG 2024-04-25 22:03:45.245 UTC: 	 	INFO 2024-04-26 00:02:43,802: 	 Retrieving output_1.root 
DEBUG 2024-04-25 22:03:45.245 UTC: 	 	DEBUG 2024-04-26 00:02:43,802: 	 Executing which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -v -K ADLER32  -T 1800  -t 60  root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240425_202013/0000/output_1.root file:///build/cmsbld/jenkins/workspace/CRABServer_ClientConfigurationValidation/crab_outputFiles/results/output_1.root
DEBUG 2024-04-25 22:03:45.245 UTC: 	 	INFO 2024-04-26 00:02:43,819: 	 Retrieving My_output_1.txt 
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	DEBUG 2024-04-26 00:02:43,819: 	 Executing which scram >/dev/null 2>&1 && eval `scram unsetenv -sh`; gfal-copy -v -K ADLER32  -T 1800  -t 60  root://cms-xrd-global.cern.ch//store/user/cmsbot/GenericTTbar/CrabAutoTest_outputFiles/240425_202013/0000/My_output_1.txt file:///build/cmsbld/jenkins/workspace/CRABServer_ClientConfigurationValidation/crab_outputFiles/results/My_output_1.txt
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	DEBUG 2024-04-26 00:02:45,170: 	 Finish executing for file My_output_1.txt
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	INFO 2024-04-26 00:02:45,170: 	 Warning: Failed retrieving My_output_1.txt
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	INFO 2024-04-26 00:02:45,171: 	 	 
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	DEBUG 2024-04-26 00:02:45,173: 	 Full stderr follows:
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	TLS: Unable to create TLS context; invalid private key.
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	TLS: 46941743392512:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	DEBUG 2024-04-26 00:02:45,181: 	 Finish executing for file output_1.root
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	INFO 2024-04-26 00:02:45,182: 	 Warning: Failed retrieving output_1.root
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	INFO 2024-04-26 00:02:45,182: 	 	 
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	DEBUG 2024-04-26 00:02:45,183: 	 Full stderr follows:
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	TLS: Unable to create TLS context; invalid private key.
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	TLS: 47836990510848:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	
DEBUG 2024-04-25 22:03:45.246 UTC: 	 	
INFO 2024-04-25 22:03:45.248 UTC: 	 For more details about the errors please open the logfile
INFO 2024-04-25 22:03:45.248 UTC: 	 No file retrieved
```

## Comment (belforte, 2024-04-25T22:20:54Z)

OTOH `crab getoutput` on same task has no problem and no TLS message even if I run it inside the singularity container.

## Comment (belforte, 2024-04-26T08:26:40Z)

crab client reports `Failed retrieving ` because the `error` string in `TLS: 47836990510848:error:0B080074:x509 certificate ...`
triggers this line:
https://github.com/dmwm/CRABClient/blob/d4b4151f668ba23cb069569e9613c83776630f6b/src/python/CRABClient/Commands/remote_copy.py#L356

We can change to check `gfal` exit code first and look for telling strings to report only if exit code is non 0.

Yet I am disturbed that the `TLS` message can not be reproduced in the singularity container started from lxplus*.
The timing of the change suggests that something is wrong with the new Jenkinis nodes.

## Comment (belforte, 2024-04-30T14:46:36Z)

I have sent a mail to Shahzad asking for advice/solution

## Comment (belforte, 2024-05-16T17:51:30Z)

No reply from Shahzad. And now we have a fix in CrabClient. I am closing
