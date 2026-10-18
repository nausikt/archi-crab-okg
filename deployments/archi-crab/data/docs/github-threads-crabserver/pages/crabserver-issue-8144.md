# dmwm/CRABServer issue #8144: avoid fake image build errors

State: closed
Opened: 2024-01-11T16:52:01Z
Closed: 2024-02-12T18:38:05Z
Labels: Area: CI/CD, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8144

## Opening post (belforte, 2024-01-11T16:52:01Z)

sometimes image build after release fails spuriosly because of this check
![image](https://github.com/dmwm/CRABServer/assets/1837785/e142e634-a46a-4377-bc74-906f6370024e)

Sometimes one of those "failure" word simply appear in the log for good reasons, like being
part of a commit
```
+ echo '(DEBUG)   \- PAYLOAD: {"action": "created", "release": {"body": "Bug fix release to solve tape recall failures when using an input block list #8140 \r\n\r\nBrings in a
```
which gets printed to the console because that comment is part of the release notes for https://github.com/dmwm/CRABServer/releases/tag/v3.240111

We can try to remember not to use those "errore/failure" words in the release note, but maybe we should look for a better way to check if build was successful. Maybe we can simply try to trust the exit code of the build script ?

## Comment (belforte, 2024-01-11T17:18:44Z)

sorry for misspell (faulure) in the screenshot above, I was editing the condition in order to build v3.240111
I have now reverted to the original `ERROR|failed|failure|error|Failed`

## Comment (belforte, 2024-02-07T10:27:22Z)

Let's remove the check and see how it goes

## Comment (belforte, 2024-02-12T18:38:05Z)

Done
![image](https://github.com/dmwm/CRABServer/assets/1837785/2adb83fb-5330-460c-91f3-2c57583bbe66)
