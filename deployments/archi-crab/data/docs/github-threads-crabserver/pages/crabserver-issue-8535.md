# dmwm/CRABServer issue #8535: fix /opt/rucio/etc/rucio.cfg in pypi contaiiners

State: closed
Opened: 2024-06-28T11:10:26Z
Closed: 2024-06-28T11:18:30Z
URL: https://github.com/dmwm/CRABServer/issues/8535

## Opening post (belforte, 2024-06-28T11:10:26Z)

rucio CLI does not work in new containers because the rucio.cfg does not define the `ca_cert` directory.
In the code we take this from the `TaskWorker(Publisher)Config.py` in `./current`.

We need to point to same place as in there: `/etc/grid-security/certificates/` which we mount from the host in the container
