# dmwm/CRABServer issue #7713: Run CheckTapeRecall.py on a TW machine

State: closed
Opened: 2023-07-03T14:08:37Z
Closed: 2024-02-07T10:48:22Z
Labels: Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7713

## Opening post (mapellidario, 2023-07-03T14:08:37Z)

Currently, we run the script CheckTapeRecall.py from a acron job owned by Stefano. We would like to run it in a centralized place instead, for example in a `crab-prod-tw*` machine.

In order to achieve this, we would need:

- [ ] write to eos with the `crab3` unix user of one of our VMs
    - This is worked a couple of weeks ago, but it is currently [broken](https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3516468)
- [ ] an environment where to run the script from
    - one option is to convert the script to a recurring action
    - [ ] otherwise, we can execute it in a crabtaskworker docker container. I would rather go this way.
        - one option would be to create a new "runContainer.sh" script.
        - [ ] install pandas inside crabtaskworker environment. This will likely require to create a new `py3-pandas.spec` in https://github.com/cms-sw/cmsdist/tree/comp_gcc630
        - [ ] rucio requires X509_USER_KEY, X509_USER_CERT, RUCIO_ACCOUNT env variables . We will need to make sure that we properly set these.

I managed to run the script on crab-dev-tw02 [1], with some small modifications to what we currently have at the moment.

---

[1]

change the script not to use the proxy, but to use the service(cert|key).pem, as in [2], then

```bash
# open a TW container
source  /data/srv/TaskManager/env.sh

# install pandas, this will be done properly next time
# from here: https://www.redhat.com/sysadmin/install-python-pip-linux
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
python3 -m pip install pandas

# these env vars will be included in the bash script that start CheckTapeRecall.py
cd /data/repos/CRABServer/script/Utils
export X509_USER_KEY=/data/certs/servicekey.pem
export X509_USER_CERT=/data/certs/servicecert.pem
export RUCIO_ACCOUNT=crab_server
python3 CheckTapeRecall.py

``` 

The result that I obtained is here: https://dmapelli.web.cern.ch/crab/20230703-checktaperecall/RecallRules.html

[2]

```diff
[crab3@crab-dev-tw02 Utils]$ git diff
diff --git a/scripts/Utils/CheckTapeRecall.py b/scripts/Utils/CheckTapeRecall.py
index 6276384..2738433 100644
--- a/scripts/Utils/CheckTapeRecall.py
+++ b/scripts/Utils/CheckTapeRecall.py
@@ -252,9 +252,9 @@ def ensureEnvironment():
     # make sure Rucio client is initialized, this also ensures X509 proxy
     rucio = Client()

-    proxy = os.environ['X509_USER_PROXY']
-    crab = CRABRest(hostname='cmsweb.cern.ch', localcert=proxy,
-                    localkey=proxy, userAgent='CheckTapeRecall')
+    # proxy = os.environ['X509_USER_PROXY']
+    crab = CRABRest(hostname='cmsweb.cern.ch', localcert="/data/certs/servicecert.pem",
+                    localkey="/data/certs/servicekey.pem", userAgent='CheckTapeRecall')
     crab.setDbInstance('prod')
```

## Comment (belforte, 2024-02-07T10:48:22Z)

now in #6493
