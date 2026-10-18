# dmwm/CRABServer issue #7559: pycurl import error in lxplus8

State: closed
Opened: 2023-03-02T16:32:09Z
Closed: 2023-03-06T15:02:22Z
Labels: Type: Question
URL: https://github.com/dmwm/CRABServer/issues/7559

## Opening post (novicecpp, 2023-03-02T16:32:09Z)

While I tried to run crab command in in lxplus8, with newest `CMSSW_13_1_0_pre1`, I got pycurl error:
```
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.230124.00/bin/crab.py", line 22, in <module>
    import pycurl
ImportError: pycurl: libcurl link-time ssl backends (openssl) do not include compile-time ssl backend (nss)
```

It is also happen with my usual `CMSSW_12_5_0_pre5` environment for submit the hc\_1kj task.
I have tried with cleanest possible shell by run
```bash
env -i bash --norc --noprofile
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd ~/crab/cmssw/CMSSW_12_5_0_pre5/
cmsenv
```
and try to run `crab --version`, I still got the pycurl error.

It is weird because it does not happen to my local machine. @mapellidario also tried it in his lxplus8 env but did not found the error.

Does anybody know how to fix this?

## Comment (belforte, 2023-03-02T16:58:07Z)

Can you tell where pycurl is imported from? You did do cmsenv, right?sent from Stefano's mobile

## Comment (novicecpp, 2023-03-02T17:05:17Z)

From `sys.path` 
```
/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pycurl/7.44.1-6ff425e3dcd7928e6ae2367eb3a5b166/lib/python3.9/site-packages
```

## Comment (belforte, 2023-03-03T09:53:10Z)

I can not reproduce this when using your recipe.
But I do not like
```
cd ~/crab/cmssw/CMSSW_12_5_0_pre5/
```
what that a release area created on lxplus8 ? 
To be fully reproducible, you must do "from scratch", like this which I did and worked for me,
I replace some comment with words...
``` bash
#ssh lxplus8
#make sure I have K5ticket (klist) and AFS token (tokens)
voms-proxy-init -voms cms
env -i bash --norc --noprofile
cd /tmp/belforte
cmsrel CMSSW_12_5_0_pre5 # odd that it prints nothing
cd CMSSW_12_5_0_pre5
cmsenv
which cmsRun  # just to confirm that cmsenv did its job
crab --version
crab status
```
and I get
```text
bash-4.4$ which cmsRun  
/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/cmssw/CMSSW_12_5_0_pre5/bin/el8_amd64_gcc10/cmsRun
bash-4.4$ crab --version
CRAB client v3.230124
bash-4.4$ crab status   
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20230302_092240
Task name:			230302_082244:belforte_crab_20230302_092240
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITTED

```

## Comment (novicecpp, 2023-03-06T15:02:22Z)

I finally found the root cause, thanks to Stefano previous comment.
It is because python load the broken pycurl package installed in my local path `~/.local/lib/python3.9/site-packages`. When printing content [1] of `sys.path`, my local path is there and has higher precedence than pycurl from cvmfs.  

I do not know if I can/should make the package from cvmfs higher than my local path. I have no idea how `sys.path` is initialized. For now, removing broken pycurl from my local path solves this issue.

<details>
<summary>[1] sys.path</summary>

```
['',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/python3/3.9.6-67e5cf5b4952101922f1d4c8474baa39/lib/python39.zip',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/python3/3.9.6-67e5cf5b4952101922f1d4c8474baa39/lib/python3.9',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/python3/3.9.6-67e5cf5b4952101922f1d4c8474baa39/lib/python3.9/lib-dynload',
 '/afs/cern.ch/user/t/tseethon/.local/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/python3/3.9.6-67e5cf5b4952101922f1d4c8474baa39/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/share/overrides/python',
 '/afs/cern.ch/user/t/tseethon/crab/cmssw/CMSSW_12_5_4/python',
 '/afs/cern.ch/user/t/tseethon/crab/cmssw/CMSSW_12_5_4/lib/el8_amd64_gcc10',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/cmssw/CMSSW_12_5_4/python',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/cmssw/CMSSW_12_5_4/lib/el8_amd64_gcc10',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/coral/CORAL_2_3_21-33dc9fef33ce0f2d7a0bc34e2361296a/el8_amd64_gcc10/python',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/coral/CORAL_2_3_21-33dc9fef33ce0f2d7a0bc34e2361296a/el8_amd64_gcc10/lib',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/cmssw-tool-conf/52.0-12aaa9dfaca14c1a587fb4b8dca38ad1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tensorflow/2.6.4-a58261bd2b56f6b3c18b1f044170a9e0/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-hepdata-lib/0.8.1-1544ac7a5d4c09e906662bc2c1d1b856/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ipywidgets/7.7.0-6b0bbd3b46ad49b5c10899e9318c2f7e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-lz4/3.1.3-fec17685678379e238ab8da390b03237/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-avro/1.11.0-2dadd35b3fb46a982c4a4af03483ef37/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyter-console/6.4.3-a37cc936e7c503de28d26ab924a07c6a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/professor2/2.3.3-a2d21ea75bb2525950e27c575e223cba/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-onnxmltools/1.9.1-7a668a3519cdaaeabea08f6332fd649a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mplhep/0.3.12-2e2fe297f38cf393672b67940dde018f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-hep_ml/0.6.2-e56e77f0ce22970759382559895e9497/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-seaborn/0.11.2-5501538367a45f91da6cbf6fb28a0984/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pycuda/2021.1-4831c914d6e8c4ac0210a01e84992795/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-correctionlib/2.1.0-6c8331f01a9ae0b1fdbbc4a2ac480990/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-flake8/3.9.2-30e00842c0513186c09a65e89778a9e5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-virtualenvwrapper/4.8.4-35b02927e6b4ac0730abb1b6e435e4d6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-uproot/4.2.2-a9ef1e95a958f1a431a28ff610b6f079/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/onnxruntime/1.10.0-1b13113c7f40c5a1c74def407c33c42b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tables/3.6.1-de2eff61058b6ece3c9eb326c8eb2f32/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-law/0.1.5-8b4a146bd6c39222c5e473ce4c2752c9/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jsonpickle/2.0.0-d0a4ad152d11041160b4299831f7cec0/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pygithub/1.55-2047aa95b43806cb772c60a569167d78/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-downhill/0.4.0-f62b018419cb083a48984e5486ec0b81/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-anyio/3.3.2-c8568591dab4009a36cac211db9697f0/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-xgboost/1.3.3-db256ced50f5439f484836d6324a2182/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/opencv/4.5.5-6df492b6406f0de9f458ea99f7d5e036/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-numba/0.54.0-164d05ce0b114bcb58b260ec2911738e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-vector/0.8.4-0bdf3ceac8c9c21e12575c26365bf4bf/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-grpcio-tools/1.39.0-d6a548b627075dda0ef4aa04a0090161/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-dxr/1.0.x-6d16ab0cb47f4350c4c6aaf2c7a818a1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/mxnet-predict/1.6.0-a0e2c980f9e4e5bf97bb3c0cbdce3b7c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-histogrammar/1.0.25-f12aa4707676818c74c8c21eb23dd225/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-uncertainties/3.1.6-007dcbabca2e5823722d7e77dcc944ab/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-python-ldap/3.4.0-4ae2591516bf24e58ee5a5ae68e94eb6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-histbook/1.2.5-8ddf8b525acccf675f4a4658c4f406cb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-GitPython/3.1.18-43f8aa2387b16ec42e76a0e8218b94a1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Bottleneck/1.3.2-ca5cbfa5e1432eb8dfb607a76792241f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-lxml/4.9.1-3ef391a7eea0b5fe440641fbfc32b8f4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-autopep8/1.5.7-bf2c29f112a0ca62a43c4cc08e9bfbd4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-sympy/1.8-171a4194ea4e9da489c10e7d0f23e6b1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-schema/0.7.4-10ffe82214d78047a318d162a6f2d545/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pydot/1.4.2-e964172c2edfc8ed40f518ad484034d2/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pycurl/7.44.1-6ff425e3dcd7928e6ae2367eb3a5b166/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-prettytable/3.2.0-a4c02ead8a25950e3562138d65d95c09/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-networkx/2.7.1-796c944fdec92fabd0e90220fe063605/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cmsml/0.1.2-6cf48846fba5404e749251e4b3b75b10/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-beautifulsoup4/4.10.0-d923fe7431308e8859f6c4db2cafac45/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-subprocess32/3.5.4-b39f04b70fe6cc39c4716c9705414d00/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-sqlalchemy/1.3.24-4819e3e38ad0f7c1ee60ed3ebad25ba5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-psutil/5.8.0-51b124dc2b264c5ba1e439051da06a9b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-prwlock/0.4.1-bcdae4fe08a06b9d2aac833edb07e79f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-plac/1.3.5-9452f42e68c649e2b965d271c1d0ec5c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-lizard/1.17.9-91a8e19cfab93a76cf52f8f3b20f59cf/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-flawfinder/2.0.19-2eeafa6d73a41862892c89cf63fae246/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-docopt/0.6.2-78f841d11c56b73006917423b468db61/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cx-Oracle/8.2.1-68cc17936a3dd5fedca3108cc0142759/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-asn1crypto/1.4.0-c4c07b7f9fe9502cbdbf51790c56b087/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-keras/2.6.0-959405eae18db53046ef0be40cfce34c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-widgetsnbextension/3.5.1-0aac3075f3708bee22b756e3109acb1f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pylint/2.13.5-3cfcedf15c4ee512caec9563e27a4546/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-rich/10.9.0-a4ae5c050b1482ca38d3c20317dddce2/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-skl2onnx/1.9.2-1d00a42e43acb5e861f7e11524c164d5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tensorboard/2.6.0-2d866e959637411e19e71c4d90b1e0ed/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/rivet/3.1.6-9dcebff19409ad8d5ff6552b62bd912e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-keras2onnx/1.7.0-5f6ceeecb150a475eb9ced68b1ce1dea/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytest-cov/2.12.1-83109d8fe18eed641296ef1d88895c87/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-awkward/1.8.0-907677752cd2d8daaf4d3bb44ebd6e00/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-luigi/3.0.3-3c91202016243ce078efe3a55e4a1a9b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-hist/2.4.0-090663227bdffe94dfe2dc3f61823deb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyterlab-widgets/1.1.0-331c493816ab48229bda7c32989a09f4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-numexpr/2.8.1-b11f3370020e80c23ae702edffc37586/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytools/2021.2.8-e08abe2965e8f95efc0d65e1653cb63a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-scinum/1.2.0-39a8cfcd46e95a4e3536d958fd547049/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-stevedore/3.4.0-aa9b7e87ad7e1f4646c79c361618ce0d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-llvmlite/0.37.0-036b29b5d50eae70f2c82e7757f952fc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-PyNaCl/1.5.0-067f5bb233ab63c5d824ead9768b0142/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pydantic/1.8.2-f2fdc6196f8cb688f95349774db8e36c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-parsimonious/0.8.1-cd01b3fee12a58130547f52591ac1e1d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-google-pasta/0.2.0-b58c810bc1c039da9c8b43d7681cc101/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-gitdb/4.0.7-827971de0bc6cf6b1915025d79dca12f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-deprecated/1.2.13-a56a00d3be407adbf12e1537d874b0f8/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-astunparse/1.6.3-0d876727d36aaedd663510f82c97f125/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Mako/1.1.5-a7a3013aee7d9537b91d164a7116347d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-virtualenv-clone/0.5.6-6c6cb8b6d3c853694f9764f61e120678/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tqdm/4.62.2-e203a42b5cad90a84dc0a69793da4320/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tensorflow-estimator/2.6.0-1a0f13460af0560a11cd4d551f24d793/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-soupsieve/2.2.1-9e5c607d7b84d2d0b21ac43dbbc2520d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-sniffio/1.2.0-810710fb0594866286583d56dea4ef64/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-python-rapidjson/1.4-caccad438a40227407962812ad34c325/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pysqlite3/0.4.6-ccf9cac7012bbff6122bb6c7b9ad5a4e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyflakes/2.3.1-6319c30b072fac95f1d1d70f860d611b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mpmath/1.2.1-a03c8695676005dd4b6808e7b8c935bb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mplhep-data/0.0.3-dabfeb3490e40fdf7dd965e85a74cdaa/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-PyJWT/2.4.0-c67fcb4e49780e4047ff6127402452cf/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-notebook/6.4.12-7c1917f4f0b609d3fa5c49b69ae2d73b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-google-auth-oauthlib/0.4.6-8ea6461b68c0e24db1089ffadb8039d3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-astroid/2.11.2-be033d359dc2ed3a9cef9afcdcaddf08/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-histoprint/2.2.0-442afcd56b25d9fbdf1cd94ae65c4c4b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-boost-histogram/1.1.0-e224319aabd7274a00be0a0c6cd6913f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-python-daemon/2.3.0-84c61c4ea9bac2e9e5861979d6c85ea9/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-fire/0.4.0-10fc91243a9984623c926ed0909748dc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tensorboard-plugin-wit/1.8.0-b6b4f3f808bcd208461254311d06a5fd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tensorboard-data-server/0.6.1-40c5b960a60ca2b196056b26e8b08a59/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tenacity/8.0.1-3db77557cf131b9a1ce6a368234f7217/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-smmap/4.0.0-0b29c871990c1b6253b516b0b10d31f4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-dill/0.3.4-9374e04354b264594b2401c795b6a0b2/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-coverage/5.5-2be27e2d19b87c80953fbaa861dbcbf1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-commonmark/0.9.1-4d6a6dae77fd1a2dca420cd2322d93e1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-colorama/0.4.4-7cb8d5dde4ae958d5bdd8419170b1fbe/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Werkzeug/2.0.1-370e538703953cd77d1b9e1dcb77acc7/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Markdown/3.3.4-a89df5d31e97f06ee3fc6ecd132eb027/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/frontier_client/2.9.1-9489e6c7ac02a80a06fbda307e9617b7/python/lib',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-isort/5.9.3-a7b2f85505eaa13c4616bdaf55cd1ff0/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-nbconvert/6.1.0-790d6642287158c4c1fc612f670522e5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-scikit-learn/0.24.2-fefa36ce80c3666b59737b7c27836b60/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-matplotlib/3.4.3-99f2fe0236aea081d0e1c8cbf5454a87/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytest/6.2.5-8a2bef13cc282c15f7691d326cbd3e75/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-onnxconverter-common/1.8.1-9a603295f741047c9518a786a3e43ac6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-terminado/0.11.1-8b6e582cdf8737a6160a043666fc74ea/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pandas/1.2.2-d8c515bb21304d75847355325863868d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mccabe/0.6.1-abd854a8a4a78d7903acbfe8dca520d9/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-lazy-object-proxy/1.6.0-4409d94995f1dd2d45402051b2c41abb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-requests-oauthlib/1.3.0-f3ec7d2b25a032e515277d7a2cff92aa/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyter-packaging/0.10.4-659f227b35bdac2c4ebb367784ad046d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-google-auth/2.0.2-7dc0fd09bad0b17cdc6d6aacded0a079/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-opt-einsum/3.3.0-7a26d85100dab9f9cd522986f901a572/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-argon2-cffi/21.1.0-26ae3f5a4062f48a5b0130c4ba186bb3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-grpcio/1.39.0-a0bc60873e832f60dd05b2b3632b49a4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-typed-ast/1.4.3-343f5eb71ee120c5d4223dec2623232c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pycodestyle/2.7.0-9a65f9158d5c11597ec3ad9b2180a614/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-prometheus-client/0.11.0-b4a2430a21a40c7e5f624145cd8fb383/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-lockfile/0.12.2-2972a89d88c75d1d5abb6476e1730856/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ipaddress/1.0.23-25326714b22305db176cbb350156036b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-flatbuffers/2.0-9d2ee65d49ad28016fea55ff22bb03b3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-astor/0.8.1-3ba8736ae2e4da2bbe9e9fae69cde4c7/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Send2Trash/1.8.0-7a2d1db5f97e49082520ee2f40f114fb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-keras-applications/1.0.8-1dba8dc60c61e53b9dc93347c104f9fc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-uhi/0.3.0-6d0555da463f2a46f1648e1c090e5469/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ipykernel/6.3.1-b7dff4bdb530668c3e4c1a83f6cc4a91/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-nbclient/0.5.4-1cf7faf08675b2cefacec21dbd675396/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/yoda/1.9.6-dd24b58f7800076b18ccf4d4e5e1b378/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pluggy/1.0.0-da21f28081c6e4b0b3b8f74498bb767b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-threadpoolctl/2.2.0-03863d43306863662a365d5076a7de70/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-testpath/0.5.0-d2fa7f82a5780e2d50dd0f7e3f806c46/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Theano/1.0.5-a4f2c7f7355d73369a2b8120d7502c58/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-py/1.10.0-df0caeab89cfa20f7fe7c606c6bc724c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-keras-preprocessing/1.1.2-932b5a691e5db6130e29b203d1cd8048/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-deprecation/2.1.0-5c17f031bb834ce6c205c060a9c72580/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mock/4.0.3-db4696779fb0bf431ed5a94277e15450/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pillow/9.0.1-f35da86662901292cc61880605776c97/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-rsa/4.7.2-b3e3c5dfaf935851c6737fbfd7b814c7/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyterlab-pygments/0.1.2-bf51db90d80e087b4ddf10f08ad281a4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cycler/0.10.0-64e3e7d0477b5acec5002ed053657c4f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-absl-py/0.13.0-173b101e66b025d0c6ee53e9242a9474/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytz/2021.1-69ecb35e495b60f9db2bbd79ddd72cfa/lib/python3.9/site-packages',']
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pandocfilters/1.4.3-7dfee5d74608fef1d479b895207c92d4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-oauthlib/3.1.1-1129ea29bf41e58ebcb0a74af8aa3a51/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-mistune/0.8.4-ce799e7173ee15c06f53eeeefc4e2a1e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-kiwisolver/1.3.2-0ba78790c0c05085316076de0bdc613d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-iniconfig/1.1.1-b89975a7cdc7a6e3626b3896c5209d17/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-fonttools/4.31.2-dd2d8ef2d8158f32922baaaa98e1ff69/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-defusedxml/0.7.1-435fa2c4a4353f247856a241dd2e97fd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cachetools/4.2.2-cd4a6bf71ddf26cec013af06b6d9c14a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-atomicwrites/1.4.0-a87ca2601423d39ee2c3f9012913724e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Click/8.0.1-797c45063de70caf70024739e1c08b5c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-h5py/3.4.0-9f3dd0f243b82b5af74f0c6b595aff39/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-nbformat/5.1.3-f74fbead3cad38b95ea0d9fff697d041/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ipython/7.31.1-710ff00df81608ebcce7d258e939718e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-onnx/1.10.1-fe8ebbaadda097142d4f6842913cc786/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyasn1-modules/0.2.8-bb94275dce34ff9e1365412bb2d39bc4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-joblib/1.0.1-3b6b1f1f26b56a171bc7349f433daaee/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-debugpy/1.5.1-a56a79a9bf95190470c1f4df2aa10c5d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-PyYAML/5.4.1-98ff589ed9b6764b962e5a257170acea/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jsonschema/3.2.0-2af04185f34ae03ad30e7e05769c7d75/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-bleach/4.1.0-be8eb1ccefaf235015983f11b916891e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-matplotlib-inline/0.1.2-4dba56f76634676eb19fc21ec1f9dbc7/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pickleshare/0.7.5-3bc216668a45079ecbfbf9c43cb32733/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-backcall/0.2.0-829267e62a92bbff57cb623a12294957/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-prompt_toolkit/3.0.29-4c519427ba87cad7a17851af240543a8/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jedi/0.18.0-9de70d4baa588d3084243bfc33fe4566/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-termcolor/1.1.0-d5eaae0ab1f713eed3ef623a64b6966a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-simplegeneric/0.8.1-6ba5e7584fa80c9259b3220204487e35/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-future/0.18.2-00b85a0b20be9bceb1f3c764864920ab/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/fastjet/3.4.0-52e3efb0f7d6dc14f7751010817f56a5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pkgconfig/1.5.5-83ce8dfef47d4758e3187335ef96046a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyter-client/7.0.2-b574d1e42fc26f42a77c9e4b1c845c40/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/llvm/12.0.1-dd4c586a5bebc335346bb0e879f6f0aa/lib64/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyrsistent/0.18.0-f44ddf7fb8cd7e17e63002aa09546cdb/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-repoze-lru/0.7-3ea0d6ac7e844b4b757263cf1c11a9c4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyasn1/0.4.8-cdd981b4d4ebd3d7a1156dfc3b542c7f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pbr/5.6.0-893b6cb15ee5c803b1d432fe8e791396/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-parso/0.8.2-34a87effa91a358a902e1a285e79fc94/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-argparse/1.4.0-3d94d336ad8fbb9b43569011f45e15e5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyzmq/22.2.1-92d80f478a003bc232d319c482056216/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Jinja2/3.0.1-740647b8d9ed36f687d8c7a4e0d48fc4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-wrapt/1.12.1-e8fa0a1598b53c2e7ed6555e04f50ff1/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-nest-asyncio/1.5.1-4ed446dbbcde7c779cb5be45c38e7eff/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-entrypoints/0.3-b145874fd9087b2448c637f7cdb8e518/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jupyter-core/4.7.1-0584defeffc5946c521fbeb4478b52f6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-funcsigs/1.0.2-2633de66441f6277775f7148aff99c10/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-scipy/1.7.1-0a92721d2bd5dbe7231e19d58903fddd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-protobuf/3.17.3-dde485549e85f322bad1b89704297340/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tornado/6.1-b11eb4a6f176b7afd9cf490c2e2f029c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-Pygments/2.10.0-40bbed48a4bea8f918d3cb0f63b27de3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-MarkupSafe/2.0.1-435fe75695f45e064d7124780349ff05/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pythran/0.9.12.post1-bb7e395cb3953267bdee260c839cf6b3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-traitlets/5.1.0-b740bee7014e47fcc9203fb7698ed61c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-wcwidth/0.2.5-ece1859ada2a11b1e626031025985a67/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytest-runner/5.3.1-df310487c01046278a56553132733d42/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-beniget/0.4.1-e11c6956c1a81400a003350686847a99/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ply/3.11-522f5ede0174392308bac2d5de670f67/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ipython_genutils/0.2.0-e17d550c24044a0ee69541059d607e2a/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-poetry/1.1.13-1ee4e7bbd4dff5a6b3edc1c906119242/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/lcg/root/6.24.07-a31cbfc28a0c92b3c007615905b5b9b2/lib',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-keyring/23.1.0-b5348e6ec80644c7dddb6ee7948b5200/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cachecontrol/0.12.6-1a23469417f1047791125878238ed2c6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-requests-toolbelt/0.9.1-a435fa500395d3ada5e0d89fa4a1bd96/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cleo/0.8.1-4b2c1c9f441b2d1fcd010fb94fe6f094/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-shellingham/1.4.0-d16f9dada50b62ab7bd9ceba4bde41e5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pkginfo/1.7.1-e8cf365663203a45ed0a74c7c09680e5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cachy/0.3.0-d4df270eee715ec95beefc48c6677755/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-virtualenv/20.7.2-127138b093950863df47e5d667f5cc28/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-secretstorage/3.3.1-3a0e442dfe2b3db65484f36964d10d11/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/xrootd/5.4.2-01e2f30cb29f5ae6cc44ce693b2a4809/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-clikit/0.6.2-b9318c6ebe0618c121ede77f126fcc17/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-msgpack/1.0.3-8d9a1973a940171c725075ac0706675f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-gast/0.5.2-47f8f540acaaccefde5d27e3c0cfdb33/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-decorator/5.0.9-90ae497be60c3679c177bb1a78ab1acd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cryptography/37.0.2-50cf26b71a5d0d35037848f950b5027c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-importlib-resources/5.2.2-3397cfdbcdc2cd8a7f7e872e84453620/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-flit/3.3.0-50b3abf79de5a707f12ea0589700e2ec/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-jeepney/0.7.1-934c1bf476d96a54c57a21ff29e989c8/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pastel/0.2.1-99390eb13ac78ac7764fff6580152bfd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-crashtest/0.3.1-afa572db4d5547d3cb3bc3bac69b168b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pylev/1.4.0-f43c503c3dfd6b0600e003d119de739b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-platformdirs/2.3.0-1b00301da820ec097e2625bb0cd1fc44/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-filelock/3.0.12-59336aab465543ddb9b6abbd55c59544/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-distlib/0.3.2-43eaa9b0a5007a9ea7d2ce68897fa987/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-backports-entry-points-selectable/1.1.0-58b8146fe5d8fae3645e5217901a2f16/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-setuptools-rust/1.1.2-d41e74130d0b770ececc75916fca635e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pybind11/2.7.1-59ab2349ababbdc8fa342a6ed28ceab5/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tomlkit/0.7.2-2586417322a2f9dc762b0d06bf8574d4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-semantic-version/2.8.5-b6c9a0c83e7008271ba87662c1f48ef3/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-python-dateutil/2.8.2-c271f4b3490fe7676c6682721eeee253/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-html5lib/1.1-bf35b0c48b762314ed6a01eb7e239749/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pexpect/4.8.0-82d1edf79fa23d2bd81a96f4521f5367/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-docutils/0.17.1-35476a9f231786ec18099059c09fdecc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-webencodings/0.5.1-e7ab55c6f5a93d6add2f41508205285b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-ptyprocess/0.7.0-6ae25831f609ae25a29aff4177ce06b8/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cffi/1.14.6-0fc7cc77aa42fd825e499de67b2cfa76/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-poetry-core/1.0.8-56829dced8e241185a9eb28ecf4b2bd8/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pycparser/2.20-fa2c260aa23cba87ef739b8c596c6ccd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-typing-extensions/3.10.0.2-4c5bef600e6e129309f21ad3da9f3fdc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-importlib-metadata/4.8.1-3e11d50e8831c732da3ba68e1a494e35/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-singledispatch/3.7.0-89d70a37b04c05b42558ea176ef31f14/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-zipp/3.6.0-9b7b6f54020ed77f96883414a351c9dc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-more-itertools/8.12.0-c74752719ec065dec5fb4bc9f2881aae/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-appdirs/1.4.4-83e3ffb2aa51cf2d1b2900180f369347/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-contextlib2/21.6.0-6ec5d6a27df5a6e64b8d82ae7439ef8e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pathlib2/2.3.6-532f20b61c2c02c4e11de2db008ac0a4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-scandir/1.10.0-a9b7b033ac6ff4fd0fc2aea8cba9669c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-requests/2.27.1-66e491f89532d25d415756449016892b/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-urllib3/1.26.6-504ee060441080cce4ff715292ff47ca/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pysocks/1.7.1-dcccf4c6462683253dfe4a7b4fdafa0e/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-charset-normalizer/2.0.4-78e63438bcbbb718ab24e629829b2f71/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-chardet/4.0.0-2f0ee657cc78a7beb2010ed4015adca9/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-idna/3.2-604a01ff03456be9f9d7c48e50017491/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-certifi/2021.5.30-d9308bdf034b40515f2b7fa0df2374ae/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-numpy/1.22.4-fed14fba556da687b0d60c63c90ca3bc/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-cython/0.29.30-ba0cbe453cd083d1585283903538da9f/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-setuptools-scm/6.3.1-2dfd0b28c0db0a2187982630c40a2819/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-tomli/1.2.1-0b793bddb7a6d66f107981564653fed4/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-packaging/21.0-4527e873b4d660579d0627448f68cacd/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-flit-core/3.3.0-a5724f1589a37183823e5990a1d913c6/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pytoml/0.1.21-324df27d623bcabf47f446202cc69a81/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-attrs/21.2.0-17cf9a2348413e028091af1d6bff2f4c/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-toml/0.10.2-de85e0710fb2f6ea7fabc145ec2d7092/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pyparsing/2.4.7-50df6d1b50368b774b125d1a5005de2d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-six/1.16.0-191eaed0649a04458bb2775b1b0a08ae/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-wheel/0.37.0-a284b6ae7bfa3cffd7ce92bff72e951d/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-pip/22.0.4-84448601ef6fb03288e044db5008fd92/lib/python3.9/site-packages',
 '/cvmfs/cms.cern.ch/el8_amd64_gcc10/external/py3-setuptools/60.9.3-ddcab3b6a742c72fed5554de8ccaaf18/lib/python3.9/site-packages']
 ```
</details>

## Comment (belforte, 2023-03-06T15:23:27Z)

maybe `pip3 install pycurl` will do ? See https://github.com/dmwm/DBSClient

## Comment (novicecpp, 2023-03-06T15:29:19Z)

That is the main reason why I have broken pycurl :)
I never manage to install pycurl successfully in lxplus8 and my local machine. I use `dmwm-base` docker image as workaround for now.

## Comment (belforte, 2023-03-06T15:45:26Z)

hmm... I have a working pycurl in ./local of my laptop. But I suspect that mixing CMSSW in the env. brings all sort of problems.  Indeed compile-time vs. link-time problems is exactly what you get when using python wrapper binary from one place and the wrapped binary from another. On lxplus* I only get SSL via CMSSW, i.e. my curl/pycurl does not have SSL support unless/until I do cmsenv.
