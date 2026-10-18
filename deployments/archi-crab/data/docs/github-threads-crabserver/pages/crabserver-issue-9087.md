# dmwm/CRABServer issue #9087: add --debug option to commands in clientValidation.sh

State: open
Opened: 2025-05-21T14:30:24Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9087

## Opening post (belforte, 2025-05-21T14:30:24Z)

is a test in clientValidation.sh fails, there is usually very littlle information the current test log, and looking up the crab.log file on the runner is difficult.

We can start by making all commands more verbose adding the `--debug` option, i.e. change `crab <command>` to `crab --debug <command>` so that logging.debug message are printed.

## Comment (belforte, 2025-08-20T10:08:11Z)

another (better?) possibility is to print the crab.log in case the command failed. Keep the log clean when possible.

## Comment (nausikt, 2025-08-20T10:08:57Z)

Thanks for hints man, Acknowledge.
