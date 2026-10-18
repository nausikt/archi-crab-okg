# dmwm/CRABServer pull request #9246: bump htcondor to latest stable 25.4.0.

State: closed
Opened: 2025-12-12T17:41:30Z
Closed: 2025-12-12T17:41:44Z
Merged: 2025-12-12T17:41:44Z
URL: https://github.com/dmwm/CRABServer/pull/9246

## Opening post (nausikt, 2025-12-12T17:41:30Z)

In response to Stefano upgrading ***All*** CRAB *APs* today. We will bump client in **TW** accordingly now.

## Comment (belforte, 2025-12-12T19:47:01Z)

@nausikt pleaase be aware that stable (i.e. LTS) HTC releases are 25.0.x 
25.4.x denotes a so called "feature release" i.e.  the new things which will become the basis of next year 26.0.x by adding new features, once those features have "stabilized"
See: https://htcondor.readthedocs.io/en/latest/version-history/introduction-version-history.html

I humbly suggest to use same 25.0.3 as we use in AP's for the TaskWorkers

Unless of course you see a strong reason not to use an LTS release.

## Comment (nausikt, 2025-12-12T19:48:48Z)

Acknowledged man.
