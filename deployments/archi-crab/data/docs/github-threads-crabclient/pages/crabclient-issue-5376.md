# dmwm/CRABClient issue #5376: scriptExe is not available via crab server UI any more

State: closed
Opened: 2025-03-03T17:36:21Z
Closed: 2025-03-04T14:42:22Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5376

## Opening post (belforte, 2025-03-03T17:36:21Z)

The UI looks in `WEB_DIR/debug` folder, but the script is not in there anymore.
Best solution is to change line 234 in
https://github.com/dmwm/CRABClient/blob/bf347bd46487754cc4388af7a8c77a835496df44/src/python/CRABClient/JobType/UserTarball.py#L219-L236

adding `/debug/` in front of the file name like done for PSet in lines above
