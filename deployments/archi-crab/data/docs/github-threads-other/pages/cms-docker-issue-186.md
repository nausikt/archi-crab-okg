# cms-sw/cms-docker issue #186: Perl issue in el8 container

State: closed
Opened: 2022-05-26T00:16:53Z
Closed: 2022-08-04T20:09:41Z
Labels: pending-assignment
URL: https://github.com/cms-sw/cms-docker/issues/186

## Opening post (kpedro88, 2022-05-26T00:16:53Z)

When I run these commands:
```bash
cmssw-el8
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
```

I get the following warning:
```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
```

This does not happen in e.g. the cc7 image, so something is probably missing from the el8 image.

## Comment (cmsbuild, 2022-05-26T00:17:10Z)

A new Issue was created by  @kpedro88 Kevin Pedro.

@Dr15Jones, @perrotta, @dpiparo, @makortel, @smuzaffar, @qliphy can you please review it and eventually sign/assign? Thanks.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-issues.html">here</a>

## Comment (kpedro88, 2022-08-04T19:57:09Z)

It looks like this is fixed now. @smuzaffar can you point out which commit fixed it?

## Comment (smuzaffar, 2022-08-04T20:08:57Z)

@kpedro88 , this was fixed buy installing `glibc-langpack-en` package ( https://github.com/cms-sw/cms-docker/commit/a2a6ca43d91bca7227a46b88e1b5096c97391069 )
