# Use python2 for submit whenever cmsrun uses it fix #5279 (#5281)

Commit 64a0834f99144640d9d9ec2321781b6cac64c6b6
Author: Stefano Belforte
Date: 2024-01-10 10:37:35 +0100

* use py2 for crab submit on older CMSSW. Fix #5279. Fix #5239

* CMSSW uses py3 internally from CMSSW_12 onward

 bin/crab | 4 ++++
 1 file changed, 4 insertions(+)
