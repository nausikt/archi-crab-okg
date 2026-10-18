# dmwm/CRABServer pull request #8621: add SUBMITREFUSED to task statuses to monitor. Fix #8620

State: closed
Opened: 2024-08-14T15:39:36Z
Closed: 2024-08-15T08:58:15Z
Merged: 2024-08-15T08:58:15Z
URL: https://github.com/dmwm/CRABServer/pull/8621

## Opening post (belforte, 2024-08-14T15:39:36Z)

I verified that this change adds the info to the json doc and does not break the code.
I think we need to merge and deploy on crab-prod-tw02 to see if data appears in OpenSeach and add a query to grafana panel
I guess I can kick off a gitlab pipeline to test this from my local repo ? What do you think @mapellidario ?
But there's no way to deploy it on prod2, via gitlab, right ?

## Comment (cmsdmwmbot, 2024-08-14T15:43:28Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 17 comments to review
 * Pycodestyle check: succeeded
   * 32 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2108/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-14T15:59:51Z)

OK. I am using pipeline to build w/o deploy. Then can give it a try on prod2. Nothing bad will happen, at worst some odd value in our grafana.

## Comment (mapellidario, 2024-08-14T16:34:39Z)

So, i have added some information to [1].

I suggest that 

- [x] you build the new container, 
- [x] ~~then i change the version of the monit container running in crab-dev-tw02 [2]~~ tag your image with `v3.latest.monit`, ssh into crab-dev-tw02, docker pull `v3.latest.monit`, let the existing cronjobs do the rest
- [x] we let it run for a while (one hour or so is good enough for me)
- [x] and we check the result from the grafana dashboard that reads from the test opensearch index (which is called `monit_crab_test` inside grafana) [3]
    - Apparently we saw some submit refused [4], from dashboard [3]. i consider this PR validated

the link at [3] default at the crab-dev-tw01, where i think that you Stefano run your tests. we can change the monit source to crab-dev-tw02 to check how it goes over night

PS: i updated [5] with an outline of what you and i did to develop and validate the changes. (i did not add many details yet, i would prefer to change runContainer.sh with the `-i` option before)

---

[1] https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-crontabs.html
[2] https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/847146c82b69e4af6fef67ffd8694a917c17acb6/data/fqdns/crab-dev-tw02.cern.ch.yaml#L19
[3] https://monit-grafana.cern.ch/goto/hUZgBFjIR?orgId=11 

[4]

![image](https://github.com/user-attachments/assets/3a579e3d-2cc4-4b2f-84b8-ef80eeee92a4)

[5] https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-crontabs.html#how-to-change-build-and-push

## Comment (belforte, 2024-08-14T16:46:34Z)

I would deploy straight on prod02 and see how it goes.
Anyhow image is there now
registry.cern.ch/cmscrab/crabtaskworker:pypi-test2-add-submitrefused-4.monit

## Comment (belforte, 2024-08-14T16:47:02Z)

I will not touch crab-prod-tw02 tonight

## Comment (belforte, 2024-08-15T08:58:12Z)

here we go with a Ferragosto-merge
