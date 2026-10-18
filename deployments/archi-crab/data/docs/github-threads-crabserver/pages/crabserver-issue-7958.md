# dmwm/CRABServer issue #7958: Add new CI pipelines (wishlist)

State: open
Opened: 2023-10-18T10:42:23Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7958

## Opening post (novicecpp, 2023-10-18T10:42:23Z)

(Thanks a lot @mapellidario and @guyzsarun for the ideas and advice!)

With 2 main goal in mind:

-   Reduce manual work that cost time to do.
-   Prevent human error that cost time to debug.

This will boost our productivity (sorry, I do not know how to measure it) and enable rapid deployment on production.

The new *N* pipelines:

- [x] Automatically deploy master branch on preprod.
      Why? Eliminating the time to deploy the new image and trigger testsuite.
- [ ] Manually trigger deployment of latest tag on production and ensure new tasks can run properly.
      Why? Improvement of current Deploy_TW/Server pipeline; tagging the new release as `-stable`, deploy it on prod, **AND** run testsuite to make sure everything is ok.
      Now in https://github.com/dmwm/CRABServer/issues/8689
- [x] Automatically deploy specific none master branch to dev env and run testsuite.
      Why? This is what I want personally, I need to make sure my code is running perfectly fine before I can open PR to other team member to review.
- [ ] Automatically trigger testsuite when puppet qa/master has new changed
      Why? <https://mattermost.web.cern.ch/cms-o-and-c/pl/8764zq4n6i815brt787b5br4fh>
- [ ] Automatically put the new CRABClient\'s release to crab-dev and open PR to cms-sw/cmsdist
      Why? It take *A LOT OF CONCENTRATION* to create proper PR (to put correct version name in spec file open PR).
      Now in https://github.com/dmwm/CRABServer/issues/8583
- [ ] Automatically apply new credentials on kube/vm from crab-secrets and update credentials for CMSWEB team can apply to new cluster.
      Why? Infra as a code: describe what we should do when we need to change credentials instead of writing some documentation.
      Now in https://github.com/dmwm/CRABServer/issues/8017
- [ ] Automatically test CRABClient against all supported cmssw version.
      Why? Current Jenkins need manual trigger for each cmssw version.

I will write implementation details for each pipeline in separate issue, but I am open for discussion here about priority and worthiness.

My plan is to have the first 3 pipelines before end of the year.

## Comment (belforte, 2023-10-18T16:33:25Z)

isn't this more CD than CI ?
Jokes aside. Do IIUC that this will be  a Jenkins (or GH hooks) pipeline which will also be used to run current Jenkins tests without those large web-UI based templates ?

## Comment (novicecpp, 2023-10-18T16:41:48Z)

> Do IIUC that this will be a Jenkins (or GH hooks) pipeline which will also be used to run current Jenkins tests without those large web-UI based templates ?

Yes. I will provide more detail later.
