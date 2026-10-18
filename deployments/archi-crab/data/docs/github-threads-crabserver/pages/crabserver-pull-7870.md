# dmwm/CRABServer pull request #7870: Including -stable suffix to crabserver images

State: closed
Opened: 2023-09-12T13:24:26Z
Closed: 2023-09-13T10:30:56Z
URL: https://github.com/dmwm/CRABServer/pull/7870

## Opening post (novicecpp, 2023-09-12T13:24:26Z)

I got a request from @arooshap to add `-stable` suffix to the crabserver image tag to comply with the new retention policy of cmsweb's space.
(Aroosha, please correct me if I am misunderstanding.) The new retention policy guarantees keeping the latest 3 tags, and older tags **without getting pulled** longer than 30 days will get deleted.

## Comment (belforte, 2023-09-12T13:28:16Z)

yeah.. it is not clear to me what the point is. If everybody marks their images as `-stable` it would be easier to simply change the policy like e.g. you did for CRAB repository on registry.cern.ch

Also we surely have nothing against deleting images which were not pulled in one month, not even to test them !

## Comment (novicecpp, 2023-09-12T13:40:59Z)

> Also we surely have nothing against deleting images which were not pulled in one month, not even to test them !

The case is some legacy software running on a production VM that gets updated once a year.
It also happened to us once early this year, IIRC. Fortunately, we did not need it or rebuild it.

## Comment (belforte, 2023-09-12T13:46:10Z)

hmmm I must have misunderstood the policy. 
I thought: delete after 30 days images which were never pulled, not images which were not pulled in last 30 days !
Indeed we'd like to retain running images as long as we use them.

## Comment (arooshap, 2023-09-12T13:46:36Z)

@novicecpp Thanks for making the changes.

@belforte The reason why we are enforcing this is because we want to ensure that despite the deletion policies, the images that are critical to us, and are deployed in production, remain available. To give you an example, the current image that is deployed in the production cluster for crabserver no longer exists in registry.cern.ch. So, if something happens and the service restarts in the production, it will lead to the `ImagePullBack` error, and thus, compromise the availability of the service.
Secondly, any image that is marked with this particular suffix is immutable because of the immutability rules that we have set up in the registry.

## Comment (arooshap, 2023-09-12T13:48:03Z)

Also please free to participate in the discussion that we are having regarding this issue at https://its.cern.ch/jira/browse/CMSKUBERNETES-241.

## Comment (belforte, 2023-09-12T13:52:38Z)

thanks @arooshap  I second Valentin's comment that screenshots are hard to read and those rules a bit hard to understand anyhow. I also suggest to do like Wa has done, to keep last N tags forever. Having only time-based expiration may not do what we want.

## Comment (belforte, 2023-09-12T14:26:55Z)

I have added a couple line to the JIRA: https://its.cern.ch/jira/browse/CMSKUBERNETES-241?focusedId=4935495&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-4935495

@novicecpp , I suspect that we do not want to tag all builds as `-stable` and have production image replaced via a bunch of test builds. Note that even if we do not use it we e.g. create a new crabserver image everytime we build in order to get a  nee TW or Publisher. Maybe we need a new Jenkins project to declare a tag as stable. 
Yeah... a bit too much work for my taste, maybe limp along with a script to be run by hand on lxplus ?

## Comment (arooshap, 2023-09-12T14:50:41Z)

@belforte another option might be to just make sure that whenever you're deploying in production, you also tag it with stable? From our side, we have changed the deploy-srv script to make sure that if you are deploying an image in the production cluster, it has a stable suffix in its name, otherwise, it issues an error.

## Comment (belforte, 2023-09-12T14:55:52Z)

@arooshap yes, that's same as I was saying, implementation details aside :-)  Sort of wrap deploy-srv with something that marks the image as stable. A script of ours, a script of yours, an option to deploy-srv, an action that we do via Jenkins (we use Jenkins to build images, we can have an option in the build). Of course the flow should be build-test-markAsStable-deployInProd.

## Comment (amaltaro, 2023-09-12T15:10:15Z)

> From our side, we have changed the deploy-srv script to make sure that if you are deploying an image in the production cluster, it has a stable suffix in its name, otherwise, it issues an error.

@arooshap has this been announced anywhere? Since we migrated to CMS Talk, I failed to properly follow things up(!)

## Comment (arooshap, 2023-09-13T07:29:05Z)

> > From our side, we have changed the deploy-srv script to make sure that if you are deploying an image in the production cluster, it has a stable suffix in its name, otherwise, it issues an error.
> 
> @arooshap has this been announced anywhere? Since we migrated to CMS Talk, I failed to properly follow things up(!)

@amaltaro Here is the ticket where Valentin requested to do that: https://its.cern.ch/jira/browse/CMSKUBERNETES-237. For the services running in the production cluster, including the dmwm namespace, I have already tagged the images with the stable suffix and redeployed them with the stable variant.

## Comment (novicecpp, 2023-09-13T10:30:56Z)

Thanks everyone for comments in this PR.

I am closing this PR because we do not want to have every release tag become stable tag.
Next step I will write doc on how to tag it manually and figure it out how to put it in Jenkins later.
