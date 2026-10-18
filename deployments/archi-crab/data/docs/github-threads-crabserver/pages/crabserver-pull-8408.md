# dmwm/CRABServer pull request #8408: Fix typos in output strings

State: closed
Opened: 2024-05-15T20:42:44Z
Closed: 2024-05-15T21:33:33Z
Merged: 2024-05-15T21:33:33Z
URL: https://github.com/dmwm/CRABServer/pull/8408

## Opening post (oljemark, 2024-05-15T20:42:44Z)

Hello. I saw some typos in the exception and printing statements (that did not seem to be parsed elsewhere as such misspellings), which I fixed. I also noticed the misspelled JSON parameter with 3 c's here: https://github.com/dmwm/CRABServer/blob/master/src/python/CRABInterface/RESTWorkerWorkflow.py#L160 
Is that intentional to not hit the exception below, or just a typo not tested with  enough malformed older REST inputs? https://github.com/dmwm/CRABServer/blob/master/src/python/CRABInterface/RESTUserWorkflow.py#L433

## Comment (cmsdmwmbot, 2024-05-15T20:43:01Z)

Can one of the admins verify this patch?

## Comment (belforte, 2024-05-15T21:05:31Z)

thanks @oljemark for such a careful proofing !
As to the misspelled `acccelerator` with 3c's, I can't really say since all in all that was to protect us in a transient situation which is long gone. Somehow it worked. Let's no try to do too much archeology, but we should cleanup the code.

## Comment (belforte, 2024-05-15T21:06:59Z)

please test this

## Comment (belforte, 2024-05-15T21:12:24Z)

test this please

## Comment (belforte, 2024-05-15T21:33:11Z)

I can't get Jenkins to run pylint.. never mind
