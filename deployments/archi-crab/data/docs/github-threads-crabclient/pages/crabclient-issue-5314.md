# dmwm/CRABClient issue #5314: crab client bash completions do not respect custom sorting order

State: closed
Opened: 2024-05-14T14:14:20Z
Closed: 2024-05-23T09:24:29Z
Labels: enhancement, In Progress
URL: https://github.com/dmwm/CRABClient/issues/5314

## Opening post (mapellidario, 2024-05-14T14:14:20Z)

### problem

When using the crab client the suggestions do not respect the desired sorting. I get

```bash
[dmapelli@lxplus9105 ~]$ crab <tab><tab>
--debug           -h                checkwrite        kill              report            status
--help            checkdataset      createmyproxy     preparelocal      resubmit          submit
--quiet           checkfile         getlog            proceed           setdatasetstatus  tasks
--version         checkusername     getoutput         remake            setfilestatus     uploadlog
```

Despite we explicitly asked for

```bash
COMPREPLY=( $(compgen -W '--version --help -h --quiet --debug status tasks proceed checkwrite getlog checkusername checkdataset checkfile submit getoutput resubmit kill uploadlog remake report preparelocal createmyproxy setdatasetstatus setfilestatus' -- $cur) )
```

### solution

PR on its way...
