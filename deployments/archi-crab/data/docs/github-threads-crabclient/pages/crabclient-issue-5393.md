# dmwm/CRABClient issue #5393: crab preparelocal should use new `tm_uploaded` flag in Task table

State: closed
Opened: 2025-06-04T09:03:10Z
Closed: 2025-07-22T14:21:47Z
Labels: enhancement
URL: https://github.com/dmwm/CRABClient/issues/5393

## Opening post (belforte, 2025-06-04T09:03:10Z)

instead of checking for `UPLOADED` status, since now `preparelocal` can work also on tasks which are submitted.
ref:
https://github.com/dmwm/CRABServer/issues/8928
https://github.com/dmwm/CRABClient/issues/5371#issuecomment-2662962817

this will make for a much cleaner situation wrt to current "list of bad states"
