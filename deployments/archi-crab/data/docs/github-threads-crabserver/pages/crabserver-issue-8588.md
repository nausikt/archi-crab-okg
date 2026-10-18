# dmwm/CRABServer issue #8588: add Client_Validation_Suite and Client_Configuration_Validation to cicd pipeline

State: closed
Opened: 2024-08-06T14:53:00Z
Closed: 2024-11-19T10:04:16Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8588

## Opening post (belforte, 2024-08-06T14:53:00Z)

maybe not run them all of the times. Definitely we do not need to validate client every time that we build TaskWorker.
But in view of getting rid of Jenkins, we need a way to do that.
CCV is important for REST and TW code validation.

## Comment (aspiringmind-code, 2024-11-19T10:04:16Z)

Done in https://github.com/dmwm/CRABServer/pull/8696 and https://github.com/dmwm/CRABServer/pull/8800
