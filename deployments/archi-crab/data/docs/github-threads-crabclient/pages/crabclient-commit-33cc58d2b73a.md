# Use python3 and rucio client with cmssw 10 (#5238)

Commit 33cc58d2b73a40fc97bde58271ac8163663f7f3c
Author: Stefano Belforte
Date: 2023-10-20 16:35:28 +0200

* use Python3 for CMSSW_10, add our LumiList, fix LumiList import, remove
pycurl from crab.py

* fix PSetCores check in CMSSWConfig.py

* remove unused, obsolete code from report.py

* add comments

 bin/crab                                      |   2 +-
 bin/crab.py                                   |  13 -
 src/python/CRABClient/Commands/report.py      |  38 +-
 src/python/CRABClient/JobType/Analysis.py     |   6 +-
 src/python/CRABClient/JobType/BasicJobType.py |   6 +-
 src/python/CRABClient/JobType/CMSSWConfig.py  |   4 +-
 src/python/CRABClient/JobType/CopyCat.py      |   6 +-
 src/python/CRABClient/JobType/LumiMask.py     |   6 +-
 src/python/CRABClient/LumiList.py             | 705 ++++++++++++++++++++++++++
 src/python/CRABClient/UserUtilities.py        |   6 +-
 10 files changed, 738 insertions(+), 54 deletions(-)
