# dmwm/CRABServer issue #8614: remove getWebdirForDb from ServerUtilities and PreJob

State: open
Opened: 2024-08-12T19:59:40Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8614

## Opening post (belforte, 2024-08-12T19:59:40Z)

the webdir URL is obtained from the REST inside AdjustSites and placed in the `webdir` file in the SPOOL_DIR. There is no need for that code anyrmore
