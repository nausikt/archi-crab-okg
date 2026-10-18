# dmwm/CRABServer pull request #7678: avoid belforte's private clone and cernbox

State: closed
Opened: 2023-06-26T18:22:19Z
Closed: 2023-06-26T18:22:38Z
Merged: 2023-06-26T18:22:38Z
URL: https://github.com/dmwm/CRABServer/pull/7678

## Opening post (belforte, 2023-06-26T18:22:19Z)

FYI @mapellidario 
I am now running this in my acrontab. I call it progress.

It fails on `crab-*-tw*` because `/usr/lib64/python3.6/site-packages` there does not have pycurl. 

I fixed the this on `crab-dev-tw01` with  (as root)
```
yum install  python3-deve
yum install libcurl-devel
yum install gcc
pip3 install pycurl
```

but then got in trouble with
```
File "/tmp/belforte/WMCore/src/python/WMCore/Services/pycurl_manager.py", line 338, in request
    curl.perform()
pycurl.error: (35, 'Peer does not recognize and trust the CA that issued your certificate.')
```
which I have seen many times, but have never found a solid recipe to fix, and none of my tricks worked so far. [*]

Current TW container misses `pandas` and a simple `pip install` failed. pff...


[*] in the end it works with my CERN certificate, fails with my INFN/Terena one. The latter works on lxplus, and aslo works with `curl https://cmsweb` from `crab-dev-tw01`.This points to something stale in `/etc/grid-security/certificates` .. oh well. I guess we do not want to solve all world's problems.

Up to you now if you want to setup a crontab with this on crab-...-tw... or rather make it work in the container first.

Grid authentication is always a pain.
Anyhow I also ran ` sudo update-ca-trust` on `crab-dev-tw01`  but can't easily test because currently we have no rules pending.
