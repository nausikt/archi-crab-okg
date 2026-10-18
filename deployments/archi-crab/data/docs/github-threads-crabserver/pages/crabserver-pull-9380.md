# dmwm/CRABServer pull request #9380: cut long stdout also when evicted. Fix #9377

State: closed
Opened: 2026-08-07T13:58:31Z
Closed: 2026-08-11T13:29:29Z
Merged: 2026-08-11T13:29:29Z
URL: https://github.com/dmwm/CRABServer/pull/9380

## Opening post (belforte, 2026-08-07T13:58:31Z)

(no text)

## Comment (belforte, 2026-08-07T13:59:29Z)

I did not test. Do you think test is needed ?

## Comment (cmsdmwmbot, 2026-08-07T14:01:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 56 comments to review
 * Pycodestyle check: succeeded
   * 7 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2878/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-08-10T19:34:32Z)

In my understanding every line is cut to 1K char. Even if output is a single line.
Please double check !
And in case complain to Claude :-)

## Comment (belforte, 2026-08-10T19:37:48Z)

I would not make any assumption on what user logs are.  Anything can happen.

## Comment (nausikt, 2026-08-11T08:03:57Z)

Forgive me, for all poor reviews yesterday. Claude did point out much clearer than what i embarrassingly did.

it mentioned one limitation of (head window) as counter example case [1], which TBH i do not clearly understand this corner cases yet. 

Claude also mentioned that 1000 chars may not hold high signal error mesg, hopefully they're rare cases.   

But Yeah your script did bounded the logs at ~4 MB no matter what the payload does. That was the original goal and It works, and we better not imagine/assume anything about user logs.


[1] The giant line lands inside the head window
head bounds by lines, not bytes. If the file has >4000 newlines and one of the first 1000 lines is enormous, head faithfully pumps that entire line into the pipe and cut throws away all but 1000 bytes of it. Same file size, giant line in two different places:

```
A) giant line at line 1     (INSIDE head window)
   file size          : 209,969,045 bytes
   bytes through head|: 209,765,046 bytes   <-- read+piped to keep 1000
   print_file output  :     203,962 bytes
   wall clock         : 0.756 s

B) giant line at line 2000  (OUTSIDE head window)
   file size          : 209,970,935 bytes
   bytes through head|:      49,890 bytes
   print_file output  :     204,901 bytes
   wall clock         : 0.258 s
```

## Comment (belforte, 2026-08-11T13:29:23Z)

Interesting point. But we cut at 1K max length nevertheless ! If and error message is too long... too bad.
