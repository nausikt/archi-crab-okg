# dmwm/CRABServer issue #7881: CVMFS failed to mount in TW machine

State: closed
Opened: 2023-09-15T11:35:06Z
Closed: 2024-02-07T10:39:02Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7881

## Opening post (novicecpp, 2023-09-15T11:35:06Z)

Sometimes, when we deploy TaskWorker we get this error:
```
docker: Error response from daemon: error while creating mount source path '/cvmfs/cms.cern.ch/SITECONF': mkdir /cvmfs/cms.cern.ch: permission denied. 
```
This error is due to `/cvmfs/cms.cern.ch` disappearing, and it does not automatically remount when needed.
Manually triggering remount (via `cvmfs_config probe`) does not work either.

## Comment (novicecpp, 2023-09-15T11:38:39Z)

Workaround is to force restart manually by:

```
# run as root
cvmfs_config killall
sleep 60 # or wait a bit
cvmfs_config reload
cvmfs_config probe 
```

Dario and I "heard" that autofs is the root cause.

Andrea's suggestion is to just get rid of autofs and manually manage umounts and mounts by

```
# Umount with

cvmfs_config umount

# then mount with

mount -t cvmfs cms.cern.ch /cvmfs/cms.cern.ch
mount -t cvmfs unpacked.cern.ch /cvmfs/unpacked.cern.ch 
```

## Comment (novicecpp, 2023-09-18T11:35:15Z)

Fortunately, there is `mount_option => 'mount'`  in [CERN IT cvmfs's puppet module](https://gitlab.cern.ch/ai/it-puppet-module-cvmfs/-/blob/ba8b79ae36d49d197557d2591e9b406985d577eb/code/manifests/init.pp#L30), which puts mount entries to `/etc/fstab` and it will mount automatically after reboot.

I have applied changes to `crab-dev-tw03` and it works perfectly. See diff: https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/compare/a425fd4461e7aeb556ec502fff80736db3541afb...crabdev_taskworker?from_project_id=4758&straight=false
The changes in bump latest cvmfs to 2.11 (from 2.5) and install fuse3 built.

Note that converting from autofs to mount with fstab needs some manual intervention steps:
- Unlink `/etc/auto.cvmfs`
- Remove `/cvmfs program:/etc/auto.cvmfs` line from /etc/auto.master
- Reboot, make sure there is no autofs entries in  /proc/mounts (`grep autofs /proc/mounts | grep cvmfs` should not return anything).

## Comment (belforte, 2024-02-07T10:39:02Z)

@novicecpp tried but experience is that forcing mount at VM start time leads to more error than current setup.
So we keep it as it and have a recipe for recovering https://github.com/dmwm/CRABServer/issues/7881#issuecomment-1721132428
