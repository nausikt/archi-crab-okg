# dmwm/CRABServer issue #8282: port Prometheus setup in VM's to alma9

State: closed
Opened: 2024-03-13T14:58:04Z
Closed: 2024-04-09T09:40:00Z
Labels: Priority: High, alma9
URL: https://github.com/dmwm/CRABServer/issues/8282

## Opening post (belforte, 2024-03-13T14:58:04Z)

- [x] we never tested current puppet code on alma9 yet
- [x] possibly not needed since`node_exporters` are now available via yum https://github.com/dmwm/CRABServer/issues/8258#issuecomment-1994123598
- [x] the firewall rules need  to be changed from using `firewall` to `nftables`
- [x] also a chance to revisit if we really need all those ports or there is some historic/legacy extra noise

## Comment (mapellidario, 2024-04-02T11:34:11Z)

I implemented the changes in this [commit](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/d1ce7af6ae656a0625f0abfcc64dea569c89e312) and the data is already reaching [grafana](https://monit-grafana.cern.ch/d/rYdddlPWkk/node-exporter-full-crab-vms?orgId=11&refresh=1m&from=now-30m&to=now). 

ideas:

- install node_exporter via yum repos
- no need of an additional "startup.sh" script, using a systemd unit instead. @novicecpp I copied what you did for wmarchiveuploader, it works for now, I do not think we will need to change any unit parameter
- open the port 9100, serving the metric via http (no https). This port is accessible from inside cern network only thanks to cern firewall confguration. no need for whitelisting cmsmonitoring machines

I am open to suggestions in case you don't like the implementation

## Comment (belforte, 2024-04-02T12:41:53Z)

Inside CERN LAN is not really secure. lxplus is quite unsafe (at least in the eyes of CERN comp. security). And htttp (not s) similarly.

So I would rather switch to https and whitelist w/o waiting for complains in next security scan.

## Comment (novicecpp, 2024-04-02T13:10:18Z)

In my limited experience (more likely I have never done it before), it is not easy to set up on exporter https on both the client (cert/rotation) and server (config) sides.  Better to ask CMSMONIT how they do this.

Use http should be fine. node_exporter metrics should not contains any sensitive information other than node name and kernel version.

## Comment (novicecpp, 2024-04-02T13:11:41Z)

For the second bullet, I am a bit surprised that MONIT did not provide the unit file.

## Comment (belforte, 2024-04-02T13:28:49Z)

The point with open ports is not what data we send, but what's the security of the service connected to the port, whether it has bugs that may allow an attacker use it to enter the system. If Prometheus importer wants not-encrypted data, we can surely comply.

## Comment (mapellidario, 2024-04-02T14:02:02Z)

> Inside CERN LAN is not really secure. lxplus is quite unsafe (at least in the eyes of CERN comp. security). And htttp (not s) similarly.
> 
> So I would rather switch to https and whitelist w/o waiting for complains in next security scan.

Just a comment: i did not really changed it. it is already like that for cc7, we already providing all the metrics via http to whoever wants to read from that, the whitelist is already useless on cc7. You can check yourself with curl from any lxplus node [1]

[1]

```bash
curl http://vocms0199.cern.ch:9100/metrics
```

## Comment (mapellidario, 2024-04-02T14:08:10Z)

> For the second bullet, I am a bit surprised that MONIT did not provide the unit file.

not that i could find: [1] [2]

[1]

```plaintext
[root@vocms0107 ~]# rpm -ql node_exporter
/usr/bin/node_exporter
/usr/share/licenses/node_exporter
/usr/share/licenses/node_exporter/LICENSE
```

[2] https://koji.cern.ch/buildinfo?buildID=66817, https://gitlab.cern.ch/monitoring/rpms/exporters/node-exporter

## Comment (belforte, 2024-04-02T17:05:56Z)

OK. I surrender.

## Comment (belforte, 2024-04-04T12:23:28Z)

Dario, shall we mark this as done ?

## Comment (mapellidario, 2024-04-09T09:40:01Z)

Data from node_exporter looks good to me, I will close this issue
