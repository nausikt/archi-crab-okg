# dmwm/CRABServer issue #9111: ASO/Rucio is not safe against multiple simultaneous tasks

State: open
Opened: 2025-06-12T10:27:43Z
Labels: Type: Bug, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/9111

## Opening post (belforte, 2025-06-12T10:27:43Z)

Current code assumes that this instance of ASO/Rucio is the only one writing in a given Rucio publish container at any given time, i.e. that it has full control.
But it is possible (as I encountered in #9094 ) that two tasks run with same Pulication tag (i.e. same targed DBS-datsaset/Rucio-Publish-container) in which case we end up with files from different tasks in same DBS-block/Rucio-dataset.

This confuses other code (Publisher e.g.), developers and users since when using ASO/FTS we are consistent with the rule
"multiple tasks can publish in same DBS dataset, each tasks with a separate (set of) block(s)"

Some redesigning and refactoring of ASO/Rucio code is needed, and of its bookkeeping.

Which is also a good time to write down more description of how it works since https://cmscrab.docs.cern.ch/crab-design/crab-rucio-aso.html#rucio-dataset was not detailed/clear enough to catch this.

## Comment (belforte, 2025-06-12T10:30:36Z)

@aspiringmind-code I am temporarely assign to both of us. Once more urgent work is over we can review together and decide how to proceed.

## Comment (belforte, 2025-11-12T10:27:25Z)

FYI @aspiringmind-code

## Comment (belforte, 2026-04-01T15:00:34Z)

Since we do not want to really encourage "switch to Rucio" yet. And use case will be rare. I am reducing priority.
