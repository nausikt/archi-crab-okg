# dmwm/CRABClient pull request #5232: Adapt checkwrite to rucio fix 5203

State: closed
Opened: 2023-10-18T22:24:30Z
Closed: 2023-10-19T19:31:24Z
Merged: 2023-10-19T19:31:24Z
URL: https://github.com/dmwm/CRABClient/pull/5232

## Opening post (belforte, 2023-10-18T22:24:30Z)

(no text)

## Comment (cmsdmwmbot, 2023-10-18T22:27:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 42 warnings and errors that must be fixed
   * 7 warnings
   * 157 comments to review
 * Pycodestyle check: succeeded
   * 166 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/952/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-18T22:28:45Z)

I believe that functionality is there, messages can (as always) be improved (color ? uppercase ? bells ?)
But we can address that as people get some experience.

example of outputs with these changes

with a CMSSW_10
```
belforte@lxplus764/belforte> crab checkwrite --site T3_IT_Trieste --lfn /store/user/rucio/belforte
Validating LFN /store/user/rucio/belforte...
LFN /store/user/rucio/belforte is valid.
Rucio client not available with this CMSSW version. Can not check
Command checkwrite failed
belforte@lxplus764/belforte> 
```

with a moder CMSSW
```

belforte@lxplus810/bot> crab checkwrite --site T3_IT_Trieste --lfn /store/user/rucio/belforte
Rucio client intialized for account belforte
Validating LFN /store/user/rucio/belforte...
LFN /store/user/rucio/belforte is valid.
you have 9 GB available as Rucio quota at site T3_IT_Trieste
This is very little and although CRAB will submit, stageout may fail. Please cleanup
FYI this is your Rucio quota situation (rounded to GBytes = 10^9 Bytes)
                Site     Quota      Used      Free
       T3_IT_Trieste        10         0        10
          T2_CH_CERN       100         3        96
belforte@lxplus810/bot> 


belforte@lxplus810/bot> crab checkwrite --site T2_CH_CERN --lfn /store/user/rucio/belforte

Rucio client intialized for account belforte
Validating LFN /store/user/rucio/belforte...
LFN /store/user/rucio/belforte is valid.
you have 90 GB available as Rucio quota at site T2_CH_CERN
You can use this site for Rucio-based ASO
FYI this is your Rucio quota situation (rounded to GBytes = 10^9 Bytes)
                Site     Quota      Used      Free
       T3_IT_Trieste        10         0        10
          T2_CH_CERN       100         3        96
belforte@lxplus810/bot> 
belforte@lxplus810/bot> 

belforte@lxplus810/bot> crab checkwrite --site T2_DE_DESY --lfn /store/user/rucio/belforte
Rucio client intialized for account belforte
Validating LFN /store/user/rucio/belforte...
LFN /store/user/rucio/belforte is valid.
You do not have any Rucio quota at site T2_DE_DESY
FYI this is your Rucio quota situation (rounded to GBytes = 10^9 Bytes)
                Site     Quota      Used      Free
       T3_IT_Trieste        10         0        10
          T2_CH_CERN       100         3        96
Command checkwrite failed
belforte@lxplus810/bot> 

elforte@lxplus810/bot> crab checkwrite --site T2_DE_NOPE --lfn /store/user/rucio/belforte
Rucio client intialized for account belforte
Validating LFN /store/user/rucio/belforte...
LFN /store/user/rucio/belforte is valid.
ERROR: RSENotFound: RSE does not exist.
Details: RSE 'T2_DE_NOPE' cannot be found in vo 'def'

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: development
	Please use 'crab uploadlog' to upload the log file /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab.log to the CRAB cache.
belforte@lxplus810/bot> 


```

## Comment (cmsdmwmbot, 2023-10-18T22:37:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 7 warnings
   * 158 comments to review
 * Pycodestyle check: succeeded
   * 164 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/953/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-19T19:31:14Z)

Merge so we can test in Jenkins

## Comment (belforte, 2023-10-19T20:16:01Z)

crab checkwrite still works fine on CMSSW 13, 11 and 9 for "old way", i.e. I did not break it
https://github.com/dmwm/CRABServer/issues/7967
https://github.com/dmwm/CRABServer/issues/7968
https://github.com/dmwm/CRABServer/issues/7969
further validation of the behavior when using Rucio-ASO will come during testing of that.

## Comment (mapellidario, 2023-10-20T16:58:59Z)

I had a look at this PR and i like it! I tested the command and it works as expected, both on lxplus and my laptop :)

I have a small suggestion: maybe

> Rucio client not available with this CMSSW version. Can not check

Should also suggest a version of cmssw where the rucio client is available

moreover, I am not sure why you wnated to remove `request_type`, which i admittedly never used, but maybe that's a question for another time.

fyi: @novicecpp

## Comment (belforte, 2023-10-20T19:27:02Z)

yeah, I am sure that exact messages printed both here and in new crab status will need refinement !
E.g. I do not think users should send us a mail when they misstype the site name !
But did tnot want to get stuck on that. Takes always time to fine tune that.

I do not understand the comment about `request_type`, sorry. Let's go back to that by voice
