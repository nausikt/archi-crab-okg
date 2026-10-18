# dmwm/CRABServer issue #8521: checktaperecall - sometimes fails without clear cause

State: open
Opened: 2024-06-20T09:45:05Z
Labels: Type: Bug, Type: Question, Priority: Medium, Status: On Hold, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/8521

## Opening post (mapellidario, 2024-06-20T09:45:05Z)

Yesterday for a few hours the monitoring script that checks tape recalls failed multiple times [1]. It started working again without any human intervention.

Every time a monitorin script fails, the stdout is saved in a file  [2].

Yesterday, the script failed at the line https://github.com/dmwm/CRABServer/blob/bfdeedbebd1e34688eca0e88991a080debd83fb4/scripts/Utils/CheckTapeRecall.py#L194 

likely because `x.tasks[-1]` was empty, see [3].

I have not checked what the cause could have been, maybe we can improve the script so that is it prints a better message.

---

[1]

![image](https://github.com/dmwm/CRABServer/assets/16376695/04f33e96-a6d7-4841-a11a-4d210de5db52)

[2]

```plaintext
[crab3@crab-prod-tw02 ~]$ ls -lrt /tmp/monit-*
-rw-r--r--. 1 crab3 zh 1477 Jun 19 15:14 /tmp/monit-3d82a206-79f8-4b56-84aa-f970310a86dc.txt
-rw-r--r--. 1 crab3 zh 1477 Jun 19 16:14 /tmp/monit-fc1d478f-3440-487c-b662-e0644173976e.txt
-rw-r--r--. 1 crab3 zh 1477 Jun 19 17:14 /tmp/monit-cd0689a5-0c7c-47c1-89b2-4fead8783592.txt
-rw-r--r--. 1 crab3 zh 1477 Jun 19 18:14 /tmp/monit-506d1009-c717-45a1-9d7e-33c4dece80b3.txt
-rw-r--r--. 1 crab3 zh 1477 Jun 19 19:14 /tmp/monit-070557ac-2eaf-417a-93b5-1214956f2a51.txt
```

[3]

<details><summary>cat /tmp/monit-070557ac-2eaf-417a-93b5-1214956f2a51.txt</summary>

```plaintext
[crab3@crab-prod-tw02 ~]$ cat /tmp/monit-070557ac-2eaf-417a-93b5-1214956f2a51.txt
ln: failed to create symbolic link '/data/srv/monit/logs/logs': File exists
281 rules exist for account: crab_tape_recall
state
OK             255
REPLICATING      3
STUCK           23
dtype: int64
finding tape source for all pending rules (takes some time...)
Add (DBS) dataset name ...
... and size
Done!
find tasks using these rules
Done!
Traceback (most recent call last):
  File "/data/srv/monit/CheckTapeRecall.py", line 440, in <module>
    main()
  File "/data/srv/monit/CheckTapeRecall.py", line 114, in main
    rulesJson = createRulesJson(pendingCompact)
  File "/data/srv/monit/CheckTapeRecall.py", line 194, in createRulesJson
    df['task0'] = df.apply(lambda x: x.tasks[-1], axis=1)
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 9423, in apply
    return op.apply().__finalize__(self, method="apply")
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 678, in apply
    return self.apply_standard()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 798, in apply_standard
    results, res_index = self.apply_series_generator()
  File "/home/crab3/.local/lib/python3.8/site-packages/pandas/core/apply.py", line 814, in apply_series_generator
    results[i] = self.f(v)
  File "/data/srv/monit/CheckTapeRecall.py", line 194, in <lambda>
    df['task0'] = df.apply(lambda x: x.tasks[-1], axis=1)
IndexError: list index out of range
```

</details>

## Comment (belforte, 2024-06-20T09:57:06Z)

thanks Dario. I do not think it is worth to invest time in making the script rock solid. It will be enough to capture the "how to debug" info in the documentation. I was worrying that it could be due to the new container. But a failure like this will be easy to debug if it happens again. I'd rather have it failing badly when `tasks` is empty and figure out why it was

## Comment (mapellidario, 2024-06-20T10:00:42Z)

>  It will be enough to capture the "how to debug" info in the documentation

it's already there :) [1]

No, it does not seem to be caused by the new container, that I have not deployed to crab-prod-tw02 yet.

So, shall we keep this issue open or do you want to close it and open a new one if and when it fails again?

---

[1] https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-crontabs.html#how-to-debug

## Comment (belforte, 2024-06-20T10:09:24Z)

hmm.. I did not get the mail. But I can't review doc in detail now. Let's leave this open for a while. IN case it happens again and we can find details.
I am putting on hold,  until we can reproduce it :-)

## Comment (mapellidario, 2024-06-20T10:11:31Z)

> hmm.. I did not get the mail.

yeah, that's weird as well, i have no idea why
