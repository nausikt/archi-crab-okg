# dmwm/CRABServer issue #8648: bump WMCore to 2.3.6rc1

State: closed
Opened: 2024-08-26T11:09:33Z
Closed: 2024-09-09T08:59:58Z
Labels: Type: Enhancement, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8648

## Opening post (belforte, 2024-08-26T11:09:33Z)

it has the fix for #865

## Comment (belforte, 2024-08-26T11:16:03Z)

@aspiringmind-code I think it is a good chance for you to practice build/release process. I do not expect any bad side effect form bumping up WMCore, but .. one never knows. We currently have 2.3.3.
Please note that out `requirements.txt` files need reviewing. It may be good to add a note in `wmcore_requirements.txt`

## Comment (belforte, 2024-08-26T19:57:42Z)

NOPE. We need another tweak to WMCore as per #8625 and https://github.com/dmwm/WMCore/issues/12075

on HOLD until there's a new WMCore tag to use
(although it may still be a good exercise already !)

## Comment (belforte, 2024-09-03T20:55:21Z)

new tag is there: https://github.com/dmwm/WMCore/releases/tag/2.3.6rc2
and has my latest fix. We are running that code in production TW since Aug 28, so are pretty confident that this will work.

## Comment (belforte, 2024-09-09T08:59:58Z)

WMCore 2.3.6rc2 is now in lastest tag deployed in preprod
https://github.com/dmwm/CRABServer/blob/9199c3a4b1ed1f0724173ac2557f6df198ae8e00/cicd/crabserver_pypi/wmcore_requirements.txt#L6
