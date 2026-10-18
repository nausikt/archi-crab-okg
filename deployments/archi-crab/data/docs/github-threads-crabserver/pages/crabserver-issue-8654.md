# dmwm/CRABServer issue #8654: change of memory in resubmit does not work

State: closed
Opened: 2024-08-26T20:23:30Z
Closed: 2024-08-30T09:50:49Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8654

## Opening post (belforte, 2024-08-26T20:23:30Z)

maybe also other params ?

reference task : https://cmsweb.cern.ch/crabserver/ui/task/240822_074626%3Aecannaer_crab_clustAlg_Suu8_chi3_WBWB_2017_JEC_AltDatasets_000
as per https://cms-talk.web.cern.ch/t/crab-jobs-killed-for-high-memory-usage-but-max-memory-usage-is-less-than-requested-ram/46376

Job 6 in there was submitted 7 times. In last execution [log](https://cmsweb.cern.ch:8443/scheddmon/0194/ecannaer/240822_074626:ecannaer_crab_clustAlg_Suu8_chi3_WBWB_2017_JEC_AltDatasets_000/job_out.6.7.txt) I find
```text
== JOB AD: RequestMemory = 2000
== JOB AD: RequestMemory_RAW = 2000
```
and in the SPOOL_DIR `/data/srv/glidecondor/condor_local/spool/8413/0/cluster108538413.proc0.subproc0` on `vocms0194` 
```text
[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ grep Req Job.6.submit 
RequestMemory = 2000
```
while in the PreJob log, created at same time
```text
 [crabtw@vocms0194 cluster108538413.proc0.subproc0]$ ls -l Job.6.submit 
-rw-r--r--. 1 crabtw zh 8137 Aug 23 22:01 Job.6.submit
[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ ls -l prejob_logs/prejob.6.7.txt 
-rw-r--r--. 1 crabtw zh 23367 Aug 23 22:01 prejob_logs/prejob.6.7.txt
[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ 
```

I find
```text
  RequestMemory_RAW = 4500
```
in agreement with
```text

[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ ls -l adjust_out.txt 
-rw-r--r--. 1 crabtw zh 13846 Aug 23 22:01 adjust_out.txt
[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ cat adjust_out.txt|grep RequestMemory
        RequestMemory = 4500; 
        Requirements = (true) && (TARGET.Arch == "X86_64") && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory); 
        RequestMemory_RAW = 4500; 
[crabtw@vocms0194 cluster108538413.proc0.subproc0]$ 
```

could this be a (new) bug in PreJob ? Due to the changes for "HTC Modernization" ?

## Comment (belforte, 2024-08-28T20:34:48Z)

PreJob code seems OK
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L242
and not affected by recent changes

A problem is that prejob log is full of jobs because logging initialization is not working. But in there I find both these
CRAB_RequestedMemory = 2000;
RequestMemory = 4500;

Could it be a hint ? Or simply `CRAB_RequestedMemory` is the initial value ?

hmm...
at same time as ` prejob_logs/prejob.6.7.txt` and ` prejob_logs/prejob.6.7.txt` were created, the input for PreJob was written in resubmit_info.job.6.txt
```text
 ls -l resubmit_info/job.6.txt 
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 resubmit_info/job.6.txt
```
that file is read in https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L181-L188
and content later used in 
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L305
(but I do not know what that `inkey` `outkey` stuff is)

but in the `resubmit_info` file:
```text
belforte@vocms0194/cluster108538413.proc0.subproc0> cat resubmit_info/job.6.txt |tr , '\n'|grep maxmem
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
 'maxmemory': 2000
belforte@vocms0194/cluster108538413.proc0.subproc0> 
```
actually:
```text
belforte@vocms0194/cluster108538413.proc0.subproc0> ls -l resubmit_info/
total 40
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.10.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.1.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 20:24 job.2.txt
-rw-r--r--. 1 crabtw zh 1324 Aug 23 20:24 job.3.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.4.txt
-rw-r--r--. 1 crabtw zh  757 Aug 22 21:32 job.5.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.6.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.7.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.8.txt
-rw-r--r--. 1 crabtw zh 1513 Aug 23 22:01 job.9.txt
belforte@vocms0194/cluster108538413.proc0.subproc0> cat resubmit_info/job.*.txt |tr , '\n'|grep maxmem|uniq
 'maxmemory': 2000
belforte@vocms0194/cluster108538413.proc0.subproc0> 
```
that value never changed, and IIUC it is what drives PreJob and Job.x.submit.

## Comment (belforte, 2024-08-28T20:38:24Z)

the file in resubmi_info is created (and later read) by PreJob itself
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L554-L558

I do not find that directory referenced in any other place in the source base.
I am confused

## Comment (belforte, 2024-08-28T20:42:13Z)

DagmanResubmitter has some helpful documentation
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanResubmitter.py#L97-L111

## Comment (belforte, 2024-08-28T20:44:41Z)

hmmm... this should be the intial setting
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L292-L293
then DagmanResubmitter communicates via the simple `RequestMemory`
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanResubmitter.py#L79-L86

and edits those in the target dagman job.
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanResubmitter.py#L106

The Dagman job ads are then save to _CONDOR_JOB_AD in the SPOOL_DIR where indeed
```text
belforte@vocms0194/cluster108538413.proc0.subproc0> grep RequestMemory _CONDOR_JOB_AD 
RequestMemory = 4500
RequestMemory_RAW = 4500
```
and that file is read by PreJob
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/PreJob.py#L173-L175

## Comment (belforte, 2024-08-28T20:54:58Z)

sounds like the only way is
1. fix logging in PreJob --> done in #8668 
2. add zilions of logging
3. try to resubmi in a test task

Maybe I can go through PreJob interactively, but I am not sure it will really reproduce the situation for resubmission https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3OperatorDebugging#To_run_a_pre_job_on_the_schedd

## Comment (belforte, 2024-08-28T20:56:08Z)

I should also test with an older tag. To sort of find when it broke. It will be a long work anyhow

## Comment (belforte, 2024-08-29T10:23:46Z)

I finally managed to run PreJOb with `pdb` and found that as feared I introduced this bug in https://github.com/dmwm/CRABServer/commit/f700045273ff40d510dea30441fd2eccde053af3#diff-4523635b2647add8f64521c2cb1208629e53538fde1905e60c8a57b285ebee30
![image](https://github.com/user-attachments/assets/b1b91cb7-5f7f-4609-bca9-a4049588741d)

I have changed the ads which are used to communicate from TW to Dagman via prepending `CRAB_` "for clarity", but somehow the change was not done consistently

## Comment (belforte, 2024-08-29T10:28:58Z)

I guess the problem is here
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanResubmitter.py#L79-L86

The root case was the confusion between ads meant for the JDL of the intial dagman-startup script, and ads used to communicate to various scripts how to submit jobs to grid.
I tried to clean that up using `CRAB_...` for the latter, but did not catch the resubmission use case.

## Comment (belforte, 2024-08-29T10:34:11Z)

I had only taken care of setting `CRAB_RequestedMemory` in DagmanSubmitter https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanSubmitter.py#L72

## Comment (belforte, 2024-08-29T10:35:16Z)

so..
**Dagman(Re)Submitter should set values for CRAB_xxxs classAds, which are then used in PreJob to create the JDL for vanilla jobs submission**

## Comment (belforte, 2024-08-29T19:12:30Z)

I tested on one job in crab-dev-tw01 and it works.

I will add some documentation comments

## Comment (belforte, 2024-08-30T08:35:31Z)

after review, it is fine as it is
