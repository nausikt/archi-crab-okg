# dmwm/CRABServer pull request #8706: Fix retag monit image in release pipeline

State: closed
Opened: 2024-09-20T12:01:32Z
Closed: 2024-09-20T12:01:45Z
Merged: 2024-09-20T12:01:45Z
URL: https://github.com/dmwm/CRABServer/pull/8706

## Opening post (novicecpp, 2024-09-20T12:01:32Z)

Context: https://github.com/dmwm/CRABServer/issues/8701
Test Pipeline: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8174105

Also refactor retag stage a bit, move command into single job (only take 6 seconds).

## Comment (belforte, 2024-09-20T12:34:41Z)

@aspiringmind-code I do not understand the code here, and am trying to avoid learning what `crane` is/does. Please make sure that you understand, so you can ask Wa in case.

## Comment (novicecpp, 2024-09-20T12:50:08Z)

We build image with temporary tag, then retag it to release the production image. We use `crane` to do that instead `docker` command.

crane explanation is in https://cmscrab.docs.cern.ch/crab-infrastructure/crab-cicd/gitlab/crab-specific-setup.html#crane
