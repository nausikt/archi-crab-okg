# dmwm/CRABServer issue #7529: improve log from condor-killed jobs

State: closed
Opened: 2023-02-10T11:00:50Z
Closed: 2023-07-20T10:43:21Z
Labels: Status: In Progress, Priority: TOP, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7529

## Opening post (belforte, 2023-02-10T11:00:50Z)

when condor kills a running job via periodic remove (out of time or memory, usually )we only get this
```
======== CMSRunAnalysis.py STARTING at Fri Feb 10 07:16:15 GMT 2023 ========
Now running the CMSRunAnalysis.py job in /srv...
++ pwd
+ python CMSRunAnalysis.py -r /srv -a sandbox.tar.gz --sourceURL=https://cmsweb.cern.ch/S3/crabcache_prod --jobNumber=327 --cmsswVersion=CMSSW_10_6_27 --scramArch=slc7_amd64_gcc700 --inputFile=job_input_file_list_327.txt --runAndLumis=job_lumis_327.json --lheInputFiles=False --firstEvent=None --firstLumi=None --lastEvent=None --firstRun=None --seeding=AutomaticSeeding --scriptExe=None --eventsPerLumi=None --maxRuntime=-60 '--scriptArgs=[]' -o '{}' --oneEventMode=0
======== Figuring out long exit code of the job for condor_chirp ========
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/usr/lib64/python2.7/json/__init__.py", line 290, in load
    **kw)
  File "/usr/lib64/python2.7/json/__init__.py", line 338, in loads
    return _default_decoder.decode(s)
  File "/usr/lib64/python2.7/json/decoder.py", line 366, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib64/python2.7/json/decoder.py", line 384, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
==== Failed to load the long exit code from jobReport.json.327. Falling back to short exit code ====
======== Short exit code also missing. Settint exit code to 80001 ========
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```
from top wrapper https://github.com/dmwm/CRABServer/blob/c484c2377476c3eeca32207fc4d2117bfdf714e2/scripts/gWMS-CMSRunAnalysis.sh#L54-L63

This should be improve to
1. print a timestamp to make it simple to tell the time lapse from ` CMSRunAnalysis.py STARTING` and ` Figuring out`
2. if json wrapper is not there dump the last 1K lines of `cmsRun-stdout.log`
3. a more ambitious goal is to figure out why stdout from the CMSRunAnalysis.py was not written/printed, since it prints quite several things before calling cmsRun

## Comment (belforte, 2023-02-10T11:02:14Z)

@mapellidario since you are currenlty working on wrapper, can you look into doing 1. and 2. above as well ? Feel free to think about 3. as well, but it may require some testing/debugging. The others are straightforward

## Comment (novicecpp, 2023-02-17T11:31:08Z)

From https://github.com/dmwm/CRABServer/issues/7536#issuecomment-1434463430, it would be nice if we also print single line indicate that job get kill due to timeout or other error that not control by cmsRun.

## Comment (belforte, 2023-02-17T12:40:30Z)

one general comment about this issue: the important thing is to be "quick" since there is not much time from when condor signals the process and when it kills everything and wraps up stdout to send it back to scheduler.

## Comment (belforte, 2023-02-20T14:57:28Z)

timestamp was added via https://github.com/dmwm/CRABServer/pull/7510
remaining tasks:
- [x] end stdout with one line indicating job killed bi timeout or memory (can compare classAd for this)  No, we decided to leae this to PostJob
- [x] print last lines of CMSSW log if possible, so one knows what job was  doing when interrupted (check first that printout is really missing

## Comment (mapellidario, 2023-07-20T10:43:21Z)

This was done in #7623
