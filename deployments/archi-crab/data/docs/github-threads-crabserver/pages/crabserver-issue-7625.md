# dmwm/CRABServer issue #7625: Document and review CRAB Task state machine

State: open
Opened: 2023-05-03T12:02:42Z
Labels: Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7625

## Opening post (belforte, 2023-05-03T12:02:42Z)

The old [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CMSCrabTaskStates) was already obsolete before we introduced TAPERECALL, as stated in the first lines there.

We have moved from them to : `status` it not simply the `status` filed in the DB, but it also matters which command we are executing, i.e. the `Command` field in the DB.

See also discussion and a tentative new diagram in https://github.com/dmwm/CRABServer/pull/7620

We need to document (which requires reviewing the code and making tests) and review to make sure it is well understood and cleanly implemented.
