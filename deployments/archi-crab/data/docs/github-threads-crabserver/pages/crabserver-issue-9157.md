# dmwm/CRABServer issue #9157: bug in commit https://github.com/dmwm/CRABServer/commit/9ac340864c34ce29acc0b732bd1410cd0e6de4ff

State: closed
Opened: 2025-08-18T23:51:19Z
Closed: 2025-08-19T10:45:20Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9157

## Opening post (belforte, 2025-08-18T23:51:19Z)

pylint spotted a
```
W0705, line 865: Catching previously caught exception type Exception 
```

in
https://github.com/dmwm/CRABServer/blob/b3518632cf1f4cfcf44ddbc6096a2fd7bdc68322/scripts/CMSRunAnalysis.py#L859-L870

indeed it seems to me that a `try` is missing (plus some indentation).
