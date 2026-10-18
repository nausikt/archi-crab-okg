# dmwm/CRABServer issue #9231: cleanup CRABServer/bin

State: closed
Opened: 2025-11-17T10:52:42Z
Closed: 2025-11-19T09:53:13Z
Labels: Status: Done, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9231

## Opening post (belforte, 2025-11-17T10:52:42Z)

most (all?) files there are old relics..

```console
LapSB:CRABServer$ tree bin
bin
|-- TunePylint.py
|-- dag_bootstrap_startup.sh
|-- dag_data_workflow.sh
|-- ftscp.py
|-- htcondor_make_runtime.sh
|-- logon_myproxy_openssl.py
|-- publisher.sh
|-- setupdb.sh
`-- test_write_to_outputs.sh
```

In particular `dag_bootstrap_startup.sh` is bad as it duplicates the acutally used one in `scripts`
