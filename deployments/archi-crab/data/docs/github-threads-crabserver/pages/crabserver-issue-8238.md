# dmwm/CRABServer issue #8238: Improve Jenkins tests reporting

State: open
Opened: 2024-02-14T18:14:30Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8238

## Opening post (belforte, 2024-02-14T18:14:30Z)

Would be good to be able to classify/mark Jenkins GH issues as suceed/fail, not open/close.
Currently all  we can do is to close both OK and Fail. So we have no simple way to indicate if they succeded when referencing from other issues, e.g.  making a list for validation.

Maybe this need will go away when all tests will be run as part of a top level action like a PR or a release build and will simply be a report inside there.

Current situation is also bad because it pollutes our repository with a plethora of issues.
