# dmwm/CRABServer issue #7511: remove transient code related to gridftp-webdav transition

State: open
Opened: 2023-01-27T14:24:51Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7511

## Opening post (belforte, 2023-01-27T14:24:51Z)

this can go away now:
https://github.com/dmwm/CRABServer/pull/6810

## Comment (belforte, 2023-01-27T14:27:07Z)

Dario, I assigned to you since in a way cmscp.py is part of the wrapper. Not as punishment for having noticed the otherwise very hard to spot
```
Lookup of /cvmfs/cms.cern.ch/SITECONF/T1_DE_KIT/KIT-T3-GPU/storage.json failed
Fall back to /cvmfs/cms.cern.ch/SITECONF/T1_DE_KIT/KIT-T3-GPU/storage.json
Failed to check protocol compatibility for stageout:
[Errno 2] No such file or directory: '/cvmfs/cms.cern.ch/SITECONF/T1_DE_KIT/KIT-T3-GPU/storage.json'
Will stick with above stageout policy 
```

## Comment (belforte, 2023-01-27T14:31:45Z)

of course it will be good to check with SiteSupport that indeed every site has a webdav endpoint by now.

## Comment (mapellidario, 2023-01-27T14:47:19Z)

I see, thank you very much Stefano for finding the offending line! :)
