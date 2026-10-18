# dmwm/CRABServer issue #7756: reduce/remove pylint complains

State: open
Opened: 2023-07-13T13:19:03Z
Labels: Priority: Medium, Area: Code Cleanup, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7756

## Opening post (belforte, 2023-07-13T13:19:03Z)

we have so many warnings and errors that risk to overlook real problems (it happened already with undefined variables).

In this issue we collect (examples of) pylint messages which we'd like to eliminate and divide in following categories (from easier to harder):
1. easy to fix even via a script
2. fixable with reasonably safe and simple code changing
3. not obvious how to solve, requires discussion/investigation
4. things we can live with
5. things which we think should be OK so that changes to pylint config should be needed
6. more as needed ?

The plan is then to fix things "one file at a time" whenever we modity it

## Comment (belforte, 2023-07-13T13:38:24Z)

I will kickstart this with "lessons" from DBSDataDiscovery refactoring  #7733 . Everybody can add.

|id| error/warning message | category | fix |
|--|--------------------------------|-------------|-----|
|W1201|  Use lazy % formatting in logging functions  | 2 | use correct format |
| W1514 | Using open without explicitly specifying an encoding  | 1 | add `, encoding='utf-8'` (unless opening a binary file) |
|W0703| Catching too general exception Exception | 2 , 4 | fix when easy, but sometimes better live with it|
|W707| Consider explicitly re-raising using the 'from' keyword  | 1 or 2 | easy fix |
|W0611| Unused import | 1 | remove |
|W0511| TODO | 4 | but should ony be used for things we really expet to do in this PR or soon after |
|C0209| Formatting a regular string which could be a f-string |2| use f-string ! |
| C0301 | Line too long | 2 | in most cases easy and safe to fix |
| C0321| More than one statement on a single line | 2 | split line |
| C0411 | import out of order | 1 | fix !|
| C0415 | Import outside toplevel | 3 | Stefano has no clue. Hints from Dario in https://github.com/dmwm/CRABServer/pull/7789#issuecomment-1660533466 |
| R0914 | Too many local variables | 4 | avoid in new code, but not change old code | 
|  R0912 | Too many branches  |  4 | avoid in new code, but not change old code | 
|  R0915 | Too many statements   |  4 | avoid in new code, but not change old code | 
| R0201 | Method could be a function | 3 | Stefano does not know how to fix. Let it be ? |
| R1702 | Too many nested blocks  | 4 | avoid in new code, but not change old code | 
| R1711| Useless return at end of function or method | 2 | remove it |
| R1720 | Unnecessary "elif" after "raise" | 2 | remove |

## Comment (FrankXenarthra, 2023-08-21T22:00:47Z)

@belforte Does it make sense to add C0103 to the ignored rules? This seems to be a heavily unused one:


   405 C0103
    117 C0301
     35 C0116
     27 W0703
     26 E0401
     12 W1401
     10 R0914
     10 R0912
      7 W0603
      7 W0511
      7 R1711
      7 E0602
      7 C0114
      6 R0915
      6 C0413
      4 R0913
      4 E1101
      4 C0305
      3 W0612
      3 W0402
      3 W0311
      3 R1705
      3 C0321
      2 W0631
      2 W0613
      2 W0201
      2 R0205
      2 E0611
      2 C0412
      2 C0115
      1 W0611
      1 R1722
      1 R0911
      1 R0123
      1 C0410
      1 C0303
      1 C0302
      1 C0121

## Comment (belforte, 2023-08-22T07:30:26Z)

thanks for the tally and the suggestion @FrankXenarthra , but I think we'd rather live with the rules set for the whole DMWM project. There's a lot of old code which predates naming standards, and it may not be worth chasing that, but it is useful to have such checks for new code or the time we happen to put our hands anyhow on some old file, e.g. we could disable it file by file when able to do it consciously.  I will certainly not go fix all of them flatly across the board.

## Comment (FrankXenarthra, 2023-08-23T21:36:01Z)

#7851
