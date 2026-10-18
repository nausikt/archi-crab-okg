# dmwm/CRABServer issue #6640: make jobs work with Py3 CMSSW

State: closed
Opened: 2021-06-10T14:44:05Z
Closed: 2021-08-31T15:12:57Z
Labels: Status: In Progress, Area: zPython3, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/6640

## Opening post (belforte, 2021-06-10T14:44:05Z)

pasting here a mail exchange with Shahzad.
This is needed regardless of CRABServer/TW etc. running in py3. Maybe as "simple" as
move from current WMCore tag 1.4.6.crab1 to more recent one.. and hope that there are no new
issues with py2/3 comaptibility changes !

For convenience, the [link](https://github.com/dmwm/WMCore/commit/2bfe9b7c7e06bf76370e89e4ea23c768f03a0efc ) to the commit which Shahzad mentioned


```
We have seen this issue and reason is that WM Core is sourcing python2 packages
and setting them for cmssw too [a] . This was fixed
https://github.com/dmwm/WMCore/commit/2bfe9b7c7e06bf76370e89e4ea23c768f03a0efc 
Looks like you need to update WMCore 

--Shahzad

[a]
==== Python discovery STARTING ====
Job requires OS: rhel7, thus setting ScramArch to: slc7_amd64_gcc630
WMAgent bootstrap: COMP Python path is: /cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external
WMAgent bootstrap: latest python release is: 2.7.13-comp
WMAgent bootstrap: found python2 at..
/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python/2.7.13-comp/bin/python2
________________________________________
From: Stefano Belforte
Sent: 10 June 2021 13:28
To: Malik Shahzad Muzaffar; Daina Dirmaite; David Lange
Cc: Stefano Belforte
Subject: Re: crab in CMSSW_12_0_X env

Hi Shahzad, David,
so that submitted w/o problems, but then job failed in cmsRun [1]
Can you say if this is something at your end or something for me to investigate ?

At first sight it is a complain about this lines

belforte@lxplus747/LOCAL> head -4 /cvmfs/cms.cern.ch/slc7_amd64_gcc900/cms/cmssw/CMSSW_12_0_0_pre2_PYTHON3/python/FWCore/ParameterSet/Config.py
#!/usr/bin/env python

### command line options helper
from __future__ import print_function

Stefano

On 09/06/2021 22:53, Stefano Belforte wrote:
> quick test (submit+status) was fine.
>
> On 09/06/2021 17:07, Malik Shahzad Muzaffar wrote:
>> Can you try  to run tests against  CMSSW_12_0_0_pre2_PYTHON3 release (cmsRun in this releases uses py3)?

[1]
from
https://cmsweb.cern.ch/scheddmon/0198/cmsprd/210609_204559:belforte_crab_20210609_224555/job_out.1.0.txt

== CMSSW: cmsRun  -j FrameworkJobReport.xml PSet.py
== CMSSW: ----- Begin Fatal Exception 09-Jun-2021 22:54:20 CEST-----------------------
== CMSSW: An exception of category 'ConfigFileReadError' occurred while
== CMSSW:    [0] Processing the python configuration file named PSet.py
== CMSSW: Exception Message:
== CMSSW:  unknown python problem occurred.
== CMSSW: ImportError: This package should not be accessible on Python 3. Either you are trying to run from the python-future src folder or your installation of python-future is corrupted.
== CMSSW:
== CMSSW: At:
== CMSSW:   /cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/py2-future/0.18.2/lib/python2.7/site-packages/reprlib/__init__.py(7): <module>
== CMSSW:   <frozen importlib._bootstrap>(219): _call_with_frames_removed
.. more lines like that


```

## Comment (belforte, 2021-06-10T14:52:21Z)

Also this very clarifying comment by David Lange:
```
The message says that python3 is finding python2 code (the future package)
on its PYTHONPATH (or other package discovery mechanism being used)
```

## Comment (belforte, 2021-06-15T13:36:20Z)

the relevant WMCore fix is in WCore 1.4.9 which @ddaina is now testing. If all OK we will try again with
CMSSW_12_0_0_pre2_PYTHON3  (a release which defaults to python2 but has python3 in it)
and then with a Py3 workflow from CMSSW_11_3_0_pre2_PY3 (a release where python=python3).

## Comment (belforte, 2021-06-29T21:27:02Z)

On Hold waiting for WMCore developers help, see: https://github.com/dmwm/CRABServer/issues/6653

## Comment (belforte, 2021-08-30T21:38:09Z)

Back to this now that CRAB job wrapper works with new WMCore.
Testing with CMSSW_12_0_0_pre6 and latest crab-dev plus the patch for python3 https://github.com/dmwm/CRABClient/pull/5073

At first attempt, I still get
```
== CMSSW: ImportError: This package should not be accessible on Python 3. Either you are trying to run from the python-future src folder or your installation of python-future is corrupted.
```
this because I forgot to change this to make Scram to start in a clean env
https://github.com/dmwm/CRABServer/blob/cfeec5e3e1541f65c909b2431d6a0bdf43215d7b/scripts/CMSRunAnalysis.py#L628

## Comment (belforte, 2021-08-30T21:42:00Z)

Scam fixed. Now cmsRun runs !
I get this error, likely a  problem with my very old Pset
```
== CMSSW: 30-Aug-2021 23:30:22 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
== CMSSW: 30-Aug-2021 23:30:31 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
== CMSSW: ----- Begin Fatal Exception 30-Aug-2021 23:30:31 CEST-----------------------
== CMSSW: An exception of category 'PluginNotFound' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW: Exception Message:
== CMSSW: Unable to find plugin 'DemoAnalyzer' in category 'CMS EDM Framework Module'. Please check spelling of name.
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
```

## Comment (belforte, 2021-08-30T21:50:39Z)

Same PSet runs interactively.  Investigatin.

## Comment (belforte, 2021-08-30T21:56:24Z)

interactively it works but prints
```
%MSG-s LegacyModules:  AfterModConstruction 30-Aug-2021 23:49:14 CEST pre-events
The following legacy modules are configured. Support for legacy modules
is going to end soon. These modules need to be converted to have type
edm::global, edm::stream, edm::one, or in rare cases edm::limited.
  DemoAnalyzer demo
%MSG
```
I guess that in non-interactive mode they replaced that msg with a failure.
I got that msg since years, but so far it was working.
Time to update.

## Comment (belforte, 2021-08-30T22:47:24Z)

I failed to create an analyzer from workbook instructions and asked for expert help: https://hypernews.cern.ch/HyperNews/CMS/get/edmFramework/3932.html

## Comment (makortel, 2021-08-31T00:23:21Z)

> I guess that in non-interactive mode they replaced that msg with a failure.

No, the behavior should be the same (i.e. the warning message) regardless of interactive vs. non-interactive.

> I got that msg since years, but so far it was working.

You should not have, because this warning was added in 12_0_0_pre5. Eventually (around 13_0_X) it will become an exception though.

The easiest explanation for `Unable to find plugin 'DemoAnalyzer' in category 'CMS EDM Framework Module'. Please check spelling of name.`  that I can think of would be the libraries from the developer area to be missing somehow.

## Comment (belforte, 2021-08-31T13:20:47Z)

thanks @makortel 
I think the "how to make an EDM analyzer that works for CMSSW_12" is addressed in your reply in HN
https://hypernews.cern.ch/HyperNews/CMS/get/edmFramework/3932/1.html
For sake of speed I have now switched to a bare minimal PSet where I do no add anything to the release
```
belforte@lxplus7109/C12> cat minimalPS.py 
import FWCore.ParameterSet.Config as cms
process = cms.Process('NoSplit')
process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root')
)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("drop *"),
    fileName = cms.untracked.string('output.root'),
)
process.out = cms.EndPath(process.output)
```
which works interactively. Using it now to test CRAB wrapper.

## Comment (makortel, 2021-08-31T13:30:41Z)

Looks good. Do you still need a disk dataset that you asked in https://hypernews.cern.ch/HyperNews/CMS/get/edmFramework/3932/1/1.html? (I'd have to dig, the IB tests use a special cache that may or may not work for this test)

## Comment (belforte, 2021-08-31T13:42:19Z)

thanks Matti. So far I am reading from this dataset which appears to work:
/eos/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2
but since it was created in CMSSW_9 it may be that less trivial tests will fail, that's all.
So far it works in CMSSW_10 and 11, but AFAIU there is no guaranteed that future releases will always work on old data.
I think that best will be to ask P&R to create similar HammerCloud dataset for CMSSW_12.
I will follow up with them as soon as I have something that works.

## Comment (belforte, 2021-08-31T14:08:28Z)

got a first CRAB job to run with CMSSW_12_0_0_pre6
https://cmsweb-test2.cern.ch/crabserver/ui/task/210831_134818%3Abelforte_crab_20210831_154720

n.b. job ran twice, the initial one failed to read data remotely (site problem) but exited with 50115 instead of 8028. To be followed up, but not critical.

## Comment (belforte, 2021-08-31T14:11:54Z)

the TaskWorker version that works is in https://github.com/dmwm/CRABServer/releases/tag/v3.210831pre1 and now deployed on crab-dev-tw01

## Comment (belforte, 2021-08-31T14:35:26Z)

I will now look at the problem indicated in https://github.com/dmwm/CRABServer/issues/6640#issuecomment-909272990 :
- [ ] wrapper fails to properly report CMSSW exit code

this looks like in WMCore land, this raises an Exception
https://github.com/dmwm/CRABServer/blob/3fb6a7de530eb3717c31c4f5ff25a1e216f3e754/scripts/CMSRunAnalysis.py#L874-L875
where `Report` is a member of https://github.com/dmwm/WMCore/blob/7c464735d1434558a7f525081fcc7fda7c2c5fc0/src/python/WMCore/FwkJobReport/Report.py#L100
with this report
```
<FrameworkJobReport>
<SkippedFile Pfn="root://xrootd-cms.infn.it//store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root" Lfn="/store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root"/>
<FrameworkError ExitStatus="8020" Type="Fatal Exception" >
<![CDATA[
An exception of category 'FileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://xrootd-cms.infn.it//store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root'
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root
      [b] Input file root://xrootd-cms.infn.it//store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root could not be opened.
      [c] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [d] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/mc/HCNONO/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/8ADD04E5-1776-E711-A1BA-FA163E6741E0.root?tried=+1213llrxrd-redir.in2p3.fr,&xrdcl.requuid=58e4b8a7-b7e9-440a-8396-d9db782c46be
      [e] Problematic data server: cms-xrd-global.cern.ch:1094
      [f] Disabled source: cms-xrd-global.cern.ch:1094

]]>
</FrameworkError>
</FrameworkJobReport>
```
digging in, exception is raised by
https://github.com/dmwm/WMCore/blob/7c464735d1434558a7f525081fcc7fda7c2c5fc0/src/python/WMCore/Algorithms/ParseXMLFile.py#L64-L65
On the good side, for a successful job with exit code 0, the FrameworkJobReport.xml parsing works.

Will try to bump this to WMCore developers.

## Comment (belforte, 2021-08-31T15:12:57Z)

well... runs but reports wrong exit code surely is different from "does not work".
So I am closing this and will open ad hoc issues on specific problems as we find them

## Comment (belforte, 2021-08-31T15:52:35Z)

I will open a WMCore issue later, but let me take note here of the source of the FJR parsing problem,
opening the file with `vi` it is pretty clear that there is an illegal character in line 16, column 315
![Screenshot from 2021-08-31 17-48-12](https://user-images.githubusercontent.com/1837785/131534814-e8bc3f7c-6a8b-47b3-95b5-a1061dba73ca.png)
And running the parser manually the exception is also quite clear (using WMCore 1.5.2 )
```
Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from WMCore.Algorithms.ParseXMLFile import coroutine, xmlFileToNode
>>> xmlFile='FJR.xml'
>>> node = xmlFileToNode(xmlFile)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/tmp/belforte/WT/WMCore/src/python/WMCore/Algorithms/ParseXMLFile.py", line 65, in xmlFileToNode
    build(node))
  File "/tmp/belforte/WT/WMCore/src/python/WMCore/Algorithms/ParseXMLFile.py", line 88, in expat_parse
    parser.ParseFile(f)
xml.parsers.expat.ExpatError: not well-formed (invalid token): line 16, column 315
>>> 
```
it is of course debatable whether the bad guy is xroot, CMSSW or WMCore.

## Comment (makortel, 2021-08-31T16:03:54Z)

I'd say xrootd, because the character is part of a status string they give to us.

## Comment (belforte, 2021-08-31T16:15:00Z)

Yeah.. . That's too easy. Let's look for a good guy now !
If we wait for an xroot fix to properly report errors....eons.
Someone at some point has to sanitize those message.
@amaltaro @khurtado what's your take ?

## Comment (klannon, 2021-08-31T16:19:48Z)

@belforte:  If there is a problem with XRootD output, do [please file an issue](https://github.com/xrootd/xrootd/issues) with them, even if you are not confident they will fix quickly.  I happen to know right now that they're working on the v5 release series pretty actively, so there's always a chance.  If you can mention me in the issue, that would help me keep track and push for the fix to be included sooner rather than later, if feasible.

## Comment (belforte, 2021-08-31T17:01:16Z)

@klannon I'll do my best

## Comment (belforte, 2021-09-01T12:36:39Z)

xrtood issue opend: https://github.com/xrootd/xrootd/issues/1501

## Comment (belforte, 2021-09-01T12:59:16Z)

and WMcore issue too: https://github.com/dmwm/WMCore/issues/10782

I will remove my patch https://github.com/dmwm/CRABServer/pull/6751 once WMCore stops failing on this.
