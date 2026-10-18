# dmwm/CRABServer issue #8655: remove check  for `username_CRAB` username for myproxy.

State: closed
Opened: 2024-08-27T14:10:02Z
Closed: 2024-08-27T23:02:52Z
Labels: Area: Code Cleanup, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8655

## Opening post (belforte, 2024-08-27T14:10:02Z)

I introduced it to simplify things, but it can not work since it breaks when users change their DN.
We have to stick with the DN hash.
Indeed CRABClient does not create this credential anymore: https://github.com/dmwm/CRABClient/blob/65a8e7ac63e2328445e1d467c37016a8efab3e08/src/python/CRABClient/CredentialInteractions.py#L66

And now I am really annoyed by the spurious error messages, which can also trigger other errors.
