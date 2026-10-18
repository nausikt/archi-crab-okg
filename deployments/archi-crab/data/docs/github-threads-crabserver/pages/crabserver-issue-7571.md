# dmwm/CRABServer issue #7571: jobwrapper not always mark the job as failed

State: closed
Opened: 2023-03-20T13:52:00Z
Closed: 2023-04-14T16:02:50Z
Labels: Type: Bug, Priority: TOP, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7571

## Opening post (mapellidario, 2023-03-20T13:52:00Z)

### overview

A user reported that cmsRun crashed in a job, but that CRAB marked the job as successful [1]

### details

cmsRun in this job [2] clearly failed, it exited with exit code 5. However cmsRun apparently produced a FrameworkJobReport.xml containing the exit code 0.

<details><summary>Extract from the job log:</summary>

```plaintext
==== CMSSW JOB Execution started at Mon Mar 13 12:25:53 2023 ====
Error executing application in CMSSW environment.
	See stdout log
==== Execution FAILED at Mon Mar 13 16:51:08 2023 ====
==== CMSSW JOB Execution completed at Mon Mar 13 16:51:08 2023 ====
Application exit code: 5
==== Execution FINISHED at Mon Mar 13 16:51:08 2023 ====
======== CMSSW OUTPUT STARTING ========
[...]
=======================================
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: slc7_amd64_gcc10
== CMSSW:         Executed: cmsRun -p PSet.py -j FrameworkJobReport.xml
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout: 13-Mar-2023 05:30:37 PDT  Initiating request to open file root://xcache-redirector.t2.ucsd.edu:2040//store/mc/RunIISummer20UL18MiniAODv2/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/2E317D12-DFB4-054F-9323-12117539CEAD.root
[...]
== CMSSW: [2023-03-13 09:51:08.145021 -0700,Error  ,XRootD            ,  346] [xrd-cache-8.ultralight.org:1094] Unable to get the response to request kXR_readv (handle: 0x00000000, chunks: [[...]
== CMSSW: /bin/bash: line 146:   346 Bus error               cmsRun -p PSet.py -j FrameworkJobReport.xml
== CMSSW:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINSHING ========
==== Report file creation STARTING at Mon Mar 13 16:51:09 2023 ====
Sanitize FJR

==== Job Exit Code from FrameworkJobReport.xml: 0 ====
== Execution site from site-local-config.xml: T2_US_UCSD
==== Report file creation FINISHED at Mon Mar 13 16:51:15 2023 ====
==== CMSRunAnalysis.py FINISHED at Mon Mar 13 16:51:15 2023 ====
Local time : Mon Mar 13 09:51:15 2023
+ jobrc=0
+ set +x
== The job had an exit code of 0 
======== CMSRunAnalysis.py FINISHING at Mon Mar 13 16:51:16 GMT 2023 ========

real	271m43.552s
user	24m51.502s
sys	14m56.239s
CMSRunAnalysis.sh complete at Mon Mar 13 16:51:18 GMT 2023 with (short) exit status 0
```
</details>

I could not replicate the error in lxplus with `crab preparelocal`.

### solution

I think I should improve the logic in the jobwrapper, so that the exitcode in the frameworkjobreport does not have the precedence over the cmsRun exitcode.

---


[1] https://cms-talk.web.cern.ch/t/crab-marking-crashed-jobs-as-successful/21636/

[2] https://cmsweb.cern.ch:8443/scheddmon/0122/sobhatta/230311_154018:sobhatta_crab_ZZTo4L/job_out.2-41.0.txt

## Comment (belforte, 2023-03-20T15:17:39Z)

@mapellidario I am not so sure of what's best to do in this case. Let's take the time to think it through.

## Comment (makortel, 2023-03-20T15:22:59Z)

As far as I can tell, in case of success the `FrameworkJobReport.xml` does not contain any exit code info. I'd be curious to see the job report parsing code in CRAB/WM that interprets  "no exit code in xml" as success.

## Comment (belforte, 2023-03-20T15:27:36Z)

Matti, do you mean "in case of insuccess ?" or... .. maybe as simple as:
WMCore finds no exit code, so calls it success and sets to 0 (we need one value !) even if there's no more info in the XML about having done any useful work ?
See: https://cmsweb.cern.ch:8443/scheddmon/0119/sobhatta/230311_084416:sobhatta_crab_TTToSemiLeptonic/job_fjr.2-2224.1.json

## Comment (belforte, 2023-03-20T15:37:33Z)

hmm.. I doubt we can converge w/o the original FJR.xml. It is a guessing game here.
Anyhow this could be where a missing exit code is reported as `0`: https://github.com/dmwm/WMCore/blob/eaaf7a3bf6b39fed0bbae03bf89238a72230e978/src/python/WMCore/FwkJobReport/Report.py#L323-L338
which is then inserted back into the JSON file by CRAB's wrapper:
https://github.com/dmwm/CRABServer/blob/e2e09dde7ebedf1450df67450e3c77bda03c113f/scripts/CMSRunAnalysis.py#L668-L681

## Comment (makortel, 2023-03-20T15:38:11Z)

> WMCore finds no exit code, so calls it success and sets to 0 (we need one value !) even if there's no more info in the XML about having done any useful work ?

I meant exactly this. I don't see any code on framework side that would add "exit code 0" to the job report XML file in case of success, and I also don't see any exit code entries in job report XML files from successful jobs in CMSSW IBs.

In case of failures the framework adds `<FrameworkError ExitStatus="..." ...> ... </FrameworkError>` element to the job report XML. In the case reported in CMS Talk the process is so screwed up that the function adding `FrameworkError` was not added.

## Comment (belforte, 2023-03-20T15:42:49Z)

this sort of makes sense so far. The unexpected bit  is that cmsRUn "failed" but created a sintactycally correct, empty FJR which WMCore's wrapper failed to mark as "bad".

We surely do not want to even think of changing what framework does in case of success ! But again, w/o the original XML there's a lot of guessing. I guess we could ask for the FJR to contain at east one step e.g.

## Comment (makortel, 2023-03-20T15:49:04Z)

Adding @Dr15Jones

## Comment (makortel, 2023-03-20T15:54:42Z)

@belforte Thanks for the code pointer (in https://github.com/dmwm/CRABServer/issues/7571#issuecomment-1476464838). As far as I can tell, the `getStepExitCodes()` and `getExitCode()`
https://github.com/dmwm/WMCore/blob/eaaf7a3bf6b39fed0bbae03bf89238a72230e978/src/python/WMCore/FwkJobReport/Report.py#L304-L340
both default to `0` if the XML parser has not found an error element.

The parser sets the error code here
https://github.com/dmwm/WMCore/blob/eaaf7a3bf6b39fed0bbae03bf89238a72230e978/src/python/WMCore/FwkJobReport/XMLParser.py#L155-L170
and the `errorHandler()` is registered for the parser in
https://github.com/dmwm/WMCore/blob/eaaf7a3bf6b39fed0bbae03bf89238a72230e978/src/python/WMCore/FwkJobReport/XMLParser.py#L517-L526

## Comment (belforte, 2023-03-20T16:36:31Z)

hmm  In the task indicated at the top has 777 instances of `Bus error` in the job stdouts !  (well out of 35K jobs total, a tiny 2%).  Maybe that Bus error originates in some memory corruption and could be reproduced ?

@makortel @dr15jones so what happens here is that something so bad happens that cmsRun is killed abruptly w/o a chance of writing anything in the FJR. Yet no so bad to kill the whole process stack. This is all in all to be expected. Question is how to diagnose. Should we shelve current policy "FJR wins" and trust application unix exit status instead  (as Dario suggested) ? What other flag do we have to confidently say "it worked" ? All in all, even if sometime in the long forgotten past there was a good reason to claim "FJR wins", so many things changed since that code settled in that I have no objection to revisit.

I was not aware of "missing exit code --> exit code = 0" in WMCore. @amaltaro how do you handle this circumstance in WMA . Maybe you do not rely on `report.getExitCode()` ?

## Comment (makortel, 2023-03-20T16:44:59Z)

In principle we could add a a new element to the job report XML indicating the job succeeded (e.g. with explicit "exit code 0"). This would introduce yet-another CMSSW release dependent behavior, and we'd be blind for many existing releases. Note that before CMSSW 12_6_0 the job report would very likely have been invalid XML (we made a change in 12_6_X that would keep the job report always as valid XML, but did not realize this kind of failure of assumptions).

So perhaps a better way forward would indeed be to first check the process exit status, and consider the job as succeeded only if the exit status is 0. For non-zero exit status I'd still check the job report XML in case it has better defined exit code and more details of the failure.

## Comment (belforte, 2023-03-20T17:29:49Z)

Thanks Matti.
I am against adding a new element exactly for the reason you indicate ! So this is likely a new problem introduced with 12_6. We do no have to worry about uncounted unknown silent failures in the past.

I agree with `check for exit status first`.  At least that's something that we are aware of both as producer and consumers of that status ! For some number of years we will remember and be protected :-)

@mapellidario go ahead

## Comment (belforte, 2023-03-20T17:43:19Z)

FWIW, currently a `FrameworkJobReport.xml` is prepared initially bycmsRun with content
```
<FrameworkJobReport>
</FrameworkJobReport>
```
which WMCore happily parses producing

```
{'Campaign': '',
 'EOSLogURL': '',
 'PrepID': '',
 'WorkerNodeInfo': {'HostName': '', 'JobFeatures': {}, 'MachineFeatures': {}},
 'fallbackFiles': [],
 'skippedFiles': [],
 'steps': {'cmsRun': {'analysis': {},
                      'cleanup': {},
                      'errors': [],
                      'input': {},
                      'logs': {},
                      'output': {'analysis': []},
                      'parameters': {},
                      'performance': {'cpu': {},
                                      'memory': {},
                                      'multicore': {},
                                      'storage': {}},
                      'site': {},
                      'start': None,
                      'status': 1,
                      'stop': None}},
 'task': None}
```
and of course `report.getExitCode()` of that returns `0` sigh, sigh, sigh. sob, sob, sob.

Everything understood.

## Comment (belforte, 2023-03-20T18:27:11Z)

I tried (and failed) to find some simple way to detect an empty FJR from CRAB wrapper via WMCore parser. The problem is that the initial template is needed so an empty FJR will only differ from a good one in the fact that those fields above have values rather than empty `{}`'s bu the structure will be there, and checking for e.g. non-null value of CPU appears a bit fragile.
Of course we could read the XML in crab wrapper as text and compare with `<FrameworkJobReport>\n</FrameworkJobReport>`. But that looks fragile and ad-hoc too.

I am giving up.

## Comment (makortel, 2023-03-20T19:11:14Z)

After discussing more with @Dr15Jones we will update the framework job report writing such that if the cmsRun process terminates abnormally, the job report XML will contain a failure exit code. In that way the job report XML will report success (by not reporting any exit code) only if the framework can guarantee all the requested data was processed, and the output files have been closed.

There is one case where we actually might want to not treat the job as a failure even if the unix process exits with non-zero value. We see occasional cases (both in IBs and in production) where the job crashes after the `main()` has returned. In such cases the produced files should be fine, and the framework job report (already now) reports the job succeeded. So in principle we could treat such a job as succeeded, in which case WM and CRAB should **not** rely on the unix process exit status.

I've gotten the impression that WM would check the unix process exit status (based on @Dr15Jones being able to find log files of such "job crashes during exit" via exit code 139), and I think in any case WM and CRAB should be consistent in how they deal with the application exit code.

## Comment (belforte, 2023-03-20T21:11:12Z)

thanks @makortel and @dr15jones I'd like to hear from @amaltaro as well, since indeed it is important to have a common, well defined behavior. IIUC the change which you propose will be effective from CMSSW_13 onward and maybe also on latest 12_x. In any case, better one good job called failed than the other way around.

## Comment (makortel, 2023-03-20T21:13:12Z)

> IIUC the change which you propose will be effective from CMSSW_13 onward and maybe also on latest 12_x. 

Right, the change would enter in 13_1_X and be backported to 13_0_X and 12_6_X.

> In any case, better one good job called failed than the other way around.

Agreed.

## Comment (amaltaro, 2023-03-20T21:26:43Z)

If I am reading the WMCore code correctly, job outcome does depend on the subprocess status code:
https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/WMSpec/Steps/Executors/CMSSW.py#L272-L281

even though a few lines below we fetch the CMSSW exit code and message (`getStepExitCodeAndMessage`).

Do we understand what can be the latency between returning from `main()` and the actual subprocess return? Unless there is a trivial way to identify those, I'd say we let such "1 in very many" jobs to follow the failure path and deal with it in a retry.

## Comment (makortel, 2023-03-20T21:37:01Z)

> Do we understand what can be the latency between returning from `main()` and the actual subprocess return?

In principle it should be "fast", but when we enter to the regime of "job crashes at exit" I can't exclude of job getting stuck there either (I think we've seen such cases in the past).

But could you elaborate how the latency between returning from `main()` and the process actually terminating impacts the consideration?

## Comment (belforte, 2023-03-20T23:23:03Z)

can we close the day on
"cmsRun must end with exit code zero AND FWR must positively report success"
?

I am not sure what's the bad side of those (unreproducible, I hope) cases where application failed after the framework complete the work and closed all files if we stay on the safe side and call them failures. Wasted CPU ? Useless fake alarms during validation ? Can we live with them until it happens often enough to be a nuisance ?

## Comment (amaltaro, 2023-03-21T05:23:23Z)

> But could you elaborate how the latency between returning from main() and the process actually terminating impacts the consideration?

Just assessing if it's worth it to chase the potential very rare success cmsRun but process exit code != 0. 

> can we close the day on
>"cmsRun must end with exit code zero AND FWR must positively report success"?

Yes, it seems to be the way! This is what we already have in WMCore (in the code I shared above), so even better, no changes required :-)

## Comment (SohamBhattacharya, 2023-04-02T14:39:41Z)

Hi, I need to start processing some Data soon, and was wondering if there's a (ad-hoc) fix to this that I can implement locally. For MC this problem is not absolutely critical, but for collision Data it is quite a problem if part of it is not processed correctly and there's no way to resubmit those jobs as crab marks them as successful.
Thanks in advance.

## Comment (belforte, 2023-04-02T15:47:55Z)

CRAB allows to resubmit successful jobs as well, if you have a simple way to identify them !
We will update CRAB most likely next week. Maybe @mapellidario will be able to slip in a fix for this as well.
