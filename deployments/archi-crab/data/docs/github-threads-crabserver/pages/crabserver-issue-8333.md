# dmwm/CRABServer issue #8333: avoid resultAds argument in schedd.submit 

State: closed
Opened: 2024-04-12T10:47:36Z
Closed: 2024-05-31T14:36:54Z
Labels: Status: Done, Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8333

## Opening post (belforte, 2024-04-12T10:47:36Z)

this is now deprecated in HTCondor.
We should change to 
```
 result = schedd.submit()
```
where `result` will be an ` htcondor.SubmitResult` object

Reference: https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#interacting-with-schedulers

![image](https://github.com/dmwm/CRABServer/assets/1837785/b4969e4c-888f-4395-9b60-04cd042d7a4c)

![image](https://github.com/dmwm/CRABServer/assets/1837785/6fcd4b11-0c05-4ced-ac00-f8b026718834)

![image](https://github.com/dmwm/CRABServer/assets/1837785/223387b2-700a-427e-90c4-ddf4a93a5427)

## Comment (belforte, 2024-04-18T20:25:06Z)

This can only work at together with #8336 !!
I had not noticed the (now) highlighted text here:
![image](https://github.com/dmwm/CRABServer/assets/1837785/e0f94051-20b7-4820-bb7f-baef1d68acd7)
