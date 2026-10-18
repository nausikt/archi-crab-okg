# dmwm/CRABClient pull request #5184: submit --dryrun. print info about last trial

State: closed
Opened: 2023-01-24T13:28:40Z
Closed: 2023-01-24T13:29:44Z
Merged: 2023-01-24T13:29:44Z
URL: https://github.com/dmwm/CRABClient/pull/5184

## Opening post (mapellidario, 2023-01-24T13:28:40Z)

Related to https://github.com/dmwm/CRABServer/issues/7493 

### status

tested

### description

submit --dryrun needs to run for at least 25s in order not to make its estimates based on very few small events. If the first dryrun attempt is too short, the same cmsRun command is called again, with an increasing number of events. with this commit, every trial reports how long it took and how many events the next trial will process.

As suggested by stefano in https://github.com/dmwm/CRABServer/issues/7493#issuecomment-1398722319, we have

```plaintext
> crab submit --dryrun
[...]
Please wait...
Task status: UPLOADED

Created temporary directory for dry run sandbox in /tmp/dmapelli/tmpp3ytfqpx
Executing test, please wait...
Last trial took only 17.4 seconds. We are trying now with 7985 events
Last trial took only 14.0 seconds. We are trying now with 15556 events
Last trial took only 13.9 seconds. We are trying now with 26811 events
^CKeyboard Interrupted
Log file is [...]/crab.log
```

(nb: in the test above I am using skipEvents to process only 300 events at each run, which is why the runtime does not increase at every new trial.)

## Comment (mapellidario, 2023-01-24T13:29:12Z)

Since we already agreed on this change, since it looks pretty simple, since I tested it, i am merging this myself.
