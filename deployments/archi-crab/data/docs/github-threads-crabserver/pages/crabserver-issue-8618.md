# dmwm/CRABServer issue #8618: getTasks() fails to get tasks if tw_name is not initialised

State: closed
Opened: 2024-08-14T08:08:12Z
Closed: 2024-08-30T12:43:49Z
URL: https://github.com/dmwm/CRABServer/issues/8618

## Opening post (aspiringmind-code, 2024-08-14T08:08:12Z)

[See](https://github.com/dmwm/CRABServer/blob/43208f8307874dab3d255415b62aa45c0cd1e32f/src/python/CRABUtils/TaskUtils.py#L10)
The code was initially taken from [here](https://github.com/dmwm/CRABServer/blob/91985873c444711865681a3211f74a72c47730ff/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L190-L207) which works.

Stefano's Diagnosis:
When tw_name column has NULL value, it fails at comparisons with the use of LIKE operator in SQL as the wild character "%".

Fix:
Initialize the tw_name to a default value that is not NULL

References:
[1] https://www.w3schools.com/sql/sql_null_values.asp
[2] https://stackoverflow.com/questions/3924400/like-does-not-accept-null-value
[3] https://stackoverflow.com/a/38765838

## Comment (aspiringmind-code, 2024-08-30T12:43:49Z)

Changed 'any' to 'NotKnownYet' in https://github.com/dmwm/CRABServer/pull/8676/commits/a925986e4a1a8a227c94aa7e898def8b26797741
