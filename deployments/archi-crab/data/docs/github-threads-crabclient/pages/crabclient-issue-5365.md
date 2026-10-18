# dmwm/CRABClient issue #5365: add list of OK/fail files to crab report output

State: closed
Opened: 2024-12-16T17:05:37Z
Closed: 2024-12-17T17:19:58Z
Labels: enhancement, Support
URL: https://github.com/dmwm/CRABClient/issues/5365

## Opening post (belforte, 2024-12-16T17:05:37Z)

like done for lumis, it should write 3 files. All containing a dictionary  jobId--> listOfFiles
 ```python
{"JobId1":["file1", "file2"], "jobId2":["file3",...], ... "JobIdN":["fileX",.."fileZ"]}
```

* filesToProcess.json = all files to be processed by this task 
 * processedFiles.json = files in jobs which succeeded
* failedFiles.json = files in jobs which failed, a dictionary

In general `pocessedFiles + faildFiles != filesToProcss` since some jobs may not have run yet !
