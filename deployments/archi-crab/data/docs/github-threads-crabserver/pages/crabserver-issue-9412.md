# dmwm/CRABServer issue #9412: remove cmsweb-test11

State: closed
Opened: 2026-09-04T09:34:16Z
Closed: 2026-09-04T11:13:13Z
Labels: Type: Documentation, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9412

## Opening post (belforte, 2026-09-04T09:34:16Z)

we do not use it anymore.
- [x] update https://cmscrab.docs.cern.ch/inventory/crab-inventory.html
- [x] remove from our code base/configs
```console
LapSB:CRABServer$ rg -. test11
src/script/task_info.js
877:            case "cmsweb-test11.cern.ch":
901:            case "cmsweb-test11.cern.ch":

.gitlab-ci.yml
26:      - "test11"

src/python/ServerUtilities.py
51:                     'test11': {'restHost': 'cmsweb-test11.cern.ch', 'dbInstance': 'devtwo'},

cicd/gitlab/parseEnv.sh
5:#   in group. Valide env are preprod/test2/test11/test2
19:  REGEX_DEV_TAG='^pypi-(preprod|test2|test11|test12|test1|test14)-.*'

cicd/gitlab/env/test11
1:KUBECONTEXT=cmsweb-test11
3:REST_Instance=test11

src/python/CRABInterface/RESTTask.py
253:           curl -X GET 'https://cmsweb-test11.cern.ch/crabserver/dev/task?subresource=counttasksbyuserandstatus&minutes=100'\
```

## Comment (nausikt, 2026-09-04T10:53:24Z)

Done. i had also removed [crab-secrets/kubernetes/test11/crabserver‎/*](https://gitlab.cern.ch/crab3/crab-secrets/-/commit/94c477e6eb5f5f35b66c01a3e1411466cb78071a)
