# dmwm/CRABServer issue #8630: adapt CheckTapeRecall to "account=username"

State: closed
Opened: 2024-08-17T11:08:58Z
Closed: 2024-08-19T17:14:46Z
Labels: Type: Bug, Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8630

## Opening post (belforte, 2024-08-17T11:08:58Z)

Now we set Rucio account = username when we make a tape recall rule.
So that a quota on user can be implemented.
But the current CheckTapeRecall code looks for rules with `account=crab_tape_recall`

Hopefully it is enough to change to `activity=Analysis TapeRecall`

## Comment (belforte, 2024-08-17T13:37:54Z)

take this chance also to make it explicit which Rucio account to use, since our robot certificate now can authenticate as any of `crabserver`, `crab_input`, `crab_tape_recall`
