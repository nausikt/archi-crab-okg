# dmwm/CRABServer issue #8590: (reminder) crabtwfilebeat's latest image get overriden by hotpatch version

State: closed
Opened: 2024-08-06T18:23:08Z
Closed: 2024-08-23T10:49:01Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8590

## Opening post (novicecpp, 2024-08-06T18:23:08Z)

When we build from older commits like hot-patch, images like `crabtwfilebeat` also build. However, because we use the static tag (e.g., `crabtwfilebeat:v3.latest`), the hot-patch pipeline will override the latest image on the registry which which has a newer version.

I do not have better idea how to avoid this. Maybe this is just reminder.

## Comment (belforte, 2024-08-06T20:05:58Z)

I am not sure I understand this. @aspiringmind-code do you ?

## Comment (belforte, 2024-08-06T22:44:31Z)

Do you mean that it just happened something like this ?
-  Let's have tag V1 and deploy it.
-  Then we create V2 and deploy.
-  V2 has a bug, we roll back TW to V1
-  But that dos not change the crabtwfilebeat which stays at V2
    -  operator (Stefano) mistake ?
-  Then you deployed V1.patch and that rolls back crabtwfilebeat to V1

In addition there's the matter of which crabtwfilebeat tag is called `latest` in registry.cern.ch

## Comment (novicecpp, 2024-08-07T07:21:25Z)

Yes. I tried to write this last night but I was too tired. Thanks.

Expanding bullet 4 and 5 a bit:
- But that dos not change the crabtwfilebeat which stays at V2
    - Because we use static tag `v3.latest`
    - **Note**: I used `runContainer.sh` script, did not even thing ot crabtwfilebeat ! No matter which tag we use, I left it unchanged
- You create V1.patch which build crabtwfilebeat V1 again and upload it as `v3.latest`.

## Comment (belforte, 2024-08-07T10:39:35Z)

I think that the disconnect is that when we deploy via pipeline we have a procedure to deploy same tag for each container, but then wanted to roll back only one. 
The fact that for `crabtwfilebeat` we always use latest build instead of a named tag, may not be that relevant since it changes rarely. But if could be sorted out as well.
I agree to take this as a reminder only for the time being.
We need more experience with the new system before looking at changing it.

## Comment (mapellidario, 2024-08-07T15:13:24Z)

>  Maybe this is just reminder.

yes! the code in `crabtwfilebeat` should not change much, the most important part is its configuration that comes from puppet. i do not see this as a problem.

Moreover, we are doing the same for the [monit](https://github.com/dmwm/CRABServer/blob/91c832b6a508e580ed7de0d27cc41442a7ebfcb2/.gitlab-ci.yml#L310) container (tag with "latest" at every release) so i would suggest to change the title and issue message to improve our reminder, but again, i do not think that this is a problem :)

## Comment (novicecpp, 2024-08-23T10:49:01Z)

In conclusion, this is just reminder.
Dario is kind to make it able to change version through hiera https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/e0f5f9eca1c2a508e1b3748fb316fe812baca045/code/manifests/crabtaskworker/generatemonit.pp#L13
