# dmwm/CRABServer issue #7999: cleanup use of encoding for FTS_Transfers.py/RESTFileTransfers.py

State: open
Opened: 2023-11-08T14:57:00Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7999

## Opening post (belforte, 2023-11-08T14:57:00Z)

see https://github.com/dmwm/CRABServer/issues/7864#issuecomment-1798854372

in FTS_Tranfers.py lists should be passed to the REST using `encodeRequest(data, listParams=['list_of_ids', 'list_of_failure_reason', 'list_of_...'])` and validated using `validate_strlist()` on server side removing the need to call `makeList()`.
