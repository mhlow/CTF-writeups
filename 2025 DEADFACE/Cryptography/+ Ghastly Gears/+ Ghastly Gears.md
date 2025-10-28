> [!abstract] Challenge Description
> > @syyntax
> ## 10 
> We intercepted this internal communcation between DEADFACE members, but all of our attempts to decipher the message have failed. Use your skills in cryptanalysis to decipher the hidden message.
> 
> Submit the flag as `deadface{flag-text}`.
> 
> ```
> ‌Fsqp: rhurk415
> Ie: ljjkhwaoj
> Vygplkc: dr: rrudok ld tig hwuw
> 
> ---
> 
> ne,
> 
> ajp rge hlpjy nayx gvt dakljn zdfpth nz enxe qoga. rip tcqe tlkmz ikyff hwu exnvzxrz—jv’w gst ceuyz yeltwo.
> 
> zltq, kubvm dazsixzfz rafpc jp xmk vxdpe.hmj. fcbdq ae c oje wa amfgexisly?
> 
> "mou dpq npxcee vpkel nca nzsu — xutm vpmis jisbfn fl hfz: ikhloknq{uw0jll_i3s3q_e1h}"
> 
> vxd ehft zx co’p hmqquxfta, lff mdk cgir emv ujhc rvdn etrwg ujtgvpfa cscs.
> 
> wqwq yr xv qho bflc nqui.
> ```
> 

It's giving vigenere.
Email format, gives us a clue.
Brute forcing `Dear: lamia415, Cc: ..., Subject:`
Shows some promising signs, namely `coqyghijkglmcxxxxxxxxxdefghijkxxx`
showing that there is an alphabet hidden in here, as well as repetition.

Lots of dead ends, from here, trying to write a python script to continue over special characters as if they counted.

Eventually I looked at the flag.
`ikhloknq{uw0jll_i3s3q_e1h}`
I tried to brute force it from here. Seeing that the key started with `fghijklm`, continuing out from here, replacing all the special characters in the flag with a dummy, so [Cyberchef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('fghijklmnopqrstuvwxyzabcde')&input=aWtobG9rbnF4dXd6amxseml6c3pxemV6aHgKaWtobG9rbnF7dXcwamxsX2kzczNxX2UxaH0) could "parse" it, gives the flag (*squinting through the dummies*).


---
> [!success] Flag: `deadface{gh0sts_n3v3r_d1e}`
