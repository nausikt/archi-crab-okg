# dmwm/CRABServer issue #9443: submit_env.sh does not pass correctly exit code to called

State: open
Opened: 2026-10-14T15:15:52Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9443

## Opening post (belforte, 2026-10-14T15:15:52Z)

see e.g. the example in #9441 where the top wrapper sees exit code 251 (=11003%256) rather then 11003 as per
https://github.com/dmwm/CRABServer/blob/30286f7d5b215860e5b6da0edda0553b446d813d/scripts/job_wrapper/submit_env.sh#L63-L65

## Comment (belforte, 2026-10-14T16:40:32Z)

one can't pass env.vars from a script to the calling script, and the exit value of the script is cut to mod(256) by bash,  but it
turns out that we have already established a way to pass long exit codes around, via the file
`jobReport.exitCode.txt`
which is currently used to pass long exit code value from `CMSRunAnalysis.py`  e.g. in
https://github.com/dmwm/CRABServer/blob/30286f7d5b215860e5b6da0edda0553b446d813d/scripts/job_wrapper/CMSRunAnalysis.py#L264-L265

The same can be used when a function from `submit_env.sh` fails
