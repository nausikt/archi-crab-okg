# dmwm/CRABClient issue #5296: Make sure checkwrite create unique LFN path

State: closed
Opened: 2024-03-07T11:12:14Z
Closed: 2024-03-07T13:36:36Z
URL: https://github.com/dmwm/CRABClient/issues/5296

## Opening post (novicecpp, 2024-03-07T11:12:14Z)

In CI, we run CV/CCV in parallel to reduce the feedback time. 

I usually have this error message when CI submit jobs (Runner run at 4 concurrents):
```
gfal-copy error: 17 (File exists) - Destination davs://eoscms.cern.ch:443/eos/cms/store/user/tseethon/crab3checkwrite_20240305_132750/crab3checkwrite_20240305_132750.tmp exists and overwrite is not set
```

This happened because current code rely on uniqueness of timestamp at the second level, which is not enough. 
Here is how [crab checkwrite](https://github.com/dmwm/CRABClient/blob/f754471bc1511805bdad2ed3972fa15318c92c31/src/python/CRABClient/Commands/checkwrite.py#L89-L91) construct LFN:
```python 
        timestamp = str(time.strftime("%Y%m%d_%H%M%S"))
        self.filename = 'crab3checkwrite_' + timestamp  + '.tmp'
        self.subdir = 'crab3checkwrite_' + timestamp
        lfn = self.lfnPrefix + '/' + self.subdir + '/' + self.filename
```

As per your suggestion in MM,  appending the  `uuid.uuid4()` to `self.filename`  should be enough.

## Comment (belforte, 2024-03-07T12:32:11Z)

Indeed there is no task name available to guarantee uniqueness when we do `crab checkwrite`
