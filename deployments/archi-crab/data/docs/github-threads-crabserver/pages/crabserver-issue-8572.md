# dmwm/CRABServer issue #8572: make HTCondor v2 bindings available on all Schedulers

State: closed
Opened: 2024-07-29T17:02:45Z
Closed: 2024-09-26T12:57:32Z
Labels: Area: HTCondor, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8572

## Opening post (belforte, 2024-07-29T17:02:45Z)

I know of two ways:
1. `pip install htcondor==23.9.0a3` in the `crabtw` user local (tested. Now running in vocms059).
   * shall we push to all VM's ?
2. deploy HTCondor 23.8.1 ?
   * try again ?

After test and debug (see below) we go for
3. deploy HTCondor 23.9.6 on our schedulers

## Comment (belforte, 2024-07-29T17:20:08Z)

I tried to deploy HTC 23.8.1 on `crab-preprod-scd03` : https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/758616c3abc293aa47b8e3458bc1d826a3490dd9

This time I tried to be extra careful
1. `condor_off`
2. `puppet agent -tv`
3. `condor_on`

there was some restarts of processes, but after a few minutes condor is up, and bindings version is good:
```text
belforte@crab-preprod-scd03/condor> condor_version
$CondorVersion: 23.8.1 2024-06-27 BuildID: 742100 PackageID: 23.8.1-1 GitSHA: 8cf018d1 $
$CondorPlatform: x86_64_AlmaLinux9 $
belforte@crab-preprod-scd03/condor> python3
Python 3.9.18 (main, Jul  3 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor2
>>> htcondor2.version()
'$CondorVersion: 23.9.0 2024-05-31 BuildID: UW_Python_Wheel_Build PRE-RELEASE-UWCS $'
>>> 
belforte@crab-preprod-scd03/condor> 
```

Need to test some jobs now. All in all in previous attempt schedd daemon was segfaulting on a negotiation attempt

## Comment (belforte, 2024-07-29T19:50:43Z)

and as feared schedd segfaulted on negotiation
```
07/29/24 21:48:32 (pid:2552701) Number of Active Workers 0
07/29/24 21:48:34 (pid:2552701) Number of Active Workers 0
07/29/24 21:48:34 (pid:2552701) Number of Active Workers 0
07/29/24 21:49:13 (pid:2552701) Number of Active Workers 0
07/29/24 21:49:15 (pid:2552701) Number of Active Workers 0
07/29/24 21:49:44 (pid:2552701) Negotiating for owner: analysis.belforte@cms
07/29/24 21:49:44 (pid:2552701) Negotiating owner=analysis.belforte@cms jobprio restricted, min=10 max=10
07/29/24 21:49:44 (pid:2552701) AutoCluster:config() significant attributes changed to ChildMemoryUsage DESIRED_Entries DESIRED_Gatekeepers DESIRED_Sites DynamicSlot GLIDEIN_PS_HAS_SINGULARITY MachineLastMatchTime MaxWallTimeMins PartitionableSlot ProportionalSetSizeKb RequestCpus RequestDisk RequestGPUs RequestMemory ResidentSetSize Slot1_SelfMonitorAge Slot1_TotalTimeClaimedBusy Slot1_TotalTimeUnclaimedIdle TotalJobRuntime ConcurrencyLimits CRAB_UserHN FlockTo JobStatus Rank Requirements
07/29/24 21:49:44 (pid:2552701) Rebuilt prioritized runnable job list in 0.000s.
07/29/24 21:49:44 (pid:2552701) Finished sending rrls to negotiator
07/29/24 21:49:44 (pid:2552701) Finished sending RRL for analysis.belforte
07/29/24 21:49:44 (pid:2552701) Activity on stashed negotiator socket: <[2620:6a:0:8421::8c]:17001>
07/29/24 21:49:44 (pid:2552701) Negotiating for owner: analysis.belforte@cms
07/29/24 21:49:44 (pid:2552701) Negotiating owner=analysis.belforte@cms jobprio restricted, min=10 max=10
Caught signal 11: si_code=1, si_pid=4, si_uid=0, si_addr=0x4
Stack dump for process 2552701 at timestamp 1722282584 (40 frames)
/lib64/libcondor_utils_23_8_1.so(_Z18dprintf_dump_stackv+0x29)[0x7f1338e1ec49]
/lib64/libcondor_utils_23_8_1.so(_Z17unix_sig_coredumpiP9siginfo_tPv+0x6c)[0x7f1338fc7e5c]
/lib64/libc.so.6(+0x3e6f0)[0x7f133843e6f0]
/lib64/libclassad.so.23.8.1(_ZNK7classad8ExprList10GetValueAtEiRNS_5ValueEPNS_9EvalStateE+0x28)[0x7f13392bb668]
/lib64/libclassad.so.23.8.1(_ZN7classad9Operation12_doOperationENS0_6OpKindERNS_5ValueES3_S3_bbbS3_PNS_9EvalStateE+0x3ff)[0x7f13392cd42f]
/lib64/libclassad.so.23.8.1(_ZNK7classad10Operation27flattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeE+0x424)[0x7f13392d3614]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x505)[0x7f13392d5975]
/lib64/libclassad.so.23.8.1(_ZNK7classad12FunctionCall8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0xbd)[0x7f13392baaed]
/lib64/libclassad.so.23.8.1(_ZNK7classad12FunctionCall8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0xbd)[0x7f13392baaed]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x309)[0x7f13392d5779]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x2cc)[0x7f13392d573c]
/lib64/libclassad.so.23.8.1(_ZNK7classad15OperationParens7flattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeE+0x57)[0x7f13392d3da7]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x505)[0x7f13392d5975]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x309)[0x7f13392d5779]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x2cc)[0x7f13392d573c]
/lib64/libclassad.so.23.8.1(_ZNK7classad15OperationParens7flattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeE+0x57)[0x7f13392d3da7]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x505)[0x7f13392d5975]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x309)[0x7f13392d5779]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x2cc)[0x7f13392d573c]
/lib64/libclassad.so.23.8.1(_ZNK7classad9Operation8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0x2cc)[0x7f13392d573c]
/lib64/libclassad.so.23.8.1(_ZNK7classad18AttributeReference8_FlattenERNS_9EvalStateERNS_5ValueERPNS_8ExprTreeEPi+0xa9)[0x7f13392a39b9]
/lib64/libclassad.so.23.8.1(_ZNK7classad7ClassAd16FlattenAndInlineEPKNS_8ExprTreeERNS_5ValueERPS1_+0x91)[0x7f13392ae191]
/lib64/libclassad.so.23.8.1(_ZN7classad12MatchClassAd24OptimizeAdForMatchmakingEPNS_7ClassAdEbPNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERKS8_SB_+0x383)[0x7f13392cca03]
condor_schedd(_ZN9Scheduler31OptimizeMachineAdForMatchmakingEPN7classad7ClassAdE+0x91)[0x555d2c1a8fc1]
condor_schedd(_ZN9Scheduler7AddMrecEPKcS1_P7PROC_IDPKN7classad7ClassAdES1_S1_PP9match_rec+0x344)[0x555d2c1b15c4]
condor_schedd(_ZN19MainScheddNegotiate21scheduler_handleMatchE7PROC_IDPKcS2_RN7classad7ClassAdES2_+0x26d)[0x555d2c19998d]
condor_schedd(_ZN15ScheddNegotiate15messageReceivedEP11DCMessengerP4Sock+0x581)[0x555d2c1ce791]
/lib64/libcondor_utils_23_8_1.so(_ZN5DCMsg19callMessageReceivedEP11DCMessengerP4Sock+0x30)[0x7f1338f78a90]
/lib64/libcondor_utils_23_8_1.so(_ZN11DCMessenger7readMsgE18classy_counted_ptrI5DCMsgEP4Sock+0x117)[0x7f1338f7a497]
condor_schedd(_ZN15ScheddNegotiate9negotiateEP4Sock+0x7b)[0x555d2c1c54ab]
condor_schedd(_ZN9Scheduler9negotiateEiP6Stream+0xefe)[0x555d2c19afee]
condor_schedd(_ZN9Scheduler23negotiatorSocketHandlerEP6Stream+0xb7)[0x555d2c19b317]
/lib64/libcondor_utils_23_8_1.so(_ZN10DaemonCore24CallSocketHandler_workerEibP6Stream+0x242)[0x7f1338fad522]
/lib64/libcondor_utils_23_8_1.so(_ZN10DaemonCore35CallSocketHandler_worker_demarshallEPv+0x21)[0x7f1338fad821]
/lib64/libcondor_utils_23_8_1.so(_ZN13CondorThreads8pool_addEPFvPvES0_PiPKc+0x3d)[0x7f1338de256d]
/lib64/libcondor_utils_23_8_1.so(_ZN10DaemonCore6DriverEv+0x103f)[0x7f1338fb0dbf]
/lib64/libcondor_utils_23_8_1.so(_Z7dc_mainiPPc+0x1936)[0x7f1338fd8716]
/lib64/libc.so.6(+0x29590)[0x7f1338429590]
/lib64/libc.so.6(__libc_start_main+0x80)[0x7f1338429640]
condor_schedd(_start+0x25)[0x555d2c1203f5]
```

## Comment (belforte, 2024-07-29T19:55:17Z)

In the meanwhile, good news from Jaime at Madison
<p><br>
</p>
<div class="moz-forward-container"><br><br>-------- Forwarded Message --------
Subject: | Re: A couple of questions related to CRAB
-- | --
Mon, 29 Jul 2024 19:51:23 +0000
Jaime Frey <jfrey@cs.wisc.edu>
Stefano Belforte <Stefano.Belforte@cern.ch>
Marco Mascheroni <marco.mascheroni@cern.ch>


<br><br>



I can reproduce the crash of the schedd on vocms059 and am working on a fix.
<div><br>
</div>
<div> - Jaime<br id="lineBreakAtBeginningOfMessage">
<div><br>
<blockquote type="cite">
<div>On Jul 25, 2024, at 1:22 PM, Stefano Belforte &lt;Stefano.Belforte@cern.ch&gt; wrote:</div>
<br class="Apple-interchange-newline">
<div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
one more note. We do not need the feature release now, but</div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
failing to upgrade to that a loaded scheduler makes me worry a bit</div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
about going from 23.0 to 24.0</div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
<br>
</div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
Our production scheduler are at 10.2 now and we have started moving</div>
<div style="margin-top: 0px; margin-bottom: 0px; caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
to 23.0</div>
<br style="caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
<div class="moz-cite-prefix" style="caret-color: rgb(0, 0, 0); font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
On 25/07/2024 19:12, Marco Mascheroni wrote:<br>
</div>
<blockquote type="cite" cite="mid:GVAP278MB074734169E9054A290D8C1AF92AB2@GVAP278MB0747.CHEP278.PROD.OUTLOOK.COM" style="font-family: Helvetica; font-size: 12px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration: none;">
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
Hi Jamie,</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
Stefano mentioned a couple of things I wanted to bring up. The first one
 is that he tried to upgrade one of the testbed schedulers to the 
development version and he got a segfault. Look for example at</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
"Stack dump for process 1154456 at timestamp 1721834410 (41 frames)"</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
in the attached SchedLog.</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
Scheduler was at 23.0.4 , then upgraded to 23.8.1 which gave the segfault. 23.7.2 was also segfaulting, and now 23.0.8 runs.</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
The second thing I wanted to bring up is that we are still using the 
refreshGSIProxy python binding method in CRAB. I believe in one of the 
last days of the HTCondor week somebody mentione if there was interest 
about keeping it. As Stefano confirms we are not
 planning of getting rid of this any time soon..</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
Thank you,</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
<br>
</div>
<div class="elementToProof" style="font-family: Aptos, Aptos_EmbeddedFont, Aptos_MSFontService, Calibri, Helvetica, sans-serif; font-size: 12pt;">
Marco</div>
</blockquote>
</div>
</blockquote>
</div>
<br>
</div>


</div>

## Comment (belforte, 2024-07-30T09:08:36Z)

given that, I will proceed with using 059 only for more testing while waiting for a fix from Madison

## Comment (belforte, 2024-08-09T14:17:20Z)

fixes in HTC 23.9 which was just release and we will test and deploy everywhere.
Handing to @aspiringmind-code for that

## Comment (belforte, 2024-08-28T09:54:29Z)

ON HOLD until JObRouter is made and verified to work #8660

## Comment (belforte, 2024-09-01T17:11:54Z)

JobRouter tested on CondorVersion: 23.9.6 on crab-sched-901

@aspiringmind-code you can proceed with moving all schedulers to that release, starting of course with vocms059 and making sure that it works before touching others.

I have already added the needed configuration flag to condor config files for all schedulers
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/255
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/256

## Comment (belforte, 2024-09-10T14:27:10Z)

rats, I changed the wrong file in puppet. New MR is coming
done: https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/258
change tested:
```
belforte@vocms0107/~> condor_config_val JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES 
True
```
it will propagate to all schedulers once puppet runs

## Comment (aspiringmind-code, 2024-09-26T12:01:45Z)

@belforte All schedulers have been updated to condor version 23.9.6

## Comment (belforte, 2024-09-26T12:45:36Z)

very good. YOu can close. And enable v2 bindings on preprod TW.
We can surely enable it also on all dev schedulers, but I leave it to you and Wa decide how to configure your test setup
