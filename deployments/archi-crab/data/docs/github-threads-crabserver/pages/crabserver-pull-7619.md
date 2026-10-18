# dmwm/CRABServer pull request #7619: correct accounting of tape locations. Fix #7589

State: closed
Opened: 2023-04-27T17:01:42Z
Closed: 2023-04-28T17:11:58Z
Merged: 2023-04-28T17:11:58Z
URL: https://github.com/dmwm/CRABServer/pull/7619

## Opening post (belforte, 2023-04-27T17:01:42Z)

(no text)

## Comment (cmsdmwmbot, 2023-04-27T17:07:28Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1503/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-27T20:35:04Z)

let's follow up by voice. I do not know what `pop` does here. Change worked in one test, but previous version was working too in that particular case which I used to test !

## Comment (belforte, 2023-04-27T21:07:19Z)

OK. I see what you mean. Yes. It is wrong. THANKS !!
I am not sure popping out the member from the set is good, I'd prefer to leave `tapeLocations` unchanged.
This is ugly but should do:
```python
if 'US' in list(tapeLocations)[0]:
```

## Comment (belforte, 2023-04-27T21:18:32Z)

mayeb this is a bit more clear (thanks StakOverflow) even if still not particularly self-explaining
I guess my problem is lack of experience with set operations. But I guess that all in all `min(aSet)` is not any better than `list{aSet}[0]`. I am open to advice of course.

```python
if len(tapeLocations) == 1:
  tape = min(tapeLocations)
  if 'US' in tape:
    #use only US RSE's
  else
```

## Comment (belforte, 2023-04-27T21:38:46Z)

@mapellidario please review again

## Comment (cmsdmwmbot, 2023-04-27T21:43:35Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1504/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-04-28T17:10:07Z)

If you do not have anything else to add here, I am ok with merging this
