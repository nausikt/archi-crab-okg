# stop distributing old DBS Client with CRAB. Fix #8566

Commit 0ea99cbf9ed4c6ca01b51f5e3a77f5d68dffbe11
Author: Stefano Belforte
Date: 2023-06-26 14:56:19 +0200



 crab-build.file          | 15 ---------------
 crab-dev.spec            |  3 +--
 crab-pre.spec            |  3 +--
 crab-prod.spec           |  3 +--
 crab/crab-setup.csh.file |  1 -
 crab/crab-setup.sh.file  |  1 -
 6 files changed, 3 insertions(+), 23 deletions(-)
