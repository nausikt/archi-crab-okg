# dmwm/CRABClient issue #5325: crab report fails to produce failedLumis.json

State: closed
Opened: 2024-07-12T14:58:20Z
Closed: 2024-07-15T07:57:06Z
Labels: bug
URL: https://github.com/dmwm/CRABClient/issues/5325

## Opening post (mapellidario, 2024-07-12T14:58:20Z)

A user reported that crab report does not produce any `failedLumis.json` [1], which should be produced when running `crab report --recovery failed`.

I could reproduce the problem and it is caused by this line where `jobid` and `status` are swapped

https://github.com/dmwm/CRABClient/blob/2a177d00a3a371d866f4cccb7e64b9a6b295e7ee/src/python/CRABClient/Commands/report.py#L190

with respect to other intances

https://github.com/dmwm/CRABClient/blob/2a177d00a3a371d866f4cccb7e64b9a6b295e7ee/src/python/CRABClient/Commands/report.py#L308

The content of `reportData['jobList']` is [2]

Comparing a job id string such as `'2-953'` with the string `failed` means that we never enter the code below this if:

https://github.com/dmwm/CRABClient/blob/2a177d00a3a371d866f4cccb7e64b9a6b295e7ee/src/python/CRABClient/Commands/report.py#L191

a PR to fix this bug is on its way...

---

[1] https://cms-talk.web.cern.ch/t/command-crab-report-not-generate-filed-files/43487/5

[2]

<details>

```plaintext
[...]
('finished', '3-383'), ('failed', '3-388'), ('finished', '3-389'), ('finished', '3-394'),
('finished', '3-379'), ('failed', '3-382'), ('failed', '3-390'), ('failed', '3-391'),
 ('finished', '3-392'), ('finished', '3-393'), ('finished', '3-34'), ('failed', '3-80'),
 ('failed', '3-134'), ('failed', '3-190'), ('failed', '3-246'), ('failed', '3-303'), ('failed', '3-354')
]
```

</details>

## Comment (belforte, 2024-07-12T21:49:46Z)

Bravo Dario

## Comment (belforte, 2024-07-15T07:57:18Z)

Dario, I do not find where `failedLumis.json` is created. Can you tell me ?

## Comment (mapellidario, 2024-07-15T09:28:16Z)

you need to use the `--recovery failed` option and apply this patch. If you do not apply this patch, then the bug that this PR fixes prevent the creation of the `failedLumis.json` file
