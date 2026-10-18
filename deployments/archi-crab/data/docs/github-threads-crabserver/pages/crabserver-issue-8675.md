# dmwm/CRABServer issue #8675: get rid of  crab3/CRAB3ServerConfig

State: closed
Opened: 2024-08-30T09:45:03Z
Closed: 2025-10-03T14:14:59Z
URL: https://github.com/dmwm/CRABServer/issues/8675

## Opening post (belforte, 2024-08-30T09:45:03Z)

as discussed in Udine's workshop we will eliminate this directory and stop pulling the external config from glitlab into CRABServer
- [ ] "compatible versions" --> remove. Since now we control client distribution via CVMFS we do not have to worry about ancient clients laying around anymore
- [ ] "banned-out-destinations" --> remove. A bad idea. And we do not use it
- [ ] "htcondorPool": "cmsgwms-collector-global.cern.ch:9620,cmsgwms-collector-global.fnal.gov:9620" --> become part of TW config template in puppet
- [ ] cmsweb-shedds-config.json --> become part of TW puppet config as well. Pick each scheduler weight from a hiera variable in each scheduler VM's yaml hiera file
- [ ] "modes" --> disappear. Means that in RESTCache.py the S3 bucket name must be chosen based on the "instance" field in the URL used by the client : `https://cmsweb..../crabserver/instance/cache?subresource=.....` **I do not know how to do this yet**
- [ ] delegate-dn --> needs to stay in the server, so that CRABClient can retrieve and create proper credential. So make it part of CRABServer's `config.py` (which should be moved out of secrets) as per #8685  Since this file "never changes" we could even make it part of REST container. And if cluster-dependent minor tweaks will ever be needed, use env.vars. set via [Helm vaues files](https://github.com/dmwm/CMSKubernetes/tree/master/helm/crabserver)
- [ ] once all of that is done and verified to work, we can remove the [code](https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/CRABInterface/Utilities.py#L97) which loads external configuration in the REST  and the [files from gitlab](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/tree/master?ref_type=heads)

## Comment (belforte, 2025-10-02T12:45:37Z)

I am/will take care in the context of #9167

## Comment (belforte, 2025-10-03T14:14:59Z)

all the actions described here are tracked in #9167. Closing
