# dmwm/CRABServer issue #8402: Reviewing how we bind mount the TW container

State: closed
Opened: 2024-05-14T10:26:40Z
Closed: 2024-05-17T08:41:36Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8402

## Opening post (novicecpp, 2024-05-14T10:26:40Z)

Before deploying the new [runContainer.sh](https://github.com/dmwm/CRABServer/blob/c69980662cbd4fa76e3801b6f3085856032743d6/src/script/Container/runContainer.sh) version, which requires a configuration change because of a path change inside the container, I would like to review all of the binding mounts we use for the TW container.

Stefano pointed out [in this PR comment](https://github.com/dmwm/CRABServer/pull/8368#issuecomment-2098503494) that there are too many bind mounts appearing on runContainer.sh script. Here is the the list of bind mount when we deploy the Publisher_schedd:


The first half, the host's working directory:
- `-v /data/container/Publisher_schedd/cfg:/data/srv/Publisher/cfg`
- `-v /data/container/Publisher_schedd/logs:/data/srv/Publisher/logs` 
- `-v /data/container/Publisher_schedd/PublisherFiles:/data/srv/Publisher/PublisherFiles`
- `-v /data/srv/tmp/:/data/srv/tmp/`
 
As Stefano suggested, mounting the `/data/container/${SERVICE}` as a single path will be easier to manage, and the application already supports custom paths via service configuration files.

The second half, the host environments:
- `-v /data/certs/:/data/certs/`
- `-v /data/container/:/data/hostdisk/`
- `-v /cvmfs:/cvmfs:shared`
- `-v /etc/grid-security/:/etc/grid-security/`
- `-v /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem:/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`
- `-v /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem:/etc/pki/tls/certs/ca-bundle.crt'`

This part is clear enough why we need it. However, the hostdisk (`-v /data/container/:/data/hostdisk/`) only for provide Filebeat configuration to Filebeat process inside container. Filebeat is not is not bundle in the new PyPI image and there is no plan to bundle it in the future.

EDITED: switch `-v /data/certs/:/data/certs/` to second half.

## Comment (novicecpp, 2024-05-14T10:39:16Z)

My proposal:

- Mount `/data/container/${SERVICE}` to `/data/container/${SERVICE}/hostdisk`
- Change configuration to `/data/container/${SERVICE}/hostdisk`, including cfg, logs, extra dir like `PublisherFiles`, tmp. 
- Remove hostdisk, move Filebeat to Puppet.

The final bind mount should be:
- `-v /data/container/Publisher_schedd:/data/srv/Publisher/hostdisk`
- `-v /data/certs/:/data/certs/`
- `-v /cvmfs:/cvmfs:shared`
- `-v /etc/grid-security/:/etc/grid-security/`
- `-v /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem:/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`
- `-v /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem:/etc/pki/tls/certs/ca-bundle.crt'`

@belforte What do you think?

## Comment (belforte, 2024-05-14T15:43:28Z)

I like it. Let's add a `/data/container/${SERVICE}/scratch` directory with write-all to facilitate file sharing to/from the container. I have been using hostidsk/tmp for that, creating it by hand.

What do you think about removing the last entry and replace it with a symlink in the container like it is in the host ? It is a bit wierd to mount twice the same file. I am not sure which way is "less obscure".  Maybe as simple as "Stefano does not understand PKI !!"

## Comment (novicecpp, 2024-05-14T16:08:39Z)

> Stefano does not understand PKI !!

It is understandable. I do not know it myself. Different distribution/library/application use different path.
But keep both mount is better IMO. Mount same file for 2 different path cause no harm in future, and keep this responsible for "ops" unless we completely sure why we need both and tell "dev" to fix (do symlink in Dockerfile step).
