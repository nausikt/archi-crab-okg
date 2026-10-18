# dmwm/CRABServer issue #9294: allow a site to force its ASO users to use Rucio

State: closed
Opened: 2026-04-09T15:44:53Z
Closed: 2026-04-14T23:20:48Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9294

## Opening post (belforte, 2026-04-09T15:44:53Z)

The Italian INFN community would like to at least experiment with forcing their local users to use ASO via Rucio, in order to facilitate disk quota management.

As discussed with @dciangot a viable strategy could be:

* introduce a configuration dictionary, maintained via `puppet` similarly to [tw_htcondorSchedds](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/data/hostgroup/vocmsglidein/crabtaskworker.yaml?ref_type=heads#L25) 
   * the dictionary will have the format `{site_name: {forceRucio:'yes'|'no', 'ASO_RSE':name}}` allowing for a site to indicate an RSE for ASO different from the site name. While a site not present among the keys means `forceRucio=NO`, having the flag allows us to keep track of which sites we are playing with and easily enable/disable according to the problem of the day
   * the puppet YAML format will be converted into a python dictionary along the lines of https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb?ref_type=heads#L86-90 and added to the TaskWorkerConfig.py file
* The TaskWorker can then take one of two actions:
   a.  silently override the user submitted configuration
   b. raise a submissionRefused exception telling the user to change LFN prefix and possibly StorageSite

@dciangot what is your preference between `a.` and `b.` ? Or is there some other way as well ?
I personally like `b.` more, because it is easier to implement and ensures that users are aware, since they will have to know and worry about Rucio quota, rules management etc. 
 
@nausikt if we decide to implement this, can you help with the puppet side ? I will take care of TaskWorker changes.

## Comment (nausikt, 2026-04-09T15:48:57Z)

@belforte Definitely, Stefano.

## Comment (dciangot, 2026-04-09T15:54:42Z)

@belforte , thanks for the summary! I'm all for `b.` too, I really do not see any good thing coming from users being unaware of that.

## Comment (belforte, 2026-04-09T15:57:30Z)

thanks guys for superfast answers. Diego, can you "by when" you need this ? I think we can put it  in production in O(1 week)

## Comment (dciangot, 2026-04-09T16:03:20Z)

Everything around O(2 weeks) is more than fine. That's the time it would take to set things up in other places (like rucio rse, etc.).

## Comment (belforte, 2026-04-09T16:31:20Z)

OK. top of my list then :-)

## Comment (nausikt, 2026-04-09T17:48:53Z)

Ciao @belforte ! Now, `rucioASOSites` is propagating well through out `qa` env for the TW to pick-ups. (*\*\*In the next hr*)

*P.S. please, let me know whether the format and default values match what you had in mind.*
```python
[crab3@crab-dev-tw05 TaskManager]$ cat cfg/TaskWorkerConfig.py
...
# Note that if site ASO_RSE is not specified will fall back to the site name as default.
config.TaskWorker.rucioASOSites = {
  "T1_IT_CNAF": {"forceRucio": True, "ASO_RSE": "T1_IT_CNAF_Disk_Temp"},
  "T2_IT_Bari": {"forceRucio": True, "ASO_RSE": "T2_IT_Bari_Temp"},
  "T2_IT_Legnaro": {"forceRucio": True, "ASO_RSE": "T2_IT_Legnaro_Test"},
  "T2_IT_Pisa": {"forceRucio": True, "ASO_RSE": "T2_IT_Pisa_Test"},
  "T2_IT_Rome": {"forceRucio": True, "ASO_RSE": "T2_IT_Rome_Temp"},
  "T3_IT_Bologna": {"forceRucio": True, "ASO_RSE": "T3_IT_Bologna_Test"},
  "T3_IT_Firenze": {"forceRucio": False, "ASO_RSE": "T3_IT_Firenze"}, # Firenze seems to have no ASO_RSE somehow?
  "T3_IT_MIB": {"forceRucio": True, "ASO_RSE": "T3_IT_MIB_Test"},
  "T3_IT_Perugia": {"forceRucio": False, "ASO_RSE": "T3_IT_Perugia"}, # As well as Perugia?
  "T3_IT_Trieste": {"forceRucio": True, "ASO_RSE": "T3_IT_Trieste_Temp"}
}
```

## Comment (belforte, 2026-04-09T20:03:11Z)

WOW @nausikt you are way too fast for me ! Great .
FOrmat is perfect..
Let's limit to T2 and start with ASO_RSE same as site name (that's the current setup).
Also kindly set default for `forceRucio` to false, I expect a site-by-site roll-out.

Let's keep this in `qa` while we test on dev/preprd TW, in case we want to make changes so we have freedom to squash commits :-)
will move to `prod` later.

Thanks !!!

## Comment (nausikt, 2026-04-09T20:17:36Z)

Roger that! 🫡

## Comment (nausikt, 2026-04-09T20:35:52Z)

Now, its looks something like.
```python
# Note that if site ASO_RSE is not specified will fall back to the site name as default.
config.TaskWorker.rucioASOSites = {
  "T2_IT_Bari": {"forceRucio": True, "ASO_RSE": "T2_IT_Bari"},
  "T2_IT_Legnaro": {"forceRucio": True, "ASO_RSE": "T2_IT_Legnaro"},
  "T2_IT_Pisa": {"forceRucio": True, "ASO_RSE": "T2_IT_Pisa"},
  "T2_IT_Rome": {"forceRucio": True, "ASO_RSE": "T2_IT_Rome"}
}
```

Just set as following then we good for testing site-by-site.
```yaml
tw_rucioASOSites:
  T2_IT_Bari:
    forceRucio: true
   ...
```

## Comment (belforte, 2026-04-12T16:09:53Z)

with that commit:
```console

belforte@lxplus802/TC3> crab submit 
Will use CRAB configuration file crabConfig.py
Importing CMSSW configuration dummyanalyzer.py
Finished importing CMSSW configuration dummyanalyzer.py
Sending the request to the server at cmsweb-test2.cern.ch
Success: Your task has been delivered to the dev CRAB3 server.
Task name: 260412_160732:belforte_crab_20260412_180730
Project dir: ./crab_20260412_180730
Please use ' crab status -d ./crab_20260412_180730 ' to check how the submission process proceeds.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20260412_180730/crab.log
# [... wait O(1min)...]
belforte@lxplus802/TC3> crab status 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20260412_180730
Task name:			260412_160732:belforte_crab_20260412_180730
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITREFUSED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/260412_160732%3Abelforte_crab_20260412_180730
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=260412_160732%3Abelforte_crab_20260412_180730&from=1776006452000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_CH_CERN_P5', 'T2_UK_SGrid_Bristol', 'T2_CH_CERN_HLT']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			You are using T2_IT_Rome as output destination
				but that site only accepts output to be sent via Rucio
				You must change your crab configuration python file to make sure that
				config.Data.outLFNDirBase starts with /store/user/rucio/ or /store/group/rucio
				And change destination name to:
				config.Site.storageSite = 'T2_IT_Rome_User'
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20260412_180730/crab.log
belforte@lxplus802/TC3> 


```
@dciangot OK with you ?

## Comment (belforte, 2026-04-12T16:13:28Z)

the change is in PR #9297
