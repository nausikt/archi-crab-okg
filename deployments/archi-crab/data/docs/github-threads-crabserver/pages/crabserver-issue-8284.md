# dmwm/CRABServer issue #8284: port dag_bootstrap.sh to alma9

State: closed
Opened: 2024-03-14T15:34:19Z
Closed: 2024-03-15T10:14:38Z
Labels: Status: Done, Priority: TOP, alma9
URL: https://github.com/dmwm/CRABServer/issues/8284

## Opening post (belforte, 2024-03-14T15:34:19Z)

(no text)

## Comment (belforte, 2024-03-15T09:19:39Z)

I surely do not understand yet how things work, because can not make sense of the fact that tasks could be running on alma9 without this !
For sure it was breaking [running PostJob interactively](https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3OperatorDebugging#To_run_a_post_job_on_the_schedd)
It may be that when called inside an environment prepared by `dag_bootstrap_startup.sh` the addition of SL7 binaries in PYTHONPATH was harmless. 
Anyhow it is surely better to consistently point to correct stuff !
