# dmwm/CRABServer issue #8269: make sure that it is impossible to submit two tasks with same name

State: closed
Opened: 2024-03-06T13:59:58Z
Closed: 2024-03-07T11:06:32Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8269

## Opening post (belforte, 2024-03-06T13:59:58Z)

while testing CI pipeline, @novicecpp found that two tasks could use same test file for stageout, but IIRC that file name has same timestamp as task, so this could only happen if we create two tasks with same name (or something very close)

To be investigate and mitigated as needed.

Hopefully can "downgrade" to "add something to checkwrite test file so that it is unique", if we verify that task name is well protected

## Comment (belforte, 2024-03-06T14:01:48Z)

@novicecpp I tentatively assign to you at least for the part "find out what happens". When we have a clear description with examples we can decide if code changing is on you or me. Let me know in case you disagree

## Comment (novicecpp, 2024-03-06T14:31:00Z)

In the CI, I have this error message when CI submit jobs in parallel (runner concurrrent is set to 4):
```
gfal-copy error: 17 (File exists) - Destination davs://eoscms.cern.ch:443/eos/cms/store/user/tseethon/crab3checkwrite_20240305_132750/crab3checkwrite_20240305_132750.tmp exists and overwrite is not set
```

This happened because we rely on uniqueness of timestamp at the second level, which is not enough. 
Here is how [crab checkwrite](https://github.com/dmwm/CRABClient/blob/f754471bc1511805bdad2ed3972fa15318c92c31/src/python/CRABClient/Commands/checkwrite.py#L89-L91) construct LFN:
```python 
        timestamp = str(time.strftime("%Y%m%d_%H%M%S"))
        self.filename = 'crab3checkwrite_' + timestamp  + '.tmp'
        self.subdir = 'crab3checkwrite_' + timestamp
        lfn = self.lfnPrefix + '/' + self.subdir + '/' + self.filename
```

As per your suggestion in MM,  appending the  `uuid.uuid4()` to `self.filename`  should be enough.

I will open the PR later.

## Comment (novicecpp, 2024-03-07T11:06:32Z)

It just realized what this issue is from the reading header.

The error on the CI is

```
++ crab submit -c ./crabConfiguration.py --proxy=/home/gitlab-runner/builds/1FJbVsxxd/2/tseethon/crabserver.tmp/X509_USER_PROXY
+ output='Will use CRAB configuration file ./crabConfiguration.py
Working area '\''/tmp/crabClientValidation/crab_20240305_132409'\'' already exists 
Please change the requestName in the config file
Log file is /home/gitlab-runner/builds/1FJbVsxxd/2/tseethon/crabserver/test/clientValidationTasks/crab.log'
```

that mean we run crab submit in the same directorty in parallel.

This is clearly user error and need to fix in the CI code.
Still, checkwrite file still not unique when we run in parallel, as described above.

Closing this issue and move "add something to checkwrite test file so that it is unique" to CRABClient.
