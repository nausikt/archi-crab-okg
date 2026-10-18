# dmwm/CRABServer issue #8441: use voms-clients-java in TW VM's

State: closed
Opened: 2024-05-29T08:56:58Z
Closed: 2024-05-29T13:15:54Z
URL: https://github.com/dmwm/CRABServer/issues/8441

## Opening post (belforte, 2024-05-29T08:56:58Z)

for consistency with lxplus*, schedulers and pipy container (ref #8438 ) we should use the Java client also on the host TW VM's. i.e. remove the lines in the hiera (`data/fqdns/crab*tw*.yaml`) which force `voms-clients-cpp`.
Removing all references to `voms` in there will do !

E.g. this is already the case for `crab-dev-tw04`

## Comment (belforte, 2024-05-29T09:30:59Z)

hmm... prod and preprod are already fine. It is only `dev-tw*` which have the old setting. I guess Wa assumed that everyone was going to take care of this machine.
So I am doing it for everybody

## Comment (belforte, 2024-05-29T13:15:54Z)

Done
