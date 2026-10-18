# dmwm/CRABServer issue #8755: make possible to run validation tests in parallel

State: open
Opened: 2024-10-31T14:43:09Z
Labels: Type: Enhancement, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8755

## Opening post (belforte, 2024-10-31T14:43:09Z)

in the new CI pipeline based on GitLab runner, we have hit the situation where two scripts run at same time creating races in accessing ~/.crab3 cache file.

Should modify test script so that every crab command explicitly uses `-d <directory>` option.
And also point CRAB3_CRAB_CACHE to /dev/null to avoid possible access conflicts, see https://github.com/dmwm/CRABClient/issues/5337

- [ ] add a `remakeTask{}` to https://github.com/dmwm/CRABServer/blob/v3.241018/test/testUtils.py  (basically the first lines of current `checkStatus{}` : do a crab remake and returns directory name
- [ ] call it in https://github.com/dmwm/CRABServer/blob/v3.241018/test/makeTests.py so to explicitly pass `-d ...` to each command.
- [ ] remove the now duplicated code from  `checkStatus{}` 

That will allow running CCV in parallel with other tests.
CV is not straightforward, since having `-d` option or not should ideally part of the test itself.

It looks to me that ST test is safe on this regard. But should be reviewed.

## Comment (belforte, 2026-07-13T14:41:42Z)

this may have been solved by now. Should check and if not, make a plan of what to do
