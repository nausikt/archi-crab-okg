# dmwm/CRABServer issue #8785: stop trying to renew proxy for <usermame>_CRAB in RenewRemoteProxies

State: closed
Opened: 2024-11-13T16:19:49Z
Closed: 2024-12-13T18:08:57Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8785

## Opening post (belforte, 2024-11-13T16:19:49Z)

```text
2024-11-13 17:13:55,413:INFO:RenewRemoteProxies,182:Retrieving proxy for ('/C=DE/O=GridGermany/OU=Karlsruhe Institute of Technology/OU=SCC/CN=Artur Gottmann', 'cms', 'dcms', '')
2024-11-13 17:13:56,032:ERROR:Proxy,600:Error executing:
 env -i sh -c 'unset X509_USER_CERT X509_USER_KEY && env X509_USER_CERT=/data/certs/robotcert.pem X509_USER_KEY=/data/certs/robotkey.pem myproxy-logon -d -n -s myproxy.cern.ch -o /data/certs/creds/6554e388aa8aaa718ab5fe03340f0bece21ae3c0.36 -l "aakhmets_CRAB" -t 168:00'
2024-11-13 17:13:56,032:ERROR:Proxy,601:Unable to retrieve delegated proxy using login aakhmets_CRAB for user DN /C=DE/O=GridGermany/OU=Karlsruhe Institute of Technology/OU=SCC/CN=Artur Gottmann!
```
