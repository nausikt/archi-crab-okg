# dmwm/CRABServer issue #8948: migrate gitlab runner to new registration workflow

State: closed
Opened: 2025-02-26T20:04:10Z
Closed: 2025-02-27T18:22:57Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8948

## Opening post (belforte, 2025-02-26T20:04:10Z)

https://cern.service-now.com/service-portal?id=outage&n=OTG0153023

## Comment (nausikt, 2025-02-27T18:22:58Z)

Done.

I've followed [new registration workflow](https://gitlab.docs.cern.ch/docs/Build%20your%20application/CI-CD/Runners/private-runner-registration/).
to get new Runner authentication tokens for both `crab3` and `crab3-shell`. The new Tokens will have the prefix, `glrt-`.
(P.S. which seems like Wa already updated it once since 2024-04. but i renewed it again anyway.)

I did it by edited `id` and `token` in our currently working gitlab-runner configs and updating it to the corresponding tbag secret keys then manually restarting gitlab runner systemd services for each `crab3`, `crab3-shell` at `crab-ci-runner01` as following.

NOTES: prefix `gitlab-runner-local*` is for shell executor (*crab3-shell*) and prefix `gitlab-runner` is for docker runner (*crab3*)
```
tbag set --hg vocmsglidein/cirunner gitlab-runner-local.config.toml --file config.shell.updated.toml
tbag set --hg vocmsglidein/cirunner gitlab-runner.config.toml --file config.updated.toml
```
```
systemctl restart gitlab-runner-local.service
systemctl restart gitlab-runner.service
```
(P.S. Since, `puppet agent -tv` not triggered systemd restart as i expected, may be because there is no changes in manifests and configs; only tbags)

Now our gitlab pipelines use only new runners. As you can see throughout the jobs in one of my pipeline here: [CI/CD pipelines were using 2 new runners](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10909499)

Thanks to our comprehensive [CRAB's Folks doc](https://cmscrab.docs.cern.ch/crab-infrastructure/crab-cicd/gitlab/private-runners.html), it's helps me a lot!

## Comment (belforte, 2025-02-27T22:47:06Z)

WOW. Amazingly fast. Do you think that it is worth to put a one-line note about this in the documentation pointing to this issue ?

## Comment (nausikt, 2025-02-27T23:11:06Z)

@belforte Yes, i also think of elaborate a little bit more about systemd related stuffs, which crucial for managing both daemons (`crab3` and `crab3-shell`) in the same vm but were implicitly mentioned in puppet manifests, and also a little bit details about gitlab-runner config file which hopefully might be helpful for other issue that try to utilize parallelism among runners for validation tests or when we wish for creating a new *crab-ci-runner02,03,04...*
