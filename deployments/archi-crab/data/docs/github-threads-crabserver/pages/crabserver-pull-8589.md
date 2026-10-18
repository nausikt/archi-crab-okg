# dmwm/CRABServer pull request #8589: Refactor process controller scripts 

State: closed
Opened: 2024-08-06T17:29:07Z
Closed: 2024-08-27T09:55:20Z
URL: https://github.com/dmwm/CRABServer/pull/8589

## Opening post (novicecpp, 2024-08-06T17:29:07Z)

Try to fix https://github.com/dmwm/CRABServer/issues/8436 ~~with over complicate solution.~~

The idea is to use `argparse` to help to parse arguments. Bash is too hard to manage.

Here is how process are called:

ENTRYPOINT (run.sh) -> manage.py (shared in 3 services) -> manage.sh -> [crab-taskworker/crab-publisher/wmc-httpd].

- Ideally, manage.sh should change into python module. But too much work for now.
- pass argument to manage.sh via env vars (we can get rid this line if we change it into python module).
- start.sh/stop.sh/env.sh also shared, just interface to manage.py.

`env.sh` is a bit special. I print (echo) the env vars that would like to use inside `manage.sh` then I wrap it in env.sh with `eval` command. So, to source env vars you can simply run `source ./env.sh`.


@belforte @mapellidario what do you think?

## Comment (cmsdmwmbot, 2024-08-06T17:31:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2093/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-06T22:05:15Z)

it will be useful to walk through this code together. I have 3 points:
1. I like the overall flow and the idea to use python to parse args
2. I fail to understand some things in the new code, but would like to
3. It is good that `env.sh` is now part of `manage` but the "wrappers aside" all work is done in `manage.sh` and that is still different for TW and Publisher "more that it absolutely needs to".  I guess we can improve later. It is getting incrementally better with time !
