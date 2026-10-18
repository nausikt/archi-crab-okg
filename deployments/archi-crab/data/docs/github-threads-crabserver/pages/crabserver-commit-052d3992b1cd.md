# only 3GB max mem for 1core at initial sub. Fix #9206 (#9207)

Commit 052d3992b1cdea072bb0ddba3ff540247aa5eff1
Author: Stefano Belforte
Date: 2025-10-10 09:55:25 +0200

* only 3GB max mem for 1core at initial sub. Fix #9206

* add pointer to policy

* when asking too much in resubmt, allow to try again

 src/python/ServerUtilities.py                    |  3 ++-
 src/python/TaskWorker/Actions/DagmanSubmitter.py | 17 ++++++++++++-----
 2 files changed, 14 insertions(+), 6 deletions(-)
