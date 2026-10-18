# dmwm/CRABServer pull request #7121: use dictionary copy when needed. Fix #7120

State: closed
Opened: 2022-03-14T16:36:24Z
Closed: 2022-03-14T17:30:42Z
Merged: 2022-03-14T17:30:42Z
URL: https://github.com/dmwm/CRABServer/pull/7121

## Opening post (belforte, 2022-03-14T16:36:24Z)

(no text)

## Comment (cmsdmwmbot, 2022-03-14T16:43:03Z)

Jenkins results:
 * Python2 Pylint check: succeeded
 * Pycodestyle check: succeeded
 * Python3 compatibility checks: succeeded
   * there are suggested fixes for newer python3 idioms
 
Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1175/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2022-03-14T16:51:50Z)

I think this is a consequence of the py3 migration. In py2, `mydict.keys()` returns a list with a static snapshot of the keys of the dictionary. In python3, `mydict.keys()` is a dictionary view, which changes when the dictionary change.

My trivial approach would be to just replicate the py2 behavior in py3 with 

```diff
-        blocksWithLocation = locationsMap.keys()
+        blocksWithLocation = list(locationsMap.keys())
[...]
-            secondaryBlocksWithLocation = secondaryLocationsMap.keys()
+            secondaryBlocksWithLocation = list(secondaryLocationsMap.keys())
```

However, if the dictionaries are not huge or and we do not repeat this many times, we can afford to copy them every time, as you did.

## Comment (belforte, 2022-03-14T17:03:02Z)

thanks @mapellidario . That explanation makes everything clear to me finally !
But all in all I would stick here with the dictionary copy, it is more clear.

OTOH... should we worry that there may be more places wherre something like this may have introduced a py2/py3 difference which is not immediately evident ?

## Comment (belforte, 2022-03-14T17:30:36Z)

Dario and myself reviewed all other places where a variable is assigned to `dict.keys()`, `dict.values()` or `dict.items()` and found no other places where the dictionary is modified before that values goes out of scope. So we are safe
