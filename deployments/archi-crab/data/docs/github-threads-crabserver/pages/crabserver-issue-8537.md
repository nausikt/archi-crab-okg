# dmwm/CRABServer issue #8537: [PyPI] Use local timezone for all images

State: closed
Opened: 2024-06-28T14:13:46Z
Closed: 2024-07-09T11:19:06Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8537

## Opening post (novicecpp, 2024-06-28T14:13:46Z)

Current timezone of new PyPI images is UTC

We have different localtime between RPM and PyPI
![timezone_diff](https://github.com/dmwm/CRABServer/assets/2346664/4a438e6b-0fad-4d98-90f9-f2cf8ecd245c)

Add one line change in Dockerfile should fix it.

And maybe also apply TZ env to docker runner https://stackoverflow.com/questions/57607381/how-do-i-change-timezone-in-a-docker-container

## Comment (belforte, 2024-06-28T14:41:04Z)

curious that ever if PyPI container is in UTC, when I added `%Z` to `date` format in bash scripts, it printed correct local tima and CEST as time zone.

## Comment (novicecpp, 2024-06-28T14:44:52Z)

> when I added %Z to date format in bash scripts, it printed correct local tima and CEST as time zone.

That is the shell runner. It run the job *directly* on VM host. 
Docker runner run the job *inside docker container* on VM host.
