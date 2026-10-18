# dmwm/CRABServer pull request #9092: use docker dns in runContainer script

State: closed
Opened: 2025-05-23T12:20:10Z
Closed: 2025-05-23T12:35:32Z
Merged: 2025-05-23T12:35:32Z
URL: https://github.com/dmwm/CRABServer/pull/9092

## Opening post (aspiringmind-code, 2025-05-23T12:20:10Z)

Fix #9074 
Inside the containers:
DNS was not going through the host’s DNS cache (127.0.0.53 managed by systemd-resolved).
Instead, containers were resolving domains directly via CERN’s upstream DNS servers (137.138.16.5, etc.), bypassing the host's caching and configuration. This behavior was not desired, as it breaks centralized DNS resolution and caching.
 
By using --dns $HOST_IP Now containers resolve DNS via the host’s DNS stack (e.g., systemd-resolved), achieving DNS caching and consistent config. resolv.conf inside the container matches the host's. DNS queries from inside the container route via the host's resolver (systemd-resolved). No more direct queries from containers to CERN DNS servers.

## Comment (cmsdmwmbot, 2025-05-23T12:21:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2482/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-23T12:24:41Z)

change looks good, but I'd love to see a "log" before and after to prove that it works. It will also serve as documentation of the way to check things inside the container.

## Comment (aspiringmind-code, 2025-05-23T12:39:44Z)

I will try to get the before and after logs.

## Comment (belforte, 2025-05-23T12:49:04Z)

:pray:
