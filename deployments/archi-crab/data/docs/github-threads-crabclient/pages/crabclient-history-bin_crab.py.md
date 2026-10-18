# dmwm/CRABClient: commit history of bin/crab.py (at 970fabd75d68)

URL: https://github.com/dmwm/CRABClient/commits/master/bin/crab.py

73b01f1 2025-06-24 15:30:50 +0200 Stefano Belforte: better reporting of exceptions. Fix #5299 (#5397)
* better reporting of exceptions. Fix #5299

* pylint

* print traceback to stderr (console)
2b8f423 2024-10-29 20:30:51 +0100 Stefano Belforte: report failing reason to log and console. FIx #5342 (#5343)
* better reporting, log and doc. Fix #5342

* cleanup

* fix except order
33cc58d 2023-10-20 16:35:28 +0200 Stefano Belforte: Use python3 and rucio client with cmssw 10 (#5238)
* use Python3 for CMSSW_10, add our LumiList, fix LumiList import, remove
pycurl from crab.py

* fix PSetCores check in CMSSWConfig.py

* remove unused, obsolete code from report.py

* add comments
da6d38f 2023-10-17 19:46:54 +0200 Stefano Belforte: make sure all commands return a dict. Fix #5224 (#5225)
* make sure all commands return a dict. Fix #5224

* fix two undefined vars

* use new CommandFailedException in crab.py

* add description of return dictionary

* checkusername must also return username, as before
ba525ea 2023-10-12 18:02:39 +0200 Stefano Belforte: Initialise Rucio client after we have proxy. Fix #5220 (#5222)

932b4c3 2023-10-10 23:08:01 +0200 Stefano Belforte: diagnostics

c31428f 2023-10-10 23:03:25 +0200 Stefano Belforte: diagnostic

c5ebc37 2023-10-10 00:58:14 +0200 Stefano Belforte: intial implementation of adding Rucio client. Fix #5213 (#5214)
* intial implementation of adding Rucio client. Fix #5213

* pylint
769a053 2022-02-21 12:43:27 +0100 Stefano Belforte: no need anymore for the warning about CMSSW_12 (#5152)

aa4374f 2022-02-09 17:15:10 +0100 Stefano Belforte: make sure CMSSW_VERSION is defined (#5149)

c5ddf66 2021-12-10 12:36:49 +0100 Stefano Belforte: warn users of crab-dev. Fix #5134 (#5136)
* warn users of crab-dev. Fix #5134

* better message
b610228 2021-12-10 09:28:16 +0100 Stefano Belforte: validate proxy VOMS extension. Fix #5131 (#5132)
* validate proxy VOMS extension. Fix #5131

* add from __future__ import division in various files
0fef759 2021-11-12 14:54:54 +0100 Daina: improve HTTP header parsing (#5111)

64d1326 2021-11-02 16:17:05 +0100 Daina: switch python versions based on CMSSW release (fix #5098) (#5102)

