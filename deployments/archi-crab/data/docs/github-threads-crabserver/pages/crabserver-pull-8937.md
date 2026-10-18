# dmwm/CRABServer pull request #8937: File-based Cacheable CRIC Service at TW, decomission CRIC Sites checking logic at CRABServer and migrated it to TW.

State: closed
Opened: 2025-02-18T19:44:57Z
Closed: 2025-02-25T15:32:01Z
URL: https://github.com/dmwm/CRABServer/pull/8937

## Opening post (nausikt, 2025-02-18T19:44:57Z)

Fixes #6917

## Comment (cmsdmwmbot, 2025-02-18T19:47:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 21 warnings and errors that must be fixed
   * 6 warnings
   * 130 comments to review
 * Pycodestyle check: succeeded
   * 636 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2381/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-02-18T19:53:05Z)

Please, see write-up and test results in #6917.

## Comment (belforte, 2025-02-18T20:41:41Z)

> Please, see write-up and test results in https://github.com/dmwm/CRABServer/issues/6917.

I have not found either. May bad ? Indeed a description of the new login would be nice.

I think it is safer to do in two steps.
 1. change TW and make sure it works w/o getting the site info from REST 
 2. change REST

overall changes look way more extensive than I expected. Are you sure we need to change so much all those files ?

## Comment (nausikt, 2025-02-18T20:58:50Z)

> > Please, see write-up and test results in #6917.
> 
> I have not found either. May bad ? Indeed a description of the new login would be nice.
> 
> I think it is safer to do in two steps.
> 
> 1. change TW and make sure it works w/o getting the site info from REST
> 2. change REST
> 
> overall changes look way more extensive than I expected. Are you sure we need to change so much all those files ?

My bad, I'm writing it. 

Yes, at first glance it's just two steps for me too. but i break it down into multiple steps to tests and addressing other high cohesive issues along the way too.

The extensive changes might feel intimidating, but it's kind of refactoring along the way to reduces boilerplate code. Hopefully, it eases our comprehension in the future.

## Comment (belforte, 2025-02-18T21:07:47Z)

i meant : have two PR and validate/merge/deploy one at a time.

## Comment (nausikt, 2025-02-18T21:09:58Z)

Ahh, Acknowledge Stefano.

## Comment (cmsdmwmbot, 2025-02-19T00:21:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 6 warnings
   * 131 comments to review
 * Pycodestyle check: succeeded
   * 636 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2382/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-02-19T02:52:07Z)

> > Please, see write-up and test results in #6917.
> 
> I have not found either. May bad ? Indeed a description of the new login would be nice.
> 
> I think it is safer to do in two steps.
> 
> 1. change TW and make sure it works w/o getting the site info from REST
> 2. change REST
> 
> overall changes look way more extensive than I expected. Are you sure we need to change so much all those files ?

I've clarified it here https://github.com/dmwm/CRABServer/issues/6917#issuecomment-2667374872.

## Comment (belforte, 2025-02-21T09:47:47Z)

thanks for changes/additions. Yet this will take some dedicated time for me to understand, and I'd rather do it after I am done with current issue in PreJob #8938 
Sorry to keep you waiting.

## Comment (belforte, 2025-02-25T15:11:23Z)

@sinonkt in light of the chat which we had, I suggest that you close this and make a new one with the simplified changes to the TW code. Once that works you can make another PR for the REST

## Comment (nausikt, 2025-02-25T15:32:01Z)

@belforte Acknowledge, Stefano. I agree with you.
