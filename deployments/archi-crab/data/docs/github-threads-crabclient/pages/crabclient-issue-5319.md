# dmwm/CRABClient issue #5319: add instructions to crab-completion.sh

State: closed
Opened: 2024-06-24T07:53:46Z
Closed: 2024-07-14T15:49:44Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5319

## Opening post (belforte, 2024-06-24T07:53:46Z)

see
https://github.com/cms-sw/cmsdist/pull/9261#issuecomment-2184074349

From Shahzad

having a comment like [a] just before the complete -F command in crab-bash-completion.sh will help for future updates

[a]
```text
######################################################
# Please make sure that 'complete` command below meet following rules
# - Starts with: complete\s+-F\s+<crab-function-name>\s+
# - Ends with: \s+crab
#  Otherwise suggest changes in crab-build.file in cms-sw/cmsdist repository
#####################################################
```

## Comment (belforte, 2024-06-24T07:54:54Z)

@mapellidario your bash is better than mine. I assign to you so that you can make sure that this is clear enough and put it in the right place.

Thanks
