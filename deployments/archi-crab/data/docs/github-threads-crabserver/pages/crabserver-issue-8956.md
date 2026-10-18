# dmwm/CRABServer issue #8956: port CRAB code to new python 3.13

State: open
Opened: 2025-02-27T15:46:32Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8956

## Opening post (belforte, 2025-02-27T15:46:32Z)

see https://github.com/dmwm/WMCore/issues/12208#issuecomment-2688340975

## Comment (belforte, 2025-02-27T15:48:35Z)

@aspiringmind-code @sinonkt 
this is up for pick... please get a sense of what it is involved, then one of you can volunteer.
I have no idea how it may impact our build scripts e.g. How closely we need to synchronize with changes in WMCore, etc. etc.

## Comment (belforte, 2025-02-27T16:14:25Z)

while you are at this, make sure that code in ServerUtilities which is shared with CRABClient stays compatible with python2.7 and be aware that CRABClient always runs with the python version set by the CMSSW Release specified by the user. Check with Shahzad if there are plans for upgrading python there.

Of course moving code which is not used by Client out of ServerUtilities in some proper (new) file in CRABServer/src/python/CRABUtils can only help, that ServerUtilities file is way too long now.

## Comment (belforte, 2025-02-27T17:12:29Z)

Additional complication: 
- scripts in the schedulers use code from GH repository but run with /usr/bin/python3
- JobWrapper (CMSRunAnalysis.py, cmscp.py) run with the python3 from /cvmfs/cms.cern.ch/COMP which is under WMCore control

So if you can have code which works with both current py3.8 and new py3.13, should be all simple, otherwise a lot of care will be needed and transition will take longer due to the need of multiple backward-compatible steps.

## Comment (belforte, 2025-02-27T17:30:27Z)

On the good side, HTCondor V2 API's should be python-version-independent. Of course to be verified.

## Comment (belforte, 2025-08-18T15:43:04Z)

Given that
* WMCore and CRAB code are "feature frozen" now
* alma9 will have security fixes (and hence be usable as container base) until [2032](https://wiki.almalinux.org/release-notes/)
* python 3.9 is and will always be the python version in Alma9

I believe that we can safely assume that we only need to be compliant with python 3.9 in order to be future-proof.

To keep full compatibility with WMCore, it is good that our code works in 3.12 as well, but we should not use anything which is only available in that.
As far as I know, python3.9 compatible code will also run in py3.12

We can (and likely should) move TW image to use Alma9 container as base, instead of python3.8 Debian one.

Note that in the schedulers (AP's) we already use alma9 and Python 3.9.21

## Comment (nausikt, 2025-08-18T15:56:33Z)

> Given that
> 
> * WMCore and CRAB code are "feature frozen" now
> * alma9 will have security fixes (and hence be usable as container base) until [2032](https://wiki.almalinux.org/release-notes/)
> * python 3.9 is and will always be the python version in Alma9
> 
> I believe that we can safely assume that we only need to be compliant with python 3.9 in order to be future-proof.
> 
> To keep full compatibility with WMCore, it is good that our code works in 3.12 as well, but we should not use anything which is only available in that. As far as I know, python3.9 compatible code will also run in py3.12
> 
> We can (and likely should) move TW image to use Alma9 container as base, instead of python3.8 Debian one.
> 
> Note that in the schedulers (AP's) we already use alma9 and Python 3.9.21

Thank you Stefano.

## Comment (belforte, 2025-08-18T16:01:37Z)

looking at Dario's exploration (first comment in this issue) I suspect that more changes are needed to go from py3.9 compatible to py3.13 compatible, but they seems all "easy". It is likely also time to remote relics of py2 to py3 migration (`from __future__ import ... `)

## Comment (belforte, 2025-12-05T16:19:16Z)

THis is getting more urgent since also CMSSW is moving to python 3.12 https://github.com/cms-sw/cmssw/issues/49327

Once they do CRABClient needs to be compatible. 

So I am rasing priority in our workplan

## Comment (belforte, 2025-12-05T16:23:24Z)

See also https://github.com/dmwm/CRABClient/pull/5350 (so maybe there's nothing to do in CLient ?)
And https://github.com/dmwm/CRABServer/issues/8804 and https://github.com/dmwm/CRABServer/issues/9150

## Comment (nausikt, 2025-12-05T16:37:38Z)

Acknowledge Man, will do next week along side Argo enabling.

## Comment (nausikt, 2026-01-16T13:31:07Z)

Feeling grateful for [Dario's extra miles made for Tier0 and CRAB](https://github.com/dmwm/WMCore/issues/12208#issuecomment-2688340975) and your guidelines here which eased the process indeed.

Since, this porting to py3.12 up-to py3.13 compatible code is also more or less coupling with other issues i.e. 
1. [moving to latest WMCore 2.4.5 (freeze) version #9150](https://github.com/dmwm/CRABServer/issues/9150).
2. ensure that [minor backward refinement for timeless module import syntax #8804](https://github.com/dmwm/CRABServer/issues/8804) works on py3.12.
3. [Migrate TW image to Alma9, maintain OS and Python version homogeneity with Schedd (AP's), support Py3.9 → Py3.12 #9252](https://github.com/dmwm/CRABServer/issues/9252), as you mentioned aboved.

Therefore, let me break it down into multiple PRs for ease of approval, also split them into two phases as following.
\*\**where all ***Phase 1*** PRs have been ***tested*** as a whole as you can see in* #9251\*\*

## Phase 1
*Ensure *buildable* and runnable on py3.12*, ***regardless** of OS-env*.
- [x] 1. make it compliant with **WMCore 2.4.5**, where *py3.13* support is **guaranteed**.
    PR ***safe*** to merge: #9254 *(was cherry-picked into [3])*
- [x] 2. address CRAB's specific *py3.9* - *py3.12* deprecations and code refinement for better long term support.
    PRs ***safe*** to merge: 
            2.1. https://github.com/dmwm/CRABServer/pull/9260
            2.2. https://github.com/dmwm/CRABServer/pull/9261
            2.3. https://github.com/dmwm/CRABServer/pull/9253
           References: [PEP632](https://peps.python.org/pep-0632/), [PEP389](https://peps.python.org/pep-0389/#deprecation-of-optparse)

*N.B. Latest WMCore was 2.4.5.2 (so called [wmfreeze](https://registry.cern.ch/harbor/projects/1771/repositories/wmagent-base/artifacts-tab)), also wmagent-base image was bumped to Debian Trixie where WM team **treated** Trixie & python 3.12 as default OS & py3 baseline for long term support.*

## Phase 2
*Moving toward **Alma9**: ensure py3.13 availability and future (3.13+) support, revise the GFAL updating method, especially in Alma9 env (where expected to be much easier).*
\*\****Most of the detail will be discussed in separated issue [3]***\*\*
- [x] 3. https://github.com/dmwm/CRABServer/issues/9252 https://github.com/dmwm/CRABServer/pull/9265
- [x] 4. Once we can lift to py3.13 (better done in **Alma9**), we will address py3.12 -> py3.13 minor shifts. 
             > *P.S. Actually, no changes needed. See also [deprecations in py3.13](https://docs.python.org/3.12/deprecations/index.html#pending-removal-in-python-3-13)* 
- [x] 5.  revise How can we update gfal and ldap deps in **Alma9** env. (Now, both CRABServer and TaskWorker were refactored [3] lifted to Alma9 with full control, mostly been decoupled from WMCore derived images.)
- [ ] 6. port CRABClient to new py3.13

*P.S. **Alma9** have py3.9 (default) and could naturally provision python up-to py3.12. more details in issue [3]*
*P.S. **Alma9** is where CRAB aims to live for long term, maintaining a homogenous OS-env with Schedd APs* which point to 3.9 as default.

## Comment (belforte, 2026-01-16T14:16:55Z)

Very nice. Thanks Krittin.
I have a technical question, we are using deprecated OptionParser in CRABClient 
https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/CRABOptParser.py

Could that be moved to argparse as well ? We need to be compatible with python down to 2.7.  Latest CMSSW_16_1 comes with python 3.9 and still works with optparse, but be a bit future proof there will be good.

## Comment (nausikt, 2026-01-16T14:28:23Z)

Acknowledged Stefano, will covered it there too. https://github.com/dmwm/CRABClient/issues/5424
