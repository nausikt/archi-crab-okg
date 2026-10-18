# dmwm/CRABServer issue #9074: High number of DNS queries from prod-tw01

State: closed
Opened: 2025-05-15T08:03:58Z
Closed: 2025-05-23T12:35:33Z
URL: https://github.com/dmwm/CRABServer/issues/9074

## Opening post (aspiringmind-code, 2025-05-15T08:03:58Z)

We get the following mail from the Spectrum Service occasionally:
```
You are listed as responsible for crab-prod-tw01 (.cern.ch).
Our DNS servers are warning that this host has been sending a VERY HIGH
rate of queries for the last hour (65.71444444444444 requests/sec).

Please, check the cause of this problem and sort it out
since it impacts the central DNS service performance. Please
also consult https://codimd.web.cern.ch/bM1_cKzkTGm0qX-8asLxwQ?view#DNS-Caching (alma9) or
http://service-dns.web.cern.ch/service-dns/faq.asp
for information on setting up dns for high demanding clients (page accessible from CERN network only).

Should this problem continue, we will have to block this system
to avoid performance problems in the central DNS service.

        Thanks in advance,
                                    CERN Network Support

More info: crab-prod-tw01
|                        |               |                  On IP DNS servers | queries/sec during 15 min |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                     --- TOTAL ---  |       65 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                     cmsweb.cern.ch |      65.6 queries/sec     |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                   monit-dc.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                 monit-otlp.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |          caproxylbp-meyrin.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                agileinf-mb.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                     cerndc.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |   cmsgwms-collector-global.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                 cmssst.web.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 |                cmsweb-prod.cern.ch |      0.0 queries/sec      |
| crab-prod-tw01.cern.ch | 137.138.53.39 | it-puppet-masters-public-b.cern.ch |      0.0 queries/sec      |
-cms-service-crab3htcondor@cern.ch-
cms-service-crab3htcondor@cern.ch  
```

It wasn't frequent enough before to call for a deep-dive investigation. See [old issue](https://github.com/dmwm/CRABServer/issues/7287) However, since the hypervisor migration on 23 April 2025, it became much too frequent. A [ticket](https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC4462896) was raised.

The problem and the proposed solution are described below:
crab-prod-tw01.cern.ch, is generating a very high rate of DNS queries (93.2 requests/sec), which is impacting CERN's central DNS service. The issue seems to be linked to how DNS resolution is handled, particularly in the Docker container running on the host.

**Host Configuration:**
The host (/etc/resolv.conf) is configured with a local DNS resolver: 127.0.0.53.
This points to systemd-resolved, which should act as a caching layer to reduce the load on upstream DNS servers.

**Container Configuration:**
Inside the Docker container, the resolv.conf is directly using CERN's DNS servers (137.138.16.5, 137.138.17.5, etc.) instead of 127.0.0.53.
This means systemd-resolved's caching is bypassed entirely, and all DNS queries are sent directly to CERN's DNS servers, resulting in high query rates.

**Docker Networking Mode:**
We are using --net host, which means the container shares the host’s network stack, but it does not automatically use the host's DNS caching (127.0.0.53).
Docker just copies the host's resolv.conf when the container starts.
Since the host's resolv.conf points to 127.0.0.53, Docker replaces it with the actual DNS servers during container startup.

**Missing Tools Inside the Container:**
Basic diagnostic tools like resolvectl and journalctl are not available in the container, which makes it harder to debug DNS resolution from inside.
Most Docker containers don't run systemd by design (they're meant to run a single process). 
Use dnsutils for dns resolution instead of systemd resolved
docker logs <container_name> --tail 50 --follow instead of journalctl

**Solutions:**
**Use the Host's Local Resolver (127.0.0.53) Inside the Container:**
Add the following flag when running Docker:
docker run --net host **--dns 127.0.0.53** …
This forces the container to query the host's systemd-resolved instead of CERN's DNS servers directly.
Expose 127.0.0.53 to Docker Containers: Make sure Docker’s --net host mode respects local DNS caching or configure nftable rules

**Monitor DNS Queries:**
Enable debugging on systemd-resolved:
resolvectl log-level DEBUG: Use dnsutils instead
journalctl -f -u systemd-resolved.service: Use docker logs instead
Inside the container, we can also use tcpdump or wireshark to check outgoing DNS queries: tcpdump may have to be installed first…did in TW

**Verify Docker Configuration:**
Ran docker inspect <container-id> and checked the DNS settings.
All DNS options empty/not set
Also, inspected Docker’s global configuration:
cat /etc/docker/daemon.json  This docker folder is empty…has no such file.
Looked for any DNS configurations that might override the host settings.
