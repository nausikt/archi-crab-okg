# dmwm/CRABServer issue #8986: daily spark job error [PATH_NOT_FOUND] in hdfs, daily rucio's history file was missing.

State: open
Opened: 2025-03-14T11:13:32Z
Labels: Area: MONIT, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8986

## Opening post (nausikt, 2025-03-14T11:13:32Z)

Thanks to well notes & documents from Dario! on how to get started around spark & hdfs:
https://cmscrab.docs.cern.ch/crab-components/crab-monitoring/crab-spark/introduction.html#data-source

P.S. if still have any problems/questions we can ask NIkodemas.

## Details
[PATH_NOT_FOUND] Path does not exist: `hdfs://analytix/project/awg/cms/rucio/2025-03-13/rules_history`.

Command to reproduce and `crab_taskdb.py`, script in issue.
```
spark-submit --master yarn --packages org.apache.spark:spark-avro_2.12:3.5.0 /data/srv/spark/notebooks/crab_taskdb.py
```

Full Error log: 
```
Traceback (most recent call last):  
 File "/data/srv/spark/notebooks/crab_taskdb.py", line 166, in <module>  
   tasks_df = spark.read.format('avro').load(HDFS_CRAB_part).cache()  
 File "/cvmfs/[sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/pyspark.zip/pyspark/sql/readwriter.py](http://sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/pyspark.zip/pyspark/sql/readwriter.py)", line 307, in load  
 File "/cvmfs/[sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py](http://sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py)", line 1322, in __call__  
 File "/cvmfs/[sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py](http://sft.cern.ch/lcg/releases/spark/3.5.0-8c620/x86_64-el9-gcc13-opt/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py)", line 185, in deco  
pyspark.errors.exceptions.captured.AnalysisException: [PATH_NOT_FOUND] Path does not exist: [hdfs://analytix/project/awg/cms/crab/tasks/2025-03-13](hdfs://analytix/project/awg/cms/crab/tasks/2025-03-13).
```
Other surrounded context:
```
 File "/data/srv/spark/workdir/./run.py", line 104, in <module>  
   subprocess.run(cmd, shell=True, timeout=3600, check=True, env=runenv)  
 File "/cvmfs/[sft.cern.ch/lcg/releases/Python/3.9.12-9a1bc/x86_64-el9-gcc13-opt/lib/python3.9/subprocess.py](http://sft.cern.ch/lcg/releases/Python/3.9.12-9a1bc/x86_64-el9-gcc13-opt/lib/python3.9/subprocess.py)", line 528, in run  
   raise CalledProcessError(retcode, process.args,  
subprocess.CalledProcessError: Command 'spark-submit --master yarn --packages org.apache.spark:spark-avro_2.12:3.5.0 /data/srv/spark/notebooks/crab_taskdb.py' returned non-zero exit status 1.
```
