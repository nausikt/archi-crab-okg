# dmwm/CRABServer issue #7844: user sandbox - improvements needed for crab recover

State: closed
Opened: 2023-08-19T13:39:05Z
Closed: 2024-05-24T15:42:57Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7844

## Opening post (mapellidario, 2023-08-19T13:39:05Z)

While investigating how we can submit a recovery task, we encountered some limitations in how we manage user sandboxes.

Their management has been designed to be allow the TW to submit a task properly, not to be reused after the task has already been submitted.

#### problem

When submitting a task, if the user sandbox is already present in the object storage, we simply re-use it. In particular, we do not check when it expires. This means that it is possible that when a task is submitted, the user sandbox that it is linked to expires in less than 30d. If we want to recover such a task, it is possible that its user sandbox is no longer in s3 when we execute `crab recover`.

#### solutions

Can we improve the sandbox management so that it is compatible with our current design of `crab recover`, which require the user sandbox to be present in s3?

I think we have a couple of options:

- [x] if we limit ourselves at recovering a task before 30d from its initial submission, then we can simply take the sandbox from the schedd webdir. I have already implemented this fallback and it works fine.
- [ ] otherwise, before we upload the user sandbox, we check if it already exists explicitly. if it is bound to expire soon, than we remove it and upload it again.

Keep in mind the following s3 features (this are design choices, not limitations):

- you can not change an object metadata after it has been uploaded. this helps guarantee consistency.
- if you set an expiry date on a bucket, it uses the upload time to decide when an object is bound to be deleted
- upload time is part of object metadata and it can not be changed!
- Dario does not want to change the bucket lifetime rules just to keep a couple of sandboxes around for a little longer

## Comment (belforte, 2023-08-19T19:15:32Z)

I like
```
 before we upload the user sandbox, we check if it already exists explicitly. if it is bound to expire soon, than we remove it and upload it again.
```
Since it would make things work "as originally intendend". Also could be implemented in the server fully transparenlty to client.
But have no idea how much work it is. Let's keep for "when we have free time" :-)

## Comment (belforte, 2023-08-19T19:30:15Z)

anyhow if it is only a matter of adding a call to `S3.Client.get_object_retention` it may be very easy

## Comment (belforte, 2023-08-21T14:51:12Z)

it is actually a different API
```python
bucket='crabcache_dev'
key='belforte/230804_162428:belforte_crab_20230804_182420/twlog'
rr=s3_client.get_object(Key=key, Bucket=bucket)
expiration=rr['Expiration']
expireDay=exp.split("\"")[1]
print(expireDay)
```
output
```
Tue, 15 Aug 2023 00:00:00 GMT
```
which somehow makes no sense since Aug 15 is passed.
Anyhow file was  created on Aug 4 (like the task) and retention day for that bucket is 10days so ExpirationDay is OK. Maybe S3 is like Rucio and expired objects are not purged immediately.
We can also hardcode that we keep things for 90 days and simply check object creation date

```
bucket='crabcache_dev'
key='belforte/230804_162428:belforte_crab_20230804_182420/twlog'
rr=s3_client.get_object(Key=key, Bucket=bucket)
expiration=rr['Expiration']
expireDay=exp.split("\"")[1]
print(f"expires      : {expireDay}")
print(f"last Modified: {rr['LastModified']}")

expires      : Tue, 15 Aug 2023 00:00:00 GMT
last Modified: 2023-08-04 16:24:55+00:00

```

## Comment (belforte, 2024-05-23T10:58:53Z)

Let's simply change retention time to 3 months !

## Comment (mapellidario, 2024-05-24T15:42:57Z)

I migrated the document by Prajesh to our mkdocs [1], added a short section on how to use the `aws` cli that feels more immediate to use than the boto3 python api, then extended the lifecycle to 3 months on `crabcache_prod` bucket [2].

I will close this issue, in the future we can come back to this with better ideas if it is not enough.

[1] https://cmscrab.docs.cern.ch/technical/crab-cache/how-tos.html

[2] 

```plaintext
> aws --endpoint-url=https://s3.cern.ch --profile crab-2024 s3api get-bucket-lifecycle-configuration --bucket crabcache_prod
{
    "Rules": [
        {
            "Expiration": {
                "Days": 93
            },
            "ID": "4w57pf3esaqfbeqzz2dhgm5t7ea155qgxsq4tv5rfwck08zk",
            "Prefix": "",
            "Status": "Enabled"
        }
    ]
}
```
