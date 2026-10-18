# dmwm/CRABServer issue #8942: script_exe is not available via crab server UI any more

State: closed
Opened: 2025-02-24T11:39:20Z
Closed: 2025-03-03T17:42:18Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8942

## Opening post (belforte, 2025-02-24T11:39:20Z)

after latest changes to TaskWorker the `debug` directory in the WEB_DIR does not have
the `scritp_exe` file anymore, which is still present in the `debug_files.tar.gz` tarball, but outside the `debug` directory
![Image](https://github.com/user-attachments/assets/38055979-efe3-4c49-a62a-157d9676573d)

```console
belforte@vocms0120/250223_201452:schenara_crab_NanoPost1> pwd
/home/grid/schenara/250223_201452:schenara_crab_NanoPost1
belforte@vocms0120/250223_201452:schenara_crab_NanoPost1> ls debug/
crabConfig.py  originalPSet.py
belforte@vocms0120/250223_201452:schenara_crab_NanoPost1> tar tf debug_files.tar.gz 
debug/originalPSet.py
debug/crabConfig.py
crab_script.sh
belforte@vocms0120/250223_201452:schenara_crab_NanoPost1> 
```

## Comment (belforte, 2025-02-27T08:58:31Z)

this should be merged and solved together with https://github.com/dmwm/CRABServer/issues/8719

## Comment (belforte, 2025-03-03T17:14:46Z)

it is not a Server-side issue.
CRAB Client prepares `debugFiles.tgz` which has the content
```text
debug/originalPSet.py
debug/crabConfig.py
simple.sh
```
i.e. puts the script outside the `debug` directory.


`crab preparelocal` and JobWrapper find all they need in the sandbox. That  `debugFiles.tgz`  is "only for debugging", so best solution looks to keep server as is (see https://github.com/dmwm/CRABServer/issues/8719#issuecomment-2695045083 )
and change client to put everything in `debug` directory. This will also be backward compatible. While removing `debug` directory from the tar would require changes in AdjustSites.py

## Comment (belforte, 2025-03-03T17:42:18Z)

moved to Client: https://github.com/dmwm/CRABClient/issues/5376
