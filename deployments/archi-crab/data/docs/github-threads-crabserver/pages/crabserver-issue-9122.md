# dmwm/CRABServer issue #9122: Fix incorrect adding site whitelist to userInputFiles.

State: closed
Opened: 2025-07-08T09:31:11Z
Closed: 2025-07-08T10:48:44Z
URL: https://github.com/dmwm/CRABServer/issues/9122

## Opening post (nausikt, 2025-07-08T09:31:11Z)

Sorry for my poor review and reckless merge of add site whitelist to userInputFiles on fix #9120 
```
config.section_('Site')
config.Site.userInputFiles = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
config.section_('Debug')
config.Debug.scheddName = "crab3@vocms059.cern.ch"
++ crab submit -c ./userInputFiles.py --proxy=/home/gitlab-runner/shell/builds/t3_ZsMk1N/0/crab3/CRABServer/X509_USER_PROXY_copy
+ output='Will use CRAB configuration file ./userInputFiles.py
Invalid CRAB configuration: Parameter Site.userInputFiles is not known.
```

Seems like we set white list in the wrong place `Site.userInputFiles = ['T2_CH_CERN']`, it has to endup `Site.whitelist`, let me fix this.

## Comment (belforte, 2025-07-08T09:57:05Z)

my bad. Thanks for quick fix.
