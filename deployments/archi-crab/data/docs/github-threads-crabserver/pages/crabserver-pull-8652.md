# dmwm/CRABServer pull request #8652: suspend tape recall rule before deleting. Fix #8647

State: closed
Opened: 2024-08-26T16:28:36Z
Closed: 2024-09-01T17:15:36Z
Merged: 2024-09-01T17:15:36Z
URL: https://github.com/dmwm/CRABServer/pull/8652

## Opening post (belforte, 2024-08-26T16:28:36Z)

(no text)

## Comment (cmsdmwmbot, 2024-08-26T16:32:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2123/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-30T09:52:55Z)

let's not wait for Rahul. I will make sure syntax is correct and put this in

## Comment (dynamic-entropy, 2024-08-30T10:10:34Z)

Hello Stefano
Apologies! I wanted to check if this is needed at all.

Rucio should not create transfer requests for expired rules by itself. Have you observed otherwise?
Why do you think this is needed?

## Comment (belforte, 2024-08-30T10:42:57Z)

It is about races.
We found that expired rules were sticking around for longish time because they had hanging FTS requests stuck in "stage from tape". Since delete has 1h grace period and the daemon which checks for expired rules and the one which submits FTS requests are asynchronous of each other, we are trying to minimize the chance that more FTS transfer requests are issued.

I agree that if we do not do this, eventually it should all clear up by itself. But in a situation like last week, were a user had too many ongoing recalls and we had him kill all tasks, the sooner we remove stuff, the better.

Reference: https://its.cern.ch/jira/browse/CMSDM-198?focusedId=6502570&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6502570

## Comment (dynamic-entropy, 2024-08-30T12:46:54Z)

For the ticket you mentioned above, no new requests were being submitted after the rule was marked for deletion. 
The issue was that the DB transaction in which a rule is moved from the `rules` table to the `rules_history` table was failing. 
But the rule was not being picked up by daemons responsible for initiating transfers.

Now, this 1 hr grace period is what I wanted to check. i.e what purpose was it supposed to serve. 
And if new submissions are tried for rules that are to expire in an hour. 

In any case, this PR does no harm. So, for me, this is a good thing to do.

## Comment (belforte, 2024-08-30T13:02:18Z)

>  this 1 hr grace period is what I wanted to check. i.e what purpose was it supposed to serve.

AFAIU it is a protection again operator mistakes, giving people 1h to roll back after a "OOPS I did not want to do that" !

It may still make sense for when users will managed their data via Rucio. For a fully automated DM-WM setup as you are trying to have now, it is likely immaterial.

## Comment (belforte, 2024-08-30T13:03:28Z)

> The issue was that the DB transaction in which a rule is moved from the rules table to the rules_history table was failing.

do you mean that this was unrleated to "pending requests" ?
Well.. I can put the suspend in for "peace of mind", but have to agree that usefulness is doubtful at best !

## Comment (dynamic-entropy, 2024-08-30T20:44:25Z)

> do you mean that this was unrleated to "pending requests" ?

A transfer request status for a rule that has been deleted does not matter.  A rule will not wait for FTS transfers to complete to be cleaned up when expire. 

> Well.. I can put the suspend in for "peace of mind", but have to agree that usefulness is doubtful at best !

I agree.
