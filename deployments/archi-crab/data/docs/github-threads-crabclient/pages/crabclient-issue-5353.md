# dmwm/CRABClient issue #5353: avoid syntax warnings with python 3.12

State: closed
Opened: 2024-11-26T17:20:42Z
Closed: 2024-11-28T10:47:38Z
Labels: enhancement, Done
URL: https://github.com/dmwm/CRABClient/issues/5353

## Opening post (belforte, 2024-11-26T17:20:42Z)

python is getting pickier about syntax:

```console
belforte@lxplus824/py3.12> crab-dev submit my.py
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/ClientUtilities.py:611: SyntaxWarning: invalid escape sequence '\d'
  if re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', jobids):
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/Commands/recover.py:704: SyntaxWarning: invalid escape sequence '\d'
  regex = "^\d{6}_\d{6}_?([^\:]*)\:[a-zA-Z0-9-]+_(crab_)?.+"
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/Commands/remake.py:77: SyntaxWarning: invalid escape sequence '\d'
  regex = "^\d{6}_\d{6}_?([^\:]*)\:[a-zA-Z0-9-]+_(crab_)?.+"  # pylint: disable=anomalous-backslash-in-string
Will use CRAB configuration file my.py
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/JobType/Analysis.py:232: SyntaxWarning: invalid escape sequence '\d'
  run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/JobType/CopyCat.py:119: SyntaxWarning: invalid escape sequence '\d'
  run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02865/share/cms/crab-dev/v3.241125.00/lib/CRABClient/JobType/Recover.py:225: SyntaxWarning: invalid escape sequence '\d'
  run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)
Importing CMSSW configuration minimalPS.py
```

## Comment (belforte, 2024-11-27T20:34:37Z)

intial list of places to edit
```console
LapSB:CRABClient$ rg "regex ="
src/python/CRABClient/JobType/Analysis.py
263:            uuid_regex = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

src/python/CRABClient/Commands/remake.py
77:        regex = "^\d{6}_\d{6}_?([^\:]*)\:[a-zA-Z0-9-]+_(crab_)?.+"  # pylint: disable=anomalous-backslash-in-string

src/python/CRABClient/Commands/recover.py
704:            regex = "^\d{6}_\d{6}_?([^\:]*)\:[a-zA-Z0-9-]+_(crab_)?.+"
LapSB:CRABClient$ rg "re\.compile"
src/python/CRABClient/LumiList.py
229:        doubleBracketRE = re.compile (r']],')

src/python/CRABClient/JobType/Analysis.py
170:                    reason_re = re.compile(r'\AFile size is ([0-9]*)B\. This is bigger than the maximum allowed size of ([0-9]*)B\.$')
263:            uuid_regex = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

src/python/CRABClient/Commands/resubmit.py
332:        sn_rec = re.compile(sn_re) #sn_rec => SiteName_RegularExpressionCompiled
LapSB:CRABClient$ rg "re\.search"
bin/crab.py
167:            errorDetail = re.search(r'(?<=X-Error-Detail:\s)[^\n]*', err).group(0)
170:            reason = re.search(r'(?<=X-Error-Info:\s)[^\n]*', err).group(0)
177:            errorId = re.search(r'(?<=X-Error-Id:\s)[^\n]*', err).group(0)

src/python/CRABClient/RestInterfaces.py
71:        response = re.search(startRegex, row)
73:            if re.search(continueRegex, row):
LapSB:CRABClient$ rg "re\.sub"
src/python/CRABClient/RestInterfaces.py
75:            res = re.sub(replaceRegex, "", response.group(0)).strip()

src/python/CRABClient/JobType/Analysis.py
121:            outputFiles = [re.sub(r'^file:', '', f) for f in getattr(self.config.JobType, 'outputFiles', [])]
127:        addoutputFiles = [re.sub(r'^file:', '', f) for f in getattr(self.config.JobType, 'outputFiles', []) if re.sub(r'^file:', '', f) not in edmfiles+tfiles]
163:            inputFiles = [re.sub(r'^file:', '', f) for f in getattr(self.config.JobType, 'inputFiles', [])]

src/python/CRABClient/JobType/CMSSWConfig.py
220:                edmfile = re.sub(r'^file:', '', o.fileName.value())
240:                tfile = re.sub(r'^file:', '', getattr(tFileService, 'fileName').value())
LapSB:CRABClient$ rg "re\.match"
src/python/CRABClient/JobType/Analysis.py
171:                    re_match = reason_re.match(reason)
232:                run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)

src/python/CRABClient/JobType/CopyCat.py
119:            run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)

src/python/CRABClient/JobType/Recover.py
225:            run_ranges_is_valid = re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', run_ranges)

src/python/CRABClient/Commands/getcommand.py
228:        if re.match("^[a-z]+://", self.dest):
282:            if re.match("^[a-z]+://", self.options.outputpath):
304:            if re.match('^yes$|^no$', self.options.checksum):

src/python/CRABClient/Commands/remote_copy.py
119:            url_input = bool(re.match("^[a-z]+://", dirpath))
282:                url_input = bool(re.match("^[a-z]+://", dirpath))

src/python/CRABClient/Commands/recover.py
705:            if not re.match(regex, self.options.cmptask):

src/python/CRABClient/Commands/SubCommand.py
457:            if re.match(item, __version__):

src/python/CRABClient/Commands/checkwrite.py
367:            if re.match('^yes$|^no$', self.options.checksum):

src/python/CRABClient/ClientUtilities.py
611:    if re.match('^\d+((?!(-\d+-))(\,|\-)\d+)*$', jobids):

src/python/CRABClient/Commands/remake.py
78:        if not re.match(regex, self.options.cmptask):
LapSB:CRABClient$ 

```

## Comment (belforte, 2024-11-27T20:46:21Z)

even if the "absolutely needed" are less
```console
LapSB:CRABClient$ find . -name '*py' -exec python3 {} \; 2>&1 |grep SyntaxWarning
/home/belforte/STEFANO/WORK/CRAB/CRABClient/./src/python/CRABClient/ClientUtilities.py:611: SyntaxWarning: invalid escape sequence '\d'
/home/belforte/STEFANO/WORK/CRAB/CRABClient/./src/python/CRABClient/JobType/Recover.py:225: SyntaxWarning: invalid escape sequence '\d'
/home/belforte/STEFANO/WORK/CRAB/CRABClient/./src/python/CRABClient/JobType/CopyCat.py:119: SyntaxWarning: invalid escape sequence '\d'
/home/belforte/STEFANO/WORK/CRAB/CRABClient/./src/python/CRABClient/JobType/Analysis.py:232: SyntaxWarning: invalid escape sequence '\d'
LapSB:CRABClient$ 


```
