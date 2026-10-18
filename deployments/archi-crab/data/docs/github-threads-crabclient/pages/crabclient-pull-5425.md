# dmwm/CRABClient pull request #5425: [PEP389] introduce argparse deprecate optparse

State: open
Opened: 2026-03-04T00:22:54Z
URL: https://github.com/dmwm/CRABClient/pull/5425

## Opening post (nausikt, 2026-03-04T00:22:54Z)

Resolve https://github.com/dmwm/CRABClient/issues/5424

The hardest part is preserving the strict `disable_interspersed_args` behaviour and adding back the validating of unknown flags in [CRABOptParser.py](https://github.com/dmwm/CRABClient/pull/5425/changes#diff-7f3c43626918e298fd25bab96b58c98477c511f0d37dffb45064238daa34484c). 
*Thanks to LLM, helping me polish this part meanwhile we both looking at original [optparse.py](https://github.com/python/cpython/blob/dc12d1999b88e84d5a6b8e491be468b73379e54b/Lib/optparse.py#L1395C5-L1445C1)*

So, CRABOptParser in general + submit, createmyproxy subcommands will behave exactly the same.
*See also [the important bit disable_interspersed_args](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.disable_interspersed_args)*

*P.S. Let me exhaustively test first (may write some unit-tests), do we already have test cases covered these behaviors?*
*P.S. Besides that, I think my proposed abstraction/structure is fairly minimal and clean. what do you think?*

## Comment (cmsdmwmbot, 2026-03-04T00:28:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 38 warnings and errors that must be fixed
   * 4 warnings
   * 679 comments to review
 * Pycodestyle check: succeeded
   * 932 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1149/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-04T18:39:17Z)

Hi @nausikt I tried to understand this `disable_interspersed_args` but it requires too much time. I think I have looked at this in the pasta and it may be that the only reason for that is that original developers wanted to have
`crab --debug <command> <other options>`
And I have no idea if anybody is actually using that, other than us in some test scripts.
If all that we need to simplify our life is to move that to be
`crab command --debug --this --that`
I am surely in favor !
