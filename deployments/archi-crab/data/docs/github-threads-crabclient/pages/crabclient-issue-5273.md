# dmwm/CRABClient issue #5273: resubmission of successful jobs only works when Dagman is running

State: closed
Opened: 2023-12-06T17:55:52Z
Closed: 2024-01-10T16:33:25Z
Labels: Documentation, MediumPrio
URL: https://github.com/dmwm/CRABClient/issues/5273

## Opening post (belforte, 2023-12-06T17:55:52Z)

it is not possible anymore once Dagman completed.
Document properly in `crab --help`, or fix it TW side.

## Comment (belforte, 2023-12-08T19:24:43Z)

Seems that all we need to do is to document.
- [x] modify HELP for `crab resubmit`  #5275
- [x] check and modify as needed twiki

## Comment (belforte, 2023-12-15T14:38:51Z)

reopen. Will close after fixing documentation.

## Comment (belforte, 2024-01-10T16:33:12Z)

Since we agreed that we do not want to support resubmission of succesful jobs, I removed mentions of this in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3Commands
I have not found any other place where it was mentioned in the twikis.
