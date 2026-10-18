# dmwm/CRABServer issue #9409: update allowed users/groups in puppet

State: open
Opened: 2026-09-03T14:21:54Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9409

## Opening post (belforte, 2026-09-03T14:21:54Z)

in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein
we still have files with the old 
`sssd::interactiveallowgroups` and  `sssd::interactiveallowusers` which were working on SL7 **only**.
Now they do nothing and must be replaced with the new classes as per
https://configdocs.web.cern.ch/access/interactive.html#c8-example

(note that EL8 in there acutally means >= EL8)

## Comment (belforte, 2026-09-03T14:25:02Z)

with reference to this mattermost chat
https://mattermost.web.cern.ch/it-dep/pl/ukesgj9m8jgd9d89n38ormyako

which also has interesting tips about how to check who can login, which are worth adding to https://cmscrab.docs.cern.ch/operations/tips-and-tricks.html#puppet

## Comment (nausikt, 2026-09-03T14:25:55Z)

Acknowledged, Thanks for hints!

## Comment (belforte, 2026-10-09T12:27:13Z)

Note also this 
https://mattermost.web.cern.ch/it-dep/pl/yqctsdxx9ff5tmmmzxxkd3f9cy
