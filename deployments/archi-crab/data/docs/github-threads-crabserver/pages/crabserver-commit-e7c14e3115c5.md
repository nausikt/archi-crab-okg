# Taperecall: allow to recall any data tier if size less than threshold (#7862)

Commit e7c14e3115c53c5542bb0884d618a45397f5886c
Author: Thanayut Seethongchuen
Date: 2023-09-05 11:18:11 +0200



 src/python/TaskWorker/Actions/DBSDataDiscovery.py  | 73 ++++++++++++++--------
 .../TaskWorker/Actions/test_DBSDataDiscovery.py    | 53 ++++++++++++++++
 2 files changed, 99 insertions(+), 27 deletions(-)
