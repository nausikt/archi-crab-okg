# dmwm/CRABServer issue #8583: [CI] Automatically put a new CRABClient's release to CVMFS

State: open
Opened: 2024-08-02T16:30:42Z
Labels: Status: Available, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8583

## Opening post (novicecpp, 2024-08-02T16:30:42Z)

Part of https://github.com/dmwm/CRABServer/issues/7958 (fifth checkbox)

Why? It take A LOT OF CONCENTRATION to create proper PR (to put correct version name in spec file open PR).

To release new client version, we need to open PR to `cms-sw/cmsdist` default branch.
There are two use cases:
1. update crab-dev to new tag, https://github.com/cms-sw/cmsdist/pull/8856
2. bump crab-prod to  crab-dev tag (and crab-pre to what crab-prod was at same time).  https://github.com/cms-sw/cmsdist/pull/8856

We can leverage GH API to open PR for us, like we do with old Testsuite where we create new issue and post status of testsuite.

Triggering, maybe make it automated for `crab-dev` every time when the new version release, and manually for `crab-prod`.

## Comment (novicecpp, 2024-09-02T09:40:42Z)

I unassigned this issue from myself.

I think it is still worth to do because beside the usefulness, it will become the boilerplate for GH bot in general to open PR/issue, comment, tagging another bot etc.
Imagine you can:
- Open PR to another repo and ask their bot to test.
- ask bot to trigger pippeline from PR/issue.
- link pipeline to PR/issue, make bot ping when pipeline complete.
- and many more.

We need to copy some cmssw people's brilliant ideas how they utilize the gh bot.

## Comment (belforte, 2024-09-02T12:18:56Z)

OK. Adding to my list. In time I'll hand to one of the new DevOps once they have learnt how to deploy CRABClient and got similarly fed up with the tedious and error-prone process !
