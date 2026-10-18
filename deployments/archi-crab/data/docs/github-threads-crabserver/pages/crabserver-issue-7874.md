# dmwm/CRABServer issue #7874: puppet - logrotate config should be 0644

State: closed
Opened: 2023-09-14T08:48:07Z
Closed: 2024-09-18T14:42:12Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7874

## Opening post (mapellidario, 2023-09-14T08:48:07Z)

#### problem

While managing the cronjob for spark, i noticed that `logrotate` ignores some of the config that we setup in puppet because we set the config files to have `mode = 0755`, while lograte requires it to be `mode = 0644` [1]. This affects both taskworker and schedd machines.

This is inconvenient, but can also be a problem. For example, on vocms059 the file `/var/log/crab/JobAutoTuner.log` is 130MB, starting from 202-07-26. 

<details>

```plaintext
[root@vocms059 dmapelli]# ls -lh /var/log/crab/
total 134M
-rw-r--r--. 1 root   root   257K Sep 10 00:00 cleanup_home_grid.log
-rw-r--r--. 1 condor condor 131M Sep 14 10:34 JobAutoTuner.log
-rw-r--r--. 1 root   root   2.4M Sep 14 06:10 JobCleanup.log
[root@vocms059 dmapelli]# head /var/log/crab/JobAutoTuner.log
2020-07-26 11:26:58,250:INFO:JobAutoTuner,44:=========================================================================
2020-07-26 11:26:58,251:INFO:JobAutoTuner,57:-------------------- JobTimeTuner.py was not enabled --------------------
2020-07-26 11:26:58,251:INFO:JobAutoTuner,71:-------------------- CMSLPCRoute.py was not enabled  --------------------
2020-07-26 11:26:58,251:INFO:JobAutoTuner,76:-------------------- Routes added by Overflow.py  --------------------
2020-07-26 11:26:58,251:INFO:Overflow,1003:=================== An Overflow object instance start! ===================
2020-07-26 11:26:58,252:WARNING:Overflow,937:Config key: JAT_OVERFLOW_serviceKey not set in condor using the default value.
2020-07-26 11:26:58,252:WARNING:Overflow,937:Config key: JAT_OVERFLOW_serviceCert not set in condor using the default value.
2020-07-26 11:26:58,252:WARNING:Overflow,937:Config key: JAT_OVERFLOW_level not set in condor using the default value.
2020-07-26 11:26:58,266:WARNING:Overflow,937:Config key: JAT_OVERFLOW_collector not set in condor using the default value.
2020-07-26 11:27:00,305:INFO:JobAutoTuner,88:=========================================================================
[root@vocms059 dmapelli]# tail /var/log/crab/JobAutoTuner.log
  File "/data/srv/SubmissionInfrastructureScripts/JobAutoTuner.py", line 79, in main
    overflow.run()
  File "/data/srv/SubmissionInfrastructureScripts/Overflow/Overflow.py", line 1190, in run
    self.overflow(jobsInThisSchedd, self.config.ovLevel, self.config.ovType)
  File "/data/srv/SubmissionInfrastructureScripts/Overflow/Overflow.py", line 1122, in overflow
    if self.estimator.needOverflow(jobObj):
  File "/data/srv/SubmissionInfrastructureScripts/Overflow/Overflow.py", line 508, in needOverflow
    currIdleTime = jobObject["ServerTime"] - jobObject["QDate"]
KeyError: 'ServerTime'
2023-09-14 10:34:04,385:INFO:JobAutoTuner,88:=========================================================================
```

</details>

#### solution

We need to change the mode for logrotate config file from 0755 to 0644, for example here:

https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/fa42ad9d8145566ca8330f7b19e7ea4d6352fa6f/code/manifests/crabschedd.pp#L195

---

[1]

<details><summary>logrotate log on crab-dev-tw04</summary>

```plaintext
[root@crab-dev-tw04 dmapelli]# /usr/sbin/logrotate -f -d /etc/logrotate.conf
reading config file /etc/logrotate.conf
including /etc/logrotate.d
reading config file btmp
reading config file chrony
reading config file collectd_logs
error: Ignoring crabspark because of bad file mode - must be 0644 or 0444.
error: Ignoring diskTest because of bad file mode - must be 0644 or 0444.
reading config file distro_sync
reading config file eos-fusex-logs
[...]
```

</details> 

<details><summary>logrotate on vocms059</summary>

```plaintext
[root@vocms059 dmapelli]# /usr/sbin/logrotate -f -d /etc/logrotate.conf
reading config file /etc/logrotate.conf
including /etc/logrotate.d
reading config file btmp
reading config file chrony
error: Ignoring cleanup_home_grid because of bad file mode - must be 0644 or 0444.
reading config file collectd_logs
reading config file cups
error: Ignoring diskTest because of bad file mode - must be 0644 or 0444.
reading config file distro_sync
reading config file firewalld
reading config file flume-agent-collectd
Ignoring hourly because it's not a regular file.
reading config file httpd
reading config file iptables
error: Ignoring job_auto_tuner because of bad file mode - must be 0644 or 0444.
error: Ignoring job_cleanup because of bad file mode - must be 0644 or 0444.
reading config file lpadmincern
reading config file mcollective-audit
reading config file mcollective-metadata
```

</details>

## Comment (aspiringmind-code, 2024-09-18T14:42:12Z)

Issue resolved in MR https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/259
