# dmwm/CRABServer issue #8285: replace usage of deprecated classad.parseOld

State: closed
Opened: 2024-03-14T20:48:45Z
Closed: 2024-03-25T22:37:02Z
Labels: Type: Bug, alma9
URL: https://github.com/dmwm/CRABServer/issues/8285

## Opening post (belforte, 2024-03-14T20:48:45Z)

with reference to https://github.com/dmwm/CRABServer/issues/8258#issuecomment-1997664317

In El9/Alma9 with HTCondor 10.2 , RetryJob badly crashes at line 108 here
https://github.com/dmwm/CRABServer/blob/8ad7dca366b8a6e4143d67a2eae7d57b2585946c/src/python/TaskWorker/Actions/RetryJob.py#L103-L118
with a core dump.

This part of the code is only executed when resubmitting a job/

Trying to open and parse same file on vocms059, HTC 10.0.9 on CC7 I get instead
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
classad.ClassAdParseError: None
```

So the error sort of understood.
Things are broken inside classAd.pareseOld(), which is anyhow [deprecated](https://htcondor.readthedocs.io/en/v10_0/apis/python-bindings/api/classad.html#classad.parseOld) in HTC 10.0  , so can't ask Madison to fix it !

What  I do not understand atm is how can work on CC7 since classad.parseOld() fails there too, even if not so  explosively and in EL9. 

Anyhow I will switch to the replacement classAd.parseAds which reads the out classAd file w/o errors on both CC7 and Alma9. 

Given the complexity and obscurity of PostJob and RetryJob a strong validation will be important :-(

## Comment (belforte, 2024-03-15T09:43:19Z)

Looking for a simple example to post here, I found that the problem seems to come from the empty line at the bottom of the `SPOOL_DIR/finished_jobs/job.N.r` files.

Here's the reproduces on A:
```
belforte@crab-sched-901/~> condor_version
$CondorVersion: 10.2.0 2023-01-05 BuildID: 621409 PackageID: 10.2.0-1 $
$CondorPlatform: x86_64_AlmaLinux9 $
belforte@crab-sched-901/~> cat ADS-no-emptyline
cat: ADS-no-emptyline: No such file or directory
belforte@crab-sched-901/~> cat > ADS-no-emptyline
ClusterId = 246
belforte@crab-sched-901/~> 
belforte@crab-sched-901/~> 
belforte@crab-sched-901/~> cat ADS-no-emptyline 
ClusterId = 246
belforte@crab-sched-901/~> cat ADS
ClusterId = 246

belforte@crab-sched-901/~> python3
Python 3.9.18 (main, Jan  4 2024, 00:00:00) 
[GCC 11.4.1 20230605 (Red Hat 11.4.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import classad
>>> with open('ADS-no-emptyline','r') as fh: classad.parseOld(fh)
... 
<stdin>:1: DeprecationWarning: ClassAd Deprecation: parseOld is deprecated; use parseOne, parseNext, or parseAds instead.
[ ClusterId = 246 ]
>>> with open('ADS','r') as fh: classad.parseOld(fh)
... 
/usr/include/c++/11/bits/basic_string.h:1059: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::operator[](std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::size_type) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference = char&; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]: Assertion '__pos <= size()' failed.
Aborted (core dumped)
belforte@crab-sched-901/~> 
```

While on CC7:
```
belforte@vocms0199/~> condor_version
$CondorVersion: 10.0.9 2023-09-28 BuildID: 678199 PackageID: 10.0.9-1 $
$CondorPlatform: x86_64_CentOS7 $
belforte@vocms0199/~> python3
Python 3.6.8 (default, Nov 14 2023, 16:29:52) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import classad
>>> with open('ADS-no-emptyline','r') as fh: classad.parseOld(fh)
... 
[ ClusterId = 246 ]
>>> with open('ADS','r') as fh: classad.parseOld(fh)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
classad.ClassAdParseError: None
>>> 
```
our python code handes the 'None`, but not the assertion failure in C++

So we can start with removing the empty line at the bottom, and take a bit of time to fully validate replacing `classad.parseOld()` with `classad.parseAds()`, although in simple test this works perfectly fine.

## Comment (belforte, 2024-03-15T10:13:40Z)

the extra empty line is a "feature" of the stdout from `condor_q`. Adding `| grep =` in here should do
https://github.com/dmwm/CRABServer/blob/8ad7dca366b8a6e4143d67a2eae7d57b2585946c/src/python/TaskWorker/Actions/PostJob.py#L1943
At least as a quick patch to progress with testing on alma9

## Comment (belforte, 2024-03-18T18:01:57Z)

there's actually a mix of all manners of using classad parsing in current code base.
All of these are used in various files
* the deprecated: `parse()`, `parseOld` - the former only support classAds in new formatn, the latter only in old format
* the valid : `parseOne()`, `parseAds()` - `parseAds` automatically adapts to new/old format

so there is no need to do extensive validation of the new `parseAds`, all in all i

## Comment (belforte, 2024-03-19T20:20:37Z)

the new `classad.parseAds` is an **iterator** while `classad.parseOld` was returning a full classAd object :-(

## Comment (belforte, 2024-03-19T20:32:06Z)

looks like `classad.parseOne(filehandle)` is what we should use to replace `classad.parseOld`
https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/classad.html
![image](https://github.com/dmwm/CRABServer/assets/1837785/85098448-e9bb-4f3e-88f0-e29bc40d337a)
to be compared with
![image](https://github.com/dmwm/CRABServer/assets/1837785/12270dd1-fa90-4877-aae8-3cbb5c52e7da)

## Comment (belforte, 2024-03-19T21:24:39Z)

testing new fix running StatusTracking again
- [ ] https://github.com/dmwm/CRABServer/issues/8300 - automatic splitting main job still running after 20h. killed, try again.
- [x] https://github.com/dmwm/CRABServer/issues/8301

## Comment (belforte, 2024-03-21T09:47:41Z)

try again to tag and validate

## Comment (belforte, 2024-03-25T22:39:22Z)

more cleanup and fixes in #8302  
- [x] tested automatic splitting on my account, OK https://cmsweb-test2.cern.ch/crabserver/ui/task/240325_213003%3Abelforte_crab_20240325_222958
- [x] Jenkins CCV and ST #8303
