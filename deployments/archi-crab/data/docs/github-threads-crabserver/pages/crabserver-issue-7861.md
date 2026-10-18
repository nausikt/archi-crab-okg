# dmwm/CRABServer issue #7861: Expose json file with lumis to process

State: open
Opened: 2023-09-01T07:38:58Z
Labels: Type: Enhancement, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7861

## Opening post (lenzip, 2023-09-01T07:38:58Z)

Its is my understanding from [this discussion](https://cms-talk.web.cern.ch/t/possible-duplication-when-using-automatic-splitting-for-crab/21384/25) and [this comment](https://github.com/cms-sw/cmssw/pull/42323#issuecomment-1701200063) that crab already produces a json file with the lumis to process in each job (in addition to the CMSSW PSet), as part of the job preparation. I'd like to request that this is documented, so that tools running on nanoAOD via script, instead of CMSSW, can parse it.

## Comment (belforte, 2023-09-01T10:37:11Z)

@mapellidario can you take care as the current "job wrapper man in charge" ?

Ideally we could do a bit of preparatory work in PreDag and only ship to each job the info it needs, instead of the full list, getting rid of the concern which I debated with David Lange in that cms-talk discussion about size of the run_and_lumis.tar.gz.
Maybe at that point we can even decompress the json files in the grid working dir. 

Anyhow a  first simple step could likely be to tweak https://github.com/dmwm/CRABServer/blob/master/scripts/TweakPSet.py to produce a run/lumi json file in the standard "lumimask" format as per https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/DataStructs/LumiList.py. List of input files should be trivial. Note that we do not have a separate  run-and-lumi list for each file. The WMCore splitter machinery does not provides that. In case the jobs has multiple input files, users must be prepared for a lumi being listed but not present in one particular file.

You can surely find the best way ahead.
