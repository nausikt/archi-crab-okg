# dmwm/CRABServer issue #8439: remove openldap from TW container

State: closed
Opened: 2024-05-29T08:48:37Z
Closed: 2026-01-28T11:24:34Z
Labels: Area: Code Cleanup, PyPI, alma9
URL: https://github.com/dmwm/CRABServer/issues/8439

## Opening post (belforte, 2024-05-29T08:48:37Z)

we now use CRIC to reselve e-groups content. No need for openldap and its dependencies.

## Comment (belforte, 2024-06-12T10:34:09Z)

hmm... looks like code still uses LDAP both in TW and scheduler. Also for high priority users
@novicecpp do you remember why we did not change ?
there are 2 use cases:
* group --> lit of users (for high prio)
* user --> groups they belong to (in several places, I still have to understand exactly what for)

## Comment (novicecpp, 2024-06-12T12:01:22Z)

What do you mean? This one https://github.com/dmwm/CRABServer/issues/7560#issuecomment-1923531953 ?
We want to remove the LDAP deps but keep high prio system, no? 

I forgot about the schedd part and I do not know about the second bullet. I can have a look later.

## Comment (novicecpp, 2024-06-12T12:02:44Z)

FYI, this task is stuck because I want to use egroup name from `highPrioEgroups` config to get the group object id in CRIC and then list all user there later. But it look like CRIC does not have such API.

## Comment (belforte, 2024-06-12T12:11:04Z)

I see. OK, this is consistent with what I saw. I am not sure I understand your question though. Maybe we have too many names for the same thing ?
Leave the second bullet to me, I want to find out what the purpose is.

## Comment (belforte, 2026-01-28T11:24:34Z)

this is  now replaced by #9224
