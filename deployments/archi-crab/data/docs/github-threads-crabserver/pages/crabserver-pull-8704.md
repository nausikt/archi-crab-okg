# dmwm/CRABServer pull request #8704: Cleanup job wrapper

State: closed
Opened: 2024-09-20T10:11:25Z
Closed: 2024-09-30T11:55:09Z
Merged: 2024-09-30T11:55:09Z
URL: https://github.com/dmwm/CRABServer/pull/8704

## Opening post (belforte, 2024-09-20T10:11:25Z)

fix #7705

## Comment (cmsdmwmbot, 2024-09-20T10:17:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2172/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-20T10:17:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2173/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-20T10:27:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2174/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-20T10:33:33Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2175/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-20T10:34:46Z)

tested with a single on on crab-dev-tw01

## Comment (cmsdmwmbot, 2024-09-20T10:36:08Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2176/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-20T10:36:12Z)

tests
- [x]  in CI: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8173758
- [x] CCV test in Jenkins: #8705

## Comment (belforte, 2024-09-20T13:31:48Z)

@aspiringmind-code you can also look at https://cmscrab.docs.cern.ch/crab-design/crab-job-wrapper.html#new-cmsrunanalysispy for a description of what this PR is supposed to achieve

## Comment (belforte, 2024-09-20T16:06:44Z)

I added one cleanup. WIll test again.
- [x] CI https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8175959
    * pipeline failed since one task failed to submit with a stupid Rucio error `lfn2pfn resolution with Rucio failed for site: T2_CH_CERN` WIll monitor jobs in [grafana](https://monit-grafana.cern.ch/d/cmsTMGlobal/cms-tasks-monitoring-globalview?orgId=11&var-user=crabint1&var-site=All&var-current_url=%2Fd%2FcmsTMDetail%2Fcms_task_monitoring&var-task=All&from=1726844400000&to=now)
- [x] Jenkins  #8709
   * navbout half submissions failed with errors talking to Rucio... pff... but overall the new wrapper is working

## Comment (cmsdmwmbot, 2024-09-20T16:08:08Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 51 comments to review
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2177/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-24T16:34:59Z)

Ready for review

## Comment (belforte, 2024-09-27T14:52:40Z)

@aspiringmind-code let me if you think that you do not have the time or feel  not competent to review this.

## Comment (aspiringmind-code, 2024-09-27T21:25:52Z)

Sorry for the delay. I'll do it by tomorrow.

On Fri, 27 Sep, 2024, 4:53 pm Stefano Belforte, ***@***.***>
wrote:

> @aspiringmind-code <https://github.com/aspiringmind-code> let me if you
> think that you do not have the time or feel not competent to review this.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/dmwm/CRABServer/pull/8704#issuecomment-2379464032>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BJE3IUROX72ZGQPOBMRKCP3ZYVWM5AVCNFSM6AAAAABORWZ6ASVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDGNZZGQ3DIMBTGI>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>

## Comment (aspiringmind-code, 2024-09-28T15:26:50Z)

@belforte I like the use of simpler sandbox argument and the merging of two functions into one. What I still would wanna improve is removing the "moving up the directory" action. IIUC, that will not be required once $CMSSW_BASE files are put inside cmsswVersion directory inside the sandbox. Do we have an open issue regarding that? If yes, this looks good to me. Thanks for my first review opportunity.

## Comment (belforte, 2024-09-28T17:43:34Z)

thanks @aspiringmind-code 
I do not like moving files around like that eiher
<strike> I thought of this solution in https://github.com/dmwm/CRABServer/issues/7705#issuecomment-2361613880 but have not created an issue
Indeed I thought I did... what I have most is to expand the tarball in two directories

BEst option looks to me at some point to modify sandboxing in client so that $CMSSW_BASE is tarred into a CMSSW_X_Y_Z directory and then all files will automatically go in the proper place when the sandbox is iteratively expanded
</strike>

sorry I was confused. You are correct. I have not created an issue for that.
Let's do

## Comment (belforte, 2024-09-30T09:51:42Z)

Well... be my memory be damned. I had not created an issue for the sandbox restructuring in the client, but have already merged a PR to do it !
https://github.com/dmwm/CRABClient/issues/5332

Please have a look and let me now if that addresses your comment

## Comment (aspiringmind-code, 2024-09-30T11:42:17Z)

Yes, this looks perfect.

## Comment (belforte, 2024-09-30T11:53:31Z)

thanks you

## Comment (belforte, 2024-09-30T11:54:37Z)

now the problem will be to remember to cleanup the duplicated untar once new client will be in production
