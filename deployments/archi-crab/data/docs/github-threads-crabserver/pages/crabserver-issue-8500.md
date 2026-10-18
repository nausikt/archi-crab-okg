# dmwm/CRABServer issue #8500: add a "pickScheduler" test to CCV

State: closed
Opened: 2024-06-14T21:08:45Z
Closed: 2024-06-14T21:14:10Z
Labels: Priority: TOP, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8500

## Opening post (belforte, 2024-06-14T21:08:45Z)

currently all Jenkins tests force selection of scheduler vocms059.
So a bug in the code which picks one from the pool can go un-noticed 
e.g. https://github.com/dmwm/CRABServer/pull/8495/commits/fd6a2e1af86c76f7ad2689dd4cdd4d86415ef98d

## Comment (belforte, 2024-06-14T21:14:10Z)

no need. CCV does not impose scheduler. I must have got confused when looking at why I had not spotted that error earlier.
