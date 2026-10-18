# dmwm/CRABServer issue #9057: remove code referring to old dasboard

State: open
Opened: 2025-04-24T16:33:43Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9057

## Opening post (belforte, 2025-04-24T16:33:43Z)

we still code in PreJob and PostJob which prepares dictionaries for old dashboard and never sends them (of course):

there are all files which contain `dashboard` string.  

- [ ] scripts/AdjustSites.py
- [ ] src/html/index.html
- [ ] scripts/Monitor/dashbgen.sh
- [ ] scripts/task_process/FTS_Transfers.py
- [ ] scripts/Monitor/dashboard-template2.tpl
- [ ] scripts/Utils/run-postjob.sh
- [ ] src/python/ServerUtilities.py
- [ ] src/script/task_info.js
- [ ] src/css/bootstrap.min.css
- [ ] src/python/TaskWorker/Actions/PostJob.py
- [ ] src/python/TaskWorker/Actions/PreJob.py
- [ ] src/script/Deployment/TaskWorker/TaskWorkerConfig.py
- [ ] src/python/TaskWorker/Actions/DagmanCreator.py
