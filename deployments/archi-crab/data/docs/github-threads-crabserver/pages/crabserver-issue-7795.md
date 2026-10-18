# dmwm/CRABServer issue #7795: remove obsolete tm_rest_host tm_rest_uri

State: closed
Opened: 2023-08-04T08:19:01Z
Closed: 2023-08-04T08:49:05Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7795

## Opening post (belforte, 2023-08-04T08:19:01Z)

no need to have them in filetransfersdb.
rest host and db instance are needed before DB can be accessed !

At this point those are not used anywhere in the code, via https://github.com/dmwm/CRABServer/pull/7507
