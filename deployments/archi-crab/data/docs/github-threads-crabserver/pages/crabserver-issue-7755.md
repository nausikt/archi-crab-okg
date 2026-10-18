# dmwm/CRABServer issue #7755: Adopting cmsrucio_import to CRABClient 

State: open
Opened: 2023-07-13T11:38:21Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7755

## Opening post (novicecpp, 2023-07-13T11:38:21Z)

Rahul wrote [cmsrucio_import](https://github.com/dmwm/CMSRucio/tree/master/UserDMTools/cmsrucio_import) to import user's files to Rucio. We need to decide if it worth to integrate to CRABClient.

## Comment (novicecpp, 2023-07-13T11:39:20Z)

My comments (move from meeting minutes):
- The script is pretty straightforward and requires only a rucio python client. It can easily integrate to CRABClient if we can import Rucio client in CMSSW env, or treat it as a standalone script like `crab checkdataset`.
- Concerns:
  - What does [rucio.client.uploadclient.UploadClient](https://github.com/dmwm/CMSRucio/blob/83a1cbbf48f30ce9bb85e1dcc408fd1e9c4e98d1/UserDMTools/cmsrucio_import/cmsrucio_import/main.py#L292C5-L292C55) use behind the scene for uploading files to temp_RSE?
  - How to estimate maintenance cost, especially edge cases from users.

## Comment (belforte, 2023-07-13T12:42:39Z)

> What does [rucio.client.uploadclient.UploadClient](https://github.com/dmwm/CMSRucio/blob/83a1cbbf48f30ce9bb85e1dcc408fd1e9c4e98d1/UserDMTools/cmsrucio_import/cmsrucio_import/main.py#L292C5-L292C55) use behind the scene for uploading files to temp_RSE?

I was so sure that the answer was `gfal-copy` that I was surprised you asked and had a look. It looks quite complex, what is used depends on the protocol which depends on the RSE configuration. But e.g. for `webDavb` it seems to using "plain" HTTP calls via the (external) [requests](https://requests.readthedocs.io/en/latest/) package. That may ultimately need `libcurl.so` but there\s a chance that it works inside `cmsenv`. To be tested. NOPE ! `requests` needs `urllib3`

## Comment (belforte, 2023-07-13T15:08:28Z)

shall we move this to CRABClient repo ?

## Comment (belforte, 2023-07-13T15:28:59Z)

My comments:
 * I found the python difficult to understand, but I agree that this is my shortcoming. This mostly suffers from lack of 100f-view documentation: use example, a sketch of a user manual, some explanation of those YAML files
 * Since it is a new tool, I would not mind to wrap tings with "if python3" and only use when CRBAClient runs with py3, which should fix all code compatibility issues
 * I worry about `poetry` and `wheel` stuff. README is not clear in this regard, also there's a `pip3 install -r requirements.txt` but no `requirements.txt` file in the repo. Is that part about how to build a package for pip ? Why, since you can simply do `pip`install rucio` ? What does this need to depend on besides Rucio ?
 * we have to see about binary dependencies though, and worry that even python compatibility may be transient since moving to next version will be done independently in Rucio and CMSSW.
 * anyhow a lot is about did/rse manipulations which should be pretty safe to import in our code
 * The fear is that if we do nothing but simply tell users to fetch it  and use it, answering questions and providing good examples will be more work than bit the bullet , strip off al lthat we do no undestand, and just adopt `upload_..._and_create_rule()` 
 * We should look into unifty code for dealing with RSE_Temp in here and RUCIO_Transfers

## Comment (novicecpp, 2023-07-13T17:01:11Z)

We can safely ignore poetry (and also wheel). It is just python package manager to locks dependency to specific version and hash, prevent tamper (supply chain attack). We do not need that if we integrate into crab. Well, he forgot to put `requirements.txt` or proper `pyproject.toml` @dynamic-entropy

## Comment (dynamic-entropy, 2023-07-14T07:24:57Z)

Hello Stefano, Wa, Dario
I never received feedback (for no one was using it other than myself), so I never bothered to make changes and corrections. 
My choice of poetry wasn't a wise one, from one recommendation to another, starting from typer. 
( We can change all that, we had a chat with Dario, but alas! he stopped reminding me anymore :eyes: ) 

What is the intended timeline for this? I am happy to help in whatever direction you wish/decide to go.

## Comment (belforte, 2023-07-14T12:44:49Z)

thanks @dynamic-entropy , and do no take it bad that we started to talk about this w/o you.
The aim is to make sure that we have a tool which users can use and we can support.
Turning it into a 'crab importotorucio' has some obvious appealing but before we do we need to understand the dependencies, current and possibly future one.
We have suffered enough in the past when grid tools and CMSSW migrated from on SL version to another and from one python version to another on different timelines. 
So we do not have a defined timeline for this, but I think that if we do not do it before end of the year, it is possible that we never do.

## Comment (novicecpp, 2023-07-18T10:30:43Z)

@dynamic-entropy Could you please update `requirements.txt`?

## Comment (dynamic-entropy, 2023-07-18T10:49:49Z)

Hello 
( I did not take it badly, it was a joke about Dario stopping reminding me :sweat_smile: - i should have noted that others do not have context ).
I think I need to remove typer and poetry for this, but you can use this requirement file if you want to go ahead as is, https://github.com/dmwm/CMSRucio/blob/af21943c6a53bf387155e4067fe6568938864a67/UserDMTools/requirements.txt

Cheers

## Comment (novicecpp, 2023-07-18T13:05:46Z)

Thanks Rahul. 
We are in the evaluation step and are figuring out how to migrate to CRABClient. Some information from you is indeed needed.

## Comment (belforte, 2023-07-20T10:37:31Z)

we have a chat in CRAB Meeting.
Some live notes:

* all in all it looks "little and easy" code, esp. after Rahul's clarifications
* so we decided to go for it and it has top be a "crab command". This is the only way to make users use it.
* how do we go ?
  * option 1) 
     * have a standalone script inside crabClient and executed in a forked subprocess after `scram unstenv` like for `crab checkdataset`
   * option 2)
     * integrate rucio client calls in the code but inside an `if this CMSSW version is good for Rucio` (this may help in other cases as well, e.g. checkwrite)
   * option 3)
      * add our own commands in `/cvmfs/cms.cern.ch/rucio/current/bin` ? is it possible ? does it make sense ? Need to talk to Shahzad.
   * option 4)
      * long shot (pipe dream?): revert how CRABClient works, instead of running in CMSSW env,, run in a "pip" env and fork a subprocess with scram commands for the little code which needs to parse PSet.py and communicate with rest of code via JSON files
 
* who will do this ?
    * Nobody has time until September at least. Not even to plan details and figure out how long it will take
   * **Let's revisit around September 15 ?**
 
**NOTE** especially if we go for 1), work on CRABClient side is minimal. Issue is all about understanding exactly what needs to be passed to the rucio_import script, document, validate args etc. etc. Also a whole new set of arguments different from what we already defined makes it horrible the already uglysh code in e.g. ClientMapping. Some decisions to take etc. But it looks like most work will go in understanding how exactly the import script works, which we need to do anyhow.

## Comment (belforte, 2023-11-07T22:02:49Z)

We went for option 2) in integrating CRABClient and Rucio

## Comment (belforte, 2023-11-08T08:46:54Z)

and this must be move to CRABClient repo !

## Comment (belforte, 2024-08-09T14:46:31Z)

we will go for option 2)
