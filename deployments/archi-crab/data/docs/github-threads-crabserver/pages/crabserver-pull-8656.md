# dmwm/CRABServer pull request #8656: monitoring image - some new additions

State: closed
Opened: 2024-08-27T15:01:59Z
Closed: 2024-08-27T15:22:34Z
Merged: 2024-08-27T15:22:34Z
URL: https://github.com/dmwm/CRABServer/pull/8656

## Opening post (mapellidario, 2024-08-27T15:01:59Z)

I decided that:

- the docker image that we use for monit should have its own place in the registry: `cmscrab/crabtwmonit`, separate from crabtaskworker.
- every time we build the monit image, for example with `git push gitlab -o ci.variable="BUILD=t" $TAG`, then we also tag the monit image with `v3.latest`, so that crab-dev-tw02 starts using it.
- production will not be affected because it runs a validated docker monit image tag.

## Comment (cmsdmwmbot, 2024-08-27T15:04:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2127/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-27T15:15:07Z)

Can you clarify last bullet ? Am I correct that it is not due to some protection but simply by us being careful about what we deploy ?

## Comment (mapellidario, 2024-08-27T15:22:30Z)

Yeah, last bullet refers to manually changing the monit image version in hiera for crab-prod-tw02, as described in the new section i added to the documentation [1] :) (yeah, sorry, many new small doc sections will appear in these last few days :) )

---

[1] https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-crontabs.html#deploy-new-version-of-monitoring-image

## Comment (belforte, 2024-08-27T15:26:08Z)

Perfect. Thanks
