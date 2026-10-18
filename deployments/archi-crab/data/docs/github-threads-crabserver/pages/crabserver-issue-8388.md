# dmwm/CRABServer issue #8388: bug in FMD retrieve

State: closed
Opened: 2024-05-09T14:17:35Z
Closed: 2024-05-09T15:20:13Z
Labels: Type: Bug, Status: Done, Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8388

## Opening post (belforte, 2024-05-09T14:17:35Z)

this line
https://github.com/dmwm/CRABServer/blob/20aaf162e334451db4a74d88e790995892fe47be/src/python/CRABInterface/DataFileMetadata.py#L68
is likely broken since ever and surely makes no sense

It should be
```python
 'created': str(row.created), 
```
where `row.created` is an object of type `datetime`

Now it returns instead a `CRABInterface.RESTBaseAPI._FakeLOB object` which makes it impossible to compare different ways of retrieving FMD since it is a pointer to a location in memory.


Clearly this value is never used in python code. It indicates the time the row was inserted in the DB and AFICT it is only used in these SQL queries
https://github.com/dmwm/CRABServer/blob/20aaf162e334451db4a74d88e790995892fe47be/src/python/Databases/FileMetaDataDB/Oracle/FileMetaData/FileMetaData.py#L112-L113
which are activated by an HTTP call with `delete` method
https://github.com/dmwm/CRABServer/blob/20aaf162e334451db4a74d88e790995892fe47be/src/python/CRABInterface/RESTFileMetadata.py#L110-L113

https://github.com/dmwm/CRABServer/blob/20aaf162e334451db4a74d88e790995892fe47be/src/python/CRABInterface/DataFileMetadata.py#L134-L144

used in https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/Recurring/FMDCleaner.py
which we do not run anymore.

All of this is  likely obsolete since we user partitions and partition dropping to cleanup the DB.
