# dmwm/CRABServer issue #7595: make it easy to deal with tails

State: closed
Opened: 2023-04-14T08:01:45Z
Closed: 2025-05-06T08:16:28Z
Labels: Type: Enhancement, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7595

## Opening post (belforte, 2023-04-14T08:01:45Z)

this is a general container for various changes that will help users.
List below is work in progress. Updated as of August 2024. RIght before Dario leaves CRAB !

- [x] a command to wrap up current task and capitalize on work done so far and ensure there's info for completing "later"  - done : `crab kill` + `crab recovery` 
- [x] a wrapper to make simple (automatic?) to create and run recovery tasks, including "more data became available" - Done with `crab recovery`
- [x] make sure recovery task can be run also for tasks older than 1 month - We decided not to do/allow this.
- [x] improve automatic retries - Left for the future
- [x] need to add last missing piece to `crab recovery`: recovery tasks submitted with FileSplitting - https://github.com/dmwm/CRABClient/issues/5330

## Comment (belforte, 2025-01-02T10:42:19Z)

will close as soon as client [v3,241218](https://github.com/dmwm/CRABClient/releases/tag/v3.241218) which includes recovery for split-by-file is in production

## Comment (belforte, 2025-05-06T08:16:28Z)

new client is in production since a while. closing :-)
