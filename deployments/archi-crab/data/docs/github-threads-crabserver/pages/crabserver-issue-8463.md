# dmwm/CRABServer issue #8463: decouple our qa from epel testing

State: closed
Opened: 2024-06-03T13:42:50Z
Closed: 2024-06-17T08:22:21Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8463

## Opening post (belforte, 2024-06-03T13:42:50Z)

by default qa gets rpms from epel-testing, not epel.
This introduces too many unknwon, uncontrolled chances, especially hen for one reason or another we have several machiines in qa. At the very least we need to be aware. Better yet be ready to disable/enable as proper. Here are instructions ([MM](https://mattermost.web.cern.ch/it-dep/pl/57tx84o9didm5mxjmo1f8xkt6h)):

![image](https://github.com/dmwm/CRABServer/assets/1837785/b40a9bed-b0ca-4c11-b0c9-0482cb109a34)

## Comment (belforte, 2024-06-03T13:45:13Z)

assigning to me to remember to bfing it up for discussion

## Comment (belforte, 2024-06-06T13:50:44Z)

we discussed in the meeting today. Pending a final review with @mapellidario the conclusions are:

- stick to epel production for all our VM’s even in qa
- Let other people test epel-testing
- Lock FTS client version anyhow, like we do for HTCondor and when an updated comes upstream, validate it.

## Comment (mapellidario, 2024-06-06T14:08:14Z)

uh! this was not easy to catch, good job Stefano (and Wa also?)!
I definitely agree with all your decisions

## Comment (aspiringmind-code, 2024-06-17T08:22:21Z)

Fixed by disabling epel-testing in `data/hostgroup/vocmsglidein.yaml` See https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/204

Test passed on crab-dev-tw03 See https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/205
