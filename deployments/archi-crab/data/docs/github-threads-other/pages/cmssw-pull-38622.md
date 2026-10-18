# cms-sw/cmssw pull request #38622: Modifiers not being set properly in EventConfig for data (GEM RecHits not in latest data)

State: closed
Opened: 2022-07-07T04:43:59Z
Closed: 2022-07-07T17:25:36Z
Merged: 2022-07-07T17:25:36Z
Labels: operations-approved, fully-signed, tests-approved, orp-approved, urgent, code-checks-approved
Milestone: CMSSW_12_5_X
URL: https://github.com/cms-sw/cmssw/pull/38622

## Opening post (watson-ij, 2022-07-07T04:43:59Z)

#### PR description:

We noticed there are no GEM rechits being added to the data output recently (in particular in the latest collision events), and when trying out Configuration/DataProcessing/test/RunPromptReco.py to see what gets added, I traced it back to Configuration/DataProcessing/python/Repack.py loading Configuration.EventContent.EventContent_cff before the era is set (it gets set after Scenario.py is loaded, which is loading Repack.py), so that modifier chains don't seem to be included at all. In particular, the run3_GEM modifier chain in RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py is not set when the EventContent is loaded by the Repack.py file (but would be if the eras are set by the scenario before the EventContent cff is loaded). Could someone clarify if my understanding is correct but this is expected (it appears the change to Repack.py was made 2 months ago?), or if not expected is the fix okay and should I backport this? Otherwise let me know if my understanding is wrong.

@jshlee 
@slowmoyang 

<!-- Please replace this text with a description of the feature proposed or problem addressed, specifying:
  - what changes are expected in the output if any, 
  - what other PRs or externals it depends upon if any,
  - link to any additional material useful to provide a documentation for this PR (slides, JIRA tickets, related pull requestes, hypernews, TWiki or Indico pages)  -->

#### PR validation:

Checked the output of Configuration/DataProcessing/test/RunPromptReco.py with ppEra_Run3 scenario before and after the change:

before the local muon content looks like:
```
    'keep *_dt4DSegments_*_*',
    'keep *_dt4DCosmicSegments_*_*',
    'keep *_cscSegments_*_*',
    'keep *_rpcRecHits_*_*'
```
after:
```
    'keep *_dt4DSegments_*_*',
    'keep *_dt4DCosmicSegments_*_*',
    'keep *_cscSegments_*_*',
    'keep *_rpcRecHits_*_*',
    'keep *_gemRecHits_*_*',
    'keep *_gemSegments_*_*'
```

I used the command 
```
python3 ${CMSSW_BASE}/src/Configuration/DataProcessing/test/RunPromptReco.py \
    --scenario=ppEra_Run3 \
    --global-tag=123X_dataRun3_Prompt_v12 \
    --reco --aod \
    --lfn /store/whatever
```
<!-- Please replace this text with a description of which tests have been performed to verify the correctness of the PR, including the eventual addition of new code for testing like unit tests, test configurations, additions or updates to the runTheMatrix test workflows -->

#### If this PR is a backport please specify the original PR and why you need to backport that PR. If this PR will be backported please specify to which release cycle the backport is meant for:

<!-- Please replace this text with any link to the master PR, or the intended backport release cycle numbers -->

Before submitting your pull requests, make sure you followed this checklist:
- verify that the PR is really intended for the chosen branch
- verify that changes follow [CMS Naming, Coding, And Style Rules](http://cms-sw.github.io/cms_coding_rules.html)
- verify that the PR passes the basic test procedure suggested in the [CMSSW PR instructions](https://cms-sw.github.io/PRWorkflow.html)

<!-- Please delete the text above after you verified all points of the checklist  -->

## Comment (cmsbuild, 2022-07-07T04:51:56Z)

-code-checks

Logs: https://cmssdt.cern.ch/SDT/code-checks/cms-sw-PR-38622/30912

ERROR: Unable to merge PR.

See log https://cmssdt.cern.ch/SDT/code-checks/cms-sw-PR-38622/30912/cms-checkout-topic.log

## Comment (cmsbuild, 2022-07-07T05:01:07Z)

+code-checks

Logs: https://cmssdt.cern.ch/SDT/code-checks/cms-sw-PR-38622/30913

- This PR adds an extra 12KB to repository

## Comment (cmsbuild, 2022-07-07T05:01:33Z)

A new Pull Request was created by  @watson-ij (Ian J. Watson) for master.

It involves the following packages:

- Configuration/DataProcessing (**operations**)


@cmsbuild, @perrotta, @qliphy, @fabiocos, @davidlange6 can you please review it and eventually sign? Thanks.
@Martin-Grunewald, @missirol, @fabiocos this is something you requested to watch as well.
@perrotta, @dpiparo, @qliphy you are the release manager for this.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-cmds.html">here</a>

## Comment (watson-ij, 2022-07-07T05:11:14Z)

please test

## Comment (perrotta, 2022-07-07T06:01:02Z)

@germanfgv could you please have a look?

## Comment (davidlange6, 2022-07-07T08:16:37Z)

The repack config should have no impact on prompt reco. What "data output" do you mean exactly?

> On Jul 7, 2022, at 8:01 AM, Andrea Perrotta ***@***.***> wrote:
> 
> 
> @germanfgv could you please have a look?
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> You are receiving this because you were mentioned.
>

## Comment (germanfgv, 2022-07-07T08:28:13Z)

@watson-ij It's not clear to how or why  this change would affect the reco output. I'll check on this.

## Comment (watson-ij, 2022-07-07T08:28:22Z)

For example:
`edmDumpEventContent root://eoscms.cern.ch//eos/cms/tier0//store/data/Run2022A/SingleMuon/AOD/PromptReco-v1/000/354/964/00000/0afb1f87-43db-42bf-989b-768d7ce882b7.root`
has no rechits (from July 3), while
```
input_file=/store/data/Commissioning2022/MinimumBias/AOD/PromptReco-v1/000/351/020/00000/2a56da7f-049d-49e7-95a5-7cc4fdb5d74e.root
edmDumpEventContent root://cmsxrootd-site.fnal.gov/${input_file}
```
does (from April, just before the change to Repack.py). The issue seems to be that EventContent is pulled in in Repack and cached, so the modifiers don't run when its pulled in later in the actual process (at least, if you generate the config pickle with the Configuration/DataProcessing/test/RunPromptReco.py method I indicated).

## Comment (watson-ij, 2022-07-07T08:39:42Z)

So, unless I'm missing some context, those two files should have the same content (at least for GEM). If I'm off-base with this though (could be), I apologize. Maybe @slowmoyang can say more about the files if needed, he helped find and debug the issue also.

If you add some print statements to `RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py` before and after the GEM modify, and run the command in the description with and without my changes, you should be able to see the effect:

(the commented out for loop was a test, but it did not seem to be an actual issue)
```
diff --git a/RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py b/RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py
index 962601e918b..34f0dcd09a3 100644
--- a/RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py
+++ b/RecoLocalMuon/Configuration/python/RecoLocalMuon_EventContent_cff.py
@@ -14,12 +14,23 @@ from Configuration.Eras.Modifier_run2_GEM_2017_cff import run2_GEM_2017
 from Configuration.Eras.Modifier_run3_GEM_cff import run3_GEM
 from Configuration.Eras.Modifier_phase2_muon_cff import phase2_muon
 from Configuration.Eras.Modifier_bParking_cff import bParking
-for e in [run2_GEM_2017, run3_GEM]:
-    e.toModify( RecoLocalMuonAOD, 
+print('before', RecoLocalMuonAOD.outputCommands)
+#for e in [run2_GEM_2017, run3_GEM]:
+
+run2_GEM_2017.toModify( RecoLocalMuonAOD, 
+                outputCommands = RecoLocalMuonAOD.outputCommands + [
+        'keep *_gemRecHits_*_*', 
+        'keep *_gemSegments_*_*'])
+run3_GEM.toModify( RecoLocalMuonAOD, 
                 outputCommands = RecoLocalMuonAOD.outputCommands + [
         'keep *_gemRecHits_*_*', 
         'keep *_gemSegments_*_*'])
 
+print('after', RecoLocalMuonAOD.outputCommands)
+
+# import pdb
+# pdb.set_trace()
+
 phase2_muon.toModify( RecoLocalMuonAOD, 
     outputCommands = RecoLocalMuonAOD.outputCommands + [
         'keep *_me0RecHits_*_*', 
```

## Comment (cmsbuild, 2022-07-07T08:58:45Z)

+1

**Summary**: https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-da417a/26035/summary.html
**COMMIT**: f2c154cd094929014888cde8c9c7e243522a0e41
**CMSSW**: CMSSW_12_5_X_2022-07-06-2300/el8_amd64_gcc10
**User test area**: For local testing, you can use `/cvmfs/cms-ci.cern.ch/week0/cms-sw/cmssw/38622/26035/install.sh` to create a dev area with all the needed externals and cmssw changes.



The following merge commits were also included on top of IB + this PR after doing git cms-merge-topic: 
 - @DryRun cms-sw/cmssw#38601

You can see more details here:
https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-da417a/26035/git-recent-commits.json
https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-da417a/26035/git-merge-result


## Comparison Summary



**Summary**:
 - No significant changes to the logs found
 - Reco comparison results: 6 differences found in the comparisons
 - DQMHistoTests: Total files compared: 50
 - DQMHistoTests: Total histograms compared: 3654771
 - DQMHistoTests: Total failures: 14
 - DQMHistoTests: Total nulls: 0
 - DQMHistoTests: Total successes: 3654735
 - DQMHistoTests: Total skipped: 22
 - DQMHistoTests: Total Missing objects: 0
 - DQMHistoSizes: Histogram memory added: 0.0 KiB( 49 files compared)
 - Checked 208 log files, 45 edm output root files, 50 DQM output files
 - [TriggerResults](https://cmssdt.cern.ch/SDT/jenkins-artifacts/baseLineComparisons/CMSSW_12_5_X_2022-07-06-2300+da417a/51438/triggerResults): no differences found

## Comment (seungjin-yang, 2022-07-07T10:04:11Z)

@perrotta, @davidlange6, @germanfgv

[Configuration/DataProcessing/test/RunPromptReco.py](https://github.com/cms-sw/cmssw/blob/master/Configuration/DataProcessing/test/RunPromptReco.py) creates an instance of [Process](https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/FWCore/ParameterSet/python/Config.py#L102) class using child classes of Scenario class.


```python
from Configuration.DataProcessing.GetScenario import getScenario
class RunPromptReco:
    def __call__(self):
        ...
        try:
            scenario = getScenario(self.scenario) # NOTE: our self.scenario is "ppEra_Run3"
        ...
        process = scenario.promptReco(self.globalTag, **kwds)
        ...
```
---------------

So, we need to investigate `Scenario`. In [Configuration/DataProcessing/python/Reco.py](https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/Configuration/DataProcessing/python/Reco.py), which is a child of `Scenario`, you can see that `Scenario` module is loaded first, and then `Reco` class is defined. Then, `promptReco` method of `Reco` class creates an instance of`Process` class with `ModifierChain` with `Era`. It means when we run `RunPromptReco.py`, `Scenario` is loaded and then `Process` is created.


```python
from Configuration.DataProcessing.Scenario import *
class Reco(Scenario):
    def __init__(self):
        ...
        self.cbSc=self.__class__.__name__
        self.promptModifiers = cms.ModifierChain()
        ...

    def promptReco(self, globalTag, **args):
        # NOTE: args (deliverd by RunPromptReco.py) == {'outputs': [{'dataTier': 'RECO', 'eventContent': 'RECO', 'moduleLabel': 'write_RECO'}]}
        ...
        options = Options()
        options.__dict__.update(defaultOptions.__dict__)
        options.scenario = self.cbSc % NOTE self.cbSc == "pp"
        options.step = 'RAW2DIGI,L1Reco,RECO'+self.recoSeq+eiStep+step+PhysicsSkimStep+miniAODStep+',DQM'+dqmStep+',ENDJOB'
        ... 
        process = cms.Process('RECO', cms.ModifierChain(self.eras, self.promptModifiers) )
        cb = ConfigBuilder(options, process = process, with_output = True)
        cb.prepare()
        ...
        return process
```
---------------

Let's keep track of `Scenario` module.

[Configuration/DataProcessing/python/Scenario.py](https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/Configuration/DataProcessing/python/Scenario.py) loaded the `Repack` module.
```python
from Configuration.DataProcessing.Repack import repackProcess
class Scenario(object):
    ...
```
[Configuration/DataProcessing/python/Repack.py](https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/Configuration/DataProcessing/python/Repack.py) loads `EventContent_cff` module, which loads a bunch of configuration files containing Modifier.toModify.
```python
...
from Configuration.EventContent.EventContent_cff import RAWEventContent
...
def repackProcess(**args):
    ...
```
-------------
However, `Modifier.toModify` does nothing when its `__chosen` attribute is false and `__chosen` is set to false in `__init__` method. Modifier.__chosen is set to `true` in `Process.__init__`.  Because `EventContent_cff` module is loaded before `Process.__init__` is called, all `Modifier.toModify` do nothing. (i.e. gemRecHits is not added into  EventContent)

- https://github.com/cms-sw/cmssw/blob/master/FWCore/ParameterSet/python/Config.py#L1777-L1867
```python
class Modifier(object):
    def __init__(self):
        self.__chosen = False
    def toModify(self,obj, func=None,**kw):
        Modifier._toModifyCheck(obj,func,**kw)
        if not self._isChosen():
            return
        Modifier._toModify(obj,func,**kw)
    def _setChosen(self):
        """Should only be called by cms.Process instances"""
        self.__chosen = True
    def _isChosen(self):
        return self.__chosen
```

- https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/FWCore/ParameterSet/python/Config.py#L102-L149
```python
class Process(object):
    def __init__(self,name,*Mods):
        ...
        self.__dict__['_Process__modifiers'] = Mods
        ...
        for m in self.__modifiers:
            m._setChosen()
```

-----------------

Then, back to `Reco.promptReco`. `promptReco` method creates an instance of `Process` and then assigns a lot of attributes to `Process` using `ConfigBuilder.prepare`.

```python
from Configuration.DataProcessing.Scenario import *
class Reco(Scenario):
    def __init__(self):
        ...
        self.cbSc=self.__class__.__name__
        self.promptModifiers = cms.ModifierChain()
        ...

    def promptReco(self, globalTag, **args):
        # NOTE: args (deliverd by RunPromptReco.py) == {'outputs': [{'dataTier': 'RECO', 'eventContent': 'RECO', 'moduleLabel': 'write_RECO'}]}
        ...
        options = Options()
        options.__dict__.update(defaultOptions.__dict__)
        options.scenario = self.cbSc % NOTE self.cbSc == "pp"
        options.step = 'RAW2DIGI,L1Reco,RECO'+self.recoSeq+eiStep+step+PhysicsSkimStep+miniAODStep+',DQM'+dqmStep+',ENDJOB'
        ... 
        process = cms.Process('RECO', cms.ModifierChain(self.eras, self.promptModifiers) )
        cb = ConfigBuilder(options, process = process, with_output = True)
        cb.prepare()
        ...
        return process
```

-----------------

In [Configuration/Applications/python/ConfigBuilder.py](https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/Configuration/Applications/python/ConfigBuilder.py), we meet the event content configuration file. In the `pp` scenario, the used event content cff file is the same as one loaded in `Configuration/DataProcessing/python/Repack.py`. 
`Process` loads "Configuration/EventContent/EventContent_cff" with modifiers whose `__chosen` are true using `__import__` BUT python get `EventContent_cff` module from the global cache without creating new one. So, all `Modifer.toModify` are not called. So, `gemRecHits` and `gemSegments` are still dropped. In other hand, when the scenario is `cosmics`, new `EventContentCosmics_cff` and `*_Cosmics_cff` modules are loaded, `Modifer.toModify` is called, and gem objects are kept.

Please refer [When I edit an imported module and reimport it, the changes don’t show up. Why does this happen?](https://docs.python.org/3/faq/programming.html?highlight=__pycache__#when-i-edit-an-imported-module-and-reimport-it-the-changes-don-t-show-up-why-does-this-happen) for more details. 


```python
class ConfigBuilder(object):
    def __init__(self, options, process = None, with_output = False, with_input = False ):
        ...
        self.EVTCONTDefaultCFF="Configuration/EventContent/EventContent_cff"
        ...
        if self._options.scenario=='cosmics':
            ...
            self.EVTCONTDefaultCFF="Configuration/EventContent/EventContentCosmics_cff"
            ...
        if self._options.scenario=='HeavyIons':
            ...
            self.EVTCONTDefaultCFF="Configuration/EventContent/EventContentHeavyIons_cff"
            ...

    def loadAndRemember(self, includeFile):
        """helper routine to load am memorize imports"""
        # we could make the imports a on-the-fly data method of the process instance itself
        # not sure if the latter is a good idea
        includeFile = includeFile.replace('/','.')
        self.imports.append(includeFile)
        self.process.load(includeFile)
        return sys.modules[includeFile]

    def prepare(self, doChecking = False):
        """ Prepare the configuration string and add missing pieces."""
        self.loadAndRemember(self.EVTCONTDefaultCFF)  #load the event contents regardless
        ...
```

- https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_6/FWCore/ParameterSet/python/Config.py#L720-L723
```python
class Process(object):
    def load(self, moduleName):
        moduleName = moduleName.replace("/",".")
        module = __import__(moduleName)
        self.extend(sys.modules[moduleName])
```



-----
Let me just recap what's happened.

1. `EventContent_cff` is loaded in `Repack.py` before calling `Process.__init__`, which set `Modifier.__chosen` to true. So, all `Modifer.toModify` do nothing.
2. `Process.__init__` is called.
3. `EventContent_cff` is imported again, but python3 get EventContent_cff from the cache without creating a new module. So, `Modifier.toModify` is not called.


Let me know if anything is unclear.

## Comment (slava77, 2022-07-07T13:07:46Z)

> Let me just recap what's happened.
> 
>     1. `EventContent_cff` is loaded in `Repack.py` before calling `Process.__init__`, which set `Modifier.__chosen` to true. So, all `Modifer.toModify` do nothing.

this analysis makes sense; good catch.
Apparently the addition is somewhat recent:
#37791 in 124X and #38017 in 12_3_X ( CMSSW_12_3_3_patch1).
I guess we may be missing more than just GEM rh.

## Comment (slava77, 2022-07-07T13:44:53Z)

> I guess we may be missing more than just GEM rh.

IIUC, only `pps` is also going to be lost (more issues would appear in HI processing, but that still has some time to get a fix).

## Comment (rappoccio, 2022-07-07T13:51:20Z)

urgent

## Comment (tvami, 2022-07-07T13:56:03Z)

urgent
 * for Sal <3

## Comment (perrotta, 2022-07-07T17:25:13Z)

+1
- It fixes https://github.com/cms-sw/cmssw/pull/37791
- While something more error-prouf should be invented to correctly apply the modifiers in Configuration.EventContent.EventContent_cff (e.g. applying the modifiers in the file itself, and not in the caller configs?), the solution adopted here looks like patching correctly the issue noticed

## Comment (cmsbuild, 2022-07-07T17:25:35Z)

This pull request is fully signed and it will be integrated in one of the next master IBs (tests are also fine). This pull request will be automatically merged.

## Comment (seungjin-yang, 2022-07-08T15:32:41Z)

@perrotta, This PR should be backported to 12_3_X and 12_4_x, right? We're ready to backport this PR to 12_3_X and 12_4_X.

## Comment (davidlange6, 2022-10-11T07:54:53Z)

No, that's not how it works. Repack.py is not used in prompt reco (just check it yourself to see if there is any change with your PR or by introducing random stuff in repack.py)

On Jul 7, 2022 10:29 AM, "Ian J. Watson" ***@***.***> wrote:

For example:
edmDumpEventContent root://eoscms.cern.ch//eos/cms/tier0//store/data/Run2022A/SingleMuon/AOD/PromptReco-v1/000/354/964/00000/0afb1f87-43db-42bf-989b-768d7ce882b7.root
has no rechits (from July 3), while

input_file=/store/data/Commissioning2022/MinimumBias/AOD/PromptReco-v1/000/351/020/00000/2a56da7f-049d-49e7-95a5-7cc4fdb5d74e.root
edmDumpEventContent root://cmsxrootd-site.fnal.gov/${input_file}


does (from April, just before the change to Repack.py). The issue seems to be that EventContent is pulled in in Repack and cached, so the modifiers don't run when its pulled in later in the actual process (at least, if you generate the config pickle with the Configuration/DataProcessing/test/RunPromptReco.py method I indicated).

—
Reply to this email directly, view it on GitHub<https://github.com/cms-sw/cmssw/pull/38622#issuecomment-1177247631>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/ABGPFQYFOFXNNXU53A4GJGLVS2ILDANCNFSM52362F5A>.
You are receiving this because you were mentioned.Message ID: ***@***.***>
