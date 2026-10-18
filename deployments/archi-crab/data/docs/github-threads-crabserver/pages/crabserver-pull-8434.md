# dmwm/CRABServer pull request #8434: add env.sh scripts, monit scripts compatible with pypi containers

State: closed
Opened: 2024-05-28T13:19:49Z
Closed: 2024-05-29T07:44:22Z
Merged: 2024-05-29T07:44:22Z
URL: https://github.com/dmwm/CRABServer/pull/8434

## Opening post (mapellidario, 2024-05-28T13:19:49Z)

This PR 

### status

tested

latest images from this PR built by: https://gitlab.cern.ch/crab3/CRABServer/-/commit/7b433f3566eeda5096a7d462b0a61eb84a5324c4/pipelines

### details

this PR contains the following changes

- added `env.sh` script for crabserver, TW and publishers
- the code for the env.sh script is extracted from the code inserted in `start.sh`. meaning that these new `env.sh` scripts now require `-c` / `-g` option. we can set a default in the future if we want `env.sh` to work without any argument
- runContainer.sh required a couple of changes in if conditions for monitoring scripts to adapt to `set -o pipefail`

## Comment (cmsdmwmbot, 2024-05-28T13:23:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2001/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-28T14:35:53Z)

LGTM even if I am wondering if we can unifyt the `env.sh` and possibly also the `start.sh` across the applications. Looks like thanks to the new PyPI way things have got simpler.

## Comment (mapellidario, 2024-05-28T16:07:51Z)

> unifyt the env.sh and possibly also the start.sh across the applications

shall i have a look now in this PR, shall i look in another PR, should i leave it to wa who knows better than me which application requires what?

## Comment (belforte, 2024-05-28T17:17:59Z)

Let's give it to Wa/Janna as cake frosting

## Comment (mapellidario, 2024-05-29T07:44:18Z)

seems that we all agree on a way forward. I am merging, thanks for the reviews! :)
