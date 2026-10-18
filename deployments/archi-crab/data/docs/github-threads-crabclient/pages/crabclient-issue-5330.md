# dmwm/CRABClient issue #5330: add FileSplitting to use cases covered by `crab recovery`

State: closed
Opened: 2024-08-28T18:27:27Z
Closed: 2024-12-18T11:27:55Z
Labels: enhancement, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5330

## Opening post (belforte, 2024-08-28T18:27:27Z)

Dario showed me where to change code.
Should be easy since the lit of input files for each job is in the `input_files.tar.gz` file on the scheduler, which we can retrieve with wget

## Comment (belforte, 2024-11-07T12:13:24Z)

better do "now" before I fully forget what Dario showed to me !

## Comment (belforte, 2024-12-16T16:59:25Z)

I am currently thinking that it is better to modify `crab report` adding a `--file` option so that it creates the lists of files to processed and files processed OK. It may be useful anyhow and cleaner than do this inside `recovery`.

I am not sure yet if to switch in that mode automatically when task has `fileBased` splitting, or use the `--files` options. Or whether to make those lists anyhow all of the times !

opened new issue for that: https://github.com/dmwm/CRABClient/issues/5365
