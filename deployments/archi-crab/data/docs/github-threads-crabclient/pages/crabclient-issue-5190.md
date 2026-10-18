# dmwm/CRABClient issue #5190: adapt to SL6 container

State: open
Opened: 2023-03-16T17:14:26Z
Labels: enhancement, MediumPrio
URL: https://github.com/dmwm/CRABClient/issues/5190

## Opening post (belforte, 2023-03-16T17:14:26Z)

when running inside `cmssw-cc6` should simply skip calls to `myproxy` or `gfal` and print proper warnings instead.
Should manage to make it work in SL6 w/o the need to use --proxy option.

## Comment (belforte, 2023-03-16T17:16:56Z)

a way to detect where we are running, in the env:
`SINGULARITY_NAME=slc6:x86_64`

## Comment (belforte, 2023-10-09T21:52:29Z)

not really that high priority !

## Comment (belforte, 2024-01-10T11:07:01Z)

better solution
* only allow `crab submit` and `crab status` commands. For everything else tell users to use el7 or newer container
