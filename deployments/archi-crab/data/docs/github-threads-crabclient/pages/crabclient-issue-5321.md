# dmwm/CRABClient issue #5321: avoid `nosort` option in crab command completion

State: closed
Opened: 2024-07-04T08:03:30Z
Closed: 2024-07-14T15:49:44Z
Labels: bug, critical
URL: https://github.com/dmwm/CRABClient/issues/5321

## Opening post (belforte, 2024-07-04T08:03:30Z)

see
https://cms-talk.web.cern.ch/t/crab-is-not-working/41539/12?u=belforte

IMHO there is no need for `nosort` and we can also remove all those weights, listing commands in alphabetical order is fine. If we want to group command and/or add a tiny online guide, we can do in `crab --help` not in `crab <TAB>`

## Comment (smuzaffar, 2024-07-04T14:42:09Z)

@belforte , I have added a [CI tests](https://github.com/cms-sw/cms-bot/pull/2281) to make sure one can run `cmsset_default.sh` (which also sources `crab-bash-completion.sh` for crab pre-prod, dev). Enabling this tests for existing crab/cms-common versions [shows](https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-9be778/40221/cmsset_default/) that we need fixes for zsh and el7. 

I have fixed [cms-common](https://github.com/cms-sw/cms-common/commit/2f8b40d4907649b7cca9a7750bf6e57b7b1f195d) to not fail under `zsh`. I also have patched crab specs to drop `-o nosort` (which fails under el6 and el7) . [cmdist PR](https://github.com/cms-sw/cmsdist/pull/9282) contains these changes and new CI tests [passed](https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-d7c5e2/40224/cmsset_default/run.log) for bash, sh and zsh under el6 to el9.

Hopefully in future we can catch such failures during CI tests

## Comment (belforte, 2024-07-05T08:52:41Z)

Thanks a lot @smuzaffar . I am sorry that CRABClient creates problems every now and then. If you think that we could/shoud review the way it is deployed, please let us know.
