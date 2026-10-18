# dmwm/CRABServer issue #9328: periodically cleanup /store/user/crabint1

State: open
Opened: 2026-06-23T08:24:58Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9328

## Opening post (belforte, 2026-06-23T08:24:58Z)

It looks like we never (!?) cleanup the EOS directory where our pipeline jobs write output, i.e. `/cms/eos/user/store/crabint1` on CERN EOS

<img width="893" height="137" alt="Image" src="https://github.com/user-attachments/assets/1e60dcb5-eb27-4c2f-bcee-956a8c6e4fb1" />

There are files as old as May 2024
```console
belforte@lxplus800/0000> pwd
/eos/cms/store/user/crabint1/GenericTTbar/autotest-1714770940/240503_211540/0000
belforte@lxplus800/0000> ls -l|head -2
total 50593
-rw-r--r--. 1 cmsprod zh 5417952 May  3  2024 output_1.root
belforte@lxplus800/0000> 
```

We need a periodic cleanup. Deleting files in the pipeline may be annoying since it will have to be done using X509 authentication and `gfal-*` commands, maybe setting up an `acrontab` script in `crabint1` account is better. But we need to be sure we do not forget to check that it keeps working ! (a panel of used quota for this and Rucio output in Grafana Overview ?)

## Comment (nausikt, 2026-06-23T09:00:22Z)

Roger that, will give this fair priority.

## Comment (belforte, 2026-06-23T09:20:12Z)

do not forget, but also note that we are only 50% full after 2 years ... Maybe a rm * by hand every 3 months is enough !
