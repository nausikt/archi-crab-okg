# dmwm/CRABServer pull request #9334: Add migration accounter to rucio publisher 9331

State: closed
Opened: 2026-06-26T10:47:46Z
Closed: 2026-06-26T14:57:08Z
Merged: 2026-06-26T14:57:07Z
URL: https://github.com/dmwm/CRABServer/pull/9334

## Opening post (belforte, 2026-06-26T10:47:46Z)

(no text)

## Comment (cmsdmwmbot, 2026-06-26T10:52:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2847/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-26T14:57:01Z)

thanks Krittin for you review !

## Comment (nausikt, 2026-06-26T15:03:06Z)

Though, i may prefer explicitly pass `migrationAccounter` instance through function args.

The current implementation seems to implicitly expect outer scope of `publishOneBlockInDBS` to contains instantiated `migrationAccounter`.

`publishOneBlockInDBS` seem to be too dependent on outer-scope and order of function called.

## Comment (belforte, 2026-06-26T19:45:18Z)

Current implementation surely is not very clean. I introduced a class only to share a file name :-(  
Maybe it will help to encapsulate future sqlite3 usage,

For my taste there already too many arguments in various function calls. I tried to do a bit better in the "Rucio" variant, in the hope that it became mainstream and the other was deprecated, but I understimated the effort to move the user community to a different way of handling their output.

So I ended up picking some "path of least resistance" now. I'd say that a good restructuring of the code would be nice, but it seems a bit out of scope at this point.

Thanks for such a careful reading, though.
If you have something simple to suggest, I will be happy to look at it, but do not spend much time on this, all in all it works and other than this stupid migration thing, which is not our fault, I have had no need to touch it since many years :-)
