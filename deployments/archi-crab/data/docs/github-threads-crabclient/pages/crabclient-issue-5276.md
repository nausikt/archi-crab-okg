# dmwm/CRABClient issue #5276: preparelocal fails when `scriptArgs` is present

State: closed
Opened: 2023-12-15T14:56:03Z
Closed: 2024-01-30T17:23:39Z
Labels: bug, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5276

## Opening post (belforte, 2023-12-15T14:56:03Z)

ref: https://cms-talk.web.cern.ch/t/issue-with-gfal-in-crab-jobs/32718/3

## Comment (belforte, 2024-01-25T14:26:13Z)

the problem is that after `preparelocal` the script `sh run_job.sh 1` ends up executing inside CMSRunaAnalysis.sh

python3 CMSRunAnalysis.py -r /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/ste/crab_20240125_151836/local -a sandbox.tar.gz --sourceURL=https://cmsweb-test2.cern.ch/S3/crabcache_dev --jobNumber=1 --cmsswVersion=CMSSW_13_3_0 --scramArch=el8_amd64_gcc12 --inputFile=job_input_file_list_1.txt --runAndLumis=job_lumis_1.json --lheInputFiles=False --firstEvent=None --firstLumi=None --lastEvent=None --firstRun=None --seeding=AutomaticSeeding --scriptExe=SIMPLE-SCRIPT.sh --eventsPerLumi=None --maxRuntime=-1 '--scriptArgs=[\"\"exitCode=666\"\",' '\"\"gotArgs=Yes\"\"]' -o '{}'

in particular this is bad
```
--scriptArgs=[\"\"exitCode=666\"\",' '\"\"gotArgs=Yes\"\"]
```
as it leads to

ERROR: Exceptional exit at Thu Jan 25 14:20:38 2024 UTC 10040: Expecting value: line 1 column 2 (char 1)
ERROR: Traceback follows:
 Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 743, in <module>
    + f" {' '.join(json.loads(options.scriptArgs))}")
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 2 (char 1)

i.e. CMSRunAnalysis.py tries to read the above `--scriptArgs=[\"\"exitCode=666\"\",' '\"\"gotArgs=Yes\"\"]` as JSON

## Comment (belforte, 2024-01-25T14:33:55Z)

the original line in `crabConfig.py` was 
```
config.JobType.scriptArgs = ['exitCode=666', 'gotArgs=Yes']
```
and works finely in the real job where data are passed around via the REST DB and in there
`tm_scriptargs`  is the string  `['exitCode=666', 'gotArgs=Yes']`
![image](https://github.com/dmwm/CRABClient/assets/1837785/5e6be05b-6ff9-4a36-bb82-7a113f0c6b80)

I think that the problem is that `preparelocal` writes this file

belforte@lxplus805/local> cat InputArgs.txt 
-a sandbox.tar.gz --sourceURL=https://cmsweb-test2.cern.ch/S3/crabcache_dev --jobNumber=1 --cmsswVersion=CMSSW_13_3_0 --scramArch=el8_amd64_gcc12 --inputFile=job_input_file_list_1.txt --runAndLumis=job_lumis_1.json --lheInputFiles=False --firstEvent=None --firstLumi=None --lastEvent=None --firstRun=None --seeding=AutomaticSeeding --scriptExe=SIMPLE-SCRIPT.sh --eventsPerLumi=None --maxRuntime=-1 --scriptArgs=[\"\"exitCode=666\"\", \"\"gotArgs=Yes\"\"] -o {}
belforte@lxplus805/local> 

While we need to pass those around in JSON format

In the job log we have


Arguments are -a sandbox.tar.gz --sourceURL=https://cmsweb-test2.cern.ch/S3/crabcache_dev --jobNumber=1 --cmsswVersion=CMSSW_13_3_0 --scramArch=el8_amd64_gcc12 --inputFile=job_input_file_list_1.txt --runAndLumis=job_lumis_1.json --lheInputFiles=False --firstEvent=None --firstLumi=None --lastEvent=None --firstRun=None --seeding=AutomaticSeeding --scriptExe=SIMPLE-SCRIPT.sh --eventsPerLumi=None --maxRuntime=-60 --scriptArgs=["exitCode=666", "gotArgs=Yes"] -o {}

i.e.
```txt
--scriptArgs=["exitCode=666", "gotArgs=Yes"]
```

## Comment (belforte, 2024-01-25T15:12:42Z)

hmmm... the "bad" format is already in the `input_args.json` file which is fetched (via InputFiles.tar.gz) from the scheduler's WEB_DIR, and is placed there by DagmanCreator which [contains](https://github.com/dmwm/CRABServer/blob/fac9dfed305043a0d1ee6cfc54cbc5072dbf6750/src/python/TaskWorker/Actions/DagmanCreator.py#L680-L726)
```python

    def prepareLocal(self, dagSpecs, info, kw, inputFiles, subdags):
        """ Prepare a file named "input_args.json" with all the input parameters of each jobs. It is a list
            with a dictionary for each job. The dictionary key/value pairs are the arguments of gWMS-CMSRunAnalysis.sh
            N.B.: in the JDL: "Executable = gWMS-CMSRunAnalysis.sh" and "Arguments =  $(CRAB_Archive) --sourceURL=$(CRAB_ISB) ..."
            where each argument of each job is set in "input_args.json".
            Also, this prepareLocal method prepare a single "InputFiles.tar.gz" file with all the inputs files moved
            from the TW to the schedd.
            This is used by the client preparelocal command.
        """

        argdicts = []
        for dagspec in dagSpecs:
            argDict = {}
            argDict['inputFiles'] = 'job_input_file_list_%s.txt' % dagspec['count'] #'job_input_file_list_1.txt'
            argDict['runAndLumiMask'] = 'job_lumis_%s.json' % dagspec['count']
            argDict['CRAB_Id'] = dagspec['count'] #'1'
            argDict['lheInputFiles'] = dagspec['lheInputFiles'] #False
            argDict['firstEvent'] = dagspec['firstEvent'] #'None'
            argDict['lastEvent'] = dagspec['lastEvent'] #'None'
            argDict['firstLumi'] = dagspec['firstLumi'] #'None'
            argDict['firstRun'] = dagspec['firstRun'] #'None'
            argDict['CRAB_Archive'] = info['cachefilename_flatten'] #'sandbox.tar.gz'
            argDict['CRAB_ISB'] = info['cacheurl_flatten'] #u'https://cmsweb.cern.ch/crabcache'
            argDict['CRAB_JobSW'] = info['jobsw_flatten'] #u'CMSSW_9_2_5'
            argDict['CRAB_JobArch'] = info['jobarch_flatten'] #u'slc6_amd64_gcc530'
            argDict['seeding'] = 'AutomaticSeeding'
            argDict['scriptExe'] = kw['task','tm_scriptexe'] #
            argDict['eventsPerLumi'] = kw['task','tm_events_per_lumi'] #
            argDict['maxRuntime'] = kw['task','max_runtime'] #-1
            argDict['scriptArgs'] = json.dumps(kw['task','tm_scriptargs']).replace('"', r'\"\"') #'[]'
            argDict['CRAB_AdditionalOutputFiles'] = info['addoutputfiles_flatten']
            #The following two are for fixing up job.submit files
            argDict['CRAB_localOutputFiles'] = dagspec['localOutputFiles']
            argDict['CRAB_Destination'] = dagspec['destination']
            argdicts.append(argDict)

        with open('input_args.json', 'w', encoding='utf-8') as fd:
            json.dump(argdicts, fd)

```

## Comment (belforte, 2024-01-25T15:13:28Z)

I have to wonder if this line is correct !
```
            argDict['scriptArgs'] = json.dumps(kw['task','tm_scriptargs']).replace('"', r'\"\"') #'[]'
```

looking in detail the same is used in preparing the DagMan spec, but it is quite possible that HTCondor args parsing has different rules from bash/python

In RunJobs.dag in the SPOOL_DIR I find

VARS Job1 count="1" runAndLumiMask="job_lumis_1.json" lheInputFiles="False" firstEvent="None" firstLumi="None" lastEvent="None" firstRun="None" maxRuntime="-60" eventsPerLumi="None" seeding="AutomaticSeeding" inputFiles="job_input_file_list_1.txt" scriptExe="SIMPLE-SCRIPT.sh" scriptArgs="[\"\"exitCode=666\"\", \"\"gotArgs=Yes\"\"]" +CRAB_localOutputFiles="\"output.root=output_1.root\"" +CRAB_DataBlock="\"/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM#3517e1b6-76e3-11e7-a0c8-02163e00d7b3\"" +CRAB_Destination="\"davs://eoscms.cern.ch:443/eos/cms/store/user/belforte/GenericTTbar/crab_20240125_151836/240125_141842/0000/log/cmsRun_1.log.tar.gz, davs://eoscms.cern.ch:443/eos/cms/store/user/belforte/GenericTTbar/crab_20240125_151836/240125_141842/0000/output_1.root\""
ABORT-DAG-ON Job1 3

Note: ` scriptArgs="[""exitCode=666"", ""gotArgs=Yes""]" `

## Comment (belforte, 2024-01-25T15:44:41Z)

I tried to chage in InputArgs.txt from (see https://github.com/dmwm/CRABClient/issues/5276#issuecomment-1910334013)
```
 --scriptArgs=[""exitCode=666"", ""gotArgs=Yes""]
```
to
```
 --scriptArgs=["exitCode=666", "gotArgs=Yes"]
```
but that is somehow mishandled in passing from CLI to bash to python since CMSRunAnalysis.py receives
```
 '--scriptArgs=["exitCode=666",' '"gotArgs=Yes"]'
```
and likely because of the embedded `' '` fails in json.loads

but removing the blank appears to do it !

bottom line seems that error needs to be fixed in DagmanCreator

## Comment (belforte, 2024-01-25T15:49:23Z)

is maybe better to replace InputArgs.txt with a JSON file ?

also there are two conversion to JSON now, which is fishy
https://github.com/dmwm/CRABServer/blob/fac9dfed305043a0d1ee6cfc54cbc5072dbf6750/src/python/TaskWorker/Actions/DagmanCreator.py#L710
https://github.com/dmwm/CRABServer/blob/fac9dfed305043a0d1ee6cfc54cbc5072dbf6750/src/python/TaskWorker/Actions/DagmanCreator.py#L718

## Comment (belforte, 2024-01-26T15:58:07Z)

I tried to avoid the double conversion and then other "hacks", but found no goo way to pass something like 
```
--scriptArgs="['exitCode=666', 'gotArgs=Yes']" 
```
to CMSRunAnalysis.sh and then to CMSRunAnalysis.py w/o bash introducing escapes (`\`) which eventually confuse things.

I now think that best way is to avoid the `InputArgs.txt` file, put the JSON file (currently `input_args.json`) prepared by DagmanCreator in the `local` dir and have `run_job.sh` pass it as argument. Which means introduce a new argument "--argFile" for CMSRunAnalysis.py and when that is present parse the JSON inside python.
