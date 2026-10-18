# dmwm/CRABServer issue #8689: [CI] Deploy new version on production using gitlab CI

State: open
Opened: 2024-09-04T15:56:26Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8689

## Opening post (novicecpp, 2024-09-04T15:56:26Z)

One of our CI wishlist, second checkbox https://github.com/dmwm/CRABServer/issues/7958

It still use tag-and-push pattern, or trigger through WebUI, which does not have a beautiful interface like Jenkins, but might be more convenient.

The pipeline would have 3 stages: deploy -> runtest -> checktest, to make sure the newly deployed services are running properly.

To deploy on prod, you need 2 variables:
- `DEPLOY_PROD`, value is container tag you want to deploy.
- `DEPLOY_SERVICE`, value is `all` or service name (REST/TaskWorker/Publisher_schedd/Publisher_rucio)

The main blocker (or not?) is to negotiate with Aroosha, to allow us to deploy REST from CI, like we do on testbed, on production backend cluster. I am not sure if she has any security concern about this.

## Comment (belforte, 2025-02-27T08:56:56Z)

@sinonkt this may actually be partially/mostly done and in a way overlaps with canary deployment.
Please review the idea and need and make a proposal about how to best handle Continuous Deployment.
