# deprecate numcores option (#5373)

Commit bf347bd46487754cc4388af7a8c77a835496df44
Author: Vijay Chakravarty
Date: 2025-02-17 15:09:26 +0100

* deprecate numcores option

* numcores only to be removed from resubmit, not completely

 etc/crab-bash-completion.sh                |  2 +-
 src/python/CRABClient/Commands/resubmit.py | 22 +++++-----------------
 2 files changed, 6 insertions(+), 18 deletions(-)
