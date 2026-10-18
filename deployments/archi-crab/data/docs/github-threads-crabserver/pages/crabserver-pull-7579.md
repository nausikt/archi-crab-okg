# dmwm/CRABServer pull request #7579: CMSRunAnalysis.py - use application exit code together with FWJR.xml

State: closed
Opened: 2023-04-04T15:25:31Z
Closed: 2023-04-14T16:02:49Z
Merged: 2023-04-14T16:02:49Z
URL: https://github.com/dmwm/CRABServer/pull/7579

## Opening post (mapellidario, 2023-04-04T15:25:31Z)

Fixes #7571 

## status

tested on test11, ready to merge

## description

The solution I propose with this PR is the less intrusive one that I can think of. 

As always, we can simplify a lot all the tangled `try`s and `if`s after the application finishes, but feels a bit out of scope and would take definitely longer than 1day.

## Comment (cmsdmwmbot, 2023-04-04T15:28:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 14 warnings
   * 126 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1481/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-04T15:36:05Z)

a bit of an overkill, especially if they fix the default FJR.xml to have an error exit code, anyhow it does the job. Thanks

## Comment (mapellidario, 2023-04-05T11:09:06Z)

Ah I see, I think I missed 

> Note that before CMSSW 12_6_0 the job report would very likely have been invalid XML

from this comment [1]. In any case, "very likely" is not "i guarantee that", so i'd rather be safe then sorry.

In any case, I updated the comments after reading again the full discussion. They should be more precise now. How do they sound now?

Thanks Stefano for the review!

[1] https://github.com/dmwm/CRABServer/issues/7571#issuecomment-1476584857

## Comment (cmsdmwmbot, 2023-04-05T11:12:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1484/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-05T15:42:06Z)

Dario, I tried but failed to edit the file. Here's how I propose to change
```

            # - For CMSSW versions earlier than 12_6, when the framework fails abnormally 
            #    it leaves behind an invalid FWJR.xml. 
            # - For any CMSSW version 12_6 and higher, cmsRun always creates a syntactically correct
            #    FWJR.xml (possibly with empty content) also when it exits with non-zero exit code.
            jobExitCode = applicationExitCode
            print("The application failed with exit code %s" % applicationExitCode)
            print("but WMCore.FwkJobReport.Report:getExitCode() returned 0 from FWJR.xml")
            print("This job will be marked as failed.")
            print("In order to help with debugging, we print the content of FrameworkJobReport.xml")
```

## Comment (SohamBhattacharya, 2023-04-14T09:11:27Z)

Hi, I have a question about which CMSSW version I need to use once this is merged.
I had been using `CMSSW_12_6_0_patch1`, where I encountered the issue. Will there be a `CMSSW_12_6_0_patch2` with this fix? Or is it that the CRAB will be updated 'globally' and I don't need to change the CMSSW version?

## Comment (belforte, 2023-04-14T09:21:47Z)

@SohamBhattacharya the plan is to make CRAB work  the same with any CMSSW release.

## Comment (belforte, 2023-04-14T09:24:45Z)

@mapellidario I think I am done here. There's a proposed changing of what gets printed which you need to do in your branch (if you agree), or you merge and I make a PR (if you prefer). Let me know if I missed something.

## Comment (mapellidario, 2023-04-14T13:32:28Z)

I improved the logs, i think this PR can be merged now

## Comment (cmsdmwmbot, 2023-04-14T13:34:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1495/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-14T16:02:44Z)

very good, thanks Dario.
