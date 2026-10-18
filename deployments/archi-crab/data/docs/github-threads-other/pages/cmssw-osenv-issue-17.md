# cms-sw/cmssw-osenv issue #17: Unset locales

State: closed
Opened: 2024-08-22T23:07:32Z
Closed: 2024-09-03T13:38:28Z
Labels: pending-assignment
URL: https://github.com/cms-sw/cmssw-osenv/issues/17

## Opening post (lmoureaux, 2024-08-22T23:07:32Z)

I have the following locales inherited from my main machine, since SSH forwards them by default:
```
LANG=fr_BE.UTF-8
LC_ADDRESS=fr_BE.UTF-8
LC_IDENTIFICATION=fr_BE.UTF-8
LC_MEASUREMENT=fr_BE.UTF-8
LC_MONETARY=fr_BE.UTF-8
LC_NAME=fr_BE.UTF-8
LC_NUMERIC=fr_BE.UTF-8
LC_PAPER=fr_BE.UTF-8
LC_TELEPHONE=fr_BE.UTF-8
LC_TIME=fr_BE.UTF-8
```
I want to keep seeing messages in French if possible, so I do not want to unset them.

This is usually not an issue since every possible locale is enabled on a typical interactive node. However, the `cmssw-*` containers have only the following:
```
$ cmssw-cc7 -- locale -a
C
POSIX
en_US.utf8
```

This causes `perl` to complain quite loudly:
```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LC_PAPER = "fr_BE.UTF-8",
        LC_ADDRESS = "fr_BE.UTF-8",
        LC_MONETARY = "fr_BE.UTF-8",
        LC_NUMERIC = "fr_BE.UTF-8",
        LC_TELEPHONE = "fr_BE.UTF-8",
        LC_IDENTIFICATION = "fr_BE.UTF-8",
        LC_MEASUREMENT = "fr_BE.UTF-8",
        LC_TIME = "fr_BE.UTF-8",
        LC_NAME = "fr_BE.UTF-8",
        LANG = "fr_BE.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
```
This is shown in particular for every `scram` call.

Generating all locales like is done for interactive nodes would make the container very large for little gain. Instead, I think the script should reset the locale in the container to the default.

## Comment (cmsbuild, 2024-08-22T23:07:52Z)

cms-bot internal usage<!-- bot cache: {"commits":{},"emoji":{},"signatures":{}} -->

## Comment (cmsbuild, 2024-08-22T23:07:52Z)

A new Issue was created by  @lmoureaux.

@Dr15Jones, @antoniovilela, @makortel, @mandrenguyen, @rappoccio, @sextonkennedy, @smuzaffar can you please review it and eventually sign/assign? Thanks.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-issues.html">here</a>

## Comment (smuzaffar, 2024-09-03T10:45:33Z)

@lmoureaux , I can update the `cmssw-env` to set `LC_ALL="C"` which should avoid these perl warnings
- without setting `LC_ALL`
```
> ./cmssw-el9 -- perl -e 'print "OK\n";'
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
OK
```
- with setting `LC_ALL="C"`
```
> ./cmssw-el9 -- LC_ALL="C" perl -e 'print "OK\n";'
OK
```

## Comment (lmoureaux, 2024-09-03T11:38:23Z)

This works! Thanks for following up :)
