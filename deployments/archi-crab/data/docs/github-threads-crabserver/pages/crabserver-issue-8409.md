# dmwm/CRABServer issue #8409: remove code only needed for transistion to "accelerators" 

State: closed
Opened: 2024-05-15T21:09:17Z
Closed: 2024-05-16T13:40:43Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8409

## Opening post (belforte, 2024-05-15T21:09:17Z)

see the point about misspelled `accceleratorparams` with 3 `c`'s in https://github.com/dmwm/CRABServer/pull/8408#issue-2298807895

## Comment (novicecpp, 2024-05-16T06:19:12Z)

I do not think we should remove those code. It will be used for the new configuration in the future.
Relate https://github.com/dmwm/CRABServer/issues/7552

## Comment (belforte, 2024-05-16T08:26:49Z)

OK. Let's simply fix the typo then. Odd that it did not lead to an error :thinking:
