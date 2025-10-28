> [!abstract] Challenge Description
> > Noxellar
> ## 100
> To all Polaris Logistics Staff,
> 
> For the foreseeable future, please avoid using or operating any of the teleportation equipment. Though it initially seemed that the experimental technology was working well, recent developments have seen multiple freight containers arrive at their destinations as one large merged freighter. Until we can find a way to fix this problem and untangle this mess, please send interplanetary shipments via regular space craft.
> 
> Anybody needing packages from these containers should **rename** them correctly for their use case, otherwise, it might appear as a different package.
> 
> Thank you for your patience.
> 
> **P.S.** If anybody sees Bobert, please have him report to upper management.
> 
> The flag format is: `NexusCTF{<message>}`

Opening the `.html` file shows a page with only `_Iz_a`, which seems to be part of the flag.

Running `file` shows that it is a `Targa image data`, and on viewing the bytes of the file, I noticed the PDF remnants in there as well. This must be some sort of polyglot file.

After going through a bunch of extensions, `png`, `mp4`, `pdf`, `.zip`, we find a number of broken pieces of the flag.

---
> [!success] Flag: `NexusCTF{th1s_Iz_a_p0lygLoT_F!l3}`
