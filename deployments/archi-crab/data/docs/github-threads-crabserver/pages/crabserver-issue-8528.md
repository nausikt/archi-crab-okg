# dmwm/CRABServer issue #8528: rationalize configurations and common functions

State: open
Opened: 2024-06-26T15:35:38Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8528

## Opening post (belforte, 2024-06-26T15:35:38Z)

We have a lot of duplication here and there of both code and configuration parameters.
We should aim for
 1. capture in some common functions the details and how we instantiate CRABServer, DBSClient, RucioClient so that we simply pass a configuration object to them and reuse those everywhere.
 2. reorganize configuration files to have one section for each such service so that we can e.g. do something like
 ```python
config = loadConfigFromFile()
rucioClient = getRucioClient(config.Rucio)
crabServer = getCrabServer(config.REST)
```
3. reorganize puppet templates and hiera variables so that we avoid duplications.  E.g. reflect the current practice that one TW VM will point all its services (TW, Publishers) to same REST instance.

4. keep only real secrets in tbag and more non-secrete part of CRABRest configuration to plain GH files  https://github.com/dmwm/CRABServer/issues/7396

This includes the work already laid out in #7624 and correlates with #7765 and the reorganization of utility functions discussed in there.


We discussed in Udine and agreed.

**TODO**

- [x] document strategy (to be done here by Stefano) including CRABClient and Publisher
   * after some thinking, description above is good enough and simply writing the new configuration files will do
   * breaking down in following steps
- [ ] add new sections to TW and Pub config. files with new structure and deploy
- [ ] modifty code to use it for
    - [ ]  TW
    - [ ] Pub Sched
    - [ ] Pub Rucio
- [ ] deploy new code
- [ ] cleanup config files 
- [ ] code change as per #7396
- [ ] code change as per #7624
- [ ] code change as per #7765
