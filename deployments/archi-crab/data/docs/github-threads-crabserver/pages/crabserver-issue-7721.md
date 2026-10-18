# dmwm/CRABServer issue #7721: remove references to tm_rest_* in filetransfersdb

State: closed
Opened: 2023-07-07T16:13:37Z
Closed: 2023-07-18T17:00:03Z
Labels: Status: Done, Area: Code Cleanup, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7721

## Opening post (belforte, 2023-07-07T16:13:37Z)

we do not use anymore columns `tm_rest_host ` and `tm_rest_uri`
see also last open tasks in
https://github.com/dmwm/CRABServer/issues/7480#issue-1464734769

time to remove refereces in
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/CRABInterface/RESTFileUserTransfers.py#L58-L59
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/CRABInterface/RESTFileUserTransfers.py#L123-L124
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/CRABInterface/RESTFileUserTransfers.py#L130

https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L12
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L16
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L246
https://github.com/dmwm/CRABServer/blob/14116832382f142e3629352d5e0b6cf7a3b3a3d9/src/python/Databases/FileTransfersDB/Oracle/Create.py#L58-L59

## Comment (belforte, 2023-07-07T22:48:18Z)

TOP prio because I am tired of having pending cleanups

## Comment (belforte, 2023-07-18T17:00:03Z)

mistake
