# dmwm/CRABServer issue #7667: wrong signature for uploadWarning inside TapeRecallManager

State: closed
Opened: 2023-06-15T15:22:56Z
Closed: 2023-06-15T16:33:06Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7667

## Opening post (belforte, 2023-06-15T15:22:56Z)

somehow we never hit the condition "rule not found in Rucio", but these lines need to be "reconciled"

https://github.com/dmwm/CRABServer/blob/f8177524190d57f89801f3bfa617d0cd31e88612/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L96

https://github.com/dmwm/CRABServer/blob/f8177524190d57f89801f3bfa617d0cd31e88612/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L174

## Comment (belforte, 2023-06-15T15:26:24Z)

I suspect there would have been no way for pylint to spot this
