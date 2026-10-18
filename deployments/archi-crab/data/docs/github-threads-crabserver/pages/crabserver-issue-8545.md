# dmwm/CRABServer issue #8545: make text select via mouse for copy/paste work in pypi container

State: closed
Opened: 2024-07-05T14:08:41Z
Closed: 2024-08-06T15:15:27Z
Labels: Priority: High, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8545

## Opening post (belforte, 2024-07-05T14:08:41Z)

need to disable visual mouse mode
https://stackoverflow.com/questions/43048243/how-to-disable-mouse-in-vim-window-when-its-enabled-by-set-mouse-a

I tested and it appears to work to add this as `/home/crab3/.vimrc`
```
set mouse=
set ttymouse=
```

## Comment (belforte, 2024-08-06T15:15:27Z)

it is enough to press SHIFT when using the mouse ! Let's not change anything.
