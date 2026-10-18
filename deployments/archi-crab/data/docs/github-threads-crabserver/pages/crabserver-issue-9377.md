# dmwm/CRABServer issue #9377: cut job stdout lines length at 1K char (also when job is evicted)

State: closed
Opened: 2026-08-04T17:40:21Z
Closed: 2026-08-11T13:29:31Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9377

## Opening post (belforte, 2026-08-04T17:40:21Z)

As of https://github.com/dmwm/CRABServer/pull/9349 stdout of evicted jobs is returned again, but its size is not limited strongly enough.
Current code only checks line number and grabs first and last lines
https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/scripts/job_wrapper/gWMS-CMSRunAnalysis.sh#L193-L204

But we have just encountered a case where the users calls `cmsDriver` in their script, and that prints out in one line the full list of file names in the PREMIX dataset, 500K file names in that case !!!!

So need to do better:
* check file size, not only N lines. 1MByte looks large enough here (after looking at size of job_out*txt one one AP)
   * this avoids that we get killed by a log with <4K lines, but where some are hugely long
* cut each line at 1K characters (for non-evicted jobs `CMSRunAnalysis.py:logCMSSW()` cuts at 3K char. seems too much to me[1])

[1] 
the limit at 3K char in `logCMSSW()` has been there since ten years https://github.com/dmwm/CRABServer/commit/ff9591d3b3fdc11cfb3f432d1b449ab9d9f39189 but there's no record of the rational for that particular value.

So I will cut at 1K character and introduce the 1MB size limit in there as well.

@nausikt @aspiringmind-code any comment, suggestion ? Am I missing some other pitfall ? Or being too much strict w/o reason  ?

## Comment (belforte, 2026-08-06T15:54:06Z)

note, how to check file size
**python**
```python
if os.path.getsize(file_path) < 1024 * 1024:
    print("File is smaller than 1 MB")
else:
    print("File is 1 MB or larger")
```
**bash**
```bash
if [ $(stat -c %s "$file") -lt $((1024 * 1024)) ]; then
    echo "File is smaller than 1 MB"
else
    echo "File is 1 MB or larger"
fi
```

## Comment (belforte, 2026-08-07T10:09:39Z)

how to limit line length in bash (I am ashamed that myself and Dario did not do this alreaady !!! )
```bash
cat <file> | cut -c 1-1000
head -10 <file> | cut -c 1-1000
tail-10 <file> | cut -c 1-1000
```
