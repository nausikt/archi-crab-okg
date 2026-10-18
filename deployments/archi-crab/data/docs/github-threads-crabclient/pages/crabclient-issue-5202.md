# dmwm/CRABClient issue #5202: do not put `.git` directories in sandbox

State: closed
Opened: 2023-07-11T08:18:34Z
Closed: 2023-09-22T09:43:30Z
Labels: enhancement, Done, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5202

## Opening post (belforte, 2023-07-11T08:18:34Z)

see https://cms-talk.web.cern.ch/t/crab-submission-fails-tarball-issues/26625/2

Maybe exclude all hidden files/directories which start with `.` ? 

@smuzaffar  @makortel any advice from framework POV ? Are there hidden files in $CMSSW_BASE which we should be careful to keep ?

## Comment (smuzaffar, 2023-07-19T10:20:30Z)

@belforte , there are few hidden files [a] in latest cmssw release cycle (old release cycles may have more). So I am not sure if you want to drop all of these. `.git` is the one which has large size, so by default you can drop it.  But I would suggest to provide a crab parameter to bundle it if explicitly requested by user.

[a]
```
./Fireworks/Core/macros/.admin
./.clang-tidy
./FWCore/Skeletons/mkTemplates/.clang-format
./.clang-format
./PhysicsTools/HeppyCore/bin/.hidden
./DQM/RPCMonitorClient/test/.startMonitorClient
./DQM/RPCMonitorClient/test/.MuonDQMClient.xml
./DQM/RPCMonitorClient/test/.profile.xml
./DQM/SiPixelMonitorClient/test/js_files/.svgmap.js
./DQM/SiPixelMonitorClient/test/.trackermap.txt
./DQM/SiPixelMonitorClient/test/.WebLib.js
./DQM/SiPixelMonitorClient/test/.profile.xml
./DQM/SiStripMonitorClient/test/.WebTest.xml
./DQM/SiStripMonitorClient/test/.trackermap.txt
./DQM/SiStripMonitorClient/test/.startMonitorClient
./DQM/SiStripMonitorClient/test/.WebLib.js
./DQM/SiStripMonitorClient/test/.profile.xml
./DQM/SiStripMonitorClient/test/.SiStripClient.xml
./DQM/SiStripCommissioningDbClients/data/.OfflineDbClient.cfg
./Validation/GlobalHits/test/.rootrc
./Validation/CaloTowers/test/macros/.rootrc
./Validation/GlobalRecHits/test/.rootrc
./Validation/GlobalDigis/test/.rootrc
./.git
```

## Comment (belforte, 2023-07-19T12:32:43Z)

thanks @smuzaffar . But we have already so many parameters. Let's wait for a sensible use case, I am not sure that issuing git command inside grid jobs make sense.

## Comment (belforte, 2023-09-01T20:29:43Z)

I gave a first look. While CLI `tar` has the nice option `--exclude-vcs`, I do not find such a simple way to exclude files using python `tarfile` class. Need to explore with a [filter](https://docs.python.org/3.10/library/tarfile.html?highlight=tarfile#tarfile.TarFile.add) in `tarfile.add`. It is supported also in python 2.7.

## Comment (belforte, 2023-09-01T20:58:11Z)

this seems to do
```python
 def excludeGit(tarinfo):
        if '.git' in tarinfo.name:
            return None
        return tarinfo
tarfile.add(fullPath, directory, recursive=True, filter=excludeGit)
```
