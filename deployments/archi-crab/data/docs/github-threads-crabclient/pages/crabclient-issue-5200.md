# dmwm/CRABClient issue #5200: make sure error message about sanbox size is clearly visible

State: closed
Opened: 2023-07-07T13:55:07Z
Closed: 2023-10-09T21:19:50Z
Labels: HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5200

## Opening post (belforte, 2023-07-07T13:55:07Z)

a user [reported](https://cms-talk.web.cern.ch/t/crab-submission-no-longer-working/26395) that 
```
Error message: Error: input tarball size 235 MB exceeds maximum allowed limit of 120 MB
```
scrolled away of the console and/or was not clearly visible.

## Comment (belforte, 2023-10-09T21:00:10Z)

Let's only print the msg
Error message: Error: input tarball size 149 MB exceeds maximum allowed limit of 120 MB
and the first 5 files sorted by size to the console. And the rest only in crab.log.
