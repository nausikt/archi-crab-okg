# dmwm/CRABServer issue #8952: enable FTS reuse in the code

State: closed
Opened: 2025-02-27T09:06:30Z
Closed: 2025-04-08T09:57:28Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8952

## Opening post (belforte, 2025-02-27T09:06:30Z)

get rid of the switch via the file `/etc/use_fts_reuse` . See #8578 for details about why that file is there. This should be always on.
clean up code and remove useless files once new code is deployed
