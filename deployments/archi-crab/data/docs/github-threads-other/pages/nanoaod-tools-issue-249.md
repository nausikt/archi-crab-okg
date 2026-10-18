# cms-nanoAOD/nanoAOD-tools issue #249: NanoAOD-tools output file is polluted with deleted TTrees (and can 5x inflate the size)

State: open
Opened: 2020-08-21T13:45:12Z
URL: https://github.com/cms-nanoAOD/nanoAOD-tools/issues/249

## Opening post (arizzi, 2020-08-21T13:45:12Z)

It has been reported on HN that some simple processing with nanoaod tools can inflate the file size as much as 5x: https://hypernews.cern.ch/HyperNews/CMS/get/physTools/3734.html

This has been tracked to be likely due to the usage of the output file as temporary storage for other ROOT trees and objects that are eventually deleted.

This is not visible when jobFwkReport is on (or hadd filename is specified) as a simple hadd(-nano)  removes the duplication.

More details are given in the HN thread. A possible fix is to avoid leaving the CWD to the output file after the TTree is initially cloned.

@osherson

## Comment (kdlong, 2020-11-18T15:56:52Z)

Did anyone ever try implementing the proposed solution? It would be kind of useful to have this fixed.

## Comment (IzaakWN, 2021-05-12T11:31:48Z)

Hi, can the experts have a look at this, please? I tried a some naive solutions that might help point in the right directions, but there might be need of more advanced or creative solutions.

## Changing CWD
First idea was to replace `outputFile.cd()` with `ROOT.gROOT.cd()` in line https://github.com/cms-nanoAOD/nanoAOD-tools/blob/4396652db3c63fc1375d4479a3fa2a94c18f98d4/python/postprocessing/framework/output.py#L121 to load the intermediate tree into the memory before cloning, or equivalently, using `outputTree.SetDirectory(0)` after the clone in line https://github.com/cms-nanoAOD/nanoAOD-tools/blob/4396652db3c63fc1375d4479a3fa2a94c18f98d4/python/postprocessing/framework/output.py#L130 but both cases end in the following error which seems to happen at line https://github.com/cms-nanoAOD/nanoAOD-tools/blob/4396652db3c63fc1375d4479a3fa2a94c18f98d4/python/postprocessing/framework/output.py#L175-L176
```
Error in <TBufferFile::WriteByteCount>: bytecount too large (more than 1073741822)
Error in <TBufferFile::WriteByteCount>: bytecount too large (more than 1073741822)
Error in <TBufferFile::CheckByteCount>: object of class TObjArray read too many bytes: 1109826024 instead of 36084200
TBufferFile::CheckByteCount:0: RuntimeWarning: TObjArray::Streamer() not in sync with data, fix Streamer()
Error in <TBufferFile::CheckByteCount>: Byte count probably corrupted around buffer position 36084491:
     -2146039808 for a possible maximum of 1667196141
Error in <TBufferFile::CheckByteCount>: object of class TTree read too many bytes: 1703280640 instead of 36089466
TBufferFile::CheckByteCount:0: RuntimeWarning: TTree::Streamer() not in sync with data, fix Streamer()
Error in <TObjArray::At>: index 96 out of bounds (size: 10, this: 0xe116f0)
Done ./D4B2903F-9F2A-9546-8BFC-3313C2B8B9B3_test_fix.root
```
Adding `self._file.cd()` before L175-L176 to hopefully copy the tree directly to the output file, did not solve this issue.

This test was run on a nanoAOD files from the `SingleMuon` dataset with 268408 events, and initial size 202MB.
For the tests, I made a minimal analysis module that adds one branch of the invariant mass between the two leading muons. No branch selections, no JSON, no pre-selection cut. Without any changes to the framework code, the file size increases from 202 MB input to 386 MB output, almost double.

_However_, when I specified `maxEntries=100000`, the naive fix above does work, the contents seem complete and healthy, and the file size actually about half than without the fix! Since it's half (146M → 75M, where 75 MB / 100000 * 268408 = 201 MB), it probably does mean the intermediate `TTree` is invisibly stored, as discussed in the HN thread. So the `TBufferFile` error above should be an issue with limited memory. Sadly a lot, if not most, of centrally produced nanoAOD files are even larger than this.

So there needs to be general solution other than loading the intermediate `TTree` into the memory instead of the output `TFile`. Maybe there can be a temporary `TFile`, which is deleted at the end?

The reason for this final `CopyTree` in L175-176, is actually to remove disabled branches from keep 'n drop branch selection, as discussed in https://github.com/cms-nanoAOD/nanoAOD-tools/issues/269#issuecomment-789794821. Maybe there is another way to to do this step?

## Deleting the temporary tree
In the [`TTree::CopyTree` class references](https://root.cern.ch/doc/master/classTTree.html#a2b57854ba133da5fc523931aa0427e21), it says "The returned copied tree stays connected with the original tree until the original tree is deleted." So the other naive thing I tried was to explicitly delete the previous tree after copying in line https://github.com/cms-nanoAOD/nanoAOD-tools/blob/4396652db3c63fc1375d4479a3fa2a94c18f98d4/python/postprocessing/framework/output.py#L175-L176 but this just leads to a segmentation fault at the very end, I think when the file is closed:
```
        oldtree = self._tree
        self._tree = self.tree().CopyTree('1', "",
                                          self.maxEntries if self.maxEntries else ROOT.TVirtualTreePlayer.kMaxEntries, 0)
        ... # write tree and other objects first
        oldtree.Delete()
```
I tried a different order, before, and after writing the tree and other objects. When using `del oldtree`, it does not result in a segmentation fault, but the file size does not change. In case it's important, I am using ROOT 6.14/09 in `CMSSW_10_6_13`.

To use `TFile::Delete`, one needs to specify a name, so I tried to rename the tree before deleting, which still lead to a segmentation fault at the very end (when the file is closed?), and the output file did not change size.
```
        oldtree.SetName("TMPTREE")
        self._file.Delete(oldtree.GetName())
```
I also tried renaming already just after cloning the input tree in L130, and the renaming the final output tree `Events`.

Following a [proposed solution on a thread on the ROOT forum](https://root-forum.cern.ch/t/segmentation-violation-after-copytree/17699/2) to reset the branch address before deleting the old tree did not solve the segmentation fault:
```
self._tree.ResetBranchAddresses()
```

Following [this ROOT forum thread](https://root-forum.cern.ch/t/large-tchain-into-roodataset/33559/6), I tried
```
self._tree.GetListOfFriends.Delete()
```
but it seems this list is empty: `<ROOT.TList object at 0x(nil)>`, probably because it's only used for `TChain`. :p

## Overwriting
The last idea was to specify the `kOverwrite` or `kWriteDelete` option in line
https://github.com/cms-nanoAOD/nanoAOD-tools/blob/4396652db3c63fc1375d4479a3fa2a94c18f98d4/python/postprocessing/framework/output.py#L102-L104
using
```
    def write(self):
        self._file.cd()
        self._tree.Write(self._tree.GetName(),self._tree.kOverwrite)
```
in the hopes it would completely remove the intermediate tree. But this did not seem to make a difference in the final file size...

Please let me know what you think...

## Comment (IzaakWN, 2021-05-12T12:07:53Z)

In case anyone needs a quick fix, using `hadd` does seem to remove unneeded data and reduce the file size, as discussed in the HN:
```
hadd -fk output_tmp.root output.root
mv output_tmp.root output.root
```

## Comment (arizzi, 2021-05-12T12:24:37Z)

please void hadd, use hadd-nano otherwise your trigger bits branches could be misaligned

## Comment (IzaakWN, 2021-05-12T12:41:03Z)

Thanks, @arizzi!

This also reduces the file size:
```
haddnano.py output_tmp.root output.root
mv output_tmp.root output.root
```

Enabling `fwkJobReport=True` in the postprocessor gives, besides an `FrameworkJobReport.xml` file, two output ROOT files: one large one like before, and one smaller one with the name `tree.root` and half the size.

## Comment (NJManganelli, 2021-05-13T01:09:17Z)

This makes sense, as specifying the fwkJobReport triggers the internal
haddnano.py call, running over all of the output files produced (and
defaulting to 'tree.root' for the aggregate file).

On Wed, May 12, 2021 at 2:41 PM Izaak ***@***.***> wrote:

> Thanks, @arizzi <https://github.com/arizzi>!
>
> This also reduces the file size:
>
> haddnano.py output_tmp.root output.root
> mv output_tmp.root output.root
>
> Enabling fwkJobReport=True in the postprocessor gives, besides an
> FrameworkJobReport.xml file, two output ROOT files: one large one like
> before, and one smaller one with the name tree.root and half the size.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/cms-nanoAOD/nanoAOD-tools/issues/249#issuecomment-839738563>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJDSMOTKYESISJODCHOGN4DTNJZPNANCNFSM4QHJVTLQ>
> .
>

## Comment (UBParker, 2021-11-11T17:23:15Z)

Just to follow up on this. This issue was effecting my WF which is built on your master branch but adds the functionality to run c++ modules as well as python ones. I think if you just add this line to your WF it will solve this problem : https://github.com/UBParker/nanoAOD-tools/blob/cloops/python/postprocessing/framework/output.py#L130 I also made some other changes but I think this one is the most important. I can try to put in a PR soon.

## Comment (pfs, 2023-03-09T09:42:28Z)

hello - recently me and @mseidel42 ran into the same issue. 
We tried the change of @UBParker but it didn't seem to do the trick for us.
haddnano.py does it correctly
Could eventually the option of enabling fwkJobReport to True be given to the user when running from PhysicsTools/NanoAODTools/scripts/nano_postproc.py ?
