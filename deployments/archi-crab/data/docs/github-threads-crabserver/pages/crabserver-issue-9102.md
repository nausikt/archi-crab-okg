# dmwm/CRABServer issue #9102: update HTCondor requirement for TW image

State: closed
Opened: 2025-05-29T17:14:45Z
Closed: 2025-06-03T08:57:48Z
Labels: Type: Bug, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/9102

## Opening post (belforte, 2025-05-29T17:14:45Z)

we currently have
https://github.com/dmwm/CRABServer/blob/31035ba5494d03c3f1aecba84a41c8606a27cdf0/cicd/crabtaskworker_pypi/requirements.txt#L6
but that exact release is not available on Pypi anymore. We need to use a `>=` logic 

I verified that this works
```
htcondor~=24.3
```
while `~=24.3.0` does not

## Comment (belforte, 2025-05-29T17:17:32Z)

@aspiringmind-code I am assigning to you not because I too lazy to do the edit, but becasue I want to make sure that you are aware of the dependencies in the build process and be prepared to fix possible future similar problem (the build pipeline fails until this is fixed, so it is reasonably urgent)

## Comment (aspiringmind-code, 2025-06-03T08:43:08Z)

Ok, thanks. I'll do it.
