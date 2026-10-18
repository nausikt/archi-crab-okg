# dmwm/CRABServer pull request #9400: Refined and New ASO ExitCodes 60XXXs and their regexes.

State: closed
Opened: 2026-08-25T21:00:47Z
Closed: 2026-08-28T15:30:20Z
Merged: 2026-08-28T15:30:20Z
URL: https://github.com/dmwm/CRABServer/pull/9400

## Opening post (nausikt, 2026-08-25T21:00:47Z)

Resolve #9363

## Finalized Summary
Code | Scope | distribution | Summary
-- | -- | -- | --
60317 | Forced timeout for stuck stage out | — | —
60318 | Internal error in Crab cmscp.py stageout script
60320 | Failure to communicate with ASO server | — | —
60321 | (legacy) Site related issue: no space, SE down, refused connection. | 0% | DELETED, migrate to 60328 due to clean ordering reason, generic failures should be catch after SOURCE/DEST.
60322 | Permission denied | 9.60% | 403 dest 7.25% · 403 src 1.58% · 403 TPC 0.75% · 401 TPC 0.02%
60323 | Quota / Storage full | 43.40% | HTTP 507 TPC 
60324 | Other stageout exception | ~1.16% | the rest stageout exception
60325 | Maximum time in FTS queue exceeded | 18.62% | max-time-in-queue
60326 | Likely error at Source RSE | 7.20% | Source site storage unavailable, unresponsive, or dropped the connection. (curl56 6.84% · curl28 0.17% · curl7 0.12% · curl35 0.07%)
60327 | Likely error at Destination RSE | 11.18% | Destination site storage unavailable, unresponsive, or dropped the connection. (curl56 4.42% · curl35 1.60% · curl7 1.50% · curl28 1.38% · curl3 1.34% · 500 0.76% · curl52 0.18% · 501 ~0%)
60328 | Generic transfer failures | 8.88% | Problem at third-party, Transfer interrupted, unstable/refused/abruptly-terminated connection. (500 TPC 6.87% · terminated abruptly 1.02% · 404 0.45% · curl52 0.45% · curl35 0.08% · 429 0.01%)

The results here derived CRAB's `filetransferdb` queried over 2 months **12-06-2026** to **12-08-2026** with 300 distinct aggregate failure reasons then applied this PR regexes for the **expected approximate** distribution above.

Raw Data Source: https://github.com/dmwm/CRABServer/issues/9363#issuecomment-5269166581

## Comment (cmsdmwmbot, 2026-08-25T21:04:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 27 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2905/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-25T21:13:44Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 27 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2906/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-26T15:24:16Z)

It is a very good start. I offer following suggestions:

1. it may be my prejudice, but I think that most (all?) permission errors are simply the way some storage servers signal "full quota". All in all before submitting TaskWorker already tries to create a directory and a file at the destination storage, if user had a permission issue, it would have popped up there.  I suspect that CERNBOX is such a storage server. We could test by filling up our quota there (via some quick way like `dd` ), but.. what else could it be ?
2. Why "Server fault" is not pat of 60321 ? Which server is faulting ? 
3. I see that you put `curl error 28` in 60321 and `curl error 56` in 60326, why ? if there's a rational, please put comments in the code explaining this
4. have you really and fully given up on telling whether the error was at source or destination ? Do you have hints that the `SOURCE|DESTINATION` labels in FTS message are unreliable ? Should we sort of give it a try ? Something like
 - likely error at source RSE
 - likely error at destination RSE
 - generic transfer failure
 ?

## Comment (nausikt, 2026-08-26T16:48:11Z)

Thanks for thoughtful review Stefano. Sorry for poor clarification in this PR. more details in [issuecomment](https://github.com/dmwm/CRABServer/issues/9363#issuecomment-5413467430)

2. I try to convey that it's FTS Server fault apart from any storage elements/sites failures. **Will add `FTS` in error-msg, definition.** 
3. At first thought, i did hesitate about these 2 class too, but end-up classified Transfer interrupt or (Third-party) Connection interrupt into the same 60326 class due to their abruptly manner, but Yeah kind of started to convince that all connection-relevant should live in 60321. **I will move it to 60321 then**
4. i did try na, isn't it? telling that where it came from source/destination/third-party copy site/storage throughout err-mesg. **but will converge to your style to have word like `likely` error or `RSE` na.**

For [1] forgive me, it still not obvious to me, you mean we better combine some `Permission Denied` into `Full Quota` 507 class?, can you help me see your point more clearly plz?

[1] Open new Issue to investigate exactly `Permission Denied` into `Full Quota` 507 class for investigating later.

## Comment (belforte, 2026-08-26T17:06:23Z)

let's talk about this tomorrow afternoon, ok ?
I do not understand your 2. We submitted a transfer job to FTS, tracked its status through it, and in the end it told us that the transfer failed and gave us this string as "reason". Where do you see indication that FTS server was not working ?
If you do not know how FTS and ThirdPartyCopy work... fine, just ask.

## Comment (nausikt, 2026-08-26T17:19:52Z)

Thank you Stefano, tomorrow afternoon work for me.

## Comment (cmsdmwmbot, 2026-08-28T12:35:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2907/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-28T12:52:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2908/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-08-28T13:18:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2909/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-08-28T13:25:30Z)

The results derived CRAB's `filetransferdb` queried over 2 months **12-06-2026** to **12-08-2026** with 300 distinct aggregate failure reasons then we applied this PR revised regexes and got distribution in table. 

See also https://github.com/dmwm/CRABServer/issues/9363#issuecomment-5269166581
_______

Below is the **expected approximate** distribution, converged to what we discussed offline.
Distribution here refers to fraction of time this message appears in FTS record in OpenSearch

Code | Scope | distribution | Summary
-- | -- | -- | --
60317 | Forced timeout for stuck stage out | — | —
60318 | Internal error in Crab cmscp.py stageout script
60320 | Failure to communicate with ASO server | — | —
60321 | (legacy) Site related issue: no space, SE down, refused connection. | 0% | DELETED, migrate to 60328 due to clean ordering reason, generic failures should be catch after SOURCE/DEST.
60322 | Permission denied | 9.60% | 403 dest 7.25% · 403 src 1.58% · 403 TPC 0.75% · 401 TPC 0.02%
60323 | Quota / Storage full | 43.40% | HTTP 507 TPC 
60324 | Other stageout exception | ~1.16% | the rest stageout exception
60325 | Maximum time in FTS queue exceeded | 18.62% | max-time-in-queue
60326 | Likely error at Source RSE | 7.20% | Source site storage unavailable, unresponsive, or dropped the connection. (curl56 6.84% · curl28 0.17% · curl7 0.12% · curl35 0.07%)
60327 | Likely error at Destination RSE | 11.18% | Destination site storage unavailable, unresponsive, or dropped the connection. (curl56 4.42% · curl35 1.60% · curl7 1.50% · curl28 1.38% · curl3 1.34% · 500 0.76% · curl52 0.18% · 501 ~0%)
60328 | Generic transfer failures | 8.88% | Problem at third-party, Transfer interrupted, unstable/refused/abruptly-terminated connection. (500 TPC 6.87% · terminated abruptly 1.02% · 404 0.45% · curl52 0.45% · curl35 0.08% · 429 0.01%)

## Comment (cmsdmwmbot, 2026-08-28T13:26:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2910/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-08-28T13:33:10Z)

Please, let me know if any wording could be more concise.

## Comment (belforte, 2026-08-28T14:37:53Z)

what's happened to 60324 ? Same as 60321 ?

## Comment (nausikt, 2026-08-28T14:39:49Z)

No Stefano, 60324 is still there, it will remains catch the remaining 1% we didn't explicitly defined here.

## Comment (belforte, 2026-08-28T14:42:04Z)

60324 is no listed in last version of the table in previous comment, that's why I asked

## Comment (belforte, 2026-08-28T14:43:21Z)

I'd change this
`FTS transfer expired, exceeded maximum time in queue`
to
`maximum time in FTS queue exceeded`

## Comment (nausikt, 2026-08-28T14:44:58Z)

Adjusted, in the table.

## Comment (cmsdmwmbot, 2026-08-28T14:48:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2911/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-28T15:13:32Z)

last thing, for long term documentation better not have two versions of same table in the comments history. At the very least add a clear not in top one that the table used for the new regexps is way below.

## Comment (nausikt, 2026-08-28T15:19:02Z)

Acknowledged, i will put the finalized one at the top of PR and Twiki.

## Comment (belforte, 2026-08-28T15:26:23Z)

you can merge and create new tag at your conveniene. I do not have any change close to being ready

## Comment (nausikt, 2026-08-28T15:29:44Z)

Thanks Stefano!, All Done, updated https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes.
